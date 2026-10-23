"""Adaptive self-tuning training algorithm."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 32
_PEAK_LEARNING_RATE = 0.002
_MIN_LEARNING_RATE_RATIO = 0.05
_WEIGHT_DECAY = 0.01
_BETA1 = 0.9
_BETA2 = 0.99
_LABEL_SMOOTHING = 0.05
_WARMUP_EPOCHS = 0.25
_DECAY_EPOCHS = 30.0


def get_batch_size(workload_name: str) -> int:
    """Return one global batch size for every workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize an adaptive optimizer and an example-count schedule."""
    del model_state, hyperparameters, rng
    steps_per_epoch = max(1, math.ceil(workload.num_train_examples / _BATCH_SIZE))
    normalization_parameters = {
        id(parameter)
        for module in model_params.modules()
        if isinstance(
            module,
            (
                torch.nn.BatchNorm1d,
                torch.nn.BatchNorm2d,
                torch.nn.BatchNorm3d,
                torch.nn.SyncBatchNorm,
                torch.nn.GroupNorm,
                torch.nn.LayerNorm,
            ),
        )
        for parameter in module.parameters(recurse=False)
    }
    regularized_parameters = [
        parameter
        for parameter in model_params.parameters()
        if id(parameter) not in normalization_parameters
    ]
    unregularized_parameters = [
        parameter
        for parameter in model_params.parameters()
        if id(parameter) in normalization_parameters
    ]
    optimizer = torch.optim.AdamW(
        (
            {"params": regularized_parameters, "weight_decay": _WEIGHT_DECAY},
            {"params": unregularized_parameters, "weight_decay": 0.0},
        ),
        lr=_PEAK_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        fused=True,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "warmup_steps": max(1, int(_WARMUP_EPOCHS * steps_per_epoch)),
        "decay_steps": max(1, int(_DECAY_EPOCHS * steps_per_epoch)),
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """Take one AdamW step with warmup followed by cosine decay."""
    del current_params_types, hyperparameters, loss_type, eval_results, global_step

    step = optimizer_state["step"]
    warmup_steps = optimizer_state["warmup_steps"]
    if step < warmup_steps:
        learning_rate = _PEAK_LEARNING_RATE * (step + 1) / warmup_steps
    else:
        progress = min((step - warmup_steps) / optimizer_state["decay_steps"], 1.0)
        cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
        learning_rate = _PEAK_LEARNING_RATE * (
            _MIN_LEARNING_RATE_RATIO + (1.0 - _MIN_LEARNING_RATE_RATIO) * cosine
        )

    optimizer = optimizer_state["optimizer"]
    for parameter_group in optimizer.param_groups:
        parameter_group["lr"] = learning_rate
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
        label_smoothing=_LABEL_SMOOTHING,
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """Expose the current training parameters and accumulated model state."""
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
    """Take the next pre-shuffled batch without changing it."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
