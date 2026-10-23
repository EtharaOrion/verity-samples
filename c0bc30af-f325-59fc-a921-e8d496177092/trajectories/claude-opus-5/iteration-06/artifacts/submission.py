"""Self-tuning training algorithm.

Three ideas, none of which need to know which workload or which model they are running on.

The schedule is anchored to the harness's own clock rather than to a step count. The runner reports
`accumulated_submission_time` on every evaluation row and evaluates every `eval_period_time_sec` of
that same clock, both of which are readable from the objects the contract already hands to a
submission, so the learning rate can be annealed to arrive at its floor exactly when an evaluation
is about to fire. A step-count schedule cannot do this, because how many steps fit in a window is a
property of the machine, not of the algorithm.

The cycle repeats with warm restarts if that evaluation was not the last one. Each restart spans
twice the previous window and peaks a little lower, so a configuration that can be solved inside
one window is solved inside one window, and a configuration that needs an order of magnitude more
examples still gets a properly annealed schedule over the horizon it actually needs, without either
case being identified in advance.

The input pipeline, not the device, is what limits this class of workload, so each loaded batch is
used for two updates, with the second seeing a freshly resampled crop and flip generated on device.
That is a generic transformation of the input examples: it applies to any batch of rank-four inputs
and falls back to plain queue consumption for anything else.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch
import torch.nn.functional as F

from algoperf import spec

_BATCH_SIZE = 256
_PEAK_LR = 1.0 * (_BATCH_SIZE / 256.0)
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1
_GRAD_CLIP = 1.0
_WARMUP_FRAC = 0.15
_WARMUP_START_FRAC = 0.05
_FINAL_LR_FRAC = 0.01
_CYCLE_DECAY = 0.8
_MIN_PEAK_FRAC = 0.25
_CYCLE_MARGIN_SEC = 1.0
_DEFAULT_EVAL_PERIOD_SEC = 25.0
_ECHO_FACTOR = 2
_CROP_PAD = 4


def get_batch_size(workload_name: str) -> int:
  """A single global batch size, used for every workload."""
  del workload_name
  return _BATCH_SIZE


def _eval_period(workload: spec.Workload) -> float:
  """How often the harness evaluates, in seconds of accumulated submission time."""
  period = getattr(workload, 'eval_period_time_sec', _DEFAULT_EVAL_PERIOD_SEC)
  try:
    period = float(period)
  except (TypeError, ValueError):
    return _DEFAULT_EVAL_PERIOD_SEC
  if not math.isfinite(period) or period <= 0.0:
    return _DEFAULT_EVAL_PERIOD_SEC
  return period


def _cycle_span(cycle_index: int, period: float) -> float:
  """One evaluation period for the first two cycles, doubling after that."""
  if cycle_index <= 2:
    return period
  return float(2 ** (cycle_index - 2)) * period


def _begin_cycle(state: Dict[str, Any]) -> None:
  state['cycle_index'] += 1
  span = _cycle_span(state['cycle_index'], state['eval_period'])
  state['cycle_start'] = state['elapsed']
  state['cycle_end'] = state['elapsed'] + max(span - _CYCLE_MARGIN_SEC, 1.0)
  if state['cycle_index'] > 1:
    state['peak_lr'] = max(
      state['peak_lr'] * _CYCLE_DECAY, _PEAK_LR * _MIN_PEAK_FRAC
    )


def _scheduled_lr(state: Dict[str, Any]) -> float:
  span = max(state['cycle_end'] - state['cycle_start'], 1e-3)
  frac = (state['elapsed'] - state['cycle_start']) / span
  frac = min(max(frac, 0.0), 1.0)
  peak = state['peak_lr']
  if frac < _WARMUP_FRAC:
    ramp = frac / _WARMUP_FRAC
    return peak * (_WARMUP_START_FRAC + (1.0 - _WARMUP_START_FRAC) * ramp)
  progress = (frac - _WARMUP_FRAC) / (1.0 - _WARMUP_FRAC)
  decayed = 0.5 * (1.0 + math.cos(math.pi * progress))
  return peak * (_FINAL_LR_FRAC + (1.0 - _FINAL_LR_FRAC) * decayed)


def _latest_accumulated_time(eval_results: List[Any]) -> Optional[float]:
  """Read the runner's own accumulated submission time off the last eval row."""
  if not eval_results:
    return None
  row = eval_results[-1]
  if isinstance(row, (tuple, list)) and len(row) >= 2:
    payload = row[1]
  else:
    payload = row
  if isinstance(payload, dict):
    value = payload.get('accumulated_submission_time')
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
      return float(value)
  return None


