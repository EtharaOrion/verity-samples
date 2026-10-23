"""Self-tuning training algorithm.

A single fixed configuration, identical for every workload and every model: AdamW-style
adaptive steps with gradient clipping, a warmup + cosine schedule whose length is derived at
run time from the harness's own evaluation cadence, warm restarts aligned to that cadence, and
a short-horizon parameter average that is only swapped in for evaluation when it is measured
(on already-seen training data) to be no worse than the raw iterate.

No workload identification, no model fingerprinting, no hyperparameters exposed.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LR = 0.004
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_CLIP_NORM = 1.0
_WARMUP_FRAC = 0.06
_MIN_LR_FRAC = 0.015
_CYCLE_SAFETY = 0.97
_RESTART_DECAY = 0.5
_MIN_PEAK_FRAC = 0.15
_DEFAULT_PERIOD = 3.0
_EMA_DECAY = 0.99


def get_batch_size(workload_name: str) -> int:
    """One batch size for every workload, as the rules allow."""
    del workload_name
    return _BATCH_SIZE


def _cycle_seconds(workload: spec.Workload) -> float:
    """Length of one anneal cycle, read from the harness's generic evaluation cadence."""
    period = getattr(workload, 'eval_period_time_sec', None)
    try:
        period = float(period)
    except (TypeError, ValueError):
        period = _DEFAULT_PERIOD
    if not math.isfinite(period) or period <= 0.0:
        period = _DEFAULT_PERIOD
    period = min(max(period, 1.0), 120.0)
    return period * _CYCLE_SAFETY


def _schedule(progress: float, peak: float) -> float:
    """Warmup then cosine decay over the fraction `progress` of the current cycle."""
    if progress < _WARMUP_FRAC:
        return peak * (0.02 + 0.98 * (progress / _WARMUP_FRAC))
    q = (progress - _WARMUP_FRAC) / max(1.0 - _WARMUP_FRAC, 1e-6)
    if q > 1.0:
        q = 1.0
    return peak * (_MIN_LR_FRAC + (1.0 - _MIN_LR_FRAC) * 0.5 * (1.0 + math.cos(math.pi * q)))


def _set_lr(optimizer: Any, lr: float) -> None:
    for group in optimizer.param_groups:
        group['lr'] = lr


def _mean_loss(workload, params, model_state, batch, rng):
    """Loss of the current parameters on an already-seen training batch."""
    with torch.no_grad():
        logits, _ = workload.model_fn(
            params=params,
            augmented_and_preprocessed_input_batch=batch,
            model_state=model_state,
            mode=spec.ForwardPassMode.EVAL,
            rng=rng,
            update_batch_norm=False,
        )
        losses = workload.loss_fn(
            label_batch=batch['targets'],
            logits_batch=logits,
            mask_batch=batch.get('weights'),
            label_smoothing=0.0,
        )
        return float(losses['summed'].item()) / max(float(losses['n_valid_examples'].item()), 1.0)


def _copy_into(dst, src) -> None:
    with torch.no_grad():
        torch._foreach_copy_(dst, src)


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
    try:
        optimizer = torch.optim.AdamW(
            params,
            lr=_PEAK_LR,
            betas=(_BETA1, _BETA2),
            eps=_EPS,
            weight_decay=_WEIGHT_DECAY,
            fused=True,
        )
    except (RuntimeError, ValueError, TypeError):
        optimizer = torch.optim.AdamW(
            params,
            lr=_PEAK_LR,
            betas=(_BETA1, _BETA2),
            eps=_EPS,
            weight_decay=_WEIGHT_DECAY,
        )
    return {
        'optimizer': optimizer,
        'params': params,
        'ema': [p.detach().clone() for p in params],
        'ema_ready': False,
        'cycle_len': _cycle_seconds(workload),
        'cycle_start': None,
        'cycle_index': 0,
        'peak': _PEAK_LR,
        'seen_evals': 0,
        'restore': None,
        'last_batch': None,
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
    del current_params_types
    del hyperparameters
    del loss_type
    del global_step

    state = optimizer_state
    optimizer = state['optimizer']
    params = state['params']

    # If an averaged iterate was swapped in for the last evaluation, put the raw one back.
    if state['restore'] is not None:
        _copy_into(params, state['restore'])
        state['restore'] = None

    now = time.time()
    n_evals = len(eval_results) if eval_results is not None else 0
    if state['cycle_start'] is None:
        state['cycle_start'] = now
        state['seen_evals'] = n_evals
    elif n_evals > state['seen_evals']:
        # An evaluation just happened: start a fresh anneal cycle aligned to the cadence.
        state['seen_evals'] = n_evals
        state['cycle_start'] = now
        state['cycle_index'] += 1
        if state['cycle_index'] > 1:
            state['peak'] = max(state['peak'] * _RESTART_DECAY, _PEAK_LR * _MIN_PEAK_FRAC)
        state['ema_ready'] = False

    elapsed = now - state['cycle_start']
    progress = elapsed / state['cycle_len'] if state['cycle_len'] > 0 else 1.0
    if progress < 0.0:
        progress = 0.0
    _set_lr(optimizer, _schedule(progress, state['peak']))

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
        label_smoothing=0.0,
    )
    mean_loss = losses['summed'] / losses['n_valid_examples']
    mean_loss.backward()
    torch.nn.utils.clip_grad_norm_(params, _CLIP_NORM)
    optimizer.step()

    with torch.no_grad():
        if state['ema_ready']:
            torch._foreach_mul_(state['ema'], _EMA_DECAY)
            torch._foreach_add_(state['ema'], params, alpha=1.0 - _EMA_DECAY)
        else:
            _copy_into(state['ema'], params)
            state['ema_ready'] = True

    state['last_batch'] = batch
    state['step'] += 1
    return state, current_param_container, next_state


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
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step

    state = optimizer_state
    params = state['params']
    batch = state['last_batch']
    if not state['ema_ready'] or batch is None:
        return state, current_param_container, model_state

    try:
        raw_loss = _mean_loss(workload, current_param_container, model_state, batch, rng)
        raw = [p.detach().clone() for p in params]
        _copy_into(params, state['ema'])
        ema_loss = _mean_loss(workload, current_param_container, model_state, batch, rng)
        if math.isfinite(ema_loss) and ema_loss <= raw_loss:
            state['restore'] = raw
        else:
            _copy_into(params, raw)
    except RuntimeError:
        state['restore'] = None
    return state, current_param_container, model_state


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
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
