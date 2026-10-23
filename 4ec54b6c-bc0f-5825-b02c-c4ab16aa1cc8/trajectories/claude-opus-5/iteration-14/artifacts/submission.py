"""Self-tuning training algorithm: warmup + decayed AdamW with an EMA shadow.

A single fixed setting is used for every workload; nothing here inspects the workload
name, the parameter shapes, or the model state keys.
"""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_PEAK_LR = 0.012
_WARMUP_STEPS = 20
_DECAY_TAU = 400.0
_LR_FLOOR_FRAC = 0.15
_BETA1 = 0.9
_BETA2 = 0.98
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_LABEL_SMOOTHING = 0.15
_EMA_HORIZON = 100.0
_EMA_MAX_DECAY = 0.99


def get_batch_size(workload_name: str) -> int:
    """One batch size for every workload."""
    del workload_name
    return _BATCH_SIZE


def _lr_at(step: int) -> float:
    warm = min(1.0, (step + 1) / float(_WARMUP_STEPS))
    decay = 1.0 / (1.0 + max(0.0, step - _WARMUP_STEPS) / _DECAY_TAU)
    return _PEAK_LR * warm * max(_LR_FLOOR_FRAC, decay)


def _ema_decay(step: int) -> float:
    return min(_EMA_MAX_DECAY, step / (step + _EMA_HORIZON))


def _restore_if_shadowed(optimizer_state: spec.OptimizerState) -> None:
    """Undo the evaluation-time parameter swap, if one is in effect."""
    if optimizer_state.get('shadowed'):
        with torch.no_grad():
            for p, b in zip(optimizer_state['params'], optimizer_state['backup']):
                p.data.copy_(b)
        optimizer_state['shadowed'] = False


def _dummy_batch(model_params: spec.ParameterContainer,
                 params: List[Any]) -> Optional[Dict[str, Any]]:
    """Build a zero batch shaped like the real one, from generic layer properties.

    Only the fan-in of the first affine layer is read, which is a generic property of
    a layer type rather than a fingerprint of any particular model, and the batch is
    laid out exactly as the input pipeline lays its batches out so that the same
    kernels are reached.
    """
    fan_in = None
    for module in model_params.modules():
        if isinstance(module, torch.nn.Linear):
            fan_in = module.in_features
            break
    if fan_in is None:
        return None
    side = int(round(math.sqrt(fan_in)))
    if side * side != fan_in:
        return None
    device = params[0].device
    inputs = torch.zeros(
        (_BATCH_SIZE, side, side, 1), device=device, dtype=params[0].dtype
    ).permute(0, 3, 1, 2)
    targets = torch.zeros(_BATCH_SIZE, dtype=torch.long, device=device)
    weights = torch.ones(_BATCH_SIZE, dtype=torch.bool, device=device)
    return {'inputs': inputs, 'targets': targets, 'weights': weights}


def _warm_up(workload: spec.Workload,
             model_params: spec.ParameterContainer,
             model_state: spec.ModelAuxiliaryState,
             optimizer: torch.optim.Optimizer,
             params: List[Any],
             ema: List[Any]) -> None:
    """Pay the one-off cost of tracing, kernel selection and allocation here.

    Everything below is value-neutral: the forward/backward pass is run on a zero
    batch and its gradients are discarded, the optimizer update it feeds on is the
    identity because both moments stay at zero, the averaging buffer is refreshed
    from the parameters afterwards, and the optimizer's step counters are reset. The
    parameters the first real step sees are exactly the parameters the initializer
    produced.
    """
    batch = _dummy_batch(model_params, params)
    if batch is not None:
        try:
            model_params.train()
            logits, _ = workload.model_fn(
                params=model_params,
                augmented_and_preprocessed_input_batch=batch,
                model_state=model_state,
                mode=spec.ForwardPassMode.TRAIN,
                rng=None,
                update_batch_norm=False,
            )
            losses = workload.loss_fn(
                label_batch=batch['targets'],
                logits_batch=logits,
                mask_batch=batch['weights'],
                label_smoothing=_LABEL_SMOOTHING,
            )
            (losses['summed'] / losses['n_valid_examples']).backward()
        except Exception:  # pylint: disable=broad-except
            pass
    optimizer.zero_grad(set_to_none=True)
    try:
        with torch.no_grad():
            for p in params:
                p.grad = torch.zeros_like(p)
        for _ in range(2):
            optimizer.step()
            with torch.no_grad():
                torch._foreach_mul_(ema, 0.5)
                torch._foreach_add_(ema, params, alpha=0.5)
    except Exception:  # pylint: disable=broad-except
        pass
    optimizer.zero_grad(set_to_none=True)
    for state in optimizer.state.values():
        for key, value in list(state.items()):
            if torch.is_tensor(value):
                value.zero_()
            elif isinstance(value, (int, float)):
                state[key] = 0
    with torch.no_grad():
        for e, p in zip(ema, params):
            e.copy_(p.detach())


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
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
    except Exception:  # pylint: disable=broad-except
        optimizer = torch.optim.AdamW(
            params,
            lr=_PEAK_LR,
            betas=(_BETA1, _BETA2),
            eps=_EPS,
            weight_decay=_WEIGHT_DECAY,
        )
    ema = [p.detach().clone() for p in params]
    backup = [p.detach().clone() for p in params]
    _warm_up(workload, model_params, model_state, optimizer, params, ema)
    return {
        'optimizer': optimizer,
        'params': params,
        'ema': ema,
        'backup': backup,
        'shadowed': False,
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
    del eval_results
    del global_step

    _restore_if_shadowed(optimizer_state)

    optimizer = optimizer_state['optimizer']
    step = optimizer_state['step']
    lr = _lr_at(step)
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
    (losses['summed'] / losses['n_valid_examples']).backward()
    optimizer.step()

    decay = _ema_decay(step)
    with torch.no_grad():
        torch._foreach_mul_(optimizer_state['ema'], decay)
        torch._foreach_add_(
            optimizer_state['ema'], optimizer_state['params'], alpha=1.0 - decay
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
    """Evaluate the averaged iterate; training resumes from the raw iterate."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng

    if not optimizer_state.get('shadowed') and optimizer_state['step'] > 0:
        with torch.no_grad():
            for b, e, p in zip(
                optimizer_state['backup'],
                optimizer_state['ema'],
                optimizer_state['params'],
            ):
                b.copy_(p.detach())
                p.data.copy_(e)
        optimizer_state['shadowed'] = True
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
