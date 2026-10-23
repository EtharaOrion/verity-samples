"""Workload-agnostic adaptive training algorithm."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LEARNING_RATE = 0.0018
_WEIGHT_DECAY = 0.05
_LABEL_SMOOTHING = 0.05
_WARMUP_FRACTION = 0.02
_SCHEDULE_MULTIPLIER = 2.0
_MIN_LEARNING_RATE_FACTOR = 0.05


def _learning_rate(step: int, warmup_steps: int, total_steps: int) -> float:
    if step < warmup_steps:
        return _PEAK_LEARNING_RATE * (step + 1) / warmup_steps
    decay_steps = max(total_steps - warmup_steps, 1)
    progress = min((step - warmup_steps) / decay_steps, 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    factor = _MIN_LEARNING_RATE_FACTOR + (1.0 - _MIN_LEARNING_RATE_FACTOR) * cosine
    return _PEAK_LEARNING_RATE * factor


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    del model_state
    del hyperparameters
    del rng
    total_steps = max(int(_SCHEDULE_MULTIPLIER * workload.step_hint), 1)
    warmup_steps = max(int(_WARMUP_FRACTION * total_steps), 1)
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_learning_rate(0, warmup_steps, total_steps),
        betas=(0.9, 0.99),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "warmup_steps": warmup_steps,
        "total_steps": total_steps,
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

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    learning_rate = _learning_rate(
        step, optimizer_state["warmup_steps"], optimizer_state["total_steps"]
    )
    for group in optimizer.param_groups:
        group["lr"] = learning_rate

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
        label_smoothing=_LABEL_SMOOTHING,
    )
    loss = losses["summed"] / losses["n_valid_examples"]
    loss.backward()
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
) -> spec.UpdateReturn:
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
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
