"""The verifier driver.

Nine steps, in the order requirements/dataset-spec.md section 9.3 fixes them. The reward contract path is
written on every code path, including every early exit, so a file the agent left behind can never survive
and a zero is always attributable to a named reason rather than to an unwritten file.

The driver is invoked by tests/test.sh inside the verifier environment. It is also invoked by the
authoring feasibility pass over frozen logs, so the graded path and the authoring path are the same code.
"""

import argparse
import os
import sys

from . import parse, redline, reward, rules, runchecks, spec

HARNESS_MEMBERS = ("algoperf", "submission_runner.py")

# The results subdirectory tests/test.sh writes the seed calibration run to, and the same name
# seed/launcher.py gives that unit. It holds a short step-capped run of the bundle's own stub, performed on
# the same device in the same verifier phase as the graded runs, and it backs `compute_efficiency` alone.
SEED_CALIBRATION_DIR = "seed_calibration"

# Packages the harness itself pins. An added dependency that re-pins one of these is a red-line crossing.
PINNED_PACKAGES = frozenset(
    {
        "absl-py",
        "numpy",
        "pandas",
        "tensorflow",
        "tensorflow-datasets",
        "clu",
        "matplotlib",
        "tabulate",
        "wandb",
        "torch",
        "torchvision",
        "jax",
        "jaxlib",
        "flax",
        "optax",
        "algoperf",
    }
)


def _load_curve(path, metric_column):
    if not os.path.exists(path):
        return parse.MalformedLog("evaluation log is absent at %s" % path)
    try:
        return parse.read_curve(path, metric_column)
    except parse.MalformedLog as error:
        return error


# The axis the reward grades. The name is the run specification's existing vocabulary and the schema's;
# the column it resolves to is `accumulated_submission_time` (`parse.budget_position`), which is what
# `submission_runner.py` accumulates and terminates on and what the upstream scorer reads. A budget
# declared in any other unit cannot be graded here, and saying so loudly beats grading the wrong axis.
TIME_BUDGET_KIND = "wall_clock_sec"

# A perturbation of this kind is the same submitted bytes under a different seed. That is a repeat
# measurement of the primary rather than a generalisation test, so it joins the primary's studies and
# is reduced by median with them instead of being graded as a unit of its own.
SEED_PERTURBATION_KIND = "seed"


def _graded_budget(unit, label):
    """The budget a unit is graded against, in seconds of accumulated submission time."""
    budget = unit["budget"]
    if budget["kind"] != TIME_BUDGET_KIND:
        raise ValueError(
            "%s declares budget kind %r, and the reward grades %r"
            % (label, budget["kind"], TIME_BUDGET_KIND)
        )
    return float(budget["value"])


def _study_rows(curve):
    """One study's eval rows, or an empty list when its log could not be read.

    An unreadable or absent log is charged at the budget by `expected_crossing_time`, which is the
    same treatment a run that never crossed receives. That is deliberate: neither reached the target,
    and at this point nothing else distinguishes them. A log the parser rejected outright has already
    voided the rollout through `validity` when it is the primary's.
    """
    return [] if isinstance(curve, parse.MalformedLog) else curve


