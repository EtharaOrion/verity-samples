# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 25 -- reward 0.9130, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4        0.8719   1.000             2 of 2         yes             50                
  5        0.9128   1.000             2 of 2         yes             25                
  6        0.5615   0.857             2 of 2         yes             204               
  7        0.0000   1.000             0 of 2         no              --                
  8        0.7551   1.000             2 of 2         yes             78                
  9        0.0000   1.000             0 of 2         no              --                
  10       0.0000   1.000             0 of 2         no              --                
  11       0.8980   1.000             2 of 2         yes             25                
  12       0.0000   1.000             0 of 2         no              --                
  13       0.8451   1.000             2 of 2         yes             71                
  14       0.6955   1.000             2 of 2         yes             100               
  15       0.0000   1.000             0 of 2         no              --                
  16       0.0000   1.000             0 of 2         no              --                
  17       0.7919   1.000             2 of 2         yes             74                
  18       0.8794   1.000             2 of 2         yes             49                
  19       0.9121   1.000             2 of 2         yes             46                
  20       0.8661   1.000             2 of 2         yes             62                
  21       0.0000   1.000             0 of 2         no              --                
  22       0.0000   1.000             0 of 2         no              --                
  23       0.8768   1.000             2 of 2         yes             50                
  24       0.8979   1.000             2 of 2         yes             25                
  25 *     0.9130   1.000             2 of 2         yes             25                

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

    attempt 5 -- reward 0.9128, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.9121, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 46
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 23 -- reward 0.8768, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 24 -- reward 0.8979, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All 25 records carry `measurement_status: "measured"`, so every one has a reward; none is a missing measurement. Listed worst to best.

**Zero-reward group (nine attempts, all `zero_reason_code: 4`, `primary_target_reached: 0.0`, `task_pass: 0.0`, `conformance_fraction: 0.0`, `all_perturbations_held: false`, `qualifying_budget: "not-measured"`):**

- Attempt 3 — reward 0.0000, wall_clock 1692.52 s
- Attempt 7 — reward 0.0000, wall_clock 1692.21 s
- Attempt 9 — reward 0.0000, wall_clock 1692.97 s
- Attempt 10 — reward 0.0000, wall_clock 1690.96 s
- Attempt 12 — reward 0.0000, wall_clock 1690.45 s
- Attempt 15 — reward 0.0000, wall_clock 1690.48 s
- Attempt 16 — reward 0.0000, wall_clock 1691.53 s
- Attempt 21 — reward 0.0000, wall_clock 1691.00 s
- Attempt 22 — reward 0.0000, wall_clock 1690.32 s

**Non-zero group, ascending:**

- Attempt 6 — reward 0.5615, wall_clock 204.09 s, qualifying_budget 204.09, rule_conformance 0.8571, task_pass 0.0, per_step_cost_ratio 1.3778
- Attempt 14 — reward 0.6955, wall_clock 99.74 s, qualifying_budget 99.74, rule_conformance 1.0, task_pass 1.0
- Attempt 8 — reward 0.7551, wall_clock 151.50 s, qualifying_budget 78.14, rule_conformance 1.0, task_pass 1.0
- Attempt 1 — reward 0.7684, wall_clock 25.46 s, qualifying_budget 25.46, rule_conformance 0.8571, task_pass 0.0, per_step_cost_ratio 1.0639
- Attempt 17 — reward 0.7919, wall_clock 73.80 s, qualifying_budget 73.80
- Attempt 2 — reward 0.8385, wall_clock 73.62 s, qualifying_budget 73.62
- Attempt 13 — reward 0.8451, wall_clock 71.31 s, qualifying_budget 71.31
- Attempt 20 — reward 0.8661, wall_clock 62.46 s, qualifying_budget 62.46, compute_efficiency 1.0
- Attempt 4 — reward 0.8719, wall_clock 50.03 s, qualifying_budget 50.03, compute_efficiency 1.0
- Attempt 23 — reward 0.8768, wall_clock 49.67 s, qualifying_budget 49.67
- Attempt 18 — reward 0.8794, wall_clock 49.33 s, qualifying_budget 49.33
- Attempt 24 — reward 0.8979, wall_clock 25.37 s, qualifying_budget 25.37
- Attempt 11 — reward 0.8980, wall_clock 25.35 s, qualifying_budget 25.35
- Attempt 19 — reward 0.9121, wall_clock 45.81 s, qualifying_budget 45.81
- Attempt 5 — reward 0.9128, wall_clock 25.34 s, qualifying_budget 25.34
- **Attempt 25 — reward 0.9130, wall_clock 25.32 s, qualifying_budget 25.32, compute_efficiency 0.8277, per_step_cost_ratio 0.8726, rule_conformance 1.0, task_pass 1.0, no failed checks. This is the highest reward recorded and it is the one to beat.**

