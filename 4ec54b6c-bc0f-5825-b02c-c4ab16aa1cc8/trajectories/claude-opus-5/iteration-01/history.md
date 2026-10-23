# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 1 -- reward 0.0000, first measured attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      NOTE: this attempt's phase was cut before it finished. What follows was graded
            on whatever was on disk at that moment, not on what it intended to submit,
            so a term below may report unfinished work rather than a failed idea.
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one ruleset run did not reach its threshold -- C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1 *      0.0000   1.000             0 of 2         no              --                

  reward  = what the attempt scored, in the closed interval 0 to 1. No value of it is a pass:
            task pass is a separate conjunction and is reported beside the reward, not inferred
            from it. A high reward with a failed pass, or the reverse, is a real outcome.
  rule conformance = the fraction of the static conformance rules the submitted bytes held.
  perturbation runs = the held-out runs beside the primary one. They are described by kind
            and are deliberately not individually named, so no run has a label you can
            iterate against; what each one measured is not published either.
  --      = the run did not produce this measurement. It is not a zero.
  *       = the best reward so far, and the one to beat.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

One graded submission exists.

- **Attempt 1 — reward 0.0000** (measurement_status: `measured_phase_cut`; `standing_against_best_so_far`: `first_measured_attempt`). This is a real measurement that returned zero, not an absent measurement.

Attempt 1 therefore holds the highest reward on record, 0.0000, and it is the one to beat. Because it is the only graded record, there is no attempt-over-attempt direction to report yet — nothing has regressed, and nothing has improved.

Supporting terms from that record, so the next attempt can tell which dimensions were already fine and which were not:

- `validity` 1.0, `rule_conformance` 1.0 — the submission was accepted and did not break the rules it was scored against.
- `red_line_crossed` 0.0 — no hard violation.
- `conformance_fraction` 0.0, `task_pass` 0.0, `primary_target_reached` 0.0 — the learning objective was simply never met.
- `compute_efficiency` 1.0, `per_step_cost_ratio` 1.0194, `wall_clock_sec` 89.98 — cost was essentially at parity with the reference per step and the run was short. Compute was not the binding constraint.
- `qualifying_budget` "not-measured" — no row qualified, so no budget position could be computed at all.
- `zero_reason_code` 4, `all_perturbations_held` false, `perturbations_declared` 2.0.

The shape of this result: the run was legal, cheap and fast, and produced no row that crossed the target threshold. The reward is zero for want of learning performance, not for want of conformance.

## 2. Approach classes tried

Exactly one approach class has been graded, and the measured terms supplied do not record what algorithm it used — no architecture, optimizer, schedule or data-handling detail is present in the record. What can be stated about it from the terms alone:

- **Class A — a single, cost-parity training run that never reached the target.** It ran to a phase cut in ~90 seconds at a per-step cost ratio of 1.0194, i.e. it did not attempt to buy performance with extra compute, and it produced evaluation rows but none crossing the declared threshold in the declared direction. It declared 2 perturbations and satisfied neither. Its logging was well-formed enough for the primary run to be scored, but not for the ruleset perturbation run (see section 3).

No second class has been tried. The next attempt should assume the whole design space is still open and should not assume any particular optimizer or schedule was already exercised, because the record does not say so.

## 3. Checks that failed

Primary run failed three checks:

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction." This is the root failure. Note the phrase *in the declared direction*: either the model genuinely did not learn enough, or the direction/threshold the submission declared does not match the sense of the metric being logged. Both readings are consistent with the reason string and both are worth checking.
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists." This is a consequence of the above, not an independent budget overrun. There was nothing to place against the budget. Fixing C-TARGET-REACHED is expected to dissolve this one; do not spend effort trimming compute to satisfy it, especially given `compute_efficiency` was already 1.0.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget."

Held-out perturbation runs, reported by kind (the runs are not identified beyond kind, and nothing in the record ties any run to any other):

- **`ruleset` kind — did not reach.** Stopped by four checks: **C-LOG-WELL-FORMED**, **C-TARGET-REACHED**, **C-BUDGET-RESPECTED**, and **C-NO-LATCH-CARRYOVER**. This is the most informative single unit in the whole record. C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER failed *here and nowhere else* — the primary run's logs were well-formed and showed no latch carryover. So under an altered ruleset the submission emits malformed log records and carries state (a latch) across a boundary it must not. That points at logging or state that is conditioned on the default ruleset rather than being derived fresh per run.
- **`held_out_variant` kind — did not reach.** Stopped by **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**, the same pair as the primary run and nothing more. Its logging and latch behaviour were clean.

