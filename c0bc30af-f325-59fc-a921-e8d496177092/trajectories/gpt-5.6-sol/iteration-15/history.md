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

    All ten attempts since have scored lower than it.
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED has failed on 2 attempts (7, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Fifteen graded submissions, all fifteen with `measurement_status: "measured"`, so every one carries a reward. Ranked worst to best:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 12 | 0.4275 | held-out variant did not reach; `task_pass` 0 |
| 2 | 7 | 0.4911 | held-out variant did not reach; `task_pass` 0 |
| 3 | 6 | 0.7580 | `C-API-SURFACE` failed; `task_pass` 0; `rule_conformance` 0.8571 |
| 4 | 4 | 0.7740 | clean, `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934 |
| 5 | 8 | 0.7805 | clean, slowest run (`wall_clock_sec` 98.60), cost ratio 1.0848 |
| 6 | 11 | 0.8067 | clean, `compute_efficiency` 1.0000, cost ratio 0.6947 |
| 7 | 2 | 0.8079 | clean, cost ratio 0.9441 |
| 8 | 9 | 0.8332 | clean, `qualifying_budget` 49.89 vs wall clock 74.39 |
| 9 | 10 | 0.8503 | clean, cost ratio 0.9615 |
| 10 | 14 | 0.8513 | clean, `compute_efficiency` 0.9705, cost ratio 0.6997 |
| 11 | 15 | 0.8579 | clean, `compute_efficiency` 0.9355 at cost ratio 0.9424 |
| 12 | 1 | 0.8630 | clean, cost ratio 1.0723 |
| 13 | 13 | 0.8657 | clean (0.8656561) |
| 14 | 3 | 0.8657 | clean (0.8657110) |
| 15 (best) | 5 | **0.8658** | clean (0.8658084) |

**Attempt 5 holds the highest reward, 0.8658. That is the number to beat.** Attempts 3 (0.8657) and 13 (0.8657) sit within 0.0002 of it and are effectively indistinguishable from it.

Direction of movement, stated plainly: attempt 2 (0.8079) was **lower** than attempt 1 (0.8630). Attempt 4 (0.7740) was **lower** than attempt 3. Attempts 6 (0.7580), 7 (0.4911), 8 (0.7805), 9 (0.8332), 10 (0.8503), 11 (0.8067), 12 (0.4275), 13 (0.8657), 14 (0.8513) and 15 (0.8579) were every one of them **lower** than the standing best; `standing_against_best_so_far` reads `worse_than_an_earlier_attempt` for all of them and that is a regression, not progress. Only attempts 3 and 5 ever read `better_than_every_earlier_attempt`, and attempt 1 was the first measured attempt. Nothing has improved on the standing best since attempt 5; the ten graded submissions after it all came in below it.

Secondary quantities worth carrying: `validity` was 1.0 and `red_line_crossed` 0.0 on every single record, and `zero_reason_code` was 0 throughout — no attempt was ever zeroed or invalidated. `task_pass` was 1.0 on twelve records and 0.0 on exactly three (6, 7, 12), the three records that carry failed checks.

## 2. Approach classes tried

No source code was carried forward, so these classes are reconstructed from the cost and efficiency signatures the harness reported. They separate cleanly into five families.

**Class A — baseline-cost configuration, near-unity per-step cost, full ~74 s run.** `per_step_cost_ratio` in 0.942–0.984, `compute_efficiency` mostly 0.68–0.75, `wall_clock_sec` ≈ 74.2–74.5, `qualifying_budget` equal to wall clock. This covers attempts 2 (0.8079), 3 (0.8657), 5 (0.8658), 10 (0.8503), 13 (0.8657) and 15 (0.8579). It contains every one of the top four results and is the only class that has ever produced the standing best. Within it, attempts 3, 5 and 13 land at 0.8657/0.8658/0.8657 — a spread of 0.0002, which is at or below run-to-run noise. Repeatedly re-instantiating this configuration without changing what limits it produced three statistically identical numbers; that is the pattern to avoid repeating blindly.

**Class B — aggressive per-step cost reduction.** `per_step_cost_ratio` driven down to 0.693–0.700 with `compute_efficiency` pushed to 0.9681, 1.0000 and 0.9705. Attempts 4 (0.7740), 11 (0.8067) and 14 (0.8513). Every member is clean — no failed checks, all perturbations held, `task_pass` 1.0 — and every member scores **below** the Class A best. Attempt 11 achieved a perfect `compute_efficiency` of 1.0000 and still returned only 0.8067.

**Class C — slower-than-baseline / above-unity per-step cost.** `per_step_cost_ratio` above 1.07. Attempt 1 (0.8630, cost ratio 1.0723, wall 76.34) and attempt 8 (0.7805, cost ratio 1.0848, wall 98.60, `compute_efficiency` 0.6575). Clean but never better than Class A, and the further the wall clock was extended the worse it got.

**Class D — early-qualify / shortened-budget variant.** Attempt 9 (0.8332): `qualifying_budget` 49.89 against a wall clock of 74.39, i.e. the target was reached far earlier than the run ended, with a Class-A-like cost ratio of 0.9516 and `compute_efficiency` 0.7505. Clean, all perturbations held, but below the Class A best. This is the one place where reaching the target sooner was measured without breaking anything, and it did not pay.

**Class E — the two check-breaking families.**
- *E1, module-level execution*: attempt 6 (0.7580) tripped `C-API-SURFACE`, ran at cost ratio 1.4094 with `compute_efficiency` 0.4942 and a `qualifying_budget` of 45.82 against a 70.37 s wall clock.
- *E2, budget trimmed past the held-out variant's margin*: attempts 7 (0.4911) and 12 (0.4275). Attempt 7 was the shortest run of all, wall clock and qualifying budget both 50.05, cost ratio 0.9657. Attempt 12 combined a Class-B-ish cost cut (cost ratio 0.8114, `compute_efficiency` 0.8464) with a full 74.11 s wall clock. Different-looking configurations, identical failure. These are the two lowest rewards on the board.

## 3. Checks that failed

Twelve of the fifteen records carry an empty `failed_checks` and `conformance_fraction` 1.0. Three do not.

**`C-PERTURBATION-REACHED` — failed twice, in attempts 7 and 12.** The verifier's reason is identical both times: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* Both records show `conformance_fraction` 0.5, `all_perturbations_held` false and `task_pass` 0.0. This is the finding that matters most. It has now failed twice, and the two attempts differ substantially in their measured profile — attempt 7 ran at a 0.9657 cost ratio in 50.05 s total, attempt 12 ran at a 0.8114 cost ratio over the full 74.11 s. **Whatever was changed between attempts 7 and 12 is not what is causing this check to fail.** The cost ratio is not the cause, the wall clock is not the cause, and `rule_conformance` was a clean 1.0 in both — the failure lives entirely in what the held-out perturbation run is given to work with.

**`C-API-SURFACE` — failed once, in attempt 6.** Reason: *"module-level statements outside imports, constants, and permitted definitions."* This dropped `rule_conformance` to 0.8571 and `task_pass` to 0.0 while all perturbations still held. It is a structural property of the submission file, not of the training algorithm, and it has appeared exactly once.

**Per-unit checks inside the perturbation runs.** `C-BUDGET-RESPECTED` failed twice (attempts 7 and 12). `C-TARGET-REACHED` failed once (attempt 12, alongside `C-BUDGET-RESPECTED` on the same unit). Note the ordering this implies for attempt 7: the unit blew its budget without `C-TARGET-REACHED` being separately flagged, whereas in attempt 12 the unit both missed the target and blew the budget.

## 4. Ruled-out directions

**Maximising `compute_efficiency` by cutting per-step cost to ~0.69.** Ruled out. Class B produced 0.7740, 0.8067 and 0.8513 across three clean, fully-conformant runs, all below 0.8658. Attempt 11 reached `compute_efficiency` 1.0000 — the ceiling of that quantity — and returned 0.8067, a large regression. Reward is not efficiency-dominated; the efficiency headroom has already been fully exercised and it does not buy reward.

**Extending the wall clock / running above unity per-step cost.** Ruled out. Attempt 8 stretched to 98.60 s at cost ratio 1.0848 and fell to 0.7805. Attempt 1's 1.0723 ratio reached 0.8630 but never exceeded the ~74 s Class A cluster. More compute per step is not what is missing.

**Shortening the overall run budget to qualify early.** Ruled out in its aggressive form. Attempt 7 compressed the whole run to 50.05 s and the held-out variant failed `C-BUDGET-RESPECTED`, costing roughly 0.37 of reward against the standing best. Attempt 9, the safe version of the same idea (qualifying at 49.89 s inside a full 74.39 s wall clock), stayed clean but still only reached 0.8332. Early qualification does not pay, and pushing it hard breaks a check.

**Combining a per-step cost cut with the full schedule.** Ruled out. Attempt 12 did exactly this (cost ratio 0.8114, full 74.11 s) and produced the worst reward on the board, 0.4275, with the held-out variant failing both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.

**Any module-level executable statement in the submission file.** Ruled out by `C-API-SURFACE`. Keep the module to imports, constants and permitted definitions; put all work inside the permitted entry points.

**Re-running the Class A baseline unchanged.** Ruled out as a way to gain. Attempts 3, 5 and 13 returned 0.8657, 0.8658 and 0.8657. Three samples of the same configuration establish the plateau; a fourth sample will land in the same 0.0002 band and cannot beat 0.8658 except by noise.

## 5. Open leads

**Held out beside the primary run there are exactly two perturbation units per record, of kind `held_out_variant` and kind `seed`.** Across all fifteen records that is thirty units, of which twenty-eight reached their threshold. Every single `seed` unit reached — fifteen of fifteen, with no failed check ever recorded against that kind. Every failure was on the `held_out_variant` kind: thirteen of fifteen reached, two did not, stopped by `C-BUDGET-RESPECTED` in both cases and additionally by `C-TARGET-REACHED` in one. The runs are not identified beyond their kind, so nothing here should be read as the same run recurring; what is solid is that **the `held_out_variant` kind is the fragile one and the budget check is what stops it, while the `seed` kind has never once been a problem.** The lead: whatever schedule is written must leave the held-out variant genuine budget margin. The two configurations that removed that margin — a 50 s total run, and a 0.81 cost ratio over a full run — both cost about half the reward. Size the schedule for the variant, not for the primary.

**Attempt 15 is the most informative unexploited data point.** It held a Class-A cost ratio of 0.9424 while carrying `compute_efficiency` 0.9355 — roughly 0.24 higher than attempts 3/5/13, which sat at 0.69 with the same cost ratio band — and it stayed fully clean at 0.8579. That shows efficiency can be lifted substantially without leaving the safe cost region and without breaking a perturbation. It scored 0.0079 below the best, so the lift alone did not pay, but it demonstrates that the efficiency and cost-ratio axes are separable near the baseline. Worth combining: hold cost ratio at 0.95–0.98 and full ~74 s wall clock as in attempt 5, and take whichever part of attempt 15's efficiency gain does not disturb the task-side result.

**Reward at the top of the board is being set by something other than the cost/efficiency axes.** Within the clean records, `compute_efficiency` ranges 0.66–1.00 and `per_step_cost_ratio` 0.69–1.08, and the best reward comes from the middle of both ranges, not from either extreme. The remaining headroom is therefore on the task side — final solution quality and the margin by which the target is reached — at fixed baseline cost. That is the axis that has not yet been varied deliberately: every attempt so far moved cost, schedule length, or file structure.

**The `qualifying_budget` versus `wall_clock_sec` gap is a lever that has been touched only twice** (attempt 9: 49.89 vs 74.39; attempt 6: 45.82 vs 70.37, but that record is confounded by the `C-API-SURFACE` failure). Attempt 9 was clean and cost 0.0326 against the best. Closing that gap — spending the full budget rather than qualifying at two-thirds of it — is consistent with the top cluster, where `qualifying_budget` equals the wall clock on every attempt that scored above 0.85.

**Call: exploit.** Rebuild the attempt-5 configuration — full ~74 s wall clock, `per_step_cost_ratio` in the 0.95–0.98 band, `qualifying_budget` equal to the wall clock, generous margin left for the `held_out_variant` perturbation, and a module file containing nothing but imports, constants and permitted definitions so `C-API-SURFACE` stays clean — and then change one thing on the task-quality axis rather than the cost axis. The efficiency-push class has been sampled three times and is exhausted; the budget-trim class has failed the same check twice and must not be sampled again unchanged; and re-running the Class A baseline verbatim is the thing earlier work already did three times for the same 0.8657–0.8658, which is neither exploration nor exploitation. Beat 0.8658 by improving what the baseline produces, not by making it cheaper or shorter.
