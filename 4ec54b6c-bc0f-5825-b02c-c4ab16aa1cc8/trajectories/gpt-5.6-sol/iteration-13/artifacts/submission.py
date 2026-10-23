from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_BASE_LEARNING_RATE = 0.003
_BETA1 = 0.9
_BETA2 = 0.99
_EPSILON = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 16
_MIN_LR_FACTOR = 0.2


def _learning_rate(step: int, horizon: int) -> float:
    """Short warmup followed by linear decay to a nonzero floor."""
    if step < _WARMUP_STEPS:
        return _BASE_LEARNING_RATE * float(step + 1) / float(_WARMUP_STEPS)
    decay_length = max(horizon - _WARMUP_STEPS, 1)
    progress = min(float(step - _WARMUP_STEPS) / float(decay_length), 1.0)
    factor = max(_MIN_LR_FACTOR, 1.0 - (1.0 - _MIN_LR_FACTOR) * progress)
    return _BASE_LEARNING_RATE * factor


def get_batch_size(workload_name: str) -> int:
    """Return one global batch size for all workloads."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize the optimizer and its workload-provided schedule horizon."""
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.Adam(
        model_params.parameters(),
        lr=_learning_rate(0, workload.step_hint),
        betas=(_BETA1, _BETA2),
        eps=_EPSILON,
        weight_decay=_WEIGHT_DECAY,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "horizon": max(int(workload.step_hint), 1),
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
    """Apply one adaptive first-order update."""
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    lr = _learning_rate(step, optimizer_state["horizon"])
    for group in optimizer.param_groups:
        group["lr"] = lr

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)
    predictions, next_state = workload.model_fn(
        params=current_param_container,
        augmented_and_preprocessed_input_batch=batch,
        model_state=model_state,
        mode=spec.ForwardPassMode.TRAIN,
        rng=rng,
        update_batch_norm=True,
    )
    losses = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=predictions,
        mask_batch=batch.get("weights"),
        label_smoothing=0.0,
    )
    loss = losses["summed"] / losses["n_valid_examples"]
    loss.backward()
    optimizer.step()

    optimizer_state["step"] = step + 1
    return optimizer_state, current_param_container, next_state


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
    """Consume the next pre-shuffled training batch."""
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
