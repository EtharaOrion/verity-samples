#!/usr/bin/env bash
# Harbor verifier entry point.
#
# This script is the only writer of the reward contract path, and it writes it on every code path
# including every early exit. A zero is always attributable to a machine-readable reason rather than to an
# unwritten or empty reward file, because Harbor raises on an empty file rather than scoring zero.
#
# It never calls scoring/score_submissions.py, which does not execute under the harness's own pinned NumPy
# floor, and it never trusts the runner exit value, which returns the lowest trial index rather than the
# fastest timing.

set -uo pipefail

BUNDLE_ROOT="${VERITY_BUNDLE_ROOT:-/bundle}"
HARNESS_ROOT="${VERITY_HARNESS_ROOT:-/harness}"
SUBMISSION_DIR="${VERITY_SUBMISSION_DIR:-/submission}"
RESULTS_ROOT="${VERITY_RESULTS_ROOT:-/logs/runs}"
OUTPUT_DIR="${VERITY_OUTPUT_DIR:-/logs/verifier}"
NETWORK_EVIDENCE="${VERITY_NETWORK_EVIDENCE:-/logs/env/network_probe.log}"
NETWORK_MODE="${VERITY_NETWORK_MODE:-no-network}"
SENTINEL="${OUTPUT_DIR}/.verity_sentinel"

mkdir -p "${OUTPUT_DIR}"

# The sentinel is written before anything reads the agent phase result. C-NO-REWARD-WRITE compares the
# reward file against it, so a reward file the agent left behind carries no sentinel and is caught.
if [[ ! -f "${SENTINEL}" ]]; then
  head -c 32 /dev/urandom | od -An -tx1 | tr -d ' \n' > "${SENTINEL}"
fi

fail_closed() {
  # Infrastructure failure. Reward zero with zero_reason_code 5, written directly so a failure inside the
  # driver still produces a parseable contract rather than an absent file.
  local reason="$1"
  python3 - "$OUTPUT_DIR" "$reason" <<'PY'
import json, sys
out, reason = sys.argv[1], sys.argv[2]
payload = {
    "reward": 0.0, "validity": 0.0, "conformance_fraction": 0.0, "closure": 0.0, "task_pass": 0.0,
    "primary_target_reached": 0.0, "qualifying_budget": -1.0, "best_metric": -1.0, "seed_metric": -1.0,
    "reference_budget": -1.0, "perturbations_declared": 0.0, "perturbations_reached": 0.0,
    "red_line_crossed": 0.0, "zero_reason_code": 5.0, "wall_clock_sec": -1.0,
}
with open(out + "/reward.json", "w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")
with open(out + "/verity_detail.json", "w", encoding="utf-8") as handle:
    json.dump({"steps": [], "checks": [], "notes": [reason]}, handle, indent=2, sort_keys=True)
    handle.write("\n")
PY
  exit 0
}

# Environment probe. C-NETWORK-POLICY-HONOURED asserts that observed reachability matches the policy the
# bundle declares, and it fails closed on an absent record because an unobserved network is not an observed
# one. The record has to be written by the environment rather than by the submission, or a submission could
# clear the check by writing its own. This is the verifier entry point, which runs after the agent phase has
# ended, so it is the environment's side of that boundary. The file is overwritten rather than appended for
# the same reason: anything the agent phase left at this path is not evidence.
mkdir -p "$(dirname "${NETWORK_EVIDENCE}")"
python3 - "$NETWORK_EVIDENCE" <<'PY' || true
import socket, sys

# Three unrelated endpoints, so a single unreachable host is not read as a closed network. Each is a raw
# TCP connect with a short timeout: no name is resolved that is not also connected to, and nothing here
# depends on an HTTP client being installed in the graded image.
TARGETS = (("pypi.org", 443), ("1.1.1.1", 443), ("8.8.8.8", 53))

lines = ["# written by tests/test.sh at the start of the verifier phase, one record per line"]
for host, port in TARGETS:
    try:
        with socket.create_connection((host, port), timeout=4):
            outcome = "reached"
    except OSError:
        outcome = "blocked"
    lines.append("%s:%d %s" % (host, port, outcome))

with open(sys.argv[1], "w", encoding="utf-8") as handle:
    handle.write("\n".join(lines) + "\n")
PY

# The graded runs. Without these the verifier reads an evaluation log that nothing produced: the only
# caller of submission_runner.py in a bundle is solution/solve.sh, which lives in the private oracle tree,
# so a model submission was never executed on any path and no attempt could be graded. The plan is derived
# from the run specification rather than written out here, so a slot's perturbation set is declared in one
# place and this entry point grades whatever it declares.
#
# A run that fails leaves its evaluation log absent rather than synthesized. The driver reports the absence,
# which is a real outcome attributable to the submitted bytes.
# Read here rather than defaulted, and read at the point of use rather than later: the script
# runs under set -u, so a forward reference to a variable assigned further down aborts before
# the first run. VERITY_DATA_DIR is ambient image state naming mnist on every image built from
# the shared base, and ${VAR:-fallback} yields the fallback only when VAR is unset, so a shell
# default cannot override it. run.data_dir is the bundle own declaration. fail_closed rather
# than default, because a wrong dataset path surfaces as a missing dataset, which reads as an
# environment fault rather than as the spec gap it is.
DATA_DIR="$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["run"]["data_dir"])' "${BUNDLE_ROOT}/tests/verity_task.json")" || fail_closed "the run specification declares no data_dir"
mkdir -p "${RESULTS_ROOT}"

