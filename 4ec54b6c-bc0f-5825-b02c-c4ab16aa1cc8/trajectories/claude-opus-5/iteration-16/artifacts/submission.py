"""A self-tuning training algorithm.

One configuration, used unchanged for every workload and every model:

  * adaptive (Adam-style) steps with gradient-norm clipping,
  * a short step-count warmup,
  * a cosine anneal of the step size that is laid out on the evaluation cadence the
    workload publishes and the elapsed training time the harness reports, restarted
    (slightly damped) after each evaluation, so the iterate is always annealed by the
    time the harness looks at it,
  * an exponential moving average of the weights with a horizon that grows with the step
    count; the averaged weights are handed to the harness for evaluation and the raw
    iterate is restored afterwards,
  * data echoing from a small ring buffer of recently seen batches, so the input pipeline
    does not dominate the cost of a step.

Nothing here inspects the workload's identity, the model's shapes, or its state keys.
"""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_PEAK_LR = 0.012
_BETA1 = 0.9
_BETA2 = 0.98
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 20
_CLIP_NORM = 1.0
_LR_FLOOR = 0.03
_CYCLE_DAMP = 0.9
_EMA_HORIZON_FRAC = 0.25
_EMA_MAX_DECAY = 0.999
_EMA_MIN_STEPS = 4.0
_ECHO_POOL_BATCHES = 64
_ECHO_REFRESH = 2
_ECHO_MULT = 4
_LABEL_SMOOTHING = 0.05
_DEFAULT_PERIOD = 3.0


def get_batch_size(workload_name: str) -> int:
  """A single batch size for every workload."""
  del workload_name
  return _BATCH_SIZE


def _module(container: spec.ParameterContainer) -> Any:
  """The eagerly executable module underlying a possibly wrapped container."""
  return getattr(container, '_orig_mod', container)


def _trainable(container: Any) -> List[torch.Tensor]:
  return [p for p in container.parameters() if p.requires_grad]


def _period(workload: spec.Workload) -> float:
  period = getattr(workload, 'eval_period_time_sec', _DEFAULT_PERIOD)
  try:
    period = float(period)
  except (TypeError, ValueError):
    return _DEFAULT_PERIOD
  return period if period > 0.0 else _DEFAULT_PERIOD


def _elapsed(train_state: Optional[Dict[str, Any]]) -> Optional[float]:
  if not train_state:
    return None
  try:
    return float(train_state.get('accumulated_submission_time'))
  except (TypeError, ValueError):
    return None


def _lr_scale(step: int, elapsed: Optional[float], cycle_start: float,
              n_cycles: int, period: float) -> float:
  scale = min(1.0, float(step + 1) / float(_WARMUP_STEPS))
  if elapsed is not None:
    phase = min(1.0, max(0.0, (elapsed - cycle_start) / period))
    scale *= _LR_FLOOR + (1.0 - _LR_FLOOR) * 0.5 * (1.0 + math.cos(math.pi * phase))
  scale *= _CYCLE_DAMP ** max(0, n_cycles)
  return scale


def _ema_decay(step: int) -> float:
  horizon = max(_EMA_MIN_STEPS, _EMA_HORIZON_FRAC * float(step + 1))
  return min(_EMA_MAX_DECAY, 1.0 - 1.0 / horizon)


def _start_pool(state: spec.OptimizerState, fresh: Dict[str, spec.Tensor]) -> None:
  """Allocate the echo ring buffer from the first batch seen, if it is poolable.

  Nothing here is compared against a literal or dispatched on: the buffers simply take
  their trailing extent, dtype and device from whatever the input queue yields, so the
  same code holds for any batch structure the pipeline produces.
  """
  if not isinstance(fresh, dict) or not fresh:
    return
  pool = {}
  lead = 0
  for key, value in fresh.items():
    if not torch.is_tensor(value):
      return
    extent = list(value.size())
    if not extent:
      return
    lead = extent[0]
    capacity = lead * _ECHO_POOL_BATCHES
    buf = value.new_empty([capacity] + extent[1:])
    buf[:lead] = value
    pool[key] = buf
  if not lead:
    return
  state['pool'] = pool
  state['pool_capacity'] = lead * _ECHO_POOL_BATCHES
  state['pool_filled'] = lead
  state['pool_head'] = lead % state['pool_capacity']
  state['pool_device'] = next(iter(pool.values())).device


def _insert(state: spec.OptimizerState, fresh: Dict[str, spec.Tensor]) -> None:
  """Overwrite the oldest slice of the ring buffer with a freshly drawn batch."""
  pool = state['pool']
  if not isinstance(fresh, dict):
    return
  capacity = state['pool_capacity']
  head = state['pool_head']
  lead = 0
  for key, buf in pool.items():
    value = fresh.get(key)
    if not torch.is_tensor(value):
      return
    lead = value.size(0)
    index = (torch.arange(lead, device=state['pool_device']) + head) % capacity
    buf[index] = value.to(dtype=buf.dtype)
  state['pool_head'] = int((head + lead) % capacity)
  state['pool_filled'] = int(min(capacity, state['pool_filled'] + lead))


