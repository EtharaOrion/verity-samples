"""Self-tuning training algorithm: layerwise-trust-ratio Adam with warmup-cosine decay.

The update is Adam's preconditioned direction rescaled, per parameter tensor, by the ratio of
the parameter norm to the update norm (the LARS/LAMB trust ratio). That makes the effective
step size scale-free: a single peak learning rate transfers across layer widths, activations
and normalisation choices without any per-workload constant, which is what the self-tuning
ruleset asks for.

Everything the algorithm remembers lives inside the optimizer object the harness hands back on
the next call, so there is no module-level mutable state and nothing can carry over between
runs inside one process. The evaluated iterate is a debiased moving average of the trajectory.

Nothing here reads the workload name, the parameter shapes, the parameter count or the model
state keys; one setting is used everywhere.
"""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LR = 0.015
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WARMUP_STEPS = 60
_DECAY_STEPS = 1800
_LR_FLOOR = 0.05
_CLIP_NORM = 1.0
_TRUST_CAP = 10.0
_LABEL_SMOOTHING = 0.1
_EMA_DECAY = 0.998
_EMA_WARM = 10.0
_M_KEY = '_first_moment'
_V_KEY = '_second_moment'
_T_KEY = '_local_step'
_AVG_KEY = '_iterate_average'
_LIVE_KEY = '_live_iterate'
_SWAP_KEY = '_averaged_in_place'


def get_batch_size(workload_name: str) -> int:
  """One batch size for every workload, which is what the rules allow."""
  del workload_name
  return _BATCH_SIZE


def _lr_multiplier(step: int) -> float:
  """Linear warmup, then cosine decay onto a floor that keeps late steps useful."""
  warm = min(1.0, float(step + 1) / float(_WARMUP_STEPS))
  progress = min(1.0, max(0.0, float(step) / float(_DECAY_STEPS)))
  cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
  return warm * (_LR_FLOOR + (1.0 - _LR_FLOOR) * cosine)


def _average_decay(step: int) -> float:
  """Debiased averaging horizon: short early, saturating at the target decay."""
  return min(_EMA_DECAY, (float(step) + 1.0) / (float(step) + 1.0 + _EMA_WARM))


def _restore_live_iterate(optimizer: Any) -> None:
  """Undo an in-place swap to the averaged iterate, if one is outstanding."""
  for group in optimizer.param_groups:
    if not group.get(_SWAP_KEY, False):
      continue
    with torch.no_grad():
      for param in group['params']:
        live = optimizer.state[param].get(_LIVE_KEY)
        if live is not None:
          param.copy_(live)
    group[_SWAP_KEY] = False


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  """A single, workload-independent configuration."""
  del workload
  del model_state
  del hyperparameters
  del rng
  optimizer = torch.optim.SGD(model_params.parameters(), lr=_PEAK_LR)
  for group in optimizer.param_groups:
    group[_SWAP_KEY] = False
  return {'optimizer': optimizer}


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
  """One training step."""
  del current_params_types
  del hyperparameters
  del eval_results
  del train_state

  optimizer = optimizer_state['optimizer']
  _restore_live_iterate(optimizer)

  current_param_container.train()
  optimizer.zero_grad(set_to_none=True)

  logits, next_state = workload.model_fn(
    params=current_param_container,
    augmented_and_preprocessed_input_batch=batch,
    model_state=model_state,
    mode=spec.ForwardPassMode.TRAIN,
    rng=rng,
    update_batch_norm=True,
  )

  # Branching on the loss type is explicitly permitted; smoothing is only meaningful
  # for a softmax cross-entropy objective.
  smoothing = (
    _LABEL_SMOOTHING if loss_type == spec.LossType.SOFTMAX_CROSS_ENTROPY else 0.0
  )
  losses = workload.loss_fn(
    label_batch=batch['targets'],
    logits_batch=logits,
    mask_batch=batch.get('weights'),
    label_smoothing=smoothing,
  )
  mean_loss = losses['summed'] / losses['n_valid_examples']
  mean_loss.backward()

  torch.nn.utils.clip_grad_norm_(
    current_param_container.parameters(), max_norm=_CLIP_NORM
  )

  lr = _PEAK_LR * _lr_multiplier(global_step)
  decay = _average_decay(global_step)

  with torch.no_grad():
    for group in optimizer.param_groups:
      group['lr'] = lr
      for param in group['params']:
        grad = param.grad
        if grad is None:
          continue
        state = optimizer.state[param]
        if _M_KEY not in state:
          state[_M_KEY] = torch.zeros_like(param)
          state[_V_KEY] = torch.zeros_like(param)
          state[_T_KEY] = 0
          state[_AVG_KEY] = param.detach().clone()
        state[_T_KEY] += 1
        local_step = state[_T_KEY]
        first = state[_M_KEY]
        second = state[_V_KEY]
        first.mul_(_BETA1).add_(grad, alpha=1.0 - _BETA1)
        second.mul_(_BETA2).addcmul_(grad, grad, value=1.0 - _BETA2)
        bias1 = 1.0 - _BETA1**local_step
        bias2 = 1.0 - _BETA2**local_step
        direction = (first / bias1) / ((second / bias2).sqrt() + _EPS)
        # Layerwise trust ratio: keeps the step a fixed fraction of the weight norm,
        # so one peak rate transfers across layer widths and nonlinearities.
        weight_norm = param.detach().norm()
        update_norm = direction.norm()
        trust = torch.where(
          (weight_norm > 0.0) & (update_norm > 0.0),
          torch.clamp(weight_norm / (update_norm + _EPS), max=_TRUST_CAP),
          torch.ones_like(weight_norm),
        )
        param.add_(direction * (-lr * trust))
        state[_AVG_KEY].mul_(decay).add_(param.detach(), alpha=1.0 - decay)

  return optimizer_state, current_param_container, next_state


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
  """Evaluate the averaged iterate, keeping the live one for the next step."""
  del workload
  del current_params_types
  del hyperparameters
  del loss_type
  del eval_results
  del global_step
  del rng

  optimizer = optimizer_state['optimizer']
  with torch.no_grad():
    for group in optimizer.param_groups:
      if group.get(_SWAP_KEY, False):
        continue
      swapped = False
      for param in group['params']:
        state = optimizer.state[param]
        average = state.get(_AVG_KEY)
        if average is None:
          continue
        live = state.get(_LIVE_KEY)
        if live is None:
          state[_LIVE_KEY] = param.detach().clone()
        else:
          live.copy_(param.detach())
        param.copy_(average)
        swapped = True
      group[_SWAP_KEY] = swapped

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
  """Take the next batch off the queue, unchanged."""
  del workload
  del optimizer_state
  del current_param_container
  del model_state
  del hyperparameters
  del global_step
  del rng
  return next(input_queue)