Direction of travel, stated plainly: after attempt 5 reached 0.9128, the next nineteen attempts produced only one score above it (attempt 25 at 0.9130, a gain of 0.0002). Attempts 6, 8, 14 and 17 were all substantially *lower* than the then-best, and nine attempts scored 0.0000 — those are regressions, not progress, and `standing_against_best_so_far` says "worse_than_an_earlier_attempt" for every one of them.

Perturbation outcomes in aggregate: every record declared 2 perturbation units, one of kind `held_out_variant` and one of kind `seed`, for 50 units across all records. 32 units reached (16 attempts × 2), 18 did not (9 attempts × 2). Broken down by kind: `held_out_variant` reached in 16 records and failed in 9; `seed` reached in 16 records and failed in 9. Every failing unit of either kind failed on exactly the same pair, `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. There is no record in which a perturbation unit failed while the primary run succeeded, and none in which one kind held while the other did not — the two kinds have always failed together and always alongside the primary. So there is no evidence of a robustness gap specific to seed variation or specific to the held-out variant; when the primary converges, both kinds converge, and when it does not, neither does.

# 2. Approach classes tried

The measured terms distinguish five regimes. Records that behaved identically are collapsed into one entry.

**Class A — fast-converging conformant runs, qualifying budget ≈ 25.3 s.** Attempts 5, 11, 24, 25 (and attempt 1, which sits in this budget regime but violated a conformance check, see Class E). Rewards 0.8979–0.9130. All checks held, `task_pass: 1.0`, `compute_efficiency` between 0.7043 and 0.8277, `per_step_cost_ratio` between 0.8726 and 1.1078. Wall clock equals qualifying budget exactly in each, meaning the run terminated at the moment it qualified. This class contains the best result and the second best.

**Class B — mid-budget conformant runs, qualifying budget ≈ 45–75 s.** Attempts 19 (45.81 s, 0.9121), 18 (49.33 s, 0.8794), 23 (49.67 s, 0.8768), 4 (50.03 s, 0.8719), 20 (62.46 s, 0.8661), 13 (71.31 s, 0.8451), 2 (73.62 s, 0.8385), 17 (73.80 s, 0.7919). All hold every check and pass the task. Reward falls roughly monotonically as qualifying budget rises within this class. Attempt 19 is the exception worth noting: at 45.81 s it scored 0.9121, essentially level with the 25 s Class A runs, and it did so with `compute_efficiency` 0.9345 and `per_step_cost_ratio` 0.7669 — a cheaper per-step profile bought back most of the penalty for the longer budget.

**Class C — long conformant runs, 99–152 s.** Attempts 14 (99.74 s, 0.6955) and 8 (qualifying budget 78.14 s but wall clock 151.50 s, 0.7551). Both pass every check and the task, both score well below the best. Attempt 8 is the only conformant record where wall clock exceeds qualifying budget, by roughly 73 s, and it scored 0.0834 below attempt 2 which had a nearly identical qualifying budget (73.62 s) but no excess wall clock. That comparison is the cleanest single piece of evidence in the data that wall clock spent after the qualifying point is charged against reward.

**Class D — non-converging runs that ran to a hard time wall.** Nine attempts (3, 7, 9, 10, 12, 15, 16, 21, 22), every one with wall clock between 1690.32 s and 1692.97 s — a spread of 2.65 s across nine runs, which is a cap being hit, not a coincidence of workloads. All nine scored 0.0000. Their `compute_efficiency` values (0.9033–1.0) and `per_step_cost_ratio` values (0.6827–0.8901) are *good*; the per-step economics were fine and the runs simply never crossed the threshold. This class was re-entered nine separate times.

**Class E — runs carrying a module-level statement in the submission file.** Attempts 1 (0.7684) and 6 (0.5615). Both scored non-zero, both had `rule_conformance` 0.8571 (six of seven rules) and `conformance_fraction` 1.0, and both had `task_pass: 0.0` despite `primary_target_reached: 1.0` and both perturbation units reaching. This class overlaps the budget regimes: attempt 1 ran at 25.46 s and still only reached 0.7684, against 0.9130 for attempt 25 at an almost identical 25.32 s. The gap of 0.1446 between two runs at the same budget is the measured cost of this single conformance failure.

# 3. Checks that failed

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions."** Failed twice, in attempt 1 and attempt 6. Whatever was changed between attempt 1 and attempt 6 is not what causes this check to fail; the same statement-placement violation survived that change. Note that this failure does not zero the reward — both records scored (0.7684 and 0.5615) — but it drives `rule_conformance` to 0.8571 and forces `task_pass` to 0.0 even though the primary target was reached and both perturbation units held. Attempts 2 onward other than 6 kept it clear, so a submission consisting only of imports, constant assignments and function/class definitions at module level satisfies it. The fix is mechanical: no executable statement at module scope — no bare calls, no `if` blocks, no prints, no seeding or configuration executed at import time. Move all of it inside the entry-point function.

**`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction."** Failed nine times: attempts 3, 7, 9, 10, 12, 15, 16, 21, 22. This is the dominant failure in the record set. Nine separate submissions were changed between these occurrences and the check failed identically every time, so whatever was varied across those nine is not what causes it. In each case the run consumed ~1690 s of wall clock and produced no row crossing the threshold.