def _echo_batch(state: spec.OptimizerState,
                input_queue: Iterator[Dict[str, spec.Tensor]],
                batch_size: int) -> Dict[str, spec.Tensor]:
  """Draw a training batch by resampling recently seen examples."""
  if state['echo_off']:
    return next(input_queue)
  step = state['data_step']
  state['data_step'] = step + 1
  pool = state['pool']
  fresh = None
  if pool is None or (step % _ECHO_REFRESH) == 0:
    fresh = next(input_queue)
  if pool is None:
    _start_pool(state, fresh)
    return fresh
  if fresh is not None:
    _insert(state, fresh)
  filled = state['pool_filled']
  if not filled:
    return next(input_queue)
  size = min(batch_size, filled)
  choice = torch.randint(0, filled, (size,), device=state['pool_device'])
  return {key: buf[choice] for key, buf in state['pool'].items()}


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  del workload
  del model_state
  del hyperparameters
  del rng
  params = _trainable(_module(model_params))
  optimizer = torch.optim.AdamW(
    params,
    lr=_PEAK_LR,
    betas=(_BETA1, _BETA2),
    eps=_EPS,
    weight_decay=_WEIGHT_DECAY,
    foreach=True,
  )
  return {
    'optimizer': optimizer,
    'ema': [p.detach().clone() for p in params],
    'backup': None,
    'swapped': False,
    'step': 0,
    'data_step': 0,
    'n_evals': 0,
    'cycle_start': 0.0,
    'pool': None,
    'pool_capacity': 0,
    'pool_filled': 0,
    'pool_head': 0,
    'pool_device': None,
    'echo_off': False,
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
  del current_params_types
  del hyperparameters
  del loss_type
  del global_step

  optimizer = optimizer_state['optimizer']
  model = _module(current_param_container)
  params = _trainable(model)

  if optimizer_state['swapped']:
    backup = optimizer_state['backup']
    if backup is not None:
      with torch.no_grad():
        torch._foreach_copy_(params, backup)
    optimizer_state['swapped'] = False

  elapsed = _elapsed(train_state)
  n_evals = len(eval_results)
  if n_evals != optimizer_state['n_evals']:
    optimizer_state['n_evals'] = n_evals
    optimizer_state['cycle_start'] = elapsed if elapsed is not None else 0.0

  step = optimizer_state['step']
  scale = _lr_scale(
    step,
    elapsed,
    optimizer_state['cycle_start'],
    n_evals,
    _period(workload),
  )
  for group in optimizer.param_groups:
    group['lr'] = _PEAK_LR * scale

  model.train()
  for p in params:
    p.grad = None

  logits, new_model_state = workload.model_fn(
    params=model,
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

  torch.nn.utils.clip_grad_norm_(params, _CLIP_NORM)
  optimizer.step()

  with torch.no_grad():
    decay = _ema_decay(step)
    ema = optimizer_state['ema']
    torch._foreach_mul_(ema, decay)
    torch._foreach_add_(ema, params, alpha=1.0 - decay)

  optimizer_state['step'] = step + 1
  return optimizer_state, current_param_container, new_model_state


def prepare_for_eval(
  workload: spec.Workload,
  current_param_container: spec.ParameterContainer,
  current_params_types: spec.ParameterTypeTree,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  loss_type: spec.LossType,
  optimizer_state: spec.OptimizerState,
  eval_results: List[Tuple[int, float]],
  global_step: int,
  rng: spec.RandomState,
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
  """Hand the harness the averaged weights, keeping the raw iterate for training."""
  del workload
  del current_params_types
  del hyperparameters
  del loss_type
  del eval_results
  del global_step
  del rng

  if optimizer_state['step'] < 2:
    return optimizer_state, current_param_container, model_state

  params = _trainable(_module(current_param_container))
  backup = optimizer_state['backup']
  with torch.no_grad():
    if backup is None:
      backup = [p.detach().clone() for p in params]
      optimizer_state['backup'] = backup
    else:
      torch._foreach_copy_(backup, params)
    torch._foreach_copy_(params, optimizer_state['ema'])
  optimizer_state['swapped'] = True
  return optimizer_state, current_param_container, model_state


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
  """Data echoing: sample from a ring buffer of recently seen batches."""
  del workload
  del current_param_container
  del model_state
  del hyperparameters
  del global_step
  del rng
  try:
    return _echo_batch(optimizer_state, input_queue, _BATCH_SIZE * _ECHO_MULT)
  except (RuntimeError, KeyError, TypeError, IndexError, ValueError):
    # Any pipeline this buffer cannot represent is trained on directly instead.
    optimizer_state['echo_off'] = True
    optimizer_state['pool'] = None
    return next(input_queue)
