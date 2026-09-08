#!/usr/bin/env bash
# Executable oracle. PRIVATE. Harbor mounts solution/ only for its oracle path.
#
# It installs the reference submission into the writable submission path and runs the same three runs
# a model submission would run, through the same invocation contract. Nothing here is a shortcut
# around the graded path: if this script and a model submission produce the same bytes at /submission,
# they are graded identically.
#
# VERITY-CANARY-BLOCK-BEGIN
# 0 VERITY-CANARY-0A7BF95E07CBDB7FB88C839E3C4352C5
# 1 VERITY-CANARY-2B0004CDF4F2A0E2094F4939EC240DD9
# 2 VERITY-CANARY-81B54DFECAF3C6DD48A609ED7B80503A
# 3 VERITY-CANARY-A585DADCF0127B69B14F490BB3E10389
# VERITY-CANARY-BLOCK-END

set -euo pipefail

BUNDLE_ROOT="${VERITY_BUNDLE_ROOT:-/bundle}"
HARNESS_ROOT="${VERITY_HARNESS_ROOT:-/harness}"
SUBMISSION_DIR="${VERITY_SUBMISSION_DIR:-/submission}"
RESULTS_ROOT="${VERITY_RESULTS_ROOT:-/logs/runs}"
DATA_DIR="${VERITY_DATA_DIR:-/data/cifar}"

mkdir -p "${SUBMISSION_DIR}" "${RESULTS_ROOT}"
cp "${BUNDLE_ROOT}/solution/submission.py" "${SUBMISSION_DIR}/submission.py"

run_one() {
  local name="$1" wl="$2" seed="$3" max_steps="$4" ruleset="$5"
  local out="${RESULTS_ROOT}/${name}"
  mkdir -p "${out}"

  local extra=()
  if [[ "${max_steps}" != "none" ]]; then extra+=(--max_global_steps="${max_steps}"); fi
  if [[ "${ruleset}" == "external" ]]; then
    # The search space is a private perturbation parameter and lives in the solution tree, which the
    # agent never sees. The runner takes it as a flag rather than as a submission-tree sibling, so the
    # external run has one without the submitted tree carrying one, which is what keeps
    # C-SEARCH-SPACE-INVARIANT satisfiable under a self-tuning primary.
    extra+=(--tuning_search_space="${BUNDLE_ROOT}/solution/tuning_search_space.json" --num_tuning_trials=5)
  fi

  # algoperf.workloads.workloads.convert_filepath_to_module builds a module name with
  # base.replace('/', '.'), so an absolute --submission_path becomes '.submission.submission', a
  # leading-dot relative module that importlib.import_module refuses without a package. Passing a
  # relative path with the submission directory on PYTHONPATH imports the same bytes by a name the
  # harness can resolve. tests/test.sh has always done this; this script did not, which is why the
  # oracle failed at import on every bundle and `oracle-unrun` was declared on all of them.
  (
    cd "${SUBMISSION_DIR}" || exit 1
    PYTHONPATH="${SUBMISSION_DIR}" python3 "${HARNESS_ROOT}/submission_runner.py" \
      --workload="${wl}" \
      --framework=pytorch \
      --tuning_ruleset="${ruleset}" \
      --submission_path=submission.py \
      --data_dir="${DATA_DIR}" \
      --experiment_dir="${out}" \
      --experiment_name=oracle \
      --rng_seed="${seed}" \
      --save_checkpoints=false \
      "${extra[@]}"
  )

  # The runner writes under {experiment_dir}/{experiment_name}/{workload}_{framework}/trial_{n}/.
  # Lift the evaluation log to the flat location the verifier reads. A missing log is left missing
  # rather than synthesized.
  local produced
  produced="$(find "${out}" -name eval_measurements.csv -print -quit || true)"
  if [[ -n "${produced}" ]]; then cp "${produced}" "${out}/eval_measurements.csv"; fi
}

# The primary objective, then one run per declared perturbation. Every parameter below is private:
# it appears here and in tests/verity_task.json, and never on the agent-visible surface.
run_one primary cifar 20260812 none self
run_one perturbation_held-out-layernorm cifar_layernorm 20260812 none self
run_one perturbation_seed-shift cifar 1468 none self
