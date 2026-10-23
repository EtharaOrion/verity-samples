# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.8658, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All 14 attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3        0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                
  5 *      0.8658   1.000             2 of 2         yes             74                
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
  13 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 13 -- reward 0.8657, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 17 -- reward 0.8655, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 18 -- reward 0.8368, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.4278, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED has failed on 3 attempts (7, 12, 19). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Nineteen graded submissions, all with `measurement_status: "measured"`. Every one carries a reward; none is missing a measurement, and none scored zero (`zero_reason_code` is 0 and `red_line_crossed` is 0.0 in all nineteen). Ordered worst to best by reward:

| Rank | Attempt | Reward | Notes |
|---|---|---|---|
| 1 (worst) | 12 | 0.4275 | `C-PERTURBATION-REACHED` failed; `task_pass` 0.0 |
| 2 | 19 | 0.4278 | `C-PERTURBATION-REACHED` failed; `task_pass` 0.0 |
| 3 | 7 | 0.4911 | `C-PERTURBATION-REACHED` failed; `task_pass` 0.0 |
| 4 | 16 | 0.7005 | all checks held |
| 5 | 6 | 0.7580 | `C-API-SURFACE` failed; `task_pass` 0.0 |
| 6 | 4 | 0.7740 | all checks held |
| 7 | 8 | 0.7805 | all checks held; longest wall clock, 98.60 s |
| 8 | 11 | 0.8067 | all checks held; `compute_efficiency` 1.0 |
| 9 | 2 | 0.8079 | all checks held |
| 10 | 9 | 0.8332 | all checks held |
| 11 | 18 | 0.8368 | all checks held |
| 12 | 10 | 0.8503 | all checks held |
| 13 | 14 | 0.8513 | all checks held |
| 14 | 15 | 0.8579 | all checks held |
| 15 | 1 | 0.8630 | all checks held; first measured attempt |
| 16 | 17 | 0.8655 | all checks held |
| 17 | 13 | 0.8657 | all checks held |
| 18 | 3 | 0.8657 | all checks held |
| 19 (best) | 5 | **0.8658** | all checks held |

**Attempt 5 holds the highest reward, 0.8658. That is the score to beat.**

The top of the table is a plateau, not a trend. Attempts 3 (0.8657), 5 (0.8658), 13 (0.8657) and 17 (0.8655) span 0.0003 in total. Whatever differed among those four submissions did not move the reward outside measurement noise. Attempt 1, the very first submission, already reached 0.8630 — eighteen further submissions have bought 0.0028 of reward over the opening attempt.

Every attempt after 5 is stated by the harness as `worse_than_an_earlier_attempt`. That is a fall, not progress: attempts 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 and 19 all rank below 0.8658, and several of them (12, 19, 7, 16, 6, 4) rank far below it. Only three records were ever `better_than_every_earlier_attempt`: attempts 3, 5, and (as the first) attempt 1.

## 2. Approach classes tried

I have the measured terms, not the source. The records nevertheless carry a clear numeric fingerprint — `per_step_cost_ratio`, `compute_efficiency`, `wall_clock_sec` and `qualifying_budget` — and the submissions group cleanly into five classes by it. Two records with the same fingerprint and the same outcome are one entry below.

**Class A — near-unit per-step cost, standard budget (the class that holds the best score).**
`per_step_cost_ratio` in 0.94–0.99, `compute_efficiency` 0.68–0.75, `wall_clock_sec` ≈ 74 s. Attempts 2, 3, 5, 9, 10, 13, 17, and also attempt 7 (ratio 0.966) which failed on a perturbation. Rewards: 0.8079, 0.8657, **0.8658**, 0.8332, 0.8503, 0.8657, 0.8655, and 0.4911 for the perturbation failure. This class contains every reward above 0.8600. It is the incumbent and it has flattened at ≈0.8657.

**Class B — aggressive per-step cost reduction.**
`per_step_cost_ratio` cut to 0.688–0.706, `compute_efficiency` driven to 0.93–1.00. Attempts 4 (0.7740), 11 (0.8067, efficiency exactly 1.0), 14 (0.8513), 16 (0.7005), 19 (0.4278, perturbation failure, efficiency exactly 1.0). Maximum efficiency was achieved twice and neither time did it produce a competitive reward. This class is uniformly below Class A despite winning every efficiency term outright.

