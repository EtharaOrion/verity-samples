"""Self-tuning training submission using a low-overhead AdamW update."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_BASE_LEARNING_RATE = 0.004
_WEIGHT_DECAY = 0.0001
_WARMUP_STEPS = 20
_MIN_LR_FACTOR = 0.1


def _learning_rate(step: int, step_hint: int) -> float:
    """Short warmup followed by a gentle, workload-provided cosine schedule."""
    if step < _WARMUP_STEPS:
        return _BASE_LEARNING_RATE * float(step + 1) / float(_WARMUP_STEPS)
    decay_steps = max(int(step_hint) - _WARMUP_STEPS, 1)
    progress = min(max(float(step - _WARMUP_STEPS) / decay_steps, 0.0), 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _BASE_LEARNING_RATE * (_MIN_LR_FACTOR + (1.0 - _MIN_LR_FACTOR) * cosine)


def get_batch_size(workload_name: str) -> int:
    """Use one moderate batch size for all workloads."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize AdamW and its parameter-independent schedule state."""
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_learning_rate(0, workload.step_hint),
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "step_hint": max(int(workload.step_hint * 64 / _BATCH_SIZE), 1),
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
    """Compute one minibatch gradient and apply an adaptive scheduled update."""
    unused = (current_params_types, hyperparameters, loss_type, eval_results, global_step)
    del unused

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    lr = _learning_rate(step, optimizer_state["step_hint"])
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
    (losses["summed"] / losses["n_valid_examples"]).backward()
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
    """Consume the next shuffled minibatch without extra selection overhead."""
    unused = (
        workload,
        optimizer_state,
        current_param_container,
        model_state,
        hyperparameters,
        global_step,
        rng,
    )
    del unused
    return next(input_queue)
