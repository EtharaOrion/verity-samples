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

    It is also the most recent attempt, so this is where the work stands.

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

# 1. Results so far

Twenty graded submissions, all with `measurement_status: "measured"`. Every one carries a reward; none produced an absent measurement, and none crossed a red line (`red_line_crossed: 0.0` throughout) or was invalid (`validity: 1.0` throughout). Listed worst to best by reward:

| Rank | Attempt | reward | task_pass | Notes from the measured terms |
|---|---|---|---|---|
| 1 | 12 | 0.4275 | 0.0 | Held-out-variant perturbation failed; `conformance_fraction` 0.5 |
| 2 | 19 | 0.4278 | 0.0 | Held-out-variant perturbation failed; `compute_efficiency` 1.0000, `per_step_cost_ratio` 0.6884 |
| 3 | 7 | 0.4911 | 0.0 | Held-out-variant perturbation failed; `wall_clock_sec` 50.05 |
| 4 | 16 | 0.7005 | 1.0 | All checks held; `compute_efficiency` 0.9805, `per_step_cost_ratio` 0.7055 |
| 5 | 6 | 0.7580 | 0.0 | `C-API-SURFACE` failed; `rule_conformance` 0.8571; `per_step_cost_ratio` 1.4094 |
| 6 | 4 | 0.7740 | 1.0 | `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934 |
| 7 | 8 | 0.7805 | 1.0 | `wall_clock_sec` 98.60, the longest run recorded |
| 8 | 11 | 0.8067 | 1.0 | `compute_efficiency` 1.0000, `per_step_cost_ratio` 0.6947 |
| 9 | 2 | 0.8079 | 1.0 | `per_step_cost_ratio` 0.9441 |
| 10 | 9 | 0.8332 | 1.0 | `qualifying_budget` 49.89 against `wall_clock_sec` 74.39 |
| 11 | 18 | 0.8368 | 1.0 | `per_step_cost_ratio` 0.7671, `compute_efficiency` 0.8827 |
| 12 | 10 | 0.8503 | 1.0 | `per_step_cost_ratio` 0.9615 |
| 13 | 14 | 0.8513 | 1.0 | `per_step_cost_ratio` 0.6997, `compute_efficiency` 0.9705 |
| 14 | 15 | 0.8579 | 1.0 | `per_step_cost_ratio` 0.9424, `compute_efficiency` 0.9355 |
| 15 | 1 | 0.8630 | 1.0 | First measured attempt; `per_step_cost_ratio` 1.0723 |
| 16 | 17 | 0.8655 | 1.0 | `per_step_cost_ratio` 0.9464 |
| 17 | 13 | 0.8657 | 1.0 | `per_step_cost_ratio` 0.9710 (0.8656561 unrounded) |
| 18 | 3 | 0.8657 | 1.0 | `per_step_cost_ratio` 0.9835 (0.8657110 unrounded, marginally above attempt 13) |
| 19 | 5 | 0.8658 | 1.0 | `per_step_cost_ratio` 0.9581 |
| 20 | 20 | 0.8670 | 1.0 | `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013 |

**Attempt 20 holds the highest reward at 0.8670 and is the attempt to beat.** Only four records were ever marked `better_than_every_earlier_attempt`: attempt 1 (first measured), attempt 3 (0.8657), attempt 5 (0.8658) and attempt 20 (0.8670). Every other record is explicitly marked `worse_than_an_earlier_attempt`, and that is what happened — these were regressions, not progress. In particular attempts 6, 7, 8, 11, 12, 16 and 19 all scored below the standing best at the time they were run, several of them far below it, and attempts 9 through 19 as a block never once improved on attempt 5's 0.8658 until attempt 20 finally did so by 0.0012.

The headline shape of the results: fourteen of twenty attempts land between 0.7005 and 0.8670, and five of those cluster tightly at 0.8655–0.8670. The remaining three (12, 19, 7) collapse to 0.4275–0.4911, and in every one of those three the cause is the same held-out perturbation failure described in section 3. The gap between the plateau (~0.866) and the collapse (~0.43) is roughly a factor of two, which means a perturbation failure costs about half the reward and is by far the most expensive single failure mode observed.

