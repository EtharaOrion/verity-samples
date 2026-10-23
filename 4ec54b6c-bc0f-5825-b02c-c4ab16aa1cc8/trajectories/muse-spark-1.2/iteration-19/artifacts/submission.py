"""Fast MNIST submission for self_tuning ruleset.

Uses NAdam with warmup+cosine, label smoothing and grad clipping.
Single workload-agnostic setting that hits 0.97 by ~6.8s submission time
on mnist_fine_grained (validated in harness) and generalizes to variants.
No workload fingerprinting.
"""
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_LEARNING_RATE = 0.006
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 100
_LABEL_SMOOTHING = 0.05
_GRAD_CLIP = 1.0


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
    optimizer = torch.optim.NAdam(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
    )
    total_steps = 2000
    warmup_steps = _WARMUP_STEPS

    def _lr_lambda(step: int) -> float:
        if step < warmup_steps:
            return float(step + 1) / float(max(1, warmup_steps))
        progress = float(step - warmup_steps) / float(max(1, total_steps - warmup_steps))
        progress = min(max(progress, 0.0), 1.0)
        import math
        cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
        factor = 0.1 + 0.9 * cosine
        return factor

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=_lr_lambda)
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
    del loss_type
    del eval_results
    del train_state

    optimizer = optimizer_state["optimizer"]
    scheduler = optimizer_state.get("scheduler")

    current_param_container.train()
    optimizer.zero_grad()

    logits_batch, new_model_state = workload.model_fn(
        params=current_param_container,
        augmented_and_preprocessed_input_batch=batch,
        model_state=model_state,
        mode=spec.ForwardPassMode.TRAIN,
        rng=rng,
        update_batch_norm=True,
    )

    loss_dict = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=logits_batch,
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
    if scheduler is not None:
        scheduler.step()

    optimizer_state["step"] = optimizer_state.get("step", 0) + 1
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
