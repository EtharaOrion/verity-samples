"""Workload-agnostic self-tuning PyTorch training algorithm."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_BASE_LEARNING_RATE = 0.003
_BETA1 = 0.9
_BETA2 = 0.999
_EPSILON = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_FRACTION = 0.001
_MIN_LR_FACTOR = 0.1


def _learning_rate(step: int, warmup_steps: int, decay_steps: int) -> float:
    """Linear warmup followed by cosine decay to a nonzero floor."""
    if step < warmup_steps:
        return _BASE_LEARNING_RATE * float(step + 1) / float(warmup_steps)
    progress = min(1.0, float(step - warmup_steps) / float(max(1, decay_steps - warmup_steps)))
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _BASE_LEARNING_RATE * (_MIN_LR_FACTOR + (1.0 - _MIN_LR_FACTOR) * cosine)


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
    decay_steps = max(1, int(workload.step_hint))
    warmup_steps = max(1, int(_WARMUP_FRACTION * decay_steps))
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_learning_rate(0, warmup_steps, decay_steps),
        betas=(_BETA1, _BETA2),
        eps=_EPSILON,
        weight_decay=_WEIGHT_DECAY,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "warmup_steps": warmup_steps,
        "decay_steps": decay_steps,
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
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step

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
