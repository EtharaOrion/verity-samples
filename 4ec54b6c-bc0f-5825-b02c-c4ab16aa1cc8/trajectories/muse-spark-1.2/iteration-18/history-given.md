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

    All 15 attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2 *      0.7155   1.000             2 of 2         yes             17                
  3        0.6279   1.000             2 of 2         yes             20                
  4        0.5792   1.000             2 of 2         yes             18                
  5        0.6587   1.000             2 of 2         yes             21                
  6        --       --                --             --              --                
  7        --       --                --             --              --                
  8        0.5444   1.000             2 of 2         yes             26                
  9        0.5164   0.857             2 of 2         yes             17                
  10       0.5983   1.000             2 of 2         yes             20                
  11       0.6639   1.000             2 of 2         yes             20                
  12       0.4962   1.000             1 of 2         yes             17                
  13       0.5590   1.000             2 of 2         yes             21                
  14       0.6426   1.000             2 of 2         yes             18                
  15       0.5830   1.000             2 of 2         yes             24                
  16       0.5701   1.000             2 of 2         yes             21                
  17       0.5274   0.857             2 of 2         yes             24                
  18       0.5755   1.000             2 of 2         yes             21                
  19       0.7134   1.000             2 of 2         yes             17                

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
  14 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 17 -- reward 0.5274, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 24
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 18 -- reward 0.5755, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.7134, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (9, 17). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Nineteen submissions were graded. Seventeen carry a measured reward; two produced no measurement at all.

Ordered worst to best by reward:

| Attempt | reward | note |
|---|---|---|
| 12 | 0.4962 | failed C-PERTURBATION-REACHED; task_pass 0.0 |
| 9 | 0.5164 | failed C-API-SURFACE; task_pass 0.0 |
| 17 | 0.5274 | failed C-API-SURFACE; task_pass 0.0 |
| 8 | 0.5444 | clean; slowest run measured (26.0978 s) |
| 13 | 0.5590 | clean |
| 16 | 0.5701 | clean |
| 18 | 0.5755 | clean |
| 4 | 0.5792 | clean |
| 15 | 0.5830 | clean |
| 10 | 0.5983 | clean |
| 3 | 0.6279 | clean |
| 14 | 0.6426 | clean |
| 5 | 0.6587 | clean |
| 11 | 0.6639 | clean |
| 1 | 0.6694 | clean; first measured attempt |
| 19 | 0.7134 | clean |
| 2 | 0.7155 | clean; best |

**Attempt 2 holds the highest reward, 0.7155, and it is the score to beat.** Attempt 19 is the second best at 0.7134 and is still below attempt 2.

Every attempt after attempt 2 that was measured came in lower than attempt 2. Stating that plainly, one by one: attempt 3 (0.6279), attempt 4 (0.5792), attempt 5 (0.6587), attempt 8 (0.5444), attempt 9 (0.5164), attempt 10 (0.5983), attempt 11 (0.6639), attempt 12 (0.4962), attempt 13 (0.5590), attempt 14 (0.6426), attempt 15 (0.5830), attempt 16 (0.5701), attempt 17 (0.5274), attempt 18 (0.5755) and attempt 19 (0.7134) are each a regression against the best so far, and the verifier labelled all of them `worse_than_an_earlier_attempt`. Nothing since attempt 2 has been an improvement.

Attempts 6 and 7 have `measurement_status: harbor_exception`. **They produced no measurement.** They did not score zero, they were never scored; every one of their terms is `not-measured` and they carry no `failed_checks`. Whatever they did is unknown from the record and cannot be counted for or against any approach.

Supporting terms on the measured runs. `red_line_crossed` is 0.0 and `zero_reason_code` is 0 on all seventeen — nothing has ever tripped a red line or been zeroed. `validity` is 1.0 on all seventeen. `primary_target_reached` is 1.0 on all seventeen, including the three that failed checks: the primary task target has never been the problem. `task_pass` is 1.0 on the fourteen clean runs and 0.0 only on attempts 9, 12 and 17 — the three runs with a failed check, and also three of the four lowest rewards. A failed check does not zero the reward; it costs roughly 0.05–0.17 of it.

The cost terms. `wall_clock_sec` equals `qualifying_budget` in every measured record, ranging 16.7808 s (attempt 12) to 26.0978 s (attempt 8). `compute_efficiency` and `per_step_cost_ratio` are near-reciprocal in every record — their product sits between 0.83 and 1.03 throughout — so they are two views of the same quantity and neither is an independent knob.

