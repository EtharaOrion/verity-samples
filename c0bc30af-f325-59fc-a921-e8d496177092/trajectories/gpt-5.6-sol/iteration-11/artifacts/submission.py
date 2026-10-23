from typing import Any, Dict, Iterator, List, Optional, Tuple

import math
import torch

from algoperf import spec

_BATCH_SIZE = 64
_MAX_LEARNING_RATE = 0.1
_MIN_LEARNING_RATE = 0.001
_MOMENTUM = 0.9
_WEIGHT_DECAY = 0.0005
_WARMUP_EPOCHS = 1.0
_CYCLE_EPOCHS = 8.0


def _learning_rate(step: int, steps_per_epoch: int) -> float:
    cycle_steps = max(int(_CYCLE_EPOCHS * steps_per_epoch), 1)
    warmup_steps = max(int(_WARMUP_EPOCHS * steps_per_epoch), 1)
    cycle = step // cycle_steps
    cycle_step = step % cycle_steps
    peak = _MAX_LEARNING_RATE if cycle == 0 else _MAX_LEARNING_RATE / 4.0
    if cycle_step < warmup_steps:
        progress = (cycle_step + 1) / warmup_steps
        return _MIN_LEARNING_RATE + progress * (peak - _MIN_LEARNING_RATE)
    progress = (cycle_step - warmup_steps) / max(cycle_steps - warmup_steps, 1)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _MIN_LEARNING_RATE + cosine * (peak - _MIN_LEARNING_RATE)


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
    steps_per_epoch = max(workload.num_train_examples // _BATCH_SIZE, 1)
    optimizer = torch.optim.SGD(
        model_params.parameters(),
        lr=_learning_rate(0, steps_per_epoch),
        momentum=_MOMENTUM,
        weight_decay=_WEIGHT_DECAY,
        nesterov=True,
    )
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
    train_state: Optional[Dict[str, Any]] = None,
) -> spec.UpdateReturn:
    del current_params_types, hyperparameters, loss_type, eval_results
    del global_step, train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    lr = _learning_rate(step, optimizer_state["steps_per_epoch"])
    for group in optimizer.param_groups:
        group["lr"] = lr

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
