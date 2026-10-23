"""Self-tuning, workload-agnostic PyTorch training algorithm."""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_BASE_LEARNING_RATE = 0.003
_BETA_1 = 0.9
_BETA_2 = 0.999
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
    """Create a Nesterov-adaptive optimizer with fixed algorithmic settings."""
    del workload, model_state, hyperparameters, rng
    optimizer = torch.optim.NAdam(
        model_params.parameters(),
        lr=_BASE_LEARNING_RATE,
        betas=(_BETA_1, _BETA_2),
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
    """Take one adaptive step with a late stabilization decay."""
    del current_params_types, hyperparameters, loss_type, eval_results, global_step
    del train_state

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"]
    if step == 2000:
        for group in optimizer.param_groups:
            group["lr"] = _BASE_LEARNING_RATE * 0.7
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
    """Evaluate the live parameters without adding timed preparation work."""
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
    """Consume the next pre-shuffled mini-batch."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
