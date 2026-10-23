"""Self-tuning training algorithm using Adam and an early-convergence schedule."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 512
_INITIAL_LR = 0.01
_BETA1 = 0.9
_BETA2 = 0.99
_EPSILON = 1e-8
_DECAY_START = 200
_DECAY_RATE = 0.998
_MIN_LR_FACTOR = 0.1


def get_batch_size(workload_name: str) -> int:
    """Return one global batch size for all workloads."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Create an adaptive optimizer; all settings are selected internally."""
    del workload, model_state, hyperparameters, rng
    optimizer = torch.optim.Adam(
        model_params.parameters(),
        lr=_INITIAL_LR,
        betas=(_BETA1, _BETA2),
        eps=_EPSILON,
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
    train_state: Optional[Dict[str, Any]] = None,
) -> spec.UpdateReturn:
    """Take one Adam step and gently decay the rate after rapid initial learning."""
    del current_params_types, hyperparameters, loss_type, eval_results, global_step
    del train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    if step >= _DECAY_START:
        factor = max(_MIN_LR_FACTOR, _DECAY_RATE ** (step - _DECAY_START + 1))
        optimizer.param_groups[0]["lr"] = _INITIAL_LR * factor

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
    (losses["summed"] / losses["n_valid_examples"]).backward()
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
) -> spec.UpdateReturn:
    """No evaluation-time parameter transformation is needed."""
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
    """Consume the next independently shuffled training batch."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