def _budget_profile(task, objective, primary_curve, replicate_curves, perturbations, entry_curves, detail):
    """The per-unit budget fractions the reward averages, and how many units were graded.

    The unit set is built from the declared perturbations rather than fixed here, because the corpus
    runs bundles with one, two and five of them. The primary and its replicates are one unit however
    many studies they carry; every perturbation that is not a seed replicate is a unit of its own.
    """
    studies = [_study_rows(primary_curve)] + [_study_rows(c) for c in replicate_curves]
    seeded = [e for e in perturbations if e["kind"] == SEED_PERTURBATION_KIND]
    for entry in seeded:
        studies.append(_study_rows(entry_curves.get(entry["id"])))

    ceiling = _graded_budget(objective, "the primary objective")
    fractions = [
        reward.budget_fraction(
            reward.unit_time(studies, objective["threshold"], objective["direction"], ceiling), ceiling
        )
    ]
    detail["steps"].append("primary unit over %d stud%s" % (len(studies), "y" if len(studies) == 1 else "ies"))

    for slot, entry in enumerate(perturbations, start=1):
        if entry["kind"] == SEED_PERTURBATION_KIND:
            continue
        # A unit that is not measured on the graded axis is not graded on the profile. The case that
        # forces this is truncation: `spec` refuses a wall-clock budget on a truncated run, because
        # such a run is bounded by its step ceiling and asking how much of a *time* budget it left
        # unspent grades an incoherent quantity. Excluding it is also what the measurement asks for --
        # graded against a 90 s budget the truncated unit crossed early on nearly every recorded turn
        # and carried almost no signal, widening the largest gap in the scale from 0.093 to 0.218.
        #
        # It keeps its own budget and its own run checks, so it still decides `conformance_fraction`
        # and `task_pass`. Only the continuous scalar declines to average it, and the exclusion is
        # recorded rather than silent.
        if entry["budget"]["kind"] != TIME_BUDGET_KIND:
            detail["notes"].append(
                "perturbation slot %d (%s) is budgeted in %r and is graded by its run checks rather "
                "than by the profile" % (slot, entry["kind"], entry["budget"]["kind"])
            )
            continue
        entry_ceiling = _graded_budget(entry, "perturbation slot %d (%s)" % (slot, entry["kind"]))
        fractions.append(
            reward.budget_fraction(
                reward.unit_time(
                    [_study_rows(entry_curves.get(entry["id"]))],
                    entry["threshold"],
                    entry["direction"],
                    entry_ceiling,
                ),
                entry_ceiling,
            )
        )
    return fractions, len(fractions)


def _resolve_batch_size(submission_dir, submission_file, workload_name):
    """Resolve the declared batch size without importing the submission.

    The train_examples axis multiplies the step count by the batch size the submission declares, so the
    verifier has to read that value. It is read from the returned constant of get_batch_size by static
    analysis rather than by executing the module, because executing agent-authored code inside the
    verifier is the exposure this design refuses to open. A submission whose get_batch_size does not
    reduce to a single constant is reported rather than guessed at.

    A return of a module level constant reduces to a single value as surely as a literal does, and
    naming the batch size is ordinary style rather than evasion: the bundle's own reference submission
    returns `_BATCH_SIZE`. Those names are folded here from module level integer assignments, which
    keeps the resolution static. Nothing else is folded. An expression, a call, or a name bound to
    anything other than a module level integer is still reported rather than guessed at, so the
    property this check defends, that the declared batch size is knowable without execution, is
    unchanged.
    """
    import ast

    path = os.path.join(submission_dir, submission_file)
    with open(path, "r", encoding="utf-8") as handle:
        tree = ast.parse(handle.read(), filename=path)

    constants = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant):
            if isinstance(node.value.value, int) and not isinstance(node.value.value, bool):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        constants[target.id] = node.value.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, int):
                if not isinstance(node.value.value, bool):
                    constants[node.target.id] = node.value.value

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "get_batch_size":
            returns = [n for n in ast.walk(node) if isinstance(n, ast.Return)]
            values = set()
            for statement in returns:
                if isinstance(statement.value, ast.Constant) and isinstance(statement.value.value, int):
                    values.add(statement.value.value)
                elif isinstance(statement.value, ast.Name) and statement.value.id in constants:
                    values.add(constants[statement.value.id])
                else:
                    return None, "get_batch_size does not return a single integer constant"
            if len(values) == 1:
                return values.pop(), None
            return None, "get_batch_size returns %d distinct constants, so the declared batch size is not a single value" % len(values)
    return None, "get_batch_size is not defined"


