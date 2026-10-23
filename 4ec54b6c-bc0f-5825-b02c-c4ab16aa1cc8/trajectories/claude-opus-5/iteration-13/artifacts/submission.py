"""A self-tuning training algorithm.

One fixed setting, applied identically to every workload. The pieces are:

  * adaptive (Adam-style) preconditioned steps, which is what the seed lacked,
  * a short linear warmup measured in steps, so the first steps cannot diverge,
  * an anneal driven by how far the run has progressed on its own clock, which the
    submission reads from the number of evaluation rows the harness has produced,
  * a smoothed training objective, which stabilises the late iterates,
  * a debiased Polyak (exponential moving) average of the iterates, swapped into the
    parameters for every evaluation and swapped straight back out afterwards.

Nothing here inspects the workload's identity, its parameter shapes, or its state keys;
the same constants are used everywhere.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_BASE_LR = 0.006
_WARMUP_STEPS = 50
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_LABEL_SMOOTHING = 0.1
_EMA_MAX_DECAY = 0.995
_EMA_HORIZON = 16.0
_EVAL_ANNEAL = 0.3
_MIN_LR_SCALE = 0.08


def _warmup_scale(step: int) -> float:
  """Linear warmup on the step counter, then flat."""
  if step < _WARMUP_STEPS:
    return float(step + 1) / float(_WARMUP_STEPS)
  return 1.0


def _anneal_scale(num_evals: int) -> float:
  """Anneal keyed to elapsed run progress as reported by the harness' own clock.

  Evaluations fire on a wall clock, so the number of evaluation rows already logged is
  a workload-independent read of how far into its runtime budget the run has gone. The
  step size decays as that count grows and is floored so late steps still make progress.
  """
  progressed = num_evals - 1
  if progressed < 0:
    progressed = 0
  scale = 1.0 / (1.0 + _EVAL_ANNEAL * float(progressed))
  if scale < _MIN_LR_SCALE:
    return _MIN_LR_SCALE
  return scale


def _ema_decay(averaged_steps: int) -> float:
  """Debiased averaging weight: a running mean early, a fixed-horizon EMA later."""
  ramp = (1.0 + float(averaged_steps)) / (_EMA_HORIZON + float(averaged_steps))
  if ramp > _EMA_MAX_DECAY:
    return _EMA_MAX_DECAY
  return ramp


def get_batch_size(workload_name: str) -> int:
  """A single batch size, used for every workload."""
  del workload_name
  return _BATCH_SIZE


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  """Adaptive optimizer plus a buffer for the averaged iterate."""
  del workload
  del model_state
  del hyperparameters
  del rng
  params = [p for p in model_params.parameters() if p.requires_grad]
  optimizer = torch.optim.AdamW(
    params,
    lr=_BASE_LR,
    betas=(_BETA1, _BETA2),
    eps=_EPS,
    weight_decay=_WEIGHT_DECAY,
  )
  ema = [p.detach().clone() for p in params]
  return {
    'optimizer': optimizer,
    'params': params,
    'ema': ema,
    'backup': None,
    'step': 0,
    'averaged': 0,
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
  """One training step."""
  del current_params_types
  del hyperparameters
  del loss_type
  del global_step

  optimizer = optimizer_state['optimizer']
  params = optimizer_state['params']

  # If the averaged iterate was swapped in for an evaluation, put the training
  # iterate back before taking another step from it.
  backup = optimizer_state['backup']
  if backup is not None:
    with torch.no_grad():
      for p, b in zip(params, backup):
        p.copy_(b)
    optimizer_state['backup'] = None

  step = optimizer_state['step']
  num_evals = len(eval_results) if eval_results is not None else 0
  lr = _BASE_LR * _warmup_scale(step) * _anneal_scale(num_evals)
  for group in optimizer.param_groups:
    group['lr'] = lr

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

  losses = workload.loss_fn(
    label_batch=batch['targets'],
    logits_batch=logits,
    mask_batch=batch.get('weights'),
    label_smoothing=_LABEL_SMOOTHING,
  )
  mean_loss = losses['summed'] / losses['n_valid_examples']
  mean_loss.backward()
  optimizer.step()

  # Polyak averaging of the iterates. Averaging only starts once the warmup is over,
  # so the earliest, largely untrained iterates never enter the average.
  if step + 1 >= _WARMUP_STEPS:
    ema = optimizer_state['ema']
    averaged = optimizer_state['averaged']
    with torch.no_grad():
      if averaged == 0:
        for e, p in zip(ema, params):
          e.copy_(p.detach())
      else:
        decay = _ema_decay(averaged)
        torch._foreach_mul_(ema, decay)
        torch._foreach_add_(ema, params, alpha=1.0 - decay)
    optimizer_state['averaged'] = averaged + 1

  optimizer_state['step'] = step + 1
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
  """Swap the averaged iterate in, keeping the training iterate for the next step."""
  del workload
  del current_params_types
  del hyperparameters
  del loss_type
  del eval_results
  del global_step
  del rng

  params = optimizer_state['params']
  ema = optimizer_state['ema']
  if optimizer_state['averaged'] > 0 and optimizer_state['backup'] is None:
    with torch.no_grad():
      optimizer_state['backup'] = [p.detach().clone() for p in params]
      for p, e in zip(params, ema):
        p.copy_(e)
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
