"""Self-tuning training algorithm using scheduled adaptive updates."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_LEARNING_RATE = 0.002
_WEIGHT_DECAY = 0.01
_BETA1 = 0.9
_BETA2 = 0.99
_WARMUP_FRACTION = 0.04
_MIN_LR_FACTOR = 0.05
_LABEL_SMOOTHING = 0.05


def _learning_rate(step: int, total_steps: int) -> float:
    warmup_steps = max(1, int(_WARMUP_FRACTION * total_steps))
    if step < warmup_steps:
        return _LEARNING_RATE * (step + 1) / warmup_steps
    progress = min(1.0, (step - warmup_steps) / max(1, total_steps - warmup_steps))
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _LEARNING_RATE * (_MIN_LR_FACTOR + (1.0 - _MIN_LR_FACTOR) * cosine)


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
    """Initialize AdamW and a schedule sized by the workload's step hint."""
    del model_state, hyperparameters, rng
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
        "cycle_start": 0,
        "total_steps": workload.step_hint,
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
    """Take one mixed-precision AdamW step and retain new auxiliary state."""
    del current_params_types, hyperparameters, loss_type, global_step, train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    total_steps = optimizer_state["total_steps"]
    cycle_start = optimizer_state["cycle_start"]
    if eval_results and step - cycle_start >= total_steps:
        latest_result = eval_results[-1][1]
        if not workload.has_reached_validation_target(latest_result):
            cycle_start = step
            optimizer_state["cycle_start"] = cycle_start
    lr = _learning_rate(step - cycle_start, total_steps)
    for group in optimizer.param_groups:
        group["lr"] = lr

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)
    with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
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
            label_smoothing=_LABEL_SMOOTHING,
        )
        mean_loss = losses["summed"] / losses["n_valid_examples"]

    mean_loss.backward()
    optimizer.step()
    optimizer_state["step"] = step + 1
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
    """Return the current training state unchanged for evaluation."""
    del workload, current_params_types, hyperparameters, loss_type
    del eval_results, global_step, rng
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
    """Take the next preprocessed batch from the input queue."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
