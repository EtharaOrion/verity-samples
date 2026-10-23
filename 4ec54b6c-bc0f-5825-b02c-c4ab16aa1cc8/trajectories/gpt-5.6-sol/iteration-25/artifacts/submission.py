"""Self-tuning training algorithm using Nesterov momentum and a conservative schedule."""

from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_PEAK_LEARNING_RATE = 0.12
_WARMUP_STEPS = 20
_DECAY_START = 700
_DECAY_RATE = 0.998
_MIN_LEARNING_RATE = 0.006


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
    """Initialize Nesterov momentum; no externally tuned values are required."""
    del workload, model_state, hyperparameters, rng
    optimizer = torch.optim.SGD(
        model_params.parameters(),
        lr=_PEAK_LEARNING_RATE / _WARMUP_STEPS,
        momentum=0.9,
        nesterov=True,
        weight_decay=1e-4,
    )
    return {"optimizer": optimizer, "step": 0}


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
    """Take one Nesterov step and update a cheap deterministic learning-rate schedule."""
    del current_params_types, hyperparameters, loss_type, eval_results, global_step

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    if step < _WARMUP_STEPS:
        learning_rate = _PEAK_LEARNING_RATE * (step + 1) / _WARMUP_STEPS
    elif step < _DECAY_START:
        learning_rate = _PEAK_LEARNING_RATE
    else:
        learning_rate = max(
            _MIN_LEARNING_RATE,
            _PEAK_LEARNING_RATE * (_DECAY_RATE ** (step - _DECAY_START + 1)),
        )
    optimizer.param_groups[0]["lr"] = learning_rate

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
    """Consume the next already shuffled batch without additional overhead."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