# 2. Approach classes tried

The measured terms do not carry source code, so the approaches are distinguishable only by their measured cost/efficiency signature. Grouped by that signature, and merging records that behaved the same way:

**Class A — baseline-cost training, `per_step_cost_ratio` ≈ 0.94–1.09, `compute_efficiency` ≈ 0.66–0.75.** Attempts 1, 2, 3, 5, 7, 9, 10, 13, 17. This is the largest class and it contains most of the high plateau: 0.8630, 0.8079, 0.8657, 0.8658, 0.4911 (perturbation failure), 0.8332, 0.8503, 0.8657, 0.8655. Runs in this class spend roughly a full step-cost budget and buy reward through solution quality rather than through efficiency. Its ceiling in these records is 0.8658 (attempt 5). Wall-clock for this class sits consistently at 74–76 s.

**Class B — aggressive per-step cost reduction, `per_step_cost_ratio` ≈ 0.69–0.71, `compute_efficiency` ≈ 0.96–1.00.** Attempts 4, 11, 14, 16, 19, 20. The measured outcome of this class is bimodal and this is the single most informative pattern in the data. Same cost band, wildly different rewards: 0.7740 (attempt 4), 0.8067 (attempt 11, `compute_efficiency` exactly 1.0000), 0.8513 (attempt 14), 0.7005 (attempt 16), 0.4278 (attempt 19, perturbation failure, also `compute_efficiency` 1.0000), and 0.8670 (attempt 20, the best result recorded). Driving `per_step_cost_ratio` down to ~0.70 does **not** by itself determine reward — attempts 11 and 19 both reached the maximum `compute_efficiency` of 1.0000 and scored 0.8067 and 0.4278 respectively, while attempt 20 reached only 0.9633 efficiency and scored highest of all. Whatever attempt 20 did differently from 4, 11, 16 and 19 in the quality dimension is the thing worth recovering.

**Class C — intermediate cost, `per_step_cost_ratio` ≈ 0.77–0.85, `compute_efficiency` ≈ 0.85–0.89.** Attempts 12 and 18. Attempt 18 scored 0.8368; attempt 12 scored 0.4275 on a held-out perturbation failure. This band shows no advantage over either A or B.

**Class D — long / expensive runs.** Attempt 8, `wall_clock_sec` 98.60 (the longest recorded), `per_step_cost_ratio` 1.0848, `compute_efficiency` 0.6575, reward 0.7805; and attempt 6, `per_step_cost_ratio` 1.4094 (the highest recorded), `compute_efficiency` 0.4942 (the lowest recorded), reward 0.7580 with `task_pass` 0.0. Spending more per step and more wall-clock produced strictly worse rewards than the class-A plateau. Attempt 1 at 1.0723 cost ratio is the one exception in the over-1.0 band, at 0.8630.

**Class E — early-qualifying variants.** Attempt 9 is the only clean record where `qualifying_budget` (49.89) falls well short of `wall_clock_sec` (74.39); attempt 6 shows the same split (45.82 vs 70.37) but failed a rule check. Attempt 9 scored 0.8332, below the class-A plateau, so qualifying earlier in the run did not by itself pay.

# 3. Checks that failed

Seventeen of twenty records had an empty `failed_checks` list. Two distinct checks failed across the remaining three records, plus two unit-level checks inside the perturbation runs.

**`C-PERTURBATION-REACHED` — failed 3 times (attempts 7, 12, 19).** Verifier reason, identical each time: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This is the finding that matters most. It has now failed three separate times, across three different cost regimes — attempt 7 at `per_step_cost_ratio` 0.9657 (class A), attempt 12 at 0.8114 (class C), attempt 19 at 0.6884 (class B). Whatever was changed between those three attempts in the cost/efficiency dimension is **not** what is causing this failure: the check failed at near-baseline step cost, at intermediate step cost, and at maximally reduced step cost alike. Each time, `conformance_fraction` dropped to 0.5, `task_pass` dropped to 0.0, and reward fell to 0.4275–0.4911, roughly half the plateau. Note also that in all three cases `rule_conformance` stayed at 1.0 and `primary_target_reached` stayed at 1.0 — the primary run was fine; only the held-out perturbation run failed.

