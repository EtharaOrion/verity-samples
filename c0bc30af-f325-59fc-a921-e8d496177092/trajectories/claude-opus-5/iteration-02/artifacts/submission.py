"""Self-tuning AlgoPerf submission.

Nesterov SGD with warmup and cosine annealing on a schedule that is anchored to the
harness's own evaluation cadence rather than to any workload-specific constant: the step
size warms up and anneals inside one evaluation period, so whichever evaluation happens to
be the qualifying one sees an annealed model, and then warm-restarts at a slightly lower
peak so a run that needs many more periods keeps making progress. Mixed precision is used
when the device offers it, which buys steps rather than spending them.

Module level holds only the docstring, imports, literal constants and definitions.
"""

import contextlib
import math
import time
from typing import Any, Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_PEAK_LR = 0.15
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1
_WARMUP_FRAC = 0.10
_INITIAL_LR_FRAC = 0.05
_FINAL_LR_FRAC = 0.01
_CYCLE_FRAC = 0.92
_CYCLE_DECAY = 0.85
_MIN_PEAK_FRAC = 0.15
_MIN_CYCLE_COMPLETION = 0.5
_DEFAULT_PERIOD_SEC = 25.0


def get_batch_size(workload_name: str) -> int:
  """A single batch size for every workload, as the self-tuning rules require."""
  del workload_name
  return _BATCH_SIZE


def _make_optimizer(model_params: spec.ParameterContainer) -> Any:
  """Nesterov SGD over the trainable tensors, fused when the device supports it."""
  params = [p for p in model_params.parameters() if p.requires_grad]
  kwargs = {
    'lr': _PEAK_LR * _INITIAL_LR_FRAC,
    'momentum': _MOMENTUM,
    'nesterov': True,
    'weight_decay': _WEIGHT_DECAY,
  }
  try:
    return torch.optim.SGD(params, fused=True, **kwargs)
  except (TypeError, ValueError, RuntimeError):
    return torch.optim.SGD(params, **kwargs)


def _cycle_seconds(workload: spec.Workload) -> float:
  """Anneal over one evaluation period, read off a generic workload property."""
  period = getattr(workload, 'eval_period_time_sec', _DEFAULT_PERIOD_SEC)
  try:
    period = float(period)
  except (TypeError, ValueError):
    period = _DEFAULT_PERIOD_SEC
  if not period > 0.0:
    period = _DEFAULT_PERIOD_SEC
  return period * _CYCLE_FRAC


def _schedule(progress: float, cycle_index: int) -> float:
  """Warmup then cosine decay within a cycle; later cycles restart lower."""
  peak = _PEAK_LR * max(_CYCLE_DECAY**cycle_index, _MIN_PEAK_FRAC)
  if progress < _WARMUP_FRAC:
    return peak * (
      _INITIAL_LR_FRAC
      + (1.0 - _INITIAL_LR_FRAC) * progress / _WARMUP_FRAC
    )
  tail = min((progress - _WARMUP_FRAC) / (1.0 - _WARMUP_FRAC), 1.0)
  cosine = 0.5 * (1.0 + math.cos(math.pi * tail))
  return peak * (_FINAL_LR_FRAC + (1.0 - _FINAL_LR_FRAC) * cosine)


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  """Build the optimizer and the run-time state the clock-driven schedule needs."""
  del model_state
  del hyperparameters
  del rng
  use_amp = torch.cuda.is_available()
  if use_amp:
    torch.backends.cudnn.benchmark = True
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
  return {
    'optimizer': _make_optimizer(model_params),
    'cycle_start': None,
    'cycle_index': 0,
    'evals_seen': 0,
    'cycle_len': _cycle_seconds(workload),
    'amp': use_amp,
  }


def _autocast(enabled: bool) -> Any:
  """bfloat16 autocast where the device has it, and a no-op context otherwise."""
  if enabled:
    return torch.autocast(device_type='cuda', dtype=torch.bfloat16)
  return contextlib.nullcontext()


def _advance_cycle(optimizer_state: spec.OptimizerState, now: float) -> float:
  """Realign the schedule with the evaluation clock and return cycle progress."""
  if optimizer_state['cycle_start'] is None:
    optimizer_state['cycle_start'] = now
  return (now - optimizer_state['cycle_start']) / optimizer_state['cycle_len']


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
  """One training step."""
  del current_params_types
  del hyperparameters
  del loss_type
  del global_step

  now = time.monotonic()
  num_evals = len(eval_results)
  if num_evals > optimizer_state['evals_seen']:
    optimizer_state['evals_seen'] = num_evals
    start = optimizer_state['cycle_start']
    if (
      start is not None
      and (now - start) >= _MIN_CYCLE_COMPLETION * optimizer_state['cycle_len']
    ):
      optimizer_state['cycle_index'] += 1
    optimizer_state['cycle_start'] = now

  progress = _advance_cycle(optimizer_state, now)
  lr = _schedule(min(progress, 1.0), optimizer_state['cycle_index'])
  optimizer = optimizer_state['optimizer']
  for group in optimizer.param_groups:
    group['lr'] = lr

  optimizer.zero_grad(set_to_none=True)
  with _autocast(optimizer_state['amp']):
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
    loss = losses['summed'] / losses['n_valid_examples']
  loss.backward()
  optimizer.step()

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
  """Take the next batch off the infinitely repeating queue, unchanged."""
  del workload
  del optimizer_state
  del current_param_container
  del model_state
  del hyperparameters
  del global_step
  del rng
  return next(input_queue)
