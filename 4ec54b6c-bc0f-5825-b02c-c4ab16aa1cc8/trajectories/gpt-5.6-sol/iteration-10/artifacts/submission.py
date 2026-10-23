"""Generic self-tuning PyTorch training algorithm for AlgoPerf."""

from typing import Any, Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_BASE_LR = 0.004
_WARMUP_STEPS = 10
_DECAY_STEPS = 8000
_MIN_LR_SCALE = 0.25
_GRAD_CLIP = 5.0


def get_batch_size(workload_name: str) -> int:
    """Use one global batch size for all workloads."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize an adaptive optimizer; all settings are internal."""
    del workload, model_state, hyperparameters, rng
    optimizer = torch.optim.Adam(
        model_params.parameters(),
        lr=_BASE_LR / _WARMUP_STEPS,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=0.0,
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """Take one clipped Adam step with a warmup followed by smooth decay."""
    del current_params_types, hyperparameters, loss_type, eval_results, global_step

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    if step < _WARMUP_STEPS:
        scale = (step + 1) / _WARMUP_STEPS
    else:
        progress = min((step - _WARMUP_STEPS) / _DECAY_STEPS, 1.0)
        scale = 1.0 - (1.0 - _MIN_LR_SCALE) * progress
    for group in optimizer.param_groups:
        group["lr"] = _BASE_LR * scale

    current_param_container.train()
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
    loss = losses["summed"] / losses["n_valid_examples"]
    loss.backward()
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), _GRAD_CLIP)
    optimizer.step()
    optimizer_state["step"] = step + 1
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """Adam needs no evaluation-time parameter transformation."""
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
    """Consume the next already shuffled training batch."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
