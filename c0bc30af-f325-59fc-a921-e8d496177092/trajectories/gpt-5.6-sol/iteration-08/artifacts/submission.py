"""Self-tuning adaptive optimizer with warmup and cosine decay."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_LEARNING_RATE = 0.0017486387539278373
_BETA1 = 0.93266073836
_BETA2 = 0.9955159689799007
_WEIGHT_DECAY = 0.08121616522670176
_WARMUP_FRACTION = 0.02


def _nadamw_step(optimizer: torch.optim.Optimizer) -> None:
    """Apply Nesterov Adam with decoupled weight decay."""
    with torch.no_grad():
        for group in optimizer.param_groups:
            beta1, beta2 = group["betas"]
            for param in group["params"]:
                if param.grad is None:
                    continue
                grad = param.grad
                state = optimizer.state[param]
                if not state:
                    state["step"] = torch.tensor(0.0)
                    state["exp_avg"] = torch.zeros_like(param)
                    state["exp_avg_sq"] = torch.zeros_like(param)

                state["step"] += 1
                step = state["step"].item()
                exp_avg = state["exp_avg"]
                exp_avg_sq = state["exp_avg_sq"]
                param.mul_(1.0 - group["lr"] * group["weight_decay"])
                exp_avg.mul_(beta1).add_(grad, alpha=1.0 - beta1)
                exp_avg_sq.mul_(beta2).addcmul_(
                    grad, grad, value=1.0 - beta2
                )
                exp_avg.mul_(beta1).add_(grad, alpha=1.0 - beta1)
                denominator = exp_avg_sq.sqrt()
                denominator.div_(math.sqrt(1.0 - beta2**step))
                denominator.add_(group["eps"])
                step_size = -group["lr"] / (1.0 - beta1**step)
                param.addcdiv_(exp_avg, denominator, value=step_size)
                exp_avg.sub_(grad, alpha=1.0 - beta1).div_(beta1)


def get_batch_size(workload_name: str) -> int:
    """Return one global batch size without identifying the workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize NAdam with a schedule derived from the workload step hint."""
    del model_state, hyperparameters, rng
    optimizer = torch.optim.SGD(model_params.parameters(), lr=_LEARNING_RATE)
    schedule_steps = max(int(workload.step_hint), 2)
    warmup_steps = max(int(_WARMUP_FRACTION * schedule_steps), 1)
    for group in optimizer.param_groups:
        group["betas"] = (_BETA1, _BETA2)
        group["eps"] = 1e-8
        group["weight_decay"] = _WEIGHT_DECAY
        group["base_lr"] = _LEARNING_RATE
        group["schedule_steps"] = schedule_steps
        group["warmup_steps"] = warmup_steps
    return {"optimizer": optimizer}


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
    """Apply one adaptive update and propagate forward-pass model state."""
    del current_params_types, hyperparameters, loss_type, eval_results, train_state
    optimizer = optimizer_state["optimizer"]
    group = optimizer.param_groups[0]
    warmup_steps = group["warmup_steps"]
    schedule_steps = group["schedule_steps"]
    if global_step < warmup_steps:
        factor = float(global_step + 1) / warmup_steps
    else:
        progress = float(global_step - warmup_steps) / (
            schedule_steps - warmup_steps
        )
        factor = 0.5 * (1.0 + math.cos(math.pi * progress))
    for group in optimizer.param_groups:
        group["lr"] = group["base_lr"] * factor

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
    _nadamw_step(optimizer)
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
    """Evaluate the current iterate and its accumulated model state."""
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
    """Take the next pre-shuffled batch without modifying it."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
