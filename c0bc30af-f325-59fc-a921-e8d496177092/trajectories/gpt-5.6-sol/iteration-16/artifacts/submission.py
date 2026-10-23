"""Self-tuning training algorithm using AdamW and adaptive cosine decay."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_BASE_LEARNING_RATE = 0.002
_MIN_LEARNING_RATE_RATIO = 0.08
_WARMUP_RATIO = 0.02
_WEIGHT_DECAY = 0.02
_BETA1 = 0.9
_BETA2 = 0.99
_LABEL_SMOOTHING = 0.03


def _scheduled_learning_rate(optimizer_state: spec.OptimizerState) -> float:
    step = optimizer_state["step"]
    warmup_steps = optimizer_state["warmup_steps"]
    decay_steps = optimizer_state["decay_steps"]
    if step < warmup_steps:
        factor = (step + 1) / warmup_steps
    else:
        progress = min((step - warmup_steps) / decay_steps, 1.0)
        cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
        factor = _MIN_LEARNING_RATE_RATIO + (
            1.0 - _MIN_LEARNING_RATE_RATIO
        ) * cosine
    return _BASE_LEARNING_RATE * factor * optimizer_state["feedback_scale"]


def _adapt_to_evaluations(
    workload: spec.Workload,
    optimizer_state: spec.OptimizerState,
    eval_results: List[Tuple[int, float]],
) -> None:
    if len(eval_results) <= optimizer_state["seen_evals"]:
        return
    optimizer_state["seen_evals"] = len(eval_results)
    latest_result = eval_results[-1][1]
    metric_name = "validation/" + workload.target_metric_name
    metric = latest_result.get(metric_name)
    if metric is None:
        return
    target = workload.validation_target_value
    if metric >= 0.98 * target:
        optimizer_state["feedback_scale"] = 0.5


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
    warmup_steps = max(1, int(_WARMUP_RATIO * workload.step_hint))
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_BASE_LEARNING_RATE / warmup_steps,
        betas=(_BETA1, _BETA2),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
        fused=torch.cuda.is_available(),
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "warmup_steps": warmup_steps,
        "decay_steps": max(1, workload.step_hint - warmup_steps),
        "feedback_scale": 1.0,
        "seen_evals": 0,
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
    del current_params_types
    del hyperparameters
    del loss_type
    del global_step
    del train_state

    _adapt_to_evaluations(workload, optimizer_state, eval_results)
    optimizer = optimizer_state["optimizer"]
    learning_rate = _scheduled_learning_rate(optimizer_state)
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
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
    optimizer.step()

    optimizer_state["step"] += 1
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
