from typing import Any, Dict, Iterator, List, Optional, Tuple
import torch
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR
from algoperf import spec
_BATCH_SIZE=256
_LEARNING_RATE=0.008
_WEIGHT_DECAY=0.005
_WARMUP_FRAC=0.02
_TOTAL_FRAC=0.5
def get_batch_size(workload_name: str) -> int:
    del workload_name
    return _BATCH_SIZE
def init_optimizer_state(workload: spec.Workload, model_params: spec.ParameterContainer, model_state: spec.ModelAuxiliaryState, hyperparameters: spec.Hyperparameters, rng: spec.RandomState) -> spec.OptimizerState:
    del model_state
    del hyperparameters
    del rng
    optimizer = torch.optim.AdamW(model_params.parameters(), lr=_LEARNING_RATE, betas=(0.9, 0.999), eps=1e-8, weight_decay=_WEIGHT_DECAY)
    step_hint = int(workload.step_hint)
    warmup_steps = max(int(_WARMUP_FRAC * step_hint), 1)
    total_steps = max(int(_TOTAL_FRAC * step_hint), warmup_steps + 1)
    warmup = LinearLR(optimizer, start_factor=1e-10, end_factor=1.0, total_iters=warmup_steps)
    cosine = CosineAnnealingLR(optimizer, T_max=max(total_steps - warmup_steps, 1))
    scheduler = SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])
    return {"optimizer": optimizer, "scheduler": scheduler}
def update_params(workload: spec.Workload, current_param_container: spec.ParameterContainer, current_params_types: spec.ParameterTypeTree, model_state: spec.ModelAuxiliaryState, hyperparameters: spec.Hyperparameters, batch: Dict[str, spec.Tensor], loss_type: spec.LossType, optimizer_state: spec.OptimizerState, eval_results: List[Tuple[int, float]], global_step: int, rng: spec.RandomState, train_state: Optional[Dict[str, Any]] = None) -> Tuple[spec.OptimizerState, spec.ParameterContainer, spec.ModelAuxiliaryState]:
    del current_params_types
    del hyperparameters
    del loss_type
    del eval_results
    del train_state
    optimizer = optimizer_state["optimizer"]
    scheduler = optimizer_state["scheduler"]
    current_param_container.train()
    optimizer.zero_grad()
    logits_batch, new_model_state = workload.model_fn(params=current_param_container, augmented_and_preprocessed_input_batch=batch, model_state=model_state, mode=spec.ForwardPassMode.TRAIN, rng=rng, update_batch_norm=True)
    loss_dict = workload.loss_fn(label_batch=batch["targets"], logits_batch=logits_batch, mask_batch=batch.get("weights"), label_smoothing=0.0)
    loss = loss_dict["summed"] / loss_dict["n_valid_examples"]
    loss.backward()
    torch.nn.utils.clip_grad_norm_(current_param_container.parameters(), max_norm=1.0)
    optimizer.step()
    scheduler.step()
    return optimizer_state, current_param_container, new_model_state
def data_selection(workload: spec.Workload, input_queue: Iterator[Dict[str, spec.Tensor]], optimizer_state: spec.OptimizerState, current_param_container: spec.ParameterContainer, model_state: spec.ModelAuxiliaryState, hyperparameters: spec.Hyperparameters, global_step: int, rng: spec.RandomState) -> Dict[str, spec.Tensor]:
    del workload
    del optimizer_state
    del current_param_container
    del model_state
    del hyperparameters
    del global_step
    del rng
    return next(input_queue)
