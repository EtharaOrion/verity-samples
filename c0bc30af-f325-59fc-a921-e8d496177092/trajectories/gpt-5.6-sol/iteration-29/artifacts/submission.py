"""Self-tuning training algorithm for image classification workloads."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_SGD_LR = 0.1
_ADAM_LR = 0.002
_WEIGHT_DECAY = 5e-4
_MOMENTUM = 0.9
_WARMUP_EPOCHS = 1.0
_DECAY_EPOCHS = 12.0
_MIN_LR_RATIO = 0.02
_TARGET_PROXIMITY = 0.93
_REFINEMENT_LR_RATIO = 0.1


def _contains_batch_norm(model: torch.nn.Module) -> bool:
    return any(
        isinstance(module, torch.nn.modules.batchnorm._BatchNorm)
        for module in model.modules()
    )


def _learning_rate(step: int, steps_per_epoch: int, peak_lr: float) -> float:
    epoch = step / steps_per_epoch
    if epoch < _WARMUP_EPOCHS:
        return peak_lr * (0.05 + 0.95 * epoch / _WARMUP_EPOCHS)

    progress = min((epoch - _WARMUP_EPOCHS) / _DECAY_EPOCHS, 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return peak_lr * (_MIN_LR_RATIO + (1.0 - _MIN_LR_RATIO) * cosine)


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

    model_params.to(memory_format=torch.channels_last)
    uses_batch_norm = _contains_batch_norm(model_params)
    if uses_batch_norm:
        optimizer = torch.optim.SGD(
            model_params.parameters(),
            lr=_SGD_LR * 0.05,
            momentum=_MOMENTUM,
            weight_decay=_WEIGHT_DECAY,
            nesterov=True,
            fused=True,
        )
        peak_lr = _SGD_LR
    else:
        optimizer = torch.optim.AdamW(
            model_params.parameters(),
            lr=_ADAM_LR * 0.05,
            betas=(0.9, 0.99),
            weight_decay=_WEIGHT_DECAY,
            fused=True,
        )
        peak_lr = _ADAM_LR

    steps_per_epoch = max(workload.num_train_examples // _BATCH_SIZE, 1)
    return {
        "optimizer": optimizer,
        "step": 0,
        "steps_per_epoch": steps_per_epoch,
        "peak_lr": peak_lr,
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

    optimizer = optimizer_state["optimizer"]
    peak_lr = optimizer_state["peak_lr"]
    lr = _learning_rate(
        optimizer_state["step"],
        optimizer_state["steps_per_epoch"],
        peak_lr,
    )
    if eval_results:
        latest_metrics = eval_results[-1][1]
        validation_key = f"validation/{workload.target_metric_name}"
        if (
            validation_key in latest_metrics
            and latest_metrics[validation_key]
            >= _TARGET_PROXIMITY * workload.validation_target_value
        ):
            lr = min(lr, peak_lr * _REFINEMENT_LR_RATIO)
    for group in optimizer.param_groups:
        group["lr"] = lr

    optimizer.zero_grad(set_to_none=True)
    batch["inputs"] = batch["inputs"].contiguous(
        memory_format=torch.channels_last
    )
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
            label_smoothing=0.0,
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
