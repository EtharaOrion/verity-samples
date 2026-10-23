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

    All two attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

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
  26       0.0000   1.000             0 of 2         no              --                
  27       0.7552   0.857             2 of 2         yes             25                

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
  22 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 26 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 27 -- reward 0.7552, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (1, 6, 27). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All 27 records carry `measurement_status: "measured"`, so every one has a reward and none is unmeasured. `validity` is 1.0 and `red_line_crossed` is 0.0 in all 27 — nothing was ever rejected outright or tripped a red line.

Worst to best by reward:

**Zero-reward group (ten attempts, all identical in signature): reward 0.0000 each — attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26.** Every one has `zero_reason_code: 4`, `primary_target_reached: 0.0`, `conformance_fraction: 0.0`, `qualifying_budget: "not-measured"`, and a wall clock pinned at roughly 1690–1693 s (1692.5, 1692.2, 1692.9, 1690.9, 1690.4, 1690.5, 1691.5, 1690.9, 1690.3, 1691.6). `rule_conformance` was a clean 1.0 in all ten — these were not rule violations, they simply never produced a qualifying evaluation row before the run was cut at the ~1690 s cap. Each is marked `worse_than_an_earlier_attempt`.

Then, ascending, the attempts that scored:

- Attempt 6 — reward **0.5615**. Wall clock 204.0889 s; `per_step_cost_ratio` 1.3778; `compute_efficiency` 0.6091; `rule_conformance` 0.8571; `task_pass` 0.0; failed C-API-SURFACE. Worse than an earlier attempt.
- Attempt 14 — reward **0.6955**. Wall clock 99.7374 s; `per_step_cost_ratio` 0.9155; `compute_efficiency` 0.9220; fully conformant; `task_pass` 1.0. Worse than an earlier attempt.
- Attempt 8 — reward **0.7551**. `qualifying_budget` 78.1441 s but wall clock 151.5049 s — the only record where wall clock exceeds the qualifying budget. `per_step_cost_ratio` 1.0291; fully conformant; `task_pass` 1.0. Worse than an earlier attempt.
- Attempt 27 — reward **0.7552**. Wall clock 25.2558 s — the fastest run in the whole set — yet scored in the bottom half because it failed C-API-SURFACE (`rule_conformance` 0.8571, `task_pass` 0.0). Worse than an earlier attempt.
- Attempt 1 — reward **0.7684**. Wall clock 25.4619 s; failed C-API-SURFACE (`rule_conformance` 0.8571, `task_pass` 0.0); `per_step_cost_ratio` 1.0639. This is the `first_measured_attempt` baseline.
- Attempt 17 — reward **0.7919**. Wall clock 73.7980 s; `per_step_cost_ratio` 0.7318; `compute_efficiency` 0.9221; fully conformant. Worse than an earlier attempt.
- Attempt 2 — reward **0.8385**. Wall clock 73.6235 s; `per_step_cost_ratio` 0.9162; fully conformant; `task_pass` 1.0. At the time it was `better_than_every_earlier_attempt`.
- Attempt 13 — reward **0.8451**. Wall clock 71.3146 s; `per_step_cost_ratio` 1.0266. Worse than an earlier attempt.
- Attempt 20 — reward **0.8661**. Wall clock 62.4628 s; `compute_efficiency` 1.0; `per_step_cost_ratio` 0.6145 (the lowest recorded). Worse than an earlier attempt.
- Attempt 4 — reward **0.8719**. Wall clock 50.0341 s; `compute_efficiency` 1.0; `per_step_cost_ratio` 0.7115. At the time `better_than_every_earlier_attempt`.
- Attempt 23 — reward **0.8768**. Wall clock 49.6669 s; `per_step_cost_ratio` 0.9384. Worse than an earlier attempt.
- Attempt 18 — reward **0.8794**. Wall clock 49.3313 s; `per_step_cost_ratio` 0.9260. Worse than an earlier attempt.
- Attempt 24 — reward **0.8979**. Wall clock 25.3699 s; `per_step_cost_ratio` 1.1078; `compute_efficiency` 0.7330. Worse than an earlier attempt.
- Attempt 11 — reward **0.8980**. Wall clock 25.3479 s; `per_step_cost_ratio` 1.0502; `compute_efficiency` 0.7043. Worse than an earlier attempt.
- Attempt 19 — reward **0.9121**. Wall clock 45.8132 s; `per_step_cost_ratio` 0.7669; `compute_efficiency` 0.9345. Worse than an earlier attempt.
- Attempt 5 — reward **0.9128**. Wall clock 25.3436 s; `per_step_cost_ratio` 0.9887; `compute_efficiency` 0.7728. At the time `better_than_every_earlier_attempt`.
- **Attempt 25 — reward 0.9130. This is the highest reward recorded and the one to beat.** Wall clock 25.3170 s; `qualifying_budget` 25.3170 s; `compute_efficiency` 0.8277; `per_step_cost_ratio` 0.8726; `rule_conformance` 1.0; `conformance_fraction` 1.0; `task_pass` 1.0; both declared perturbations held; `standing_against_best_so_far: better_than_every_earlier_attempt`.

