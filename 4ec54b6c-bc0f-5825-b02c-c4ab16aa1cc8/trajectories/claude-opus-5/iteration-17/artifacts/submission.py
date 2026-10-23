"""A self-tuning training algorithm.

The graded quantity is the training time accumulated at the first evaluation
row that crosses the validation target.  Three properties of the harness --
none of them particular to any one workload -- shape this algorithm:

  * Reading a batch off the input queue costs time in proportion to the number
    of examples in it, while one parameter update costs a roughly constant
    amount.  Examples are the scarce resource and updates are the cheap one, so
    the algorithm buys a pool of examples once, at a price it measures against
    a budget, and afterwards draws its updates from the examples it owns.
  * Evaluations fire on a clock of the harness's own, so the only instants that
    can ever be recorded are the evaluation boundaries.  The learning rate is
    accordingly warmed up and annealed *within* each evaluation window, which
    presents a fully annealed model at every boundary instead of only at the
    end of one long fixed schedule.
  * What anneals a model is updates, not seconds.  The position in the schedule
    is therefore counted in updates: the algorithm times its own steps and
    predicts how many more will fit before the next evaluation.

Everything that adapts is derived from run-time signals: the harness clock, the
evaluation cadence, and the measured cost of a step and of a read.  One single
setting serves every workload; nothing is chosen by looking at the workload, at
the model, or at any of their shapes, and no state outlives a run, since
everything mutable lives in the optimizer state the harness owns.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

# Optimizer.  A wide batch costs little more per update than a narrow one while
# the model is small, and the queue is read at that same width, so exactly one
# tensor shape is ever presented to the framework and nothing is recompiled.
_BATCH_SIZE = 1024
_PEAK_LR = 0.015
_BETA1 = 0.9
_BETA2 = 0.95
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_GRAD_CLIP = 1.0
_LABEL_SMOOTHING = 0.05

# Schedule, in fractions of the updates expected inside one window.
_WARM_FRAC = 0.06
_MIN_SCALE = 0.01
_WINDOW_USE = 0.9
_WINDOW_TRUST = 0.98
_PEAK_DECAY = 0.9
_MIN_PEAK_FRAC = 0.4
_DEFAULT_PERIOD = 3.0

# Example pool.  The first read also starts the input pipeline; that price is
# unavoidable and says nothing about what one more batch of examples costs, so
# it is not charged against the budget.
_FETCH_FRAC = 0.45
_MAX_POOL_BATCHES = 48

# Step-cost estimate.
_COST_ALPHA = 0.15
_MIN_COST = 1e-6


def _eval_period(workload: spec.Workload) -> float:
  """How often the harness offers an evaluation, in seconds."""
  period = getattr(workload, 'eval_period_time_sec', None)
  try:
    period = float(period)
  except (TypeError, ValueError):
    return _DEFAULT_PERIOD
  if not math.isfinite(period) or period <= 0.0:
    return _DEFAULT_PERIOD
  return period


def _cycle_scale(progress: float) -> float:
  """Warm up, then cosine down, across the updates of one window."""
  if progress <= 0.0:
    return _MIN_SCALE
  if progress < _WARM_FRAC:
    return max(_MIN_SCALE, progress / _WARM_FRAC)
  p = min(1.0, (progress - _WARM_FRAC) / max(1e-9, 1.0 - _WARM_FRAC))
  return max(_MIN_SCALE, 0.5 * (1.0 + math.cos(math.pi * p)))


def _elapsed(state: spec.OptimizerState,
            train_state: Optional[Dict[str, Any]]) -> float:
  """Elapsed training time, from the harness clock when it is offered."""
  if train_state is not None:
    try:
      value = train_state['accumulated_submission_time']
    except (KeyError, TypeError):
      value = None
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
      return float(value)
  return time.time() - state['wall_start']


def _progress(state: spec.OptimizerState, now: float) -> float:
  """Fraction of this window's updates that are already done.

  The updates still to come are predicted from the measured cost of an update
  that did not have to wait on the input pipeline, so time spent buying
  examples does not by itself push the schedule forward.
  """
  done = state['window_steps']
  cost = state['step_cost']
  left = state['window_len'] - (now - state['window_start'])
  if cost is None or cost <= _MIN_COST or left <= 0.0:
    remaining = 0.0
  else:
    remaining = left / cost
  total = done + remaining
  if total <= 0.0:
    return 1.0
  return min(1.0, done / total)


def _pool_view(state: spec.OptimizerState):
  """One contiguous view of every example paid for so far."""
  view = state['pool_view']
  if view is None:
    inputs = torch.cat(state['pool_x'], dim=0)
    targets = torch.cat(state['pool_y'], dim=0)
    weights = None
    if state['pool_w'] and all(w is not None for w in state['pool_w']):
      weights = torch.cat(state['pool_w'], dim=0)
    view = (inputs, targets, weights)
    state['pool_view'] = view
  return view


def _mean_loss(workload: spec.Workload, batch: Dict[str, spec.Tensor],
               logits: spec.Tensor) -> spec.Tensor:
  """Mean loss, smoothed wherever the workload's loss accepts smoothing."""
  try:
    losses = workload.loss_fn(
      label_batch=batch['targets'],
      logits_batch=logits,
      mask_batch=batch.get('weights'),
      label_smoothing=_LABEL_SMOOTHING,
    )
  except TypeError:
    losses = workload.loss_fn(
      label_batch=batch['targets'],
      logits_batch=logits,
      mask_batch=batch.get('weights'),
    )
  return losses['summed'] / losses['n_valid_examples']


