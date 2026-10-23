"""Self-tuning submission: AdamW with short warmup, cosine decay to a floor, and an EMA of the weights.

No workload identification, no model fingerprinting, a single fixed setting for every workload.
"""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 192
_PEAK_LR = 0.008
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 40
_DECAY_STEPS = 2500
_LR_FLOOR = 0.05
_EMA_DECAY = 0.998


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def _learning_rate(step: int) -> float:
    if step < _WARMUP_STEPS:
        return _PEAK_LR * float(step + 1) / float(_WARMUP_STEPS)
    progress = min(1.0, float(step - _WARMUP_STEPS) / float(max(1, _DECAY_STEPS)))
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _PEAK_LR * (_LR_FLOOR + (1.0 - _LR_FLOOR) * cosine)


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    del workload
    del model_state
    del hyperparameters
    del rng
    params = [p for p in model_params.parameters() if p.requires_grad]
    try:
        optimizer = torch.optim.AdamW(
            params, lr=_PEAK_LR, betas=(_BETA1, _BETA2), eps=_EPS,
            weight_decay=_WEIGHT_DECAY, fused=True)
    except (RuntimeError, ValueError, TypeError):
        optimizer = torch.optim.AdamW(
            params, lr=_PEAK_LR, betas=(_BETA1, _BETA2), eps=_EPS,
            weight_decay=_WEIGHT_DECAY)
    return {
        'optimizer': optimizer,
        'params': params,
        'ema': [p.detach().clone() for p in params],
        'backup': None,
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
) -> spec.UpdateReturn:
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del train_state

    optimizer = optimizer_state['optimizer']
    params = optimizer_state['params']

    backup = optimizer_state['backup']
    if backup is not None:
        with torch.no_grad():
            for p, b in zip(params, backup):
                p.copy_(b)
        optimizer_state['backup'] = None

    lr = _learning_rate(optimizer_state['step'])
    for group in optimizer.param_groups:
        group['lr'] = lr

    current_param_container.train()
    for p in params:
        p.grad = None

    logits, new_model_state = workload.model_fn(
        params=current_param_container,
        augmented_and_preprocessed_input_batch=batch,
        model_state=model_state,
        mode=spec.ForwardPassMode.TRAIN,
        rng=rng,
        update_batch_norm=True,
    )
    loss_dict = workload.loss_fn(
        label_batch=batch['targets'],
        logits_batch=logits,
        mask_batch=batch.get('weights'),
        label_smoothing=0.0,
    )
    loss = loss_dict['summed'] / loss_dict['n_valid_examples']
    loss.backward()
    optimizer.step()

    step = optimizer_state['step'] + 1
    optimizer_state['step'] = step
    decay = min(_EMA_DECAY, (1.0 + step) / (10.0 + step))
    with torch.no_grad():
        for e, p in zip(optimizer_state['ema'], params):
            e.lerp_(p.detach(), 1.0 - decay)

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
) -> spec.UpdateReturn:
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng
    params = optimizer_state['params']
    if optimizer_state['step'] > 0:
        optimizer_state['backup'] = [p.detach().clone() for p in params]
        with torch.no_grad():
            for p, e in zip(params, optimizer_state['ema']):
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
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
