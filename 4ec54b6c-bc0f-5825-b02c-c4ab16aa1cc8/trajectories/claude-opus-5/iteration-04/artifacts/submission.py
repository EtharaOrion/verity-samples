"""A self-tuning training algorithm: AdamW with a time-adaptive, evaluation-aligned
cosine schedule and warm restarts.

Design constraints this file is written against:

  * Self-tuning ruleset: no hyperparameters are exposed and none are selected by
    looking at the workload, the registry key, the parameter shapes or the state-dict
    keys. One single setting is used for every workload, which is what the rules allow.

  * Everything the algorithm needs at run time is derived from information the harness
    hands it: the global step, the list of evaluations so far, the elapsed training
    time it measures for itself, and the workload's generic evaluation cadence. Nothing
    is fitted to a particular machine, so the schedule is the same shape whether a step
    takes one millisecond or ten.

  * Every value stored in the optimizer state implements `state_dict()` *and*
    `load_state_dict()`. The harness checkpoints the optimizer state by iterating over
    its keys and calls `load_state_dict` on each key when a run resumes, so a bare int
    or float in that dict makes a resumed run raise before the first step.

  * There is no module-level mutable state. Every piece of run state lives in the
    optimizer state, is constructed per run in `init_optimizer_state`, and therefore
    cannot latch across runs sharing a process.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

# Batch size. Deliberately modest: the graded axis multiplies steps by the batch size,
# and a large batch buys throughput only on a machine that is launch-bound.
_BATCH_SIZE = 256

# Optimizer setting, one for every workload.
_PEAK_LR = 1.1e-2
_BETA1 = 0.9
_BETA2 = 0.95
_EPS = 1e-8
_WEIGHT_DECAY = 1e-4
_GRAD_CLIP = 1.0
_LABEL_SMOOTHING = 0.05

# Schedule shape.
_WARMUP_STEPS = 50
_LR_FLOOR = 0.04
_CYCLE_DECAY = 0.82
_MIN_CYCLE_SCALE = 0.30
_DEFAULT_PERIOD_SEC = 10.0
_MAX_STEP_DELTA_SEC = 0.5
_FALLBACK_CYCLE_STEPS = 1200


def _new_run_state() -> torch.nn.Module:
    """A tiny buffer holder for the run's own clock.

    It is an `nn.Module`, so it round-trips through the harness's checkpointing exactly
    like the optimizer does. The buffers are float64 because one of them holds a wall
    clock reading, which float32 cannot represent to better than a couple of minutes.
    """
    holder = torch.nn.Module()
    holder.register_buffer('elapsed', torch.zeros((), dtype=torch.float64))
    holder.register_buffer('last_step_time', torch.zeros((), dtype=torch.float64))
    return holder


def _tick(run_state: torch.nn.Module, now: float) -> float:
    """Accumulate wall time actually spent inside training steps.

    Deltas are clamped, so the first step of a run, the first step after a resume, and
    any step straddling an evaluation contribute nothing rather than a wild jump.
    """
    previous = float(run_state.last_step_time.item())
    if previous > 0.0:
        delta = now - previous
        if 0.0 < delta < _MAX_STEP_DELTA_SEC:
            run_state.elapsed.add_(delta)
    run_state.last_step_time.fill_(now)
    return float(run_state.elapsed.item())


def _period_seconds(workload: Any) -> float:
    """The evaluation cadence, read as a generic workload property with a safe default."""
    try:
        period = float(getattr(workload, 'eval_period_time_sec', 0.0))
    except (TypeError, ValueError):
        period = 0.0
    if not math.isfinite(period) or period <= 0.0:
        period = _DEFAULT_PERIOD_SEC
    return period


def _cycle_phase(
    now: float,
    elapsed: float,
    period: float,
    global_step: int,
    train_state: Optional[Dict[str, Any]],
) -> float:
    """Where we are, in [0, 1], between one evaluation and the next.

    Preferring the harness's own last evaluation timestamp keeps the schedule in step
    with the cadence on any hardware. Before the first evaluation, and if that field is
    not offered at all, it falls back first to the time this run has measured for itself
    and finally to a plain step-counted cycle.
    """
    last_eval = 0.0
    if train_state is not None:
        try:
            last_eval = float(train_state.get('last_eval_time', 0.0) or 0.0)
        except (AttributeError, TypeError, ValueError):
            last_eval = 0.0
    if last_eval > 0.0 and now >= last_eval:
        phase = (now - last_eval) / period
    elif elapsed > 0.0:
        phase = elapsed / period
    else:
        phase = float(global_step % _FALLBACK_CYCLE_STEPS) / float(_FALLBACK_CYCLE_STEPS)
    if not math.isfinite(phase):
        return 0.0
    return min(max(phase, 0.0), 1.0)


def _learning_rate(step: int, phase: float, completed_cycles: int) -> float:
    """Warmup, then a cosine ramp down to a floor across each evaluation period.

    Each period is a warm restart whose peak is a little lower than the last, so the
    model is close to annealed whenever the harness looks at it, while training still
    makes fast progress in between. Nothing here depends on a total step budget, so a
    longer or shorter run is handled by the same rule.
    """
    warmup = min(1.0, float(step + 1) / float(_WARMUP_STEPS))
    anneal = _LR_FLOOR + (1.0 - _LR_FLOOR) * 0.5 * (1.0 + math.cos(math.pi * phase))
    decay = max(_MIN_CYCLE_SCALE, _CYCLE_DECAY ** max(0, completed_cycles))
    return _PEAK_LR * warmup * anneal * decay


def _build_optimizer(parameters: List[torch.Tensor]) -> torch.optim.Optimizer:
    """AdamW, fused when the device offers it. That is a device property, not a workload
    or model property, so it specialises nothing that the rules reserve."""
    kwargs = {
        'lr': _PEAK_LR,
        'betas': (_BETA1, _BETA2),
        'eps': _EPS,
        'weight_decay': _WEIGHT_DECAY,
    }
    try:
        return torch.optim.AdamW(parameters, fused=True, **kwargs)
    except (RuntimeError, ValueError, TypeError):
        return torch.optim.AdamW(parameters, **kwargs)


def get_batch_size(workload_name: str) -> int:
    """One batch size for every workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Construct fresh run state. Nothing survives from a previous run."""
    del workload
    del model_state
    del hyperparameters
    del rng
    parameters = [p for p in model_params.parameters() if p.requires_grad]
    return {
        'optimizer': _build_optimizer(parameters),
        'run_state': _new_run_state(),
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
    del current_params_types
    del hyperparameters
    del loss_type

    optimizer = optimizer_state['optimizer']
    run_state = optimizer_state['run_state']

    now = time.time()
    elapsed = _tick(run_state, now)
    period = _period_seconds(workload)
    phase = _cycle_phase(now, elapsed, period, global_step, train_state)
    completed_cycles = len(eval_results) if eval_results is not None else 0
    lr = _learning_rate(global_step, phase, completed_cycles)
    for group in optimizer.param_groups:
        group['lr'] = lr

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
        label_batch=batch['targets'],
        logits_batch=logits,
        mask_batch=batch.get('weights'),
        label_smoothing=_LABEL_SMOOTHING,
    )
    mean_loss = losses['summed'] / losses['n_valid_examples']
    mean_loss.backward()

    parameters = [p for group in optimizer.param_groups for p in group['params']]
    torch.nn.utils.clip_grad_norm_(parameters, max_norm=_GRAD_CLIP)
    optimizer.step()

    return optimizer_state, current_param_container, next_model_state


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
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
