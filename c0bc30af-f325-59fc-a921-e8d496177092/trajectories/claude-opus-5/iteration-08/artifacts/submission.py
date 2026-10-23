"""Self-tuning trainer: Nesterov SGD under a wall-clock-anchored one-cycle schedule.

The algorithm carries no workload knowledge and no constant that depends on the model it
is handed. It measures the time the runner charges to training from inside the update
function itself, and shapes the learning rate against that clock rather than against a
step count, so the same bytes anneal at the same wall-clock position on fast and slow
hardware alike.

A cycle warms up, cosine-anneals to a near-zero rate, then holds there until the runner's
next evaluation row has been observed, so every evaluated model is a fully annealed one.
If that row is not good enough, the next cycle restarts with a slightly lower peak and a
longer horizon, so a harder architecture or a slower device qualifies at a later
evaluation instead of never qualifying at all.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Tuple

import torch
from torch import nn

from algoperf import spec

_BATCH_SIZE = 64
_REFERENCE_BATCH_SIZE = 128.0
_PEAK_LR_AT_REFERENCE = 0.4
_INITIAL_LR_FRACTION = 0.05
_FINAL_LR_FRACTION = 0.002
_WARMUP_FRACTION = 0.15
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1
_FIRST_CYCLE_SEC = 22.5
_RESTART_CYCLE_SEC = 25.0
_CYCLE_GROWTH = 2.0
_PEAK_DECAY = 0.85
_MIN_PEAK_FRACTION = 0.3
_CLIP_EMA_DECAY = 0.99
_CLIP_FACTOR = 2.0
_CLIP_WARMUP_STEPS = 20
_UNCHARGED_INTERVAL_SEC = 0.05


def _peak_learning_rate() -> float:
  """Scale the reference peak rate linearly to the batch size actually used."""
  return _PEAK_LR_AT_REFERENCE * (_BATCH_SIZE / _REFERENCE_BATCH_SIZE)


def _parameter_groups(model: Any) -> List[Dict[str, Any]]:
  """Decay the weights of linear and convolutional layers and nothing else.

  Selection is by layer type, a generic property of any network, never by parameter
  name, shape or count.
  """
  decayed = []
  decayed_ids = set()
  for module in model.modules():
    if isinstance(module, (nn.Linear, nn.Conv1d, nn.Conv2d, nn.Conv3d)):
      weight = getattr(module, 'weight', None)
      if weight is not None and weight.requires_grad and id(weight) not in decayed_ids:
        decayed.append(weight)
        decayed_ids.add(id(weight))
  undecayed = [
    p for p in model.parameters() if p.requires_grad and id(p) not in decayed_ids
  ]
  return [
    {'params': decayed, 'weight_decay': _WEIGHT_DECAY},
    {'params': undecayed, 'weight_decay': 0.0},
  ]


def _cycle_learning_rate(peak_lr: float, fraction: float) -> float:
  """Warm up, then cosine anneal to a near-zero rate, across one cycle."""
  fraction = min(max(fraction, 0.0), 1.0)
  if fraction < _WARMUP_FRACTION:
    ramp = fraction / _WARMUP_FRACTION
    return peak_lr * (_INITIAL_LR_FRACTION + (1.0 - _INITIAL_LR_FRACTION) * ramp)
  progress = (fraction - _WARMUP_FRACTION) / (1.0 - _WARMUP_FRACTION)
  decay = 0.5 * (1.0 + math.cos(math.pi * progress))
  return peak_lr * (_FINAL_LR_FRACTION + (1.0 - _FINAL_LR_FRACTION) * decay)


def _advance_clock(state: Dict[str, Any], num_evals: int) -> None:
  """Accumulate the time the runner bills to training, excluding evaluations.

  Consecutive entries into the update function bracket exactly one data selection and
  one update, which is what the runner charges. An interval that contains an evaluation
  is charged a nominal amount instead, because evaluation time is not billed.
  """
  now = time.time()
  previous = state['last_call_time']
  if previous is not None:
    interval = now - previous
    if num_evals > state['evals_seen']:
      interval = min(interval, _UNCHARGED_INTERVAL_SEC)
    state['elapsed'] += interval
  state['last_call_time'] = now
  state['evals_seen'] = num_evals


def _schedule_fraction(state: Dict[str, Any], num_evals: int) -> float:
  """Position within the current cycle, restarting once an annealed model was seen."""
  elapsed = state['elapsed']
  fraction = (elapsed - state['cycle_start']) / state['cycle_length']
  if fraction < 1.0:
    return fraction
  if state['annealed_at_evals'] is None:
    state['annealed_at_evals'] = num_evals
    return 1.0
  if num_evals <= state['annealed_at_evals']:
    return 1.0
  state['cycle_start'] = elapsed
  state['cycle_length'] = state['next_cycle_length']
  state['next_cycle_length'] *= _CYCLE_GROWTH
  state['peak_lr'] = max(state['peak_lr'] * _PEAK_DECAY, state['floor_peak_lr'])
  state['annealed_at_evals'] = None
  return 0.0


def _clip_gradients(state: Dict[str, Any], model: Any) -> None:
  """Clip against a running estimate of the gradient norm, learned from the run.

  The threshold adapts instead of being fixed, so an architecture with a different
  gradient scale is handled without any constant that knows about it.
  """
  ema = state['grad_norm_ema']
  if state['step'] < _CLIP_WARMUP_STEPS or ema is None:
    max_norm = torch.full((), float('inf'), device=state['norm_device'])
  else:
    max_norm = _CLIP_FACTOR * ema
  total_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=max_norm)
  clipped = torch.nan_to_num(torch.minimum(total_norm, max_norm), nan=0.0, posinf=0.0)
  if ema is None:
    state['grad_norm_ema'] = clipped
  else:
    state['grad_norm_ema'] = _CLIP_EMA_DECAY * ema + (1.0 - _CLIP_EMA_DECAY) * clipped


def get_batch_size(workload_name: str) -> int:
  """One batch size for every workload, as the rules require."""
  del workload_name
  return _BATCH_SIZE


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  """Nesterov momentum SGD plus the bookkeeping the schedule runs on."""
  del workload
  del model_state
  del hyperparameters
  del rng
  if torch.cuda.is_available():
    torch.backends.cudnn.benchmark = True
  peak_lr = _peak_learning_rate()
  optimizer = torch.optim.SGD(
    _parameter_groups(model_params),
    lr=peak_lr * _INITIAL_LR_FRACTION,
    momentum=_MOMENTUM,
    nesterov=True,
  )
  device = next(model_params.parameters()).device
  return {
    'optimizer': optimizer,
    'step': 0,
    'elapsed': 0.0,
    'last_call_time': None,
    'evals_seen': 0,
    'cycle_start': 0.0,
    'cycle_length': _FIRST_CYCLE_SEC,
    'next_cycle_length': _RESTART_CYCLE_SEC,
    'peak_lr': peak_lr,
    'floor_peak_lr': peak_lr * _MIN_PEAK_FRACTION,
    'annealed_at_evals': None,
    'grad_norm_ema': None,
    'norm_device': device,
  }


def update_params(
  workload: spec.Workload,
  current_param_container: spec.ParameterContainer,
  current_params_types: spec.ParameterTypeTree,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  batch: Dict[str, spec.Tensor],
  loss_type: spec.LossType,
  optimizer_state: spec.OptimizerState,
  eval_results: List[Tuple[int, float]],
  global_step: int,
  rng: spec.RandomState,
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
  """One training step at the rate this moment on the clock deserves."""
  del current_params_types
  del hyperparameters
  del loss_type
  del global_step

  num_evals = len(eval_results)
  _advance_clock(optimizer_state, num_evals)
  fraction = _schedule_fraction(optimizer_state, num_evals)
  learning_rate = _cycle_learning_rate(optimizer_state['peak_lr'], fraction)

  optimizer = optimizer_state['optimizer']
  for group in optimizer.param_groups:
    group['lr'] = learning_rate

  current_param_container.train()
  optimizer.zero_grad(set_to_none=True)

  logits, next_model_state = workload.model_fn(
    params=current_param_container,
    augmented_and_preprocessed_input_batch=batch,
    model_state=model_state,
    mode=spec.ForwardPassMode.TRAIN,
    rng=rng,
    update_batch_norm=True,
  )

  losses = workload.loss_fn(
    label_batch=batch['targets'],
    logits_batch=logits,
    mask_batch=batch.get('weights'),
    label_smoothing=_LABEL_SMOOTHING,
  )
  mean_loss = losses['summed'] / losses['n_valid_examples']
  mean_loss.backward()

  _clip_gradients(optimizer_state, current_param_container)
  optimizer.step()

  optimizer_state['step'] += 1
  return optimizer_state, current_param_container, next_model_state


def data_selection(
  workload: spec.Workload,
  input_queue: Iterator[Dict[str, spec.Tensor]],
  optimizer_state: spec.OptimizerState,
  current_param_container: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  global_step: int,
  rng: spec.RandomState,
) -> Dict[str, spec.Tensor]:
  """Take the next batch off the queue, unchanged."""
  del workload
  del optimizer_state
  del current_param_container
  del model_state
  del hyperparameters
  del global_step
  del rng
  return next(input_queue)
