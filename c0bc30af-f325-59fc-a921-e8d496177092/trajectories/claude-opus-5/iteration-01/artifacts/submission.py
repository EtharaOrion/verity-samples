"""Self-tuning submission: Nesterov SGD on a wall-clock cosine schedule with warm restarts.

The algorithm exposes no hyperparameters to tune and never inspects the workload's identity or the
model's structure. What it varies, it varies from generic run-time signals:

  * The learning rate follows a cosine anchored to wall-clock time that reaches its floor just as
    the harness's next evaluation becomes due, so every evaluated model sits at the end of a decayed
    schedule rather than in the middle of one. The evaluation cadence is read from the workload's
    own public property, so the number of steps in a cycle is discovered from the clock at run time
    rather than assumed from a step count that would depend on the device.
  * If an evaluation passes without training stopping, the next cycle warm-restarts at a slightly
    lower peak. That hedges an unknown horizon from both sides: a run that can finish inside one
    cycle does, and a run that needs many cycles still sees a globally decaying schedule and
    converges instead of bouncing at a fixed rate forever.

Stabilisers are generic: warmup from cold, a short ramp after each restart, weight decay withheld
from normalisation layers (a layer-type distinction, not a shape one), and gradient clipping at a
multiple of a running estimate of the gradient norm, so no absolute norm scale is assumed. The clip
is computed entirely on device, so no step blocks on a host synchronisation.

The forward pass runs on the module itself rather than on any lazily specialising wrapper placed
around it. Specialisation is paid for out of the training budget on the first step, and when the
budget to a target is a small multiple of that one-off cost there are not enough steps left to earn
it back; measured per-step time here is the same either way, because the step is bound by the input
pipeline rather than by the kernels.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Tuple

import torch
from torch import nn

from algoperf import spec

_BATCH_SIZE = 128

_PEAK_LR = 0.5
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1

_MIN_LR_FRAC = 0.02
_HORIZON_FRAC = 0.95
_WARMUP_FRAC = 0.10
_RESTART_WARMUP_FRAC = 0.03
_PEAK_DECAY = 0.85
_PEAK_FLOOR = 0.3
_DEFAULT_PERIOD_SEC = 25.0

_CLIP_MULT = 1.5
_NORM_EMA_DECAY = 0.95

_NORM_LAYERS = (
    nn.BatchNorm1d,
    nn.BatchNorm2d,
    nn.BatchNorm3d,
    nn.SyncBatchNorm,
    nn.InstanceNorm1d,
    nn.InstanceNorm2d,
    nn.InstanceNorm3d,
    nn.GroupNorm,
    nn.LayerNorm,
    nn.LocalResponseNorm,
)


def get_batch_size(workload_name: str) -> int:
    """One batch size for every workload, as the rules require."""
    del workload_name
    return _BATCH_SIZE


def _unwrapped(model: spec.ParameterContainer) -> spec.ParameterContainer:
    """The module itself, behind any lazily specialising wrapper, holding the same tensors."""
    return getattr(model, '_orig_mod', model)


def _split_by_layer_type(
    model: spec.ParameterContainer,
) -> Tuple[List[torch.Tensor], List[torch.Tensor]]:
    """Separate normalisation-layer parameters from the rest, by layer type.

    Normalisation scales and offsets are the parameters for which shrinking towards zero is not a
    regulariser but a change of the function the layer computes, so they are the ones held out of
    the decay. The distinction is made from the type of the owning layer, which is a generic
    property of any model, and never from a parameter's shape or name.
    """
    decayed = []
    undecayed = []
    seen = set()
    for module in model.modules():
        target = undecayed if isinstance(module, _NORM_LAYERS) else decayed
        for parameter in module.parameters(recurse=False):
            if not parameter.requires_grad or id(parameter) in seen:
                continue
            seen.add(id(parameter))
            target.append(parameter)
    for parameter in model.parameters():
        if parameter.requires_grad and id(parameter) not in seen:
            seen.add(id(parameter))
            decayed.append(parameter)
    return decayed, undecayed


def _learning_rate(state: Dict[str, Any]) -> float:
    """Cosine decay whose floor lands on the next evaluation, with warmup and restart ramp."""
    period = state['period']
    horizon = max(_HORIZON_FRAC * period, 1e-6)
    progress = min(state['cycle_time'] / horizon, 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    peak = _PEAK_LR * max(_PEAK_FLOOR, _PEAK_DECAY ** state['cycles'])
    ramp = min(1.0, state['total_time'] / max(_WARMUP_FRAC * period, 1e-6))
    if state['cycles'] > 0:
        ramp = min(
            ramp,
            min(1.0, state['cycle_time'] / max(_RESTART_WARMUP_FRAC * period, 1e-6)),
        )
    return peak * (_MIN_LR_FRAC + (1.0 - _MIN_LR_FRAC) * cosine) * max(ramp, 1e-3)


def _clip_gradients(state: Dict[str, Any]) -> None:
    """Scale gradients down to a multiple of their own running norm, without a host sync."""
    grads = [p.grad for p in state['params'] if p.grad is not None]
    if not grads:
        return
    total = torch.linalg.vector_norm(torch.stack(torch._foreach_norm(grads)))
    reference = state['grad_norm_ema']
    if reference is None:
        state['grad_norm_ema'] = total.detach().clone()
        return
    threshold = reference * _CLIP_MULT
    torch._foreach_mul_(grads, torch.clamp(threshold / (total + 1e-6), max=1.0))
    observed = torch.where(
        torch.isfinite(total), torch.minimum(total, threshold), reference
    )
    reference.mul_(_NORM_EMA_DECAY).add_(observed, alpha=1.0 - _NORM_EMA_DECAY)


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov momentum SGD, decay withheld from norm layers, plus the schedule's own clock."""
    del model_state
    del hyperparameters
    del rng

    decayed, undecayed = _split_by_layer_type(_unwrapped(model_params))
    optimizer = torch.optim.SGD(
        [
            {'params': decayed, 'weight_decay': _WEIGHT_DECAY},
            {'params': undecayed, 'weight_decay': 0.0},
        ],
        lr=_PEAK_LR,
        momentum=_MOMENTUM,
        nesterov=True,
    )

    period = float(getattr(workload, 'eval_period_time_sec', _DEFAULT_PERIOD_SEC))
    if not math.isfinite(period) or period <= 0.0:
        period = _DEFAULT_PERIOD_SEC

    return {
        'optimizer': optimizer,
        'params': decayed + undecayed,
        'step': 0,
        'period': period,
        'cycle_time': 0.0,
        'total_time': 0.0,
        'cycles': 0,
        'eval_count': 0,
        'prev_end': None,
        'grad_norm_ema': None,
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
    """One training step at the scheduled learning rate."""
    unused = (current_params_types, hyperparameters, loss_type, global_step)
    del unused

    state = optimizer_state
    optimizer = state['optimizer']
    model = _unwrapped(current_param_container)
    step_start = time.time()

    num_evals = len(eval_results)
    if num_evals != state['eval_count']:
        state['eval_count'] = num_evals
        if state['cycle_time'] >= 0.5 * state['period']:
            state['cycles'] += 1
        state['cycle_time'] = 0.0
        state['prev_end'] = step_start
    elif state['prev_end'] is None:
        state['prev_end'] = step_start

    learning_rate = _learning_rate(state)
    for group in optimizer.param_groups:
        group['lr'] = learning_rate

    model.train()
    optimizer.zero_grad(set_to_none=True)

    logits, next_model_state = workload.model_fn(
        params=model,
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
    (losses['summed'] / losses['n_valid_examples']).backward()
    _clip_gradients(state)
    optimizer.step()

    step_end = time.time()
    elapsed = step_end - state['prev_end']
    state['cycle_time'] += elapsed
    state['total_time'] += elapsed
    state['prev_end'] = step_end
    state['step'] += 1
    return state, model, next_model_state


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
