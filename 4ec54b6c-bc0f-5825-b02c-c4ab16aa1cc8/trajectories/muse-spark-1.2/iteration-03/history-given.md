# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 2 -- reward 0.7155, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2 *      0.7155   1.000             2 of 2         yes             17                

  reward  = what the attempt scored, in the closed interval 0 to 1. No value of it is a pass:
            task pass is a separate conjunction and is reported beside the reward, not inferred
            from it. A high reward with a failed pass, or the reverse, is a real outcome.
  rule conformance = the fraction of the static conformance rules the submitted bytes held.
  perturbation runs = the held-out runs beside the primary one. They are described by kind
            and are deliberately not individually named, so no run has a label you can
            iterate against; what each one measured is not published either.
  --      = the run did not produce this measurement. It is not a zero.
  *       = the best reward so far, and the one to beat.

  The other attempts held in detail, best-scoring and most recent:

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Two graded submissions, both with `measurement_status: "measured"`. Listed worst to best by reward:

- **Attempt 1 — reward 0.6694** (0.6693816459755828). `standing_against_best_so_far: "first_measured_attempt"`. All gates at ceiling: `validity` 1.0, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `primary_target_reached` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, `all_perturbations_held` true. `compute_efficiency` 0.5488, `per_step_cost_ratio` 1.5134, `wall_clock_sec` 17.4264, `qualifying_budget` 17.4264.
- **Attempt 2 — reward 0.7155** (0.7155227862405694). `standing_against_best_so_far: "better_than_every_earlier_attempt"` — this is an improvement over attempt 1, not a regression. Same ceiling on every gate: `validity` 1.0, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `primary_target_reached` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, `all_perturbations_held` true. `compute_efficiency` 0.6205, `per_step_cost_ratio` 1.5175, `wall_clock_sec` 17.4531, `qualifying_budget` 17.4531.

**Attempt 2 holds the highest reward, 0.7155. That is the score to beat.** No record so far produced a missing measurement, and no record scored zero.

The one term that moved materially between the two attempts is `compute_efficiency`: 0.5488 → 0.6205, a gain of +0.0717, alongside a reward gain of +0.0461. Every other reported term is either identical (all the pass/conformance/perturbation flags) or moved trivially in the *wrong* direction: `per_step_cost_ratio` rose slightly 1.5134 → 1.5175, and `wall_clock_sec` / `qualifying_budget` rose slightly 17.4264 → 17.4531. So the reward gain is attributable to the compute-efficiency term and not to wall clock, per-step cost, or any correctness gate — the efficiency measure evidently is not a pure function of wall clock, since wall clock got marginally worse while efficiency improved substantially.

## 2. Approach classes tried

Both records report only measured terms; the supplied data contains no source, no configuration and no textual description of what either submission did, so the approaches can only be characterised by the fingerprint they left in the metrics. I will not invent method details that the terms do not support.

- **Class A — a fully conforming, target-reaching trainer (attempt 1).** Establishes the working baseline: passes the task, satisfies the full ruleset, holds every declared perturbation, stays under the red line, and finishes in ~17.43 s wall clock at a per-step cost ratio of ~1.51× the reference. Reward 0.6694. The entire correctness half of the score was already saturated here; the deficit was in `compute_efficiency` (0.5488).
- **Class B — the same conforming trainer with an efficiency-directed change (attempt 2).** Identical fingerprint on every correctness and perturbation term, with `compute_efficiency` lifted to 0.6205 while wall clock and per-step cost ratio both nudged very slightly upward. Reward 0.7155. The signature — efficiency up, wall clock flat-to-worse, per-step ratio flat-to-worse — indicates the improvement came from doing *fewer or cheaper units of work* (steps, epochs, passes, or sampled data) rather than from making each step faster, since making steps faster would have shown up as a lower `per_step_cost_ratio`.

There is only one distinct approach family here — a conforming trainer — explored at two efficiency operating points. Nothing structurally different has been attempted.

## 3. Checks that failed

**None.** `failed_checks` is an empty list in both records, for the primary run and for every perturbation unit. `conformance_fraction` is 1.0 and `rule_conformance` is 1.0 in both. There is no repeated failing check to report, because there has been no failing check at all.