**`C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists."** Failed nine times, in exactly the same nine attempts. This is a consequence of `C-TARGET-REACHED`, not an independent problem: with no qualifying row there is nothing to position against the budget, and `qualifying_budget` is reported as "not-measured" in all nine. Fixing target-reaching fixes this.

**`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget."** Failed nine times, same nine attempts, and always at 0 of 2 — never 1 of 2. Within those records, the `held_out_variant` unit and the `seed` unit each failed on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. Again, whatever changed across those nine attempts did not move this check.

Never observed across any record: `red_line_crossed` is 0.0 everywhere and `validity` is 1.0 everywhere. No submission was ever invalid or crossed a red line, so neither is a live risk to design around.

# 4. Ruled-out directions

**Anything that lands in the ~1690 s regime.** Nine attempts did, and all nine scored 0.0000 on `C-TARGET-REACHED`. Their `compute_efficiency` was 0.9033–1.0 and `per_step_cost_ratio` 0.6827–0.8901 — i.e. these were *efficient per step* and still failed. Efficiency without convergence is worthless here. Do not submit any configuration whose expected runtime approaches four figures of seconds; the harness wall is at roughly 1690 s and hitting it forfeits the entire reward.

**Leaving executable code at module scope.** Ruled out by `C-API-SURFACE` failing in attempts 1 and 6, costing an estimated 0.1446 of reward at an otherwise-identical budget (attempt 1's 0.7684 versus attempt 25's 0.9130 at ~25.3 s) and forcing `task_pass` to 0.0.

**Budgets above roughly 75 s.** Attempts 14 (99.74 s → 0.6955), 8 (151.50 s wall → 0.7551) and 6 (204.09 s → 0.5615) are the three longest conformant or near-conformant runs and they are three of the four lowest non-zero scores. No run above 75 s of qualifying budget has ever exceeded 0.7919.

