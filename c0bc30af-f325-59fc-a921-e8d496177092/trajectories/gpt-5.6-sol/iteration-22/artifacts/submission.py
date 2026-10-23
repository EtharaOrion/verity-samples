import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_BASE_LEARNING_RATE = 0.1
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_WARMUP_EPOCHS = 1
_DECAY_EPOCHS = 20
_MIN_LEARNING_RATE_RATIO = 0.02


def _learning_rate(step: int, warmup_steps: int, decay_steps: int) -> float:
    if step < warmup_steps:
        return _BASE_LEARNING_RATE * float(step + 1) / float(warmup_steps)
    progress = min(float(step - warmup_steps) / float(decay_steps), 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    factor = _MIN_LEARNING_RATE_RATIO + (1.0 - _MIN_LEARNING_RATE_RATIO) * cosine
    return _BASE_LEARNING_RATE * factor


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
    steps_per_epoch = max(workload.num_train_examples // _BATCH_SIZE, 1)
    warmup_steps = _WARMUP_EPOCHS * steps_per_epoch
    optimizer = torch.optim.SGD(
        model_params.parameters(),
        lr=_BASE_LEARNING_RATE / float(warmup_steps),
        momentum=_MOMENTUM,
        weight_decay=_WEIGHT_DECAY,
        nesterov=True,
        fused=True,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "warmup_steps": warmup_steps,
        "decay_steps": _DECAY_EPOCHS * steps_per_epoch,
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
        step, optimizer_state["warmup_steps"], optimizer_state["decay_steps"]
    )
    for group in optimizer.param_groups:
        group["lr"] = learning_rate

    optimizer.zero_grad(set_to_none=True)
    with torch.autocast(
        device_type=batch["inputs"].device.type,
        dtype=torch.bfloat16,
        enabled=batch["inputs"].is_cuda,
    ):
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