if [[ ! -f "${SUBMISSION_DIR}/submission.py" ]]; then
  fail_closed "no submission at ${SUBMISSION_DIR}/submission.py, so no run could be performed"
fi

STUB_DIR="${VERITY_STUB_DIR:-${BUNDLE_ROOT}/environment/submission_stub}"

# The framework is a field of the run specification, not a property of this script. The bundle
# already parses that file three lines below to build the run plan; reading one more key from it
# keeps the invocation contract in one place.
FRAMEWORK="$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["harness"]["framework"])' "${BUNDLE_ROOT}/tests/verity_task.json")" || fail_closed "the run specification declares no framework"

RUN_PLAN="$(python3 - "${BUNDLE_ROOT}/tests/verity_task.json" <<'PY'
import json, sys

# The step cap for the seed calibration unit, held identical to SEED_CALIBRATION_MAX_GLOBAL_STEPS in
# seed/launcher.py, where the choice is justified in full. In short: the runner's first untimed eval fires
# after step one and a final eval is forced at the cap, so any cap above one produces the two rows a
# per-step rate needs, and one hundred steps is 6,400 examples at the stub's batch size of 64 -- a small
# fraction of one graded run, far short of convergence, and long enough that warmup does not dominate.
CALIBRATION_MAX_STEPS = 100

with open(sys.argv[1], "r", encoding="utf-8") as handle:
    task = json.load(handle)
run = task["run"]

# The primary run, and one run per perturbation that differs from it in exactly the field its kind names.
# A kind this harness cannot apply by invocation emits no row: its log is then absent, the driver reports
# the perturbation unreached, and that is a truthful record rather than a silently skipped grading unit.
base = {
    "workload": run["workload"],
    "seed": run["rng_seed"],
    "max_steps": run.get("max_global_steps") or "none",
    "ruleset": run["tuning_ruleset"],
    "origin": "agent",
}
rows = [dict(base, name="primary")]

# Additional studies of the primary: the same submitted bytes under a different seed, which the driver
# reduces by median rather than grading as separate units. Held identical to primary_studies() in
# seed/launcher.py, where the choice of an explicit seed list and of the median is justified in full.
# A bundle declaring no replicate_seeds emits exactly the one primary row it always did.
for seed in (run.get("replicate_seeds") or []):
    rows.append(dict(base, name="primary_replicate_%d" % seed, seed=seed))

for entry in task["perturbations"]:
    row = dict(base, name="perturbation_%s" % entry["id"])
    kind = entry["kind"]
    if kind == "truncation":
        row["max_steps"] = entry["max_global_steps"]
    elif kind == "seed":
        row["seed"] = entry["rng_seed"]
    elif kind == "held_out_variant":
        row["workload"] = entry["workload"]
    elif kind == "ruleset":
        row["ruleset"] = entry["tuning_ruleset"]
    else:
        continue
    rows.append(row)

# The seed calibration unit, last. It runs the pristine stub rather than the submitted bytes, on this
# device, inside this same verifier invocation, so the driver can publish a per-step cost ratio whose
# numerator and denominator were measured by the same clock on the same accelerator. It is placed after
# every graded unit because it grades nothing: it feeds one published diagnostic, it enters neither the
# reward nor the pass, and a phase that ends before it runs leaves its log absent, which the driver reports
# as unmeasured rather than as a zero. Nothing graded is delayed or displaced to obtain it.
rows.append(dict(base, name="seed_calibration", max_steps=CALIBRATION_MAX_STEPS, origin="stub"))

for row in rows:
    print(
        "%s %s %s %s %s %s"
        % (row["name"], row["workload"], row["seed"], row["max_steps"], row["ruleset"], row["origin"])
    )
PY
)" || fail_closed "the run specification could not be read, so no graded run could be planned"

