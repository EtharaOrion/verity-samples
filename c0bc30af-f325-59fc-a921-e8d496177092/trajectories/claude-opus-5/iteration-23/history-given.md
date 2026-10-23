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

    All 17 attempts since have scored lower than it.
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
  9        0.0000   1.000             0 of 2         no              --                
  10       0.0000   1.000             0 of 2         no              --                
  11       0.8980   1.000             2 of 2         yes             25                
  12       0.0000   1.000             0 of 2         no              --                
  13       0.8451   1.000             2 of 2         yes             71                
  14       0.6955   1.000             2 of 2         yes             100               
  15       0.0000   1.000             0 of 2         no              --                
  16       0.0000   1.000             0 of 2         no              --                
  17       0.7919   1.000             2 of 2         yes             74                
  18       0.8794   1.000             2 of 2         yes             49                
  19       0.9121   1.000             2 of 2         yes             46                
  20       0.8661   1.000             2 of 2         yes             62                
  21       0.0000   1.000             0 of 2         no              --                
  22       0.0000   1.000             0 of 2         no              --                

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
  16 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.9121, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 46
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 20 -- reward 0.8661, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 62
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 21 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 22 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 2 of your last 4 attempts
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same seed run has now failed on 2 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All twenty-two records carry `measurement_status: "measured"`, so every one has a reward. Ordered worst to best:

**Zero-reward group (nine attempts, all identical in their measured signature):** attempts 3, 7, 9, 10, 12, 15, 16, 21 and 22 each scored **0.0000**. Every one of them has `zero_reason_code: 4`, `primary_target_reached: 0.0`, `task_pass: 0.0`, `conformance_fraction: 0.0`, `qualifying_budget: "not-measured"`, and a wall clock pinned in a very narrow band around 1690–1693 seconds (1690.32, 1690.45, 1690.48, 1690.96, 1691.00, 1691.53, 1692.21, 1692.52, 1692.97). Note that `rule_conformance` was a clean 1.0 in all nine and `red_line_crossed` was 0.0 — these did not fail on code-surface grounds, they simply never reached the target and ran to what looks like a hard time cap.

Then the scoring attempts, worst to best:

- Attempt 6 — **0.5615** (wall clock / qualifying budget 204.09 s; `rule_conformance` 0.857; `task_pass` 0.0; `per_step_cost_ratio` 1.3778). Worse than every earlier scoring attempt at the time.
- Attempt 14 — **0.6955** (99.74 s; clean conformance; `task_pass` 1.0). Lower than the then-best.
- Attempt 8 — **0.7551** (qualifying budget 78.14 s but wall clock 151.50 s; clean conformance; `per_step_cost_ratio` 1.0291). Lower than the then-best.
- Attempt 1 — **0.7684** (25.46 s; `rule_conformance` 0.857; `task_pass` 0.0). First measured attempt.
- Attempt 17 — **0.7919** (73.80 s; clean; `per_step_cost_ratio` 0.7318). Lower than the then-best.
- Attempt 2 — **0.8385** (73.62 s; clean; first attempt with `task_pass` 1.0). Better than every earlier attempt at the time.
- Attempt 13 — **0.8451** (71.31 s; clean; `per_step_cost_ratio` 1.0266). Lower than the then-best.
- Attempt 20 — **0.8661** (62.46 s; `compute_efficiency` 1.0; `per_step_cost_ratio` 0.6145). Lower than the then-best.
- Attempt 4 — **0.8719** (50.03 s; `compute_efficiency` 1.0; `per_step_cost_ratio` 0.7115). Better than every earlier attempt at the time.
- Attempt 18 — **0.8794** (49.33 s; clean; `per_step_cost_ratio` 0.9260). Lower than the then-best.
- Attempt 11 — **0.8980** (25.35 s; clean; `per_step_cost_ratio` 1.0502; `compute_efficiency` 0.7043). Lower than the then-best.
- Attempt 19 — **0.9121** (45.81 s; clean; `compute_efficiency` 0.9345; `per_step_cost_ratio` 0.7669). Lower than the then-best, by a hair.
- Attempt 5 — **0.9128** (25.34 s; clean; `compute_efficiency` 0.7728; `per_step_cost_ratio` 0.9887; `task_pass` 1.0; all perturbations held). **This is the highest reward recorded and it is the one to beat.**

Everything after attempt 5 is `worse_than_an_earlier_attempt`; the best score has not been improved since attempt 5, and thirteen attempts have been graded since without matching it. `validity` is 1.0 and `red_line_crossed` is 0.0 in every single record, so nothing has ever been rejected as invalid or tripped a red line.

# 2. Approach classes tried

Only measured terms are available to me — no source was carried forward — so these classes are grouped by their measured fingerprints, which are sharply distinct.

**Class A — conforming, fast-converging trainer (the scoring family).** Eleven attempts (2, 4, 5, 11, 13, 14, 17, 18, 19, 20, and 8 as a variant): `rule_conformance` 1.0, no failed checks, `primary_target_reached` 1.0, `task_pass` 1.0, both perturbation units reached, qualifying budget between 25.3 and 99.7 seconds. Reward within this class moves almost monotonically against the qualifying budget: 25.3 s → ~0.90–0.91, 45–50 s → ~0.87–0.91, 62–74 s → ~0.79–0.87, 100 s → 0.70. Budget is the dominant lever the exposed terms show.

