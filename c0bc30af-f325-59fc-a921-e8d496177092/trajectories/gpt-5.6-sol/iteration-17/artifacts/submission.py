"""Adaptive, scheduled training algorithm for the self-tuning ruleset."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_BASE_LEARNING_RATE = 0.00175
_MIN_LEARNING_RATE_FACTOR = 0.1
_WEIGHT_DECAY = 0.01
_BETA1 = 0.9
_BETA2 = 0.99
_WARMUP_DIVISOR = 4
_DECAY_EPOCHS = 24


def _learning_rate(step: int, warmup_steps: int, decay_steps: int) -> float:
    if step < warmup_steps:
        return _BASE_LEARNING_RATE * (step + 1) / warmup_steps
    progress = min((step - warmup_steps) / decay_steps, 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    factor = _MIN_LEARNING_RATE_FACTOR + (
        1.0 - _MIN_LEARNING_RATE_FACTOR
    ) * cosine
    if progress == 1.0:
        factor *= math.sqrt((warmup_steps + decay_steps) / (step + 1))
    return _BASE_LEARNING_RATE * factor


def get_batch_size(workload_name: str) -> int:
    """Return one global training batch size for every workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize AdamW and a schedule scaled by the training set size."""
    del model_state
    del hyperparameters
    del rng

    decay_params = []
    no_decay_params = []
    normalization_layers = (
        torch.nn.modules.batchnorm._BatchNorm,
        torch.nn.GroupNorm,
        torch.nn.LayerNorm,
    )
    for module in model_params.modules():
        parameters = decay_params
        if isinstance(module, normalization_layers):
            parameters = no_decay_params
        parameters.extend(
            parameter
            for parameter in module.parameters(recurse=False)
            if parameter.requires_grad
        )

    optimizer = torch.optim.AdamW(
        [
            {"params": decay_params, "weight_decay": _WEIGHT_DECAY},
            {"params": no_decay_params, "weight_decay": 0.0},
        ],
        lr=_BASE_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=1e-8,
        fused=torch.cuda.is_available(),
    )
    steps_per_epoch = max(workload.num_train_examples // _BATCH_SIZE, 1)
    return {
        "optimizer": optimizer,
        "step": 0,
        "warmup_steps": max(steps_per_epoch // _WARMUP_DIVISOR, 1),
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
    """Take one adaptive update and propagate model auxiliary state."""
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    lr = _learning_rate(
        step, optimizer_state["warmup_steps"], optimizer_state["decay_steps"]
    )
    for group in optimizer.param_groups:
        group["lr"] = lr

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
    """Take the next batch from the harness-provided shuffled queue."""
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
