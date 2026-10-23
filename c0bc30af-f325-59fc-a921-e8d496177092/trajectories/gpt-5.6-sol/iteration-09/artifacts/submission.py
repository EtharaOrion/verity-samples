"""Self-tuning adaptive optimizer submission."""

from typing import Dict, Iterator, List, Tuple

import torch
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR

from algoperf import spec

_BATCH_SIZE = 128
_LEARNING_RATE = 0.0017486387539278373
_BETA1 = 0.93266073836
_BETA2 = 0.9955159689799007
_WEIGHT_DECAY = 0.08121616522670176
_WARMUP_FACTOR = 0.02


def get_batch_size(workload_name: str) -> int:
    """Return one broadly applicable training batch size."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Create NAdam with decoupled decay and a warmup-cosine schedule."""
    del model_state
    del hyperparameters
    del rng

    optimizer = torch.optim.NAdam(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
        decoupled_weight_decay=True,
        foreach=True,
    )
    warmup_steps = max(1, int(_WARMUP_FACTOR * workload.step_hint))
    warmup = LinearLR(
        optimizer,
        start_factor=0.01,
        end_factor=1.0,
        total_iters=warmup_steps,
    )
    decay = CosineAnnealingLR(
        optimizer,
        T_max=max(1, workload.step_hint - warmup_steps),
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
) -> spec.UpdateReturn:
    """Take one adaptive update and retain forward-pass model state."""
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step

    optimizer = optimizer_state["optimizer"]
    optimizer.zero_grad(set_to_none=True)
    logits, new_model_state = workload.model_fn(
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
    optimizer.step()
    optimizer_state["scheduler"].step()
    return optimizer_state, current_param_container, new_model_state


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
    """Evaluate the current scheduled-optimizer parameters unchanged."""
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
    """Take the next shuffled and augmented batch."""
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
