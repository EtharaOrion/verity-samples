"""Adaptive, scheduled training algorithm for the self-tuning ruleset."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_LEARNING_RATE = 0.00175
_BETA1 = 0.933
_BETA2 = 0.9955
_WEIGHT_DECAY = 0.08
_WARMUP_FRACTION = 0.02
_SCHEDULE_MULTIPLIER = 2
_MIN_LR_FACTOR = 0.05
_FINAL_EVAL_FRACTION = 0.75


def get_batch_size(workload_name: str) -> int:
    """Return one workload-independent global training batch size."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize decoupled NAdam and a workload-provided schedule horizon."""
    del model_state, hyperparameters, rng
    optimizer = torch.optim.NAdam(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        weight_decay=_WEIGHT_DECAY,
        momentum_decay=0.0,
        decoupled_weight_decay=True,
        foreach=True,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "schedule_steps": max(int(_SCHEDULE_MULTIPLIER * workload.step_hint), 2),
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
    """Apply one adaptive update with linear warmup and cosine decay."""
    del current_params_types, hyperparameters, loss_type, eval_results
    del global_step
    if (
        train_state is not None
        and train_state["accumulated_submission_time"]
        >= _FINAL_EVAL_FRACTION * workload.max_allowed_runtime_sec
    ):
        raise spec.TrainingCompleteError

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"] + 1
    schedule_steps = optimizer_state["schedule_steps"]
    warmup_steps = max(int(_WARMUP_FRACTION * schedule_steps), 1)
    if step <= warmup_steps:
        lr_factor = step / warmup_steps
    else:
        progress = min((step - warmup_steps) / (schedule_steps - warmup_steps), 1.0)
        cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
        lr_factor = _MIN_LR_FACTOR + (1.0 - _MIN_LR_FACTOR) * cosine
    for group in optimizer.param_groups:
        group["lr"] = _LEARNING_RATE * lr_factor

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

    optimizer_state["step"] = step
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
    """Take the next pre-shuffled training batch."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
