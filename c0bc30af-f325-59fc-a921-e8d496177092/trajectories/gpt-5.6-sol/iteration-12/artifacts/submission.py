import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_BASE_LR = 0.002
_BETA1 = 0.9
_BETA2 = 0.99
_WEIGHT_DECAY = 0.02
_WARMUP_FRACTION = 0.02
_MIN_LR_FRACTION = 0.02
_LABEL_SMOOTHING = 0.05


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
    optimizer = torch.optim.NAdam(
        model_params.parameters(),
        lr=_BASE_LR,
        betas=(_BETA1, _BETA2),
        weight_decay=_WEIGHT_DECAY,
        decoupled_weight_decay=True,
        foreach=True,
    )
    horizon = max(int(workload.step_hint), 1)
    return {
        "optimizer": optimizer,
        "step": 0,
        "horizon": horizon,
        "warmup": max(int(_WARMUP_FRACTION * horizon), 1),
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
    warmup = optimizer_state["warmup"]
    horizon = optimizer_state["horizon"]
    if step < warmup:
        lr_fraction = (step + 1) / warmup
    else:
        progress = min((step - warmup) / max(horizon - warmup, 1), 1.0)
        lr_fraction = _MIN_LR_FRACTION + 0.5 * (
            1.0 - _MIN_LR_FRACTION
        ) * (1.0 + math.cos(math.pi * progress))
    for group in optimizer.param_groups:
        group["lr"] = _BASE_LR * lr_fraction

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
        label_smoothing=_LABEL_SMOOTHING,
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