Two controlled comparisons inside this class are worth carrying forward verbatim:

- Attempts 5 and 11 finished at essentially the same qualifying budget (25.3436 s vs 25.3479 s) yet scored 0.9128 and 0.8980. The exposed terms that differ are `per_step_cost_ratio` (0.9887 vs 1.0502) and `compute_efficiency` (0.7728 vs 0.7043). Lower per-step cost and higher compute efficiency at equal budget bought roughly +0.015 reward.
- Attempt 19 at 45.81 s scored 0.9121, statistically level with attempt 5 at 25.34 s. So budget is not the whole story: attempt 19 paid nearly double the time and made it back through `compute_efficiency` 0.9345 and `per_step_cost_ratio` 0.7669. There is a second term in the reward that the budget alone does not capture.
- Counterexample against over-fitting to `compute_efficiency`: attempts 4 and 20 both hit `compute_efficiency` 1.0 with low per-step cost ratios (0.7115, 0.6145) and still scored only 0.8719 and 0.8661, because their budgets were 50.0 s and 62.5 s. Maximising compute efficiency while letting the budget grow is a net loss.

**Class A′ — the same family with a trailing non-qualifying phase.** Attempt 8 is the only record where `wall_clock_sec` (151.50) exceeds `qualifying_budget` (78.14). It scored 0.7551, below attempt 2 which had a near-identical qualifying budget of 73.62 s and scored 0.8385. Work done after the qualifying row appears to cost reward rather than being free. Do not leave extra epochs, extra evaluation sweeps, or cleanup training running past the point where the target row is produced.

**Class B — conforming family with an API-surface violation.** Attempts 1 and 6: `rule_conformance` 0.857 (6 of 7), `task_pass` 0.0, but `primary_target_reached` 1.0 and both perturbation units reached. These attempts *trained successfully* and were docked purely on the code-surface check. Attempt 1 still scored 0.7684 at a 25.46 s budget — which, compared against attempt 5's 0.9128 at a nearly identical 25.34 s budget, prices the C-API-SURFACE violation at roughly 0.14 of reward. Attempt 6 compounded it with a 204 s budget and a `per_step_cost_ratio` of 1.3778, landing at 0.5615.

**Class C — the non-converging long-run class.** Nine attempts (3, 7, 9, 10, 12, 15, 16, 21, 22), all scoring 0.0000, all running to ~1690 s. Their `per_step_cost_ratio` values (0.6827–0.8901) and `compute_efficiency` values (0.9033–1.0) are *good* — several are better than the winning attempt's. That is the trap: this class produced cheap, efficient steps that never crossed the threshold. Whatever it is that distinguishes these nine from Class A, it is not step cost and not compute efficiency. Nine separate attempts landed in this basin, which is the single largest waste in the record.

# 3. Checks that failed

**C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction". Failed in **nine** records (attempts 3, 7, 9, 10, 12, 15, 16, 21, 22). This is the primary failure and every other failure in those records is downstream of it.

**C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". Failed in the same **nine** records. This is a consequence of C-TARGET-REACHED, not an independent budget overrun: with no row crossing the threshold there is no row whose budget could be assessed. Fixing convergence fixes this check for free; tightening the budget alone will not.

**C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed in the same **nine** records, always with the count 0 of 2, never 1 of 2.

**C-API-SURFACE** — "module-level statements outside imports, constants, and permitted definitions". Failed in **two** records (attempts 1 and 6). These two are separated by four other graded attempts and by very different runtime profiles (25.46 s vs 204.09 s, `per_step_cost_ratio` 1.0639 vs 1.3778), and the check failed identically in both with the identical reason. Whatever was changed in the training procedure between those two attempts is not what causes this check to fail. It is caused by the shape of the module: executable statements sitting at import level. The fix is mechanical — move every top-level statement that is not an import, a constant assignment, a function definition or a class definition inside a function body, and guard any driver code. This check has held cleanly (`rule_conformance` 1.0) in the other twenty records, so a conforming module shape is demonstrably achievable.

Since attempt 6 no submission has failed C-API-SURFACE; the outstanding failure mode is the convergence cluster.

# 4. Ruled-out directions

**Long-running training that runs to the ~1690 s cap.** Nine attempts did this and all nine returned 0.0000 with C-TARGET-REACHED, C-BUDGET-RESPECTED and C-PERTURBATION-REACHED all failing. Repeating a configuration that runs past a couple of minutes without producing a threshold-crossing evaluation row is a guaranteed zero. Nine records is more than enough evidence; do not spend another attempt here.

**Optimising `per_step_cost_ratio` or `compute_efficiency` as the objective.** The zero cluster achieved per-step cost ratios as low as 0.6827 and compute efficiency up to 1.0 and still scored 0.0000. Within the scoring class, attempts 4 and 20 reached `compute_efficiency` 1.0 and scored 0.8719 and 0.8661, both below attempt 5's 0.9128 at `compute_efficiency` 0.7728. Cheap steps do not substitute for reaching the target quickly in wall-clock terms.

