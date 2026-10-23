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

    All 11 attempts since have scored lower than it.
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
  10 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 14 -- reward 0.8513, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 15 -- reward 0.8579, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 16 -- reward 0.7005, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 75
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED has failed on 2 attempts (7, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Sixteen graded submissions, all of them with `measurement_status: "measured"`, so every one carries a reward. None had `validity` below 1.0 and none crossed a red line (`red_line_crossed: 0.0`, `zero_reason_code: 0`) in any record. Ordered worst to best by reward:

| Rank | Attempt | reward | Notes from its own terms |
|---|---|---|---|
| 1 (worst) | 12 | 0.4275 | `task_pass 0.0`; failed `C-PERTURBATION-REACHED`; `conformance_fraction 0.5`; `all_perturbations_held false` |
| 2 | 7 | 0.4911 | `task_pass 0.0`; failed `C-PERTURBATION-REACHED`; `conformance_fraction 0.5`; `all_perturbations_held false` |
| 3 | 16 | 0.7005 | Clean checks, `task_pass 1.0`; `compute_efficiency 0.9805`, `per_step_cost_ratio 0.7055` |
| 4 | 6 | 0.7580 | `task_pass 0.0`; failed `C-API-SURFACE`; `rule_conformance 0.8571`; `compute_efficiency 0.4942`, `per_step_cost_ratio 1.4094` |
| 5 | 4 | 0.7740 | Clean; `compute_efficiency 0.9681`, `per_step_cost_ratio 0.6934` |
| 6 | 8 | 0.7805 | Clean; `wall_clock_sec 98.60` — by far the longest run |
| 7 | 11 | 0.8067 | Clean; `compute_efficiency 1.0000` (the maximum observed), `per_step_cost_ratio 0.6947` |
| 8 | 2 | 0.8079 | Clean; `compute_efficiency 0.7226`, `per_step_cost_ratio 0.9441` |
| 9 | 9 | 0.8332 | Clean; `qualifying_budget 49.89` vs `wall_clock_sec 74.39` |
| 10 | 10 | 0.8503 | Clean; `compute_efficiency 0.7433`, `per_step_cost_ratio 0.9615` |
| 11 | 14 | 0.8513 | Clean; `compute_efficiency 0.9705`, `per_step_cost_ratio 0.6997` |
| 12 | 15 | 0.8579 | Clean; `compute_efficiency 0.9355`, `per_step_cost_ratio 0.9424` |
| 13 | 1 | 0.8630 | Clean; first measured attempt; `per_step_cost_ratio 1.0723` |
| 14 | 13 | 0.8657 (0.8656561) | Clean; `compute_efficiency 0.6829`, `per_step_cost_ratio 0.9710` |
| 15 | 3 | 0.8657 (0.8657110) | Clean; `compute_efficiency 0.6922`, `per_step_cost_ratio 0.9835` |
| 16 (best) | 5 | 0.8658 (0.8658084) | Clean; `compute_efficiency 0.6926`, `per_step_cost_ratio 0.9581`, `wall_clock_sec 74.38` |

**Attempt 5 holds the highest reward at 0.8658 and is the one to beat.** Attempts 13 (0.8657) and 3 (0.8657) sit within two ten-thousandths of it; the three of them are effectively one plateau, and the spread among them is smaller than any deliberate change is likely to have caused.

Direction of movement must be stated plainly, because `standing_against_best_so_far` states it: only attempts 3 and 5 are marked `better_than_every_earlier_attempt`. Attempt 1 is the `first_measured_attempt`. **Every other attempt — 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 and 16 — is marked `worse_than_an_earlier_attempt`.** In particular, attempt 13 (0.8657) is a regression against attempt 5 (0.8658), not progress; attempt 16 (0.7005) is a large regression against the 0.8658 plateau; and the two most recent structural excursions, 12 (0.4275) and 7 (0.4911), are the two worst results recorded. Nothing after attempt 5 has improved on it.

## 2. Approach classes tried

I was given only the graded measurements, not the source of each submission, so these classes are grouped by their measured cost/efficiency signature. Records with the same signature and the same outcome are one entry.

**Class A — balanced-cost configuration (`per_step_cost_ratio` ≈ 0.94–0.99, `compute_efficiency` ≈ 0.68–0.75, `wall_clock_sec` ≈ 74.3).** Attempts 2 (0.8079), 3 (0.8657), 5 (0.8658), 9 (0.8332), 10 (0.8503), 13 (0.8657). This class contains the best result and three of the top four. All clean on checks, `task_pass 1.0`, both perturbation units reached. It is the productive class.

**Class B — aggressive compute reduction (`per_step_cost_ratio` ≈ 0.69–0.71, `compute_efficiency` ≈ 0.97–1.00).** Attempts 4 (0.7740), 11 (0.8067), 14 (0.8513), 16 (0.7005). All clean on checks and `task_pass 1.0`, so the cost cutting was legal — but every one of them scored below the Class A plateau, and attempt 11 achieved the maximum `compute_efficiency 1.0000` while scoring only 0.8067. Cheapness alone does not buy reward.

**Class C — intermediate cost with high efficiency (`per_step_cost_ratio` ≈ 0.94, `compute_efficiency` 0.9355).** Attempt 15 (0.8579). The best of anything outside Class A, and still below it.

**Class D — expensive / over-budget-leaning configurations (`per_step_cost_ratio` ≥ 1.07).** Attempts 1 (0.8630, ratio 1.0723, the first measured attempt) and 8 (0.7805, ratio 1.0848, `wall_clock_sec 98.60`). Attempt 1 shows a costly configuration can still score near the plateau; attempt 8 shows that stretching wall clock to ~98.6 s costs roughly 0.085 reward relative to the ~74 s plateau.

**Class E — module-surface-violating variant.** Attempt 6 (0.7580). `compute_efficiency 0.4942`, `per_step_cost_ratio 1.4094`, `rule_conformance 0.8571`, `task_pass 0.0`. This is the only class that broke an API-surface rule.

**Class F — perturbation-fragile variants.** Attempts 7 (0.4911) and 12 (0.4275). Both had `primary_target_reached 1.0` and `rule_conformance 1.0`, yet `task_pass 0.0` and `conformance_fraction 0.5`, because a held-out run failed. This class is catastrophic for reward: roughly half the plateau value.

## 3. Checks that failed

Two named checks failed at the submission level, plus two named checks inside perturbation units.

**`C-PERTURBATION-REACHED` — failed twice**, in attempt 7 and attempt 12. Verifier reason, identical in both records: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This is the finding that matters most. It has now failed in two separate attempts, and whatever was changed between those two attempts is not what is causing it — the same check with the same reason survived that change. Both records show `perturbations_declared 2.0`, `conformance_fraction 0.5`, `all_perturbations_held false`, and `task_pass 0.0`, and both are the two lowest rewards recorded (0.4911 and 0.4275). Note that both also had `primary_target_reached 1.0` and `rule_conformance 1.0`: the primary run was fine and the rules were obeyed; the failure is entirely in the held-out runs.

**`C-API-SURFACE` — failed once**, in attempt 6. Verifier reason: *"module-level statements outside imports, constants, and permitted definitions."* This drove `rule_conformance` down to 0.8571 and `task_pass` to 0.0 while both perturbation units still reached. It has not recurred in any other record.

**Inside the perturbation units**, the checks that stopped a run were `C-BUDGET-RESPECTED` (attempt 7's failing unit; and again in attempt 12's failing unit) and `C-TARGET-REACHED` (attempt 12's failing unit, alongside `C-BUDGET-RESPECTED`). So `C-BUDGET-RESPECTED` is the recurrent unit-level failure — twice — and in the worse of the two cases the run additionally never reached its target at all.

Note also that `task_pass` was 0.0 in attempts 6, 7 and 12 even though `primary_target_reached` was 1.0 in all three: reaching the primary target does not by itself produce a task pass. Conversely, all thirteen attempts with no failed checks had `task_pass 1.0`.

## 4. Ruled-out directions

**Maximising `compute_efficiency` / minimising `per_step_cost_ratio`.** Ruled out as a reward strategy. Attempt 11 reached the ceiling `compute_efficiency 1.0000` with `per_step_cost_ratio 0.6947` and scored 0.8067 — below the 0.8658 plateau. Attempt 16 reached 0.9805 efficiency at ratio 0.7055 and scored 0.7005, the worst clean result. Attempt 4 (0.9681 / 0.6934) scored 0.7740. The one partial exception, attempt 14 (0.9705 / 0.6997, reward 0.8513), still did not beat attempt 5. Four attempts in this class, none better than the plateau: driving cost down further is not where the remaining reward is.

**Long wall-clock configurations.** Ruled out. Attempt 8 ran 98.60 s — about 24 s more than the plateau's ~74.3 s — and scored 0.7805, well below attempt 5's 0.8658 at 74.38 s. Extra wall clock did not convert into reward.

**Anything that puts module-level statements outside imports, constants and permitted definitions.** Ruled out by the `C-API-SURFACE` failure in attempt 6, which forced `task_pass 0.0` and `rule_conformance 0.8571` and cost the attempt roughly 0.11 reward against the plateau despite its perturbation units both reaching. Keep the module top level to imports, constants and permitted definitions only; put all executable logic inside the permitted definitions.

**Any change that lets a held-out run exceed its own budget.** Ruled out as a reward strategy by attempts 7 (0.4911) and 12 (0.4275). Both are the lowest rewards on record, roughly half the plateau, because `conformance_fraction` halves to 0.5 and `task_pass` goes to 0.0. Whatever raises throughput or per-step cost variance enough to blow a single held-out unit's budget destroys more reward than any efficiency gain can return — attempt 12 even had a healthy `compute_efficiency 0.8464` and still scored 0.4275.

**Repeating the Class A configuration unchanged.** Attempts 3, 5 and 13 landed at 0.8657, 0.8658 and 0.8657. Re-submitting a configuration with that signature and no substantive change is not exploitation, it is re-measurement noise; it has already been done three times and the spread was under 0.0002.

## 5. Open leads

**Reproduce the attempt-5 operating point first, then perturb one lever.** Its signature is: `wall_clock_sec` ≈ 74.38, `qualifying_budget` ≈ 74.38 (equal to wall clock), `per_step_cost_ratio` 0.9581, `compute_efficiency` 0.6926, both perturbation units reached, no failed checks. Attempts 3 (ratio 0.9835) and 13 (ratio 0.9710) bracket it and land essentially level. The plateau is flat across ratio 0.958–0.984, so the remaining reward is probably not in that band's interior.

**Probe the unexplored middle of the cost curve.** Measured `per_step_cost_ratio` values cluster at ~0.69–0.71 (rewards 0.70–0.85), ~0.81 (attempt 12, invalidated by a perturbation failure so its reward tells us nothing about the configuration), ~0.94–0.98 (rewards 0.81–0.866), and ≥1.07 (rewards 0.78–0.863). The band roughly 0.85–0.93 has only one clean sample — attempt 15 at ratio 0.9424 with `compute_efficiency` 0.9355, reward 0.8579, which is notable because it got Class-B-level efficiency at Class-A-level cost ratio and came within 0.008 of the best. That combination is the single most promising untried direction: hold `per_step_cost_ratio` in the 0.94–0.96 band where the plateau lives, and try to lift `compute_efficiency` above the plateau's 0.69 toward attempt 15's 0.94 without letting the ratio drop into the 0.69–0.71 region that has never beaten 0.8513.

**Understand the `qualifying_budget` vs `wall_clock_sec` divergence.** In attempts 6, 7 and 9 these differ (45.82 vs 70.37; 50.05 vs 50.05 with wall clock also 50.05; 49.89 vs 74.39). Attempt 9 is the interesting clean case: `qualifying_budget` 49.89 while wall clock was 74.39, reward 0.8332 — below the plateau despite an otherwise Class A signature. Whatever truncates the qualifying budget relative to wall clock appears to cost reward; a run that keeps the two equal (as attempts 3, 5 and 13 do) is the safer shape.

**Harden the held-out variant path specifically.** Across all sixteen records there were thirty-two perturbation units, sixteen of kind `seed` and sixteen of kind `held_out_variant`. **All sixteen `seed` runs reached their threshold and none of them ever failed a named check.** Fourteen of the sixteen `held_out_variant` runs reached; the two that did not both failed `C-BUDGET-RESPECTED`, and one of those two additionally failed `C-TARGET-REACHED`. The failing kind is unambiguously the held-out variant, and the failing check is unambiguously the budget one. The runs are not identified beyond their kind, so nothing can be said about which variant it is or whether it is the same variant across the two records. The lead is to give the held-out variant path explicit budget headroom — an early-stopping or step-count guard that is conditioned on elapsed budget rather than on the primary run's calibration — so that a variant which converges more slowly still terminates inside its own budget. Since the seed runs have never failed, this hardening should be scoped so it does not slow the seed or primary paths and does not push `per_step_cost_ratio` above the ~0.98 region where the plateau sits.

**Reduce measurement noise before believing a small gain.** The top three results differ by 0.0002. Any candidate should be judged against 0.8658, and a result inside a few ten-thousandths of it should be treated as a tie, not an improvement.

**Call: exploit.** The productive class (balanced cost, ~74 s wall clock, `per_step_cost_ratio` ≈ 0.95–0.98, all checks clean) still holds every top result, and there is a concrete, unexhausted lever inside it — attempt 15's demonstration that high `compute_efficiency` is attainable at plateau-level cost ratio, which came within 0.008 of the best and has been sampled exactly once. Take the attempt-5 configuration, keep the module top level to imports, constants and permitted definitions so `C-API-SURFACE` cannot recur, keep every held-out run inside its own budget so `C-PERTURBATION-REACHED` cannot recur, and push efficiency upward while holding the cost ratio in the 0.94–0.98 band. Do not re-run the aggressive-cost-reduction class: four attempts there, all worse, and the mechanism is understood. Do not re-submit the plateau unchanged — that has already happened three times and produced no movement.
