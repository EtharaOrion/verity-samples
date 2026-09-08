"""The reward contract.

Two graded quantities come out of one run and neither is computed from the other. task_pass is the
conjunction that difficulty measurement consumes. reward is the bounded continuous scalar a refinement
loop consumes. Both read the same parsed rows the run checks read.

The scalar is the **Budget-Fraction Profile**, and it is AlgoPerf's own per-workload score with the
reference anchored to the declared budget. AlgoPerf grades time-to-target: it forms a performance
ratio `r = t / t_ref` and awards `max(0, r_max - r) / (r_max - 1)`, then averages over workloads
(`scoring/performance_profile.py`, and Dahl et al. arXiv:2306.07179 Eq. 1-3). Substituting the
reference `t_ref = C / r_max` collapses that ramp to

    [r_max / (r_max - 1)] * max(0, 1 - t / C)

whose zero sits at `t = C` for *every* `r_max`; the parameter only sets the width of a saturated
plateau at the top, where credit clips at one. Taking `r_max` to infinity removes the plateau and
leaves `B = 1 - t/C`, which is what this module computes. On the recorded ep-sbx4 corpus the
published `r_max = 4` put 23 of 112 unit times inside that plateau, where wall time could be inflated
1.87x at no cost to the score; at `r_max` infinite none saturate.

Anchoring to the budget rather than to a cohort minimum is the one authored choice here, and it is
made because a pool-relative reference is not computable online, is not comparable across episodes,
and lets one lucky attempt rescale every other. AlgoPerf's own implementation admits a fixed
reference submission in place of the pool minimum; the budget is a fixed reference this bundle
already owns and declares.

`t` is `accumulated_submission_time` at the first crossing, which is the column AlgoPerf's own scorer
reads, and it is the axis the harness enforces: the runner terminates on it. The graded budget is
whatever the unit declares, so nothing here hardcodes a ceiling.

Two departures from upstream are deliberate and are named so they are not mistaken for transcription:

  * the crossing is softened by the measured validation noise rather than tested as a hard threshold,
    for which see `expected_crossing_time`;
  * `validity` and `rule_conformance` gate the scalar to zero. Upstream has no red lines.

The formulas are fixed in requirements/thresholds.md sections 5.2 and 5.3 and are reproduced here as
code, never re-derived.
"""

import json
import math
import os

# The standard deviation of a validation-accuracy reading, in metric units. Measured from the paired
# primary and seed-shift runs of ep-sbx4: the same submitted bytes under two seeds differ by a mean
# absolute 0.001152, which for two independent normals implies a per-reading sigma of 8.15e-4. The
# value is carried at 8.5e-4, the round figure just above it.
#
# It exists because the target sits inside the measurement. Across 168 recorded runs the best
# validation accuracy ever seen was 0.9770 against a 0.97 threshold, and 35 of 140 (turn, study) pairs
# ended within one sigma of the target. A hard comparison there is a coin flip that the reward would
# otherwise report as a fact, and two validation images decided full conformance on two ep-sbx4 turns.
METRIC_SIGMA = 8.5e-4

ZERO_REASON = {
    "above_zero": 0,
    "red_line": 1,
    "rule_check": 2,
    "malformed_log": 3,
    "no_improvement": 4,
    "infrastructure": 5,
}


def _clip(value, low, high):
    return max(low, min(high, value))


