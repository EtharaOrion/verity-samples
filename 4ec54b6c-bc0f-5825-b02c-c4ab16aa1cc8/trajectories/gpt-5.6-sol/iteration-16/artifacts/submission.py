"""Self-tuning training algorithm for AlgoPerf workloads."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import math
import torch

from algoperf import spec

_BATCH_SIZE = 64
_PEAK_LEARNING_RATE = 0.003
_WARMUP_STEPS = 16
_HOLD_FRACTION = 0.20
_MIN_LR_FACTOR = 0.05
_BETA1 = 0.9
_BETA2 = 0.99
_EPSILON = 1e-8
_WEIGHT_DECAY = 0.0
_EMA_DECAY = 0.99


def _learning_rate_factor(step: int, total_steps: int) -> float:
    """Fast warmup followed by a hold and smooth decay."""
    if step < _WARMUP_STEPS:
        return float(step + 1) / float(_WARMUP_STEPS)
    hold_steps = max(_WARMUP_STEPS + 1, int(total_steps * _HOLD_FRACTION))
    if step < hold_steps:
        return 1.0
    decay_steps = max(1, total_steps - hold_steps)
    progress = min(1.0, float(step - hold_steps) / float(decay_steps))
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _MIN_LR_FACTOR + (1.0 - _MIN_LR_FACTOR) * cosine


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
    optimizer = torch.optim.Adam(
        model_params.parameters(),
        lr=_PEAK_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=_EPSILON,
        weight_decay=_WEIGHT_DECAY,
    )
    total_steps = max(_WARMUP_STEPS + 2, int(workload.step_hint))
    scheduler = torch.optim.lr_scheduler.LambdaLR(
        optimizer, lr_lambda=lambda step: _learning_rate_factor(step, total_steps)
    )
    ema_params = [p.detach().clone() for p in model_params.parameters()]
    return {
        "optimizer": optimizer,
        "scheduler": scheduler,
        "ema_params": ema_params,
        "raw_params": None,
        "step": 0,
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
    del current_params_types, hyperparameters, loss_type
    del eval_results, global_step, train_state

    optimizer = optimizer_state["optimizer"]
    parameters = list(current_param_container.parameters())
    raw_params = optimizer_state["raw_params"]
    if raw_params is not None:
        with torch.no_grad():
            for parameter, raw in zip(parameters, raw_params):
                parameter.copy_(raw)
        optimizer_state["raw_params"] = None
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
    with torch.no_grad():
        for average, parameter in zip(optimizer_state["ema_params"], parameters):
            average.lerp_(parameter, 1.0 - _EMA_DECAY)
    optimizer_state["scheduler"].step()
    optimizer_state["step"] += 1
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
    parameters = list(current_param_container.parameters())
    with torch.no_grad():
        optimizer_state["raw_params"] = [
            parameter.detach().clone() for parameter in parameters
        ]
        for parameter, average in zip(parameters, optimizer_state["ema_params"]):
            parameter.copy_(average)
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
