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

    All 12 attempts since have scored lower than it.
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
  11 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 4 -- reward 0.8719, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 15 -- reward 0.0000, worse than an earlier attempt
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

    attempt 16 -- reward 0.0000, worse than an earlier attempt
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

    attempt 17 -- reward 0.7919, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 7 attempts (3, 7, 9, 10, 12, 15, 16). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 7 attempts (3, 7, 9, 10, 12, 15, 16). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 7 attempts (3, 7, 9, 10, 12, 15, 16). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Seventeen graded submissions, all with `measurement_status: "measured"` — every one carries a reward, so none needs to be reported as unmeasured. Listed worst to best:

- **Attempts 3, 7, 9, 10, 12, 15 and 16 — reward 0.0000 each.** Seven separate attempts, all failing identically (see Section 3). Each ran to ~1690–1693 s of wall clock (1692.5152, 1692.2115, 1692.9717, 1690.9593, 1690.4476, 1690.4794, 1691.5261) with `zero_reason_code: 4`, `primary_target_reached: 0.0`, `conformance_fraction: 0.0`. Note that all seven still had `rule_conformance: 1.0`, `validity: 1.0` and `red_line_crossed: 0.0` — the code was well-formed and legal; it simply never produced an evaluation row that crossed the threshold before time ran out.
- **Attempt 6 — reward 0.5615.** Lower than every earlier scoring attempt; `standing_against_best_so_far: worse_than_an_earlier_attempt`. Target reached (`primary_target_reached: 1.0`) but `task_pass: 0.0` because `C-API-SURFACE` failed; `rule_conformance: 0.8571`; wall clock 204.0885 s, `per_step_cost_ratio: 1.3778`, `compute_efficiency: 0.6091`.
- **Attempt 14 — reward 0.6955.** Lower than earlier attempts. Fully clean (no failed checks, `task_pass: 1.0`), but slow: qualifying budget 99.7374 s.
- **Attempt 8 — reward 0.7551.** Lower than earlier attempts. Clean, `task_pass: 1.0`, qualifying budget 78.1441 s but wall clock 151.5049 s — the only clean attempt where wall clock far exceeds the qualifying budget.
- **Attempt 1 — reward 0.7684.** First measured attempt. Fast (25.4619 s) and target reached, but `C-API-SURFACE` failed, `rule_conformance: 0.8571`, `task_pass: 0.0`.
- **Attempt 17 — reward 0.7919.** Lower than earlier attempts. Clean, qualifying budget 73.7980 s.
- **Attempt 2 — reward 0.8385.** Clean, `task_pass: 1.0`, qualifying budget 73.6235 s. Was `better_than_every_earlier_attempt` at the time.
- **Attempt 13 — reward 0.8451.** Lower than the then-best. Clean, qualifying budget 71.3146 s.
- **Attempt 4 — reward 0.8719.** Clean, qualifying budget 50.0341 s, `compute_efficiency: 1.0`. Was `better_than_every_earlier_attempt` at the time.
- **Attempt 11 — reward 0.8980.** Lower than the best. Clean, qualifying budget 25.3479 s.
- **Attempt 5 — reward 0.9128. This is the highest reward recorded and the one to beat.** Clean (`failed_checks: []`, `rule_conformance: 1.0`, `task_pass: 1.0`, `all_perturbations_held: true`), qualifying budget and wall clock both 25.3436 s, `compute_efficiency: 0.7728`, `per_step_cost_ratio: 0.9887`.

The single clearest signal across the ten scoring attempts is that reward tracks **time-to-target**, not raw efficiency metrics. Ranking the clean attempts by qualifying budget reproduces the reward ranking almost exactly: 25.34 s → 0.9128, 25.35 s → 0.8980, 50.03 s → 0.8719, 71.31 s → 0.8451, 73.62 s → 0.8385, 73.80 s → 0.7919, 78.14 s (151.50 s wall) → 0.7551, 99.74 s → 0.6955. Meanwhile `compute_efficiency: 1.0` (attempt 4) did **not** produce the top reward and `per_step_cost_ratio` below 1.0 did not either — attempt 17 had a better per-step cost ratio (0.7318) than attempt 2 (0.9162) at nearly identical wall clock and scored lower. Do not optimise `per_step_cost_ratio` or `compute_efficiency` as a proxy; optimise wall-clock time to first threshold-crossing evaluation row while keeping every conformance check green.

# 2. Approach classes tried

The submission source is not carried forward, so these classes are grouped by their measured signature. Four distinct classes are visible:

**Class A — fast converger, fully conformant (~25 s to target).** Attempts 5 (0.9128) and 11 (0.8980). Target reached, both declared perturbations held, no failed checks, wall clock ≈ qualifying budget ≈ 25.3 s. This class contains both of the top two results and is the productive region.

