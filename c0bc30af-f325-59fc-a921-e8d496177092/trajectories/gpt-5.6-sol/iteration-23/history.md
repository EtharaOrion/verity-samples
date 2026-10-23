# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 20 -- reward 0.8670, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All three attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3        0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                
  5        0.8658   1.000             2 of 2         yes             74                
  6        0.7580   0.857             2 of 2         yes             46                
  7        0.4911   1.000             1 of 2         yes             50                
  8        0.7805   1.000             2 of 2         yes             99                
  9        0.8332   1.000             2 of 2         yes             50                
  10       0.8503   1.000             2 of 2         yes             75                
  11       0.8067   1.000             2 of 2         yes             74                
  12       0.4275   1.000             1 of 2         yes             74                
  13       0.8657   1.000             2 of 2         yes             74                
  14       0.8513   1.000             2 of 2         yes             74                
  15       0.8579   1.000             2 of 2         yes             74                
  16       0.7005   1.000             2 of 2         yes             75                
  17       0.8655   1.000             2 of 2         yes             76                
  18       0.8368   1.000             2 of 2         yes             74                
  19       0.4278   1.000             1 of 2         yes             74                
  20 *     0.8670   1.000             2 of 2         yes             74                
  21       0.0000   1.000             0 of 2         no              --                
  22       0.8594   1.000             2 of 2         yes             70                
  23       0.8170   1.000             2 of 2         yes             95                

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
  17 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 5 -- reward 0.8658, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 21 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 2 of your last 4 attempts
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 22 -- reward 0.8594, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 70
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 23 -- reward 0.8170, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 95
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-BUDGET-RESPECTED failed on attempt 21.
    C-PERTURBATION-REACHED has failed on 4 attempts (7, 12, 19, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 21.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All 23 graded records carry `measurement_status: "measured"`, so every one of them has a reward. None produced "no measurement". One of them scored a true 0.0000 (attempt 21) — that is a measured zero, not an absent measurement.

Ranked worst to best by reward:

| Rank | Attempt | Reward | Notes |
|---|---|---|---|
| 1 (worst) | 21 | 0.0000 | `zero_reason_code: 4`; primary target never reached; wall clock 1691.67 s vs. the ~74 s typical of every other run |
| 2 | 12 | 0.4275 | held-out perturbation did not reach |
| 3 | 19 | 0.4278 | held-out perturbation did not reach |
| 4 | 7 | 0.4911 | held-out perturbation did not reach |
| 5 | 16 | 0.7005 | all checks held; low-cost profile, but quality term collapsed |
| 6 | 6 | 0.7580 | `C-API-SURFACE` failure; `rule_conformance` 0.857, `task_pass` 0 |
| 7 | 4 | 0.7740 | all checks held |
| 8 | 8 | 0.7805 | all checks held; wall clock 98.60 s |
| 9 | 11 | 0.8067 | all checks held; `compute_efficiency` 1.0 |
| 10 | 2 | 0.8079 | all checks held |
| 11 | 23 | 0.8170 | all checks held; wall clock 94.75 s |
| 12 | 9 | 0.8332 | all checks held; qualifying budget 49.89 s |
| 13 | 18 | 0.8368 | all checks held |
| 14 | 10 | 0.8503 | all checks held |
| 15 | 14 | 0.8513 | all checks held |
| 16 | 15 | 0.8579 | all checks held |
| 17 | 22 | 0.8594 | all checks held |
| 18 | 1 | 0.8630 | first measured attempt |
| 19 | 17 | 0.8655 | all checks held |
| 20 | 13 | 0.8657 | all checks held (0.8656561) |
| 21 | 3 | 0.8657 | all checks held (0.8657110) |
| 22 | 5 | 0.8658 | all checks held |
| 23 (best) | 20 | 0.8670 | all checks held; `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013 |

**Attempt 20 holds the highest reward at 0.8670 and is the attempt to beat.**

Direction of movement, stated plainly: only four records ever set a new best — attempt 1 (0.8630, first measured), attempt 3 (0.8657), attempt 5 (0.8658), attempt 20 (0.8670). Every other record carries `standing_against_best_so_far: "worse_than_an_earlier_attempt"`. That includes the long tail after attempt 5 — attempts 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 were each **lower** than the then-best, not incremental progress toward it; attempts 21, 22 and 23 after the new best were likewise **lower** than 0.8670. Attempt 21 in particular is a regression from 0.8670 all the way to 0.0000.

The top five rewards (0.8655, 0.8657, 0.8657, 0.8658, 0.8670) span 0.0015. Treat that band as a plateau: differences inside it are not reliably meaningful signal.

# 2. Approach classes tried

No source code was carried into this summary; the classes below are grouped by the measured cost/efficiency signature (`per_step_cost_ratio`, `compute_efficiency`, `wall_clock_sec`, `qualifying_budget`), which is what the terms actually distinguish. Two records with the same signature and the same outcome are one entry.

**Class A — baseline per-step cost, ~74 s budget.** `per_step_cost_ratio` ≈ 0.94–1.07, `compute_efficiency` ≈ 0.68–0.75, qualifying budget ≈ 70–76 s. Attempts 1, 2, 3, 5, 9, 10, 13, 17, 22. Rewards 0.8079 to 0.8658. This is the most-sampled class and the most reliable: every member passed all checks and all perturbations. Its top members (3, 5, 13, 17) sit at 0.8655–0.8658, i.e. the plateau. It does not contain the current best.

**Class B — reduced per-step cost (a cheaper step, roughly 30 % off).** `per_step_cost_ratio` ≈ 0.69–0.71, `compute_efficiency` ≈ 0.96–1.00. Attempts 4 (0.7740), 11 (0.8067), 14 (0.8513), 16 (0.7005), 20 (0.8670), and 19 (0.4278, perturbation failure). This class is the only one that has ever beaten the Class A plateau — attempt 20 did it — but it is also the highest-variance class by a wide margin, spanning 0.7005 to 0.8670 among the runs where every check held. Cutting per-step cost by itself does not buy reward: attempt 11 achieved `compute_efficiency` 1.0 and still scored 0.8067, below Class A's typical result, and attempt 16 achieved 0.9805 efficiency for 0.7005. Something other than cost — a solution-quality margin the supplied terms do not expose directly — is what separates 20 from 16.

**Class C — intermediate cost.** `per_step_cost_ratio` ≈ 0.74–0.81, `compute_efficiency` ≈ 0.85–0.89. Attempts 18 (0.8368), 23 (0.8170), 12 (0.4275, perturbation failure). Attempt 15 is a near-neighbour with an unusual pairing of high efficiency (0.9355) and near-baseline cost ratio (0.9424), scoring 0.8579. No member of this class reached the plateau; it looks strictly dominated.

**Class D — longer wall clock.** Attempts 8 (98.60 s, ratio 1.085, 0.7805) and 23 (94.75 s, 0.8170). Spending more wall clock reduced reward relative to the ~74 s runs.

**Class E — tightened declared budget.** Attempts 9 and 7 both declared/qualified near 50 s (49.89 s and 50.05 s) while the primary still ran to ~74 s in attempt 9's case. Attempt 9 held everything but scored 0.8332, below the plateau; attempt 7 lost the held-out perturbation on `C-BUDGET-RESPECTED` and scored 0.4911. Tightening the budget bought nothing and cost robustness.

**Class F — module-level execution.** Attempt 6 only: `rule_conformance` 0.857, `task_pass` 0, reward 0.7580, with a `qualifying_budget` of 45.82 s against 70.37 s wall clock and an inflated `per_step_cost_ratio` of 1.4094. Distinct from every other record in that its failure was structural, not numeric.

**Class G — heavyweight / non-converging regime.** Attempt 21 only: 1691.67 s wall clock, ~23× the typical run, `primary_target_reached` 0.0, `qualifying_budget` "not-measured", reward 0.0000, `zero_reason_code` 4. Whatever was scaled up here never crossed the threshold at all.

# 3. Checks that failed

**`C-PERTURBATION-REACHED` — failed in 4 records: attempts 7, 12, 19 and 21.** Verifier reason in 7, 12 and 19: "1 of 2 declared perturbations reached their own threshold inside their own budget". In 21: "0 of 2 declared perturbations reached their own threshold inside their own budget". This is the single most important finding in the record set. Those four attempts sit in three different cost classes — `per_step_cost_ratio` 0.9657, 0.8114, 0.6884 and 0.6727; `compute_efficiency` 0.6954, 0.8464, 1.0000 and 0.9829 — so **whatever was changed between those attempts is not what is causing this check to fail.** Per-step cost tuning is not the discriminator. Every time this check failed, `conformance_fraction` dropped to 0.5 (or 0.0) and `task_pass` went to 0, and reward roughly halved to 0.4275–0.4911 (or, in attempt 21, to zero). It is worth about 0.44 of reward — far more than any efficiency gain observed anywhere in the data.

**`C-BUDGET-RESPECTED` — failed in 4 records: attempts 7, 12, 19 and 21**, at the perturbation-run level in all four, and additionally as a primary-level check in attempt 21 with the reason "no qualifying row, so no budget position exists". At the perturbation level it is always the accompanying symptom of a held-out run that did not finish inside its own budget position.

**`C-TARGET-REACHED` — failed in 3 records: attempts 12, 19 and 21**, at the perturbation-run level, and additionally as a primary-level check in attempt 21 with the reason "no evaluation row crosses the threshold in the declared direction". Attempt 7 is the one case where the held-out run failed budget *without* also failing target — it got there, just not inside the budget position.

**`C-API-SURFACE` — failed once, attempt 6.** Reason: "module-level statements outside imports, constants, and permitted definitions". It has not recurred; it is a one-off structural violation, and it cost `task_pass` outright (0) and dropped `rule_conformance` to 0.857 for a reward of 0.7580.

In 19 of the 23 records, `failed_checks` was empty and `rule_conformance`, `validity` and `conformance_fraction` were all 1.0. `red_line_crossed` was 0.0 in every single record, including attempt 21 — nothing has ever tripped a red line.

# 4. Ruled-out directions

- **Raising `compute_efficiency` / cutting `per_step_cost_ratio` as an end in itself.** Ruled out as a reward lever on its own. Attempt 11 reached `compute_efficiency` 1.0000 with every check held and scored 0.8067; attempt 16 reached 0.9805 and scored 0.7005; attempt 4 reached 0.9681 and scored 0.7740. All three are *below* the ordinary Class A results at efficiency ~0.69. Efficiency is necessary for attempt 20's 0.8670 but nowhere near sufficient.

- **Spending more wall clock.** Ruled out. The two runs above 90 s (attempts 8 at 98.60 s and 23 at 94.75 s) scored 0.7805 and 0.8170, both below the ~74 s norm. There is no record in which extra wall clock bought reward.

- **The heavyweight / long-running regime of attempt 21.** Ruled out hard. 1691.67 s produced `primary_target_reached` 0.0, no qualifying budget row at all, and the only 0.0000 in the set. Do not re-enter this regime.

- **Tightening the declared qualifying budget toward ~50 s.** Ruled out. Attempt 9 held everything at a 49.89 s qualifying budget and still only scored 0.8332, below the 0.8655+ plateau; attempt 7 at 50.05 s lost the held-out perturbation on `C-BUDGET-RESPECTED` and scored 0.4911. The declared budget must leave headroom for the held-out variant, which is measurably slower to reach threshold than the primary.

- **Module-level executable statements in the submission.** Ruled out by `C-API-SURFACE` in attempt 6: the module may contain imports, constants and permitted definitions only. All work must live inside the permitted definitions; nothing that executes at import time.

- **The intermediate cost band (`per_step_cost_ratio` ≈ 0.74–0.81).** Ruled out as dominated: attempts 18 and 23 scored 0.8368 and 0.8170, below both Class A's plateau and attempt 20, with no compensating robustness.

- **Re-running Class A unchanged to chase the plateau.** Ruled out as progress. Attempts 3, 5, 13 and 17 land at 0.8655–0.8658 with a spread of 0.0003; further samples from that configuration reproduce the plateau rather than exceed it.

# 5. Open leads

- **Reproduce attempt 20's operating point precisely, then perturb it only in the quality dimension.** Its signature is `per_step_cost_ratio` 0.7013, `compute_efficiency` 0.9633, `qualifying_budget` 73.66 s, `wall_clock_sec` 73.66 s, all perturbations held. It is the only configuration that has cleared the Class A plateau. The gap between it (0.8670) and its same-class siblings 16 (0.7005) and 4 (0.7740) is the largest unexplained variance in the data and is where the remaining headroom sits.

- **Isolate the quality term.** Reward is not a monotone function of the terms exposed here: at essentially identical `per_step_cost_ratio` ≈ 0.70 the rewards range 0.7005–0.8670, and at `compute_efficiency` ≈ 0.69 they range 0.8079–0.8658. Something about how far past the threshold the solution lands, or how it does so, dominates. Instrument or reason about the margin by which the primary crosses its threshold rather than about step cost, and prefer configurations that cross with room to spare.

- **Buy explicit margin on the held-out variant.** This is the highest-expected-value single change available. `C-PERTURBATION-REACHED` has cost ~0.44 of reward on four separate occasions, always via the held-out variant. The held-out variant needs more of both: more headroom against the declared budget position, and more headroom against the threshold itself. A configuration that scores 0.86 with a comfortable held-out margin beats one that might score 0.87 and risks halving.

- **Keep the declared budget near ~74 s.** Every record in the 0.85–0.87 band declared a qualifying budget between 73.6 s and 75.6 s. Both tighter (≈50 s) and looser (≈95–99 s) declarations scored worse. Treat ~74 s as the calibrated setting and change it only with a reason.

- **Re-verify the module surface before submitting.** `C-API-SURFACE` is cheap to avoid and cost 0.10 of reward once. Confirm the module contains only imports, constants and permitted definitions, with no import-time execution.

## Perturbation-run outcomes, by kind and in aggregate

Every record declared exactly 2 perturbations (`perturbations_declared: 2.0`), one of kind `held_out_variant` and one of kind `seed`. Across the 23 records that is 46 held-out runs in total.

- **`seed` runs: 23 attempted, 22 reached their threshold, 1 did not.** The single failure occurred in the record where the primary itself failed (attempt 21, reward 0.0000), and it failed on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. Seed perturbation is essentially solved; it has never been the reason a otherwise-working submission lost points.
- **`held_out_variant` runs: 23 attempted, 19 reached their threshold, 4 did not** (in attempts 7, 12, 19 and 21). All 4 failures include `C-BUDGET-RESPECTED`; 3 of the 4 (attempts 12, 19, 21) also include `C-TARGET-REACHED`. The remaining one (attempt 7) failed `C-BUDGET-RESPECTED` alone — it reached the target but outside its budget position.
- **Aggregate: 41 of 46 perturbation runs reached, 5 did not.** Four of the five failures were of kind `held_out_variant`. `all_perturbations_held` was true in 19 of 23 records.

The kind of run that is failing is the **held-out variant**, and the check it fails on is **`C-BUDGET-RESPECTED`** in every instance, with `C-TARGET-REACHED` alongside it in three of the four. The runs are not identified across records, so no claim is made that the same run recurred.

## Call: exploit

Take attempt 20's configuration — `per_step_cost_ratio` ≈ 0.70, `compute_efficiency` ≈ 0.96, declared budget ≈ 74 s — and fix the one thing that has repeatedly stopped this family: held-out-variant margin against its own budget position. Do not chase efficiency further; attempts 11 and 16 already showed that road is flat or negative. Do not resample Class A hoping to exceed 0.8658; four records have now landed within 0.0003 of each other there.

One process note, stated plainly because the record shows it: three separate attempts (7, 12, 19) lost roughly half their reward to `C-PERTURBATION-REACHED` on the held-out variant while varying per-step cost across a wide range. Varying cost again without addressing held-out margin would be repeating a failure without changing what caused it, and that is neither exploring nor exploiting.
