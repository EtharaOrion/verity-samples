"""Fast training algorithm with adaptive optimization and schedule."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128


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
    _base_lr = 0.003
    _weight_decay = 0.02
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_base_lr,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=_weight_decay,
    )
    _step_hint = workload.step_hint
    _warmup_steps = max(1, int(0.07 * _step_hint))
    _cosine_steps = max(_step_hint - _warmup_steps, 1)
    _warmup = torch.optim.lr_scheduler.LinearLR(
        optimizer, start_factor=0.1, end_factor=1.0, total_iters=_warmup_steps
    )
    _cosine = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=_cosine_steps, eta_min=_base_lr * 0.03
    )
    scheduler = torch.optim.lr_scheduler.SequentialLR(
        optimizer, schedulers=[_warmup, _cosine], milestones=[_warmup_steps]
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
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