def _compute_efficiency(calibration_curve, primary_curve):
    """How cheap a step of the submitted algorithm is against a step of the seed, on one device.

    Returns the pair (efficiency, reason). The efficiency is

        clip(seed per-step cost / graded per-step cost, 0, 1)

    so 1.0 says the submission costs no more per step than the algorithm it was handed, and 0.33 says it
    costs three times as much. It is clipped above rather than reported unbounded because the quantity is
    published to a refinement loop as a diagnostic to hold at ceiling, not as a lever to climb: a
    submission that made its steps ten times cheaper than the seed's and converged nowhere would otherwise
    read as ten times better on this axis than one that matched the seed exactly.

    This exists beside `per_step_cost_ratio` rather than in place of it, and the two answer different
    questions. That ratio divides a cost measured here by `seed_per_step_cost_sec`, a constant pinned in
    the task specification, which is what the C-PER-STEP-COST-CEILING red line has to compare against: a
    red line must be stated in the bundle rather than measured at grading time, or the bar moves with the
    machine and a rollout stops being reproducible from its recorded bytes. The price of that pinning is
    that the numerator and the denominator come from different accelerators, so the published number
    carries the hardware ratio as well as the algorithmic one. `compute_efficiency` pays the opposite
    price: both sides are measured in this invocation, on this device, by the same clock, so the hardware
    term divides out and nothing about it is pinned or reproducible across revisions of the seed.

    Absence is reported as None, never as 0.0, and the caller carries it through to a null in the reward
    contract. A calibration run that did not happen, produced an unreadable log, or produced a curve too
    short to support a quotient is a measurement nobody took. Zero is a measurement, and it would read as
    a submission of unbounded per-step cost, which is the most damning value on the scale.
    """
    if isinstance(calibration_curve, parse.MalformedLog):
        return None, "the seed calibration log is unreadable: %s" % calibration_curve
    if isinstance(primary_curve, parse.MalformedLog):
        return None, "there is no primary curve to compare the seed calibration against"

    seed_cost = redline.per_step_cost(calibration_curve)
    graded_cost = redline.per_step_cost(primary_curve)
    if seed_cost is None:
        return None, "the seed calibration curve cannot support a per-step cost"
    if graded_cost is None:
        return None, "the primary curve cannot support a per-step cost"
    if seed_cost <= 0.0 or graded_cost <= 0.0:
        # A non-positive per-step cost is a clock that did not advance across the measured span rather
        # than a free step, and dividing by it would publish either an infinity or a sign flip.
        return None, "a measured per-step cost is not positive, so the quotient is meaningless"

    return max(0.0, min(1.0, seed_cost / graded_cost)), None


def _rule_conformance(results):
    """The fraction of the declared rule checks the submitted bytes held.

    Ranges over spec.RULE_IDS alone. The red lines are excluded because they void a rollout rather than
    score it, and the run checks are excluded because closure and the perturbation term already carry
    what they measure, so counting them here would grade the same outcome twice.
    """
    rule_ids = set(spec.RULE_IDS)
    ran = [r for r in results if r.check_id in rule_ids]
    if not ran:
        return 0.0
    return sum(1 for r in ran if r.passed) / float(len(ran))


