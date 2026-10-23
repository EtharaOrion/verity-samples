"""Self-tuning submission: AdamW with warmup, time-aware decay and Polyak-averaged evaluation."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_PEAK_LR = 0.010
_WARMUP_STEPS = 30
_DECAY_FRACTION = 0.30
_LR_FLOOR = 0.05
_EMA_DECAY = 0.995
_WEIGHT_DECAY = 1e-4
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_CLIP = 0.0
_LABEL_SMOOTHING = 0.05
_STEP_HORIZON = 4000.0


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def _progress(step: int, elapsed: Optional[float], horizon: Optional[float]) -> float:
    p = float(step) / _STEP_HORIZON
    if elapsed is not None and horizon is not None and horizon > 0.0:
        p = max(p, float(elapsed) / horizon)
    return min(1.0, max(0.0, p))


def _lr_at(step: int, progress: float) -> float:
    if step < _WARMUP_STEPS:
        return _PEAK_LR * float(step + 1) / float(_WARMUP_STEPS)
    cos = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _PEAK_LR * (_LR_FLOOR + (1.0 - _LR_FLOOR) * cos)


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    del model_state, hyperparameters, rng
    params = [p for p in model_params.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(
        params,
        lr=_PEAK_LR,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
        foreach=True,
    )
    horizon = None
    runtime = getattr(workload, 'max_allowed_runtime_sec', None)
    if isinstance(runtime, (int, float)) and runtime > 0:
        horizon = _DECAY_FRACTION * float(runtime)
    return {
        'optimizer': optimizer,
        'step': 0,
        'params': params,
        'ema': [p.detach().clone() for p in params],
        'backup': None,
        'horizon': horizon,
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
    del current_params_types, hyperparameters, eval_results, loss_type

    opt = optimizer_state['optimizer']
    params = optimizer_state['params']
    ema = optimizer_state['ema']

    backup = optimizer_state['backup']
    if backup is not None:
        with torch.no_grad():
            torch._foreach_copy_(params, backup)
        optimizer_state['backup'] = None

    elapsed = None
    if train_state is not None:
        elapsed = train_state.get('accumulated_submission_time', None)
    progress = _progress(global_step, elapsed, optimizer_state['horizon'])
    lr = _lr_at(global_step, progress)
    for group in opt.param_groups:
        group['lr'] = lr

    model = current_param_container
    model.train()
    for p in params:
        p.grad = None

    logits, next_state = workload.model_fn(
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
    if _CLIP > 0.0:
        torch.nn.utils.clip_grad_norm_(params, _CLIP)
    opt.step()

    t = optimizer_state['step'] + 1
    optimizer_state['step'] = t
    decay = min(_EMA_DECAY, float(1 + t) / float(10 + t))
    with torch.no_grad():
        torch._foreach_mul_(ema, decay)
        torch._foreach_add_(ema, params, alpha=1.0 - decay)
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
    del workload, current_params_types, hyperparameters, loss_type
    del eval_results, global_step, rng
    params = optimizer_state['params']
    ema = optimizer_state['ema']
    if optimizer_state['step'] > 0 and optimizer_state['backup'] is None:
        with torch.no_grad():
            optimizer_state['backup'] = [p.detach().clone() for p in params]
            torch._foreach_copy_(params, ema)
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
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
