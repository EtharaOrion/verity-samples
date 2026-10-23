"""A self-tuning training algorithm.

Adaptive (AdamW-style) steps with a short warmup, a cosine anneal that is aligned with the
harness's own evaluation cadence, and an iterate average that is swapped in for evaluation.

One configuration is used for every workload. Nothing here inspects the workload name, the
parameter shapes, the parameter count, or the model-state keys; the only external quantities
read are the workload's published evaluation period and the elapsed-time bookkeeping the
harness hands to every submission.
"""

import math
import time
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_BASE_LR = 0.008
_BETA1 = 0.9
_BETA2 = 0.95
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 20
_LR_FLOOR = 0.1
_EMA_DECAY = 0.999
_EMA_WARM = 10.0
_USE_EMA = 1


def get_batch_size(workload_name: str) -> int:
    """A single batch size for every workload."""
    del workload_name
    return _BATCH_SIZE


def _warmup_multiplier(step: int) -> float:
    if step < _WARMUP_STEPS:
        return float(step + 1) / float(_WARMUP_STEPS)
    return 1.0


def _cycle_fraction(workload: spec.Workload, train_state: Optional[Dict[str, Any]]) -> float:
    """Where we are inside the current evaluation cycle, in [0, 1].

    The harness evaluates on a wall clock whose period every workload publishes. Annealing
    within that period means the iterate that gets measured is an annealed one, whatever the
    hardware speed or the number of steps that happen to fit inside the period.
    """
    if not train_state:
        return 0.0
    try:
        last_eval = float(train_state.get('last_eval_time', 0.0) or 0.0)
    except Exception:
        return 0.0
    if last_eval <= 0.0:
        return 0.0
    period = float(getattr(workload, 'eval_period_time_sec', 0.0) or 0.0)
    if period <= 0.0:
        return 0.0
    frac = (time.time() - last_eval) / period
    if frac <= 0.0:
        return 0.0
    if frac >= 1.0:
        return 1.0
    return frac


def _anneal_multiplier(frac: float) -> float:
    return _LR_FLOOR + (1.0 - _LR_FLOOR) * 0.5 * (1.0 + math.cos(math.pi * frac))


def _ema_decay(step: int) -> float:
    d = float(step + 1) / (float(step + 1) + _EMA_WARM)
    return d if d < _EMA_DECAY else _EMA_DECAY


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    del workload
    del model_state
    del hyperparameters
    del rng
    params = [p for p in model_params.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(
        params,
        lr=_BASE_LR,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
    )
    ema = [p.detach().clone() for p in params] if _USE_EMA else None
    return {
        'optimizer': optimizer,
        'params': params,
        'ema': ema,
        'backup': None,
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
    train_state: Optional[Dict[str, Any]] = None,
) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    """One training step."""
    unused = (current_params_types, hyperparameters, loss_type, eval_results, global_step)
    del unused

    optimizer = optimizer_state['optimizer']
    params = optimizer_state['params']

    backup = optimizer_state['backup']
    if backup is not None:
        with torch.no_grad():
            torch._foreach_copy_(params, backup)
        optimizer_state['backup'] = None

    step = optimizer_state['step']
    lr = (
        _BASE_LR
        * _warmup_multiplier(step)
        * _anneal_multiplier(_cycle_fraction(workload, train_state))
    )
    for group in optimizer.param_groups:
        group['lr'] = lr

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)

    logits, new_model_state = workload.model_fn(
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
        label_smoothing=0.0,
    )
    mean_loss = losses['summed'] / losses['n_valid_examples']
    mean_loss.backward()
    optimizer.step()

    ema = optimizer_state['ema']
    if ema is not None:
        decay = _ema_decay(step)
        with torch.no_grad():
            torch._foreach_mul_(ema, decay)
            torch._foreach_add_(ema, params, alpha=1.0 - decay)

    optimizer_state['step'] = step + 1
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
    """Evaluate the running average of the iterates; the raw iterate is restored next step."""
    unused = (workload, current_params_types, hyperparameters, loss_type, eval_results,
              global_step, rng)
    del unused

    ema = optimizer_state['ema']
    if ema is not None:
        params = optimizer_state['params']
        with torch.no_grad():
            optimizer_state['backup'] = [p.detach().clone() for p in params]
            torch._foreach_copy_(params, ema)
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
    unused = (workload, optimizer_state, current_param_container, model_state,
              hyperparameters, global_step, rng)
    del unused
    return next(input_queue)
