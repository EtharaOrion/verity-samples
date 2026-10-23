"""Self-tuning training algorithm using normalized SGD and cosine decay."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LEARNING_RATE = 0.1
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_WARMUP_EPOCHS = 1.0
_DECAY_EPOCHS = 25.0
_MIN_LEARNING_RATE = 0.001
_ANNEAL_START_FRACTION = 0.75
_MIN_SCHEDULE_PROGRESS = 0.25
_LABEL_SMOOTHING = 0.0


def get_batch_size(workload_name: str) -> int:
    """Return one global batch size for every workload."""
    del workload_name
    return _BATCH_SIZE


def _learning_rate(
    step: int, examples_per_epoch: int, progress_cap: float
) -> float:
    """Compute a batch-size-normalized warmup and guarded cosine schedule."""
    epoch_size = max(examples_per_epoch, _BATCH_SIZE)
    epoch = step * _BATCH_SIZE / epoch_size
    if epoch < _WARMUP_EPOCHS:
        increment = _BATCH_SIZE / epoch_size
        return _PEAK_LEARNING_RATE * (epoch + increment) / _WARMUP_EPOCHS
    scheduled_progress = (
        (epoch - _WARMUP_EPOCHS) / (_DECAY_EPOCHS - _WARMUP_EPOCHS)
    )
    time_progress = min(0.5 * scheduled_progress, 1.0)
    progress = min(scheduled_progress, max(progress_cap, time_progress), 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _MIN_LEARNING_RATE + (_PEAK_LEARNING_RATE - _MIN_LEARNING_RATE) * cosine


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize momentum SGD and its data-normalized schedule state."""
    del model_state, hyperparameters, rng
    optimizer = torch.optim.SGD(
        model_params.parameters(),
        lr=_PEAK_LEARNING_RATE,
        momentum=_MOMENTUM,
        weight_decay=_WEIGHT_DECAY,
        nesterov=True,
        foreach=True,
    )
    return {
        "optimizer": optimizer,
        "examples_per_epoch": workload.num_train_examples,
        "step": 0,
        "eval_count": 0,
        "schedule_progress_cap": 1.0,
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
    """Apply one mixed-precision momentum step and preserve auxiliary state."""
    del current_params_types, hyperparameters, loss_type, global_step, train_state

    if len(eval_results) > optimizer_state["eval_count"]:
        metric_key = "validation/" + workload.target_metric_name
        best_metric = max(result[1][metric_key] for result in eval_results)
        target = workload.validation_target_value
        quality_progress = (best_metric / target - _ANNEAL_START_FRACTION) / (
            1.0 - _ANNEAL_START_FRACTION
        )
        optimizer_state["schedule_progress_cap"] = max(
            _MIN_SCHEDULE_PROGRESS, min(quality_progress, 1.0)
        )
        optimizer_state["eval_count"] = len(eval_results)

    optimizer = optimizer_state["optimizer"]
    lr = _learning_rate(
        optimizer_state["step"],
        optimizer_state["examples_per_epoch"],
        optimizer_state["schedule_progress_cap"],
    )
    for group in optimizer.param_groups:
        group["lr"] = lr

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)
    with torch.autocast(
        device_type=batch["inputs"].device.type,
        dtype=torch.bfloat16,
        enabled=batch["inputs"].is_cuda,
    ):
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
    """Select the next already shuffled and augmented batch."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