Note plainly: only five attempts (1, 2, 4, 5, 25) ever improved on the standing best. Every other attempt, including everything after attempt 25, is recorded as `worse_than_an_earlier_attempt`. The margin between the two best (0.9128 at attempt 5 and 0.9130 at attempt 25) is 0.0002 — the top band has essentially flattened.

# 2. Approach classes tried

The records carry no source, so the classes below are grouped by their measured signature. Each class is one entry regardless of how many records share it.

**Class A — fast conformant configuration at the ~25.3 s budget floor.** Attempts 5 (0.9128), 11 (0.8980), 24 (0.8979), 25 (0.9130). All four qualified at 25.32–25.37 s, a value four separate runs land on to within 0.06 s, which strongly suggests a floor imposed by the harness's evaluation cadence rather than by the training work itself. This class contains the best result and three of the top five. Within the class, reward tracks `compute_efficiency` and inversely tracks `per_step_cost_ratio`: 25 (0.8277 eff / 0.8726 cost) → 0.9130; 5 (0.7728 / 0.9887) → 0.9128; 11 (0.7043 / 1.0502) → 0.8980; 24 (0.7330 / 1.1078) → 0.8979. The two runs with `per_step_cost_ratio` above 1.0 both fell to ~0.898; the two below 1.0 both cleared 0.912.

**Class B — mid-budget conformant configuration, roughly 45–80 s.** Attempts 19 (45.8132 s, 0.9121), 18 (49.3313 s, 0.8794), 23 (49.6669 s, 0.8768), 4 (50.0341 s, 0.8719), 20 (62.4628 s, 0.8661), 13 (71.3146 s, 0.8451), 2 (73.6235 s, 0.8385), 17 (73.7980 s, 0.7919), 8 (78.1441 s qualifying, 0.7551). Reward falls monotonically with qualifying budget across this class with one striking exception at the fast end: attempt 19 at 45.8 s scored 0.9121, within 0.001 of the 25 s band, and it did so with the best combination in the class (`compute_efficiency` 0.9345, `per_step_cost_ratio` 0.7669). That says the budget term is not the only lever — a slower run with a much better per-step cost profile nearly matches the fastest runs.

**Class C — long-budget conformant configuration.** Attempt 14 (99.7374 s, 0.6955) and attempt 6 (204.0889 s, 0.5615, also non-conformant). These are the worst non-zero results. Extending the budget past ~100 s destroys reward even when the target and both perturbations are reached.

**Class D — submission with module-level executable code.** Attempts 1 (0.7684), 6 (0.5615), 27 (0.7552). All three reached the primary target and held both perturbations, all three were capped at `rule_conformance` 0.8571 (6 of 7) and forced to `task_pass: 0.0` by C-API-SURFACE. Attempt 27 is the cleanest measurement of the cost: it ran in 25.2558 s, faster than the best-ever attempt 25, and still scored only 0.7552 — roughly 0.16 of reward burned purely on the surface violation.

**Class E — non-converging configuration.** Ten attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26), all reward 0.0000. Every one ran to the ~1690 s cap and produced no evaluation row crossing the threshold in the declared direction. Their `per_step_cost_ratio` values (0.6827–0.8901) and `compute_efficiency` values (0.9033–1.0) were often *better* than the scoring runs' — the per-step economics were fine, the run simply never reached the target. This class was re-entered ten times and never once scored.

