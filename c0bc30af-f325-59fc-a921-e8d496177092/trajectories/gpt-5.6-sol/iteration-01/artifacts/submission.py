"""Self-tuning training algorithm for image classification workloads."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LEARNING_RATE = 0.003
_WEIGHT_DECAY = 0.01
_WARMUP_FRACTION = 0.02
_SCHEDULE_MULTIPLIER = 2
_MIN_LEARNING_RATE_RATIO = 0.05


def _learning_rate_multiplier(step: int, total_steps: int) -> float:
    warmup_steps = max(int(total_steps * _WARMUP_FRACTION), 1)
    if step < warmup_steps:
        return float(step + 1) / warmup_steps
    progress = min(
        (step - warmup_steps) / max(total_steps - warmup_steps, 1), 1.0
    )
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _MIN_LEARNING_RATE_RATIO + (1.0 - _MIN_LEARNING_RATE_RATIO) * cosine


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

    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_PEAK_LEARNING_RATE,
        betas=(0.9, 0.99),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
        fused=next(model_params.parameters()).is_cuda,
    )
    total_steps = max(int(workload.step_hint * _SCHEDULE_MULTIPLIER), 1)
    scheduler = torch.optim.lr_scheduler.LambdaLR(
        optimizer,
        lr_lambda=lambda step: _learning_rate_multiplier(step, total_steps),
    )
    return {"optimizer": optimizer, "scheduler": scheduler}


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
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step

    optimizer = optimizer_state["optimizer"]
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
        label_smoothing=0.0,
    )
    (losses["summed"] / losses["n_valid_examples"]).backward()
    optimizer.step()
    optimizer_state["scheduler"].step()

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