**Class C — moderate per-step cost reduction.**
`per_step_cost_ratio` 0.767–0.811. Attempts 18 (0.8368, all checks held) and 12 (0.4275, perturbation failure). Sits between A and B on reward exactly as it sits between them on cost ratio.

**Class D — above-unit per-step cost.**
`per_step_cost_ratio` above 1.0. Attempt 1 (1.072, 0.8630 — the strongest result outside Class A), attempt 8 (1.085 with `wall_clock_sec` 98.60 s, 0.7805), attempt 6 (1.409, `C-API-SURFACE` failure, 0.7580). Mildly over-unit cost is survivable (attempt 1); pushing cost up further and running longer is not.

**Class E — efficiency gain without cost-ratio sacrifice (single record, attempt 15).**
`compute_efficiency` 0.9355 alongside `per_step_cost_ratio` 0.9424 — the only submission that raised efficiency into Class B territory while keeping per-step cost in Class A territory. Reward 0.8579, all checks held, all perturbations held. It is the most informative record in the set: it shows those two terms are separable, and it is the only non-Class-A configuration within 0.008 of the best score.

**Budget-shortening variations, cutting across classes.** Attempt 9 ran a full 74.39 s wall clock but reported `qualifying_budget` 49.89 s and scored 0.8332 — below the Class A plateau. Attempts 6 (45.82 s) and 7 (50.05 s) also carry compressed qualifying budgets and both failed a check. Shortening the qualifying budget has never been paired with a reward above 0.8332.

## 3. Checks that failed

Two named checks failed, in four records total. Fifteen of nineteen records had `failed_checks: []`.

**`C-PERTURBATION-REACHED` — failed three times: attempts 7, 12 and 19.** The verifier's reason is identical each time: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This is the dominant finding in the whole record set. The three failures are separated by many intervening submissions and span two different approach classes (attempt 7 is Class A, attempts 12 and 19 are Classes C and B). **Whatever was changed between those attempts is not what is causing this failure.** The changes in per-step cost, in efficiency and in budget shape all varied across those three records and the same check went down each time; the cause lies somewhere the fingerprint terms do not distinguish, and it must be attacked directly rather than by re-tuning cost.

The cost of this check is severe and consistent: `conformance_fraction` drops to 0.5, `task_pass` drops to 0.0, and reward collapses to 0.4275, 0.4278 and 0.4911 — roughly half the incumbent. Note that in all three cases `primary_target_reached` was still 1.0 and `rule_conformance` was still 1.0. The primary run was fine; the held-out run was not.

**`C-API-SURFACE` — failed once: attempt 6.** Reason: *"module-level statements outside imports, constants, and permitted definitions."* This is a structural requirement on the submission file, not an algorithmic one. It drove `rule_conformance` to 0.8571 and `task_pass` to 0.0, with reward 0.7580. It has not recurred, so it appears to have been fixed and stayed fixed; the next attempt must simply not reintroduce module-level executable code.

## 4. Ruled-out directions

**Maximising `compute_efficiency` by cutting `per_step_cost_ratio`.** Class B drove the cost ratio to ≈0.69 and reached `compute_efficiency` of exactly 1.0 twice (attempts 11 and 19). Attempt 11 scored 0.8067 and attempt 19 scored 0.4278; the whole class tops out at 0.8513 (attempt 14) and bottoms at 0.7005 (attempt 16). Cheap steps are being paid for out of whatever quality term dominates the reward. Ruled out as a primary lever: the efficiency term is already near its ceiling in that class and the reward went down anyway.

**Running longer / spending more per step.** Attempt 8 combined `per_step_cost_ratio` 1.085 with the longest wall clock in the set, 98.60 s, and returned 0.7805 — clearly below the ≈74 s Class A plateau. Attempt 6 pushed the ratio to 1.409 and returned 0.7580 with a failed check. More compute has never bought reward here.

**Shortening the qualifying budget.** Attempt 9 held every check with a `qualifying_budget` of 49.89 s and still landed at 0.8332, below the plateau; attempts 6 and 7, the other compressed-budget records, both failed checks. There is no evidence the reward rewards a short qualifying budget, and there is evidence that compressing it endangers the held-out run.

