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

    All four attempts since have scored lower than it.
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
  3 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.8630, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 7 -- reward 0.4911, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 8 -- reward 0.7805, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 99
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.8332, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED failed on attempt 7.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Nine graded submissions, all with `measurement_status: "measured"`, so all nine carry a reward. Listed worst to best:

| Rank | Attempt | reward | standing |
|---|---|---|---|
| 1 (worst) | 7 | 0.4911 | worse than an earlier attempt |
| 2 | 6 | 0.7580 | worse than an earlier attempt |
| 3 | 4 | 0.7740 | worse than an earlier attempt |
| 4 | 8 | 0.7805 | worse than an earlier attempt |
| 5 | 2 | 0.8079 | worse than an earlier attempt |
| 6 | 9 | 0.8332 | worse than an earlier attempt |
| 7 | 1 | 0.8630 | first measured attempt |
| 8 | 3 | 0.8657 | better than every earlier attempt |
| 9 (best) | 5 | 0.8658 | better than every earlier attempt |

**Attempt 5 holds the highest reward at 0.8658. That is the number to beat.**

Attempt 3 (0.8657) is effectively tied with it — the gap is 0.0001 — and attempt 1 (0.8630) sits just below both. Those three form the top cluster; everything else is materially lower.

Plainly stated regressions: attempt 2 (0.8079) is lower than attempt 1 (0.8630). Attempt 4 (0.7740) is lower than attempts 1, 3 and 5. Attempt 6 (0.7580) is lower than every attempt before it except none — it is below all of 1–5. Attempt 7 (0.4911) is the worst result recorded, far below everything preceding it. Attempt 8 (0.7805) is lower than attempts 1, 3 and 5. Attempt 9 (0.8332) is lower than attempts 1, 3 and 5, so the most recent work is a regression against the best, not progress toward it.

Supporting per-record terms worth carrying forward (all nine had `validity = 1.0`, `red_line_crossed = 0.0`, `zero_reason_code = 0`, `primary_target_reached = 1.0`, and `perturbations_declared = 2.0`):

| Attempt | reward | compute_efficiency | per_step_cost_ratio | wall_clock_sec | qualifying_budget | task_pass | rule_conformance | conformance_fraction |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.8630 | 0.6784 | 1.0723 | 76.34 | 76.34 | 1.0 | 1.0 | 1.0 |
| 2 | 0.8079 | 0.7226 | 0.9441 | 74.26 | 74.26 | 1.0 | 1.0 | 1.0 |
| 3 | 0.8657 | 0.6922 | 0.9835 | 74.37 | 74.37 | 1.0 | 1.0 | 1.0 |
| 4 | 0.7740 | 0.9681 | 0.6934 | 73.74 | 73.74 | 1.0 | 1.0 | 1.0 |
| 5 | 0.8658 | 0.6926 | 0.9581 | 74.38 | 74.38 | 1.0 | 1.0 | 1.0 |
| 6 | 0.7580 | 0.4942 | 1.4094 | 70.37 | 45.82 | 0.0 | 0.8571 | 1.0 |
| 7 | 0.4911 | 0.6954 | 0.9657 | 50.05 | 50.05 | 0.0 | 1.0 | 0.5 |
| 8 | 0.7805 | 0.6575 | 1.0848 | 98.60 | 98.60 | 1.0 | 1.0 | 1.0 |
| 9 | 0.8332 | 0.7505 | 0.9516 | 74.39 | 49.89 | 1.0 | 1.0 | 1.0 |

