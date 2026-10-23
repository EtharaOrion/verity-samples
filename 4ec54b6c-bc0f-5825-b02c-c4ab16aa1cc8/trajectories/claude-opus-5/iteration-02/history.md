# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 2 -- reward 0.5019, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      NOTE: this attempt's phase was cut before it finished. What follows was graded
            on whatever was on disk at that moment, not on what it intended to submit,
            so a term below may report unfinished work rather than a failed idea.
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 1 of 2 reached
        one ruleset run did not reach its threshold -- C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER
        the same ruleset run has now failed on 2 of your last 2 attempts
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.0000   1.000             0 of 2         no              --                
  2 *      0.5019   1.000             1 of 2         yes             14                

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

    attempt 1 -- reward 0.0000, first measured attempt
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

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED has failed on 2 attempts (1, 2). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Two graded attempts, both carrying a measurement (`measurement_status: measured_phase_cut` in each case). Ordered worst to best by reward:

- **Attempt 1 — reward 0.0000.** `zero_reason_code: 4`. `primary_target_reached: 0.0`, `conformance_fraction: 0.0`, `qualifying_budget: "not-measured"`, `task_pass: 0.0`. `validity: 1.0` and `rule_conformance: 1.0` (so the submission ran and broke no rule; it simply never reached the target). `compute_efficiency: 1.0`, `per_step_cost_ratio: 1.0194`, `wall_clock_sec: 89.98`. `red_line_crossed: 0.0`. Standing: `first_measured_attempt`.
- **Attempt 2 — reward 0.5019** (`0.5018889886411652`). `zero_reason_code: 0`. `primary_target_reached: 1.0`, `conformance_fraction: 0.5`, `qualifying_budget: 14.1634`, `wall_clock_sec: 14.1634`, `compute_efficiency: 0.6529`, `per_step_cost_ratio: 1.5029`. `validity: 1.0`, `rule_conformance: 1.0`, `red_line_crossed: 0.0`, `task_pass: 0.0`. Standing: `better_than_every_earlier_attempt`.

**Attempt 2 holds the highest reward, 0.5019, and it is the attempt to beat.** Attempt 1 produced a measurement whose reward was 0.0000 — it is a measured zero, not a missing measurement. Neither attempt has `all_perturbations_held: true`; both are capped by the same unheld perturbation.

# 2. Approach classes tried

Only the measured terms were supplied, so the approaches are distinguishable only by their measured signatures. Two distinct classes appear:

**Class A — the slow, target-missing configuration (attempt 1).** Ran ~90 s of wall clock at a near-baseline per-step cost (`per_step_cost_ratio: 1.0194`) and full `compute_efficiency: 1.0`, meaning it was cheap per step and used its allowance, yet **no evaluation row ever crossed the threshold in the declared direction**. Because no row qualified, no budget position could even be computed (`qualifying_budget: "not-measured"`). This class is characterised by: cheap steps, long run, no convergence to the target. Its rule conformance and validity were perfect, so the failure was purely one of learning progress, not of harness compliance.

**Class B — the expensive-per-step, fast-converging configuration (attempt 2).** Raised per-step cost by roughly 50% over baseline (`per_step_cost_ratio: 1.5029`, `compute_efficiency: 0.6529`) and in exchange crossed the primary threshold in 14.16 s of wall clock, which became the qualifying budget. This is the class that scored. The trade it makes is explicit in the numbers: it pays ~1.5× per step and recovers far more than that in steps-to-target, cutting wall clock from ~90 s to ~14 s. Everything the loop has actually earned comes from this class.

The move from Class A to Class B fixed the primary target and half the perturbation conformance (`conformance_fraction` 0.0 → 0.5) but left the `ruleset` perturbation failing identically.

# 3. Checks that failed

**Primary-run checks.**

