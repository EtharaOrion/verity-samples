"""Fast MNIST - balanced AdamW."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR

from algoperf import spec

_BATCH_SIZE = 128
_LEARNING_RATE = 0.0035
_WEIGHT_DECAY = 0.015
_BETA1 = 0.9
_BETA2 = 0.999

def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE

def _pytorch_cosine_warmup(step_hint: int, optimizer: torch.optim.Optimizer):
    warmup_steps = int(0.025 * step_hint)
    if warmup_steps < 5:
        warmup_steps = 5
    warmup = LinearLR(optimizer, start_factor=0.2, end_factor=1.0, total_iters=warmup_steps)
    cosine_steps = max(step_hint - warmup_steps, 1)
    cosine_decay = CosineAnnealingLR(optimizer, T_max=cosine_steps)
    return SequentialLR(optimizer, schedulers=[warmup, cosine_decay], milestones=[warmup_steps])

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
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
    )
    scheduler = _pytorch_cosine_warmup(workload.step_hint, optimizer)
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
    current_param_container.train()
    optimizer_state["optimizer"].zero_grad()
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
        label_smoothing=0.0,
    )
    loss = loss_dict["summed"] / loss_dict["n_valid_examples"]
    loss.backward()
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), max_norm=1.0)
    optimizer_state["optimizer"].step()
    optimizer_state["scheduler"].step()
    optimizer_state["step"] += 1
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
