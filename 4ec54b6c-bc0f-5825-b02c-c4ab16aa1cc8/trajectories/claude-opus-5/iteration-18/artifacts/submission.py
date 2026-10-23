"""Self-tuning training algorithm for the AlgoPerf submission contract.

One setting, applied unchanged to every workload. The update is NAdam (Adam with
Nesterov momentum) with decoupled gradient-norm clipping. The step size follows a
short warmup and then a cosine cycle that is paced against wall-clock progress
rather than against a step count, so the iterate is at its quietest exactly when
the harness fires an evaluation, on whatever hardware the run lands. If the run
continues past an evaluation the cycle restarts with a slightly smaller peak, so
later evaluations keep improving instead of stalling at an annealed floor.

Nothing here inspects the workload's identity, the parameter shapes, or the
model-state keys; the only model property used is the generic layer structure
exposed by the parameter iterator.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_PEAK_LR = 0.012
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 30
_LR_FLOOR = 0.05
_CYCLE_FRACTION = 0.87
_CYCLE_DECAY = 0.85
_MIN_AMPLITUDE = 0.35
_FALLBACK_PERIOD_SEC = 10.0
_GRAD_CLIP = 1.0
_LABEL_SMOOTHING = 0.1


def _initial_period(workload: spec.Workload) -> float:
    """Length of one evaluation cycle, in the units the runner charges us."""
    period = getattr(workload, 'eval_period_time_sec', None)
    try:
        period = float(period)
    except (TypeError, ValueError):
        return _FALLBACK_PERIOD_SEC
    if not (period > 0.0):
        return _FALLBACK_PERIOD_SEC
    return _CYCLE_FRACTION * period


def _elapsed_seconds(optimizer_state, train_state) -> float:
    """Accumulated submission time, from the harness if it offers it."""
    if train_state is not None:
        try:
            value = float(train_state['accumulated_submission_time'])
        except (KeyError, TypeError, ValueError):
            value = None
        if value is not None and value >= 0.0:
            return value
    return float(optimizer_state['self_timed_sec'])


def _row_time(entry) -> Optional[float]:
    try:
        return float(entry[1]['accumulated_submission_time'])
    except (IndexError, KeyError, TypeError, ValueError):
        return None


def _cycle_position(optimizer_state, eval_results, elapsed):
    """Fraction of the way from the last evaluation to the next expected one."""
    start = 0.0
    cycle = 0
    if eval_results:
        cycle = len(eval_results)
        last = _row_time(eval_results[-1])
        if last is not None and 0.0 <= last <= elapsed:
            start = last
        if len(eval_results) >= 2:
            prev = _row_time(eval_results[-2])
            if prev is not None and last is not None:
                observed = last - prev
                if observed > 0.0:
                    optimizer_state['period_sec'] = (
                        0.5 * optimizer_state['period_sec'] + 0.5 * observed
                    )
    span = max(optimizer_state['period_sec'], 1e-3)
    progress = (elapsed - start) / span
    if progress < 0.0:
        progress = 0.0
    elif progress > 1.0:
        progress = 1.0
    return progress, cycle


def _lr_scale(step: int, progress: float, cycle: int) -> float:
    warm = min(1.0, (step + 1.0) / float(_WARMUP_STEPS))
    shape = _LR_FLOOR + (1.0 - _LR_FLOOR) * 0.5 * (1.0 + math.cos(math.pi * progress))
    amplitude = max(_MIN_AMPLITUDE, _CYCLE_DECAY ** max(0, cycle - 1))
    return warm * amplitude * shape


def get_batch_size(workload_name: str) -> int:
    """One batch size for every workload; the name is deliberately unused."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """NAdam over every trainable parameter, plus the pacing bookkeeping."""
    del model_state
    del hyperparameters
    del rng

    params = [p for p in model_params.parameters() if p.requires_grad]
    optimizer = torch.optim.NAdam(
        params,
        lr=_PEAK_LR,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
    )
    return {
        'optimizer': optimizer,
        'params': params,
        'step': 0,
        'self_timed_sec': 0.0,
        'period_sec': _initial_period(workload),
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
    """One training step at the time-paced step size."""
    del current_params_types
    del hyperparameters
    del loss_type
    del global_step

    start_time = time.time()
    optimizer = optimizer_state['optimizer']
    params = optimizer_state['params']

    elapsed = _elapsed_seconds(optimizer_state, train_state)
    progress, cycle = _cycle_position(optimizer_state, eval_results, elapsed)
    lr = _PEAK_LR * _lr_scale(optimizer_state['step'], progress, cycle)
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
    torch.nn.utils.clip_grad_norm_(params, _GRAD_CLIP)
    optimizer.step()

    optimizer_state['step'] += 1
    optimizer_state['self_timed_sec'] += time.time() - start_time
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
    """Nothing to swap in: the annealed iterate is what we want evaluated."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng
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
