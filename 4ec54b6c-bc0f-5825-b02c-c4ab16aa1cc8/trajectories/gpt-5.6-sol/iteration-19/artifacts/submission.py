"""Low-overhead self-tuning PyTorch training algorithm.

A workload-independent Adam update and moderate batch size provide adaptive
steps while retaining enough stochastic updates for robust generalization.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_LEARNING_RATE = 0.003
_BETA1 = 0.9
_BETA2 = 0.999
_EPSILON = 1e-8


def get_batch_size(workload_name: str) -> int:
    """Return one global batch size without identifying the workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize an adaptive optimizer with no externally tuned values."""
    del workload, model_state, hyperparameters, rng
    optimizer = torch.optim.Adam(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=_EPSILON,
        weight_decay=0.0,
    )
    return {"optimizer": optimizer}


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
    """Apply one Adam update to the mean loss of the selected batch."""
    del current_params_types, hyperparameters, loss_type
    del eval_results, global_step, train_state

    optimizer = optimizer_state["optimizer"]
    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)

    logits, next_model_state = workload.model_fn(
        params=current_param_container,
        augmented_and_preprocessed_input_batch=batch,
        model_state=model_state,
        mode=spec.ForwardPassMode.TRAIN,
        rng=rng,
        update_batch_norm=True,
    )
    losses = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=logits,
        mask_batch=batch.get("weights"),
        label_smoothing=0.0,
    )
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
    optimizer.step()
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
    """No special evaluation parameters or state are required."""
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
    """Consume the next pre-shuffled batch without modifying it."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
