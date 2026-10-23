"""Adaptive, scheduled training algorithm for AlgoPerf workloads."""

import math
from typing import Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_LEARNING_RATE = 0.003
_WEIGHT_DECAY = 0.01
_BETA1 = 0.9
_BETA2 = 0.999
_WARMUP_FRACTION = 0.02
_MIN_LR_FRACTION = 0.01


def get_batch_size(workload_name: str) -> int:
    """Return one workload-independent training batch size."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize AdamW and a generic step-hint-based schedule."""
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        weight_decay=_WEIGHT_DECAY,
        fused=True,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "total_steps": max(int(workload.step_hint), 1),
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
    train_state: Optional[Dict[str, object]] = None,
) -> spec.UpdateReturn:
    """Take one adaptive gradient step and propagate auxiliary model state."""
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    total_steps = optimizer_state["total_steps"]
    warmup_steps = max(int(_WARMUP_FRACTION * total_steps), 1)
    if step < warmup_steps:
        multiplier = (step + 1) / warmup_steps
    else:
        progress = min(
            (step - warmup_steps) / max(total_steps - warmup_steps, 1), 1.0
        )
        cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
        multiplier = _MIN_LR_FRACTION + (1.0 - _MIN_LR_FRACTION) * cosine
    optimizer.param_groups[0]["lr"] = _LEARNING_RATE * multiplier

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
    (losses["summed"] / losses["n_valid_examples"]).backward()
    optimizer.step()

    optimizer_state["step"] = step + 1
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
) -> spec.UpdateReturn:
    """Return the current training state unchanged for evaluation."""
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
    """Take the next preprocessed training batch."""
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
