"""Self-tuning adaptive training algorithm for AlgoPerf workloads."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_BASE_LEARNING_RATE = 0.003
_WEIGHT_DECAY = 0.01
_BETA1 = 0.9
_BETA2 = 0.99
_WARMUP_FRACTION = 0.02
_MIN_LR_FACTOR = 0.02
_LABEL_SMOOTHING = 0.05


def _learning_rate(step: int, warmup_steps: int, total_steps: int) -> float:
    if step < warmup_steps:
        return _BASE_LEARNING_RATE * float(step + 1) / float(warmup_steps)
    progress = min(float(step - warmup_steps) / float(total_steps - warmup_steps), 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    factor = _MIN_LR_FACTOR + (1.0 - _MIN_LR_FACTOR) * cosine
    return _BASE_LEARNING_RATE * factor


def _parameter_groups(model: torch.nn.Module) -> List[Dict[str, Any]]:
    no_decay = set()
    normalization_types = (
        torch.nn.modules.batchnorm._BatchNorm,
        torch.nn.GroupNorm,
        torch.nn.LayerNorm,
    )
    for module in model.modules():
        for name, parameter in module.named_parameters(recurse=False):
            if name == "bias" or isinstance(module, normalization_types):
                no_decay.add(id(parameter))
    decay_params = []
    no_decay_params = []
    for parameter in model.parameters():
        if id(parameter) in no_decay:
            no_decay_params.append(parameter)
        else:
            decay_params.append(parameter)
    return [
        {"params": decay_params, "weight_decay": _WEIGHT_DECAY},
        {"params": no_decay_params, "weight_decay": 0.0},
    ]


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
    """Initialize AdamW and a schedule derived from the workload step hint."""
    del model_state
    del hyperparameters
    del rng

    total_steps = max(int(workload.step_hint), 2)
    warmup_steps = max(int(_WARMUP_FRACTION * total_steps), 1)
    optimizer = torch.optim.AdamW(
        _parameter_groups(model_params),
        lr=_BASE_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=1e-8,
        fused=torch.cuda.is_available(),
    )
    return {
        "optimizer": optimizer,
        "step": 0,
        "warmup_steps": warmup_steps,
        "total_steps": total_steps,
        "last_eval_step": -1,
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
    """Apply one adaptive update and retain the forward pass auxiliary state."""
    del current_params_types
    del hyperparameters
    del loss_type
    del global_step
    del train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    if eval_results:
        eval_step, latest_result = eval_results[-1]
        if eval_step != optimizer_state["last_eval_step"]:
            optimizer_state["last_eval_step"] = eval_step
            schedule_end = optimizer_state["total_steps"]
            if (
                step * 4 >= schedule_end * 3
                and not workload.has_reached_validation_target(latest_result)
            ):
                optimizer_state["total_steps"] = max(schedule_end * 2, step + 2)
    lr = _learning_rate(
        step, optimizer_state["warmup_steps"], optimizer_state["total_steps"]
    )
    for group in optimizer.param_groups:
        group["lr"] = lr

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)
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
        label_smoothing=_LABEL_SMOOTHING,
    )
    (losses["summed"] / losses["n_valid_examples"]).backward()
    optimizer.step()

    optimizer_state["step"] = step + 1
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
    """Evaluate the current parameters and accumulated model state."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng
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
    """Take the next pre-shuffled batch from the input queue."""
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