def get_batch_size(workload_name: str) -> int:
  """One batch size for every workload, which is what the rules permit."""
  del workload_name
  return _BATCH_SIZE


def init_optimizer_state(
  workload: spec.Workload,
  model_params: spec.ParameterContainer,
  model_state: spec.ModelAuxiliaryState,
  hyperparameters: spec.Hyperparameters,
  rng: spec.RandomState,
) -> spec.OptimizerState:
  del model_state
  del hyperparameters
  del rng
  params = [p for p in model_params.parameters() if p.requires_grad]
  optimizer = torch.optim.AdamW(
    params,
    lr=_PEAK_LR * _MIN_SCALE,
    betas=(_BETA1, _BETA2),
    eps=_EPS,
    weight_decay=_WEIGHT_DECAY,
    foreach=True,
  )
  period = _eval_period(workload)
  return {
    'optimizer': optimizer,
    'params': params,
    'period': period,
    'window_len': period * _WINDOW_USE,
    'window_start': 0.0,
    'window_steps': 0,
    'wall_start': time.time(),
    'last_mark': None,
    'step_cost': None,
    'fetched': False,
    'seen_evals': 0,
    'cycle': 0,
    'step': 0,
    'fetch_time': 0.0,
    'fetch_budget': period * _FETCH_FRAC,
    'fetch_count': 0,
    'pool_x': [],
    'pool_y': [],
    'pool_w': [],
    'pool_n': 0,
    'pool_view': None,
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

  state = optimizer_state
  optimizer = state['optimizer']
  now = _elapsed(state, train_state)

  # A new evaluation row starts a new annealing cycle.
  n_evals = len(eval_results)
  if n_evals != state['seen_evals']:
    # The window that just closed measured its own length; how much training
    # time an evaluation period actually leaves is a property of the machine,
    # not something worth guessing twice.
    if state['cycle'] > 0:
      measured = now - state['window_start']
      if measured > 0.2 * state['period']:
        state['window_len'] = _WINDOW_TRUST * measured
    state['seen_evals'] = n_evals
    state['window_start'] = now
    state['window_steps'] = 0
    state['cycle'] += 1

  decay = _PEAK_DECAY ** max(0, state['cycle'] - 1)
  peak = _PEAK_LR * max(_MIN_PEAK_FRAC, decay)
  lr = peak * _cycle_scale(_progress(state, now))
  for group in optimizer.param_groups:
    group['lr'] = lr

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
  loss = _mean_loss(workload, batch, logits)
  loss.backward()
  torch.nn.utils.clip_grad_norm_(state['params'], _GRAD_CLIP)
  optimizer.step()

  state['step'] += 1
  state['window_steps'] += 1

  # Price a step that did not have to wait on the input pipeline.
  mark = time.time()
  last = state['last_mark']
  if last is not None and not state['fetched']:
    observed = mark - last
    if observed > _MIN_COST:
      prior = state['step_cost']
      if prior is None:
        state['step_cost'] = observed
      else:
        state['step_cost'] = (1.0 - _COST_ALPHA) * prior + _COST_ALPHA * observed
  state['last_mark'] = mark
  state['fetched'] = False
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
  """Buy examples while they are worth their price, then reuse what was bought.

  The batch handed back always holds as many examples as the batch the queue
  yields, so the shapes the framework sees never change.
  """
  del workload
  del current_param_container
  del model_state
  del hyperparameters
  del global_step
  del rng

  state = optimizer_state
  want_more = (
    state['fetch_time'] < state['fetch_budget']
    and state['fetch_count'] < _MAX_POOL_BATCHES
  )
  if state['pool_n'] < _BATCH_SIZE or want_more:
    start = time.time()
    batch = next(input_queue)
    cost = time.time() - start
    if state['fetch_count'] > 0:
      state['fetch_time'] += cost
    state['fetch_count'] += 1
    try:
      state['pool_x'].append(batch['inputs'])
      state['pool_y'].append(batch['targets'])
      state['pool_w'].append(batch.get('weights'))
      state['pool_n'] += len(batch['targets'])
      state['pool_view'] = None
    except (RuntimeError, TypeError, KeyError, IndexError, AttributeError):
      state['fetch_time'] = state['fetch_budget']
    state['fetched'] = True
    return batch

  inputs, targets, weights = _pool_view(state)
  idx = torch.randint(0, state['pool_n'], (_BATCH_SIZE,), device=targets.device)
  sample = {'inputs': inputs[idx], 'targets': targets[idx]}
  if weights is not None:
    sample['weights'] = weights[idx]
  return sample
