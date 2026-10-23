"""Self-tuning, adaptive training algorithm for AlgoPerf workloads."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_LEARNING_RATE = 0.003
_BETA1 = 0.9
_BETA2 = 0.999
_EPSILON = 1e-8
_WARMUP_STEPS = 100
_MIN_LR_FACTOR = 0.1


def get_batch_size(workload_name: str) -> int:
    """Return one workload-independent global batch size."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize Adam and a generic warmup/cosine schedule."""
    del model_state, hyperparameters, rng
    optimizer = torch.optim.Adam(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=_EPSILON,
        weight_decay=1e-4,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "decay_steps": max(int(workload.step_hint), _WARMUP_STEPS + 1),
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
    """Take one adaptive gradient step."""
    del current_params_types, hyperparameters, loss_type, eval_results
    del global_step, train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    if step < _WARMUP_STEPS:
        factor = float(step + 1) / float(_WARMUP_STEPS)
    else:
        progress = min(
            1.0,
            float(step - _WARMUP_STEPS)
            / float(optimizer_state["decay_steps"] - _WARMUP_STEPS),
        )
        factor = _MIN_LR_FACTOR + (1.0 - _MIN_LR_FACTOR) * 0.5 * (
            1.0 + math.cos(math.pi * progress)
        )
    optimizer.param_groups[0]["lr"] = _LEARNING_RATE * factor

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
) -> spec.UpdateReturn:
    """Evaluate the directly trained parameters without extra computation."""
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
    """Consume the next pre-shuffled batch."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
