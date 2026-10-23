"""A self-tuning training algorithm.

One setting for every workload: fused AdamW with a short linear warmup, an
inverse-square-root decay of the step size, mild label smoothing, and an
exponential moving average of the iterates that is swapped in for evaluation
only. Nothing here inspects the workload name, the parameter shapes, or the
model state keys, and no state lives at module level, so each run starts clean.
"""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LR = 0.008
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-6
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 60
_DECAY_TAU = 700.0
_EMA_DECAY = 0.999
_EMA_WARMUP = 10.0
_LABEL_SMOOTHING = 0.1


def get_batch_size(workload_name: str) -> int:
    """A single batch size that is used for every workload."""
    del workload_name
    return _BATCH_SIZE


def _lr_at(step: int) -> float:
    """Linear warmup, then an inverse-square-root decay with no fixed horizon."""
    if step < _WARMUP_STEPS:
        return _PEAK_LR * float(step + 1) / float(_WARMUP_STEPS)
    return _PEAK_LR / math.sqrt(1.0 + (step - _WARMUP_STEPS) / _DECAY_TAU)


def _lerp_(dst: List[torch.Tensor], src: List[torch.Tensor], weight: float) -> None:
    try:
        torch._foreach_lerp_(dst, src, weight)
    except (AttributeError, RuntimeError, TypeError):
        for d, s in zip(dst, src):
            d.add_(s.detach() - d, alpha=weight)


def _copy_(dst: List[torch.Tensor], src: List[torch.Tensor]) -> None:
    for d, s in zip(dst, src):
        d.copy_(s)


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
    kwargs = {
        'lr': _PEAK_LR,
        'betas': (_BETA1, _BETA2),
        'eps': _EPS,
        'weight_decay': _WEIGHT_DECAY,
    }
    try:
        optimizer = torch.optim.AdamW(params, fused=True, **kwargs)
    except (RuntimeError, ValueError, TypeError):
        optimizer = torch.optim.AdamW(params, **kwargs)
    # All auxiliary state is attached to the optimizer, which owns a state_dict,
    # so the harness can checkpoint and restore the returned mapping unchanged.
    optimizer._algo_params = params
    optimizer._algo_step = 0
    optimizer._algo_ema = [p.detach().clone() for p in params]
    optimizer._algo_backup = [p.detach().clone() for p in params]
    optimizer._algo_swapped = False
    return {'optimizer': optimizer}


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
    """One training step."""
    del current_params_types
    del hyperparameters
    del eval_results
    del loss_type
    del global_step

    optimizer = optimizer_state['optimizer']
    params = optimizer._algo_params

    # If an evaluation left the averaged weights in the model, restore the
    # training iterate first so optimisation always continues from it.
    if optimizer._algo_swapped:
        with torch.no_grad():
            _copy_(params, optimizer._algo_backup)
        optimizer._algo_swapped = False

    step = optimizer._algo_step
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
    mean_loss = losses['summed'] / losses['n_valid_examples']
    mean_loss.backward()
    optimizer.step()

    decay = min(_EMA_DECAY, (step + 1.0) / (step + 1.0 + _EMA_WARMUP))
    with torch.no_grad():
        _lerp_(optimizer._algo_ema, params, 1.0 - decay)

    optimizer._algo_step = step + 1
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
    """Evaluate the moving average of the iterates instead of the last iterate."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng

    optimizer = optimizer_state['optimizer']
    if not optimizer._algo_swapped:
        with torch.no_grad():
            _copy_(optimizer._algo_backup, optimizer._algo_params)
            _copy_(optimizer._algo_params, optimizer._algo_ema)
        optimizer._algo_swapped = True
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
