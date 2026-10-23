"""Self-tuning AdamW with cosine schedule for MNIST family."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import math
import torch

from algoperf import spec

_BATCH_SIZE = 256
_PEAK_LR = 0.01
_END_LR = 0.00002
_WARMUP_STEPS = 50
_TOTAL_STEPS = 1500
_WEIGHT_DECAY = 0.01
_BETA1 = 0.9
_BETA2 = 0.999
_EPS = 1e-8
_GRAD_CLIP = 1.0
_LABEL_SMOOTHING = 0.0


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def _lr_schedule(step: int) -> float:
    if step < _WARMUP_STEPS:
        return _PEAK_LR * (step + 1) / max(1, _WARMUP_STEPS)
    progress = (step - _WARMUP_STEPS) / max(1, _TOTAL_STEPS - _WARMUP_STEPS)
    if progress >= 1.0:
        return _END_LR
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _END_LR + (_PEAK_LR - _END_LR) * cosine


def _update_lr(optimizer: torch.optim.Optimizer, step: int) -> None:
    lr = _lr_schedule(step)
    for pg in optimizer.param_groups:
        pg["lr"] = lr


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
        lr=_lr_schedule(0),
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
    )
    return {"optimizer": optimizer, "step": 0}


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
    del train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]

    _update_lr(optimizer, step)

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
    predictions, next_state = outputs

    losses = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=predictions,
        mask_batch=batch.get("weights"),
        label_smoothing=_LABEL_SMOOTHING,
    )
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()

    if _GRAD_CLIP is not None:
        torch.nn.utils.clip_grad_norm_(
            current_param_container.parameters(), max_norm=_GRAD_CLIP
        )

    optimizer.step()

    optimizer_state["step"] = step + 1
    return optimizer_state, current_param_container, next_state


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