**Letting the run continue after the qualifying row is produced.** Attempt 8 is the one record where wall clock (151.50 s) exceeds qualifying budget (78.14 s), and it scored 0.7551 against attempt 2's 0.8385 at a comparable 73.62 s qualifying budget. The extra unqualified runtime cost roughly 0.08 with no compensating gain.

**Budgets in the 70–210 second range.** Attempts 2 (73.62 s, 0.8385), 17 (73.80 s, 0.7919), 8 (78.14 s, 0.7551), 14 (99.74 s, 0.6955) and 6 (204.09 s, 0.5615) form a clean descending staircase. Nothing above ~65 s has ever beaten 0.8451. The best region is 25–50 s.

**Module-level executable statements.** Ruled out by C-API-SURFACE failing twice with the same reason and costing about 0.14 of reward at an otherwise-competitive budget (attempt 1: 0.7684 at 25.46 s versus attempt 5: 0.9128 at 25.34 s). There is no upside to this shape and the penalty is large.

# 5. Open leads

**Held-out run outcomes.** Two held-out runs accompany the primary one in every record: one of kind `held_out_variant` and one of kind `seed`. Across all twenty-two records that is 44 held-out runs. **26 reached their threshold** — every held-out run attached to a record whose primary target was reached, including both of the C-API-SURFACE records, where the surface violation did not stop either held-out run. **18 did not reach**: 9 of kind `held_out_variant` and 9 of kind `seed`, exactly the nine zero-reward records, and in every one of those the runs were stopped by **C-TARGET-REACHED** and **C-BUDGET-RESPECTED** together. By kind, the pattern is completely symmetric — the `held_out_variant` runs and the `seed` runs succeed and fail in lockstep with the primary run, never independently. No record has ever shown 1 of 2 perturbations reaching. The practical implication: there is no evidence of a robustness gap specific to seed variation or to the held-out variant. If the primary configuration converges, the held-out runs converge too. Spend no budget on seed-hardening or variant-hardening as a separate concern; spend it on the primary run reaching its threshold quickly.

**Reconstruct the attempt-5 configuration and shave the budget.** Attempt 5 is the target: reward 0.9128 with a qualifying budget of 25.34 s, `compute_efficiency` 0.7728, `per_step_cost_ratio` 0.9887, clean conformance, `task_pass` 1.0. Attempt 11 shows that at the same ~25.3 s budget, driving `per_step_cost_ratio` from 1.05 down toward 0.99 and `compute_efficiency` from 0.70 up to 0.77 was worth about +0.015. Attempt 5's `per_step_cost_ratio` of 0.9887 is by no means the lowest observed — attempt 20 reached 0.6145 and attempt 21 reached 0.6826. The clear untried point in the space is **attempt 5's ~25 s budget combined with attempt 20's per-step cost profile**: keep the fast-converging schedule that produces a threshold-crossing row inside 25–30 s, and make the individual steps cheaper (smaller batches per step, lighter per-step bookkeeping, fewer redundant evaluations inside the loop) without extending the number of steps. If the two effects compose the way attempts 5-vs-11 and 4-vs-20 suggest, that is the most likely route past 0.9128.

**Probe below 25 seconds, but only once and carefully.** No attempt has ever produced a qualifying budget under 25.34 s. Three attempts cluster at 25.34–25.46 s, suggesting a floor was approached deliberately. Cutting further risks landing in the Class C basin where nothing crosses the threshold and the reward is 0.0000, so any such probe should retain a fallback: continue training past the intended stopping point if the threshold has not yet been crossed, so that a too-aggressive early stop degrades into a slower qualifying run rather than a zero.

**Stop the run the moment the qualifying row is produced.** Attempt 8's gap between wall clock and qualifying budget cost roughly 0.08. Every other scoring record has `wall_clock_sec` exactly equal to `qualifying_budget`, so terminating immediately on the threshold crossing is both achievable and standard in the good records.

**Keep the module surface clean.** Imports, constants, function and class definitions at module level only; everything executable inside a function. This is cheap insurance against the 0.14 penalty seen in attempts 1 and 6.

**Call: exploit.** The scoring family has not stopped improving — it has simply not been revisited in its best form. Attempt 5 (0.9128) and attempt 19 (0.9121) came from opposite ends of the budget range and scored the same, which means the two levers behind the reward (fast qualification and cheap efficient steps) have never been combined in a single submission. The next attempt should rebuild the fast-qualifying Class A trainer at a ~25–30 s qualifying budget, drive `per_step_cost_ratio` well below 0.99 toward the 0.61–0.68 range that has already been demonstrated elsewhere, terminate the instant the threshold-crossing row exists, and keep the module surface conformant. It should explicitly *not* re-enter the long-run regime: nine prior attempts scored 0.0000 by running to the ~1690 s cap without changing what caused the non-convergence, and that repetition is the single clearest waste in the record so far.
