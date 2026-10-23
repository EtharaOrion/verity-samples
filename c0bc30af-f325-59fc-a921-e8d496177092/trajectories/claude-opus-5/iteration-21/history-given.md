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

    All 15 attempts since have scored lower than it.
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
  15 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 18 -- reward 0.8794, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 49
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

All twenty records carry `measurement_status: "measured"`, so every one has a reward; none is a missing measurement. Ordered worst to best:

| Reward | Attempt(s) | Notes |
|---|---|---|
| 0.0000 | 3, 7, 9, 10, 12, 15, 16 | seven attempts, all `zero_reason_code: 4`, all with wall clock ≈1690–1693 s and `primary_target_reached: 0.0` |
| 0.5615 | 6 | `C-API-SURFACE` failed; wall clock 204.09 s |
| 0.6955 | 14 | clean checks; wall clock 99.74 s |
| 0.7551 | 8 | clean checks; qualifying budget 78.14 s but wall clock 151.50 s |
| 0.7684 | 1 | `C-API-SURFACE` failed; wall clock 25.46 s |
| 0.7919 | 17 | clean; 73.80 s |
| 0.8385 | 2 | clean; 73.62 s |
| 0.8451 | 13 | clean; 71.31 s |
| 0.8661 | 20 | clean; 62.46 s; `compute_efficiency` 1.0, `per_step_cost_ratio` 0.6145 |
| 0.8719 | 4 | clean; 50.03 s; `compute_efficiency` 1.0 |
| 0.8794 | 18 | clean; 49.33 s |
| 0.8980 | 11 | clean; 25.35 s |
| 0.9121 | 19 | clean; 45.81 s |
| 0.9128 | 5 | clean; 25.34 s — **highest reward, this is the one to beat** |

Attempt 5 (0.9128) holds the top score. Attempts 2, 4 and 5 were each marked `better_than_every_earlier_attempt` at the time they ran; every attempt after 5 was marked `worse_than_an_earlier_attempt`. That is the plain reading: attempts 6 through 20 are all regressions against attempt 5, including the near-miss 19 at 0.9121 and 11 at 0.8980, and including the seven zero-reward attempts. Nothing since attempt 5 has improved on it.

Detail worth carrying forward on the top band: attempt 5 scored 0.9128 with `compute_efficiency` 0.7728 and `per_step_cost_ratio` 0.9887 at 25.34 s; attempt 19 scored 0.9121 with `compute_efficiency` 0.9345 and `per_step_cost_ratio` 0.7669 at 45.81 s. So reward is not a pure function of wall clock — a run twice as long nearly tied the fastest one by being cheaper per step and more compute-efficient. Attempts 4 and 20 both reached `compute_efficiency` 1.0 and still scored below attempt 5 (0.8719 and 0.8661), so maximising compute efficiency alone does not top the board either.

# 2. Approach classes tried

The records contain metrics only, not source, so these classes are grouped by their measured signature. Four distinct classes appear.

**Class A — conforming trainer that converges quickly inside budget.** Thirteen attempts (2, 4, 5, 8, 11, 13, 14, 17, 18, 19, 20). `validity` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, no failed checks, `primary_target_reached` 1.0, `task_pass` 1.0, both declared perturbations reached. Rewards span 0.6955 to 0.9128. Within the class the reward tracks the qualifying budget and the per-step cost together: the 25 s runs (5, 11) and the 45–50 s runs (19, 18, 4) occupy the top, the 62–74 s runs (20, 2, 13, 17) the middle, and the 99–151 s runs (14, 8) the bottom. This is the only class that has ever produced a top-band score and is the class to build on.

**Class B — same trainer shape but with executable code at module import time.** Attempts 1 and 6. Both reached the primary target and both perturbations, yet both were penalised: `rule_conformance` 0.8571, `conformance_fraction` still 1.0, and `task_pass` forced to 0.0 despite `primary_target_reached` 1.0. Rewards 0.7684 and 0.5615. Attempt 1 ran in 25.46 s — essentially the same speed profile as the best-scoring attempt 5 — and still lost roughly 0.14 of reward to the conformance penalty alone. That comparison is the cleanest evidence available that the API-surface violation is pure lost value, not a side effect of anything else.

