"""Self-tuning training algorithm for the AlgoPerf submission API.

One configuration for every workload: nothing is selected by workload name, nothing branches on a
model shape. The only run-time adaptation is the learning-rate schedule, which is anchored to the
harness's own evaluation clock (read from the workload's evaluation period and re-anchored on every
evaluation that is actually observed), so that the annealed end of each cosine cycle lands on an
evaluation whatever the hardware speed. Cycles restart on a geometrically growing horizon, so a
workload that needs far more training than the first cycle provides still gets repeated,
well-annealed chances to cross its target.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LR = 0.4
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1
_GRAD_CLIP = 2.0
_WARMUP_FRAC = 0.15
_MAX_WARMUP_SEC = 4.0
_LR_FLOOR_FRAC = 0.02
_CYCLE_LR_DECAY = 0.9
_MIN_PEAK_FRAC = 0.5
_DEFAULT_EVAL_PERIOD_SEC = 25.0
# Evaluation indices at which a cosine cycle ends. The harness evaluates on a fixed period, so these
# are 1, 2, 3, 5, 9, ... periods of training: a short first cycle for an early crossing, then
# doubling horizons for anything that needs much longer to converge.
_CYCLE_BOUNDARIES = (1, 2, 3, 5, 9, 17, 33, 65, 129)
# Fallback clock only: a gap longer than this between two training steps is an untimed evaluation,
# which the harness does not charge to the submission.
_MAX_CHARGED_STEP_SEC = 2.0


def _unwrap(module: Any) -> Any:
    """Return the eager module underneath a graph-compilation wrapper, if there is one."""
    inner = getattr(module, '_orig_mod', None)
    return module if inner is None else inner


def _eval_period(workload: spec.Workload) -> float:
    period = getattr(workload, 'eval_period_time_sec', None)
    if period is None:
        return _DEFAULT_EVAL_PERIOD_SEC
    period = float(period)
    return period if period > 0.0 else _DEFAULT_EVAL_PERIOD_SEC


def _cycle_window(
    evals_seen: int, last_eval_elapsed: float, period: float
) -> Tuple[int, float, float]:
    """The cosine cycle containing the present moment, as (index, start, end) in charged seconds."""
    if evals_seen <= 0:
        return 0, 0.0, period
    started = _CYCLE_BOUNDARIES[0]
    index = 0
    for position, boundary in enumerate(_CYCLE_BOUNDARIES):
        if boundary <= evals_seen:
            started = boundary
            index = position
        else:
            ends = boundary
            break
    else:
        ends = evals_seen + 1
    start = last_eval_elapsed - (evals_seen - started) * period
    return index, start, last_eval_elapsed + (ends - evals_seen) * period


def _learning_rate(
    elapsed: float, evals_seen: int, last_eval_elapsed: float, period: float
) -> float:
    index, start, end = _cycle_window(evals_seen, last_eval_elapsed, period)
    span = end - start
    if span <= 0.0:
        return _PEAK_LR * _LR_FLOOR_FRAC
    frac = (elapsed - start) / span
    frac = 0.0 if frac < 0.0 else (1.0 if frac > 1.0 else frac)
    decay = _CYCLE_LR_DECAY**index
    peak = _PEAK_LR * (decay if decay > _MIN_PEAK_FRAC else _MIN_PEAK_FRAC)
    warmup = min(_WARMUP_FRAC, _MAX_WARMUP_SEC / span)
    if frac < warmup:
        scale = _LR_FLOOR_FRAC + (1.0 - _LR_FLOOR_FRAC) * (frac / warmup)
    else:
        progress = (frac - warmup) / (1.0 - warmup)
        scale = _LR_FLOOR_FRAC + (1.0 - _LR_FLOOR_FRAC) * 0.5 * (
            1.0 + math.cos(math.pi * progress)
        )
    return peak * scale


def _elapsed_seconds(
    optimizer_state: spec.OptimizerState, train_state: Optional[Dict[str, Any]]
) -> float:
    """Training time as the harness charges it, with a self-maintained fallback."""
    if train_state is not None and 'accumulated_submission_time' in train_state:
        return float(train_state['accumulated_submission_time'])
    now = time.monotonic()
    last = optimizer_state['last_step_time']
    if last is not None:
        delta = now - last
        optimizer_state['elapsed'] += delta if delta < _MAX_CHARGED_STEP_SEC else 0.0
    optimizer_state['last_step_time'] = now
    return optimizer_state['elapsed']


def get_batch_size(workload_name: str) -> int:
    """A single batch size for every workload, as the self-tuning rules allow."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov momentum, weight decay on matrix-shaped parameters only, clock-driven schedule."""
    del model_state
    del hyperparameters
    del rng

    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True

    decayed = []
    undecayed = []
    for parameter in _unwrap(model_params).parameters():
        if not parameter.requires_grad:
            continue
        # A generic property of the tensor, not of any particular model: kernels and matrices are
        # regularised, vectors (biases, normalisation scales) are not.
        if parameter.ndim > 1:
            decayed.append(parameter)
        else:
            undecayed.append(parameter)

    optimizer = torch.optim.SGD(
        [
            {'params': decayed, 'weight_decay': _WEIGHT_DECAY},
            {'params': undecayed, 'weight_decay': 0.0},
        ],
        lr=_PEAK_LR * _LR_FLOOR_FRAC,
        momentum=_MOMENTUM,
        nesterov=True,
    )
    return {
        'optimizer': optimizer,
        'elapsed': 0.0,
        'last_step_time': None,
        'last_eval_elapsed': 0.0,
        'evals_seen': 0,
        'period': _eval_period(workload),
        'use_bf16': torch.cuda.is_available() and torch.cuda.is_bf16_supported(),
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
    """One training step at the schedule's current learning rate."""
    unused = (current_params_types, hyperparameters, loss_type, global_step)
    del unused

    elapsed = _elapsed_seconds(optimizer_state, train_state)
    seen = len(eval_results)
    if seen > optimizer_state['evals_seen']:
        # An evaluation just fired, and evaluation time is not charged, so the present clock
        # reading is where that evaluation sits. Re-anchor the schedule on it.
        optimizer_state['evals_seen'] = seen
        optimizer_state['last_eval_elapsed'] = elapsed

    optimizer = optimizer_state['optimizer']
    learning_rate = _learning_rate(
        elapsed,
        optimizer_state['evals_seen'],
        optimizer_state['last_eval_elapsed'],
        optimizer_state['period'],
    )
    for group in optimizer.param_groups:
        group['lr'] = learning_rate

    model = _unwrap(current_param_container)
    model.train()
    optimizer.zero_grad(set_to_none=True)

    if optimizer_state['use_bf16']:
        context = torch.autocast(device_type='cuda', dtype=torch.bfloat16)
    else:
        context = torch.autocast(device_type='cpu', enabled=False)
    with context:
        logits, next_model_state = workload.model_fn(
            params=model,
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
    mean_loss = losses['summed'] / losses['n_valid_examples']
    mean_loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), _GRAD_CLIP)
    optimizer.step()

    return optimizer_state, model, next_model_state


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
    unused = (
        workload,
        optimizer_state,
        current_param_container,
        model_state,
        hyperparameters,
        global_step,
        rng,
    )
    del unused
    return next(input_queue)
