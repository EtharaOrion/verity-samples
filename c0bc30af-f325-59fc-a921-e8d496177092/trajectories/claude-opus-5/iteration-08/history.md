# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.9128, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All three attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4        0.8719   1.000             2 of 2         yes             50                
  5 *      0.9128   1.000             2 of 2         yes             25                
  6        0.5615   0.857             2 of 2         yes             204               
  7        0.0000   1.000             0 of 2         no              --                
  8        0.7551   1.000             2 of 2         yes             78                

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
  2 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 2 -- reward 0.8385, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.8719, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 6 -- reward 0.5615, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 204
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 7 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 8 -- reward 0.7551, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 78
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 2 attempts (3, 7). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 2 attempts (3, 7). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 2 attempts (3, 7). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Eight graded attempts, all of them measured (none is missing a measurement; none is a "no measurement" record). Listed worst to best by `reward`:

- **Attempt 3 — reward 0.0000.** `zero_reason_code` 4, `primary_target_reached` 0, `task_pass` 0, `conformance_fraction` 0.0, `all_perturbations_held` false. `wall_clock_sec` 1692.5153, `qualifying_budget` not measured. `rule_conformance` was 1.0 and `validity` 1.0 — the code was well-formed; it simply never crossed the threshold. Standing: worse than an earlier attempt.
- **Attempt 7 — reward 0.0000.** Identical failure signature to attempt 3: `zero_reason_code` 4, `primary_target_reached` 0, `conformance_fraction` 0.0, `wall_clock_sec` 1692.2115, `qualifying_budget` not measured, `rule_conformance` 1.0, `validity` 1.0. Standing: worse than an earlier attempt.
- **Attempt 6 — reward 0.5615** (0.5614595915946324). Target reached (`primary_target_reached` 1.0) and both perturbations held, but `task_pass` 0 and `rule_conformance` 0.8571 because of a failed check. `wall_clock_sec` 204.0885, `per_step_cost_ratio` 1.3778, `compute_efficiency` 0.6091. Standing: worse than an earlier attempt — this is a regression, not progress.
- **Attempt 8 — reward 0.7551** (0.7551378151147599). Fully clean: no failed checks, `rule_conformance` 1.0, `task_pass` 1.0, both perturbations held. But `wall_clock_sec` 151.5049 against a `qualifying_budget` of 78.1441 — the only record where these two numbers differ — with `per_step_cost_ratio` 1.0291 and `compute_efficiency` 0.8703. Standing: worse than an earlier attempt. A clean run that still scored below three earlier clean runs.
- **Attempt 1 — reward 0.7684** (0.7684495494479875). First measured attempt. Target reached and both perturbations held, but `task_pass` 0 and `rule_conformance` 0.8571 from one failed check. `wall_clock_sec` 25.4619, `per_step_cost_ratio` 1.0639, `compute_efficiency` 0.8160.
- **Attempt 2 — reward 0.8385** (0.8385437894774304). Fully clean, `task_pass` 1.0, `rule_conformance` 1.0, both perturbations held. `wall_clock_sec` 73.6235, `per_step_cost_ratio` 0.9162, `compute_efficiency` 0.9164. Standing at the time: better than every earlier attempt.
- **Attempt 4 — reward 0.8719** (0.8718974477208268). Fully clean, `task_pass` 1.0, both perturbations held. `wall_clock_sec` 50.0341, `per_step_cost_ratio` 0.7115, `compute_efficiency` 1.0000 (the highest compute efficiency recorded). Standing at the time: better than every earlier attempt.
- **Attempt 5 — reward 0.9128** (0.9128129743237858). **Highest reward recorded; this is the one to beat.** Fully clean: no failed checks, `rule_conformance` 1.0, `task_pass` 1.0, `validity` 1.0, `primary_target_reached` 1.0, both perturbations held, `red_line_crossed` 0. `wall_clock_sec` 25.3436 (the shortest of any run that reached target), `qualifying_budget` 25.3436, `per_step_cost_ratio` 0.9887, `compute_efficiency` 0.7728.

