"""Self-tuning training algorithm for image classification workloads."""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch
import torch.distributed as dist
import torch.distributed.nn.functional as dist_nn

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LEARNING_RATE = 0.002
_MIN_LEARNING_RATE = 0.00002
_WEIGHT_DECAY = 0.02
_WARMUP_EPOCHS = 1.0
_DECAY_EPOCHS = 24.0
_BETA1 = 0.9
_BETA2 = 0.995


def _parameter_groups(model: torch.nn.Module) -> List[Dict[str, Any]]:
    normalization_types = (
        torch.nn.modules.batchnorm._BatchNorm,
        torch.nn.GroupNorm,
        torch.nn.LayerNorm,
    )
    no_decay = set()
    for module in model.modules():
        if isinstance(module, normalization_types):
            no_decay.update(id(parameter) for parameter in module.parameters(False))
        bias = getattr(module, "bias", None)
        if isinstance(bias, torch.nn.Parameter):
            no_decay.add(id(bias))

    regularized = []
    unregularized = []
    for parameter in model.parameters():
        if id(parameter) in no_decay:
            unregularized.append(parameter)
        else:
            regularized.append(parameter)
    return [
        {"params": regularized, "weight_decay": _WEIGHT_DECAY},
        {"params": unregularized, "weight_decay": 0.0},
    ]


def _learning_rate(step: int, steps_per_epoch: int) -> float:
    warmup_steps = max(1, int(_WARMUP_EPOCHS * steps_per_epoch))
    decay_steps = max(1, int(_DECAY_EPOCHS * steps_per_epoch))
    if step < warmup_steps:
        return _PEAK_LEARNING_RATE * float(step + 1) / float(warmup_steps)
    progress = min(float(step - warmup_steps) / float(decay_steps), 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _MIN_LEARNING_RATE + (
        _PEAK_LEARNING_RATE - _MIN_LEARNING_RATE
    ) * cosine


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
    del model_state
    del hyperparameters
    del rng
    steps_per_epoch = max(1, workload.num_train_examples // _BATCH_SIZE)
    optimizer = torch.optim.AdamW(
        _parameter_groups(model_params),
        lr=_learning_rate(0, steps_per_epoch),
        betas=(_BETA1, _BETA2),
        eps=1e-8,
        fused=torch.cuda.is_available(),
    )
    return {"optimizer": optimizer, "step": 0, "steps_per_epoch": steps_per_epoch}


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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    learning_rate = _learning_rate(step, optimizer_state["steps_per_epoch"])
    for group in optimizer.param_groups:
        group["lr"] = learning_rate

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
    summed_loss = losses["summed"]
    valid_examples = losses["n_valid_examples"]
    if dist.is_available() and dist.is_initialized():
        summed_loss = dist_nn.all_reduce(summed_loss)
        valid_examples = dist_nn.all_reduce(valid_examples)
    (summed_loss / valid_examples).backward()
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
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
