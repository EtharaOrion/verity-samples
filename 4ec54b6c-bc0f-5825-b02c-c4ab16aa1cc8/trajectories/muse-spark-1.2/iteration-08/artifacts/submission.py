"""Robust MNIST AdamW across variants - final."""
from typing import Any, Dict, Iterator, List, Optional, Tuple
import math
import torch
from algoperf import spec
_BATCH_SIZE = 256
_BASE_LR = 0.003
_WEIGHT_DECAY = 0.01
_WARMUP_FRAC = 0.05
_TOTAL = 6000

def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE

def _lr_schedule(step: int) -> float:
    warmup = max(1, int(_TOTAL * _WARMUP_FRAC))
    if step < warmup:
        return _BASE_LR * float(step + 1) / float(warmup)
    prog = (step - warmup) / max(1, _TOTAL - warmup)
    return _BASE_LR * 0.5 * (1.0 + math.cos(math.pi * min(prog, 1.0)))

def init_optimizer_state(workload, model_params, model_state, hyperparameters, rng):
    del workload
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.AdamW(
        model_params.parameters(),
        lr=_BASE_LR,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=_WEIGHT_DECAY,
    )
    return {"optimizer": optimizer}

def update_params(workload, current_param_container, current_params_types, model_state, hyperparameters, batch, loss_type, optimizer_state, eval_results, global_step, rng):
    del current_params_types
    del hyperparameters
    del eval_results
    lr = _lr_schedule(global_step)
    for pg in optimizer_state["optimizer"].param_groups:
        pg["lr"] = lr
    opt = optimizer_state["optimizer"]
    current_param_container.train()
    opt.zero_grad()
    outputs = workload.model_fn(
        params=current_param_container,
        augmented_and_preprocessed_input_batch=batch,
        model_state=model_state,
        mode=spec.ForwardPassMode.TRAIN,
        rng=rng,
        update_batch_norm=True,
    )
    predictions, next_state = outputs
    losses = workload.loss_fn(
        label_batch=batch["targets"],
        logits_batch=predictions,
        mask_batch=batch.get("weights"),
        label_smoothing=0.0,
    )
    mean_loss = losses["summed"] / losses["n_valid_examples"]
    mean_loss.backward()
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), 1.0)
    opt.step()
    return optimizer_state, current_param_container, next_state

def data_selection(workload, input_queue, optimizer_state, current_param_container, model_state, hyperparameters, global_step, rng):
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
