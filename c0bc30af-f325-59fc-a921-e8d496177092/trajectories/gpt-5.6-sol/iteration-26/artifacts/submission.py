import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_LEARNING_RATE = 0.003
_BETA1 = 0.9
_BETA2 = 0.99
_WEIGHT_DECAY = 0.02
_WARMUP_FRACTION = 0.05
_MIN_LR_FACTOR = 0.1


def _learning_rate_factor(step: int, warmup_steps: int, total_steps: int) -> float:
    if step < warmup_steps:
        return float(step + 1) / float(warmup_steps)
    progress = min(1.0, (step - warmup_steps) / (total_steps - warmup_steps))
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return _MIN_LR_FACTOR + (1.0 - _MIN_LR_FACTOR) * cosine


def get_batch_size(workload_name: str) -> int:
    """Return one workload-independent global training batch size."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Create an adaptive optimizer and a horizon-normalized schedule."""
    del model_state
    del hyperparameters
    del rng

    parameters = list(model_params.parameters())
    optimizer = torch.optim.AdamW(
        parameters,
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
        fused=parameters[0].is_cuda,
    )
    total_steps = max(2, int(workload.step_hint))
    warmup_steps = max(1, int(_WARMUP_FRACTION * total_steps))
    scheduler = torch.optim.lr_scheduler.LambdaLR(
        optimizer,
        lambda step: _learning_rate_factor(step, warmup_steps, total_steps),
    )
    return {"optimizer": optimizer, "scheduler": scheduler}


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
) -> spec.UpdateReturn:
    """Take one mixed-precision AdamW step and retain new auxiliary state."""
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del train_state

    optimizer = optimizer_state["optimizer"]
    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)

    device_type = batch["inputs"].device.type
    with torch.autocast(
        device_type=device_type,
        dtype=torch.bfloat16,
        enabled=device_type == "cuda",
    ):
        predictions, next_model_state = workload.model_fn(
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
        mean_loss = losses["summed"] / losses["n_valid_examples"]

    mean_loss.backward()
    optimizer.step()
    optimizer_state["scheduler"].step()
    return optimizer_state, current_param_container, next_model_state


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
) -> spec.UpdateReturn:
    """Evaluate the current iterate and its accumulated auxiliary state."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng
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
    """Take the next batch from the fixed, shuffled input pipeline."""
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
