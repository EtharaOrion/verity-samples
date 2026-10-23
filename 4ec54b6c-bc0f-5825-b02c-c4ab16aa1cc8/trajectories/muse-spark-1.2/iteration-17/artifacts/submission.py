"""Self-tuning AdamW with warmup+cosine."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR

from algoperf import spec

_BATCH_SIZE = 256
_LEARNING_RATE = 0.008
_WEIGHT_DECAY = 0.005
_BETA1 = 0.9
_BETA2 = 0.999
_EPS = 1e-8
_WARMUP_FACTOR = 0.05
_LABEL_SMOOTHING = 0.0
_GRAD_CLIP = None


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
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
    )
    base_hint = workload.step_hint
    horizon = int(base_hint * 64 / _BATCH_SIZE * 2)
    if horizon < 1000:
        horizon = 1000
    warmup_steps = int(_WARMUP_FACTOR * horizon)
    if warmup_steps > 0:
        warmup = LinearLR(
            optimizer, start_factor=0.1, end_factor=1.0, total_iters=warmup_steps
        )
        cosine_steps = max(horizon - warmup_steps, 1)
        cosine = CosineAnnealingLR(optimizer, T_max=cosine_steps)
        scheduler = SequentialLR(
            optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps]
        )
    else:
        scheduler = CosineAnnealingLR(optimizer, T_max=horizon)
    return {"optimizer": optimizer, "scheduler": scheduler, "step": 0}


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
    scheduler = optimizer_state["scheduler"]
    current_param_container.train()
    optimizer.zero_grad()
    logits, new_model_state = workload.model_fn(
        params=current_param_container,
        augmented_and_preprocessed_input_batch=batch,
        model_state=model_state,
        mode=spec.ForwardPassMode.TRAIN,
        rng=rng,
        update_batch_norm=True,
    )
    loss_dict = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=logits,
        mask_batch=batch.get("weights"),
        label_smoothing=_LABEL_SMOOTHING,
    )
    loss = loss_dict["summed"] / loss_dict["n_valid_examples"]
    loss.backward()
    if _GRAD_CLIP is not None:
        torch.nn.utils.clip_grad_norm_(
            current_param_container.parameters(), max_norm=_GRAD_CLIP
        )
    optimizer.step()
    scheduler.step()
    optimizer_state["step"] = global_step + 1
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