- `C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction". Failed on attempt 1 only. Fixed by Class B.
- `C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists". Failed on attempt 1 only, and strictly as a consequence of `C-TARGET-REACHED`: with nothing qualifying there is no budget position to check. Fixed by Class B.
- `C-PERTURBATION-REACHED` — failed on **both** attempts, twice now. Attempt 1's reason: "0 of 2 declared perturbations reached their own threshold inside their own budget". Attempt 2's reason: "1 of 2 declared perturbations reached their own threshold inside their own budget". **This is the finding that matters most. Whatever was changed between attempt 1 and attempt 2 — the shift to a ~1.5× per-step-cost, fast-converging configuration — is not what is causing this check to fail.** It improved the count from 0/2 to 1/2 and then stopped; the remaining failure is untouched by that change.

**Held-out perturbation runs.** Two perturbations are declared per attempt (`perturbations_declared: 2.0`), of kinds `ruleset` and `held_out_variant`. Reporting by kind:

- **`ruleset` kind: did not reach its threshold in either attempt — 0 of 2 attempts.** In both records it failed the identical set of four checks: `C-LOG-WELL-FORMED`, `C-TARGET-REACHED`, `C-BUDGET-RESPECTED`, and `C-NO-LATCH-CARRYOVER`. The presence of `C-LOG-WELL-FORMED` and `C-NO-LATCH-CARRYOVER` here — neither of which ever appears on the primary run, where `rule_conformance` is 1.0 — is the distinctive signal: under a ruleset perturbation the submission emits a log the verifier cannot parse as well-formed and carries latched state across a boundary it must not. The `C-TARGET-REACHED`/`C-BUDGET-RESPECTED` failures on this run may well be downstream of the malformed log rather than independent, since a log that cannot be parsed cannot yield a crossing row.
- **`held_out_variant` kind: reached in attempt 2 (no failed checks), not reached in attempt 1, where it failed `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`** — the same convergence failure seen on attempt 1's primary run, and fixed by the same Class B change.
- **Aggregate across both attempts: 1 of 4 held-out perturbation runs reached its threshold.** The single unheld kind that blocks `all_perturbations_held` today is the `ruleset` kind.

The perturbation runs are not individually identified in the records, so no run can be tracked as "the same one" across attempts; the statements above are by kind only.

# 4. Ruled-out directions

- **Chasing validity, rule conformance, or red-line safety on the primary run.** `validity: 1.0`, `rule_conformance: 1.0`, `red_line_crossed: 0.0` in both attempts, including the attempt that scored 0.0000. Nothing here has ever been the binding constraint; effort spent hardening these buys nothing.
- **Class A's cheap-step / long-run configuration.** It reached no threshold at all on the primary run and none of its perturbations, for a measured reward of 0.0000. Its only advantage, `compute_efficiency: 1.0` and `per_step_cost_ratio: 1.0194`, is worthless when `C-TARGET-REACHED` fails, since the budget position is then not even measurable. Reverting toward it, or trimming attempt 2's per-step cost back toward baseline at the risk of losing the crossing, is ruled out by the direct comparison.
- **Treating the `ruleset` perturbation failure as a convergence or speed problem.** The Class A → Class B change was exactly a convergence-and-speed change; it flipped the `held_out_variant` run from unreached to reached and left the `ruleset` run failing the same four checks with no improvement. The `ruleset` failure is therefore not caused by the learning dynamics that were altered.
- **Reading `C-BUDGET-RESPECTED` on attempt 1's primary run as an overspend.** The verifier's own reason states there was no qualifying row and hence no budget position. It is a consequence of the missing target crossing, not an independent budget violation, and should not be addressed as one.

# 5. Open leads

