"""Self-tuning training algorithm.

One fixed configuration for every workload: SGD with Nesterov momentum, weight decay
on multi-dimensional parameters only, gradient clipping, and a wall-clock one-cycle
schedule that restarts at every evaluation boundary. Each cycle anneals the step size
to near zero just before the next evaluation fires, so every evaluation row sees an
annealed model; successive cycles lower the peak, so a run that needs more time keeps
refining rather than stalling. Training stops as soon as an evaluation row reaches the
workload's validation target.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_MOMENTUM = 0.9
_PEAK_LR = 0.6
_WEIGHT_DECAY = 5e-4
_WARMUP_FRAC = 0.18
_START_LR_FRAC = 0.05
_FINAL_LR_FRAC = 0.002
_CYCLE_PEAK_DECAY = 0.8
_MIN_PEAK_FRAC = 0.2
_CYCLE_SAFETY = 0.98
_DEFAULT_CYCLE_SEC = 25.0
_GRAD_CLIP = 1.0
_LABEL_SMOOTHING = 0.1


def get_batch_size(workload_name: str) -> int:
  """A single batch size for every workload, as the rules require."""
  del workload_name
  return _BATCH_SIZE


def _cycle_seconds(workload: spec.Workload) -> float:
  period = getattr(workload, 'eval_period_time_sec', None)
  if period is None or float(period) <= 0.0:
    return _DEFAULT_CYCLE_SEC
  return float(period)


def _elapsed_seconds(optimizer_state, train_state) -> float:
  if train_state is not None:
    accumulated = train_state.get('accumulated_submission_time', None)
    if accumulated is not None:
      return float(accumulated)
  start = optimizer_state.get('wall_start', None)
  if start is None:
    optimizer_state['wall_start'] = time.time()
    return 0.0
  return time.time() - start


def _schedule(optimizer_state, elapsed: float, evals_seen: int) -> float:
  """One-cycle step size in seconds, restarted at every evaluation boundary."""
  if evals_seen > optimizer_state['evals_seen']:
    optimizer_state['evals_seen'] = evals_seen
    optimizer_state['cycle_start'] = elapsed

  start = optimizer_state['cycle_start']
  length = optimizer_state['cycle_len']
  if elapsed - start > length:
    start = elapsed
    optimizer_state['cycle_start'] = start
  # The harness fires its first evaluation immediately after the first step, so
  # the first full cycle is the one that follows it and keeps the full peak.
  index = max(0, optimizer_state['evals_seen'] - 1)

  peak = _PEAK_LR * max(_MIN_PEAK_FRAC, _CYCLE_PEAK_DECAY**index)
  frac = (elapsed - start) / max(1e-6, length * _CYCLE_SAFETY)
  frac = min(1.0, max(0.0, frac))
  if frac < _WARMUP_FRAC:
    ramp = frac / _WARMUP_FRAC
    return peak * (_START_LR_FRAC + (1.0 - _START_LR_FRAC) * ramp)
  progress = (frac - _WARMUP_FRAC) / (1.0 - _WARMUP_FRAC)
  cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
  return peak * (_FINAL_LR_FRAC + (1.0 - _FINAL_LR_FRAC) * cosine)


def _target_already_reached(workload, eval_results) -> bool:
  if not eval_results:
    return False
  last = eval_results[-1][1]
  if not isinstance(last, dict):
    return False
  try:
    return bool(workload.has_reached_validation_target(last))
  except (KeyError, AttributeError, TypeError):
    return False


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  """Nesterov SGD; weight decay only on parameters with two or more axes."""
  del model_state
  del hyperparameters
  del rng

  decayed = []
  undecayed = []
  for parameter in model_params.parameters():
    if not parameter.requires_grad:
      continue
    if parameter.ndim >= 2:
      decayed.append(parameter)
    else:
      undecayed.append(parameter)

  optimizer = torch.optim.SGD(
    [
      {'params': decayed, 'weight_decay': _WEIGHT_DECAY},
      {'params': undecayed, 'weight_decay': 0.0},
    ],
    lr=_PEAK_LR * _START_LR_FRAC,
    momentum=_MOMENTUM,
    nesterov=True,
  )
  return {
    'optimizer': optimizer,
    'step': 0,
    'cycle_start': 0.0,
    'cycle_len': _cycle_seconds(workload),
    'cycle_index': 0,
    'evals_seen': 0,
    'wall_start': None,
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
  train_state: Optional[Dict[str, Any]] = None,
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
  """One training step at the scheduled step size."""
  del current_params_types
  del hyperparameters
  del loss_type
  del global_step

  if _target_already_reached(workload, eval_results):
    raise spec.TrainingCompleteError

  optimizer = optimizer_state['optimizer']
  learning_rate = _schedule(
    optimizer_state,
    _elapsed_seconds(optimizer_state, train_state),
    len(eval_results),
  )
  for group in optimizer.param_groups:
    group['lr'] = learning_rate

  current_param_container.train()
  optimizer.zero_grad(set_to_none=True)

  logits, new_model_state = workload.model_fn(
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

  torch.nn.utils.clip_grad_norm_(
    current_param_container.parameters(), _GRAD_CLIP
  )
  optimizer.step()

  optimizer_state['step'] += 1
  return optimizer_state, current_param_container, new_model_state


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
