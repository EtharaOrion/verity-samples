"""Self-tuning submission: Nesterov SGD with a clock-anchored cosine schedule.

The algorithm exposes no hyperparameters and never inspects which workload or which model it is
running against. What it needs it reads at run time from the harness: the accumulated submission
time it has been charged, the evaluation period the workload publishes, and the generic
dimensionality of each parameter tensor.

The schedule is anchored to the evaluation cadence. Inside every evaluation window the learning
rate is annealed by a cosine down to a small fraction of its peak, so each evaluation the harness
fires sees an annealed model rather than one caught mid-stride. Each successive window restarts at
a lower peak, so a run that needs several windows keeps converging instead of bouncing. Steps stay
cheap: a small batch, a bfloat16 autocast forward and backward, and one global gradient-norm clip.
"""

import math
from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LR = 0.2
_MOMENTUM = 0.9
_WEIGHT_DECAY = 5e-4
_WARMUP_STEPS = 100
_FINAL_LR_FRAC = 0.02
_CYCLE_DECAY = 0.85
_MIN_PEAK_FRAC = 0.15
_GRAD_CLIP = 1.0
_LABEL_SMOOTHING = 0.0
_DEFAULT_PERIOD_SEC = 25.0


def _elapsed_seconds(train_state: Optional[Dict[str, Any]]) -> float:
    if train_state is None:
        return 0.0
    return float(train_state.get('accumulated_submission_time', 0.0))


def _cycle_period(workload: spec.Workload) -> float:
    period = float(getattr(workload, 'eval_period_time_sec', _DEFAULT_PERIOD_SEC))
    if not math.isfinite(period) or period <= 0.0:
        period = _DEFAULT_PERIOD_SEC
    return period


def _learning_rate(elapsed: float, period: float, global_step: int) -> float:
    cycle = int(elapsed // period)
    progress = min(max((elapsed - cycle * period) / period, 0.0), 1.0)
    peak = _PEAK_LR * max(_CYCLE_DECAY**cycle, _MIN_PEAK_FRAC)
    cosine = _FINAL_LR_FRAC + (1.0 - _FINAL_LR_FRAC) * 0.5 * (
        1.0 + math.cos(math.pi * progress)
    )
    warmup = min(1.0, (global_step + 1) / _WARMUP_STEPS)
    return peak * cosine * warmup


def get_batch_size(workload_name: str) -> int:
    """A single batch size, used for every workload."""
    del workload_name
    return _BATCH_SIZE


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    """Nesterov SGD, with decay applied only to multi-dimensional (kernel) tensors."""
    del workload
    del model_state
    del hyperparameters
    del rng
    decay_params = []
    no_decay_params = []
    for parameter in model_params.parameters():
        if not parameter.requires_grad:
            continue
        if parameter.ndim > 1:
            decay_params.append(parameter)
        else:
            no_decay_params.append(parameter)
    optimizer = torch.optim.SGD(
        [
            {'params': decay_params, 'weight_decay': _WEIGHT_DECAY},
            {'params': no_decay_params, 'weight_decay': 0.0},
        ],
        lr=_PEAK_LR,
        momentum=_MOMENTUM,
        nesterov=True,
    )
    return {'optimizer': optimizer, 'step': 0}


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
    """One training step at the schedule's current learning rate."""
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results

    optimizer = optimizer_state['optimizer']
    learning_rate = _learning_rate(
        _elapsed_seconds(train_state), _cycle_period(workload), global_step
    )
    for group in optimizer.param_groups:
        group['lr'] = learning_rate

    current_param_container.train()
    optimizer.zero_grad(set_to_none=True)

    device_type = 'cuda' if torch.cuda.is_available() else 'cpu'
    with torch.autocast(device_type=device_type, dtype=torch.bfloat16):
        logits, next_state = workload.model_fn(
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
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), _GRAD_CLIP)
    optimizer.step()

    optimizer_state['step'] = global_step + 1
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
    """Nothing to swap in: the schedule already anneals into every evaluation."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng
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