def _normal_cdf(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def crossing_probability(best_so_far, threshold, direction, sigma=METRIC_SIGMA):
    """The probability that a reading of `best_so_far` reflects a metric genuinely past `threshold`.

    Direction-agnostic: the sign of the standardised distance flips with the direction the metric
    improves in, so a minimising objective reads the same way a maximising one does.

    `sigma <= 0` recovers the hard comparison exactly, which is what makes the softening auditable:
    the unsoftened AlgoPerf crossing is this function at the limit rather than a different code path.
    """
    if best_so_far is None or math.isnan(best_so_far):
        return 0.0
    distance = (best_so_far - threshold) if direction == "max" else (threshold - best_so_far)
    if sigma <= 0.0:
        return 1.0 if distance > 0.0 else 0.0
    return _normal_cdf(distance / sigma)


def expected_crossing_time(rows, threshold, direction, ceiling, sigma=METRIC_SIGMA):
    """The budget position at which one study crossed, in expectation over the reading noise.

    Walks the curve accumulating the probability mass that has crossed by each row and charges each
    increment at that row's position, then charges whatever mass is left over:

        T = sum_i (W_i - W_{i-1}) * min(ast_i, C)  +  (1 - W_last) * R

    where the residual position `R` is the ceiling for a run that never crossed, and the observed
    crossing position for a run that did.

    That split is the whole of it, and it matters. Charging an unresolved run at the budget is the
    organisers' own convention for a miss, and at this anchor it is numerically identical to
    AlgoPerf's zero credit: `t = C` gives `B = 0`. But it answers the question "what if this run never
    crossed", and that question is already settled for a run whose best reading passes the threshold
    on the unsoftened test. For such a run the leftover mass is uncertainty about *when* it crossed,
    not *whether*, and the honest bound on when is the row where it was seen to happen.

    Charging that residual at the ceiling instead is a measured defect, not a hypothetical. On
    ep-sbx4 it overcharged crossed studies by 4.53 s on average and 28.55 s at the extreme: t18 held
    the fastest raw crossing in the entire episode at 11.16 s, ended its curve one eval row later at
    0.9704 against a 0.970 target, kept 31.9% of its mass unresolved, and was charged 39.70 s for it.
    A curve that crosses on its last row is the ordinary case at this eval cadence -- the grid fires
    every 10 s against runs of a few tens of seconds -- so the penalty fell hardest on exactly the
    fast submissions the reward exists to reward.

    `W` is taken over the *running best* rather than the row's own reading, so the sequence cannot
    fall back and the increments cannot go negative. A run whose accuracy dips after crossing keeps
    the credit it earned.

    Returns the ceiling for an empty or unreadable curve, which is the same treatment a run that
    never crossed receives, because neither reached the target and no other quantity distinguishes
    them at this point.
    """
    if ceiling <= 0:
        raise ValueError("the graded budget must be positive to place a run on the scale")
    if not rows:
        return float(ceiling)

    best = None
    previous = 0.0
    total = 0.0
    # The position at which the unsoftened test first passes. `None` means this study never crossed
    # on the hard reading, and its residual mass is charged at the budget.
    resolved_at = None
    for row in rows:
        value = row.get("metric")
        position = row.get("accumulated_submission_time")
        if value is None or math.isnan(value) or position is None:
            continue
        if best is None:
            best = value
        else:
            best = max(best, value) if direction == "max" else min(best, value)
        capped = min(float(position), float(ceiling))
        if resolved_at is None and crossing_probability(best, threshold, direction, 0.0) > 0.0:
            resolved_at = capped
        reached = crossing_probability(best, threshold, direction, sigma)
        if reached <= previous:
            continue
        total += (reached - previous) * capped
        previous = reached

    if resolved_at is None:
        # Never crossed on the unsoftened test, so the whole study is charged the budget and nothing
        # it accumulated on the way is credited. Returning `total + (1 - W_last) * C` instead would
        # credit the mass a near-miss accrued, and the softening makes that mass strictly positive for
        # any curve that got close: measured against this module at C = 90 and a 0.97 target, a study
        # parked at exactly 0.9700 -- which fails a strict `>` and is exactly representable -- scored
        # 0.4833 of a unit, beating an honest crossing at 60 s on 0.3333. Approaching the threshold and
        # stopping paid better than reaching it. The cap was half a unit, because `crossing_probability`
        # at `best == thr` is `Phi(0) = 0.5`.
        return float(ceiling)
    return total + (1.0 - previous) * resolved_at


def _median(values):
    ordered = sorted(values)
    count = len(ordered)
    if not count:
        raise ValueError("a unit needs at least one study to be graded")
    middle = count // 2
    if count % 2:
        return ordered[middle]
    return 0.5 * (ordered[middle - 1] + ordered[middle])


def unit_time(studies, threshold, direction, ceiling, sigma=METRIC_SIGMA):
    """One unit's graded time: the median over its studies, as upstream takes it.

    Upstream reduces a workload to `median_j(min_i(t_ij))` over studies and trials
    (`docs/DOCUMENTATION.md`, `NUM_STUDIES = 3`). The self-tuning ruleset runs a single trial per
    study, so the inner minimum is the identity and only the median survives here.

    The median rather than the mean, and the reason is miss absorption rather than efficiency: a
    study that never crosses is charged the full ceiling, and on the recorded corpus at least one
    study missed on 9 of 28 turns. A mean lets that one miss drag the unit; a median over three
    studies absorbs it. For Gaussian jitter alone a mean would be the tighter estimator, and that is
    not the failure this is chosen against.
    """
    return _median([expected_crossing_time(rows, threshold, direction, ceiling, sigma) for rows in studies])


def budget_fraction(time, ceiling):
    """AlgoPerf's per-workload ramp at the budget anchor: full credit at zero, none at the budget."""
    if ceiling <= 0:
        raise ValueError("the graded budget must be positive to place a run on the scale")
    return _clip(1.0 - (float(time) / float(ceiling)), 0.0, 1.0)


def aggregate(fractions):
    """The compensatory mean over units, which is what the performance profile reduces to.

    `rho(tau)` counts the workloads meeting a ratio and divides by their number
    (`scoring/performance_profile.py`), so a unit that is never reached costs `1/n` and nothing more.
    A conjunction over units is not upstream and is not used: the perturbations are stochastic
    training runs decided by a handful of validation examples, and a cliff on that is a coin flip
    rather than a measurement. The shipped conjunctive predicate is retained separately as
    `task_pass`, where a cliff is legitimate because it is not the training signal.

    Note the cost of this honestly: `n` here is between two and six, where upstream carries eight or
    nine, so abandoning one unit is worth more here than the `1/9` upstream dilution. Whether a unit
    was reached is therefore not recoverable from the scalar, and `task_pass` carries it instead.
    """
    if not fractions:
        raise ValueError("no graded units, so there is nothing to average")
    return sum(fractions) / float(len(fractions))


def is_feasible(rule_conformance, conformance_fraction):
    """Whether every constraint the pass conjuncts over is satisfied, speed aside."""
    return rule_conformance == 1 and conformance_fraction == 1


def compose(validity, rule_conformance, profile):
    """The continuous scalar a refinement loop climbs.

    One gate and one price. `validity` is the gate: it carries the six red lines and a log the parser
    could not read, and it hard-zeroes. Those are categorical facts -- the harness was modified or it
    was not, the reward file was written or it was not -- and across every episode this corpus has run
    only one red line has ever fired, correctly. The gate reads `validity` and not `rule_conformance`,
    a distinction that disqualified three earlier formulas: `rule_conformance` ranges over the rule
    checks alone and excludes every red line, so a scalar gated on it would pay a submission that
    crossed one.

    `rule_conformance` is now a PRICE rather than a second gate, and the change is forced by
    measurement. The static checks are AST analyses, and two of them have been shown to reject
    conforming code: `C-NO-SHAPE-FINGERPRINT` rejected 16 of 16 real submissions across 113 files and
    11 episodes, every one a false positive; `C-NO-WORKLOAD-DISPATCH` zeroed an attempt whose only
    flagged line asked whether a workload attribute was a float, which identifies nothing. Four
    otherwise-passing attempts were destroyed this way, each having already earned a closure above
    0.92 across a three-hour agent phase.

    A cliff is only defensible on a check that cannot be wrong. These can be, so they are priced:

        reward = profile * rule_conformance

    A submission holding six of seven rules keeps 85.7% of what it earned rather than losing all of
    it, and one holding four of seven keeps 57%. That preserves the incentive -- the rules guard
    against variant-specific tuning, which is exactly what the held-out perturbations exist to
    measure, so leaving them unpriced would invite the loop to find that hole -- while ensuring no
    single analyser bug can annihilate a costly trajectory. `task_pass` still conjuncts over full rule
    conformance, so nothing is hidden: a submission that broke a rule cannot pass, it can only score.
    """
    if not validity:
        return 0.0
    return _clip(profile, 0.0, 1.0) * _clip(rule_conformance, 0.0, 1.0)


def task_pass(validity, rule_conformance, conformance_fraction, all_units_reached):
    """The conjunction, as a predicate over the components rather than a threshold on the scalar.

    Deliberately no longer ordinally consistent with `reward`, and that is a change from the shipped
    contract rather than an oversight. Consistency was previously bought by thresholding the scalar
    at the pass, which welded the conjunction's discontinuity into the training signal -- measured on
    ep-sbx4, a single feasible/infeasible switch explained 93.2% of the reward's variance and was 3.2
    times more powerful than the entire graded axis. Forcing the two back into agreement costs the
    scalar its resolution, so they are reported side by side instead and the predicate is read from
    the components directly.
    """
    return (
        1.0
        if (
            validity == 1
            and rule_conformance == 1
            and is_feasible(rule_conformance, conformance_fraction)
            and all_units_reached
        )
        else 0.0
    )


# The greatest reward any run can attain. A submission crossing every unit at zero elapsed time would
# score one, which no run reaches: the first eval row cannot precede the first step, and across 168
# recorded runs the earliest was 2.663 s. The bound is therefore a limit rather than an attainable
# value, and unlike the shipped contract nothing here manufactures that gap with a tail term.
FULL_REWARD = 1.0

def write(directory, payload):
    """The only writer of the reward contract path. Overwrites on every code path.

    Written to reward.json and never to score.json, so the higher-precedence file Harbor reads first
    cannot mask the one this bundle documents.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "reward.json")
    flat = {}
    for key, value in payload.items():
        if isinstance(value, bool):
            flat[key] = 1.0 if value else 0.0
        elif value is None:
            flat[key] = -1.0
        else:
            flat[key] = float(value)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(flat, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def write_detail(directory, detail):
    """Per-check detail cannot live in reward.json because of the flat-key constraint."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "verity_detail.json")
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(detail, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path