1. **Fix `C-LOG-WELL-FORMED` under the `ruleset` perturbation.** This is the highest-value lead: it is the only check that has failed and has never been addressed by anything tried, it appears in both records, and it plausibly gates the `C-TARGET-REACHED`/`C-BUDGET-RESPECTED` failures on that same run. The primary run's logging parses fine (`rule_conformance: 1.0`), so the defect is specific to what the code emits when the ruleset differs — likely a field, row shape, or header that is written conditionally on rule-dependent state and becomes absent, duplicated, or wrongly typed when the ruleset changes. Make the log emission unconditional and identical in schema regardless of ruleset.
2. **Fix `C-NO-LATCH-CARRYOVER` under the `ruleset` perturbation.** Also present in both records and also never addressed. This names state that is latched in one phase or episode and survives into the next when it must be cleared. Audit every piece of persistent state — best-so-far trackers, cached thresholds, early-stop or "target already hit" flags, running normalisers, optimiser/schedule state — and reset it explicitly at each ruleset boundary rather than relying on re-initialisation that only happens on a fresh process. A latched "already reached" flag would explain a run that neither logs well-formed rows nor registers a crossing.
3. **Clearing 1 and 2 should flip `C-PERTURBATION-REACHED` to 2 of 2 and `conformance_fraction` from 0.5 toward 1.0, with `all_perturbations_held` becoming true.** That is the mechanically identified path from 0.5019 upward, since the primary run is already fully conformant.
4. **Preserve Class B's primary-run behaviour exactly while doing the above.** The target crossing at 14.16 s is the only earned asset; verify after each change that `primary_target_reached` stays 1.0 and `qualifying_budget` does not grow.
5. **Secondary, only after the perturbation checks hold:** `compute_efficiency` fell from 1.0 to 0.6529 and `per_step_cost_ratio` rose to 1.5029 in the scoring attempt. If reward is sensitive to these, there may be headroom in trimming per-step cost while keeping the fast convergence — but attempt 1 shows the downside of losing the crossing is total, so this is strictly a later refinement, not a first move.
6. **`task_pass` is 0.0 in both records, including the attempt that reached its primary target and scored 0.5019.** No supplied term explains what would raise it, and no attempt has moved it. Worth noting as an unexplained zero rather than acted on speculatively; do not trade away the perturbation work for it.

**Call: exploit.** Attempt 2's Class B configuration already scores 0.5019 and its primary run is clean on every check. The single thing stopping it is the `ruleset` perturbation, which fails on a named and stable pair of checks — `C-LOG-WELL-FORMED` and `C-NO-LATCH
# 1. Results so far

Two graded attempts, both carrying a measurement (measurement_status `measured_phase_cut` in each).

- **Attempt 1 — reward 0.0000.** zero_reason_code 4. Its primary run did not reach the target (primary_target_reached 0.0), so no qualifying budget existed and nothing was ranked below it except by being first. standing_against_best_so_far marks it `first_measured_attempt`.
- **Attempt 2 — reward 0.5019** (0.5018889886411652). Its primary run reached the target (primary_target_reached 1.0), qualifying_budget 14.16, per_step_cost_ratio 1.50, compute_efficiency 0.65. standing_against_best_so_far marks it `better_than_every_earlier_attempt`.

**Attempt 2 at reward 0.5019 is the highest and the one to beat.** Both attempts were measured; neither produced a null result. red_line_crossed is 0.0 in both, task_pass is 0.0 in both, so the reward gain came entirely from the primary target being reached in attempt 2 and not in attempt 1.

# 2. Approach classes tried

Only two graded configurations exist, and they differ in one visible respect: whether the primary training run crosses its declared target threshold inside budget.

- **Class A — target not reached (attempt 1).** The primary run failed C-TARGET-REACHED, which cascaded into C-BUDGET-RESPECTED having no qualifying row to score. per_step_cost_ratio was near 1.02 and compute_efficiency 1.0, i.e. cheap per step but never actually crossing the line. Reward 0.0000.
- **Class B — primary target reached, one perturbation short (attempt 2).** The primary run crossed the threshold, qualifying_budget became a real number (14.16), and reward rose to 0.5019. The cost of getting there rose too: per_step_cost_ratio 1.50 and compute_efficiency dropped to 0.65. This is the approach to build on.

