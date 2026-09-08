# VERITY-CANARY-BLOCK-BEGIN
# 0 VERITY-CANARY-EA9F085DB6DDB92A348057A6381F323F
# 1 VERITY-CANARY-460A0F0C9B269107825353622C89A815
# 2 VERITY-CANARY-1833BEB1301332A4CA8A610962DE078C
# 3 VERITY-CANARY-99570E00CAFE25A12A33397769893A0F
# VERITY-CANARY-BLOCK-END
"""Reference submission. PRIVATE CARRIER. Never on the agent-visible surface.

This is the oracle: the answer the task was built to have, and the budget it consumes is what
`objective.anchors.reference_budget` is measured from.

Its provenance is recorded rather than implied. Unlike the reference it replaces, this is not code the
author wrote. It is the submission produced by turn 3 of episode `scripts/runs/ep-5turn`, the first
rollout to clear this corpus's conjunctive predicate, preserved byte for byte below its docstring at
source sha256 6dd545439ed59cc40b88673c7cbcd1e87d7c4652c8912acda91e3b490e2ec1e4. It was promoted because
it is the only compliant submission ever measured on this bundle and it reaches the target in 54,512
train examples against the 190,976 the authored reference needed, so an anchor taken from the authored
reference calibrates the closure scale against a submission a compliant model already beats by 3.5x.

Two consequences follow and neither is hidden. `anchor_class` stays `authored`, because the closed set
admits `measured_public` only for the fastest known public submission and `measured_baseline` only for
the upstream NAdamW baseline, and this is neither. And the oracle is no longer independent of the model
population the corpus measures, which is carried as the declared gap
`reference-derived-from-measured-rollout`.

The design point it demonstrates is the one the task grades. The budget axis is train_examples, so
sample efficiency rather than wall-clock is what closure rewards: the algorithm takes extra gradient
steps on batches it has already consumed, which buys progress without spending budget, and it is held
in check by C-PER-STEP-COST-CEILING rather than by the budget itself. It selects nothing from the
workload name, the parameter shapes or the model state keys, which is what lets it survive both the
shape-fingerprint rule and the held-out architectural variants.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 8
_BASE_LR = 0.0015
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 50
_REPLAY_STEPS = 2
_REPLAY_EXAMPLES = 64
_BUFFER_BATCHES = 8192
_EMA_DECAY = 0.99
_EMA_WARMUP = 10.0


def get_batch_size(workload_name: str) -> int:
  """A single batch size, used for every workload."""
  del workload_name
  return _BATCH_SIZE


def _detach_batch(batch: Dict[str, spec.Tensor]) -> Dict[str, spec.Tensor]:
  out = {}
  for key, value in batch.items():
    if torch.is_tensor(value):
      out[key] = value.detach().clone()
  return out


def _batch_len(batch: Dict[str, spec.Tensor]) -> int:
  for value in batch.values():
    if torch.is_tensor(value):
      return int(value.shape[0])
  return 0


def _concat(batches: List[Dict[str, spec.Tensor]]) -> Dict[str, spec.Tensor]:
  if len(batches) == 1:
    return batches[0]
  keys = set(batches[0].keys())
  for b in batches[1:]:
    keys &= set(b.keys())
  return {k: torch.cat([b[k] for b in batches], dim=0) for k in sorted(keys)}


def _sample_replay(state: spec.OptimizerState) -> Optional[Dict[str, spec.Tensor]]:
  buffer = state['buffer']
  n = len(buffer)
  if n == 0:
    return None
  k = state['replay_chunks']
  if k <= 1:
    idx = int(torch.randint(0, n, (1,), generator=state['generator']).item())
    return buffer[idx]
  idx = torch.randint(0, n, (k,), generator=state['generator']).tolist()
  return _concat([buffer[i] for i in idx])


def _gradient_step(
  workload: spec.Workload,
  params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  batch: Dict[str, spec.Tensor],
  optimizer: Any,
  rng: spec.RandomState,
  update_batch_norm: bool,
) -> spec.ModelAuxiliaryState:
  optimizer.zero_grad(set_to_none=True)
  logits, new_model_state = workload.model_fn(
    params=params,
    augmented_and_preprocessed_input_batch=batch,
    model_state=model_state,
    mode=spec.ForwardPassMode.TRAIN,
    rng=rng,
    update_batch_norm=update_batch_norm,
  )
  losses = workload.loss_fn(
    label_batch=batch['targets'],
    logits_batch=logits,
    mask_batch=batch.get('weights'),
    label_smoothing=0.0,
  )
  loss = losses['summed'] / losses['n_valid_examples']
  loss.backward()
  optimizer.step()
  return new_model_state


def _update_ema(state: spec.OptimizerState) -> None:
  step = state['step']
  decay = min(_EMA_DECAY, (step + 1.0) / (step + _EMA_WARMUP))
  with torch.no_grad():
    for shadow, param in zip(state['ema'], state['params']):
      shadow.mul_(decay).add_(param.detach(), alpha=1.0 - decay)


def _restore_raw_weights(state: spec.OptimizerState) -> None:
  backup = state['backup']
  if backup is None:
    return
  with torch.no_grad():
    for param, saved in zip(state['params'], backup):
      param.copy_(saved)
  state['backup'] = None


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  """Adam with warmup, a replay buffer and a weight EMA. No workload-specific choices."""
  del workload
  del model_state
  del hyperparameters
  params = [p for p in model_params.parameters() if p.requires_grad]
  optimizer = torch.optim.AdamW(
    params,
    lr=_BASE_LR,
    betas=(_BETA1, _BETA2),
    eps=_EPS,
    weight_decay=_WEIGHT_DECAY,
  )
  generator = torch.Generator()
  try:
    seed = int(rng[0]) % (2**31 - 1)
  except (TypeError, IndexError, ValueError):
    seed = 0
  generator.manual_seed(seed)
  return {
    'optimizer': optimizer,
    'params': params,
    'ema': [p.detach().clone() for p in params],
    'backup': None,
    'buffer': [],
    'replay_chunks': max(1, _REPLAY_EXAMPLES // max(1, _BATCH_SIZE)),
    'generator': generator,
    'step': 0,
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
  """One consumed batch: one fresh step plus a few steps on already-seen examples."""
  del current_params_types
  del hyperparameters
  del loss_type
  del eval_results
  del global_step

  _restore_raw_weights(optimizer_state)

  optimizer = optimizer_state['optimizer']
  step = optimizer_state['step']
  scale = min(1.0, (step + 1.0) / _WARMUP_STEPS)
  for group in optimizer.param_groups:
    group['lr'] = _BASE_LR * scale

  current_param_container.train()
  new_model_state = _gradient_step(
    workload,
    current_param_container,
    model_state,
    batch,
    optimizer,
    rng,
    True,
  )

  buffer = optimizer_state['buffer']
  if _batch_len(batch) > 0:
    buffer.append(_detach_batch(batch))
    if len(buffer) > _BUFFER_BATCHES:
      buffer.pop(0)

  for _ in range(_REPLAY_STEPS):
    replay_batch = _sample_replay(optimizer_state)
    if replay_batch is None:
      break
    _gradient_step(
      workload,
      current_param_container,
      new_model_state,
      replay_batch,
      optimizer,
      rng,
      False,
    )

  _update_ema(optimizer_state)
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
  """Swap the averaged weights in for the evaluation; training resumes from the raw ones."""
  del workload
  del current_params_types
  del hyperparameters
  del loss_type
  del eval_results
  del global_step
  del rng
  if optimizer_state['step'] > 0 and optimizer_state['backup'] is None:
    params = optimizer_state['params']
    optimizer_state['backup'] = [p.detach().clone() for p in params]
    with torch.no_grad():
      for param, shadow in zip(params, optimizer_state['ema']):
        param.copy_(shadow)
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
