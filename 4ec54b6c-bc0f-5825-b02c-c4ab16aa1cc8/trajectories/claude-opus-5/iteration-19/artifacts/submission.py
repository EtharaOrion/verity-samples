"""A self-tuning training algorithm.

One fixed configuration, applied identically to every workload and every model:

  * NAdam, which gives each coordinate its own effective step size and carries Nesterov
    momentum, so the algorithm needs no per-workload step-size choice.
  * A short linear warmup followed by an inverse-square-root decay. The warmup keeps the
    first updates from being dominated by the optimizer's own uninitialised second-moment
    estimate; the decay lets the run settle without ever needing to know how long it will be.
  * Global gradient-norm clipping, which bounds the damage a single unlucky batch can do and
    is what makes one step size usable across activations and normalisations that scale
    gradients very differently.
  * Mild label smoothing on the softmax cross-entropy loss.
  * An exponential moving average of the weights, bias-corrected early through a warmup on
    the decay itself, swapped in for evaluation and swapped straight back out afterwards so
    training always continues from the raw iterate.

Nothing here inspects the workload's identity, the parameter shapes or counts, or the keys of
the model state. Every choice is a constant or is derived from the step counter alone.
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 256
_PEAK_LR = 0.012
_WARMUP_STEPS = 10
_DECAY_TAU = 600.0
_BETA1 = 0.9
_BETA2 = 0.99
_EPS = 1e-8
_LABEL_SMOOTHING = 0.05
_CLIP_NORM = 1.0
_EMA_DECAY = 0.99
_EMA_WARMUP = 10.0


def _learning_rate(step: int) -> float:
    """Linear warmup into an inverse-square-root decay, in units of the peak rate."""
    warm = min(1.0, float(step + 1) / float(_WARMUP_STEPS))
    decay = (1.0 + float(step) / _DECAY_TAU) ** -0.5
    return _PEAK_LR * warm * decay


def _ema_rate(step: int) -> float:
    """EMA decay, warmed up so the average is not anchored to the initialisation."""
    return min(_EMA_DECAY, (1.0 + float(step)) / (_EMA_WARMUP + float(step)))


def _unswap(optimizer_state: Dict[str, Any], params: List[Any]) -> None:
    """Put the raw training iterate back if an averaged one was swapped in for an eval."""
    backup = optimizer_state.get('backup')
    if backup is None:
        return
    with torch.no_grad():
        for param, saved in zip(params, backup):
            param.copy_(saved)
    optimizer_state['backup'] = None


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
    del workload
    del model_state
    del hyperparameters
    del rng
    params = [p for p in model_params.parameters() if p.requires_grad]
    optimizer = torch.optim.NAdam(
        params,
        lr=_PEAK_LR,
        betas=(_BETA1, _BETA2),
        eps=_EPS,
    )
    shadow = [p.detach().clone() for p in params] if _EMA_DECAY > 0.0 else None
    return {'optimizer': optimizer, 'shadow': shadow, 'backup': None, 'step': 0}


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
    del eval_results
    del loss_type
    del train_state

    optimizer = optimizer_state['optimizer']
    params = optimizer.param_groups[0]['params']
    shadow = optimizer_state['shadow']

    _unswap(optimizer_state, params)

    step = optimizer_state['step']
    lr = _learning_rate(step)
    for group in optimizer.param_groups:
        group['lr'] = lr

    current_param_container.train()
    for param in params:
        param.grad = None

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

    if _CLIP_NORM > 0.0:
        torch.nn.utils.clip_grad_norm_(params, _CLIP_NORM)
    optimizer.step()

    if shadow is not None:
        decay = _ema_rate(step)
        with torch.no_grad():
            for avg, param in zip(shadow, params):
                avg.mul_(decay).add_(param.detach(), alpha=1.0 - decay)

    optimizer_state['step'] = step + 1
    del global_step
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
    """Swap the averaged weights in for the upcoming evaluation."""
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng

    shadow = optimizer_state['shadow']
    if shadow is not None and optimizer_state.get('backup') is None:
        params = optimizer_state['optimizer'].param_groups[0]['params']
        with torch.no_grad():
            optimizer_state['backup'] = [p.detach().clone() for p in params]
            for param, avg in zip(params, shadow):
                param.copy_(avg)
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
