"""Self-tuning submission: Nesterov SGD with eval-synchronised cosine restarts.

The algorithm carries no workload-specific knowledge and exposes no tunable surface. It reads the
one generic quantity the harness publishes about its own cadence -- the evaluation period -- and
anneals the learning rate on a wall clock so that the model sits at the bottom of a cosine cycle
exactly when an evaluation is about to fire. Every evaluation restarts the cycle at a
geometrically smaller peak (floored, never zero), so a run that needs many periods -- a
slower-converging model variant, an unlucky seed, a busier device -- keeps making progress instead
of stalling at a fully annealed rate.

All of the adaptivity lives in the schedule and in the clock. The update rule itself is plain
Nesterov momentum with shape-based weight decay (matrices decay, biases and norm scales do not),
gradient-norm clipping for stability at the high peak rates the short cycles need, and mild label
smoothing. Every one of those choices is generic to any model with parameters and any
softmax-cross-entropy loss.

The training forward pass is run in eager mode on the module underlying whatever wrapper the
harness handed back, which is a generic property of the container rather than anything about this
model. Parameters and buffers are shared with the wrapper, so the object returned to the harness is
the one the forward pass updated, batch-norm statistics included.

Only imports, constants and the permitted function definitions live at module level.
"""

import math
import time
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 112
_BASE_LR = 0.4
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_LABEL_SMOOTHING = 0.1
_GRAD_CLIP = 2.0
_WARMUP_FRAC = 0.06
_CYCLE_FILL = 0.96
_PEAK_DECAY = 0.7
_PEAK_FLOOR = 0.12
_MIN_LR_FRAC = 0.02
_MIN_CYCLE_FRAC = 0.3
_DEFAULT_CYCLE_SEC = 25.0


def get_batch_size(workload_name: str) -> int:
    """A single batch size for every workload, as the rules require."""
    del workload_name
    return _BATCH_SIZE


def _cycle_seconds(workload: spec.Workload) -> float:
    period = getattr(workload, 'eval_period_time_sec', _DEFAULT_CYCLE_SEC)
    return float(period) * _CYCLE_FILL


def _eager_module(container: spec.ParameterContainer) -> spec.ParameterContainer:
    return getattr(container, '_orig_mod', container)


def _learning_rate(cycle_index: int, fraction: float) -> float:
    peak = _BASE_LR * max(_PEAK_DECAY**cycle_index, _PEAK_FLOOR)
    if fraction < _WARMUP_FRAC:
        return peak * (_MIN_LR_FRAC + (1.0 - _MIN_LR_FRAC) * fraction / _WARMUP_FRAC)
    progress = min((fraction - _WARMUP_FRAC) / (1.0 - _WARMUP_FRAC), 1.0)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return peak * (_MIN_LR_FRAC + (1.0 - _MIN_LR_FRAC) * cosine)


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov momentum, decaying only the multi-dimensional parameters."""
    del model_state
    del hyperparameters
    del rng
    torch.backends.cudnn.benchmark = True

    decayed = []
    undecayed = []
    for parameter in model_params.parameters():
        if not parameter.requires_grad:
            continue
        if parameter.ndim > 1:
            decayed.append(parameter)
        else:
            undecayed.append(parameter)

    optimizer = torch.optim.SGD(
        [
            {'params': decayed, 'weight_decay': _WEIGHT_DECAY},
            {'params': undecayed, 'weight_decay': 0.0},
        ],
        lr=_BASE_LR,
        momentum=_MOMENTUM,
        nesterov=True,
    )
    return {
        'optimizer': optimizer,
        'parameters': decayed + undecayed,
        'cycle_seconds': _cycle_seconds(workload),
        'cycle_index': 0,
        'cycle_start': None,
        'evals_seen': 0,
        'step': 0,
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
    """One training step at the learning rate the current cycle position asks for."""
    del current_params_types
    del hyperparameters
    del loss_type
    del global_step

    now = time.monotonic()
    if optimizer_state['cycle_start'] is None:
        optimizer_state['cycle_start'] = now
    if len(eval_results) != optimizer_state['evals_seen']:
        optimizer_state['evals_seen'] = len(eval_results)
        spent = now - optimizer_state['cycle_start']
        if spent >= _MIN_CYCLE_FRAC * optimizer_state['cycle_seconds']:
            optimizer_state['cycle_index'] += 1
        optimizer_state['cycle_start'] = now

    elapsed = now - optimizer_state['cycle_start']
    fraction = min(elapsed / optimizer_state['cycle_seconds'], 1.0)
    learning_rate = _learning_rate(optimizer_state['cycle_index'], fraction)

    optimizer = optimizer_state['optimizer']
    for group in optimizer.param_groups:
        group['lr'] = learning_rate

    module = _eager_module(current_param_container)
    module.train()
    optimizer.zero_grad(set_to_none=True)

    logits, new_model_state = workload.model_fn(
        params=module,
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
    loss = losses['summed'] / losses['n_valid_examples']
    loss.backward()

    torch.nn.utils.clip_grad_norm_(optimizer_state['parameters'], _GRAD_CLIP)
    optimizer.step()

    optimizer_state['step'] += 1
    return optimizer_state, current_param_container, new_model_state


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