`red_line_crossed` is 0.0 and `validity` is 1.0 in every record — nothing has ever tripped a hard safety/validity stop.

**The strongest pattern in the whole record set:** among runs that reach the target with full conformance, reward falls monotonically as `wall_clock_sec` rises. 25.3436 s → 0.9128; 50.0341 s → 0.8719; 73.6235 s → 0.8385; 151.5049 s → 0.7551. Note that `compute_efficiency` does *not* track reward: attempt 4 had the maximum `compute_efficiency` of 1.0000 and still scored below attempt 5, whose `compute_efficiency` was only 0.7728. Elapsed wall clock, not the efficiency figure, is what separates the scoring attempts. Attempt 8 further suggests the graded quantity follows `wall_clock_sec` (151.5) rather than `qualifying_budget` (78.1), since its reward sits well below attempt 2's despite a comparable qualifying budget.

# 2. Approach classes tried

Four distinct classes are visible in the measured terms; eight records collapse into these four.

**Class A — short-horizon conforming trainer that reaches the target quickly.** Attempts 2, 4 and 5. All three are fully clean (no failed checks, `rule_conformance` 1.0, `task_pass` 1.0, both perturbation runs reached). They differ only in how long they ran and how expensive each step was: attempt 2 at 73.6235 s with `per_step_cost_ratio` 0.9162, attempt 4 at 50.0341 s with `per_step_cost_ratio` 0.7115 and `compute_efficiency` 1.0000, attempt 5 at 25.3436 s with `per_step_cost_ratio` 0.9887. This class produced every top score and contains the best result. Within the class, the shortest total elapsed time won, and it won despite having a *worse* per-step cost ratio and a *worse* compute-efficiency figure than attempt 4 — i.e. cutting total steps/epochs beat cutting per-step cost.

**Class B — same style of trainer, but with disallowed module-level code.** Attempts 1 and 6. Both reached the primary target and both held all perturbations, so the learning side worked; both were docked to `rule_conformance` 0.8571 and `task_pass` 0 by a single failed conformance check (named in section 3). Attempt 1 was fast (25.4619 s, reward 0.7684); attempt 6 was slow and expensive (204.0885 s, `per_step_cost_ratio` 1.3778, `compute_efficiency` 0.6091, reward 0.5615). The conformance penalty and the long run compounded in attempt 6 to produce the worst non-zero reward on record.

**Class C — long-horizon configuration that never crosses the threshold.** Attempts 3 and 7. Both ran to ~1692 s (1692.5154 and 1692.2115 — near-identical, consistent with hitting a hard time cap rather than converging), both produced `primary_target_reached` 0, `conformance_fraction` 0.0, no qualifying row and therefore no measurable `qualifying_budget`, and both scored 0.0000 with `zero_reason_code` 4. Notably both were fully rule-conforming (`rule_conformance` 1.0) and valid, and attempt 3's `compute_efficiency` was 0.9672 with attempt 7's at 1.0000 — high efficiency figures on runs that scored nothing. Whatever was changed between attempts 3 and 7 did not change the outcome at all.

**Class D — conforming run with substantial elapsed time beyond the qualifying window.** Attempt 8. Clean on every check, target reached, perturbations held, but `wall_clock_sec` 151.5049 against `qualifying_budget` 78.1441 — roughly 73 s of elapsed time outside the qualifying row. `per_step_cost_ratio` 1.0291. Reward 0.7551, below all three Class A results. This is the only record where the two time figures diverge, and it is the clean run that scored lowest, which is the evidence that total elapsed wall clock is being charged, not just the qualifying budget.

# 3. Checks that failed

Four distinct named checks have failed, across four records.

- **C-API-SURFACE** — reason given by the verifier: *"module-level statements outside imports, constants, and permitted definitions."* **This check has now failed twice**, in attempt 1 and again in attempt 6. Whatever was changed between those two attempts is not what causes this check to fail: the identical check fired with the identical reason on both, so the differences between them (run length, per-step cost, whatever else was edited) are irrelevant to it. The fix is specific and mechanical: the submission file must contain nothing at module scope except imports, constant assignments, and the permitted `def`/`class` definitions. Any executable statement at top level — a print, a call, a loop, a config-building expression, an `if __name__ == "__main__"` block if that is not among the permitted forms, a seeding or device-selection call outside a function — is what trips it. Move all of it inside the required entry-point function. Each failure cost `rule_conformance` (1.0 → 0.8571) and forced `task_pass` to 0.

