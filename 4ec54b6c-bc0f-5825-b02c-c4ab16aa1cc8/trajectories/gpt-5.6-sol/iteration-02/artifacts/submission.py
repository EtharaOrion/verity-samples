"""Self-tuning training algorithm using AdamW with cosine learning-rate decay."""

from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_LEARNING_RATE = 0.003
_WEIGHT_DECAY = 0.0001
_BETA1 = 0.9
_BETA2 = 0.99
_EPSILON = 1e-8


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
    """Initialize an adaptive optimizer and a smooth full-budget schedule."""
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=_EPSILON,
        weight_decay=_WEIGHT_DECAY,
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer,
        T_max=max(int(workload.step_hint) // 2, 1),
        eta_min=0.1 * _LEARNING_RATE,
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
    """Take one AdamW step and advance the learning-rate schedule."""
    unused = (
        current_params_types,
        hyperparameters,
        loss_type,
        eval_results,
        global_step,
    )
    del unused

    optimizer = optimizer_state["optimizer"]
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
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
    optimizer.step()
    optimizer_state["scheduler"].step()
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
    """Consume the next batch from the fixed shuffled input pipeline."""
    unused = (
        workload,
        optimizer_state,
        current_param_container,
        model_state,
        hyperparameters,
        global_step,
        rng,
    )
    del unused
    return next(input_queue)
