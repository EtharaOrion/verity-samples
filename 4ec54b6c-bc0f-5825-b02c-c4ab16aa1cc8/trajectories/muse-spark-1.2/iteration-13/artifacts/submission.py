"""Fast MNIST training: AdamW with cosine warmup, tuned for robustness."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import math

import torch

from algoperf import spec

_BATCH_SIZE = 256
_BASE_LR = 0.003
_WEIGHT_DECAY = 0.01
_WARMUP_FRAC = 0.1


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
    del workload
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_BASE_LR,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
    )
    return {"optimizer": optimizer}


def _lr_schedule(step: int, total_steps: int) -> float:
    warmup_steps = int(total_steps * _WARMUP_FRAC)
    if step < warmup_steps:
        return _BASE_LR * (step + 1) / max(warmup_steps, 1)
    progress = (step - warmup_steps) / max(total_steps - warmup_steps, 1)
    return _BASE_LR * 0.5 * (1.0 + math.cos(math.pi * progress))


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
    del eval_results
    del loss_type
    optimizer = optimizer_state["optimizer"]
    lr = _lr_schedule(global_step, workload.step_hint)
    for param_group in optimizer.param_groups:
        param_group["lr"] = lr
    current_param_container.train()
    optimizer.zero_grad()
    predictions, new_model_state = workload.model_fn(
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
    )
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), 1.0)
    optimizer.step()
    return optimizer_state, current_param_container, new_model_state


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