**Class F — work continued past the qualifying row.** Attempt 8 alone: qualifying budget 78.1441 s against 151.5049 s of wall clock. It scored 0.7551, consistent with its qualifying budget; the extra 73 s of wall clock bought nothing measurable.

# 3. Checks that failed

**C-API-SURFACE — "module-level statements outside imports, constants, and permitted definitions." Failed three times: attempts 1, 6 and 27.** This is the finding that matters most among the conformance failures. Those three attempts are separated by many intervening submissions that did *not* fail it, and they differ from each other in budget (25.46 s, 204.09 s, 25.26 s), in `per_step_cost_ratio` (1.0639, 1.3778, 0.7111) and in `compute_efficiency` (0.8160, 0.6091, 0.9740). Whatever was being varied between those attempts is not what causes this check to fail. The cause is a structural property of the submission file: executable statements sitting at module scope. Only imports, constants and permitted definitions may appear at module level; anything that runs at import time — a print, a seed call, an argparse invocation, a device probe, a config-building expression, a `if __name__` block's contents if hoisted, a call that instantiates anything — trips it. Each occurrence pinned `rule_conformance` at 0.8571 and `task_pass` at 0.0 while the run itself was otherwise fine (target reached, both perturbations held).

**C-TARGET-REACHED — "no evaluation row crosses the threshold in the declared direction." Failed ten times: attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26.** Ten failures across widely separated attempts. This is the single largest loss of reward in the whole record: ten measured 0.0000s. Again, the thing varied between those ten attempts is demonstrably not the cause — they all failed identically, with `rule_conformance` a clean 1.0 and healthy per-step cost. The training run does not reach the declared threshold at all inside the ~1690 s cap.

**C-BUDGET-RESPECTED — "no qualifying row, so no budget position exists." Failed ten times, on exactly the same attempts.** This is downstream of C-TARGET-REACHED, not an independent problem: with no row crossing the threshold there is no budget position to evaluate, and `qualifying_budget` is reported as "not-measured".

**C-PERTURBATION-REACHED — "0 of 2 declared perturbations reached their own threshold inside their own budget." Failed ten times, on exactly the same attempts.** Also downstream: whenever the primary failed, both held-out runs failed too, and whenever the primary succeeded, both held-out runs succeeded.

# Perturbation outcomes by kind

Every record declares exactly two held-out runs beside the primary: one of kind `held_out_variant` and one of kind `seed`. No run is identified beyond its kind, so nothing here attributes a particular run to a particular position or claims continuity of any one run across records.

- **`held_out_variant`:** reached its threshold in 17 records (attempts 1, 2, 4, 5, 6, 8, 11, 13, 14, 17, 18, 19, 20, 23, 24, 25, 27) and failed to reach it in 10 (attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26). In every failure it was stopped by C-TARGET-REACHED and C-BUDGET-RESPECTED.
- **`seed`:** identical tally — reached in the same 17, failed in the same 10, stopped by the same two checks, C-TARGET-REACHED and C-BUDGET-RESPECTED.

In aggregate that is 54 held-out runs: 34 reached, 20 failed, and the 20 failures are 10 of each kind, all on the same two checks. Two things follow. First, neither kind is a differentially weak point: `held_out_variant` and `seed` succeed and fail together, always in lockstep with the primary. Robustness to variant or to seed has never been the independent limiter. Second, the three C-API-SURFACE failures left all six of their held-out runs reaching threshold — a surface violation costs reward and `task_pass` without touching perturbation behaviour at all.

# 4. Ruled-out directions

