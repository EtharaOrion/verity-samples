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

    All five attempts since have scored lower than it.
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
  24       0.8426   1.000             2 of 2         yes             96                
  25       0.7757   1.000             2 of 2         yes             70                

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
  19 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 23 -- reward 0.8170, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 95
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 24 -- reward 0.8426, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 96
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 25 -- reward 0.7757, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 70
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-BUDGET-RESPECTED failed on attempt 21.
    C-PERTURBATION-REACHED has failed on 4 attempts (7, 12, 19, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 21.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Twenty-five graded records, all with `measurement_status: "measured"`, so every one carries a reward. Ordered worst to best:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 21 | 0.0000 | `zero_reason_code: 4`, `primary_target_reached: 0`, `qualifying_budget` not-measured, `wall_clock_sec` 1691.67 |
| 2 | 12 | 0.4275 | `conformance_fraction` 0.5, held-out variant unit did not reach |
| 3 | 19 | 0.4278 | `conformance_fraction` 0.5, held-out variant unit did not reach, `compute_efficiency` 1.0 |
| 4 | 7 | 0.4911 | `conformance_fraction` 0.5, held-out variant unit did not reach |
| 5 | 16 | 0.7005 | fully conformant, `compute_efficiency` 0.9805 |
| 6 | 6 | 0.7580 | `rule_conformance` 0.857, `task_pass` 0, C-API-SURFACE |
| 7 | 4 | 0.7740 | `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934 |
| 8 | 25 | 0.7757 | `wall_clock_sec` 70.17 |
| 9 | 8 | 0.7805 | `wall_clock_sec` 98.60 |
| 10 | 11 | 0.8067 | `compute_efficiency` 1.0, `per_step_cost_ratio` 0.6947 |
| 11 | 2 | 0.8079 | |
| 12 | 23 | 0.8170 | `wall_clock_sec` 94.75 |
| 13 | 9 | 0.8332 | `qualifying_budget` 49.89 vs `wall_clock_sec` 74.39 |
| 14 | 18 | 0.8368 | `per_step_cost_ratio` 0.7671 |
| 15 | 24 | 0.8426 | `wall_clock_sec` 96.18 |
| 16 | 10 | 0.8503 | |
| 17 | 14 | 0.8513 | `per_step_cost_ratio` 0.6997, `compute_efficiency` 0.9705 |
| 18 | 15 | 0.8579 | `compute_efficiency` 0.9355, `per_step_cost_ratio` 0.9424 |
| 19 | 22 | 0.8594 | `wall_clock_sec` 70.30 |
| 20 | 1 | 0.8630 | first measured attempt, `per_step_cost_ratio` 1.0723 |
| 21 | 17 | 0.8655 | |
| 22 | 13 | 0.8657 | (0.86565613) |
| 23 | 3 | 0.8657 | (0.86571101) |
| 24 | 5 | 0.8658 | |
| 25 (best) | 20 | 0.8670 | `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013, `wall_clock_sec` 73.66, all checks held |

**Attempt 20 holds the highest reward at 0.8670 and is the attempt to beat.** Only four records were ever recorded as better than every earlier attempt: 1 (as the first measurement), 3, 5, and 20. Every other record carries `standing_against_best_so_far: "worse_than_an_earlier_attempt"` — that is a plain regression against the running best in each case, not incremental progress. In particular attempts 21 through 25, all of which came after the 0.8670 peak, scored 0.0000, 0.8594, 0.8170, 0.8426 and 0.7757 respectively; every one of them is below the peak, and the most recent record (25, at 0.7757) is roughly nine points of reward below it. The loop has been drifting downward since attempt 20, not converging on it.

No record ever crossed a red line (`red_line_crossed: 0.0` throughout) and `validity` is 1.0 throughout, so nothing here was disqualified for invalidity.

## 2. Approach classes tried

Only the measured terms are available, so approaches are grouped by their measured signature — the cost-per-step regime, the wall-clock/budget regime, and the conformance outcome. Where two attempts share a signature and a reward band they are one entry.

**Class A — the "baseline pace" family: `per_step_cost_ratio` near 0.94–1.00, wall clock near 74 s, `compute_efficiency` 0.68–0.75.** Attempts 1 (1.0723 / 76.34 s / 0.8630), 2 (0.9441 / 74.26 s / 0.8079), 3 (0.9835 / 74.37 s / 0.8657), 5 (0.9581 / 74.38 s / 0.8658), 13 (0.9710 / 74.26 s / 0.8657), 17 (0.9464 / 75.53 s / 0.8655), 22 (0.9380 / 70.30 s / 0.8594), 10 (0.9615 / 74.54 s / 0.8503). This is the most-repeated class and the most reliable: four separate members land within 0.0003 of each other at 0.8655–0.8658, which is a strong signal that this configuration has a hard ceiling just under 0.866 and that re-running it with small variations does not move it. Attempt 2 at 0.8079 is the outlier inside this class and shows that something other than pace can still cost eight points here.

**Class B — the "cheap step" family: `per_step_cost_ratio` 0.67–0.77, `compute_efficiency` 0.88–1.00, wall clock still near 74 s.** Attempts 4 (0.6934 / 0.9681 / 0.7740), 11 (0.6947 / 1.0000 / 0.8067), 14 (0.6997 / 0.9705 / 0.8513), 16 (0.7055 / 0.9805 / 0.7005), 18 (0.7671 / 0.8827 / 0.8368), 20 (0.7013 / 0.9633 / **0.8670**), 23 (0.7375 / 0.8859 / 0.8170, at 94.75 s). This class contains both the best result on record and the worst fully-conformant result on record (16, at 0.7005). Driving `compute_efficiency` to its maximum does not buy reward: attempt 11 hit `compute_efficiency` 1.0000 and scored 0.8067, below six members of the slower Class A. The spread of 0.7005 to 0.8670 across near-identical cost ratios is the single most informative pattern in the data: **the reward is dominated by a quality/margin term that is largely independent of the cost terms**, and cheapening the step only helps when that quality term is already held.

**Class C — the "extended budget" family: wall clock 94–99 s.** Attempts 8 (98.60 s / 0.7805), 23 (94.75 s / 0.8170), 24 (96.18 s / 0.8426). All three qualified and passed, all three landed below the ~0.866 plateau. Spending more wall clock was measured three times and never once produced a top-band result.

**Class D — the "early qualification" family: `qualifying_budget` around 46–50 s while wall clock stayed near 70–74 s.** Attempts 9 (qualifying 49.89, wall 74.39, reward 0.8332), 6 (qualifying 45.82, wall 70.37, but failed C-API-SURFACE), 7 (qualifying 50.05, wall 50.05, failed C-PERTURBATION-REACHED). Crossing the threshold early did not raise reward — 9 is more than three points below the peak — and two of the three members of this class broke a check.

**Class E — the aggressive/long-running search: attempt 21.** `wall_clock_sec` 1691.67, roughly twenty-three times the ~74 s of every other record, `per_step_cost_ratio` 0.6727, and yet `primary_target_reached: 0` with no qualifying row at all. This is the only 0.0000 and the only record where the seed perturbation also failed.

**Class F — a submission with disallowed module structure: attempt 6.** Fully reaching its primary target (`primary_target_reached: 1`, `qualifying_budget` 45.82, the earliest on record) but `rule_conformance` 0.857 and `task_pass` 0 because of C-API-SURFACE. Its reward of 0.7580 shows how much a structural violation costs on an otherwise fast, qualifying run.

## 3. Checks that failed

**C-PERTURBATION-REACHED — failed four times**, in attempts 7, 12, 19 and 21. Reason in attempts 7, 12 and 19: "1 of 2 declared perturbations reached their own threshold inside their own budget". Reason in attempt 21: "0 of 2 declared perturbations reached their own threshold inside their own budget". This is by a wide margin the dominant failure and it is the finding that matters most. It has now failed across four attempts spanning very different cost regimes — attempt 7 at `per_step_cost_ratio` 0.9657 and wall clock 50.05 s, attempt 12 at 0.8114 and 74.11 s, attempt 19 at 0.6884 with `compute_efficiency` 1.0000, attempt 21 at 0.6727 with wall clock 1691.67 s. **Whatever was being changed between those four attempts — the step cost, the compute efficiency, the wall clock — is not what is causing this check to fail.** The cause lies in the generalisation/robustness of the trained result on the held-out perturbation, not in the pacing knobs that were varied.

**C-TARGET-REACHED (on the primary run) — failed once**, in attempt 21, reason "no evaluation row crosses the threshold in the declared direction". This is the check behind the single 0.0000.

**C-BUDGET-RESPECTED (on the primary run) — failed once**, in attempt 21, reason "no qualifying row, so no budget position exists". This is a consequence of the C-TARGET-REACHED failure in the same record, not an independent budget overrun.

**C-API-SURFACE — failed once**, in attempt 6, reason "module-level statements outside imports, constants, and permitted definitions". This dropped `rule_conformance` to 0.857 and `task_pass` to 0 on a run that had otherwise reached its target with the earliest qualifying budget on record. It is a pure structural/style violation of the submission file and is separately and cheaply fixable: keep the module body to imports, constants and permitted definitions, and put all executable logic inside the permitted functions.

## 4. Ruled-out directions

**Maximising `compute_efficiency` / minimising `per_step_cost_ratio` as the primary lever.** Ruled out because attempt 11 reached `compute_efficiency` 1.0000 with `per_step_cost_ratio` 0.6947 and scored 0.8067, and attempt 19 also reached `compute_efficiency` 1.0000 and scored 0.4278 while breaking C-PERTURBATION-REACHED; meanwhile attempts 3, 5, 13 and 17 sat at `compute_efficiency` 0.69–0.73 and scored 0.8655–0.8658. Cheap steps alone do not buy reward.

**Extending the wall-clock / training budget past ~90 s.** Ruled out by three independent measurements: attempt 8 (98.60 s → 0.7805), attempt 24 (96.18 s → 0.8426), attempt 23 (94.75 s → 0.8170). All qualified and all landed below the ~0.866 plateau reached at ~74 s. More time is measured as a cost with no compensating quality gain.

**Very long search / heavy-compute runs.** Ruled out by attempt 21: 1691.67 s of wall clock produced no qualifying row at all, failed C-TARGET-REACHED, C-BUDGET-RESPECTED and C-PERTURBATION-REACHED on both units, and scored 0.0000. This is the only record where even the seed unit failed to reach.

**Cutting the run short to qualify early.** Ruled out as a scoring lever by attempt 9, which qualified at 49.89 s inside a 74.39 s run and scored 0.8332 — over three points below the peak — and by attempt 7, which finished at 50.05 s and lost the held-out perturbation to C-BUDGET-RESPECTED for 0.4911. Early qualification does not raise reward and does raise perturbation risk.

**Any submission with executable statements at module scope.** Ruled out by attempt 6's C-API-SURFACE failure, which cost `task_pass` outright on an otherwise successful run.

**Re-running the Class A baseline unchanged.** Ruled out as an improvement path: four members converged to 0.8655–0.8658 with a spread of 0.0003. That configuration has stopped improving; repeating it will reproduce ~0.8657 and will not beat 0.8670.

## 5. Open leads

**Reconstruct the attempt-20 operating point exactly.** It is the only record combining `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013, `wall_clock_sec` 73.66, `qualifying_budget` 73.66, full conformance on both perturbation units, and reward 0.8670. Attempts 14 (0.6997 / 0.9705 / 0.8513) and 4 (0.6934 / 0.9681 / 0.7740) sat in the same cost regime and scored much lower, so the cost regime is necessary but far from sufficient — the difference lives in the training recipe itself (optimiser schedule, regularisation, initialisation, data handling), not in the pacing. Re-derive a Class-B-shaped run: keep the total wall clock near 73–74 s, keep the per-step cost near 0.70 of the reference, and let the qualifying row land near the end of the run rather than early.

**Attack the held-out-variant robustness directly.** By kind, the held-out-variant unit failed to reach in four of twenty-five records (attempts 7, 12, 19, 21) while the seed unit failed to reach in only one (attempt 21). In aggregate, 45 of 50 perturbation units reached; all five unit failures were C-BUDGET-RESPECTED, and four of those (12, 19, 21 on the held-out variant, plus 21 on the seed) also carried C-TARGET-REACHED. The kind of run that fails is the **held-out variant**, and it fails on **C-TARGET-REACHED and C-BUDGET-RESPECTED** — it either never crosses its threshold or crosses it too late. The runs are not individually identified, so no claim can be made that the same variant recurs across records; what is measurable is that this kind, and only this kind (outside the total collapse of attempt 21), is the fragile one. The lead: build in headroom against the variant rather than tuning for the primary run — hold a margin above the threshold rather than crossing it by a hair, and leave slack in the per-unit budget so a slightly harder variant still qualifies. Every attempt that lost this check scored 0.4275–0.4911, roughly half the peak, so this is the highest-value single fix available.

**Explore the quality term while pinning the cost terms.** The measured evidence says reward varies by ~0.17 (0.7005 at attempt 16 up to 0.8670 at attempt 20) across attempts whose `per_step_cost_ratio` differs by less than 0.01. That residual variance is where the remaining reward is. Vary the learning recipe — schedule shape, weight decay/regularisation strength, ensembling or averaging of the final weights, augmentation — while holding wall clock at ~74 s and per-step cost at ~0.70, and read the reward difference as attributable to the recipe.

**Keep a margin above threshold rather than optimising for the earliest qualifying row.** `qualifying_budget` equalled `wall_clock_sec` in nearly every top-band record (3, 5, 13, 17, 20, 22), whereas the records where `qualifying_budget` was well below wall clock (6 at 45.82/70.37, 7 at 50.05, 9 at 49.89/74.39) either broke a check or scored below the plateau. Treating the whole run as the qualifying run correlates with the good results.

**Mechanical guard on C-API-SURFACE.** Before submitting, verify the module body contains only imports, constant assignments and permitted definitions. This costs nothing and has already cost one attempt its `task_pass`.

## Call: exploit

Exploit. The best result, 0.8670 at attempt 20, is fully conformant, held both perturbation units, and is only 0.0012 above the tightly-clustered 0.8655–0.8658 plateau — but that plateau itself is a dead end that four attempts have re-measured to three decimal places, and everything since attempt 20 has regressed. The exploit is not to repeat the plateau; it is to rebuild the attempt-20 operating point (≈74 s wall clock, per-step cost ≈0.70, compute efficiency ≈0.96, qualifying row at the end of the run) and then spend the remaining freedom on the one thing that has repeatedly destroyed otherwise-good runs: held-out-variant robustness against C-TARGET-REACHED and C-BUDGET-RESPECTED, which has taken four attempts down to the 0.43–0.49 band or to zero. Cost-side tuning has been measured to exhaustion in both directions and should not be varied further.

One caution about the loop's own history: attempt 21 repeated a heavy-compute direction that produced a 0.0000 with no qualifying row, and attempts 7, 12 and 19 repeatedly lost C-PERTURBATION-REACHED while only the pacing knobs were changed between them. That is neither exploration nor exploitation — it is re-running a failure without changing what caused it, and it should not be repeated.
