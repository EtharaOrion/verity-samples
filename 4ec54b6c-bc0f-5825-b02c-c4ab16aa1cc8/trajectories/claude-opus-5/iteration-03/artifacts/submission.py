"""Self-tuning submission for the AlgoPerf PyTorch workloads.

One setting for every workload, chosen by the algorithm rather than by identifying the
workload: NAdam with decoupled weight decay, a short linear warmup into a flat rate, global
gradient-norm clipping, mild label smoothing, and an exponential moving average of the weights
whose averaging horizon widens with the step count. The average is what the evaluator sees:
`prepare_for_eval` installs it and parks the training weights, and the next `update_params`
puts the training weights back before stepping, so training itself is never perturbed.

All mutable state lives in the torch optimizer's per-parameter `state`, including the parked
copy whose mere presence records which weights are currently installed. Nothing is latched at
module level, so the state round-trips through the harness checkpoint path and a fresh run
starts from a clean slate no matter what a previous one did.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_LEARNING_RATE = 0.008
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 20.0
_DECAY_STEPS = 1000000.0
_DECAY_POWER = 1.0
_MIN_LR_FRACTION = 0.1
_MAX_GRAD_NORM = 1.0
_EMA_MAX_DECAY = 0.99
_EMA_HORIZON = 10.0
_LABEL_SMOOTHING = 0.1


def _params_of(optimizer: Any) -> List[Any]:
    return [p for group in optimizer.param_groups for p in group['params']]


def _learning_rate_at(step: int) -> float:
    warmup = min(1.0, (float(step) + 1.0) / _WARMUP_STEPS)
    decay = 1.0 / (1.0 + float(step) / _DECAY_STEPS) ** _DECAY_POWER
    return _LEARNING_RATE * warmup * max(decay, _MIN_LR_FRACTION)


def _ema_decay_at(step: int) -> float:
    return min(_EMA_MAX_DECAY, (float(step) + 1.0) / (float(step) + _EMA_HORIZON))


def _update_ema(optimizer: Any, step: int) -> None:
    params = _params_of(optimizer)
    shadows = []
    live = []
    for p in params:
        state = optimizer.state[p]
        shadow = state.get('ema')
        if shadow is None:
            state['ema'] = p.detach().clone()
            continue
        shadows.append(shadow)
        live.append(p.detach())
    if not shadows:
        return
    decay = _ema_decay_at(step)
    torch._foreach_mul_(shadows, decay)
    torch._foreach_add_(shadows, live, alpha=1.0 - decay)


def _install_average(optimizer: Any) -> None:
    """Park the training weights and put the moving average in the model.

    The parked copy lives in the per-parameter optimizer state, so its presence is
    itself the record of what is currently installed. That record is a tensor and
    therefore survives `state_dict`/`load_state_dict`, which means a run that is
    interrupted between an evaluation and the next step resumes in exactly the
    state it left, with nothing latched outside the optimizer.
    """
    for p in _params_of(optimizer):
        state = optimizer.state[p]
        shadow = state.get('ema')
        if shadow is None or 'live' in state:
            continue
        state['live'] = p.detach().clone()
        p.detach().copy_(shadow)


def _restore_live(optimizer: Any) -> None:
    """Undo `_install_average`; a no-op when the training weights are installed."""
    for p in _params_of(optimizer):
        state = optimizer.state[p]
        parked = state.pop('live', None)
        if parked is not None:
            p.detach().copy_(parked)


def get_batch_size(workload_name: str) -> int:
    """One batch size for every workload, as the rules require."""
    del workload_name
    return _BATCH_SIZE


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
    trainable = [p for p in model_params.parameters() if p.requires_grad]
    optimizer = torch.optim.NAdam(
        trainable,
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
        decoupled_weight_decay=True,
    )
    # NOTE: the moving average buffers are created lazily, after the first optimizer
    # step, because torch initialises its own per-parameter state only when it finds
    # that state empty.
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
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results

    optimizer = optimizer_state['optimizer']

    # If the previous call handed the averaged weights to the evaluator, put the
    # training weights back before stepping again.
    with torch.no_grad():
        _restore_live(optimizer)

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

    learning_rate = _learning_rate_at(global_step)
    for group in optimizer.param_groups:
        group['lr'] = learning_rate

    torch.nn.utils.clip_grad_norm_(_params_of(optimizer), max_norm=_MAX_GRAD_NORM)
    optimizer.step()
    with torch.no_grad():
        _update_ema(optimizer, global_step)

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
    """Hand the moving average of the weights to the evaluator."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng

    optimizer = optimizer_state['optimizer']
    with torch.no_grad():
        _install_average(optimizer)
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
