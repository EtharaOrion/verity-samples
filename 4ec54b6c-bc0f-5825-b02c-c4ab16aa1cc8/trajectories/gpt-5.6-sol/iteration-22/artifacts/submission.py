"""Self-tuning optimizer submission.

Adam supplies scale adaptation and momentum while a conservative late decay keeps
training stable across generic architectural variants.  The algorithm deliberately
uses one global configuration and never identifies the workload or model.
"""

from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_BASE_LR = 0.003
_BETA1 = 0.9
_BETA2 = 0.999
_EPSILON = 1e-8
_DECAY_START = 1000


def get_batch_size(workload_name: str) -> int:
    """Return one global batch size for every workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Initialize a scale-adaptive optimizer with first-moment momentum."""
    del workload, model_state, hyperparameters, rng
    optimizer = torch.optim.Adam(
        model_params.parameters(),
        lr=_BASE_LR,
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """Take one Adam step and gently reduce the rate late in training."""
    del current_params_types, hyperparameters, loss_type, eval_results

    optimizer = optimizer_state["optimizer"]
    step = global_step
    if step >= _DECAY_START:
        rate = _BASE_LR * (_DECAY_START / (step + 1)) ** 0.5
        for group in optimizer.param_groups:
            group["lr"] = rate

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
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
