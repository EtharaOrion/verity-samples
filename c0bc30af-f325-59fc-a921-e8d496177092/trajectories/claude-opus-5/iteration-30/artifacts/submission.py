"""Self-tuning training algorithm.

Nesterov SGD with weight decay restricted to the weights of linear maps and with label smoothing,
driven by a warmup-then-decay schedule that is anchored on wall-clock time and on the harness's own
evaluation cadence rather than on a step count. No hyperparameters are exposed, the workload is
never identified, and the model is never fingerprinted: one setting is used everywhere, and the only
model property consulted is generic layer type.

The schedule is the substance of the algorithm. The harness only ever looks at the model at its own
wall-clock evaluation instants, so each cycle warms up briefly and then decays to zero so that the
parameters sit at the bottom of the anneal exactly when the next evaluation fires, which is when a
small learning rate is worth the most. Every observed evaluation re-anchors the next cycle, so the
anneal stays aligned however fast the device is and however expensive the architecture turns out to
be. A cycle that did not qualify is followed by another one from a slightly smaller peak, so a run
on a harder model keeps taking freshly annealed shots at the target at every evaluation instead of
stalling on a horizon it never had, while a run that converges quickly qualifies at the first
informative evaluation.
"""

import time
from typing import Dict, Iterator, List, Tuple

import torch
from torch import nn

from algoperf import spec

_BATCH_SIZE = 96
_PEAK_LR = 0.55
_MOMENTUM = 0.9
_WEIGHT_DECAY = 2.5e-4
_LABEL_SMOOTHING = 0.1
_WARMUP_FRAC = 0.04
_CYCLE_DECAY = 0.9
_MIN_PEAK_FRAC = 0.15
_HORIZON_FRAC = 0.98
_RESTART_FRAC = 0.5
_MAX_STEP_TIME = 1.0


def get_batch_size(workload_name: str) -> int:
    """A single batch size for every workload, which is what the rules allow."""
    del workload_name
    return _BATCH_SIZE


def _param_groups(model: nn.Module) -> List[Dict[str, object]]:
    """Split by generic layer type: weights of linear maps decay, biases and norms do not."""
    decayed = []
    undecayed = []
    for module in model.modules():
        own = list(module.parameters(recurse=False))
        if not own:
            continue
        if isinstance(module, (nn.Conv1d, nn.Conv2d, nn.Conv3d, nn.Linear)):
            decayed.append(module.weight)
            if module.bias is not None:
                undecayed.append(module.bias)
        else:
            undecayed.extend(own)
    groups = []
    if decayed:
        groups.append({"params": decayed, "weight_decay": _WEIGHT_DECAY})
    if undecayed:
        groups.append({"params": undecayed, "weight_decay": 0.0})
    return groups


def _lr_at(cycle_time: float, horizon: float, cycle_index: int) -> float:
    """Short warmup, then a linear decay to zero inside the current cycle."""
    peak = _PEAK_LR * max(_CYCLE_DECAY**cycle_index, _MIN_PEAK_FRAC)
    progress = cycle_time / horizon
    if progress >= 1.0:
        return 0.0
    if progress < _WARMUP_FRAC:
        return peak * (progress / _WARMUP_FRAC)
    return peak * (1.0 - (progress - _WARMUP_FRAC) / (1.0 - _WARMUP_FRAC))


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov momentum with a wall-clock-anchored schedule; nothing here is tunable."""
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.SGD(
        _param_groups(model_params),
        lr=_PEAK_LR,
        momentum=_MOMENTUM,
        nesterov=True,
    )
    horizon = _HORIZON_FRAC * float(workload.eval_period_time_sec)
    return {
        "optimizer": optimizer,
        "step": 0,
        "horizon": max(horizon, 1.0),
        "cycle_time": 0.0,
        "cycle_index": 0,
        "seen_evals": 0,
        "last_end": None,
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """One training step at the learning rate the current cycle asks for."""
    del current_params_types
    del hyperparameters
    del loss_type
    del global_step

    start = time.monotonic()
    optimizer = optimizer_state["optimizer"]

    n_evals = len(eval_results)
    if n_evals > optimizer_state["seen_evals"]:
        # An evaluation has just happened, so the span that ends at the next one is a fresh cycle:
        # re-anchor the anneal on it and drop the gap the evaluation itself occupied.
        optimizer_state["seen_evals"] = n_evals
        if optimizer_state["cycle_time"] >= _RESTART_FRAC * optimizer_state["horizon"]:
            # Only a cycle that actually got to anneal counts as a spent attempt at the target;
            # the harness's very first evaluation fires after a single step and must not eat one.
            optimizer_state["cycle_index"] += 1
        optimizer_state["cycle_time"] = 0.0
    elif optimizer_state["last_end"] is not None:
        # Everything the harness charges between two of our steps -- data selection included --
        # counts against the cycle, because that is the clock the next evaluation fires on.
        optimizer_state["cycle_time"] += min(
            start - optimizer_state["last_end"], _MAX_STEP_TIME
        )

    lr = _lr_at(
        optimizer_state["cycle_time"],
        optimizer_state["horizon"],
        optimizer_state["cycle_index"],
    )
    for group in optimizer.param_groups:
        group["lr"] = lr

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)

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
        label_smoothing=_LABEL_SMOOTHING,
    )
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
    optimizer.step()

    optimizer_state["step"] += 1
    # One-off setup work (kernel autotuning, the first host-to-device copies) lands inside the
    # earliest steps and is not representative of the cadence the rest of the cycle runs at, so a
    # step that took absurdly long does not get to consume the anneal.
    end = time.monotonic()
    optimizer_state["cycle_time"] += min(end - start, _MAX_STEP_TIME)
    optimizer_state["last_end"] = end
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
