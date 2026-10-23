"""Self-tuning training algorithm: warmup + decayed Adam with a bias-corrected
parameter average evaluated at eval time.

A single fixed configuration is used for every workload, as the self-tuning
ruleset requires. No workload identification, no model fingerprinting.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_LR = 0.010
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 20
_DECAY_STEPS = 2000
_FINAL_LR_FRAC = 0.2
_EMA_DECAY = 0.99
_GRAD_CLIP = 1.0


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def _lr_at(step: int) -> float:
    if step < _WARMUP_STEPS:
        return _LR * float(step + 1) / float(_WARMUP_STEPS)
    progress = float(step - _WARMUP_STEPS) / float(_DECAY_STEPS)
    if progress > 1.0:
        progress = 1.0
    return _LR * (1.0 - (1.0 - _FINAL_LR_FRAC) * progress)


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
    optimizer = torch.optim.Adam(
        params,
        lr=_LR,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
    )
    ema = [torch.zeros_like(p, memory_format=torch.preserve_format) for p in params]
    backup = [torch.zeros_like(p, memory_format=torch.preserve_format) for p in params]
    return {
        'optimizer': optimizer,
        'params': params,
        'ema': ema,
        'backup': backup,
        'ema_weight': 0.0,
        'step': 0,
        'swapped': False,
    }


def _restore_if_swapped(optimizer_state: spec.OptimizerState) -> None:
    if optimizer_state['swapped']:
        with torch.no_grad():
            for p, b in zip(optimizer_state['params'], optimizer_state['backup']):
                p.copy_(b)
        optimizer_state['swapped'] = False


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
    unused = (current_params_types, hyperparameters, loss_type, eval_results, train_state)
    del unused

    _restore_if_swapped(optimizer_state)

    optimizer = optimizer_state['optimizer']
    step = optimizer_state['step']
    lr = _lr_at(step)
    for group in optimizer.param_groups:
        group['lr'] = lr

    current_param_container.train()
    for p in optimizer_state['params']:
        p.grad = None

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
    loss = losses['summed'] / losses['n_valid_examples']
    loss.backward()
    optimizer.step()

    with torch.no_grad():
        torch._foreach_mul_(optimizer_state['ema'], _EMA_DECAY)
        torch._foreach_add_(optimizer_state['ema'], optimizer_state['params'],
                            alpha=1.0 - _EMA_DECAY)
    optimizer_state['ema_weight'] = (
        optimizer_state['ema_weight'] * _EMA_DECAY + (1.0 - _EMA_DECAY)
    )
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
    unused = (workload, current_params_types, hyperparameters, loss_type,
              eval_results, global_step, rng)
    del unused
    w = optimizer_state['ema_weight']
    if w > 0.0 and not optimizer_state['swapped']:
        with torch.no_grad():
            for p, b, e in zip(optimizer_state['params'],
                               optimizer_state['backup'],
                               optimizer_state['ema']):
                b.copy_(p)
                p.copy_(e / w)
        optimizer_state['swapped'] = True
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
    unused = (workload, optimizer_state, current_param_container, model_state,
              hyperparameters, global_step, rng)
    del unused
    return next(input_queue)