Aggregate: 0 of 2 declared perturbations held; `all_perturbations_held` is false. Both kinds fail on C-TARGET-REACHED and its downstream C-BUDGET-RESPECTED; only the `ruleset` kind additionally fails on well-formedness and latch carryover.

Recurrence: within this single record, **C-TARGET-REACHED** and **C-BUDGET-RESPECTED** each failed three times — once in the primary run and once in each of the two perturbation units. That breadth matters: the target miss is not specific to one held-out condition, it is the submission's uniform behaviour everywhere it was evaluated. Across attempts there is as yet only one record, so no check can yet be said to have survived a change; the next summary will be the first able to say that.

## 4. Ruled-out directions

- **Reducing compute per step, shortening the run, or otherwise optimising for cost.** Ruled out because `compute_efficiency` was already 1.0 and `per_step_cost_ratio` 1.0194 at a 90-second wall clock. Cost is not what is being penalised, and C-BUDGET-RESPECTED failed for the absence of a qualifying row, not for exceeding a budget.
- **Chasing validity or rule conformance.** Ruled out because `validity` 1.0, `rule_conformance` 1.0 and `red_line_crossed` 0.0 — the harness accepted the submission cleanly. Effort spent making the submission "more compliant" in the general sense addresses nothing that failed.
- **Re-submitting Class A unchanged, or changed only in ways that do not affect whether an evaluation row crosses the threshold.** That would repeat a zero without touching what caused it, which is neither exploration nor exploitation. This is stated pre-emptively: with only one record there is no established pattern of repetition yet, and there should not become one.
- **Treating C-BUDGET-RESPECTED as a separate problem to solve.** Ruled out by its own reason string: it is strictly downstream of having no qualifying row.

## 5. Open leads

Ordered by expected value.

1. **Verify the declared threshold and direction against what is actually logged.** C-TARGET-REACHED's reason names the direction explicitly. Before assuming the model underfits, confirm that the metric being written to evaluation rows is the one the threshold is declared over, that its sign/orientation matches the declared direction (loss-lower-is-better versus score-higher-is-better is the classic inversion), and that rows are emitted at points where the threshold could plausibly be crossed. A declaration mismatch would explain a uniform miss across the primary run and both perturbation kinds at once, which a pure capability shortfall explains less economically.
2. **Actually raise task performance, and spend compute to do it.** If the declaration is correct, the run is simply underperforming. There is headroom: cost ratio ~1.02 and 90 seconds wall clock, with compute efficiency already maxed, means a longer or larger run is affordable in a way the record gives no evidence against. Train longer, tune the learning rate and schedule, and confirm the loss is descending at the cut rather than diverging or flat — a phase cut at 90 seconds may simply have arrived before the threshold.
3. **Make logging independent of the ruleset.** C-LOG-WELL-FORMED failed only under the `ruleset` perturbation. Emit log rows with fields, ordering and types constructed from the run's own configuration rather than from any default-ruleset assumption, and exercise the writer under a non-default ruleset before submitting.
4. **Eliminate cross-run latched state.** C-NO-LATCH-CARRYOVER failed only under the `ruleset` perturbation, so some object — a cached statistic, a module-level singleton, a persisted normaliser, an optimizer or RNG state — survives from one run into the next. Construct all such state inside the per-run entry point, reset or reseed explicitly at run start, and avoid module-level mutable globals.
5. **Confirm the perturbation runs use their own budgets and thresholds.** C-PERTURBATION-REACHED specifies "their own threshold inside their own budget." If the submission hardcodes the primary run's threshold or budget, the perturbations will fail even after the primary succeeds. Read these per run.

Leads 3 and 4 will not by themselves produce reward — the `held_out_variant` kind failed with clean logs and no latch carryover, so well-formedness is not the gate on reaching the target. They are necessary to make `all_perturbations_held` true once the target is reachable, and they are cheap. Lead 1 is the one that could flip the result on its own.

**Call: explore.** The only graded approach scored 0.0000, so there is no scoring approach to make better; "exploit" would mean refining a result that does not exist. The single measured class was legal and cheap but never crossed the target in any of the three places it was evaluated, and the cost terms show the failure was not a resource limit. The next attempt should change the substance of the training — and first re-derive the threshold declaration from scratch — rather than tune the margins of Class A.