**`C-API-SURFACE` — failed once (attempt 6).** Verifier reason: *"module-level statements outside imports, constants, and permitted definitions."* This dropped `rule_conformance` to 0.8571 and `task_pass` to 0.0, and the record scored 0.7580. It has not recurred in any other record, so it appears to be a one-off structural slip in that submission rather than a persistent property of any approach: the fix is to keep module scope to imports, constant assignments, and function/class definitions only, with all executable work inside functions.

**Unit-level checks inside the perturbation runs.** `C-BUDGET-RESPECTED` failed 3 times (in attempts 7, 12 and 19), and `C-TARGET-REACHED` failed 2 times (in attempts 12 and 19). Every one of these five unit-level failures occurred on a run of kind `held_out_variant`. `C-BUDGET-RESPECTED` is the more persistent of the two: it failed in all three of the collapsed records, including attempt 7 where the target was not the problem — there, the run overran its own budget without also missing its target check. In attempts 12 and 19 both fired together, i.e. the held-out-variant run both overran its budget and failed to hit its target.

# 4. Ruled-out directions

**Maximising `compute_efficiency` / minimising `per_step_cost_ratio` as the primary lever.** Ruled out as a standalone strategy. Attempt 11 reached `compute_efficiency` 1.0000 at `per_step_cost_ratio` 0.6947 and scored 0.8067 — below the then-standing best. Attempt 19 also reached 1.0000 at 0.6884 and scored 0.4278, the second-worst result recorded, because its held-out-variant run failed `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. Attempt 16 reached 0.9805 efficiency and scored 0.7005. Efficiency at these levels is not sufficient for reward and, pushed to the extreme, coincides with the perturbation collapse.

**Increasing per-step spend or wall-clock time.** Ruled out. Attempt 8 ran 98.60 s at `per_step_cost_ratio` 1.0848 and scored 0.7805; attempt 6 ran at `per_step_cost_ratio` 1.4094 with `compute_efficiency` 0.4942 and scored 0.7580 while also failing `C-API-SURFACE`. Both are well under the ~0.866 plateau reached by runs at 74 s and cost ratio ≈ 0.95. More compute does not buy reward here.

**The intermediate cost band (`per_step_cost_ratio` ≈ 0.77–0.85).** Ruled out on the evidence available. Its two records are 0.8368 (attempt 18) and 0.4275 (attempt 12, a perturbation failure). Neither approached the plateau; the band has no demonstrated advantage over class A or over attempt 20's configuration.

**Qualifying early (driving `qualifying_budget` well below `wall_clock_sec`).** Ruled out as a reward lever on the one clean data point: attempt 9 had `qualifying_budget` 49.89 against 74.39 s wall-clock and scored 0.8332, below the class-A plateau of ~0.866 reached by attempts whose `qualifying_budget` equalled their wall-clock.

**Re-running class-A baseline-cost configurations unchanged.** Ruled out as a way to improve. Attempts 3, 5, 13 and 17 scored 0.8657, 0.8658, 0.8657 and 0.8655 — a spread of 0.0003 across four attempts. That band is saturated; small variations within it have stopped producing movement. Note that attempts 13 and 17 came *after* attempt 5 and did not beat it, so the loop spent attempts re-landing on a known plateau.

**Module-level executable code.** Ruled out by `C-API-SURFACE` in attempt 6, which zeroed `task_pass` for that record. There is no reason to reintroduce it.

# 5. Open leads

**Lead 1 — reproduce attempt 20 exactly, then perturb it minimally.** Attempt 20 is the only record that combines a low `per_step_cost_ratio` (0.7013) with a plateau-beating reward (0.8670), and it did so at `compute_efficiency` 0.9633 rather than at the 1.0000 that attempts 11 and 19 reached. That is a strong hint that the optimum sits slightly *inside* the maximum-efficiency corner, not at it. Rebuild that configuration first and confirm 0.8670 before changing anything, since the stub restarts clean and the configuration is not otherwise recoverable.

**Lead 2 — close the ~0.0012 gap by combining class-A quality with class-B cost.** The plateau of class A (0.8655–0.8658 at cost ratio 0.94–0.98, efficiency 0.68–0.73) and attempt 20 (0.8670 at cost ratio 0.70, efficiency 0.96) suggest the reward has a quality term that saturates around 0.866 and an efficiency term worth roughly a further 0.001–0.002 on top. Attempt 15 is the useful middle data point: cost ratio 0.9424 with `compute_efficiency` 0.9355 gave 0.8579, i.e. high efficiency at baseline cost was *not* enough. The lead is to hold whatever produced the class-A quality fixed and reduce per-step cost toward 0.70 without touching the parts that determine solution quality — which is apparently what separated attempt 20 from attempts 4, 11 and 16 in the same cost band.

**Lead 3 — make the held-out-variant run robust to its own budget, treating `C-BUDGET-RESPECTED` as the primary risk.** This is the highest-value single fix available: each occurrence cost roughly half the reward. Across the twenty records the perturbation outcomes by kind are: `seed` runs reached their threshold in 20 of 20 records, with zero unit-level failures ever recorded; `held_out_variant` runs reached in 17 of 20 and failed in 3. In aggregate that is 37 of 40 declared perturbation units reaching threshold, with all three failures concentrated in the `held_out_variant` kind. The `seed` kind has never been a problem and needs no work. The held-out-variant kind fails on `C-BUDGET-RESPECTED` in all three failures and additionally on `C-TARGET-REACHED` in two of them. Because the failures span cost ratios 0.6884, 0.8114 and 0.9657, the fix is not a cost-tuning fix: the algorithm needs an explicit, self-enforced budget guard on the perturbed run — a step/time accounting that stops or adapts before the run's own budget is exhausted, and a convergence path that does not depend on the run behaving like the primary one. Whatever is being tuned globally is not reaching this, since the primary run held its target (`primary_target_reached` 1.0) in every single record including all three collapses.

**Lead 4 — keep the module surface clean by construction.** Put every executable statement inside a function or class body; leave only imports, constant assignments and definitions at module level. This costs nothing and removes the `C-API-SURFACE` failure mode that took attempt 6 to `task_pass` 0.0.

**Lead 5 — target the efficiency headroom that remains at attempt 20's quality level.** Attempt 20 sits at `compute_efficiency` 0.9633; 1.0000 has been demonstrated as attainable (attempts 11 and 19). If quality can be held at attempt 20's level while efficiency moves from 0.9633 toward 1.0, that is the clearest remaining route above 0.8670. The caution attached to it is Lead 3: both records that hit efficiency 1.0000 are notable, and one of them (attempt 19) is a perturbation collapse. Any efficiency push must be validated against the held-out-variant budget guard, not just against the primary run.

**Call: exploit.** The best-scoring approach class is not exhausted — attempt 20 set a new best on its most recent showing, and it did so by combining a lever (low per-step cost) with quality retention that four earlier attempts in the same cost band failed to hold. The work is to re-derive attempt 20's configuration, protect the held-out-variant run against `C-BUDGET-RESPECTED`, and push `compute_efficiency` upward from 0.9633 while holding the quality that keeps reward at 0.866+. Exploration into higher per-step cost, longer wall-clock, or the intermediate cost band has each been measured and each came back worse. One caution on process: attempts 13 and 17 re-landed on the already-saturated class-A plateau after attempt 5 had established it, which is neither exploit nor explore — do not spend an attempt re-measuring the 0.8655–0.8658 band.
