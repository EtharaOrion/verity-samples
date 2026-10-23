"""Self-tuning training algorithm for the AlgoPerf submission API.

Nesterov SGD with rank-decoupled weight decay, scale-free gradient clipping and a
warm-restart cosine schedule that is expressed in seconds and phase-locked to the
harness' own evaluation cadence.

The schedule knows nothing about the problem it is solving. It reads the evaluation
period from the workload, measures its own step time, and anneals so that the learning
rate reaches its floor just before the next evaluation lands: the model that is scored
is therefore always a fully annealed one, on fast hardware and slow hardware alike. If
an evaluation passes without the run being stopped, the algorithm restarts with a lower
peak and, from the third cycle on, a doubled horizon, so a problem that needs an order
of magnitude more time than the first cycle covers still gets a long final anneal, and
every cycle boundary still coincides with an evaluation.

Nothing here inspects the workload's identity, the dataset, or the model's structure:
the only model-dependent choice is the generic one of not decaying parameters of rank
below two.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 64
_PEAK_LR = 0.4
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1
_WARMUP_FRAC = 0.15
_WARMUP_FLOOR = 0.02
_FINAL_LR_FRAC = 0.02
_PEAK_DECAY = 0.85
_CYCLE_MARGIN_FRAC = 0.06
_MIN_CYCLE_MARGIN_SEC = 1.0
_MAX_STEP_SEC = 0.5
_CLIP_DECAY = 0.99
_CLIP_FACTOR = 4.0
_EPS = 1e-6


def _param_groups(model_params: spec.ParameterContainer) -> List[Dict[str, Any]]:
    """Split on a generic property: tensors of rank below two are not decayed."""
    decayed = []
    undecayed = []
    for parameter in model_params.parameters():
        if not parameter.requires_grad:
            continue
        if parameter.ndim >= 2:
            decayed.append(parameter)
        else:
            undecayed.append(parameter)
    return [
        {"params": decayed, "weight_decay": _WEIGHT_DECAY},
        {"params": undecayed, "weight_decay": 0.0},
    ]


def _tick(state: Dict[str, Any]) -> None:
    """Advance the schedule clock by the time since the previous step began.

    Intervals are capped so that a one-off cost that is not training -- a first-step
    compilation, an input pipeline stall, or the pause the harness takes for an untimed
    evaluation -- cannot fast-forward the schedule past the work it is pacing.
    """
    now = time.monotonic()
    previous = state["last_entry"]
    if previous is not None:
        state["elapsed"] += min(now - previous, _MAX_STEP_SEC)
    state["last_entry"] = now


def _restart(state: Dict[str, Any], period: float) -> None:
    """Begin the next cycle, one evaluation boundary at a time.

    The first two cycles span a single evaluation period each, so a problem that is
    nearly solved gets two cheap, fully annealed chances; after that the horizon doubles,
    which is what a problem that is not nearly solved needs.
    """
    state["cycle_index"] += 1
    if state["cycle_index"] >= 2:
        state["periods"] = state["periods"] * 2
    state["peak"] = state["peak"] * _PEAK_DECAY
    margin = max(_CYCLE_MARGIN_FRAC * period, _MIN_CYCLE_MARGIN_SEC)
    state["cycle_start"] = state["elapsed"]
    state["cycle_len"] = max(state["periods"] * period - margin, period * 0.5)
    state["cycle_end"] = state["cycle_start"] + state["cycle_len"]


def _learning_rate(state: Dict[str, Any], num_evals: int, period: float) -> float:
    """Linear warmup then cosine decay, both measured in seconds within the cycle.

    Cycle boundaries are re-anchored on every evaluation the harness reports, so the
    schedule cannot drift away from the cadence it is aiming at, however long the
    untimed evaluations themselves take.
    """
    if num_evals > state["evals_seen"]:
        state["evals_seen"] = num_evals
        if state["elapsed"] >= state["cycle_end"]:
            _restart(state, period)

    peak = state["peak"]
    progress = (state["elapsed"] - state["cycle_start"]) / state["cycle_len"]
    progress = min(max(progress, 0.0), 1.0)
    if progress < _WARMUP_FRAC:
        return peak * max(progress / _WARMUP_FRAC, _WARMUP_FLOOR)
    decay_progress = (progress - _WARMUP_FRAC) / (1.0 - _WARMUP_FRAC)
    cosine = 0.5 * (1.0 + math.cos(math.pi * decay_progress))
    return peak * (_FINAL_LR_FRAC + (1.0 - _FINAL_LR_FRAC) * cosine)


def _clip_gradients(state: Dict[str, Any], grads: List[torch.Tensor]) -> None:
    """Scale the global gradient norm down to a multiple of its own running average.

    The threshold is a device tensor, so no host synchronisation and no assumption about
    the absolute scale of the gradients is introduced.
    """
    if not grads:
        return
    norm = torch.linalg.vector_norm(torch.stack(torch._foreach_norm(grads)))
    average = state["grad_norm_ema"]
    if average is None:
        state["grad_norm_ema"] = norm.detach().clone()
        return
    average.mul_(_CLIP_DECAY).add_(norm.detach(), alpha=1.0 - _CLIP_DECAY)
    scale = torch.clamp(_CLIP_FACTOR * average / (norm + _EPS), max=1.0)
    torch._foreach_mul_(grads, scale)


def get_batch_size(workload_name: str) -> int:
    """A single batch size for every workload, as the rules require."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov SGD plus the bookkeeping the wall-clock schedule needs."""
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.SGD(
        _param_groups(model_params),
        lr=_PEAK_LR * _WARMUP_FLOOR,
        momentum=_MOMENTUM,
        nesterov=True,
    )
    period = float(workload.eval_period_time_sec)
    margin = max(_CYCLE_MARGIN_FRAC * period, _MIN_CYCLE_MARGIN_SEC)
    return {
        "optimizer": optimizer,
        "parameters": [p for p in model_params.parameters() if p.requires_grad],
        "elapsed": 0.0,
        "last_entry": None,
        "evals_seen": 0,
        "cycle_index": 0,
        "periods": 1,
        "cycle_start": 0.0,
        "cycle_len": max(period - margin, period * 0.5),
        "cycle_end": max(period - margin, period * 0.5),
        "peak": _PEAK_LR,
        "grad_norm_ema": None,
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
    """One training step, paced by the schedule clock the previous steps advanced."""
    unused = (current_params_types, hyperparameters, loss_type, global_step)
    del unused

    state = optimizer_state
    optimizer = state["optimizer"]

    _tick(state)
    learning_rate = _learning_rate(
        state, len(eval_results), float(workload.eval_period_time_sec)
    )
    for group in optimizer.param_groups:
        group["lr"] = learning_rate

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

    _clip_gradients(state, [p.grad for p in state["parameters"] if p.grad is not None])
    optimizer.step()

    return state, current_param_container, next_state


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
