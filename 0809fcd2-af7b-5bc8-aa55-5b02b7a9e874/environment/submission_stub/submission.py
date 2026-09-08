"""Seed submission.

This is a working training algorithm, not an empty stub. It runs to completion, produces a well-formed
evaluation log, and satisfies every conformance check the task declares. What it is bad at is the graded
axis: it converges slowly, so it does not reach the validation target inside the budget.

It is here to be improved. The reward scale is anchored so that a reward of zero means you did not improve
on what you were handed, rather than meaning you produced nothing.

Only the functions defined below may exist at module level, alongside imports and constants. See the
vendored upstream documentation for the full submission contract.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_LEARNING_RATE = 0.05
_MOMENTUM = 0.9
_WEIGHT_DECAY = 0.0
_MAX_GRADIENT_NORM = 0.002


def _bound_gradients(params: spec.ParameterContainer) -> None:
    """Rescale the whole gradient so its norm never exceeds the bound this submission declares."""
    torch.nn.utils.clip_grad_norm_(params.parameters(), _MAX_GRADIENT_NORM)


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
    """Stochastic gradient descent with momentum, with every update passed through a fixed norm bound.

    The bound is applied to the assembled gradient before each step and is held at one value for the whole
    run, so the distance the parameters travel in a step is settled by the bound rather than by how steep
    the loss surface happens to be at that point.
    """
    del workload
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.SGD(
        model_params.parameters(),
        lr=_LEARNING_RATE,
        momentum=_MOMENTUM,
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
    """One training step, taken along the bounded gradient."""
    unused = (current_params_types, hyperparameters, eval_results, global_step)
    del unused

    sgd = optimizer_state["optimizer"]
    current_param_container.train()
    sgd.zero_grad()

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
        label_smoothing=0.0,
    )
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
    _bound_gradients(current_param_container)
    sgd.step()

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
