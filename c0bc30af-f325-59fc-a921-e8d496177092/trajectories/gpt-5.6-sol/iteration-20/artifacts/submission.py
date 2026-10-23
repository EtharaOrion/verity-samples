"""Autonomous momentum training with warmup and cosine decay."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_PEAK_LEARNING_RATE = 0.05
_MIN_LEARNING_RATE = 0.00025
_MOMENTUM = 0.9
_WEIGHT_DECAY = 0.0005
_WARMUP_FRACTION = 0.04
_SCHEDULE_BATCH_REFERENCE = 128


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
    del model_state, hyperparameters, rng
    cycle_steps = max(
        int(workload.step_hint * _SCHEDULE_BATCH_REFERENCE / _BATCH_SIZE), 1
    )
    optimizer = torch.optim.SGD(
        model_params.parameters(),
        lr=_PEAK_LEARNING_RATE * _WARMUP_FRACTION,
        momentum=_MOMENTUM,
        nesterov=True,
        weight_decay=_WEIGHT_DECAY,
    )
    return {"optimizer": optimizer, "step": 0, "cycle_steps": cycle_steps}


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
    del current_params_types, hyperparameters, loss_type, eval_results, global_step

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    cycle_steps = optimizer_state["cycle_steps"]
    schedule_step = min(step, cycle_steps - 1)
    warmup_steps = max(int(_WARMUP_FRACTION * cycle_steps), 1)
    if schedule_step < warmup_steps:
        fraction = (schedule_step + 1) / warmup_steps
        learning_rate = _MIN_LEARNING_RATE + (
            _PEAK_LEARNING_RATE - _MIN_LEARNING_RATE
        ) * fraction
    else:
        fraction = (schedule_step - warmup_steps) / max(
            cycle_steps - warmup_steps - 1, 1
        )
        learning_rate = _MIN_LEARNING_RATE + 0.5 * (
            _PEAK_LEARNING_RATE - _MIN_LEARNING_RATE
        ) * (1.0 + math.cos(math.pi * fraction))
    for parameter_group in optimizer.param_groups:
        parameter_group["lr"] = learning_rate

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
    (losses["summed"] / losses["n_valid_examples"]).backward()
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
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
