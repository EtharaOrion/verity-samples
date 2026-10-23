"""A single self-tuning training algorithm, identical for every workload.

The update rule is adaptive-moment descent (Adam-style, decoupled weight decay set to zero)
with a short linear warmup, a slow linear decay of the step size anchored to the workload's
own published step hint, and an exponential moving average of the iterates that is swapped in
for evaluation and swapped back out before the next training step.

Nothing here inspects the workload's identity, its parameter shapes, its parameter count or
its state keys: the same constants and the same update rule are used everywhere, and the only
workload-derived quantity is the generic `step_hint` property that the spec exposes for all
workloads (with a fallback when it is absent).
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 128
_PEAK_LR = 0.008
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 40
_FINAL_LR_FRAC = 0.1
_MIN_HORIZON = 2000
_HORIZON_FRAC = 0.5
_DEFAULT_HORIZON = 4000
_EMA_DECAY = 0.999
_EMA_WARM = 10.0


def get_batch_size(workload_name: str) -> int:
    """One batch size for every workload, as the rules require."""
    del workload_name
    return _BATCH_SIZE


def _horizon(workload: spec.Workload) -> int:
    """Length of the decay ramp, taken from the generic step hint when one exists."""
    hint = getattr(workload, 'step_hint', None)
    try:
        hint = int(hint)
    except (TypeError, ValueError):
        hint = 0
    if hint <= 0:
        return _DEFAULT_HORIZON
    return max(_MIN_HORIZON, int(_HORIZON_FRAC * hint))


def _lr_scale(step: int, horizon: int) -> float:
    if step < _WARMUP_STEPS:
        return float(step + 1) / float(_WARMUP_STEPS)
    span = float(max(1, horizon - _WARMUP_STEPS))
    progress = min(1.0, (step - _WARMUP_STEPS) / span)
    return _FINAL_LR_FRAC + (1.0 - _FINAL_LR_FRAC) * (1.0 - progress)


def init_optimizer_state(
    workload: spec.Workload,
    model_params: spec.ParameterContainer,
    model_state: spec.ModelAuxiliaryState,
    hyperparameters: spec.Hyperparameters,
    rng: spec.RandomState,
) -> spec.OptimizerState:
    del model_state
    del hyperparameters
    del rng
    params = [p for p in model_params.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(
        params,
        lr=_PEAK_LR,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
        weight_decay=_WEIGHT_DECAY,
        foreach=True,
    )
    ema = [p.detach().clone() for p in params]
    return {
        'optimizer': optimizer,
        'params': params,
        'ema': ema,
        'backup': None,
        'step': 0,
        'horizon': _horizon(workload),
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
    unused = (
        current_params_types,
        hyperparameters,
        loss_type,
        eval_results,
        global_step,
        train_state,
    )
    del unused

    optimizer = optimizer_state['optimizer']
    params = optimizer_state['params']

    # If the last evaluation swapped the averaged iterate in, put the training
    # iterate back before taking another step.
    backup = optimizer_state.get('backup')
    if backup is not None:
        with torch.no_grad():
            for p, b in zip(params, backup):
                p.copy_(b)
        optimizer_state['backup'] = None

    step = optimizer_state['step']
    lr = _PEAK_LR * _lr_scale(step, optimizer_state['horizon'])
    for group in optimizer.param_groups:
        group['lr'] = lr

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
        label_batch=batch['targets'],
        logits_batch=logits,
        mask_batch=batch.get('weights'),
        label_smoothing=0.0,
    )
    mean_loss = losses['summed'] / losses['n_valid_examples']
    mean_loss.backward()
    optimizer.step()

    # Iterate averaging, with an early-step ramp so the average is not anchored
    # to the random initialisation.
    decay = min(_EMA_DECAY, (1.0 + step) / (_EMA_WARM + step))
    with torch.no_grad():
        torch._foreach_lerp_(
            optimizer_state['ema'], [p.detach() for p in params], 1.0 - decay
        )

    optimizer_state['step'] = step + 1
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
    """Evaluate the averaged iterate, keeping the training iterate for the next step."""
    unused = (
        workload,
        current_params_types,
        hyperparameters,
        loss_type,
        eval_results,
        global_step,
        rng,
    )
    del unused
    params = optimizer_state['params']
    with torch.no_grad():
        # Only take a backup if the training iterate is currently live, so a
        # second call before the next step cannot overwrite it with the average.
        if optimizer_state.get('backup') is None:
            optimizer_state['backup'] = [p.detach().clone() for p in params]
        for p, e in zip(params, optimizer_state['ema']):
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