Perturbation outcomes, reported by kind and in aggregate: each record declared 2 perturbations (`perturbations_declared: 2.0`) and each carried one unit of kind `held_out_variant` and one of kind `ruleset`. In every case `reached` is true and `failed_checks` is empty, and `all_perturbations_held` is true in both records. Aggregating across the two records: 2 of 2 `held_out_variant` runs reached their threshold with no check failures, 2 of 2 `ruleset` runs reached their threshold with no check failures, 4 of 4 perturbation units held overall. No kind of held-out run is currently failing, and no check is currently stopping any of them. (The units are not identified across records; nothing here should be read as tracking a particular run from one attempt to the next.)

## 4. Ruled-out directions

- **Further work on correctness, validity, or rule conformance.** Ruled out as a scoring lever: `validity`, `task_pass`, `rule_conformance`, `conformance_fraction`, and `primary_target_reached` are all exactly 1.0 in both records, and `red_line_crossed` is 0.0 with `zero_reason_code` 0. There is no headroom in these terms — effort spent here cannot raise the reward, and any change that disturbs them can only lower it.
- **Hardening against the declared perturbations.** Ruled out for the same reason: `all_perturbations_held` is true in both records and all four perturbation units across both records reached their thresholds with empty `failed_checks`. Both the `held_out_variant` and the `ruleset` kinds are already fully satisfied; there is no failure to repair.
- **Chasing wall-clock time as the proxy for the efficiency term.** Ruled out by the observed data: wall clock rose from 17.4264 s to 17.4531 s between attempts 1 and 2 while `compute_efficiency` rose 0.5488 → 0.6205 and reward rose. Wall clock is therefore not what the efficiency term is tracking (or it is a very weak component of it), and optimising it in isolation is not supported as the route to a higher score. Note also that `qualifying_budget` equals `wall_clock_sec` exactly in both records, so the budget figure carries no information independent of wall clock.
- **Micro-optimising the cost of an individual step as the primary lever.** Not ruled out as harmful, but ruled out as the explanation of the gain so far: `per_step_cost_ratio` was essentially unchanged and slightly worse (1.5134 → 1.5175) across the attempt that improved the reward. Whatever produced the +0.0461 reward gain was not a reduction in per-step cost.

Nothing has been ruled out by a failed check, because no check has failed.

## 5. Open leads

- **Push `compute_efficiency` further — this is the only term with demonstrated headroom and demonstrated influence on reward.** It sits at 0.6205 after the best attempt, well below 1.0. The single observed cause–effect link in the data is efficiency up ⇒ reward up (+0.0717 efficiency, +0.0461 reward), which is roughly consistent with the efficiency term carrying a weight in the region of 0.6 of the reward's marginal movement. Continue in the same direction as attempt 2: reduce the total quantity of training work (step count, epoch count, data passes, evaluation passes, or redundant recomputation) while keeping every correctness gate at 1.0.
- **Attack `per_step_cost_ratio`, which has never been improved.** It is ~1.51 in both records, meaning each step costs roughly 1.5× the reference. It has moved by only +0.004 across two attempts, so it is effectively untouched territory — no attempt has yet tried to make an individual step cheaper. Candidates that do not risk the correctness gates: lower-precision arithmetic where the task tolerates it, fusing or eliminating per-step overhead such as redundant metric computation, avoiding per-step host/device synchronisation or logging, batching work that is currently done element-wise, and removing any per-step allocation. If the efficiency score has a per-step-cost component, this is unexploited; if it does not, this experiment cleanly separates the two hypotheses.
- **Run a deliberate separation experiment.** Because attempt 2 changed the efficiency score without changing wall clock or per-step ratio, the definition of `compute_efficiency` is still inferred rather than known. One attempt that moves *only* `per_step_cost_ratio` down, holding step count fixed, would pin down whether the efficiency term is step-count-driven, cost-driven, or both — and that knowledge directs every subsequent attempt.
- **Preserve the margin on the gates while doing so.** Both perturbation kinds (`held_out_variant`, `ruleset`) currently reach their thresholds, but the terms report only reached/not-reached, not by how much. Aggressive truncation of training to buy efficiency is the most plausible way to break `primary_target_reached` or to drop a `held_out_variant` unit below its threshold. Advance efficiency in increments and keep the target comfortably met rather than marginally met.

**Call: exploit.** The conforming-trainer approach is scoring, it improved on its second outing (0.6694 → 0.7155), and it has not plateaued — the term that drives the reward, `compute_efficiency`, is still at 0.6205 with clear headroom, and a second lever, `per_step_cost_ratio` at ~1.51, has not been touched at all. Take attempt 2's configuration as the base, keep every gate at 1.0 and all perturbation units held, and press further on reducing total training work while additionally trying, for the first time, to lower the per-step cost.
