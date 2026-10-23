"""Self-tuning AdamW with cosine warmup; single config robust across seeds."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR

from algoperf import spec

_BATCH_SIZE = 128
_LEARNING_RATE = 0.005
_WEIGHT_DECAY = 0.01
_WARMUP_FRACTION = 0.08


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def _get_scheduler(optimizer, total_steps: int):
    warmup_steps = max(1, int(total_steps * _WARMUP_FRACTION))
    warmup = LinearLR(
        optimizer, start_factor=0.1, end_factor=1.0, total_iters=warmup_steps
    )
    cosine_steps = max(1, total_steps - warmup_steps)
    cosine = CosineAnnealingLR(
        optimizer, T_max=cosine_steps, eta_min=_LEARNING_RATE * 0.02
    )
    return SequentialLR(
        optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps]
    )


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
        lr=_LEARNING_RATE,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
    )
    try:
        hint = workload.step_hint
    except Exception:
        hint = 7813
    total_steps = int(hint * 64 // _BATCH_SIZE)
    total_steps = max(total_steps, 2000)
    scheduler = _get_scheduler(optimizer, total_steps)
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
    del eval_results
    del loss_type
    del global_step
    optimizer = optimizer_state["optimizer"]
    scheduler = optimizer_state["scheduler"]
    current_param_container.train()
    optimizer.zero_grad()
    outputs = workload.model_fn(
        params=current_param_container,
        augmented_and_preprocessed_input_batch=batch,
        model_state=model_state,
        mode=spec.ForwardPassMode.TRAIN,
        rng=rng,
        update_batch_norm=True,
    )
    predictions, new_model_state = outputs
    losses = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=predictions,
        mask_batch=batch.get("weights"),
        label_smoothing=0.0,
    )
    loss = losses["summed"] / losses["n_valid_examples"]
    loss.backward()
    torch.nn.utils.clip_grad_norm_(
        current_param_container.parameters(), max_norm=1.0
    )
    optimizer.step()
    scheduler.step()
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
