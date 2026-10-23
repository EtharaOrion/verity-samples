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

    All nine attempts since have scored lower than it.
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
  9 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 12 -- reward 0.4275, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED has failed on 2 attempts (7, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Every one of the fourteen records carries `measurement_status: "measured"`, so all fourteen have a reward. None was unmeasured, none crossed a red line (`red_line_crossed: 0.0` throughout), and `validity` is 1.0 in every record.

Ordered worst to best by reward:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 12 | 0.4275 | `task_pass` 0.0; C-PERTURBATION-REACHED failed; worse than an earlier attempt |
| 2 | 7 | 0.4911 | `task_pass` 0.0; C-PERTURBATION-REACHED failed; worse than an earlier attempt |
| 3 | 6 | 0.7580 | `task_pass` 0.0; C-API-SURFACE failed; `rule_conformance` 0.8571; worse than an earlier attempt |
| 4 | 4 | 0.7740 | all checks held; worse than an earlier attempt |
| 5 | 8 | 0.7805 | all checks held; longest run at 98.5950 s wall clock; worse than an earlier attempt |
| 6 | 11 | 0.8067 | all checks held; `compute_efficiency` 1.0000, the highest recorded; still worse than an earlier attempt |
| 7 | 2 | 0.8079 | all checks held; worse than an earlier attempt |
| 8 | 9 | 0.8332 | all checks held; worse than an earlier attempt |
| 9 | 10 | 0.8503 | all checks held; worse than an earlier attempt |
| 10 | 14 | 0.8513 | all checks held; worse than an earlier attempt |
| 11 | 1 | 0.8630 | first measured attempt; all checks held |
| 12 | 13 | 0.8657 | (0.8656561 unrounded) all checks held; worse than an earlier attempt |
| 13 | 3 | 0.8657 | (0.8657110 unrounded, i.e. fractionally above attempt 13) all checks held; better than every earlier attempt at the time |
| 14 (best) | 5 | 0.8658 | all checks held; better than every earlier attempt at the time |

**Attempt 5 holds the highest reward, 0.8658, and it is the one to beat.** Attempts 3 (0.8657110) and 13 (0.8656561) sit within one ten-thousandth of it; the top three are effectively a plateau, and the differences between them are smaller than the spread seen elsewhere in the same approach class.

Directional facts that must not be softened: attempts 2, 4, 6, 7, 8, 9, 10, 11, 12, 13 and 14 are each recorded as `worse_than_an_earlier_attempt`. That includes every attempt after 5 — attempts 6 through 14 produced nine consecutive results, none of which beat the standing best. Attempt 14 (0.8513) is a regression against attempt 5 (0.8658), not progress; attempt 11 (0.8067) is a larger regression; attempts 7 (0.4911) and 12 (0.4275) are the two worst results recorded.

# 2. Approach classes tried

No source was carried forward, so the classes below are grouped by the measured signature each attempt left — chiefly `per_step_cost_ratio` (cost per step against the reference) and `compute_efficiency`. Records with the same signature and the same outcome are one entry.

**Class A — moderate cost reduction, per-step cost ratio ≈ 0.94–0.98.** Attempts 2, 3, 5, 9, 10, 13. `per_step_cost_ratio` between 0.9441 and 0.9835; `compute_efficiency` between 0.6829 and 0.7505; wall clock tightly clustered at 74.26–74.54 s. All checks held in every one; `task_pass` 1.0 in every one. Rewards 0.8079, 0.8657, 0.8658, 0.8332, 0.8503, 0.8657. **This class contains the entire top of the leaderboard, including the best result (attempt 5).** Within the class the highest rewards (attempts 3, 5, 13, all ≈ 0.8657–0.8658) came with `compute_efficiency` in the narrow band 0.6829–0.6926 and `per_step_cost_ratio` 0.9581–0.9835 — i.e. the *less* aggressively optimised members of the class, not the more efficient ones (attempts 9 and 10, efficiency 0.7433–0.7505, scored lower at 0.8332 and 0.8503).

**Class B — aggressive cost reduction, per-step cost ratio ≈ 0.69–0.70.** Attempts 4, 11, 14. `compute_efficiency` 0.9681, 1.0000, 0.9705 — the three highest efficiencies recorded. All checks held, `task_pass` 1.0, wall clock 73.74–74.15 s. Rewards 0.7740, 0.8067, 0.8513. Every member scored below the Class A best. Attempt 11 reached the maximum possible `compute_efficiency` of 1.0000 and still returned only 0.8067. This is the single most informative pattern in the data: **reward is not monotone in `compute_efficiency`**, so whatever quality term the grader also weighs is being paid for out of the cost savings, and cutting per-step cost further has been counterproductive three times.

**Class C — slower than reference, per-step cost ratio > 1.0.** Attempts 1 and 8. Attempt 1: ratio 1.0723, efficiency 0.6784, wall 76.34 s, reward 0.8630 — a strong result despite being more expensive per step than the reference. Attempt 8: ratio 1.0848, efficiency 0.6575, wall 98.5950 s (by far the longest), reward 0.7805. Both held all checks with `task_pass` 1.0. The class spans a wide reward range; the difference between them tracks the large wall-clock gap.

**Class D — variant that broke the module API surface.** Attempt 6 only. `per_step_cost_ratio` 1.4094 (the highest, i.e. slowest per step), `compute_efficiency` 0.4942 (the lowest), `qualifying_budget` 45.82 s against 70.37 s wall clock, `rule_conformance` 0.8571, `task_pass` 0.0, reward 0.7580. Failed C-API-SURFACE. Both perturbation runs still reached their thresholds.

**Class E — variants whose held-out perturbation run blew its budget.** Attempts 7 and 12. `task_pass` 0.0, `conformance_fraction` 0.5, `all_perturbations_held` false, C-PERTURBATION-REACHED failed. Attempt 7: `per_step_cost_ratio` 0.9657, efficiency 0.6954 (a Class-A-looking primary run), `qualifying_budget` 50.05 s = wall clock 50.05 s, reward 0.4911. Attempt 12: `per_step_cost_ratio` 0.8114, efficiency 0.8464, wall 74.11 s, reward 0.4275. These are the two lowest rewards on record: failing a perturbation run costs roughly 0.37–0.44 of reward relative to the Class A plateau, far more than any tuning gain observed anywhere else.

# 3. Checks that failed

Three named checks did not hold. Eleven of the fourteen records had `failed_checks: []` and `conformance_fraction: 1.0`.

**C-PERTURBATION-REACHED — failed twice**, at the top level of attempts 7 and 12. Verifier's reason, identical in both: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This check has now failed in two separate attempts. **Whatever was changed between attempt 7 and attempt 12 is not what causes it** — the two differ markedly in their primary-run signature (per-step cost ratio 0.9657 vs 0.8114; compute efficiency 0.6954 vs 0.8464) and yet the same check failed the same way in both, and in both the primary target was still reached (`primary_target_reached: 1.0`). The failure is confined to the held-out run, not the primary one.

**C-BUDGET-RESPECTED — failed twice**, both times inside a `held_out_variant` perturbation unit (attempts 7 and 12). This is the unit-level check that produced the C-PERTURBATION-REACHED failure above. Note that in attempt 7 this was the *only* unit-level check that failed: the run was stopped by budget, not by missing its target.

**C-TARGET-REACHED — failed once**, inside the `held_out_variant` unit of attempt 12, alongside C-BUDGET-RESPECTED in the same unit.

**C-API-SURFACE — failed once**, attempt 6. Verifier's reason: *"module-level statements outside imports, constants, and permitted definitions."* This is a literal structural constraint on the submission file: code that executes at import time, beyond imports, constant assignments and permitted definitions, is rejected. It cost `rule_conformance` (0.8571) and `task_pass` (0.0) even though both perturbation runs reached their thresholds. It has failed only once and has not recurred in any later record.

# 4. Ruled-out directions

**Maximising `compute_efficiency` / minimising per-step cost.** Ruled out as a route to a higher reward. Class B pushed `per_step_cost_ratio` down to 0.6934–0.6997 and `compute_efficiency` up to 0.9681, 1.0000 and 0.9705, and returned 0.7740, 0.8067 and 0.8513 — all below the best result's 0.8658, which was achieved at `compute_efficiency` 0.6926. Attempt 11 saturated efficiency at 1.0000 and still lost 0.059 of reward against attempt 5. Three independent attempts in this direction, three results below the standing best.

**Letting the run get slower in wall clock.** Ruled out by attempt 8: 98.5950 s wall clock, `per_step_cost_ratio` 1.0848, reward 0.7805 — the worst of the eleven fully-conformant results apart from attempt 4. Attempt 1 shows a per-step ratio above 1.0 is survivable (0.8630 at 1.0723, 76.34 s), but the extra 24 s in attempt 8 came with a 0.083 reward loss.

**Any change that puts executable statements at module level.** Ruled out by C-API-SURFACE in attempt 6: it zeroes `task_pass` and drops `rule_conformance` to 0.8571 regardless of how well the runs themselves perform — attempt 6's perturbations both reached their thresholds and it still landed at 0.7580.

**Any configuration whose held-out variant run exceeds its own budget.** Ruled out by attempts 7 and 12: rewards 0.4911 and 0.4275, roughly half the plateau. The primary run passing (`primary_target_reached: 1.0` in both) provides no protection. Whatever budget headroom the held-out variant needs, it is not covered by tuning that looks safe on the primary run — attempt 7's primary signature was indistinguishable from a healthy Class A run.

**Further micro-tuning inside the Class A band as it has been done so far.** Six attempts landed in this class and the top three (3, 5, 13) are separated by less than 0.0002 of reward. The class has produced the best result but has stopped improving; attempts 9, 10 and 13 all came after attempt 5 and none beat it.

# 5. Open leads

**Recover the exact Class A configuration and hold it.** The single most valuable thing the next attempt can do is land back in the band that produced 0.8657–0.8658: `per_step_cost_ratio` ≈ 0.958–0.984, `compute_efficiency` ≈ 0.683–0.693, wall clock ≈ 74.2–74.4 s, both perturbation runs reaching threshold, no module-level executable statements. That is the target signature to aim the primary run at; anything materially cheaper per step has three times scored worse.

**Look for reward in the quality term, not the cost term.** The data show reward rising as `compute_efficiency` falls across Classes A and B, which means the grader is rewarding something the efficiency number does not capture — final task quality on the primary objective. Spending the ~0.30 of per-step cost headroom that Class A leaves unused (ratio 0.958 vs the 0.694 that Class B proved achievable) on more/better optimisation per step, rather than on fewer steps, is the untried direction with the clearest supporting evidence.

**Give the held-out variant run explicit budget headroom.** C-BUDGET-RESPECTED has now stopped a `held_out_variant` run twice. Because the primary run's budget is not the binding constraint (attempts 7 and 12 both cleared it), any schedule that is sized against the primary run's observed step count is a risk. Prefer a stopping rule expressed in terms of the run's *own* budget — checking elapsed budget and terminating early with the best-so-far state — rather than a fixed step or epoch count tuned on the primary run. This converts a 0.43–0.49 catastrophe into at worst a slightly lower-quality pass.

**Treat attempt 1's profile as a hedge, not a plan.** Attempt 1 scored 0.8630 with a per-step ratio *above* 1.0, close to the plateau. That says a modestly more expensive but higher-quality step is competitive, and reinforces the lead above — but attempt 8, further in the same direction, fell to 0.7805, so there is a ceiling.

**Re-verify the module surface before submitting.** C-API-SURFACE is a cheap, purely structural check: keep the submission to imports, constant assignments and function/class definitions, with no top-level execution, no top-level prints, no top-level configuration side effects. It has failed once and is trivially avoidable.

## Perturbation-run outcomes

Across all fourteen records, `perturbations_declared` was 2.0 every time, giving 28 held-out runs in total: 14 of kind `seed` and 14 of kind `held_out_variant`. Reporting by kind, with no claim that any run in one record is the same run as in another (they are not identified, and no ordering among them is implied):

- **`seed` kind: 14 of 14 reached their threshold.** No `seed` run has ever recorded a failed check. This kind has never been a source of loss.
- **`held_out_variant` kind: 12 of 14 reached their threshold; 2 did not.** Both failures were stopped by **C-BUDGET-RESPECTED**; one of those two was additionally stopped by **C-TARGET-REACHED**. These occurred in attempts 7 and 12.
- **Aggregate: 26 of 28 held-out runs reached threshold.** Every failure is concentrated in the `held_out_variant` kind, and every one of them involves the budget check.

The finding to carry forward: **the kind of run that fails is the held-out variant, and the check it fails on is C-BUDGET-RESPECTED.**

## Call: exploit

Take the Class A approach that produced attempt 5's 0.8658 — moderate per-step cost around 0.96, compute efficiency around 0.69, ~74 s wall clock — and improve the quality achieved within that same cost envelope, while guarding the held-out variant run with an elapsed-budget-based stopping rule and keeping the module surface clean. The scoring approaches have plateaued only within the narrow tuning that has been tried; the efficiency/quality trade-off has been probed in exactly one direction (cheaper) and it lost three times, so the opposite side of that trade-off is still open and still lives inside a class that has already scored well.

For the record, no attempt scored zero and none went unmeasured, so there is no "repeated a zero-scoring approach without changing what made it zero" pattern here. The nearest analogue is the pair of held-out-variant budget failures (attempts 7 and 12), which cost more than half a reward point between them and which recurred despite substantially different primary-run configurations — that check must be addressed directly, not tuned around.
