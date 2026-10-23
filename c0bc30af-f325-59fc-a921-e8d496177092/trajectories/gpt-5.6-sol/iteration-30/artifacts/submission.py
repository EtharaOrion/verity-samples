"""Self-tuning Nesterov method with a workload-scaled one-cycle schedule."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LEARNING_RATE = 0.2
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_WARMUP_FRACTION = 0.1
_INITIAL_FACTOR = 0.1
_FINAL_FACTOR = 0.01


def get_batch_size(workload_name: str) -> int:
    """Return one workload-independent global batch size."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize Nesterov momentum and schedule bookkeeping."""
    del model_state
    del hyperparameters
    del rng
    total_steps = max(2, int(workload.step_hint))
    warmup_steps = max(1, int(_WARMUP_FRACTION * total_steps))
    optimizer = torch.optim.SGD(
        model_params.parameters(),
        lr=_PEAK_LEARNING_RATE * _INITIAL_FACTOR,
        momentum=_MOMENTUM,
        weight_decay=_WEIGHT_DECAY,
        nesterov=True,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "total_steps": total_steps,
        "warmup_steps": warmup_steps,
    }


def _scheduled_learning_rate(
    workload: spec.Workload,
    optimizer_state: spec.OptimizerState,
    eval_results: List[Tuple[int, float]],
) -> float:
    """Apply a warmup and cosine cycle scaled by generic workload guidance."""
    del workload
    del eval_results
    step = min(optimizer_state["step"] + 1, optimizer_state["total_steps"])
    warmup_steps = optimizer_state["warmup_steps"]
    if step <= warmup_steps:
        progress = step / warmup_steps
        factor = _INITIAL_FACTOR + (1.0 - _INITIAL_FACTOR) * progress
        return _PEAK_LEARNING_RATE * factor

    decay_steps = max(1, optimizer_state["total_steps"] - warmup_steps)
    progress = (step - warmup_steps) / decay_steps
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    factor = _FINAL_FACTOR + (1.0 - _FINAL_FACTOR) * cosine
    return _PEAK_LEARNING_RATE * factor


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
    """Apply one scheduled Nesterov training update."""
    del current_params_types
    del hyperparameters
    del loss_type
    del global_step

    optimizer = optimizer_state["optimizer"]
    learning_rate = _scheduled_learning_rate(
        workload, optimizer_state, eval_results
    )
    for group in optimizer.param_groups:
        group["lr"] = learning_rate

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)
    predictions, next_model_state = workload.model_fn(
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

    optimizer_state["step"] += 1
    return optimizer_state, current_param_container, next_model_state


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
    """Expose the current training state unchanged for evaluation."""
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
    """Take the next preprocessed batch without additional overhead."""
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