**Module-level executable statements in the submission.** Directly and unambiguously ruled out by the `C-API-SURFACE` reason text: only imports, constants, and permitted definitions may appear at module level.

**Resubmitting the Class A configuration unchanged.** Attempts 3, 5, 13 and 17 returned 0.8657, 0.8658, 0.8657 and 0.8655. Four samples of the same plateau is four samples; it is neither exploration nor exploitation and it will not produce a new best. If the next attempt reproduces Class A, it must change something inside it that plausibly moves quality, not merely re-roll it.

## 5. Open leads

**Lead 1 — protect the held-out variant run; that is where all the reward is being lost.** Across the nineteen records there were thirty-eight held-out runs beside the primary one: nineteen of kind `seed` and nineteen of kind `held_out_variant`. By kind: **every single `seed` run reached its threshold, nineteen out of nineteen, with no failed checks anywhere.** The `held_out_variant` kind reached in sixteen of nineteen and failed in three. In aggregate, thirty-five of thirty-eight held-out runs reached; all three failures are of the `held_out_variant` kind and none is a `seed` run. The failing unit's own checks were `C-BUDGET-RESPECTED` in one record, and `C-TARGET-REACHED` together with `C-BUDGET-RESPECTED` in the other two. So the variant run is exhausting its own budget before hitting its own target, while the seed run never has trouble. The concrete lead: make the schedule adaptive to the variant's own budget rather than fixed to what the primary run needs — detect that progress is behind pace and cut steps or converge earlier inside the variant's budget. Recovering that check is worth roughly 0.44 of reward relative to those failures, far more than any tuning gain observed. Note that the harness does not name, number or order these runs; I cannot tell whether the same underlying variant failed in all three records, only that the failing kind was `held_out_variant` each time.

**Lead 2 — the attempt 15 configuration is the one unexplored corner of the space.** Attempt 15 achieved `compute_efficiency` 0.9355 while holding `per_step_cost_ratio` at 0.9424, all checks held, all perturbations held, reward 0.8579. Every other high-efficiency record bought its efficiency by dropping the cost ratio to ≈0.69 and paid for it in reward. Attempt 15 shows the two terms are separable — efficiency can come from using fewer or better steps rather than cheaper ones. Pushing this direction while keeping the cost ratio in the 0.94–0.99 band is the most promising route past 0.8658, because it stacks an efficiency gain on top of the cost profile that produced every reward above 0.8600.

**Lead 3 — the mild over-unit cost point is under-sampled.** Attempt 1, at `per_step_cost_ratio` 1.072, scored 0.8630 — the best result outside Class A and within 0.003 of the incumbent — with `compute_efficiency` only 0.6784. Nothing between ratio 0.99 and 1.07 has been sampled. If the reward is dominated by solution quality, a small deliberate increase in per-step work above unity, paired with fewer steps to keep the wall clock near 74 s, is a plausible way to buy quality without the efficiency penalty attempt 8 incurred by running to 98.6 s.

**Lead 4 — hold the wall clock near 74 s.** Sixteen of nineteen records ran 73.6–75.5 s and this band contains every reward above 0.8500. The two departures, 98.60 s (0.7805) and 50.05 s (0.4911, failed check), were both worse. Treat ≈74 s as the operating point and vary what happens inside it.

**Constraints to carry forward regardless of direction:** no module-level statements beyond imports, constants and permitted definitions (`C-API-SURFACE`); `primary_target_reached` has been 1.0 in all nineteen records and `validity` 1.0 in all nineteen — neither is at risk and neither needs work.

**Call: exploit.** Class A already holds the best score at 0.8658 and the reward loss is concentrated in one identified place — the `held_out_variant` run running out of its own budget before hitting its own target, `C-PERTURBATION-REACHED`, three times. That is the "one thing that stopped it," and fixing it is worth an order of magnitude more than any tuning delta seen. Take the Class A cost profile (per-step cost ratio ≈0.95, wall clock ≈74 s), add the attempt-15 style efficiency gain that does not come from cheapening steps, and add explicit per-run budget awareness so the variant converges inside its own budget. What must not happen again is a bare resubmission of the Class A plateau: attempts 3, 5, 13 and 17 already did that four times and returned the same 0.8655–0.8658, which is repetition rather than refinement.