The strongest pattern in the data: the three highest rewards (0.7155, 0.7134, 0.6694) all come from runs of 17.4265 s, 17.4531 s and 17.4869 s with `per_step_cost_ratio` 1.51–1.58 and `compute_efficiency` 0.55–0.62. **No run longer than 20.0571 s has ever exceeded 0.6639.** The relationship is not deterministic, though: attempt 4 sat in the same 17.5 s band and scored only 0.5792, and attempts 1, 2 and 19 have near-identical cost profiles yet spread 0.6694 to 0.7155. There is a quality component driving reward that these terms do not expose.

## 2. Approach classes tried

The record supplies measured terms only, not source, so the classes below are grouped by the cost and conformance signature each submission produced. Records with the same signature and the same outcome are one entry.

**Class A — fast-band configuration, ~17.4–17.8 s, per-step cost ratio ~1.51–1.63, compute efficiency ~0.55–0.63.** Attempts 1 (0.6694), 2 (0.7155), 19 (0.7134), 14 (0.6426), and attempt 4 (0.5792, but see class D — its cost ratio was 1.1656, not in this range). This class contains every reward above 0.70 and is the best-performing class by a clear margin. Attempts 9 (17.1217 s) and 12 (16.7808 s) also fall in this time band but were spoiled by failed checks, so their rewards say nothing about the class.

**Class B — mid-band configuration, ~20.0–21.0 s, cost ratio ~1.02–1.63.** Attempts 11 (0.6639), 10 (0.5983), 3 (0.6279), 5 (0.6587), 13 (0.5590), 18 (0.5755), 16 (0.5701). Seven data points, best of them 0.6639, mean around 0.607. This class has never come close to attempt 2.

**Class C — long-budget configuration, ~23.5–26.1 s.** Attempts 15 (0.5830), 8 (0.5444) and 17 (23.5810 s, spoiled by C-API-SURFACE, 0.5274). Uniformly the weakest measured region.

**Class D — per-step-cost minimisation / efficiency maximisation, cost ratio ≤1.17 and compute efficiency ≥0.84.** Attempts 8 (efficiency 0.9679, ratio 0.9674, reward 0.5444), 4 (0.8832 / 1.1656, 0.5792), 16 (0.8684 / 1.1256, 0.5701), 11 (0.8424 / 1.0166, 0.6639), 13 (0.7642 / 1.2404, 0.5590), 17 (0.8228 / 1.2123, spoiled). This class drove the reported efficiency almost to 1.0 and drove reward down. Attempt 8, the most compute-efficient submission ever measured, is the fourth-worst reward on record and also took the longest wall clock — pushing per-step cost down lengthened the run.

**Class E — submissions with module-level executable code.** Attempts 9 and 17. Both failed C-API-SURFACE, both had `task_pass` forced to 0.0 and `rule_conformance` cut to 0.8571 (6 of 7). Rewards 0.5164 and 0.5274.

**Class F — aggressively shortened run.** Attempt 12, the fastest submission at 16.7808 s. It broke the held-out perturbation and scored 0.4962, the worst reward on record.

**Class G — two submissions that never reached measurement.** Attempts 6 and 7, both `harbor_exception`. No terms, no reward, no failed checks. Nothing can be inferred about their approach.

## 3. Checks that failed

Two named checks have ever failed on the primary submission, plus two more inside a perturbation unit.

**C-API-SURFACE — "module-level statements outside imports, constants, and permitted definitions".** Failed twice: attempt 9 and attempt 17. **This is the finding that matters most.** It has now failed on two separate submissions, and whatever was changed between attempt 9 and attempt 17 — the cost profile moved substantially, from 17.1217 s / efficiency 0.6647 to 23.5810 s / efficiency 0.8228, so the training body was materially rewritten — is not what is causing it. The cause is exactly what the reason names: executable statements sitting at module level in the submission file. Both times it set `rule_conformance` to 0.8571 and `task_pass` to 0.0 even though `primary_target_reached` stayed 1.0 and both perturbation units held. The fix is mechanical and unrelated to the learning algorithm: at module scope, permit only imports, constant assignments and `def`/`class` definitions; move every other statement inside a function.

**C-PERTURBATION-REACHED — "1 of 2 declared perturbations reached their own threshold inside their own budget".** Failed once, attempt 12. `conformance_fraction` fell to 0.5, `all_perturbations_held` went false, `task_pass` went to 0.0, reward 0.4962, the lowest measured.

**C-TARGET-REACHED and C-BUDGET-RESPECTED.** These two failed together inside a single perturbation unit on attempt 12 and nowhere else. They are the unit-level cause behind that record's C-PERTURBATION-REACHED failure.

On all fourteen other measured attempts, `failed_checks` is empty, `conformance_fraction` is 1.0 and `rule_conformance` is 1.0.

## 4. Ruled-out directions