- **Re-entering the non-converging configuration class (Class E) unchanged.** Ten attempts produced reward 0.0000 with the identical triple of failed checks and an identical ~1690 s wall clock. This has been tried repeatedly and has never scored. Repeating it without changing what stops the run from crossing the threshold is neither exploration nor exploitation, and that is exactly what earlier work kept doing — ten times. Do not submit anything whose training loop cannot be shown to cross the declared threshold well inside the cap.
- **Spending more budget to buy a better result.** Ruled out by direct measurement: 99.7374 s → 0.6955 and 204.0889 s → 0.5615 are the two worst non-zero scores, both with the target reached and both perturbations held. Reward falls as qualifying budget rises across the entire 25–204 s range. Long budgets do not pay.
- **Letting the process keep working after the qualifying row is produced.** Attempt 8 ran 151.5049 s of wall clock for a 78.1441 s qualifying budget and scored 0.7551. The extra time changed nothing in the score's favour.
- **Any submission that carries executable statements at module scope.** Three attempts prove the cost independently of every other variable: attempt 27 ran in 25.2558 s, faster than the best-ever run, and still scored only 0.7552 because C-API-SURFACE capped `rule_conformance` at 0.8571 and zeroed `task_pass`. There is no configuration good enough to absorb this penalty.
- **Chasing `per_step_cost_ratio` down in isolation.** Attempt 20 achieved the lowest ratio in the record, 0.6145, together with `compute_efficiency` 1.0, and scored 0.8661 — below four runs with worse ratios — because its budget was 62.4628 s. Cost-per-step only pays when the budget is already short.
- **Treating perturbation robustness as the blocker.** Across 54 held-out runs, no run of either kind ever failed while the primary succeeded. Hardening specifically against seed variation or against the held-out variant addresses a failure mode that has never occurred in isolation.

# 5. Open leads

- **Reconstruct the attempt-25 configuration and beat it on the two secondary terms.** It is the target: reward 0.9130, qualifying budget 25.3170 s, `compute_efficiency` 0.8277, `per_step_cost_ratio` 0.8726, `rule_conformance` 1.0, `task_pass` 1.0, both perturbations held. The four Class-A runs all sit at the same 25.3 s budget, so budget appears to be saturated there; what separates 0.9130 from 0.8979 within that class is `compute_efficiency` (0.8277 vs 0.7043–0.7330) and `per_step_cost_ratio` (0.8726 vs 1.05–1.11). The lead is a run that qualifies at ~25.3 s while pushing `compute_efficiency` toward the 0.93–1.0 seen in attempts 19, 20 and 4, and holding `per_step_cost_ratio` at or below 0.77.
- **Test whether attempt 19's profile can be moved to the 25 s floor.** Attempt 19 scored 0.9121 at 45.8132 s with `compute_efficiency` 0.9345 and `per_step_cost_ratio` 0.7669 — a far better efficiency profile than attempt 25's, at nearly twice the budget, for almost the same reward. If that profile can be preserved while the qualifying budget drops to the ~25.3 s floor, the arithmetic suggests a score above 0.9130. This is the single most promising untried combination in the record.
- **Verify the ~25.3 s value really is a floor before optimising against it.** Four runs at 25.317, 25.344, 25.348 and 25.370 s, plus 25.256 s and 25.462 s in the non-conformant class, cluster far too tightly to be coincidence. If it is an evaluation-cadence floor, no further reward is available from shortening the run and all remaining headroom is in `compute_efficiency` and `per_step_cost_ratio`. If it is not, a shorter qualifying row is the most direct gain available.
- **Make the module-level surface constraint structurally impossible to violate.** Put every statement inside a function or a permitted definition; leave only imports, literal constants and def/class at module scope. No seeding, no device selection, no config construction, no logging, nothing that executes at import. Three attempts have been lost to this check and one of them (27) would otherwise have been in the top band.
- **Guard against the ten-times-repeated non-convergence before submitting.** The zero class is not a rule problem — those runs had `rule_conformance` 1.0 and good per-step cost. The failure is that no evaluation row ever crosses the threshold in the declared direction. Confirm the declared direction matches the metric's sense, confirm evaluation rows are actually emitted during training rather than only at the end, and confirm the threshold is reachable by the configuration being shipped. A run that emits its first qualifying row early is also, mechanically, a run with a small qualifying budget — which is what the top band rewards.

**Call: exploit.** The path to beating 0.9130 is to rebuild the fast conformant configuration of attempt 25 — target reached, both perturbations held, zero failed checks, qualifying at the ~25.3 s floor — and improve its `compute_efficiency` and `per_step_cost_ratio` toward the values attempt 19 already demonstrated. The exploratory alternatives have been measured and lost: longer budgets score worse, and the non-converging class has been re-entered ten times for ten rewards of 0.0000 without anyone changing the thing that makes it fail. Do not re-enter that class.
