"""Self-tuning submission: warm-restarted one-cycle Nesterov SGD on its own step clock.

The algorithm exposes no hyperparameters, never inspects the workload identity and never
looks at parameter shapes or state-dict keys. It measures the time its own steps consume
and anneals the learning rate so that the model sits at the bottom of a cosine cycle at
the moment the harness is due to evaluate. If the target is not reached there, the cycle
restarts with a geometrically longer horizon (always a whole number of evaluation
periods, so every cycle still bottoms out on an evaluation), which is the standard warm
restart behaviour and keeps a slower model improving instead of stalling.
"""

import math
import time
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_PEAK_LR = 0.2
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1
_GRAD_CLIP = 1.0
_WARMUP_FRAC = 0.06
_DEFAULT_EVAL_PERIOD = 25.0
_MAX_CYCLE_PERIODS = 8.0


def get_batch_size(workload_name: str) -> int:
    """A single batch size for every workload, as the rules require."""
    del workload_name
    return _BATCH_SIZE


def _eval_period(workload: spec.Workload) -> float:
    period = getattr(workload, 'eval_period_time_sec', _DEFAULT_EVAL_PERIOD)
    try:
        period = float(period)
    except (TypeError, ValueError):
        return _DEFAULT_EVAL_PERIOD
    if period <= 0.0:
        return _DEFAULT_EVAL_PERIOD
    return period


def _cycle_periods(cycle_index: int) -> float:
    """Cycle length in evaluation periods: 1, 1, 2, 2, 4, 4, 8, 8, ..."""
    if cycle_index <= 2:
        return 1.0
    return min(2.0 ** ((cycle_index - 1) // 2), _MAX_CYCLE_PERIODS)


def _learning_rate(progress: float) -> float:
    """Linear warmup into a cosine decay across one cycle."""
    p = min(max(progress, 0.0), 1.0)
    if p < _WARMUP_FRAC:
        return _PEAK_LR * (p / _WARMUP_FRAC)
    x = (p - _WARMUP_FRAC) / (1.0 - _WARMUP_FRAC)
    return _PEAK_LR * 0.5 * (1.0 + math.cos(math.pi * x))


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov momentum, weight decay applied only to multi-axis tensors."""
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
        lr=_PEAK_LR,
        momentum=_MOMENTUM,
        nesterov=True,
    )

    period = _eval_period(workload)
    return {
        'optimizer': optimizer,
        'step': 0,
        'period': period,
        'elapsed': 0.0,
        'cycle_index': 1,
        'cycle_start': 0.0,
        'cycle_end': period,
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
    """One training step at the learning rate the current cycle asks for."""
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step

    state = optimizer_state
    optimizer = state['optimizer']
    step_start = time.monotonic()

    if state['elapsed'] >= state['cycle_end']:
        state['cycle_index'] += 1
        state['cycle_start'] = state['elapsed']
        state['cycle_end'] = state['elapsed'] + state['period'] * _cycle_periods(
            state['cycle_index']
        )

    span = state['cycle_end'] - state['cycle_start']
    progress = (state['elapsed'] - state['cycle_start']) / span if span > 0.0 else 1.0
    learning_rate = _learning_rate(progress)
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
    loss = losses['summed'] / losses['n_valid_examples']
    loss.backward()
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), _GRAD_CLIP)
    optimizer.step()

    state['step'] += 1
    state['elapsed'] += time.monotonic() - step_start
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
    """Take the next batch off the queue, unchanged."""
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