**Class B — mid-budget converger, fully conformant (50–100 s to target).** Attempts 4 (0.8719, 50.03 s), 13 (0.8451, 71.31 s), 2 (0.8385, 73.62 s), 17 (0.7919, 73.80 s), 8 (0.7551, 78.14 s qualifying / 151.50 s wall), 14 (0.6955, 99.74 s). Everything here passes every check and reaches the target on the primary run and on both held-out runs; it simply takes longer and is paid less. Reward decays roughly monotonically with the time taken. Attempt 8 is the informative member: its wall clock (151.50 s) is nearly double its qualifying budget (78.14 s), and it scores below attempts with a similar qualifying budget but no such gap (2 at 73.62 s → 0.8385, 17 at 73.80 s → 0.7919), so post-target or non-qualifying work still costs reward.

**Class C — converges but violates the module surface rule.** Attempts 1 (0.7684) and 6 (0.5615). Both reached the primary target and both held both perturbation runs, yet both scored `task_pass: 0.0` and `rule_conformance: 0.8571` (6 of 7 rules) because `C-API-SURFACE` failed. Attempt 1 is the crucial data point: at 25.4619 s it was as fast as the best-ever Class A runs but scored 0.7684 instead of ~0.91. The `C-API-SURFACE` violation alone costs on the order of 0.14 reward at equal speed.

**Class D — never converges, hits the harness time ceiling.** Attempts 3, 7, 9, 10, 12, 15, 16 — seven attempts, all 0.0000. Each terminated at ~1692 s of wall clock (the values cluster in 1690.45–1692.97 s, which is almost certainly a hard harness cap rather than a chosen stopping point). In every case `qualifying_budget` is `"not-measured"`, `conformance_fraction` is 0.0, and `zero_reason_code` is 4. These runs were syntactically and legally fine (`rule_conformance: 1.0`, `validity: 1.0`, `red_line_crossed: 0.0`); they trained for the full allowed time and never logged an evaluation row past the threshold in the declared direction.

Seven of the seventeen attempts — a plurality — landed in Class D, repeatedly, with the identical failure triple. That is the pattern of re-running a zero-scoring approach without changing what makes it score zero, and it should not be repeated.

# 3. Checks that failed

**`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction". Failed 7 times**, on attempts 3, 7, 9, 10, 12, 15, 16. This is the dominant failure of the whole record. Whatever was varied between those seven attempts is not what causes it: their `per_step_cost_ratio` ranges from 0.7237 to 0.8901 and their `compute_efficiency` from 0.9033 to 1.0000, all of them look efficient, and all seven still fail this check after ~1692 s. The cause is not per-step cost and not the efficiency knobs; it is either that the run never gets far enough to evaluate within the ceiling, or that the metric being written out is not compared in the declared direction / against the declared threshold. Both possibilities must be checked explicitly, because seven attempts of tuning failed to move it.

**`C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists". Failed 7 times**, on the same attempts 3, 7, 9, 10, 12, 15, 16. This is strictly downstream of `C-TARGET-REACHED`: with no threshold-crossing row there is nothing to position against the budget. It is not an independent problem and does not need a separate fix; fixing `C-TARGET-REACHED` resolves it.

