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

    All six attempts since have scored lower than it.
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
  26       0.7607   1.000             2 of 2         yes             70                

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
  20 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 26 -- reward 0.7607, worse than an earlier attempt
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

# 1. Results so far

All 26 records carry `measurement_status: "measured"`, so every one has a real reward. None of them is an unmeasured record. Attempt 21 has a genuine measured reward of 0.0000 (`zero_reason_code: 4`, primary target never reached) — that is a measured zero, not an absent measurement.

Ranked worst to best by reward:

| Rank | Attempt | Reward | Notes from the measured terms |
|---|---|---|---|
| 1 (worst) | 21 | 0.0000 | wall_clock 1691.6668 s; no qualifying row; primary_target_reached 0; both perturbation units failed |
| 2 | 12 | 0.4275 | held-out variant not reached; task_pass 0 |
| 3 | 19 | 0.4278 | compute_efficiency 1.0000 but held-out variant not reached; task_pass 0 |
| 4 | 7 | 0.4911 | held-out variant not reached; task_pass 0 |
| 5 | 16 | 0.7005 | conformant, both perturbations held; ce 0.9805, psc 0.7055 |
| 6 | 6 | 0.7580 | C-API-SURFACE failed; rule_conformance 0.8571; task_pass 0; ce 0.4942, psc 1.4094 |
| 7 | 26 | 0.7607 | ce 0.9881, psc 0.7182, wall 69.83 s |
| 8 | 4 | 0.7740 | ce 0.9681, psc 0.6934 |
| 9 | 25 | 0.7757 | ce 0.7453, psc 0.9472 |
| 10 | 8 | 0.7805 | wall 98.5950 s, psc 1.0848 |
| 11 | 11 | 0.8067 | ce 1.0000, psc 0.6947 |
| 12 | 2 | 0.8079 | ce 0.7226, psc 0.9441 |
| 13 | 23 | 0.8170 | wall 94.7474 s |
| 14 | 9 | 0.8332 | qualifying_budget 49.8865 s vs wall 74.3877 s |
| 15 | 18 | 0.8368 | ce 0.8827, psc 0.7671 |
| 16 | 24 | 0.8426 | wall 96.1754 s, psc 1.0041 |
| 17 | 10 | 0.8503 | ce 0.7433, psc 0.9615 |
| 18 | 14 | 0.8513 | ce 0.9705, psc 0.6997 |
| 19 | 15 | 0.8579 | ce 0.9355, psc 0.9424 |
| 20 | 22 | 0.8594 | wall 70.2965 s |
| 21 | 1 | 0.8630 | first measured attempt; ce 0.6784, psc 1.0723 |
| 22 | 17 | 0.8655 | ce 0.7320, psc 0.9464 |
| 23 | 13 | 0.8657 | (0.8656561) ce 0.6829, psc 0.9710 |
| 24 | 3 | 0.8657 | (0.8657110) ce 0.6922, psc 0.9835 |
| 25 | 5 | 0.8658 | ce 0.6926, psc 0.9581 |
| 26 (best) | 20 | 0.8670 | ce 0.9633, psc 0.7013, wall 73.6617 s, all perturbations held |

**Attempt 20 holds the highest reward, 0.8670. That is the one to beat.**

