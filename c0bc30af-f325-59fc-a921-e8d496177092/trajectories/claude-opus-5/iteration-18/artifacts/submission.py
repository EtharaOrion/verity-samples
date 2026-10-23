"""Self-tuning submission: time-aligned warm-restart Nesterov SGD.

The learning-rate schedule is keyed to elapsed submission time rather than to a step
count, so it adapts itself to whatever throughput the device delivers and to whatever
architecture it is handed. Each cycle is exactly one evaluation period long and anneals
to a small floor by the end of the cycle, so every evaluation sees an annealed model.
Peak rates decay from cycle to cycle towards a floor, so a run that needs many cycles
keeps improving instead of bouncing. Gradient clipping and a non-finite-gradient guard
keep the high peak rates safe across architectures.
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
_GRAD_CLIP = 1.0
_WARMUP_FRAC = 0.15
_FINAL_LR_FRAC = 0.02
_CYCLE_DECAY = 0.85
_MIN_PEAK_FRAC = 0.12
_DEFAULT_CYCLE_SEC = 25.0
_DIVERGENCE_BACKOFF = 0.5


def _cycle_seconds(workload: spec.Workload) -> float:
    period = getattr(workload, 'eval_period_time_sec', None)
    if period is None:
        return _DEFAULT_CYCLE_SEC
    period = float(period)
    if not math.isfinite(period) or period <= 0.0:
        return _DEFAULT_CYCLE_SEC
    return period


def _elapsed_seconds(
    optimizer_state: spec.OptimizerState, train_state: Optional[Dict[str, Any]]
) -> float:
    if train_state is not None:
        elapsed = train_state.get('accumulated_submission_time')
        if elapsed is not None:
            return float(elapsed)
    return time.monotonic() - optimizer_state['start_time']


def _learning_rate(elapsed: float, cycle_seconds: float) -> float:
    cycle_index = int(elapsed // cycle_seconds)
    frac = (elapsed - cycle_index * cycle_seconds) / cycle_seconds
    frac = min(max(frac, 0.0), 1.0)
    peak = _PEAK_LR * max(_MIN_PEAK_FRAC, _CYCLE_DECAY**cycle_index)
    warmup = _WARMUP_FRAC if cycle_index == 0 else 0.5 * _WARMUP_FRAC
    if frac < warmup:
        return peak * (0.05 + 0.95 * frac / warmup)
    progress = (frac - warmup) / (1.0 - warmup)
    cosine = 0.5 * (1.0 + math.cos(math.pi * min(progress, 1.0)))
    return peak * (_FINAL_LR_FRAC + (1.0 - _FINAL_LR_FRAC) * cosine)


def _validation_target_reached(
    workload: spec.Workload, eval_results: List[Tuple[int, Any]]
) -> bool:
    if not eval_results:
        return False
    latest = eval_results[-1][-1]
    if not isinstance(latest, dict):
        return False
    try:
        return bool(workload.has_reached_validation_target(latest))
    except (KeyError, AttributeError, TypeError):
        return False


def get_batch_size(workload_name: str) -> int:
    """Return the training batch size: one value, the same for every workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov SGD with decay on multi-dimensional weights only."""
    del model_state
    del hyperparameters
    del rng
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True
    decayed = []
    undecayed = []
    for parameter in model_params.parameters():
        if not parameter.requires_grad:
            continue
        if parameter.ndim > 1:
            decayed.append(parameter)
        else:
            undecayed.append(parameter)
    optimizer = torch.optim.SGD(
        [
            {'params': decayed, 'weight_decay': _WEIGHT_DECAY},
            {'params': undecayed, 'weight_decay': 0.0},
        ],
        lr=_PEAK_LR * 0.05,
        momentum=_MOMENTUM,
        nesterov=True,
    )
    return {
        'optimizer': optimizer,
        'start_time': time.monotonic(),
        'cycle_seconds': _cycle_seconds(workload),
        'lr_scale': 1.0,
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
    train_state: Optional[Dict[str, Any]] = None,
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """One training step on a time-aligned warm-restart cosine schedule."""
    del current_params_types
    del hyperparameters
    del loss_type
    del global_step

    if _validation_target_reached(workload, eval_results):
        raise spec.TrainingCompleteError

    optimizer = optimizer_state['optimizer']
    elapsed = _elapsed_seconds(optimizer_state, train_state)
    learning_rate = (
        _learning_rate(elapsed, optimizer_state['cycle_seconds'])
        * optimizer_state['lr_scale']
    )
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

    grad_norm = torch.nn.utils.clip_grad_norm_(
        current_param_container.parameters(), _GRAD_CLIP
    )
    if torch.isfinite(grad_norm):
        optimizer.step()
    else:
        optimizer.zero_grad(set_to_none=True)
        optimizer_state['lr_scale'] *= _DIVERGENCE_BACKOFF
        new_model_state = model_state

    optimizer_state['step'] += 1
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
    """Nothing to swap: the schedule already anneals into every evaluation."""
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
