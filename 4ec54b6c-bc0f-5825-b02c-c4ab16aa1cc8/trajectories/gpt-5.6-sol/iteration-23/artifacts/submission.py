"""Self-tuning, workload-agnostic PyTorch training submission.

The update is deliberately inexpensive: Adam adds only standard optimizer state to
one forward/backward pass.  A short warmup protects architectures with very different
early gradient scales, after which a gentle inverse-square-root schedule keeps useful
progress without requiring a workload-specific horizon.
"""

from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_BASE_LEARNING_RATE = 0.003
_WARMUP_STEPS = 32
_WEIGHT_DECAY = 0.0


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
    """Initialize an adaptive optimizer with no externally tuned inputs."""
    del workload, model_state, hyperparameters, rng
    optimizer = torch.optim.Adam(
        model_params.parameters(),
        lr=_BASE_LEARNING_RATE / _WARMUP_STEPS,
        betas=(0.9, 0.999),
        eps=1e-8,
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
    """Apply one Adam update and advance the inexpensive analytic schedule."""
    del current_params_types, hyperparameters, loss_type, eval_results, global_step

    optimizer = optimizer_state["optimizer"]
    step = optimizer_state["step"] + 1
    if step <= _WARMUP_STEPS:
        learning_rate = _BASE_LEARNING_RATE * step / _WARMUP_STEPS
    else:
        # Constant through the important early phase, then decay without needing
        # a workload-specific step horizon.
        learning_rate = _BASE_LEARNING_RATE * min(1.0, (2048.0 / step) ** 0.5)
    optimizer.param_groups[0]["lr"] = learning_rate

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

    optimizer_state["step"] = step
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
    """Consume the next batch from the benchmark's shuffled input stream."""
    del workload, optimizer_state, current_param_container, model_state
    del hyperparameters, global_step, rng
    return next(input_queue)