- **C-TARGET-REACHED** — reason: *"no evaluation row crosses the threshold in the declared direction."* **Failed twice**, in attempts 3 and 7, on the primary run. Again, whatever was changed between attempts 3 and 7 did not address it. Two readings are consistent with the terms: either the run genuinely never reaches the declared metric threshold, or it reaches it but the declared *direction* of comparison is wrong so no row is counted as crossing. The near-identical ~1692 s wall clock on both points to the run being cut off at a cap before any row qualified.

- **C-BUDGET-RESPECTED** — reason: *"no qualifying row, so no budget position exists."* **Failed twice**, in attempts 3 and 7. This is a downstream consequence of C-TARGET-REACHED, not an independent budget overrun: with no row crossing the threshold, there is nothing against which a budget position can be computed, which is also why `qualifying_budget` is reported as not measured in both records. Fixing C-TARGET-REACHED should clear this automatically.

- **C-PERTURBATION-REACHED** — reason: *"0 of 2 declared perturbations reached their own threshold inside their own budget."* **Failed twice**, in attempts 3 and 7, driving `conformance_fraction` to 0.0 and `all_perturbations_held` to false in both.

Every one of the four checks has failed exactly twice, and in each pair the same reason string was returned both times. Nothing edited between the members of either pair touched the cause.

# 4. Ruled-out directions

- **Leaving executable code at module scope.** Ruled out by two independent failures of C-API-SURFACE with the same verifier reason (attempts 1 and 6). Both of those runs reached the target and held all perturbations, so the training logic was fine and the entire loss was the conformance penalty. Attempt 1 scored 0.7684 with a 25.46 s run while attempt 5 scored 0.9128 with a 25.34 s run — an almost identical time budget, and the gap of roughly 0.14 is attributable to the conformance failure. There is no scenario in which keeping module-level statements is worth it.

- **Long-horizon training that runs to the ~1692 s cap.** Ruled out by attempts 3 and 7, both reward 0.0000 with `zero_reason_code` 4. High `compute_efficiency` (0.9672 and 1.0000) and clean `rule_conformance` did not rescue either. Running longer is not merely inefficient here — it produces no qualifying row at all and collapses the reward to zero. Repeating this shape without changing what stops the threshold from being crossed would be neither exploration nor exploitation.

- **Optimising `per_step_cost_ratio` or `compute_efficiency` as the objective.** Ruled out by direct comparison. Attempt 4 achieved `compute_efficiency` 1.0000 and the best `per_step_cost_ratio` of any scoring run (0.7115) and still lost to attempt 5, which had `compute_efficiency` 0.7728 and `per_step_cost_ratio` 0.9887, by 0.0409 reward. Attempt 7 had `compute_efficiency` 1.0000 and scored 0.0000. These two figures do not rank attempts; total elapsed wall clock among target-reaching, conforming runs does.

- **Letting elapsed time run past the qualifying window.** Ruled out by attempt 8: fully clean on every check, target reached, all perturbations held, and still only 0.7551 — below attempts 2, 4 and 5 — with `wall_clock_sec` 151.5049 against `qualifying_budget` 78.1441. Post-target work, extra evaluation passes, redundant re-training, or anything else that keeps the process alive after the qualifying row is produced appears to be charged. Stop as soon as the target is banked.

- **Accepting per-step cost ratios above 1.0.** Every record with `per_step_cost_ratio` > 1.0 (attempt 1 at 1.0639, attempt 6 at 1.3778, attempt 8 at 1.0291) scored 0.7684 or below; the best result sat at 0.9887, just under 1.0. This is weaker evidence than the wall-clock relation and is partly confounded with the conformance failures, so treat it as a caution rather than a hard rule — but do not deliberately buy per-step expense.

