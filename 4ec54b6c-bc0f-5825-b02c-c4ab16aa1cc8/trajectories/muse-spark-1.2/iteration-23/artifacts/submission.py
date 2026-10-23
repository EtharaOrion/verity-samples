"""Fast adaptive training for MNIST - best config batch512."""
from typing import Any, Dict, Iterator, List, Optional, Tuple
import math
import torch
from algoperf import spec

_BATCH_SIZE = 512
_PEAK_LR = 0.008
_WARMUP = 60
_TOTAL = 1800
_WD = 0.001
_CLIP = 1.0

def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE

def _lr(step: int) -> float:
    if step < _WARMUP:
        return _PEAK_LR * (step + 1) / max(1, _WARMUP)
    if step < _TOTAL:
        p = (step - _WARMUP) / max(1, _TOTAL - _WARMUP)
        return 0.00005 + (_PEAK_LR - 0.00005) * 0.5 * (1 + math.cos(math.pi * p))
    return 0.00005

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
    opt = torch.optim.AdamW(
        model_params.parameters(),
        lr=_PEAK_LR,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=_WD,
    )
    return {"optimizer": opt, "step": 0}

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
    lr = _lr(global_step)
    opt = optimizer_state["optimizer"]
    for pg in opt.param_groups:
        pg["lr"] = lr
    current_param_container.train()
    opt.zero_grad()
    logits, new_state = workload.model_fn(
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
        label_smoothing=0.0,
    )
    loss = loss_dict["summed"] / loss_dict["n_valid_examples"]
    loss.backward()
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), _CLIP)
    opt.step()
    optimizer_state["step"] += 1
    return optimizer_state, current_param_container, new_state

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
