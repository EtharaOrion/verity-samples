"""Self-tuning adaptive optimizer with warmup and cosine decay."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR

from algoperf import spec

_BATCH_SIZE = 64
_LEARNING_RATE = 0.0017486387539278373
_BETA1 = 0.93266073836
_BETA2 = 0.9955159689799007
_WEIGHT_DECAY = 0.08121616522670176
_WARMUP_FACTOR = 0.02


def get_batch_size(workload_name: str) -> int:
    """Return the training batch size.

    A single value that works across every workload is what the rules allow. Selecting a value by
    identifying the workload is not.
    """
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize decoupled NAdam and a workload-provided-horizon schedule."""
    del model_state
    del hyperparameters
    del rng

    optimizer = torch.optim.NAdam(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        weight_decay=_WEIGHT_DECAY,
        decoupled_weight_decay=True,
        foreach=True,
    )
    warmup_steps = max(int(_WARMUP_FACTOR * workload.step_hint), 1)
    warmup = LinearLR(
        optimizer,
        start_factor=1e-5,
        end_factor=1.0,
        total_iters=warmup_steps,
    )
    decay = CosineAnnealingLR(
        optimizer,
        T_max=max(workload.step_hint - warmup_steps, 1),
        eta_min=0.0,
    )
    scheduler = SequentialLR(
        optimizer,
        schedulers=[warmup, decay],
        milestones=[warmup_steps],
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
    """Apply one adaptive update and propagate forward-pass model state."""
    unused = (
        current_params_types,
        hyperparameters,
        loss_type,
        eval_results,
        global_step,
        train_state,
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
) -> spec.UpdateReturn:
    """Evaluate the current online parameters without copying them."""
    unused = (
        workload,
        current_params_types,
        hyperparameters,
        loss_type,
        eval_results,
        global_step,
        rng,
    )
    del unused
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
    """Take the next batch off the queue, unchanged."""
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