# 5. Open leads

- **Start from the attempt-5 configuration and shave wall clock further.** It is the record holder at 0.9128 with `wall_clock_sec` 25.3436, and reward has moved monotonically with elapsed time across every clean run (25.34 → 0.9128, 50.03 → 0.8719, 73.62 → 0.8385, 151.50 → 0.7551). The gradient is steepest at the low end: the step from 50.03 s to 25.34 s bought 0.0409. Cutting to, say, the 15–20 s range plausibly buys more, provided the target is still crossed on the primary run and on both perturbation runs. Concretely: fewer epochs/steps, early exit the moment the evaluation row crosses the threshold, drop any extra evaluation passes, avoid re-instantiating the model or re-loading data more than once, and skip any warm-up or final full-dataset pass that is not needed to produce the qualifying row.

- **Add an explicit early-stop on threshold crossing.** Attempt 8's split between `wall_clock_sec` 151.5049 and `qualifying_budget` 78.1441 shows roughly half its elapsed time was spent after the qualifying position existed. If the current code always runs a fixed number of epochs, converting it to "evaluate each epoch, return immediately once the declared metric crosses in the declared direction" should collect the same qualifying row at a strictly lower wall clock.

- **Find the floor before it becomes a cliff.** The risk of trimming is falling into the Class C outcome (reward 0.0000 via C-TARGET-REACHED). Because attempts 3 and 7 show that a non-crossing run scores zero rather than a reduced score, the downside of over-trimming is total, while the upside of trimming is incremental. Keep a comfortable margin above the threshold rather than tuning to just barely cross, and keep the early-stop condition tied to the actual measured metric rather than a fixed step count that was tuned on one seed.

- **Protect the margin on the perturbation runs specifically.** Across all eight records there were 16 held-out runs, two per record, one of kind `held_out_variant` and one of kind `seed`. Twelve reached their threshold. Four did not: in each of the two zero-scoring records, both the `held_out_variant` run and the `seed` run failed, each on C-TARGET-REACHED and C-BUDGET-RESPECTED. By kind, that is two `held_out_variant` failures and two `seed` failures, and in both records the failure was total (0 of 2 reached), never partial — the perturbation runs have always succeeded or failed together with the primary run, never independently. So there is no evidence of a perturbation-specific fragility to fix; the perturbation runs simply mirror whatever the primary run does. That said, since the `seed` perturbation re-runs under a different random seed, any trimming should leave enough headroom that seed variance alone cannot push the metric back below threshold — this is the single most likely way an aggressive time cut turns 0.9128 into 0.0000.

- **Keep the file surface strictly clean.** Before submitting, read the module top-to-bottom and confirm that at module scope there are only `import` statements, constant assignments, and function/class definitions. Seeding, device selection, config construction and any diagnostic output belong inside the entry-point function. This is worth roughly 0.14 reward based on the attempt-1 versus attempt-5 comparison at equal run time, and it has already cost two attempts.

- **Secondary, lower-confidence lead:** attempt 4 reached `compute_efficiency` 1.0000 with `per_step_cost_ratio` 0.7115, and attempt 5 reached the best reward with a much worse 0.9887. If the cheap-per-step machinery from attempt 4 can be combined with attempt 5's short horizon, both figures might improve at once. Treat this as an add-on to the wall-clock reduction, not a substitute — the evidence says per-step cost does not rank attempts on its own.

**Call: exploit.** The attempt-5 configuration scored 0.9128 with a fully clean check sheet, and the scoring family (attempts 2, 4, 5) is still improving along a clear, measured axis — shorter total wall clock — with the largest observed gain coming from the most recent cut. The next attempt should rebuild that short, conforming, early-stopping trainer and reduce elapsed time further while keeping a safety margin above the metric threshold, rather than introducing a structurally different method. Two directions have already been repeated without changing their cause — the C-API-SURFACE module-level violation (attempts 1 and 6) and the ~1692 s non-converging run (attempts 3 and 7) — and repeating either again would be neither exploring nor exploiting.