**Class C — long-running configuration that never crosses the threshold.** Seven attempts (3, 7, 9, 10, 12, 15, 16), all scoring 0.0000. Their signature is unmistakable and identical: wall clock 1690.4, 1690.9, 1690.5, 1691.5, 1692.2, 1692.5, 1692.9 s — a spread of under three seconds across seven runs, which is a hard ceiling being hit, not a training curve. `qualifying_budget` is `"not-measured"` in every one, `conformance_fraction` 0.0, `primary_target_reached` 0.0, `zero_reason_code` 4. Notably `rule_conformance` is 1.0 and `validity` is 1.0 in all seven, and `compute_efficiency` is high (0.9033–1.0): the code was well-formed and the per-step cost was fine. What failed was that the metric never crossed the declared threshold before the ceiling. Seven separate attempts produced this identical outcome, which means the loop repeatedly re-entered this class without changing the thing that causes it.

**Class D — converges, then keeps running.** Attempt 8, reward 0.7551. It is the only record where `wall_clock_sec` (151.50) diverges from `qualifying_budget` (78.14). It passed every check and both perturbations, but its reward sits below every Class A attempt that stopped at its qualifying point. The measured terms are consistent with work continuing after the qualifying row was produced, and that surplus wall clock costing reward. Treat "stop as soon as the target is demonstrably crossed" as a live lever.

# 3. Checks that failed

Four distinct check identifiers appear across the records.

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions."** Failed twice, in attempts 1 and 6. This is the finding that matters most among the conformance failures: two attempts separated by five intervening attempts, with wall clocks of 25.46 s and 204.09 s and compute efficiencies of 0.8160 and 0.6091 — wildly different runtime behaviour, identical violation and identical verifier reason. Whatever was changed between attempt 1 and attempt 6 is not what causes this check to fail. It is caused by the file having executable statements at module scope; the fix is to move all such code inside the permitted function/class definitions and leave only imports, constant assignments and definitions at module level. In both cases the penalty was visible and large: `rule_conformance` fell from 1.0 to 0.8571 and `task_pass` was zeroed even though the primary target was reached.

**`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction."** Failed seven times, in attempts 3, 7, 9, 10, 12, 15, 16, with the identical reason each time. Seven repeats means the differences between those seven submissions are not what causes this check to fail. Either the training does not reach the declared threshold at all within the ceiling, or the declared direction of the comparison does not match the metric being written into the evaluation rows. The latter is worth checking explicitly because `compute_efficiency` was near 1.0 in several of these runs, which is not the profile of a run that is simply too slow to learn.

**`C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists."** Failed seven times, in the same attempts 3, 7, 9, 10, 12, 15, 16. This is downstream of `C-TARGET-REACHED`, not an independent defect: with no row crossing the threshold there is no qualifying row and therefore no budget position to evaluate. It should resolve automatically once `C-TARGET-REACHED` holds, and it has never failed in any attempt where the target was reached.

