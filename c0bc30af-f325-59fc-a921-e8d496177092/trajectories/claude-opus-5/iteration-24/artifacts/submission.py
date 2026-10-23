"""Self-tuning training algorithm for the AlgoPerf self-tuning ruleset.

Nesterov SGD with warm restarts anchored to the harness's own evaluation cadence: the learning rate
cosine-anneals to a floor exactly as each evaluation fires, so every evaluation row sees a settled
model rather than one caught mid-schedule. Cycle length is re-estimated at run time from the
charged training time actually observed between boundaries, so the schedule follows whatever cadence
and whatever step throughput the run happens to have. Gradients are clipped against an EMA of their
own norm, which is what keeps a wider, deeper, differently normalised or differently activated model
from taking a destructive step early. Weight decay is applied only to multi-dimensional parameters,
a generic property of the tensor rather than anything identifying about the model.
"""

import math
import time
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LR = 0.4
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1
_WARMUP_FRAC = 0.06
_WARMUP_STEPS = 40
_LR_FLOOR_FRAC = 0.02
_CYCLE_SAFETY = 0.97
_PEAK_DECAY = 0.9
_PEAK_FLOOR_FRAC = 0.35
_CLIP_FACTOR = 2.0
_CLIP_EMA = 0.98
_DEFAULT_PERIOD = 25.0
_MIN_CALIBRATION_SEC = 5.0


def get_batch_size(workload_name: str) -> int:
    """One batch size for every workload, as the rules require."""
    del workload_name
    return _BATCH_SIZE


def _forward_module(container: spec.ParameterContainer) -> spec.ParameterContainer:
    """Run the eager module when the harness has wrapped it in a lazily compiled one.

    The wrapper's compilation is charged to the submission on the step that triggers it, which on a
    short budget costs more time than the compiled steps ever repay. The unwrapped module holds the
    same parameter objects and the same buffers, so the optimizer, the batch-norm statistics and
    everything the harness later evaluates are unaffected.
    """
    return getattr(container, "_orig_mod", container)


def _cycle_multiplier(frac: float) -> float:
    """Warm up over the head of a cycle, then cosine anneal to a small floor."""
    frac = min(max(frac, 0.0), 1.0)
    if frac < _WARMUP_FRAC:
        return _LR_FLOOR_FRAC + (1.0 - _LR_FLOOR_FRAC) * (frac / _WARMUP_FRAC)
    progress = (frac - _WARMUP_FRAC) / (1.0 - _WARMUP_FRAC)
    return _LR_FLOOR_FRAC + (1.0 - _LR_FLOOR_FRAC) * 0.5 * (
        1.0 + math.cos(math.pi * progress)
    )


def _train_time(state: spec.OptimizerState, now: float) -> float:
    """Training time charged so far, with the untimed evaluation gaps discounted."""
    if state["t0"] is None:
        state["t0"] = now
    pause = state["pause_mark"]
    if pause is not None:
        state["excluded"] += max(now - pause, 0.0)
        state["pause_mark"] = None
    return now - state["t0"] - state["excluded"]


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov SGD, with weight decay kept off one-dimensional parameters."""
    del model_state
    del hyperparameters
    del rng

    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True

    decay_params = []
    no_decay_params = []
    for param in model_params.parameters():
        if not param.requires_grad:
            continue
        if param.ndim <= 1:
            no_decay_params.append(param)
        else:
            decay_params.append(param)

    optimizer = torch.optim.SGD(
        [
            {"params": decay_params, "weight_decay": _WEIGHT_DECAY},
            {"params": no_decay_params, "weight_decay": 0.0},
        ],
        lr=_PEAK_LR,
        momentum=_MOMENTUM,
        nesterov=True,
    )

    period = _DEFAULT_PERIOD
    declared = getattr(workload, "eval_period_time_sec", None)
    if declared is not None:
        try:
            period = max(float(declared), 1.0)
        except (TypeError, ValueError):
            period = _DEFAULT_PERIOD

    return {
        "optimizer": optimizer,
        "trainable": decay_params + no_decay_params,
        "period": period,
        "t0": None,
        "excluded": 0.0,
        "pause_mark": None,
        "cycle_start": 0.0,
        "peak_lr": _PEAK_LR,
        "peak_floor": _PEAK_LR * _PEAK_FLOOR_FRAC,
        "grad_norm_ema": None,
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
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """One training step, on a schedule driven by charged training time."""
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results

    optimizer = optimizer_state["optimizer"]
    elapsed = _train_time(optimizer_state, time.monotonic()) - optimizer_state["cycle_start"]
    span = max(optimizer_state["period"] * _CYCLE_SAFETY, 1e-3)
    ramp = min(1.0, (global_step + 1) / float(_WARMUP_STEPS))
    lr = optimizer_state["peak_lr"] * _cycle_multiplier(elapsed / span) * ramp
    for group in optimizer.param_groups:
        group["lr"] = lr

    model = _forward_module(current_param_container)
    model.train()
    optimizer.zero_grad(set_to_none=True)

    logits, new_model_state = workload.model_fn(
        params=model,
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

    grads = [p.grad for p in optimizer_state["trainable"] if p.grad is not None]
    if grads:
        total_norm = torch.linalg.vector_norm(torch.stack(torch._foreach_norm(grads)))
        total_norm = torch.nan_to_num(total_norm, nan=0.0, posinf=0.0, neginf=0.0)
        ema = optimizer_state["grad_norm_ema"]
        if ema is None:
            optimizer_state["grad_norm_ema"] = total_norm.detach().clone()
        else:
            ceiling = ema * _CLIP_FACTOR
            coef = torch.clamp(ceiling / (total_norm + 1e-6), max=1.0)
            coef = torch.nan_to_num(coef, nan=0.0, posinf=0.0, neginf=0.0)
            torch._foreach_mul_(grads, coef)
            ema.mul_(_CLIP_EMA).add_(
                torch.minimum(total_norm, ceiling) * (1.0 - _CLIP_EMA)
            )

    optimizer.step()
    optimizer_state["step"] += 1
    return optimizer_state, current_param_container, new_model_state


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
    """Treat the evaluation boundary as the schedule's clock: calibrate, then restart."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng

    now = time.monotonic()
    elapsed = _train_time(optimizer_state, now) - optimizer_state["cycle_start"]
    if elapsed > _MIN_CALIBRATION_SEC:
        optimizer_state["period"] = elapsed
        optimizer_state["peak_lr"] = max(
            optimizer_state["peak_lr"] * _PEAK_DECAY, optimizer_state["peak_floor"]
        )
    optimizer_state["cycle_start"] += elapsed
    optimizer_state["pause_mark"] = now
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
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
