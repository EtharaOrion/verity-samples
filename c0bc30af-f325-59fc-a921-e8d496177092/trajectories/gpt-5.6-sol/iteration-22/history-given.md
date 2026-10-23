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

    All one attempts since have scored lower than it.
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
  16 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 19 -- reward 0.4278, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-BUDGET-RESPECTED failed on attempt 21.
    C-PERTURBATION-REACHED has failed on 4 attempts (7, 12, 19, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 21.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-one graded records, all with `measurement_status: measured`, so every one carries a reward. Listed worst to best:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 | 21 | 0.0000 | `zero_reason_code: 4`, `primary_target_reached: 0`, `task_pass: 0`, `qualifying_budget: not-measured`, `wall_clock_sec: 1691.67` |
| 2 | 12 | 0.4275 | `task_pass: 0`, one perturbation lost |
| 3 | 19 | 0.4278 | `task_pass: 0`, one perturbation lost |
| 4 | 7 | 0.4911 | `task_pass: 0`, one perturbation lost |
| 5 | 16 | 0.7005 | all checks held, `compute_efficiency` 0.9805 |
| 6 | 6 | 0.7580 | `task_pass: 0`, `rule_conformance: 0.8571` |
| 7 | 4 | 0.7740 | all checks held, `compute_efficiency` 0.9681 |
| 8 | 8 | 0.7805 | all checks held, `wall_clock_sec` 98.60 |
| 9 | 11 | 0.8067 | all checks held, `compute_efficiency` 1.0000 |
| 10 | 2 | 0.8079 | all checks held |
| 11 | 9 | 0.8332 | all checks held |
| 12 | 18 | 0.8368 | all checks held |
| 13 | 10 | 0.8503 | all checks held |
| 14 | 14 | 0.8513 | all checks held |
| 15 | 15 | 0.8579 | all checks held |
| 16 | 1 | 0.8630 | first measured attempt |
| 17 | 17 | 0.8655 | all checks held |
| 18 | 13 | 0.8657 | (0.865656 unrounded) |
| 19 | 3 | 0.8657 | (0.865711 unrounded) |
| 20 | 5 | 0.8658 | all checks held |
| 21 | **20** | **0.8670** | **highest reward; this is the one to beat** |

Attempt 20 holds the highest reward at 0.8670 and is the mark to beat. Only four attempts were ever recorded as `better_than_every_earlier_attempt`: 3 (0.8657), 5 (0.8658) and 20 (0.8670), plus attempt 1 as the first measurement. Every other record is explicitly `worse_than_an_earlier_attempt` — that includes attempts 21, 19, 16, 14, 15, 17, 13, 18, 11, 12, 10, 9, 8, 7, 6, 4 and 2. Those are regressions, not progress, and several of them (13, 17) came within a thousandth of the leader while still being strictly below it.

Attempt 21 produced a measured reward of exactly 0.0000; it is a genuine zero, not a missing measurement. No record in this set is unmeasured.

The distribution matters as much as the ranking: fourteen of twenty-one attempts landed between 0.80 and 0.867, and the top six are spread over 0.8630–0.8670. The scoring surface around the leader is flat to within about 0.004. Movement inside that band is noise-sized; the large reward differences all come from checks failing, not from tuning.

# 2. Approach classes tried

The records carry no source, so the classes below are reconstructed from the measured knobs: `compute_efficiency`, `per_step_cost_ratio`, `wall_clock_sec` and `qualifying_budget`. Each class is described by its measured signature so the next attempt can re-derive it.

**Class A — moderate-speed, quality-first configuration (`per_step_cost_ratio` ≈ 0.94–0.98, `compute_efficiency` ≈ 0.68–0.75, wall clock ≈ 74–76 s).** Attempts 2, 3, 5, 9, 10, 13, 15, 17, and attempt 1 as a slightly slower relative (`per_step_cost_ratio` 1.0723, wall clock 76.34). This class is the reliable scorer: every member held every check, `task_pass: 1`, `conformance_fraction: 1.0`, both perturbation units reached. Its rewards cluster tightly at 0.8655–0.8658 (attempts 3, 5, 13, 17) with weaker members at 0.8079 (2), 0.8332 (9), 0.8503 (10) and 0.8579 (15). The class ceiling is roughly 0.8658 — it saturates. Note that within this class, `compute_efficiency` moved from 0.6784 to 0.7504 with essentially no reward gain, so the per-step cost is not what the class is trading on.

**Class B — high-efficiency, low per-step-cost configuration (`per_step_cost_ratio` ≈ 0.69–0.77, `compute_efficiency` ≈ 0.88–1.00, wall clock ≈ 73.7–75.3 s).** Attempts 4, 11, 14, 16, 18 and 20. All held every check. Rewards are wildly inconsistent: 0.7005 (16, `compute_efficiency` 0.9805), 0.7740 (4, 0.9681), 0.8067 (11, `compute_efficiency` 1.0000 — a perfect efficiency score paired with a middling reward), 0.8368 (18), 0.8513 (14), and 0.8670 (20, `compute_efficiency` 0.9633). This is the decisive finding of the whole run: **maximising `compute_efficiency` does not maximise reward.** Attempt 11 achieved the theoretical maximum efficiency of 1.0000 and scored 0.8067, well below Class A's saturated 0.8658. Attempt 20 achieved 0.9633 — deliberately *not* the maximum — and took the lead at 0.8670. Whatever else attempt 20 did, it preserved the task-quality that attempts 4, 11 and 16 lost while cutting per-step cost to 0.7013.

**Class C — aggressive-speed / short-budget configurations that broke the held-out run.** Attempts 7, 12 and 19. Each has `conformance_fraction: 0.5`, `task_pass: 0`, `all_perturbations_held: false`, and rewards of 0.4911, 0.4275 and 0.4278 respectively — roughly half of what a conforming attempt scores. Attempt 7 ran a short 50.05 s with `qualifying_budget` 50.05; attempt 19 ran at `compute_efficiency` 1.0000 with `per_step_cost_ratio` 0.6884; attempt 12 sat between them at 0.8464 / 0.8114. Different speeds, same failure. The primary run passed in all three (`primary_target_reached: 1.0`) — the loss was entirely in the held-out variant.

**Class D — module-level-statement variant.** Attempt 6 alone. `rule_conformance` 0.8571, `task_pass: 0`, `per_step_cost_ratio` 1.4094, `compute_efficiency` 0.4942, `qualifying_budget` 45.82 against a wall clock of 70.37. Reward 0.7580. Both perturbation units reached; the loss came purely from the API-surface check.

**Class E — long-run / over-training configuration.** Attempt 8, at `wall_clock_sec` 98.60 and `qualifying_budget` 98.60, `per_step_cost_ratio` 1.0848, `compute_efficiency` 0.6575. It held every check but scored 0.7805, below the Class A cluster that ran ~24 s shorter. Spending more wall clock actively hurt.

**Class F — the runaway.** Attempt 21, `wall_clock_sec` 1691.67 — roughly 23× the ~74 s that every other attempt took — with `compute_efficiency` 0.9829 and `per_step_cost_ratio` 0.6727. It reached nothing: `primary_target_reached: 0`, `qualifying_budget: not-measured`, `conformance_fraction: 0.0`, both perturbation units failed, reward 0.0000, `zero_reason_code: 4`. The combination of a very low per-step cost with an enormous wall clock is consistent with a run that never converged and kept iterating rather than one that was cut off.

Across every record, `validity` is 1.0 and `red_line_crossed` is 0.0. Nothing has ever tripped a safety or validity gate; the losses are all target, budget and API-surface losses.

# 3. Checks that failed

**C-PERTURBATION-REACHED — failed 4 times (attempts 7, 12, 19, 21).** This is the dominant failure of the entire run and the single finding that matters most. Verifier reason on attempts 7, 12 and 19: "1 of 2 declared perturbations reached their own threshold inside their own budget." On attempt 21: "0 of 2 declared perturbations reached their own threshold inside their own budget." Those four attempts span very different configurations — a 50 s short run (7), a mid-speed run (12), a maximum-efficiency run (19) and a 1691 s runaway (21) — with `compute_efficiency` ranging from 0.6954 to 1.0000 and `per_step_cost_ratio` from 0.6727 to 0.9657. **Whatever was changed between those four attempts is not what causes this check to fail.** The knobs were varied across nearly their whole observed range and the check kept failing; the cause lies elsewhere, in whatever makes the held-out variant unable to hit its own threshold inside its own budget rather than in the speed/cost trade.

**C-BUDGET-RESPECTED — failed once at the top level (attempt 21),** reason: "no qualifying row, so no budget position exists." It also appears repeatedly inside perturbation units (see below).

**C-TARGET-REACHED — failed once at the top level (attempt 21),** reason: "no evaluation row crosses the threshold in the declared direction." Also appears inside perturbation units.

**C-API-SURFACE — failed once (attempt 6),** reason: "module-level statements outside imports, constants, and permitted definitions." This drove `rule_conformance` to 0.8571 and `task_pass` to 0 on an attempt whose perturbations both held. It is a single, isolated, and mechanically fixable defect: keep the submission module free of executable statements at module scope, restricting top level to imports, constants and permitted definitions.

**Perturbation-unit outcomes.** Every record declared 2 perturbations, one of kind `held_out_variant` and one of kind `seed`. Across 21 records that is 42 held-out runs.

- *By kind — `held_out_variant`:* reached its threshold in 17 of 21 records; failed in 4 (attempts 7, 12, 19, 21). On attempt 7 it was stopped by `C-BUDGET-RESPECTED` alone. On attempts 12, 19 and 21 it was stopped by both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.
- *By kind — `seed`:* reached its threshold in 20 of 21 records; failed exactly once, in attempt 21, stopped by `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` — the same attempt in which the primary run also failed outright.
- *Aggregate:* 37 of 42 held-out runs reached their threshold; 5 did not. Four of those five failures were of kind `held_out_variant`.

The pattern is unambiguous: **the run that fails is the `held_out_variant` kind, and the checks it fails on are `C-BUDGET-RESPECTED` and, in three of the four cases, `C-TARGET-REACHED` as well.** The `seed` kind is essentially robust — it only broke when the whole submission broke. Note that the run identities are not disclosed; there is no basis for saying that the failing held-out variant in one record is the same one as in another, and no name, number or position for any of them.

Cost of these failures: a `C-PERTURBATION-REACHED` failure roughly halves the reward (0.4275–0.4911 against a conforming baseline near 0.85), because it also forces `task_pass` to 0. The `C-API-SURFACE` failure cost less (0.7580) but still forced `task_pass` to 0.

# 4. Ruled-out directions

**Maximising `compute_efficiency` as the optimisation objective — ruled out.** Attempt 11 reached `compute_efficiency` 1.0000 and scored 0.8067, and attempt 19 reached 1.0000 and scored 0.4278 after losing the held-out variant. Attempt 16 at 0.9805 scored 0.7005, the worst of any fully-conforming attempt. The leader, attempt 20, sits at 0.9633. Efficiency past roughly 0.96 buys nothing and repeatedly costs task quality.

**Driving `per_step_cost_ratio` below about 0.69 — ruled out.** The three lowest ratios in the set are attempt 21 (0.6727, reward 0.0000), attempt 19 (0.6884, reward 0.4278) and attempt 4 (0.6934, reward 0.7740). None beat the leader; two failed checks outright. Attempt 20's 0.7013 is the lowest ratio that has ever led.

**Longer wall clock / larger budget — ruled out.** Attempt 8 ran 98.60 s (the longest conforming run) with `qualifying_budget` 98.60 and scored 0.7805, below the ~74 s Class A cluster at 0.8655–0.8658. Attempt 1 at 76.34 s scored 0.8630, under the 74 s leaders. Attempt 21 at 1691.67 s scored 0.0000. More time has never helped and once destroyed the run entirely.

**Very short budgets — ruled out.** Attempt 7 at 50.05 s and attempt 6 with `qualifying_budget` 45.82 both scored `task_pass: 0`. Attempt 9 recorded `qualifying_budget` 49.89 against a 74.39 s wall clock and did hold all checks, but scored 0.8332, below the leader. Compressing the qualifying budget has never produced a leading score.

**Any module-level executable statement — ruled out.** Attempt 6 lost `C-API-SURFACE` on exactly this and forfeited `task_pass` despite both perturbations holding. There is no upside; it is a pure loss of 0.10+ reward.

**Further micro-tuning inside the Class A band — ruled out as a path to a new leader.** Attempts 3, 5, 13 and 17 landed at 0.8657, 0.8658, 0.8657 and 0.8655. Four separate configurations converged on the same three-decimal value. That ridge is saturated and sits below attempt 20's 0.8670.

**Re-running Class C speed-pushes without changing what breaks the held-out variant — ruled out.** Attempts 7, 12 and 19 each pushed the speed/budget trade differently and each lost `C-PERTURBATION-REACHED` in the same place. Repeating that trade with a fourth setting is not exploration and not exploitation; the earlier work already did it three times for no information gain beyond the first.

# 5. Open leads

**Lead 1 — reconstruct attempt 20's operating point and treat it as the base.** Target `compute_efficiency` ≈ 0.963, `per_step_cost_ratio` ≈ 0.701, `wall_clock_sec` ≈ 73.7, `qualifying_budget` ≈ 73.7. This is the only configuration that has combined Class-B efficiency with Class-A task quality, and it is the sole record above 0.866. Everything else should be a perturbation of this point, not of the Class A point.

**Lead 2 — close the gap between attempt 20 and attempt 14/18.** Attempt 14 (`compute_efficiency` 0.9705, `per_step_cost_ratio` 0.6997, 0.8513) and attempt 18 (0.8827 / 0.7671, 0.8368) sit at almost the same operating point as the leader but score 0.016–0.030 lower. Since the cost knobs are nearly identical, the reward difference must come from the task-quality side — the final model's performance on the primary evaluation, not its speed. Identifying and holding whatever attempt 20 did on that axis is the highest-value single move available.

**Lead 3 — attack the `held_out_variant` robustness directly rather than through the speed knobs.** Four attempts lost `C-PERTURBATION-REACHED`, and in every case the failing unit was of kind `held_out_variant`, stopped by `C-BUDGET-RESPECTED` and usually `C-TARGET-REACHED` too. Because these failures occurred at `compute_efficiency` 0.6954, 0.8464, 1.0000 and 0.9829, the cost setting is demonstrably not the cause. The productive question is what makes the held-out variant slower to reach its threshold than the primary and the seed run — for example, a schedule or early-stopping criterion tuned to the primary distribution, a fixed iteration count that happens to suffice on the primary but not on a shifted variant, or per-variant budget accounting. Adding margin specifically on the variant path (an adaptive stopping rule, or a slightly larger reserve for the variant's own budget) is worth more than any efficiency gain, since the failure costs roughly half the reward.

**Lead 4 — build in an unconditional wall-clock guard.** Attempt 21's 1691.67 s is the only catastrophic record and the only 0.0000. Its `per_step_cost_ratio` of 0.6727 with an enormous wall clock points to a run that iterated without terminating. A hard iteration cap plus a wall-clock ceiling around the ~74 s that every successful attempt used would make this failure mode structurally impossible at negligible cost.

**Lead 5 — preserve the API surface mechanically.** Keep module scope to imports, constants and permitted definitions only; put all execution inside the required function or class bodies. This is a checklist item, not a design decision, but it cost attempt 6 its `task_pass`.

**Lead 6 — accept that the achievable band is narrow.** Fourteen conforming attempts spanned 0.7005–0.8670 and the top six spanned 0.004. Improvements over 0.8670 will be small, and the far larger risk is dropping into the 0.43–0.49 band by losing a perturbation. Any change that gambles conformance for a fractional efficiency gain is a bad trade at these numbers.

**Call: exploit.** Take attempt 20's configuration — `compute_efficiency` ≈ 0.963, `per_step_cost_ratio` ≈ 0.701, ~74 s wall clock, all checks held, reward 0.8670 — and improve it along the task-quality axis while adding explicit margin on the `held_out_variant` path (Leads 1, 2 and 3) and the two mechanical guards (Leads 4 and 5). Do not push `compute_efficiency` toward 1.0 or `per_step_cost_ratio` below 0.69; both have been measured and both lose. The approaches that scored have not stopped improving — attempt 20 raised the ceiling above the saturated 0.8658 ridge — so a structural change is not yet warranted. One caution drawn from the record: earlier work repeatedly re-entered the Class C speed-push and lost `C-PERTURBATION-REACHED` three separate times without changing what causes that check to fail. Do not do that again; if the held-out variant is touched at all, change the thing that determines whether it reaches its threshold inside its budget.