# 3. Checks that failed

- **C-PERTURBATION-REACHED — failed in both attempts (2 of 2 records).** Reason in attempt 1: "0 of 2 declared perturbations reached their own threshold inside their own budget." Reason in attempt 2: "1 of 2 declared perturbations reached their own threshold inside their own budget." This is the standing blocker: it survived the change from Class A to Class B. Whatever was altered between the two attempts moved the primary run and one held-out run across their thresholds but **did not fix the perturbation that keeps failing this check** — so the cause of C-PERTURBATION-REACHED is not the thing that changed between attempts 1 and 2.
- **C-TARGET-REACHED — failed in attempt 1** at the primary level: "no evaluation row crosses the threshold in the declared direction." Cleared in attempt 2.
- **C-BUDGET-RESPECTED — failed in attempt 1** at the primary level: "no qualifying row, so no budget position exists." This was a downstream consequence of C-TARGET-REACHED, not an independent budget violation; it cleared in attempt 2 once a qualifying row existed.

# perturbation_units (reported by kind, since the runs are unnamed)

There are two held-out runs per attempt, of two kinds: **ruleset** and **held_out_variant**. I do not identify which is which beyond kind, and make no claim that any one run is the same across attempts.

- **ruleset kind — failed to reach in both attempts.** In each record it failed the same four checks: C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER. This kind never reached its threshold and is the one dragging C-PERTURBATION-REACHED down in attempt 2. The presence of C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER here — checks the primary run never trips — points at malformed logging and latch state carried across the ruleset perturbation, not at the training target itself.
- **held_out_variant kind — reached in attempt 2, not in attempt 1.** In attempt 1 it failed C-TARGET-REACHED and C-BUDGET-RESPECTED and did not reach. In attempt 2 it reached with an empty failed-checks list. So the held_out_variant kind is now passing; the ruleset kind is the outstanding failure.
- **Aggregate:** attempt 1, 0 of 2 reached; attempt 2, 1 of 2 reached, the miss being the ruleset kind.

# 4. Ruled-out directions

- **Chasing per-step cheapness at the expense of reaching the target (Class A).** Attempt 1 had the best per_step_cost_ratio (1.02) and full compute_efficiency (1.0) yet scored 0.0000 because no row crossed the threshold. Optimising cost while missing C-TARGET-REACHED is ruled out: efficiency is worthless without a qualifying row.
- **Assuming the primary-level fixes also fix the perturbations.** Attempt 2 cleared C-TARGET-REACHED and C-BUDGET-RESPECTED at the primary level and on the held_out_variant, but C-PERTURBATION-REACHED still failed because the ruleset kind stayed stuck. Treating the perturbation failure as the same defect as the primary target miss is ruled out by the evidence — they moved independently.

# 5. Open leads

- **Fix the ruleset perturbation directly (exploit).** It fails C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER in addition to the target/budget pair. Those two checks did not appear at the primary level, so the ruleset path likely emits malformed log rows and carries latched state across the perturbation boundary. Making the ruleset run's logging well-formed and clearing latch state between runs is the single change most likely to turn C-PERTURBATION-REACHED from "1 of 2" to "2 of 2" and lift reward above 0.5019.
- **Watch the cost regression while doing so.** Reaching the target in attempt 2 raised per_step_cost_ratio from 1.02 to 1.50 and cut compute_efficiency from 1.0 to 0.65. If reward has a cost component, recovering some efficiency at the reached target — without losing C-TARGET-REACHED — is a secondary gain worth holding onto once the ruleset perturbation reaches.

**Call: exploit.** Attempt 2 already scored 0.5019 and is still improving from attempt 1's 0.0000; the one thing stopping a higher reward is the ruleset perturbation failing C-PERTURBATION-REACHED via C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER. Fix that specific run rather than restructuring the approach.
