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

    All two attempts since have scored lower than it.
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-BUDGET-RESPECTED failed on attempt 21.
    C-PERTURBATION-REACHED has failed on 4 attempts (7, 12, 19, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 21.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-two graded submissions, all with `measurement_status: measured`, so every one carries a reward. Ordered worst to best:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 21 | 0.0000 | `zero_reason_code: 4`; primary target not reached; wall clock 1691.6668 s; `qualifying_budget` "not-measured" |
| 2 | 12 | 0.4275 | one of two perturbations failed; `task_pass` 0 |
| 3 | 19 | 0.4278 | one of two perturbations failed; `task_pass` 0 |
| 4 | 7 | 0.4911 | one of two perturbations failed; `task_pass` 0 |
| 5 | 16 | 0.7005 | all perturbations held, `task_pass` 1 |
| 6 | 6 | 0.7580 | `C-API-SURFACE` failed; `rule_conformance` 0.8571; `task_pass` 0 |
| 7 | 4 | 0.7740 | clean |
| 8 | 8 | 0.7805 | clean; longest clean wall clock, 98.5950 s |
| 9 | 11 | 0.8067 | clean; `compute_efficiency` 1.0 |
| 10 | 2 | 0.8079 | clean |
| 11 | 9 | 0.8332 | clean |
| 12 | 18 | 0.8368 | clean |
| 13 | 10 | 0.8503 | clean |
| 14 | 14 | 0.8513 | clean |
| 15 | 15 | 0.8579 | clean |
| 16 | 22 | 0.8594 | clean |
| 17 | 1 | 0.8630 | clean; first measured attempt |
| 18 | 17 | 0.8655 | clean |
| 19 | 13 | 0.8657 | clean (0.86566 raw) |
| 20 | 3 | 0.8657 | clean (0.86571 raw) |
| 21 | 5 | 0.8658 | clean |
| 22 (best) | **20** | **0.8670** | clean; `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013 |

**Attempt 20 holds the highest reward, 0.8670. That is the number to beat.**

Only three attempts were ever recorded as `better_than_every_earlier_attempt`: attempt 3 (0.8657), attempt 5 (0.8658), and attempt 20 (0.8670). Attempt 1 is the `first_measured_attempt`. Every other record carries `standing_against_best_so_far: worse_than_an_earlier_attempt` — that is a regression against the then-best, not progress, and it should be read that way. In particular attempts 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21 and 22 all scored below the best standing at the time they were run.

There is a dense plateau: six attempts (17, 13, 3, 5, 22, 1) land between 0.8594 and 0.8658, and the best result, 0.8670, sits only 0.0012 above the top of that plateau. Improvements in this region are small and easily swamped.

No record was left unmeasured, so nothing here needs to be reported as "no measurement". `validity` is 1.0 and `red_line_crossed` is 0.0 in all twenty-two records; no red line has ever been tripped.

# 2. Approach classes tried

The measured terms name no source code, so the approaches are distinguishable only by their cost/efficiency signatures — `per_step_cost_ratio` (cost per step relative to the reference) and `compute_efficiency`. These group cleanly into five classes.

**Class A — at or above reference per-step cost (`per_step_cost_ratio` ≥ 1.00).** Attempts 1 (1.0723, eff 0.6784, 0.8630), 8 (1.0848, eff 0.6575, 0.7805), 6 (1.4094, eff 0.4942, 0.7580). Spending more per step than the reference. This class never beat the plateau; attempt 1 is its best at 0.8630 and it was the very first run. Attempt 8 also stretched wall clock to 98.5950 s, the longest clean run, and paid for it.

**Class B — mild cost reduction, low-to-mid efficiency (`per_step_cost_ratio` 0.93–0.99, `compute_efficiency` 0.68–0.75).** Attempts 3 (0.9835/0.6922, 0.8657), 5 (0.9581/0.6926, 0.8658), 13 (0.9710/0.6829, 0.8657), 17 (0.9464/0.7320, 0.8655), 22 (0.9380/0.6898, 0.8594), 10 (0.9615/0.7433, 0.8503), 9 (0.9516/0.7505, 0.8332), 2 (0.9441/0.7226, 0.8079), and 7 (0.9657/0.6954, 0.4911, perturbation failure). This is the most-repeated class and it produced the plateau at ~0.8655–0.8658. It is reliable but appears saturated: four separate runs in it land within 0.0003 of each other.

**Class C — aggressive cost reduction, high efficiency (`per_step_cost_ratio` 0.67–0.71, `compute_efficiency` 0.96–1.00).** Attempts 20 (0.7013/0.9633, **0.8670** — the best result), 14 (0.6997/0.9705, 0.8513), 4 (0.6934/0.9681, 0.7740), 16 (0.7055/0.9805, 0.7005), 11 (0.6947/1.0000, 0.8067), 19 (0.6884/1.0000, 0.4278, perturbation failure), 21 (0.6727/0.9829, 0.0000, total failure). This class contains both the single best result and the two worst non-zero results and the only zero. Note that attempts 4, 14 and 20 have nearly identical cost signatures (0.6934/0.9681, 0.6997/0.9705, 0.7013/0.9633) and rewards of 0.7740, 0.8513 and 0.8670 — a spread of 0.0930 across effectively the same cost profile. Whatever separates them is not the per-step cost; it is the quality margin the run achieves, and that is the variable actually being graded here.

**Class D — intermediate cost with high efficiency (`per_step_cost_ratio` 0.77–0.85).** Attempts 18 (0.7671/0.8827, 0.8368), 12 (0.8114/0.8464, 0.4275, perturbation failure), 15 (0.9424/0.9355, 0.8579 — mild cost but unusually high efficiency, the only run to combine the two). Attempt 15 is worth singling out: it reached efficiency 0.9355 at a Class-B cost ratio and scored 0.8579, near the plateau but not above it.

**Class E — long-running.** Attempt 21 alone: 1691.6668 s wall clock, over twenty times any other run, `compute_efficiency` 0.9829 and the cheapest per-step ratio measured (0.6727), and it reached nothing at all. Reward 0.0000.

The central observation across classes: reward is **not** monotone in `compute_efficiency`. Attempt 11 achieved `compute_efficiency` 1.0 and scored 0.8067; attempt 16 achieved 0.9805 and scored 0.7005; attempt 3 achieved only 0.6922 and scored 0.8657. Efficiency is a secondary term. The dominant term is reaching the target with margin on the primary run *and* on both perturbation runs.

# 3. Checks that failed

Four distinct checks have failed, across five records.

**`C-PERTURBATION-REACHED` — failed four times (attempts 7, 12, 19, 21).** This is the finding that matters most. In attempts 7, 12 and 19 the reason was "1 of 2 declared perturbations reached their own threshold inside their own budget". In attempt 21 the reason was "0 of 2 declared perturbations reached their own threshold inside their own budget". Those four attempts span three different approach classes — 7 is Class B (cost 0.9657), 12 is Class D (0.8114), 19 and 21 are Class C (0.6884, 0.6727). Whatever was changed between those attempts is **not** what causes this check to fail: it has failed at mild cost reduction, at intermediate cost reduction and at aggressive cost reduction alike. The cost/efficiency dial is not the lever on this check.

The reward cost of this failure is severe and consistent: attempts 7, 12 and 19 scored 0.4911, 0.4275 and 0.4278 while their primary target was reached (`primary_target_reached` 1.0) and `conformance_fraction` fell to 0.5. Losing one perturbation costs roughly 0.37–0.44 reward against the plateau. Nothing else measured here costs that much.

**`C-BUDGET-RESPECTED` — failed as a primary check once (attempt 21), reason "no qualifying row, so no budget position exists". It also failed inside perturbation units four times** (see section on perturbation units below).

**`C-TARGET-REACHED` — failed as a primary check once (attempt 21), reason "no evaluation row crosses the threshold in the declared direction". It also failed inside perturbation units three times.**

**`C-API-SURFACE` — failed once (attempt 6), reason "module-level statements outside imports, constants, and permitted definitions".** This dropped `rule_conformance` to 0.8571 and `task_pass` to 0 while `conformance_fraction` stayed 1.0 and both perturbations held. Reward 0.7580. This is a purely structural violation: the submission put executable statements at module level. It has appeared exactly once and has not recurred, so keeping the module body to imports, constants and permitted definitions is a solved constraint — but the stub restarts each time, so it must be re-honoured deliberately, not assumed.

### Perturbation-unit outcomes

Every record declares exactly two perturbation units, one of kind `held_out_variant` and one of kind `seed`. That is 44 units across the twenty-two records; 39 held and 5 did not.

By kind:

- **`held_out_variant`: 4 failures out of 22 (attempts 7, 12, 19, 21).** In attempt 7 the only failing check on this unit was `C-BUDGET-RESPECTED` — it got where it needed to go but not inside its own budget. In attempts 12, 19 and 21 the unit failed both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. **This kind is the fragile one.** `C-BUDGET-RESPECTED` failed on a held-out-variant unit in all four cases; `C-TARGET-REACHED` in three of the four.
- **`seed`: 1 failure out of 22 (attempt 21), on both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`** — and that occurred only in the record where the primary run itself reached nothing. In every record where the primary run succeeded, the seed unit held. The seed perturbation is not the problem.

In aggregate: 18 of 22 records had `all_perturbations_held: true`. All four failures involve the held-out-variant kind, and the check that stopped it every single time is `C-BUDGET-RESPECTED`. The runs are not individually identified, so no claim is made that the same physical run recurs across records — only that the *kind* that fails is the held-out variant, and the *check* it fails is the budget check.

# 4. Ruled-out directions

**Module-level executable statements.** Ruled out by `C-API-SURFACE` on attempt 6: "module-level statements outside imports, constants, and permitted definitions". It zeroed `task_pass` and cut `rule_conformance` to 0.8571 despite an otherwise clean run, costing roughly 0.11 against the plateau. Keep the module body to imports, constants and function/class definitions.

**Long wall-clock runs.** Ruled out by attempt 21: 1691.6668 s, `qualifying_budget` "not-measured", `primary_target_reached` 0.0, all four checks failed, reward 0.0000 with `zero_reason_code: 4`. Every other run finished between 70.30 s and 98.60 s. Extending run time past that band does not merely fail to help — it produced the only zero on record. There is a hard budget position and a long run has no qualifying row at all.

**Spending more per step than the reference (`per_step_cost_ratio` > 1.0).** Ruled out by attempts 1 (1.0723 → 0.8630), 8 (1.0848 → 0.7805) and 6 (1.4094 → 0.7580). Three runs, all below the plateau, monotonically worse as cost rose. There is no evidence a costlier step buys quality here.

**Maximising `compute_efficiency` as the objective.** Ruled out by attempts 11 (efficiency 1.0000 → 0.8067) and 16 (efficiency 0.9805 → 0.7005), against attempt 3 (efficiency 0.6922 → 0.8657). Pushing efficiency to its ceiling has twice landed well below runs with efficiency in the 0.69 range. Efficiency is a minor term in the reward; treating it as the target inverts the priorities.

**Cutting per-step cost below roughly 0.69 of reference.** The two cheapest runs measured are attempt 21 (0.6727 → 0.0000) and attempt 19 (0.6884 → 0.4278, held-out variant failed target and budget). Both broke. Attempt 11 at 0.6947 held its perturbations but scored only 0.8067. The productive band appears to bottom out near 0.70, where attempt 20 sits.

**Further repetition of the Class-B mild-cost profile at face value.** Attempts 3, 5, 13 and 17 landed at 0.8657, 0.8658, 0.8657 and 0.8655 — four runs within 0.0003 of each other and all below 0.8670. This class has stopped improving. Re-running it as-is is not exploitation, it is repetition; if earlier work kept returning to it hoping for a different number, that is the pattern to break.

# 5. Open leads

**Reconstruct attempt 20's profile.** It is the only run to clear the plateau, at 0.8670. Its signature: `per_step_cost_ratio` 0.7013, `compute_efficiency` 0.9633, wall clock 73.6617 s, `qualifying_budget` 73.6617 s, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, both perturbation units reached. Target that signature: aggressive but not extreme per-step cost reduction (aim ~0.70, do not go under ~0.69), efficiency in the 0.95–0.97 range rather than pushed to 1.0, total wall clock in the low 70s.

**Resolve the Class-C spread, which is the largest single opportunity.** Attempts 4, 14 and 20 have almost identical cost signatures and rewards of 0.7740, 0.8513 and 0.8670. A 0.0930 reward spread at constant cost profile means the reward is being driven by how far past the threshold the evaluation row lands, not by speed. Whatever produces margin — more conservative optimisation settings, better initialisation, a slightly longer effective schedule within the same wall-clock band — is where the remaining headroom is. Deliberately trade a little of attempt 20's efficiency back for margin and see whether reward rises; attempt 15 (cost 0.9424, efficiency 0.9355, reward 0.8579) shows an unexplored middle of the cost/efficiency plane that has only been sampled once.

**Build explicit headroom into the held-out-variant run.** `C-BUDGET-RESPECTED` stopped the held-out-variant unit in all four of its failures, and `C-PERTURBATION-REACHED` has now failed four separate times across three different cost classes — so tuning cost is demonstrably not the fix. The lead is to make the stopping rule budget-aware rather than fixed: whatever schedule length, patience or iteration count the primary run uses, the held-out variant needs to converge and record a qualifying row comfortably inside its own budget, not at the edge of it. Attempt 7 is the diagnostic case — the unit reached its threshold but missed the budget, meaning the work was right and only the timing was wrong. Leaving 20–25% budget slack on that unit is worth more than 0.37 reward, far more than any efficiency gain available.

**Do not let a margin-tightening experiment silently break the primary target.** Attempt 21 shows the failure mode when the primary run itself stops qualifying: reward drops from ~0.86 to 0.0000 in one step. Any change that shortens or cheapens the run should be checked against `primary_target_reached` first.

**Call: exploit.** The best-scoring approach class (Class C, aggressive cost reduction at ~0.70 per-step ratio) contains both the top result and its own worst outcomes, which means it is under-controlled rather than exhausted — attempt 20 proved 0.8670 is reachable within it, and attempts 4 and 14 show 0.09 of reward is being lost to something other than cost. Rebuild attempt 20's cost/efficiency signature, add explicit budget slack on the held-out-variant perturbation so `C-BUDGET-RESPECTED` cannot bite, keep the module body free of executable statements so `C-API-SURFACE` stays clean, and keep total wall clock in the low 70s. Do not re-run the Class-B mild-cost profile unchanged: it has now been sampled four times at 0.8655–0.8658 and has stopped moving.
