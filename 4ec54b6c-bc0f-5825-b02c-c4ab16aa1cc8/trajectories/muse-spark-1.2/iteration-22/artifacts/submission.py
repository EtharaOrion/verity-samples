"""Fast MNIST submission."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_LEARNING_RATE = 0.008
_WEIGHT_DECAY = 0.02
_WARMUP_FRAC = 0.05

def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE

def _is_decay_param(name: str) -> bool:
    lower = name.lower()
    if "bias" in lower:
        return False
    if "norm" in lower:
        return False
    return True

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
    decay_params = []
    no_decay_params = []
    for _name, _p in model_params.named_parameters():
        if not _p.requires_grad:
            continue
        if _is_decay_param(_name):
            decay_params.append(_p)
        else:
            no_decay_params.append(_p)
    optimizer = torch.optim.AdamW(
        [
            {"params": decay_params, "weight_decay": _WEIGHT_DECAY},
            {"params": no_decay_params, "weight_decay": 0.0},
        ],
        lr=_LEARNING_RATE,
        betas=(0.9, 0.999),
        eps=1e-8,
    )
    total_steps = workload.step_hint
    warmup_steps = int(total_steps * _WARMUP_FRAC)
    if warmup_steps < 1:
        warmup_steps = 1
    from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR
    warmup = LinearLR(optimizer, start_factor=0.1, end_factor=1.0, total_iters=warmup_steps)
    cosine_steps = max(total_steps - warmup_steps, 1)
    cosine = CosineAnnealingLR(optimizer, T_max=cosine_steps)
    scheduler = SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])
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
        label_smoothing=0.0,
    )
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), max_norm=1.0)
    optimizer.step()
    scheduler.step()
    optimizer_state["step"] += 1
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
