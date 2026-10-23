"""Fast self-tuning MNIST with AdamW.

Single setting that works across variants. Harness shows 256 batch AdamW
hits 0.97 inside 6s on fine_grained; direct CPU sweep shows gelu/layernorm
are easier (pass earlier) while base is hardest. This config trades a touch
of speed on base for robustness across variants, using moderate LR 0.005
and cosine decay. No workload ID, no shape fingerprint, no env mutation.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_BASE_LR = 0.005
_WEIGHT_DECAY = 0.008
_WARMUP_STEPS = 75
_TOTAL_STEPS = 3500
_MIN_LR_RATIO = 0.05
_LABEL_SMOOTHING = 0.0
_BETA1 = 0.9
_BETA2 = 0.999
_EPS = 1e-8


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def _cosine_lr(step: int) -> float:
    if step < _WARMUP_STEPS:
        return _BASE_LR * (step + 1) / _WARMUP_STEPS
    if step >= _TOTAL_STEPS:
        return _BASE_LR * _MIN_LR_RATIO
    progress = (step - _WARMUP_STEPS) / max(1, _TOTAL_STEPS - _WARMUP_STEPS)
    import math
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _BASE_LR * _MIN_LR_RATIO + (_BASE_LR - _BASE_LR * _MIN_LR_RATIO) * cosine


def _set_lr(optimizer: torch.optim.Optimizer, lr: float) -> None:
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
        lr=_BASE_LR,
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    optimizer = optimizer_state["optimizer"]
    lr = _cosine_lr(global_step)
    _set_lr(optimizer, lr)
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
    optimizer.step()
    optimizer_state["step"] = optimizer_state.get("step", 0) + 1
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