**`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget."** Failed seven times, in the same seven attempts. Again always co-occurring with the target failure, never alone.

# 4. Ruled-out directions

**Leaving executable statements at module scope.** Ruled out by `C-API-SURFACE` failing on exactly this reason in attempts 1 and 6, costing `rule_conformance` (1.0 → 0.8571) and `task_pass` (1.0 → 0.0) in both. Attempt 1 matched the best attempt's ~25 s runtime yet scored 0.7684 against 0.9128. There is no upside here to trade against.

**Whatever configuration produces the ~1690 s non-converging run.** Ruled out by seven independent attempts (3, 7, 9, 10, 12, 15, 16) all scoring exactly 0.0000 on the same three checks. Re-entering this class is neither exploration nor exploitation — it is repeating an approach that scored zero without changing what made it score zero, and the record shows this happened seven times.

**Pushing wall clock high in the hope of a better metric.** Ruled out within the scoring class as well: attempt 14 at 99.74 s scored 0.6955, attempt 8 at 151.50 s scored 0.7551, attempt 6 at 204.09 s scored 0.5615 — all well below the 25–50 s band that produced 0.8719 through 0.9128. Longer runs have never bought a better reward here.

**Running past the qualifying point.** Ruled out by attempt 8, the sole record where wall clock (151.50 s) exceeds the qualifying budget (78.14 s). It passed every check and still landed at 0.7551, below every other clean attempt with a comparable qualifying budget.

**Maximising `compute_efficiency` as the primary objective.** Ruled out as a sufficient strategy: attempts 4 and 20 both achieved `compute_efficiency` 1.0 and scored 0.8719 and 0.8661, both below attempt 5's 0.9128 at `compute_efficiency` 0.7728. The metric is not the reward.

# 5. Open leads

**Held-out run outcomes, by kind and in aggregate.** Every record declared two perturbation units, one of kind `held_out_variant` and one of kind `seed`. Across the twenty records that is forty held-out runs. Twenty-six reached their threshold: thirteen of kind `held_out_variant` and thirteen of kind `seed`, in the thirteen attempts where the primary target was also reached, with no failed checks recorded on any of them. Fourteen did not reach: seven of kind `held_out_variant` and seven of kind `seed`, all in the seven zero-reward attempts, and each of those fourteen failed on the same two checks, `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. The pattern is complete and symmetric: neither kind has ever failed while the primary run succeeded, and both kinds fail together whenever the primary run fails. `all_perturbations_held` is true in exactly the thirteen scoring attempts and false in exactly the seven zero attempts. The practical consequence is that generalisation across seeds and across the held-out variant has never been the bottleneck — fixing the primary run has always carried the held-out runs with it — so effort should go to the primary run, not to robustness hardening.

**Reconstruct the attempt-5 profile and hold conformance.** The target to beat is 0.9128: a clean run, no failed checks, qualifying budget 25.34 s, `per_step_cost_ratio` 0.9887, `compute_efficiency` 0.7728. Attempt 11 reproduced almost exactly that budget (25.35 s) and scored 0.8980, so the fast-convergence recipe is reproducible but has some spread — roughly 0.015 of reward — between runs at the same budget. Start from the fast profile, not from a slow one.

**Combine attempt 5's short budget with attempt 19's cheaper steps.** Attempt 19 scored 0.9121 at 45.81 s with `per_step_cost_ratio` 0.7669 and `compute_efficiency` 0.9345 — nearly matching attempt 5 from a very different operating point. A run that keeps attempt 5's ~25 s budget while lowering `per_step_cost_ratio` toward 0.72–0.77 (the range seen in attempts 4, 17, 19 and 20) is the most concrete untried combination the data supports, since the two top scores achieve the same reward through opposite trade-offs.

**Terminate at the qualifying row.** Attempt 8 is the only demonstration that extra wall clock past the qualifying point is paid for. Making the run stop the moment the threshold is crossed in the declared direction is cheap to implement and protects the short-budget profile from drifting into the 70–150 s band that produced 0.6955–0.8451.

**Verify the declared direction of the threshold comparison before anything else.** The seven zero attempts share the reason "no evaluation row crosses the threshold in the declared direction" while retaining `rule_conformance` 1.0, `validity` 1.0 and high `compute_efficiency`. A direction or sign mismatch between the metric written into the evaluation rows and the declared threshold would produce exactly this signature, as would writing rows whose metric column is not the one being thresholded. Confirm this on the very first evaluation row rather than discovering it after the ~1690 s ceiling.

**Guard the module surface mechanically.** Before submitting, read the file back and confirm that every module-level node is an import, a constant assignment, or a permitted definition, with no bare calls, no `if __name__` block executing work, and no setup or seeding statements at module scope. This is the check that has failed twice for the same reason, and it is entirely preventable.

**Call: exploit.** The scoring class is not exhausted — the top three clean scores are 0.9128, 0.9121 and 0.8980, close enough that the difference is in budget and per-step cost rather than in the method — and the two failure modes that destroyed reward (`C-API-SURFACE` twice, `C-TARGET-REACHED` seven times) are both specific and named. Rebuild the Class A fast-convergence trainer at the ~25 s qualifying budget, drive `per_step_cost_ratio` down toward the 0.72–0.77 range, stop at the qualifying row, and keep the module surface free of executable statements. Do not re-enter the ~1690 s non-converging class without first changing the threshold-direction handling that produced it seven times.
