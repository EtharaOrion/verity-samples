"""Adaptive, scheduled training algorithm for the self-tuning ruleset."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch
import torch.distributed.nn.functional as dist_nn
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR
from torch.optim.swa_utils import AveragedModel, get_ema_multi_avg_fn

from algoperf import spec

_BATCH_SIZE = 128
_LEARNING_RATE = 0.001
_WEIGHT_DECAY = 0.01
_LABEL_SMOOTHING = 0.05
_WARMUP_EPOCHS = 1
_SCHEDULE_EPOCHS = 30


def _optimizer_parameter_groups(
    model: spec.ParameterContainer,
) -> List[Dict[str, Any]]:
    no_decay_ids = set()
    normalization_layers = (
        torch.nn.modules.batchnorm._BatchNorm,
        torch.nn.GroupNorm,
        torch.nn.LayerNorm,
    )
    for module in model.modules():
        if isinstance(module, normalization_layers):
            no_decay_ids.update(id(parameter) for parameter in module.parameters(False))
        bias = getattr(module, "bias", None)
        if isinstance(bias, torch.nn.Parameter):
            no_decay_ids.add(id(bias))

    decay = []
    no_decay = []
    for parameter in model.parameters():
        if id(parameter) in no_decay_ids:
            no_decay.append(parameter)
        else:
            decay.append(parameter)
    return [
        {"params": decay, "weight_decay": _WEIGHT_DECAY},
        {"params": no_decay, "weight_decay": 0.0},
    ]


def _swap_parameters(
    model: spec.ParameterContainer,
    averaged_model: AveragedModel,
) -> None:
    with torch.no_grad():
        for parameter, averaged_parameter in zip(
            model.parameters(), averaged_model.parameters()
        ):
            parameter.data, averaged_parameter.data = (
                averaged_parameter.data,
                parameter.data,
            )


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

    optimizer = torch.optim.AdamW(
        _optimizer_parameter_groups(model_params),
        lr=_LEARNING_RATE,
        betas=(0.9, 0.99),
    )
    steps_per_epoch = max(
        (workload.num_train_examples + _BATCH_SIZE - 1) // _BATCH_SIZE, 1
    )
    warmup_steps = _WARMUP_EPOCHS * steps_per_epoch
    schedule_steps = _SCHEDULE_EPOCHS * steps_per_epoch
    warmup = LinearLR(
        optimizer,
        start_factor=0.1,
        end_factor=1.0,
        total_iters=warmup_steps,
    )
    cosine = CosineAnnealingLR(
        optimizer,
        T_max=max(schedule_steps - warmup_steps, 1),
        eta_min=0.05 * _LEARNING_RATE,
    )
    scheduler = SequentialLR(
        optimizer,
        schedulers=[warmup, cosine],
        milestones=[warmup_steps],
    )
    averaged_model = AveragedModel(
        model_params,
        multi_avg_fn=get_ema_multi_avg_fn(0.99),
        use_buffers=False,
    )
    return {
        "optimizer": optimizer,
        "scheduler": scheduler,
        "averaged_model": averaged_model,
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    del current_params_types, hyperparameters, loss_type, train_state

    optimizer = optimizer_state["optimizer"]
    averaged_model = optimizer_state["averaged_model"]
    if eval_results and eval_results[-1][0] == global_step:
        _swap_parameters(current_param_container, averaged_model)
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
    summed_loss = losses["summed"]
    valid_examples = losses["n_valid_examples"]
    if torch.distributed.is_initialized():
        summed_loss = dist_nn.all_reduce(summed_loss)
        valid_examples = dist_nn.all_reduce(valid_examples)
    mean_loss = summed_loss / valid_examples
    mean_loss.backward()

    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), 5.0)
    optimizer.step()
    optimizer_state["scheduler"].step()
    averaged_model.update_parameters(current_param_container)
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
    del workload, current_params_types, hyperparameters, loss_type
    del eval_results, global_step, rng
    _swap_parameters(current_param_container, optimizer_state["averaged_model"])
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