**Minimising per-step compute cost / maximising the reported `compute_efficiency`.** Ruled out as a reward lever. The four submissions with efficiency ≥0.84 scored 0.5444, 0.5792, 0.5701 and 0.6639 — a mean well below the fast-band class and none of them near attempt 2's 0.7155. The extreme case, attempt 8 at efficiency 0.9679 and per-step cost ratio 0.9674, scored 0.5444. Meanwhile the best reward on record, attempt 2, has efficiency 0.6205 and cost ratio 1.5175 — an unremarkable per-step cost. Because efficiency and cost ratio are near-reciprocals in every record, tuning one is tuning the other, and neither tracks reward.

**Long-budget training, wall clock ≥20 s.** Ruled out. Ten measured runs sit at or above 20.0571 s and the best of them is 0.6639; the mean is near 0.59. Every reward above 0.70 came from a run in the 17.43–17.49 s band. Spending more wall clock has not once bought reward.

**Submissions with any module-level executable statement.** Ruled out by C-API-SURFACE failing twice, on attempts 9 and 17, each time zeroing `task_pass` and dropping conformance to 6 of 7 while the underlying training itself hit its primary target and held both perturbations. This is pure lost reward.

**Cutting wall clock below ~17 s.** Ruled out. Attempt 12 was the only submission under 17 s (16.7808 s) and it is the only one whose held-out perturbation unit failed, on C-TARGET-REACHED and C-BUDGET-RESPECTED together, giving the worst reward on record, 0.4962. There is a floor: the held-out variant needs enough budget to reach its own threshold.

**Treating attempts 6 and 7 as evidence about any approach.** Ruled out for lack of data — they are `harbor_exception` with every term `not-measured`. Whatever they contained produced no measurement, and it would be a mistake to read them as failures of a technique.

## 5. Open leads

**Reconstruct the attempt-2 profile as the base.** Target: wall clock ≈17.45 s, per-step cost ratio ≈1.52, compute efficiency ≈0.62, no failed checks, both perturbations reached. That configuration produced 0.7155 and attempt 19's near-twin produced 0.7134, so the profile reproduces roughly. Treat ~17.5 s as the working ceiling and ~17.1 s as the floor.

**Attack the unobserved quality component, not the cost terms.** Attempts 1, 2 and 19 have nearly identical cost signatures and rewards of 0.6694, 0.7155 and 0.7134 — a spread of 0.046 that no reported term explains. Reward is evidently sensitive to something like the margin by which the primary target and each perturbation threshold are cleared, or to run-to-run variance. Concretely worth trying inside the fixed ~17.5 s budget: deterministic seeding to remove the lottery; better initialisation, learning-rate schedule or normalisation so the model clears its target earlier and by more; and stopping as soon as the target is comfortably cleared rather than consuming the remaining budget.

**The held-out variant is the only perturbation kind that has ever failed.** Aggregating the perturbation units across the seventeen measured records: 34 units ran, 33 reached their threshold. Of the seventeen `ruleset` units, all seventeen reached — that kind has never failed a check. Of the seventeen `held_out_variant` units, sixteen reached and one did not, failing C-TARGET-REACHED and C-BUDGET-RESPECTED. So the generalisation risk lives entirely in the held-out-variant kind, and the failure mode is not reaching its target inside its own budget. Protect it with regularisation and fast early convergence rather than extra steps, since extra steps cost the wall clock that correlates with lower reward.

**Enforce the API surface mechanically before submitting.** Keep module scope to imports, constants and definitions only; wrap any setup, logging, seeding or configuration in a function called from the entry point. This has cost two attempts already and is free to prevent.

**Keep the submission simple enough not to provoke a harbor exception.** Two submissions never reached measurement. The cause is not in the record, so the only defensible mitigation is to avoid unusual constructs, heavy imports or anything at import time that could abort the harness, and to keep the file close in shape to the ones that measured cleanly.

## Call: exploit

Exploit. The fast-band class has produced every reward above 0.70 and has not been exhausted — the 0.046 spread between attempt 2 (0.7155) and attempt 1 (0.6694) at essentially identical cost profiles says there is headroom inside it that nothing yet has deliberately targeted. Rebuild attempt 2's profile and improve the quality margin within a ~17.5 s budget, while mechanically guarding C-API-SURFACE and leaving the held-out variant enough budget to reach its threshold.

One caution for the next attempt, since it is visible in the history: the mid-band and efficiency-maximising configurations were tried repeatedly — attempts 3, 5, 10, 13, 16, 18 in the 20 s band and 4, 8, 11, 16 in the high-efficiency band — and each time came back below attempt 2 without the changed variable being the one that mattered. Do not re-enter those regions.
