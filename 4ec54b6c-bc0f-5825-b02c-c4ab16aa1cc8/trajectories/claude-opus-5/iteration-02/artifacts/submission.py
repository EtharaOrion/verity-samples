"""Self-tuning training algorithm.

NAdam with a short linear warmup, a gentle cosine decay with a floor,
gradient-norm clipping, mild label smoothing, and an exponential moving average
of the weights which is what gets evaluated. One fixed setting is used for every
workload: the module never inspects the workload name, never inspects parameter
shapes, names or counts, and holds no module-level mutable state. Every piece of
algorithm state is created inside `init_optimizer_state`, which the harness calls
once per run, so nothing can carry over between runs.
"""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_BASE_LR = 0.016
_BETA1 = 0.9
_BETA2 = 0.999
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 20
_DECAY_STEPS = 4000
_LR_FLOOR = 0.15
_EMA_DECAY = 0.99
_GRAD_CLIP = 1.0
_LABEL_SMOOTHING = 0.1


def get_batch_size(workload_name: str) -> int:
    """A single batch size for every workload."""
    del workload_name
    return _BATCH_SIZE


def _lr_multiplier(step: int) -> float:
    """Linear warmup into a cosine decay with a floor, a function of the step only."""
    warm = min(1.0, float(step) / float(max(1, _WARMUP_STEPS)))
    progress = min(1.0, float(step) / float(_DECAY_STEPS))
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return warm * (_LR_FLOOR + (1.0 - _LR_FLOOR) * cosine)


def _trainable(optimizer: Any) -> List[Any]:
    return [p for group in optimizer.param_groups for p in group['params']]


def _restore_raw_params(optimizer_state: spec.OptimizerState) -> None:
    """Undo an averaged-weight swap made before an evaluation, if one is active."""
    if not optimizer_state['params_are_averaged']:
        return
    saved = optimizer_state['saved_params']
    if saved is not None:
        live = _trainable(optimizer_state['optimizer'])
        with torch.no_grad():
            for param, backup in zip(live, saved):
                param.copy_(backup)
    optimizer_state['saved_params'] = None
    optimizer_state['params_are_averaged'] = False


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Construct the optimizer and the weight-average buffers fresh, per run."""
    del workload
    del model_state
    del hyperparameters
    del rng
    params = [p for p in model_params.parameters() if p.requires_grad]
    optimizer = torch.optim.NAdam(
        params,
        lr=_BASE_LR,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
    )
    averaged = [p.detach().clone() for p in params]
    return {
        'optimizer': optimizer,
        'averaged_params': averaged,
        'saved_params': None,
        'params_are_averaged': False,
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
    """One scheduled NAdam step with clipping, followed by the weight average."""
    unused = (current_params_types, hyperparameters, loss_type, eval_results, train_state)
    del unused

    _restore_raw_params(optimizer_state)

    optimizer = optimizer_state['optimizer']
    current_param_container.train()
    trainable = _trainable(optimizer)
    for param in trainable:
        param.grad = None

    step = int(optimizer_state['step']) + 1
    lr = _BASE_LR * _lr_multiplier(step)
    for group in optimizer.param_groups:
        group['lr'] = lr

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
        label_smoothing=_LABEL_SMOOTHING,
    )
    loss = loss_dict['summed'] / loss_dict['n_valid_examples']
    loss.backward()

    torch.nn.utils.clip_grad_norm_(trainable, _GRAD_CLIP)
    optimizer.step()

    averaged = optimizer_state['averaged_params']
    decay = min(_EMA_DECAY, 1.0 - 1.0 / (step + 1.0))
    with torch.no_grad():
        torch._foreach_mul_(averaged, decay)
        torch._foreach_add_(averaged, trainable, alpha=1.0 - decay)

    optimizer_state['step'] = step
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
    """Evaluate the averaged weights; the raw iterate returns before the next step."""
    unused = (
        workload,
        current_params_types,
        hyperparameters,
        loss_type,
        eval_results,
        global_step,
        rng,
    )
    del unused

    if int(optimizer_state['step']) < 1:
        return optimizer_state, current_param_container, model_state
    if optimizer_state['params_are_averaged']:
        return optimizer_state, current_param_container, model_state

    trainable = _trainable(optimizer_state['optimizer'])
    averaged = optimizer_state['averaged_params']
    with torch.no_grad():
        optimizer_state['saved_params'] = [p.detach().clone() for p in trainable]
        for param, avg in zip(trainable, averaged):
            param.copy_(avg)
    optimizer_state['params_are_averaged'] = True
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
    """Take the next batch off the pre-shuffled queue, unchanged."""
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