**`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed 7 times**, on the same seven attempts. Also downstream — all-or-nothing alongside the primary run in every record.

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions". Failed 2 times**, on attempts 1 and 6. These two attempts are far apart in every other respect (25.46 s vs 204.09 s wall clock, `per_step_cost_ratio` 1.0639 vs 1.3778, reward 0.7684 vs 0.5615), so whatever was changed between them is not what causes this check to fail. The cause is structural and literal: executable statements at module scope. Only imports, constant assignments, and permitted definitions (functions/classes) may appear at the top level. Any setup work, device selection, seeding, config construction, print/logging call, `if`/`try` block, or `if __name__ == "__main__":` guard placed at module level trips it; all such work must be moved inside a function body. Every attempt that scored above 0.79 had `failed_checks: []`, so keeping this green is a precondition for competing.

# 4. Ruled-out directions

**Running to the harness time ceiling.** Seven attempts (3, 7, 9, 10, 12, 15, 16) consumed ~1690–1693 s and each returned exactly 0.0000. Meanwhile every attempt that finished inside ~205 s scored. Long training schedules are ruled out by direct measurement: the harness caps the run and an uncrossed threshold at the cap is worth nothing at all, regardless of how good the trajectory looked.

**Optimising `compute_efficiency` as the objective.** Attempt 4 achieved `compute_efficiency: 1.0` and scored 0.8719, below attempt 5's 0.9128 at `compute_efficiency: 0.7728`. Four of the seven zero-scoring attempts also had `compute_efficiency` ≥ 0.93, including two at exactly 1.0. High compute efficiency neither implies nor produces high reward.

**Optimising `per_step_cost_ratio` downward as the objective.** Attempt 17 (0.7318) scored 0.7919 while attempt 2 (0.9162) scored 0.8385 at essentially the same qualifying budget; attempt 11 with a ratio above 1.0 (1.0502) scored 0.8980. Cheaper steps that take more of them do not pay. The zero-scoring class had ratios between 0.72 and 0.89 — cheap steps, no result.

**Leaving executable code at module scope.** Ruled out by the two `C-API-SURFACE` failures. Attempt 1 shows the cost concretely: same ~25.4 s speed class as the best result, but 0.7684 instead of ~0.91, and `task_pass` forced to 0.0 despite the target actually being reached. There is no version of this trade worth taking.

**Doing significant work after the target is crossed.** Attempt 8's wall clock (151.5049 s) is roughly twice its qualifying budget (78.1441 s), and it scored 0.7551 — below attempts 2 and 17 which had comparable qualifying budgets and no wall-clock overhang. Extra post-qualification work is charged.

**Long budgets in the 100–205 s band.** Attempt 14 (99.74 s → 0.6955) and attempt 6 (204.09 s → 0.5615) are the two worst scoring results. Even fully conformant, this band cannot reach 0.9128.

# 5. Open leads

**Reproduce the ~25 s conformant configuration.** Attempts 5 (0.9128), 11 (0.8980) and 1 (25.4619 s, but `C-API-SURFACE`-broken) all reached the target in ~25.3–25.5 s. Three independent attempts landing in that band suggests a stable convergence point rather than luck. Rebuild for that band first, verify `failed_checks` is empty, and treat 0.9128 as the bar.

**Push the qualifying budget below 25 s.** The reward-versus-time curve through the clean attempts (25.34 s → 0.9128, 50.03 s → 0.8719, 71.31 s → 0.8451, 99.74 s → 0.6955) is steep and has not been probed below 25 s. Nothing in the record establishes a floor there. Shortening the schedule — fewer epochs, higher learning rate with a short warmup, larger batch, early-exit as soon as an evaluation row crosses the threshold with a small safety margin — is the most direct route above 0.9128. The two hard constraints are that the primary run and *both* declared perturbation runs must each cross their own threshold inside their own budget, so any speed-up must keep a margin large enough to survive a different seed and a held-out variant.

**Stop the moment the target is crossed.** Attempt 8's 73 s of post-qualification wall clock cost it visibly. Evaluate frequently, compare against the threshold in the declared direction after each evaluation, and return immediately on the first crossing rather than finishing a fixed schedule.

**Guarantee `C-API-SURFACE` by construction.** Before submitting, read the module top to bottom and confirm that every top-level line is an `import`, a constant assignment, a `def`, or a `class`. No module-level configuration, seeding, device probing, logging, or `__main__` guard. This has cost two attempts already and is entirely mechanical to prevent.

**Confirm the evaluation row is written in the declared direction and comparable to the threshold.** Seven attempts failed `C-TARGET-REACHED` with the reason "no evaluation row crosses the threshold in the declared direction" — a phrasing that admits both "never good enough" and "never compared correctly". Since the fast configurations pass this check trivially, the cheap defensive move is to emit evaluation rows early and often (including one very early in training) so that a directional or naming mismatch shows up as a failure at 25 s rather than at the 1692 s ceiling.

**Held-out run behaviour (report by kind and in aggregate).** Every record declared exactly 2 perturbations, one of kind `held_out_variant` and one of kind `seed`. Across the seventeen records that is 17 `held_out_variant` runs and 17 `seed` runs, 34 in total. In the ten scoring attempts, both kinds reached their thresholds with no failed checks: 10 of 10 `held_out_variant` reached, 10 of 10 `seed` reached, 20 of 20 in aggregate, and `all_perturbations_held` was `true`. In the seven zero-scoring attempts, both kinds failed together: 7 of 7 `held_out_variant` failed, 7 of 7 `seed` failed, 14 of 14 in aggregate, each one stopped by the same two checks, `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. Neither kind is the weak one — no `held_out_variant` has ever failed while its accompanying `seed` run passed, or vice versa. The held-out runs fail exactly when the primary run fails, and on the same checks, so robustness across seeds or across the variant is not a separate problem to solve; the primary convergence is the whole of it. (These runs are unidentified, so nothing here tracks any individual run across records.)

**Verdict: exploit.** The scoring approaches have not exhausted themselves — the top region (Class A, ~25 s, fully conformant) has been reached three times and never probed below 25 s, and the reward-versus-time gradient there is steep and unexplored. Take the ~25 s conformant configuration that produced 0.9128, keep `failed_checks` empty (especially `C-API-SURFACE`), cut time-to-target further with an immediate exit on the first threshold crossing, and keep enough margin that both the `seed` and `held_out_variant` runs still cross. Explicitly do not re-run any long-schedule configuration: seven attempts have now taken that path to the ~1692 s ceiling and returned 0.0000 each time, and re-running it without changing the convergence speed or the evaluation-row emission is neither exploration nor exploitation.
