"""Self-tuning NAdamW submission with warmup and cosine decay."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LEARNING_RATE = 0.003
_MIN_LEARNING_RATE_RATIO = 0.05
_WARMUP_EPOCHS = 0.5
_SCHEDULE_EPOCHS = 8.0
_BETA1 = 0.9
_BETA2 = 0.99
_WEIGHT_DECAY = 0.005
_LABEL_SMOOTHING = 0.0


def get_batch_size(workload_name: str) -> int:
    """Return the training batch size.

    A single value that works across every workload is what the rules allow. Selecting a value by
    identifying the workload is not.
    """
    del workload_name
    return _BATCH_SIZE


def _learning_rate(step: int, steps_per_epoch: int) -> float:
    warmup_steps = max(int(_WARMUP_EPOCHS * steps_per_epoch), 1)
    if step < warmup_steps:
        return _PEAK_LEARNING_RATE * (step + 1) / warmup_steps

    schedule_steps = max(int(_SCHEDULE_EPOCHS * steps_per_epoch), warmup_steps + 1)
    progress = min((step - warmup_steps) / (schedule_steps - warmup_steps), 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    multiplier = _MIN_LEARNING_RATE_RATIO + (1.0 - _MIN_LEARNING_RATE_RATIO) * cosine
    return _PEAK_LEARNING_RATE * multiplier


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize an adaptive optimizer and a workload-scaled schedule."""
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.NAdam(
        model_params.parameters(),
        lr=_PEAK_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
        decoupled_weight_decay=True,
        foreach=True,
    )
    steps_per_epoch = max(workload.num_train_examples // _BATCH_SIZE, 1)
    return {
        "optimizer": optimizer,
        "step": 0,
        "steps_per_epoch": steps_per_epoch,
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
    """Take one NAdamW step and propagate all forward-pass model state."""
    unused = (
        current_params_types,
        hyperparameters,
        eval_results,
        global_step,
        loss_type,
    )
    del unused

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    learning_rate = _learning_rate(step, optimizer_state["steps_per_epoch"])
    for parameter_group in optimizer.param_groups:
        parameter_group["lr"] = learning_rate

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)

    outputs = workload.model_fn(
        params=current_param_container,
        augmented_and_preprocessed_input_batch=batch,
        model_state=model_state,
        mode=spec.ForwardPassMode.TRAIN,
        rng=rng,
        update_batch_norm=True,
    )
    predictions, next_state = outputs

    losses = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=predictions,
        mask_batch=batch.get("weights"),
        label_smoothing=_LABEL_SMOOTHING,
    )
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
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
    """Evaluate the current optimized parameters and accumulated model state."""
    unused = (
        workload,
        current_params_types,
        hyperparameters,
        loss_type,
        eval_results,
        global_step,
        rng,
    )
    del unused
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
    """Take the next batch off the queue, unchanged."""
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