def run(args):
    detail = {"steps": [], "checks": [], "notes": []}
    results = []
    # Per-perturbation rows are held apart from `results` rather than extended into it. `results` is
    # graded: `_rule_conformance` reads it and `red_line_crossed` scans it, so a perturbation's
    # C-LOG-WELL-FORMED row entering that list would let a malformed perturbation log void a rollout
    # that only the primary run can void today, and five more C-TARGET-REACHED rows would collide
    # with the primary's under any consumer that keys on check id.
    perturbation_detail = []
    red_line_crossed = False
    zero_reason = reward.ZERO_REASON["above_zero"]

    def emit(payload_overrides, detail_note=None):
        if detail_note:
            detail["notes"].append(detail_note)
        detail["checks"] = [r.as_dict() for r in results] + perturbation_detail
        payload = {
            "reward": 0.0,
            "validity": 0.0,
            "rule_conformance": 0.0,
            "conformance_fraction": 0.0,
            "closure": 0.0,
            "task_pass": 0.0,
            "primary_target_reached": 0.0,
            "qualifying_budget": None,
            "per_step_cost_ratio": None,
            "compute_efficiency": None,
            "perturbations_declared": 0.0,
            "perturbations_reached": 0.0,
            "red_line_crossed": 0.0,
            "zero_reason_code": float(reward.ZERO_REASON["infrastructure"]),
            "wall_clock_sec": None,
        }
        payload.update(payload_overrides)
        reward.write(args.output_dir, payload)
        reward.write_detail(args.output_dir, detail)
        return payload

    # Step zero: the specification. A specification the verifier cannot interpret stops the pass.
    try:
        task = spec.load(args.spec)
    except (OSError, spec.SpecError) as error:
        emit({"zero_reason_code": float(reward.ZERO_REASON["infrastructure"])}, "specification unreadable: %s" % error)
        return 1

    objective = task["objective"]
    metric_column = objective["metric"]
    anchors = objective["anchors"]
    perturbations = task["perturbations"]
    surface = task["submission_surface"]

    # Step one: re-hash the harness tree.
    harness_check = redline.c_harness_immutable(
        args.harness_root, HARNESS_MEMBERS, task["harness"].get("tree_digest")
    )
    results.append(harness_check)
    detail["steps"].append("harness immutability")

    # The two environment red lines.
    network_params = spec.check_params(task, "C-NETWORK-POLICY-HONOURED")
    results.append(
        redline.c_network_policy_honoured(
            args.network_evidence, network_params.get("network_mode"), args.network_mode
        )
    )
    results.append(redline.c_no_reward_write(os.path.join(args.output_dir, "reward.json"), args.sentinel))
    detail["steps"].append("environment red lines")

    # Step two: the static rule checks over the submitted bytes.
    try:
        registry_keys = rules.load_registry_keys(
            os.path.join(args.harness_root, "algoperf", "workloads", "workloads.py")
        )
    except (OSError, ValueError) as error:
        emit({"zero_reason_code": float(reward.ZERO_REASON["infrastructure"])}, "registry keys unresolvable: %s" % error)
        return 1

    try:
        static = rules.run_all(
            args.submission_dir,
            args.submission_file,
            registry_keys,
            surface["search_space_required"],
            surface["allow_requirements_txt"],
            PINNED_PACKAGES,
        )
    except SyntaxError as error:
        results.append(rules.Result("C-API-SURFACE", False, "the submission does not parse: %s" % error))
        static = []
    results.extend(static)
    detail["steps"].append("static rule checks")

    red_line_ids = set(spec.RED_LINE_IDS)
    red_line_crossed = any((not r.passed) and r.check_id in red_line_ids for r in results)
    rule_failed = any((not r.passed) and r.check_id in set(spec.RULE_IDS) for r in results)
    rule_conformance = _rule_conformance(results)

    # Steps three through five: the runs and the parsed curves. The runs themselves are performed by the
    # launcher before the verifier is reached; this driver reads what they produced.
    primary_log = os.path.join(args.results_root, "primary", "eval_measurements.csv")
    primary_curve = _load_curve(primary_log, metric_column)

    # Additional studies of the primary, one per declared replicate seed. Their unit ids are held
    # identical to primary_studies() in seed/launcher.py and to the run plan test.sh emits. They carry
    # no run checks: a replicate is graded by contributing its crossing time to the primary unit's
    # median, and a bundle declaring none is graded exactly as it was before replicates existed.
    replicate_curves = [
        _load_curve(
            os.path.join(args.results_root, "primary_replicate_%d" % seed, "eval_measurements.csv"),
            metric_column,
        )
        for seed in (task["run"].get("replicate_seeds") or [])
    ]

    # This re-parses a submission whose SyntaxError C-API-SURFACE already caught, so unguarded it killed
    # the driver after the rule pass had survived it, and a driver that dies writes no reward at all.
    try:
        batch_size, batch_error = _resolve_batch_size(
            args.submission_dir, args.submission_file, task["run"]["workload"]
        )
    except (SyntaxError, ValueError, OSError) as error:
        batch_size, batch_error = None, "%s" % error
    if batch_error and objective["budget"]["kind"] == "train_examples":
        detail["notes"].append("batch size unresolved: %s" % batch_error)
        # rule_check rather than infrastructure, because the submission missed the declared surface and
        # grading that as broken infrastructure misreports whose defect it is.
        emit(
            {"zero_reason_code": float(reward.ZERO_REASON["rule_check"])},
            "the declared batch size does not reduce to a single constant, so the train_examples axis is not computable",
        )
        return 1

    # The comparator lives in the conformance params because the run-specification schema admits no
    # comparator key on a graded unit. Resolve it from the declared check and attach it here, so the
    # evaluation reads a value the specification declared rather than one this module chose.
    primary_unit = dict(objective)
    primary_unit["comparator"] = spec.comparator_for(task, "C-TARGET-REACHED")
    primary_results, primary_row = runchecks.evaluate(primary_curve, primary_unit, batch_size, "primary")
    results.extend(primary_results)
    detail["steps"].append("primary run checks")

    # Step four: one run per perturbation.
    reached = 0
    # Kept for the reward, which grades each perturbation as its own unit rather than conjuncting over
    # them. Keyed by id and never emitted: the ids stay private, as they always have.
    entry_curves = {}
    perturbation_comparator = spec.comparator_for(task, "C-PERTURBATION-REACHED")
    for slot, entry in enumerate(perturbations, start=1):
        path = os.path.join(args.results_root, "perturbation_%s" % entry["id"], "eval_measurements.csv")
        curve = _load_curve(path, entry["metric"])
        entry_curves[entry["id"]] = curve
        entry_unit = dict(entry)
        entry_unit["comparator"] = perturbation_comparator
        # The label reaches the reason text, and the reason text reaches the refinement loop. It
        # carries the slot and the already-published kind and never `entry["id"]`: AlgoPerf withholds
        # its held-out variant selection because a submitter who knows which variants run can tune
        # against them, so naming one here would convert the generalisation test into a targeted-fix
        # loop. The relabel is done at the point of emission because a downstream filter is something
        # a later caller can forget to apply.
        entry_results, entry_row = runchecks.evaluate(
            curve, entry_unit, batch_size, "perturbation slot %d (%s)" % (slot, entry["kind"])
        )
        entry_passed = entry_row is not None and all(r.passed for r in entry_results)
        for result in entry_results:
            row = result.as_dict()
            row["slot"] = slot
            row["kind"] = entry["kind"]
            row["unit_reached"] = entry_passed
            perturbation_detail.append(row)
        if entry_passed:
            reached += 1
    perturbation_check = runchecks.perturbation_result(reached, len(perturbations))
    results.append(perturbation_check)
    detail["steps"].append("perturbation run checks")

    step_params = spec.check_params(task, "C-PER-STEP-COST-CEILING")
    per_step_ratio = None
    if isinstance(primary_curve, parse.MalformedLog):
        results.append(
            rules.Result(
                "C-PER-STEP-COST-CEILING",
                False,
                "no curve to read, so per-step cost is unmeasurable rather than clear",
            )
        )
    else:
        step_result, per_step_ratio = redline.c_per_step_cost_ceiling(
            primary_curve,
            step_params.get("seed_per_step_cost_sec"),
            step_params.get("per_step_cost_ceiling_ratio", 3.0),
        )
        results.append(step_result)
    detail["steps"].append("per-step cost ceiling")

    # Step six and a half: the device-local companion to the ratio above. The calibration curve is read
    # through the same loader and the same declared metric column as the primary curve, because it is the
    # same workload run for fewer steps and a log this driver cannot read is a log this driver cannot read
    # whichever unit produced it. No check is appended: `compute_efficiency` is published and never graded,
    # so a calibration run that failed costs the submission nothing.
    calibration_curve = _load_curve(
        os.path.join(args.results_root, SEED_CALIBRATION_DIR, "eval_measurements.csv"), metric_column
    )
    compute_efficiency, efficiency_reason = _compute_efficiency(calibration_curve, primary_curve)
    if efficiency_reason:
        detail["notes"].append("compute efficiency unmeasured: %s" % efficiency_reason)
    detail["steps"].append("seed calibration compute efficiency")

    log_malformed = isinstance(primary_curve, parse.MalformedLog)

    # Recomputed rather than carried, because the per-step red line appends after the first pass over the
    # results. A red-line set sampled before every red line has run is the defect this line exists to avoid.
    red_line_crossed = any((not r.passed) and r.check_id in red_line_ids for r in results)

    # Step seven: closure from the primary curve and the anchors.
    conformance_fraction = (reached / len(perturbations)) if perturbations else 0.0

    # A failed rule check no longer appears here. It is priced by `rule_conformance` in the product
    # instead, so a submission that holds six of seven rules outscores one that holds two. `validity`
    # keeps only the outcomes that void a rollout rather than grade it: a crossed red line and a log the
    # parser could not read. `task_pass` names `rule_conformance == 1` explicitly, so the conjunction is
    # unchanged by this softening.
    validity = 0.0 if (red_line_crossed or log_malformed) else 1.0

    best = None
    closure = 0.0
    qualifying_position = None
    graded_units = 0
    if not log_malformed:
        best = parse.best_metric(primary_curve, objective["direction"])
        if primary_row is not None:
            qualifying_position = parse.budget_position(primary_row, objective["budget"]["kind"], batch_size)
        try:
            fractions, graded_units = _budget_profile(
                task, objective, primary_curve, replicate_curves, perturbations, entry_curves, detail
            )
            closure = reward.aggregate(fractions)
        except ValueError as error:
            detail["notes"].append("budget profile uncomputable: %s" % error)
            closure = 0.0
            validity = 0.0

    # Step eight: compose both quantities. `closure` carries the budget-fraction profile -- the mean
    # over graded units of how much of each unit's declared budget was left unspent at its crossing.
    # The key name is the reward contract's and predates the profile; the quantity it now carries is
    # the one `reward.aggregate` returns.
    scalar = reward.compose(validity, rule_conformance, closure)
    passed = reward.task_pass(validity, rule_conformance, conformance_fraction, reached == len(perturbations))

    if red_line_crossed:
        zero_reason = reward.ZERO_REASON["red_line"]
    elif rule_failed and scalar <= 0.0:
        zero_reason = reward.ZERO_REASON["rule_check"]
    elif log_malformed:
        zero_reason = reward.ZERO_REASON["malformed_log"]
    elif scalar <= 0.0:
        zero_reason = reward.ZERO_REASON["no_improvement"]
    else:
        zero_reason = reward.ZERO_REASON["above_zero"]

    wall_clock = None
    if not log_malformed and primary_curve:
        wall_clock = primary_curve[-1]["accumulated_submission_time"]

    # Step nine: write the reward contract and the sibling detail artifact.
    emit(
        {
            "reward": scalar,
            "validity": validity,
            "rule_conformance": rule_conformance,
            "conformance_fraction": conformance_fraction,
            "closure": closure,
            "task_pass": passed,
            "primary_target_reached": 1.0 if primary_row is not None else 0.0,
            "qualifying_budget": qualifying_position,
            "per_step_cost_ratio": per_step_ratio,
            "compute_efficiency": compute_efficiency,
            "perturbations_declared": float(len(perturbations)),
            "perturbations_reached": float(reached),
            "red_line_crossed": 1.0 if red_line_crossed else 0.0,
            "zero_reason_code": float(zero_reason),
            "wall_clock_sec": wall_clock,
        }
    )
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="verity_verifier", description="Grade one Verity rollout.")
    parser.add_argument("--spec", required=True, help="path to tests/verity_task.json")
    parser.add_argument("--submission-dir", required=True, help="directory holding the submitted bytes")
    parser.add_argument("--submission-file", default="submission.py")
    parser.add_argument("--harness-root", required=True, help="root of the pinned AlgoPerf tree")
    parser.add_argument("--results-root", required=True, help="root holding primary/ and perturbation_<id>/")
    parser.add_argument("--output-dir", required=True, help="verifier output directory, where reward.json is written")
    parser.add_argument("--network-evidence", required=True, help="path to the environment network probe record")
    parser.add_argument("--network-mode", required=True, help="the declared Harbor network mode observed at runtime")
    parser.add_argument("--sentinel", required=True, help="path to the verifier sentinel written before grading")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
