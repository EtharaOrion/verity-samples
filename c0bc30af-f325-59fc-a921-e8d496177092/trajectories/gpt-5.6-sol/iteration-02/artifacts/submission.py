"""Adaptive, scheduled training algorithm for the self-tuning ruleset."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LEARNING_RATE = 0.003
_FINAL_LR_RATIO = 0.03
_WARMUP_RATIO = 0.02
_WEIGHT_DECAY = 0.01


def _learning_rate(step: int, total_steps: int) -> float:
    warmup_steps = max(1, int(_WARMUP_RATIO * total_steps))
    if step < warmup_steps:
        return _PEAK_LEARNING_RATE * float(step + 1) / warmup_steps
    progress = min(
        1.0, (step - warmup_steps) / max(1, total_steps - warmup_steps)
    )
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _PEAK_LEARNING_RATE * (
        _FINAL_LR_RATIO + (1.0 - _FINAL_LR_RATIO) * cosine
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
        model_params.parameters(),
        lr=_learning_rate(0, workload.step_hint),
        betas=(0.9, 0.99),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
        fused=torch.cuda.is_available(),
    )
    return {"optimizer": optimizer, "total_steps": workload.step_hint}


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
) -> spec.UpdateReturn:
    del current_params_types, hyperparameters, loss_type, eval_results

    optimizer = optimizer_state["optimizer"]
    optimizer.param_groups[0]["lr"] = _learning_rate(
        global_step, optimizer_state["total_steps"]
    )
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
