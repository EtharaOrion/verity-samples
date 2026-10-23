"""A self-tuning training algorithm.

One fixed configuration applied identically to every workload: no workload identification,
no model fingerprinting, no search space, and no hyperparameters exposed to the harness.
The algorithm is an Adam-style adaptive optimizer with decoupled weight decay, a short
linear warmup, a mild inverse-sqrt decay, a loose global gradient-norm clip as a stability
net, and an exponential moving average of the parameters that is swapped in for evaluation
(Polyak averaging) and swapped back out before the next training step.

All state lives in the optimizer state that the harness creates fresh for each run, so
nothing is latched from one run into another, and the algorithm emits no logging of its own.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_LEARNING_RATE = 0.008
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 5e-6
_WARMUP_STEPS = 25
_DECAY_SCALE = 1500.0
_CLIP_NORM = 5.0
_EMA_DECAY = 0.995
_EMA_START = 10


def get_batch_size(workload_name: str) -> int:
    """Return the training batch size (a single value used for every workload)."""
    del workload_name
    return _BATCH_SIZE


def _lr_multiplier(step: int) -> float:
    """Linear warmup followed by a mild inverse-square-root decay."""
    warm = min(1.0, float(step + 1) / float(_WARMUP_STEPS))
    decay = (_DECAY_SCALE / (_DECAY_SCALE + float(step))) ** 0.5
    return warm * decay


def _trainable(param_container: spec.ParameterContainer) -> List[Any]:
    return [p for p in param_container.parameters() if p.requires_grad]


def _restore_raw_params(optimizer_state: spec.OptimizerState, params: List[Any]) -> None:
    """Undo a pending evaluation-time parameter swap, if there is one."""
    backup = optimizer_state.get("backup")
    if backup is not None:
        with torch.no_grad():
            for p, b in zip(params, backup):
                p.copy_(b)
        optimizer_state["backup"] = None


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Adaptive optimizer plus a parameter average. Every field is created fresh here."""
    del workload
    del model_state
    del hyperparameters
    del rng
    params = _trainable(model_params)
    optimizer = torch.optim.AdamW(
        params,
        lr=_LEARNING_RATE,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
        foreach=True,
    )
    return {
        "optimizer": optimizer,
        "ema": [p.detach().clone() for p in params],
        "backup": None,
        "step": 0,
    }


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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """One training step."""
    unused = (current_params_types, hyperparameters, eval_results, loss_type, train_state,
              global_step)
    del unused

    optimizer = optimizer_state["optimizer"]
    params = _trainable(current_param_container)
    _restore_raw_params(optimizer_state, params)

    current_param_container.train()
    for p in params:
        p.grad = None

    step = optimizer_state["step"]
    lr = _LEARNING_RATE * _lr_multiplier(step)
    for group in optimizer.param_groups:
        group["lr"] = lr

    logits, next_state = workload.model_fn(
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

    torch.nn.utils.clip_grad_norm_(params, _CLIP_NORM)
    optimizer.step()

    ema = optimizer_state["ema"]
    with torch.no_grad():
        detached = [p.detach() for p in params]
        if step < _EMA_START:
            for e, p in zip(ema, detached):
                e.copy_(p)
        else:
            decay = min(_EMA_DECAY, (1.0 + step) / (10.0 + step))
            torch._foreach_mul_(ema, decay)
            torch._foreach_add_(ema, detached, alpha=1.0 - decay)

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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """Swap the averaged parameters in for evaluation; the next step swaps them back."""
    unused = (workload, current_params_types, hyperparameters, loss_type, eval_results,
              global_step, rng)
    del unused

    params = _trainable(current_param_container)
    ema = optimizer_state.get("ema")
    if ema is not None and optimizer_state["step"] > _EMA_START:
        if optimizer_state.get("backup") is None:
            optimizer_state["backup"] = [p.detach().clone() for p in params]
        with torch.no_grad():
            for p, e in zip(params, ema):
                p.copy_(e)
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