run_one() {
  local name="$1" wl="$2" seed="$3" max_steps="$4" ruleset="$5" origin="$6"
  local out="${RESULTS_ROOT}/${name}"
  mkdir -p "${out}"

  # Which bytes this unit runs. Every graded unit runs the submitted bytes; the calibration unit runs the
  # bundle's own stub, which is read-only to the agent phase and is the algorithm the reward anchors on.
  local sub_dir="${SUBMISSION_DIR}"
  if [[ "${origin}" == "stub" ]]; then sub_dir="${STUB_DIR}"; fi
  if [[ ! -f "${sub_dir}/submission.py" ]]; then
    # Only reachable for the calibration unit, since an absent submission fails closed above. Left absent
    # rather than substituted: a calibration that silently ran some other module would publish a ratio
    # against an algorithm nobody named.
    echo "no submission at ${sub_dir}/submission.py, so unit ${name} was not run" \
      >> "${OUTPUT_DIR}/run_${name}.log"
    return 0
  fi

  local extra=()
  if [[ "${max_steps}" != "none" ]]; then extra+=(--max_global_steps="${max_steps}"); fi

  # submission_runner.py refuses an external run without a search space, before any training, which
  # leaves no evaluation log for the verifier to read. The space stays in the solution tree and
  # reaches the runner as a flag rather than as a submission-tree sibling: a search space inside the
  # submitted bytes would fail C-SEARCH-SPACE-INVARIANT under a self-tuning primary.
  if [[ "${ruleset}" == "external" ]]; then
    extra+=(--tuning_search_space="${BUNDLE_ROOT}/solution/tuning_search_space.json" --num_tuning_trials=5)
  fi

  # algoperf.workloads.workloads.convert_filepath_to_module builds a module name with
  # base.replace('/', '.'), so an absolute --submission_path becomes '.submission.submission', a
  # leading-dot relative module that importlib.import_module refuses without a package. Passing a
  # relative path with the submission directory on PYTHONPATH imports the same bytes by a name the
  # harness can resolve.
  (
    cd "${sub_dir}" || exit 1
    PYTHONPATH="${sub_dir}" python3 "${HARNESS_ROOT}/submission_runner.py" \
      --workload="${wl}" \
      --framework="${FRAMEWORK}" \
      --tuning_ruleset="${ruleset}" \
      --submission_path=submission.py \
      --data_dir="${DATA_DIR}" \
      --experiment_dir="${out}" \
      --experiment_name=graded \
      --rng_seed="${seed}" \
      --save_checkpoints=false \
      "${extra[@]}"
  ) >> "${OUTPUT_DIR}/run_${name}.log" 2>&1

  # The runner writes under {experiment_dir}/{experiment_name}/{workload}_{framework}/trial_{n}/.
  # Lift the evaluation log to the flat location the verifier reads. A missing log is left missing.
  # External tuning writes one trial directory per tuning trial, so the first match is an arbitrary
  # trial rather than the one the unit is scored on. select_trial.py resolves that; its empty output
  # falls through to the single-trial search every other unit has always used.
  local produced
  produced="$(python3 "${BUNDLE_ROOT}/tests/select_trial.py" "${out}" "${BUNDLE_ROOT}/tests/verity_task.json" "${name}" 2>/dev/null || true)"
  if [[ -z "${produced}" ]]; then
    produced="$(find "${out}" -name eval_measurements.csv -print -quit || true)"
  fi
  if [[ -n "${produced}" ]]; then
    cp "${produced}" "${out}/eval_measurements.csv"
    # RESULTS_ROOT is declared in task.toml `artifacts`, but that list is collected from the agent
    # container, where nothing writes it: the graded runs happen here, in the separate verifier
    # environment, so the declared path reaches the host as an empty directory. OUTPUT_DIR is the one
    # tree this phase writes that does reach the host, so the log is copied there under its unit name
    # as well. The verifier still reads the RESULTS_ROOT original and grades exactly what it always
    # graded; this second copy is a record for the host and is read by nothing in the reward path.
    cp "${produced}" "${OUTPUT_DIR}/eval_${name}.csv"
  fi
}

while read -r name wl seed max_steps ruleset origin; do
  [[ -z "${name}" ]] && continue
  run_one "${name}" "${wl}" "${seed}" "${max_steps}" "${ruleset}" "${origin}"
done <<< "${RUN_PLAN}"

cd "${BUNDLE_ROOT}/tests" || fail_closed "verifier tree is not where the bundle declares it"

PYTHONPATH="${BUNDLE_ROOT}/tests" python3 -m verity_verifier.main \
  --spec "${BUNDLE_ROOT}/tests/verity_task.json" \
  --submission-dir "${SUBMISSION_DIR}" \
  --submission-file submission.py \
  --harness-root "${HARNESS_ROOT}" \
  --results-root "${RESULTS_ROOT}" \
  --output-dir "${OUTPUT_DIR}" \
  --network-evidence "${NETWORK_EVIDENCE}" \
  --network-mode "${NETWORK_MODE}" \
  --sentinel "${SENTINEL}"
driver_status=$?

if [[ ! -s "${OUTPUT_DIR}/reward.json" ]]; then
  fail_closed "the driver exited ${driver_status} without writing a reward contract"
fi

# The compiled rubric tests read the detail artifact the driver wrote. They assert the implied relation
# only, and they are reached through this entry point rather than run separately.
if [[ -f "${BUNDLE_ROOT}/tests/test_output.py" ]]; then
  VERITY_DETAIL="${OUTPUT_DIR}/verity_detail.json" \
    python3 -m pytest -q "${BUNDLE_ROOT}/tests/test_output.py" \
    > "${OUTPUT_DIR}/rubric_tests.log" 2>&1 || true
fi

exit 0