**Letting the run continue after it qualifies.** Attempt 8 is the sole record where wall clock (151.50 s) exceeds qualifying budget (78.14 s), and it scored 0.7551 against attempt 2's 0.8385 at a comparable 73.62 s qualifying budget with no excess. Trailing work after the qualifying row is charged and buys nothing.

**Maximising `compute_efficiency` as the objective.** Ruled out by direct comparison: attempts 4 and 20 both reported `compute_efficiency` 1.0 and scored 0.8719 and 0.8661, while attempt 25 reported 0.8277 and scored 0.9130, and attempt 5 reported 0.7728 and scored 0.9128. The correlation between this term and reward is weak-to-negative among conformant runs. Time-to-qualify is the term that tracks reward.

**Driving `per_step_cost_ratio` below 1 as an end in itself.** The two best runs sit at 0.8726 (attempt 25) and 0.9887 (attempt 5); attempts 11 and 24 exceeded 1.0 (1.0502, 1.1078) and still scored 0.8980 and 0.8979. Meanwhile every zero-reward run had a ratio below 0.90. A low ratio is neither necessary nor sufficient.

**Hardening specifically against seed variation, or specifically against the held-out variant.** Ruled out by the perturbation data: across 50 units, no unit of either kind has ever failed while the primary run succeeded, and the two kinds have never diverged from each other in any record. There is no measured robustness gap to close; the perturbation failures are entirely explained by the primary run not converging.

# 5. Open leads

**Reproduce the Class A configuration exactly and treat 0.9130 as the floor.** The target shape is: every check held, `task_pass` 1.0, both perturbation units reached, wall clock equal to qualifying budget at approximately 25.3 s. Four independent attempts (5, 11, 24, 25) landed in this regime and scored 0.8979–0.9130, so it is reliably reachable rather than a lucky draw. The spread within the regime is 0.0151, and attempt 25's edge over 5 came with a lower `per_step_cost_ratio` (0.8726 versus 0.9887) at essentially identical wall clock — that is the one dimension inside Class A that appears to separate 0.9130 from 0.9128.

**Push `per_step_cost_ratio` down while holding qualifying budget at ~25.3 s.** This is the most specific untested combination the data points at. The lowest ratios observed on conformant runs are attempt 20 at 0.6145 (62.46 s, 0.8661) and attempt 19 at 0.7669 (45.81 s, 0.9121) — both achieved cheap steps but at longer budgets. No run has yet combined a sub-0.75 ratio with a ~25 s budget. Attempt 19's result is the encouraging signal: at nearly double the budget of Class A it still reached 0.9121 on the strength of its cost ratio, which suggests the two terms trade off and that pairing the best of each could clear 0.9130.

**Terminate immediately on qualification.** Every top-scoring run has wall clock exactly equal to qualifying budget. Make the entry point return the instant the declared threshold is crossed in the declared direction, with no trailing evaluation, no extra epochs, no final full-dataset pass. Attempt 8 shows what the alternative costs.

**Guard the module surface mechanically before submitting.** Since the stub is pristine each time, `C-API-SURFACE` can recur. Keep module scope to imports, literal constant assignments, and `def`/`class` definitions only. Put seeding, device selection, hyperparameter derivation and any logging inside the function body. This is worth roughly 0.14 of reward at a fixed budget.

**Keep the safety margin against the 1690 s wall large.** The nine zeros show the downside is total. A configuration that qualifies in 25 s has a margin of nearly two orders of magnitude; do not trade that away for a speculative accuracy gain, because the gain is capped near 0.09 (0.9130 to 1.0) while the loss is the full 0.9130.

**Call: exploit.** Class A already scores and the single best result sits inside it; the lead worth pursuing is the one thing measurably separating runs within it — lower per-step cost at the same ~25 s qualifying budget, with immediate termination on qualification and a clean module surface. Explore is not warranted: the scoring approaches have not exhausted their fine structure, and the structurally different directions that were tried are precisely the nine ~1690 s runs that scored 0.0000. Those nine are worth naming for what they were — the same non-converging regime re-entered nine times without changing the thing that made it fail `C-TARGET-REACHED`, which is neither exploiting nor exploring. Do not re-enter it.
