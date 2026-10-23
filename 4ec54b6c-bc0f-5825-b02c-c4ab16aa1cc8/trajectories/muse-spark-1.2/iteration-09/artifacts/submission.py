"""Fast self-tuning submission for mnist_fine_grained."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR

from algoperf import spec

_BATCH_SIZE = 128
_LEARNING_RATE = 0.003
_WEIGHT_DECAY = 0.001
_BETA1 = 0.9
_BETA2 = 0.999
_EPS = 1e-8
_WARMUP_FRACTION = 0.03


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def _get_warmup_steps(step_hint: int) -> int:
    ws = int(step_hint * _WARMUP_FRACTION)
    if ws < 50:
        ws = 50
    if ws > 1000:
        ws = 1000
    return ws


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
    step_hint = getattr(workload, "step_hint", 7813)
    try:
        step_hint = int(step_hint)
    except Exception:
        step_hint = 7813
    warmup_steps = _get_warmup_steps(step_hint)
    warmup = LinearLR(
        optimizer,
        start_factor=1e-8,
        end_factor=1.0,
        total_iters=warmup_steps,
    )
    cosine_steps = max(step_hint - warmup_steps, 1)
    cosine = CosineAnnealingLR(optimizer, T_max=cosine_steps)
    scheduler = SequentialLR(
        optimizer,
        schedulers=[warmup, cosine],
        milestones=[warmup_steps],
    )
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
    train_state: Optional[Dict[str, Any]] = None,
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    del current_params_types
    del hyperparameters
    del eval_results
    del train_state
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
    logits, new_model_state = outputs
    losses = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=logits,
        mask_batch=batch.get("weights"),
        label_smoothing=0.0,
    )
    loss = losses["summed"] / losses["n_valid_examples"]
    loss.backward()
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
