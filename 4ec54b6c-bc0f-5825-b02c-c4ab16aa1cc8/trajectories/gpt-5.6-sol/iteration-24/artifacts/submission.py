"""Self-tuning training algorithm using a lightweight adaptive update."""

from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_BASE_LEARNING_RATE = 0.002
_BETA1 = 0.9
_BETA2 = 0.999
_EPSILON = 1e-8
_WEIGHT_DECAY = 0.0001
_DECAY_START_FRACTION = 0.4
_MIN_LEARNING_RATE_FRACTION = 0.1


def get_batch_size(workload_name: str) -> int:
    """Use one global batch size without identifying the workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize Adam and a workload-provided-horizon decay schedule."""
    del model_state, hyperparameters, rng
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_BASE_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=_EPSILON,
        weight_decay=_WEIGHT_DECAY,
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "decay_start": max(1, int(workload.step_hint * _DECAY_START_FRACTION)),
        "step_hint": max(2, int(workload.step_hint)),
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
    """Take one Adam step, with a cheap late linear decay."""
    del current_params_types, hyperparameters, loss_type, eval_results, global_step

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    decay_start = optimizer_state["decay_start"]
    if step > decay_start:
        span = optimizer_state["step_hint"] - decay_start
        progress = min(1.0, (step - decay_start) / span)
        fraction = 1.0 - progress * (1.0 - _MIN_LEARNING_RATE_FRACTION)
        optimizer.param_groups[0]["lr"] = _BASE_LEARNING_RATE * fraction

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
    """Consume the next independently shuffled minibatch."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
