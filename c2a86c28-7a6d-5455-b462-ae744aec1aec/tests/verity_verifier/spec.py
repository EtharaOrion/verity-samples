"""Run-specification loader.

Reads tests/verity_task.json and exposes it as plain dicts. Nothing about grading lives in the
verifier that is not first declared in that file, so this module is the only place the specification is
interpreted.

Dependency-free by design: the package runs inside the verifier image and inside a bare authoring
checkout without the bundle pinning a parser it would then have to trust.
"""

import json
import os

REQUIRED_TOP_LEVEL = (
    "task_id",
    "meta",
    "harness",
    "run",
    "objective",
    "perturbations",
    "conformance",
    "submission_surface",
    "refinement",
    "upstream_provenance",
)

BUDGET_KINDS = ("wall_clock_sec", "train_examples", "global_steps", "eval_index")

COMPARATORS = ("strictly_greater", "strictly_less", "at_least", "at_most")

RED_LINE_IDS = (
    "C-HARNESS-IMMUTABLE",
    "C-NETWORK-POLICY-HONOURED",
    "C-PER-STEP-COST-CEILING",
    "C-NO-REWARD-WRITE",
    "C-NO-CREDENTIAL",
    "C-DEPS-UNCHANGED",
)

RULE_IDS = (
    "C-API-SURFACE",
    "C-NO-WORKLOAD-DISPATCH",
    "C-NO-SHAPE-FINGERPRINT",
    "C-SEARCH-SPACE-INVARIANT",
    "C-NO-ENV-MUTATION",
    "C-NO-KERNEL",
    "C-NO-BACKGROUND-WORK",
)

RUN_IDS = (
    "C-LOG-WELL-FORMED",
    "C-TARGET-REACHED",
    "C-BUDGET-RESPECTED",
    "C-PERTURBATION-REACHED",
    "C-NO-LATCH-CARRYOVER",
)

CLOSED_VOCABULARY = RED_LINE_IDS + RULE_IDS + RUN_IDS


class SpecError(ValueError):
    """Raised when the run specification cannot be interpreted. Never swallowed."""


def load(path):
    with open(path, "rb") as handle:
        spec = json.loads(handle.read().decode("utf-8"))
    validate(spec)
    return spec


def validate(spec):
    """Structural obligations a JSON Schema cannot express.

    Raises SpecError rather than returning a boolean, because a specification the verifier cannot
    interpret must stop the pass instead of producing a score.
    """
    missing = [key for key in REQUIRED_TOP_LEVEL if key not in spec]
    if missing:
        raise SpecError("missing required top-level keys: %s" % ", ".join(sorted(missing)))

    run = spec["run"]
    if run.get("rng_seed") is None:
        raise SpecError("run.rng_seed must be set explicitly, or the runner draws from the OS")
    if "skip_evals" in (run.get("extra_flags") or {}):
        raise SpecError("--skip_evals removes the only path by which a target can be observed")

    ruleset = run.get("tuning_ruleset")
    if ruleset not in ("external", "self"):
        raise SpecError("run.tuning_ruleset must be external or self")
    trials = run.get("num_tuning_trials")
    if ruleset == "external" and not trials:
        raise SpecError("the external ruleset requires num_tuning_trials")
    if ruleset == "self" and trials:
        raise SpecError("the self-tuning ruleset rejects num_tuning_trials")

    truncated = run.get("max_global_steps") is not None
    objective = spec["objective"]
    _validate_graded_unit(objective, truncated, "objective")

    if objective.get("budget", {}).get("kind") == "global_steps" and not run.get("batch_size_pinned"):
        raise SpecError("the global_steps axis requires run.batch_size_pinned, because a step is not a fixed unit otherwise")

    perturbations = spec["perturbations"]
    if not perturbations:
        raise SpecError("a task with no perturbation grades a single run")
    seen = set()
    for entry in perturbations:
        if entry["id"] in seen:
            raise SpecError("duplicate perturbation id: %s" % entry["id"])
        seen.add(entry["id"])
        entry_truncated = truncated or entry.get("kind") == "truncation"
        _validate_graded_unit(entry, entry_truncated, "perturbation %s" % entry["id"])

    declared = [check["id"] for check in spec["conformance"]]
    unknown = [cid for cid in declared if cid not in CLOSED_VOCABULARY]
    if unknown:
        raise SpecError("conformance identifiers outside the closed vocabulary: %s" % ", ".join(unknown))
    if len(set(declared)) != len(declared):
        raise SpecError("duplicate conformance identifier")

    # The comparator is declared in the conformance params rather than on the graded unit, because
    # dataset.schema.json fixes the objective and perturbation objects with additionalProperties false and
    # admits no comparator key there. It is still a declared parameter of a declared check, so the verifier
    # holds no private check: it is read from the run specification and never defaulted.
    for check_id in ("C-TARGET-REACHED", "C-PERTURBATION-REACHED"):
        if check_id not in declared:
            continue
        comparator = check_params(spec, check_id).get("comparator")
        if comparator not in COMPARATORS:
            raise SpecError(
                "%s must declare a comparator from %s in its params" % (check_id, ", ".join(sorted(COMPARATORS)))
            )

    anchors = objective.get("anchors")
    if not anchors:
        raise SpecError("objective.anchors is required, or the task cannot emit a continuous reward")
    if anchors.get("anchor_class") not in ("measured_public", "measured_baseline", "authored"):
        raise SpecError("objective.anchors.anchor_class is outside its closed set")

    image = spec["harness"].get("image")
    if image == "unbuilt":
        raise SpecError(
            "harness.image is declared unbuilt, so no rollout can be graded against an identified image. "
            "This is the delivery-image-unbuilt gap, and it fails closed rather than grading in an "
            "environment the bundle cannot name."
        )
    if image is not None and "@sha256:" not in image:
        raise SpecError("harness.image must be referenced by digest, never by tag")

    return True


def _validate_graded_unit(unit, truncated, label):
    budget = unit.get("budget") or {}
    kind = budget.get("kind")
    if kind not in BUDGET_KINDS:
        raise SpecError("%s: budget.kind outside its closed set" % label)
    if unit.get("direction") not in ("min", "max"):
        raise SpecError("%s: direction must be stated explicitly as min or max" % label)
    provenance = unit.get("threshold_provenance")
    if provenance not in ("workload_class", "authored"):
        raise SpecError("%s: threshold_provenance outside its closed set" % label)
    if truncated and provenance == "workload_class":
        raise SpecError("%s: a truncated run measured against the published target grades an impossibility" % label)
    if truncated and kind == "wall_clock_sec":
        raise SpecError("%s: a truncated run may not use a wall-clock budget" % label)


def declared_ids(spec, klass):
    return [c["id"] for c in spec["conformance"] if c.get("class") == klass]


def comparator_for(spec, check_id):
    """The comparator a declared check binds. Never defaulted: an absent one is a specification error."""
    value = check_params(spec, check_id).get("comparator")
    if value not in COMPARATORS:
        raise SpecError("%s declares no valid comparator" % check_id)
    return value


def check_params(spec, check_id):
    for check in spec["conformance"]:
        if check["id"] == check_id:
            return check.get("params") or {}
    return {}


def resolve(path, root):
    """Resolve a bundle-relative path against a root, refusing escapes."""
    candidate = os.path.normpath(os.path.join(root, path))
    if not candidate.startswith(os.path.normpath(root)):
        raise SpecError("path escapes the bundle root: %s" % path)
    return candidate
