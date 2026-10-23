"""Self-tuning training algorithm for image classification workloads."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 192
_MAX_LEARNING_RATE = 0.004
_MIN_LEARNING_RATE = 0.00004
_WEIGHT_DECAY = 0.01
_WARMUP_EPOCHS = 1
_CYCLE_EPOCHS = 20
_EMA_DECAY = 0.995
_EMA_START_EPOCH = 2


class _TrainingState:
    """Checkpointable state for averaging and scheduling."""

    def __init__(self, parameters: List[torch.Tensor], steps_per_epoch: int):
        self.steps_per_epoch = steps_per_epoch
        self.ema_start = _EMA_START_EPOCH * steps_per_epoch
        self.ema = [parameter.detach().clone() for parameter in parameters]
        self.train_weights = [
            parameter.detach().clone() for parameter in parameters
        ]
        self.ema_updates = 0
        self.eval_swapped = False

    def state_dict(self) -> Dict[str, Any]:
        return {
            "steps_per_epoch": self.steps_per_epoch,
            "ema_start": self.ema_start,
            "ema": self.ema,
            "train_weights": self.train_weights,
            "ema_updates": self.ema_updates,
            "eval_swapped": self.eval_swapped,
        }

    def load_state_dict(self, state: Dict[str, Any]) -> None:
        self.steps_per_epoch = state["steps_per_epoch"]
        self.ema_start = state["ema_start"]
        self.ema = state["ema"]
        self.train_weights = state["train_weights"]
        self.ema_updates = state["ema_updates"]
        self.eval_swapped = state["eval_swapped"]


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
    """Initialize AdamW, an example-count schedule, and evaluation EMA."""
    del model_state, hyperparameters, rng
    parameters = list(model_params.parameters())
    optimizer = torch.optim.AdamW(
        parameters,
        lr=_MAX_LEARNING_RATE,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
        fused=parameters[0].is_cuda,
    )
    steps_per_epoch = max(1, workload.num_train_examples // _BATCH_SIZE)
    return {
        "optimizer": optimizer,
        "state": _TrainingState(parameters, steps_per_epoch),
    }


def _set_learning_rate(
    optimizer: torch.optim.Optimizer, step: int, steps_per_epoch: int
) -> None:
    warmup_steps = _WARMUP_EPOCHS * steps_per_epoch
    if step < warmup_steps:
        progress = (step + 1) / warmup_steps
        learning_rate = _MIN_LEARNING_RATE + (
            _MAX_LEARNING_RATE - _MIN_LEARNING_RATE
        ) * progress
    else:
        decay_steps = (_CYCLE_EPOCHS - _WARMUP_EPOCHS) * steps_per_epoch
        progress = ((step - warmup_steps) % decay_steps) / decay_steps
        learning_rate = _MIN_LEARNING_RATE + 0.5 * (
            _MAX_LEARNING_RATE - _MIN_LEARNING_RATE
        ) * (1.0 + math.cos(math.pi * progress))
    for group in optimizer.param_groups:
        group["lr"] = learning_rate


@torch.no_grad()
def _swap_evaluation_weights(
    state: _TrainingState,
    model: spec.ParameterContainer,
) -> None:
    parameters = list(model.parameters())
    if state.eval_swapped:
        torch._foreach_copy_(parameters, state.train_weights)
    else:
        torch._foreach_copy_(state.train_weights, parameters)
        torch._foreach_copy_(parameters, state.ema)
    state.eval_swapped = not state.eval_swapped


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
    """Take one adaptive step and update the evaluation-weight average."""
    del current_params_types, hyperparameters, loss_type, eval_results, train_state
    state = optimizer_state["state"]
    if state.eval_swapped:
        _swap_evaluation_weights(state, current_param_container)

    optimizer = optimizer_state["optimizer"]
    _set_learning_rate(optimizer, global_step, state.steps_per_epoch)
    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)

    with torch.autocast(
        device_type="cuda",
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
    (losses["summed"] / losses["n_valid_examples"]).backward()
    optimizer.step()

    if global_step == state.ema_start:
        torch._foreach_copy_(state.ema, list(current_param_container.parameters()))
    elif global_step > state.ema_start:
        parameters = list(current_param_container.parameters())
        decay = min(
            _EMA_DECAY, (state.ema_updates + 1.0) / (state.ema_updates + 10.0)
        )
        torch._foreach_lerp_(state.ema, parameters, 1.0 - decay)
        state.ema_updates += 1

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
    """Expose averaged parameters after enough training updates."""
    del workload, current_params_types, hyperparameters, loss_type, eval_results, global_step, rng
    state = optimizer_state["state"]
    if state.ema_updates and not state.eval_swapped:
        _swap_evaluation_weights(state, current_param_container)
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
    """Select the next shuffled and augmented batch."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