The single most important cross-record fact: **compute efficiency and reward move in opposite directions over most of the range.** The cheapest, most efficient run (attempt 4: `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934) scored 0.7740, well below the top cluster, and attempt 9 (efficiency 0.7505) scored 0.8332, also below it. The top cluster all sit near `compute_efficiency` ≈ 0.68–0.69 with `per_step_cost_ratio` ≈ 0.96–1.07 and `wall_clock_sec` ≈ 74–76. The reward is therefore not dominated by cheapness; buying efficiency by spending less per step has cost more reward than it gained, every time it was tried.

# 2. Approach classes tried

Grouped by what was actually varied, as visible in the measured terms. Records that failed the same way are collapsed into one entry.

**A. Baseline-cost conformant run (attempt 1 — 0.8630).** Per-step cost slightly above the reference (`per_step_cost_ratio` 1.0723), efficiency 0.6784, wall clock 76.34 s. Full conformance, both perturbation units reached. This established that the straightforward configuration clears the primary target and every check, and set the bar at 0.8630.

**B. Mild cost trimming at ~74 s wall clock (attempts 2, 3, 5 — 0.8079, 0.8657, 0.8658).** Per-step cost pulled just under the reference (0.9441, 0.9835, 0.9581), efficiency 0.69–0.72, wall clock 74.26–74.38 s, all fully conformant with both units reached. This class contains the two best results and also one of the weaker ones. The cost terms across 2, 3 and 5 are nearly identical, so the 0.058 spread between attempt 2 (0.8079) and attempts 3/5 (0.8657, 0.8658) is **not** explained by cost — something in the learning configuration itself, at essentially the same budget, was worth ~0.058 of reward. Attempt 2's slightly higher efficiency (0.7226 vs 0.6922/0.6926) alongside its lower reward reinforces that the difference was a quality-side, not a spend-side, effect.

**C. Aggressive per-step cost reduction (attempt 4 — 0.7740).** Cost driven hard down: `per_step_cost_ratio` 0.6934, `compute_efficiency` 0.9681 — by far the best efficiency of any record — wall clock 73.74 s. Fully conformant, both units reached, `task_pass` 1.0. Reward fell to 0.7740, 0.0918 below attempt 5. Cutting per-step cost by ~30% bought efficiency and lost far more elsewhere.

**D. Heavier / longer run (attempt 8 — 0.7805).** Wall clock pushed to 98.60 s with `per_step_cost_ratio` 1.0848 and efficiency down to 0.6575. Fully conformant, both units reached, `task_pass` 1.0. Reward 0.7805, 0.0853 below attempt 5. Spending more wall clock than the ~74 s band also lost reward.

**E. Truncated qualifying budget with full wall clock (attempt 9 — 0.8332).** Distinctive signature: `wall_clock_sec` 74.39 but `qualifying_budget` only 49.89 — the qualifying window closed well before the run ended, the first fully-conformant record where those two numbers diverge. Efficiency 0.7505, per-step 0.9516, `task_pass` 1.0, both units reached, no failed checks. Reward 0.8332 — a regression of 0.0326 against attempt 5. Reaching the target earlier in the budget did not pay for what was given up.

**F. Configuration that broke the module API surface (attempt 6 — 0.7580).** The only record with `rule_conformance` below 1.0 (0.8571) and the only `C-API-SURFACE` failure. `task_pass` dropped to 0.0. Also the most expensive per step of any record (`per_step_cost_ratio` 1.4094, efficiency 0.4942) with `qualifying_budget` 45.82 against `wall_clock_sec` 70.37. Both perturbation units still reached. Reward 0.7580.

**G. Budget-shrinking configuration that starved the held-out variant (attempt 7 — 0.4911).** Wall clock and qualifying budget both cut to 50.05 s. The primary run still reached its target (`primary_target_reached` 1.0) and `rule_conformance` stayed 1.0, but `conformance_fraction` fell to 0.5, `all_perturbations_held` went false, `task_pass` 0.0, and the reward collapsed to 0.4911 — the worst recorded, 0.3747 below attempt 5. This is the clearest signal in the whole record set: the penalty for a perturbation unit missing its threshold dwarfs any cost saving.

# 3. Checks that failed

Two records carry failed checks; seven carry none.

**`C-API-SURFACE`** — attempt 6 only. Verifier reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions"*. This one failure pulled `rule_conformance` to 0.8571 and `task_pass` to 0.0. It has failed **once** across all nine records. The submission must confine module scope to imports, constants and permitted definitions — no executable statements at module level (no top-level calls, no top-level assignments beyond plain constants, no top-level seeding, config construction, device probing, printing or `if __name__` side effects). Put all such work inside the permitted function definitions.

**`C-PERTURBATION-REACHED`** — attempt 7 only, at the record level. Verifier reason, verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget"*. `conformance_fraction` 0.5, `all_perturbations_held` false, `task_pass` 0.0.

**`C-BUDGET-RESPECTED`** — attempt 7 only, at the unit level, on the held-out-variant run. This is the underlying cause of the `C-PERTURBATION-REACHED` failure above: that unit did not reach its threshold inside its own budget.

No check has failed more than once, and no check appears in two different records. There is therefore no single recurring conformance finding across this record set; the two failures are distinct, one-off, and each is attributable to the specific configuration of the attempt that produced it. Both `C-API-SURFACE` and the budget failure are avoidable by construction and neither appeared in any of the seven clean records, including the three best.

Note also that `task_pass` is 0.0 in attempts 6 and 7 yet both still carry a reward (0.7580 and 0.4911). A failed check does not zero the reward here, but it is expensive — and in attempt 7's case, catastrophically so.

# 4. Ruled-out directions

**Aggressive per-step cost reduction.** Attempt 4 achieved `compute_efficiency` 0.9681 and `per_step_cost_ratio` 0.6934, the best cost profile in the record set, and scored 0.7740 — 0.0918 below the best. Cheapening the per-step work is not the reward lever; it is a reward sink.

**Extending the wall clock beyond the ~74 s band.** Attempt 8 ran 98.60 s at `per_step_cost_ratio` 1.0848 and scored 0.7805, 0.0853 below the best, while remaining fully conformant. More time did not translate into more reward.

**Closing the qualifying window early while still running the full wall clock.** Attempt 9's `qualifying_budget` of 49.89 against a 74.39 s wall clock produced 0.8332, a 0.0326 regression against attempt 5 despite higher efficiency (0.7505) and a clean check sheet. Front-loading the target within a shorter qualifying window is not free.

**Cutting the total budget to ~50 s.** Attempt 7 did this and the held-out-variant unit failed `C-BUDGET-RESPECTED`, taking `conformance_fraction` to 0.5 and the reward to 0.4911, the worst on record. The held-out variant needs more headroom than the primary run does; a budget the primary run clears comfortably is not necessarily one the variant clears.

**Any module-level executable code.** Attempt 6 failed `C-API-SURFACE` on *"module-level statements outside imports, constants, and permitted definitions"*, losing `task_pass` and ~0.108 of reward against the best. Non-negotiable structural constraint.

**Attempt 2's specific configuration within class B.** At virtually the same budget as attempts 3 and 5 it scored 0.8079, ~0.058 lower. Whatever it varied on the quality side was a step backwards; the 3/5 configuration is the one to reproduce, not the 2 configuration.

# 5. Open leads

**Reproduce the attempt-5 / attempt-3 operating point first, exactly.** Target `wall_clock_sec` ≈ 74.4 s, `per_step_cost_ratio` ≈ 0.96–0.98, `compute_efficiency` ≈ 0.692, `qualifying_budget` equal to the wall clock (not truncated), full conformance, both perturbation units reaching. That profile produced 0.8657 and 0.8658 twice, independently, which makes it a reliable base rather than a lucky sample. Everything else should be a delta on top of it.

**Improve quality at fixed budget, not cost at fixed quality.** The spread within class B (0.8079 vs 0.8658 at near-identical cost terms) is direct evidence that ~0.058 of reward is available from the learning configuration alone with the compute profile held constant. Concretely: optimizer and schedule choices (learning-rate schedule shape, warmup, final decay), regularisation, initialisation, batch composition, and any averaging of the final weights — all of which change the result without changing per-step cost or step count. Hold `per_step_cost_ratio` in the 0.95–1.00 band while doing so and verify it did not drift.

**Treat ~0.866 as a plateau to be broken, not a ceiling to be re-touched.** Attempts 3 and 5 differ by 0.0001, so simply re-running near that point will not advance the number. A delta needs to be a real change to the quality side, then measured against 0.8658.

**Do not spend the safety margin on the held-out variant.** Attempt 1 ran at `per_step_cost_ratio` 1.0723 and 76.34 s and still scored 0.8630 with both units reaching, so there is a little slack above the 74 s band. Attempt 7 shows there is none below ~50 s. If a change makes the run slower, prefer letting it run at 76 s over cutting steps to fit.

**Keep the module surface trivially clean.** Imports, plain constants, and the permitted definitions only. Any seeding, device selection, configuration assembly or logging belongs inside the functions. This is cheap insurance against re-losing `task_pass` the way attempt 6 did.

**Verdict: exploit.** Class B is the approach that scored, its best point is reproducible (0.8657 and 0.8658 from two separate attempts), and the ~0.058 within-class spread shows it has not yet been optimised — the quality-side levers at fixed compute are untried in the direction that helped. Every structurally different direction attempted so far (cheaper steps, longer runs, truncated qualifying window, shorter total budget) produced a measured regression, so exploring further along those axes is not warranted. Note for the record that the cost-cutting idea was pursued in several distinct forms (attempts 4, 7, 9) and regressed each time without the underlying premise being revisited; do not repeat it again unchanged.
