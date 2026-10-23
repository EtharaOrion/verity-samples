"""Self-tuning training algorithm: orthogonalised momentum steps with iterate averaging."""

import math
from typing import Dict, Iterator, List, Tuple

import torch

from algoperf import spec

_BATCH_SIZE = 1024
_MICRO_BATCH = 128
_MATRIX_LR = 0.02
_VECTOR_LR = 0.008
_MOMENTUM = 0.95
_BETA1 = 0.9
_BETA2 = 0.95
_EPS = 1e-8
_WEIGHT_DECAY = 0.0
_WARMUP_STEPS = 15
_NS_STEPS = 5
_NS_A = 3.4445
_NS_B = -4.7750
_NS_C = 2.0315
_EMA_MAX_DECAY = 0.999
_EMA_HORIZON = 10.0


def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE


def _orthogonalise(grad: torch.Tensor) -> torch.Tensor:
    x = grad.float()
    x = x / (x.norm() + 1e-7)
    transposed = x.shape[0] > x.shape[1]
    if transposed:
        x = x.t()
    for _ in range(_NS_STEPS):
        a = x @ x.t()
        b = _NS_B * a + _NS_C * (a @ a)
        x = _NS_A * x + b @ x
    if transposed:
        x = x.t()
    return x


def _split_params(container: spec.ParameterContainer):
    trainable = [p for p in container.parameters() if p.requires_grad]
    planes = [p for p in trainable if p.ndim == 2]
    rest = [p for p in trainable if p.ndim != 2]
    return trainable, planes, rest


def _build_optimizer(params: List[torch.Tensor]):
    if not params:
        return None
    try:
        return torch.optim.AdamW(params, lr=_VECTOR_LR, betas=(_BETA1, _BETA2),
                                 eps=_EPS, weight_decay=_WEIGHT_DECAY, fused=True)
    except (RuntimeError, ValueError, TypeError):
        return torch.optim.AdamW(params, lr=_VECTOR_LR, betas=(_BETA1, _BETA2),
                                 eps=_EPS, weight_decay=_WEIGHT_DECAY)


def _warmup(workload, model_params, model_state) -> None:
    affine = [m for m in model_params.modules() if isinstance(m, torch.nn.Linear)]
    if not affine:
        return
    device = affine[0].weight.device
    fan_in = affine[0].in_features
    side = int(math.isqrt(fan_in))
    shapes = [(_MICRO_BATCH, fan_in), (_MICRO_BATCH, 1, side, side)]
    targets = torch.zeros(_MICRO_BATCH, dtype=torch.long, device=device)
    for shape in shapes:
        try:
            fake = {'inputs': torch.zeros(*shape, device=device), 'targets': targets}
            model_params.train()
            logits, _ = workload.model_fn(
                params=model_params,
                augmented_and_preprocessed_input_batch=fake,
                model_state=model_state,
                mode=spec.ForwardPassMode.TRAIN,
                rng=None,
                update_batch_norm=False,
            )
            losses = workload.loss_fn(label_batch=targets, logits_batch=logits)
            (losses['summed'] / losses['n_valid_examples']).backward()
            for p in model_params.parameters():
                if p.ndim == 2 and p.grad is not None:
                    _orthogonalise(p.grad)
        except Exception:  # pylint: disable=broad-except
            pass
    try:
        model_params.zero_grad(set_to_none=True)
    except Exception:  # pylint: disable=broad-except
        pass


def _restore_raw(optimizer_state, params) -> None:
    if optimizer_state.get('swapped'):
        with torch.no_grad():
            for p, b in zip(params, optimizer_state['backup']):
                p.copy_(b)
        optimizer_state['swapped'] = False


def init_optimizer_state(workload, model_params, model_state, hyperparameters, rng):
    del hyperparameters
    del rng
    _warmup(workload, model_params, model_state)
    trainable, planes, rest = _split_params(model_params)
    return {
        'optimizer': _build_optimizer(rest),
        'params': trainable,
        'planes': planes,
        'momentum': [torch.zeros_like(p) for p in planes],
        'ema': [p.detach().clone() for p in trainable],
        'backup': [p.detach().clone() for p in trainable],
        'swapped': False,
        'step': 0,
        'chunk': None,
        'order': None,
        'cursor': 0,
    }


def update_params(workload, current_param_container, current_params_types, model_state,
                  hyperparameters, batch, loss_type, optimizer_state, eval_results,
                  global_step, rng):
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step

    params = optimizer_state['params']
    planes = optimizer_state['planes']
    optimizer = optimizer_state['optimizer']
    _restore_raw(optimizer_state, params)

    current_param_container.train()
    for p in params:
        p.grad = None

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
    (losses['summed'] / losses['n_valid_examples']).backward()

    step = optimizer_state['step'] + 1
    optimizer_state['step'] = step
    scale = min(1.0, step / _WARMUP_STEPS)

    with torch.no_grad():
        for p, buf in zip(planes, optimizer_state['momentum']):
            if p.grad is None:
                continue
            buf.mul_(_MOMENTUM).add_(p.grad)
            direction = p.grad.add(buf, alpha=_MOMENTUM)
            shape_gain = math.sqrt(max(1.0, p.shape[0] / p.shape[1]))
            p.add_(_orthogonalise(direction), alpha=-_MATRIX_LR * scale * shape_gain)

    if optimizer is not None:
        for group in optimizer.param_groups:
            group['lr'] = _VECTOR_LR * scale
        optimizer.step()

    decay = min(_EMA_MAX_DECAY, (1.0 + step) / (_EMA_HORIZON + step))
    with torch.no_grad():
        ema = optimizer_state['ema']
        torch._foreach_mul_(ema, decay)
        torch._foreach_add_(ema, params, alpha=1.0 - decay)

    return optimizer_state, current_param_container, next_state


def prepare_for_eval(workload, current_param_container, current_params_types, model_state,
                     hyperparameters, loss_type, optimizer_state, eval_results,
                     global_step, rng):
    del workload
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del global_step
    del rng
    if optimizer_state['step'] > 0 and not optimizer_state['swapped']:
        params = optimizer_state['params']
        with torch.no_grad():
            for b, p, e in zip(optimizer_state['backup'], params, optimizer_state['ema']):
                b.copy_(p)
                p.copy_(e)
        optimizer_state['swapped'] = True
    return optimizer_state, current_param_container, model_state


def data_selection(workload, input_queue, optimizer_state, current_param_container,
                   model_state, hyperparameters, global_step, rng):
    del workload
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    chunk = optimizer_state.get('chunk')
    cursor = optimizer_state.get('cursor', 0)
    if chunk is None or cursor + _MICRO_BATCH > chunk['targets'].shape[0]:
        chunk = next(input_queue)
        size = chunk['targets'].shape[0]
        if size < _MICRO_BATCH:
            optimizer_state['chunk'] = None
            optimizer_state['cursor'] = 0
            return chunk
        optimizer_state['chunk'] = chunk
        optimizer_state['order'] = torch.randperm(size, device=chunk['targets'].device)
        cursor = 0
    index = optimizer_state['order'][cursor:cursor + _MICRO_BATCH]
    optimizer_state['cursor'] = cursor + _MICRO_BATCH
    micro = {'inputs': chunk['inputs'][index], 'targets': chunk['targets'][index]}
    weights = chunk.get('weights')
    if weights is not None:
        micro['weights'] = weights[index]
    return micro