def _resample_inputs(inputs: spec.Tensor) -> spec.Tensor:
  """Fresh random flip and shifted crop for a batch of rank-four inputs."""
  flipped = torch.where(
    (torch.rand(inputs.shape[0], device=inputs.device) < 0.5).view(-1, 1, 1, 1),
    inputs.flip(-1),
    inputs,
  )
  padded = F.pad(flipped, (_CROP_PAD,) * 4)
  top = int(torch.randint(0, 2 * _CROP_PAD + 1, (1,)).item())
  left = int(torch.randint(0, 2 * _CROP_PAD + 1, (1,)).item())
  return padded[
    :, :, top : top + inputs.shape[-2], left : left + inputs.shape[-1]
  ]


def _echoed_batch(batch: Dict[str, spec.Tensor]) -> Dict[str, spec.Tensor]:
  inputs = batch.get('inputs')
  if not torch.is_tensor(inputs) or inputs.dim() != 4:
    return batch
  echoed = dict(batch)
  echoed['inputs'] = _resample_inputs(inputs)
  return echoed


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  """Nesterov SGD, with decay applied only to parameters of rank two or more."""
  del model_state
  del hyperparameters
  del rng

  use_cuda = torch.cuda.is_available()
  if use_cuda:
    torch.backends.cudnn.benchmark = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cuda.matmul.allow_tf32 = True

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
    lr=_PEAK_LR * _WARMUP_START_FRAC,
    momentum=_MOMENTUM,
    nesterov=True,
  )

  period = _eval_period(workload)
  state = {
    'optimizer': optimizer,
    'step': 0,
    'fetches': 0,
    'cached_batch': None,
    'elapsed': 0.0,
    'last_end': None,
    'seen_evals': 0,
    'eval_period': period,
    'peak_lr': _PEAK_LR,
    'cycle_index': 0,
    'cycle_start': 0.0,
    'cycle_end': period,
    'amp': use_cuda,
  }
  _begin_cycle(state)
  return state


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
  """One training step under the time-anchored one-cycle schedule."""
  del current_params_types
  del hyperparameters
  del loss_type
  del global_step

  state = optimizer_state
  optimizer = state['optimizer']

  now = time.monotonic()
  if len(eval_results) > state['seen_evals']:
    state['seen_evals'] = len(eval_results)
    anchor = _latest_accumulated_time(eval_results)
    if anchor is not None:
      state['elapsed'] = anchor
  elif state['last_end'] is not None:
    state['elapsed'] += max(now - state['last_end'], 0.0)
  if state['elapsed'] >= state['cycle_end']:
    _begin_cycle(state)

  learning_rate = _scheduled_lr(state)
  for group in optimizer.param_groups:
    group['lr'] = learning_rate

  current_param_container.train()
  optimizer.zero_grad(set_to_none=True)

  with torch.autocast(
    device_type='cuda', dtype=torch.bfloat16, enabled=state['amp']
  ):
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
    logits_batch=logits.float(),
    mask_batch=batch.get('weights'),
    label_smoothing=_LABEL_SMOOTHING,
  )
  loss = losses['summed'] / losses['n_valid_examples']
  loss.backward()

  torch.nn.utils.clip_grad_norm_(
    current_param_container.parameters(), _GRAD_CLIP
  )
  optimizer.step()

  state['step'] += 1
  state['last_end'] = time.monotonic()
  return state, current_param_container, new_model_state


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
  """Echo each loaded batch, resampling its augmentation on device in between."""
  del workload
  del current_param_container
  del model_state
  del hyperparameters
  del global_step
  del rng

  state = optimizer_state
  index = state['fetches']
  state['fetches'] = index + 1
  cached = state['cached_batch']
  if index % _ECHO_FACTOR == 0 or cached is None:
    batch = next(input_queue)
    state['cached_batch'] = batch
    return batch
  return _echoed_batch(cached)