Only four records ever improved on the running best: attempt 1 (first measured), then 3 (0.8657), 5 (0.8658), 20 (0.8670). Every other record is marked `worse_than_an_earlier_attempt`, and that is a regression, not progress — including the ce 1.0000 runs (11 at 0.8067 and 19 at 0.4278, both plainly below 20's 0.8670), the long-wall-clock runs (8 at 0.7805, 23 at 0.8170, 24 at 0.8426), and the entire held-out-failure family (7, 12, 19). The ceiling has moved only 0.0040 from attempt 1 (0.8630) to attempt 20 (0.8670) across all subsequent work.

# 2. Approach classes tried

The records supply metrics only, not source, so approaches are grouped by their measured cost/efficiency/outcome signature. Six distinct classes appear.

**Class A — baseline-cost, fully conformant, ~74 s runs.** Signature: per_step_cost_ratio ≈ 0.94–1.07, compute_efficiency ≈ 0.66–0.75, wall_clock ≈ 70–76 s, qualifying_budget ≈ wall_clock, both perturbation units reached. Members: 1, 2, 3, 5, 9, 10, 13, 17, 22, 25. Rewards 0.7757–0.8658. This class produces a tight plateau at 0.8655–0.8658 (17, 13, 3, 5) that four separate attempts reproduced almost exactly, and it never exceeded 0.8658. Attempt 9 is the interesting outlier inside it: qualifying_budget 49.8865 s against wall_clock 74.3877 s, i.e. the qualifying row was reached at roughly two thirds of the run, yet reward was 0.8332 — below the class plateau.

**Class B — cheap-per-step, high-efficiency runs.** Signature: per_step_cost_ratio ≈ 0.67–0.77, compute_efficiency ≈ 0.88–1.00. Members: 4 (0.7740), 11 (0.8067), 14 (0.8513), 16 (0.7005), 18 (0.8368), 20 (0.8670), 23 (0.8170), 26 (0.7607), plus the failures 19 and 21. This class contains both the single best result and the worst. Rewards inside it span 0.0000–0.8670 at near-identical cost signatures (14 at ce 0.9705/psc 0.6997 scored 0.8513; 16 at ce 0.9805/psc 0.7055 scored 0.7005; 20 at ce 0.9633/psc 0.7013 scored 0.8670). Whatever varied between those three was not the cost profile.

**Class C — intermediate cost.** per_step_cost_ratio ≈ 0.81–0.94 with elevated compute_efficiency. Members: 15 (ce 0.9355, psc 0.9424, reward 0.8579) and 12 (ce 0.8464, psc 0.8114, reward 0.4275 — held-out variant lost). Attempt 15 is the best result outside Class B's leader that also carries high efficiency, and it sits 0.0091 below attempt 20.

**Class D — long-wall-clock runs.** wall_clock ≥ 94 s: 8 (98.5950 s, 0.7805), 24 (96.1754 s, 0.8426), 23 (94.7474 s, 0.8170). All three conformed and held both perturbations, and all three scored below the ~74 s plateau.

**Class E — overhead-heavy / module-level-work variant.** Attempt 6 alone: per_step_cost_ratio 1.4094, compute_efficiency 0.4942, wall_clock 70.3708 s against qualifying_budget 45.8165 s, C-API-SURFACE failed, rule_conformance 0.8571, task_pass 0, reward 0.7580. Both perturbation units still reached.

**Class F — held-out-fragile family.** Primary target reached and rule_conformance 1.0, but the held-out variant does not reach its threshold: attempts 7 (0.4911), 12 (0.4275), 19 (0.4278). conformance_fraction 0.5 in all three, task_pass 0, reward roughly halved relative to the conformant plateau. These three span different cost profiles (7 at psc 0.9657, 12 at psc 0.8114, 19 at psc 0.6884), so this family is not tied to one cost regime.

**Class G — non-convergent long run.** Attempt 21 alone: wall_clock 1691.6668 s, qualifying_budget "not-measured", primary_target_reached 0, both perturbation units failed, reward 0.0000.

# 3. Checks that failed

Three named checks appear in the primary `failed_checks` lists, plus two named inside perturbation units.

- **C-PERTURBATION-REACHED** — "1 of 2 declared perturbations reached their own threshold inside their own budget" (attempts 7, 12, 19) and "0 of 2 declared perturbations reached their own threshold inside their own budget" (attempt 21). **This check has now failed four times.** Attempts 7, 12 and 19 differ substantially in cost profile — per_step_cost_ratio 0.9657, 0.8114 and 0.6884, compute_efficiency 0.6954, 0.8464 and 1.0000 — and every one of them still lost the same check. Whatever was changed between those attempts is not what is causing this failure. It is the single most repeated finding in the record set and it costs roughly half the reward when it fires (0.4275–0.4911 versus a conformant plateau of ~0.866).

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction" (attempt 21, primary). Also the named failure inside held-out perturbation units in attempts 12, 19 and 21, and inside the seed unit in attempt 21. Five unit-level or primary occurrences in total across four records.

- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists" (attempt 21, primary). Also the named unit-level failure in the held-out variant of attempts 7, 12, 19 and 21, and in the seed unit of attempt 21. It is the *only* unit-level failure recorded for attempt 7's held-out variant, which is the distinguishing detail there: that run did not miss the threshold outright, it missed it inside the budget.

- **C-API-SURFACE** — "module-level statements outside imports, constants, and permitted definitions" (attempt 6, once). This is the only rule_conformance failure in the whole set (0.8571; every other record is 1.0000). It set task_pass to 0 despite both perturbations holding.

`validity` is 1.0 and `red_line_crossed` is 0.0 in all 26 records. No validity or red-line check has ever failed.

# 4. Ruled-out directions

- **Module-level executable statements in the submission file.** Ruled out by attempt 6: C-API-SURFACE, "module-level statements outside imports, constants, and permitted definitions", rule_conformance 0.8571, task_pass 0, reward 0.7580. Everything must live inside imports, constants and the permitted definitions.

- **Maximising compute_efficiency as the objective.** Ruled out because it does not track reward. Attempts 11 and 19 both reached compute_efficiency 1.0000 and scored 0.8067 and 0.4278 respectively, both below attempt 20's 0.8670 and below the 0.8658 achieved at compute_efficiency 0.6926 (attempt 5). Attempts 16 (ce 0.9805 → 0.7005) and 26 (ce 0.9881 → 0.7607) confirm it. Efficiency is not the binding term.

- **Extending wall clock past ~94 s.** Ruled out by 8 (98.5950 s → 0.7805), 24 (96.1754 s → 0.8426) and 23 (94.7474 s → 0.8170), all conformant with both perturbations held, all below the ~70–76 s plateau of ~0.866. More wall clock bought nothing.

- **Very long training runs.** Ruled out by attempt 21: 1691.6668 s produced no qualifying row at all (C-TARGET-REACHED, C-BUDGET-RESPECTED, C-PERTURBATION-REACHED all failed) and a measured reward of 0.0000. Running far past the budget window does not produce a qualifying row; it destroys one.

- **Re-running the held-out-fragile configuration unchanged.** Attempts 7, 12 and 19 each lost C-PERTURBATION-REACHED on the held-out variant and each landed near 0.43–0.49. Varying the cost profile between them (psc 0.9657 → 0.8114 → 0.6884) did not touch the failing check. Repeating that family without changing the held-out margin specifically is neither exploring nor exploiting, and the record shows it was done at least three times.

- **Per-step cost above baseline as a deliberate trade.** Nothing with per_step_cost_ratio above 1.05 beat the plateau: 8 (1.0848 → 0.7805), 6 (1.4094 → 0.7580, non-conformant). Attempt 1 at 1.0723 reached 0.8630, so mildly-above-baseline is survivable, but no run in this region ever approached 0.8670.

# 5. Open leads

- **Reconstruct attempt 20's operating point and beat it from there.** Target signature: compute_efficiency ≈ 0.9633, per_step_cost_ratio ≈ 0.7013, wall_clock ≈ 73.66 s, qualifying_budget ≈ 73.66 s, conformance_fraction 1.0, both perturbation units reached, reward 0.8670. This combines a cheap per-step schedule with a fully-held perturbation set, and it is the only configuration that has done both at once.

- **The dominant unexplained variance is not cost.** Within the cheap-per-step class, attempts 14, 16, 20 and 26 sit at essentially the same cost signature (psc 0.6997–0.7182, ce 0.9633–0.9881) yet span rewards 0.7005 to 0.8670 — a 0.1665 spread. The lever that separates them is whatever governs the quality/margin of the qualifying row, not the step cost. Hold the cheap schedule fixed and vary only the accuracy-margin side.

- **Buy margin on the held-out variant specifically.** The held-out variant is the failing kind (see aggregate below). In attempt 7 its only unit-level failure was C-BUDGET-RESPECTED — the threshold was missed inside the budget rather than missed outright — so a configuration that reaches its declared threshold earlier, or declares a threshold with more headroom under variant shift, is the direct fix. In attempts 12 and 19 both C-TARGET-REACHED and C-BUDGET-RESPECTED failed on that variant, so margin, not just timing, is short there.

- **Early qualification looks available and is under-exploited.** Attempt 9 recorded qualifying_budget 49.8865 s against wall_clock 74.3877 s, and attempt 6 recorded 45.8165 s against 70.3708 s. Reaching the qualifying row well before the run ends is demonstrably achievable; neither of those runs converted it into a top reward, but pairing early qualification with attempt 20's cost profile has not been tried.

- **Seed robustness is not the constraint; do not spend effort there.** The seed unit reached its threshold in 25 of 26 records, failing only in attempt 21 where everything failed. Effort belongs on the held-out variant.

**Perturbation-unit outcomes, by kind and in aggregate.** Every record declared exactly 2 perturbations, one of kind `held_out_variant` and one of kind `seed`, giving 52 units in total. Aggregate: 47 units reached their threshold, 5 did not. By kind: the `held_out_variant` kind reached in 22 of 26 records and failed in 4 (attempts 7, 12, 19, 21) — stopped by C-BUDGET-RESPECTED alone in one case and by C-TARGET-REACHED together with C-BUDGET-RESPECTED in three. The `seed` kind reached in 25 of 26 records and failed once (attempt 21), stopped by C-TARGET-REACHED and C-BUDGET-RESPECTED. The failing kind is unambiguously the held-out variant, and the checks that stop it are C-TARGET-REACHED and C-BUDGET-RESPECTED.

**Call: exploit.** Attempt 20 at 0.8670 is the best measured result and the mark to beat. The best-scoring family has not stopped improving — it moved 0.8630 → 0.8657 → 0.8658 → 0.8670 — and there is a large, unexplained 0.1665 reward spread inside attempt 20's own cost regime that has never been attacked directly. Rebuild attempt 20's cheap-per-step, ~74 s, fully-conformant configuration, keep all code inside permitted definitions so C-API-SURFACE cannot recur, and spend the remaining effort widening the held-out variant's threshold margin so C-PERTURBATION-REACHED — which has now failed four times across four different cost profiles — cannot halve the reward again.
