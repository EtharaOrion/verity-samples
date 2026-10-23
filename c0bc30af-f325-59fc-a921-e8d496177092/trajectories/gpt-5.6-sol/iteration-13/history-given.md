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

    All seven attempts since have scored lower than it.
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
  6 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 10 -- reward 0.8503, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 75
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.8067, worse than an earlier attempt
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED has failed on 2 attempts (7, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All twelve graded records carry `measurement_status: "measured"`, so every one has a reward; none is missing a measurement, and none scored zero (`zero_reason_code` is 0 and `red_line_crossed` is 0.0 throughout, `validity` 1.0 throughout).

Worst to best by reward:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 12 | 0.4275 | failed C-PERTURBATION-REACHED; `task_pass` 0.0 |
| 2 | 7 | 0.4911 | failed C-PERTURBATION-REACHED; `task_pass` 0.0 |
| 3 | 6 | 0.7580 | failed C-API-SURFACE; `task_pass` 0.0, `rule_conformance` 0.8571 |
| 4 | 4 | 0.7740 | clean; `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934 |
| 5 | 8 | 0.7805 | clean; slowest run, `wall_clock_sec` 98.5950, `per_step_cost_ratio` 1.0848 |
| 6 | 11 | 0.8067 | clean; `compute_efficiency` 1.0000, `per_step_cost_ratio` 0.6947 |
| 7 | 2 | 0.8079 | clean; `per_step_cost_ratio` 0.9441 |
| 8 | 9 | 0.8332 | clean; `qualifying_budget` 49.8865 vs `wall_clock_sec` 74.3877 |
| 9 | 10 | 0.8503 | clean; `per_step_cost_ratio` 0.9615, `compute_efficiency` 0.7433 |
| 10 | 1 | 0.8630 | clean; `per_step_cost_ratio` 1.0723, `compute_efficiency` 0.6784 |
| 11 | 3 | 0.8657 | clean; `per_step_cost_ratio` 0.9835, `compute_efficiency` 0.6922 |
| 12 (best) | 5 | **0.8658** | clean; `per_step_cost_ratio` 0.9581, `compute_efficiency` 0.6926 |

**Attempt 5 holds the highest reward at 0.8658 and is the one to beat.** Attempt 3 at 0.8657 is within 0.0001 of it and should be treated as the same operating point, not as a distinct second-best idea.

Direction of travel, stated plainly rather than softened: after attempt 5, every single subsequent attempt (6, 7, 8, 9, 10, 11, 12) is marked `worse_than_an_earlier_attempt`. Attempts 2, 4, 8, 9, 10, 11 were clean regressions — they passed every check and still scored below the incumbent (0.8079, 0.7740, 0.7805, 0.8332, 0.8503, 0.8067 against 0.8658). Only three records ever improved on the state of the art: attempt 1 (`first_measured_attempt`, 0.8630), attempt 3 (0.8657) and attempt 5 (0.8658). The improvement from 1 to 5 totals 0.0028 across the whole run; the regressions since have been up to 0.4383. The search has not been climbing since attempt 5.

# 2. Approach classes tried

I was given measured terms only, not the source of any submission, so these classes are reconstructed from the cost and conformance signatures the terms expose. Treat the signature, not a guessed implementation, as the identifying fact.

**Class A — the baseline-cost operating point (attempts 1, 3, 5, 10, and 2 nearby).** `per_step_cost_ratio` between 0.9441 and 1.0723, `compute_efficiency` between 0.6784 and 0.7433, `wall_clock_sec` 74–76 with `qualifying_budget` equal to it. This class contains every attempt that ever led: 0.8630, 0.8657, 0.8658, 0.8503, with 0.8079 as the weak member. All perturbations held every time. This is the productive class and the best-so-far lives inside it.

**Class B — aggressive per-step speed-up (attempts 4 and 11).** `per_step_cost_ratio` driven down to 0.6934 and 0.6947, `compute_efficiency` pushed to 0.9681 and 1.0000 — the highest efficiency figures anywhere in the record set, with attempt 11 hitting the efficiency ceiling exactly. Both were fully conformant, both reached the primary target, both held all perturbations, and both scored *below* class A: 0.7740 and 0.8067 against 0.8658. Maximising `compute_efficiency` demonstrably does not maximise reward.

**Class C — the slow / expensive direction (attempt 8).** `per_step_cost_ratio` 1.0848, `wall_clock_sec` 98.5950 (the only run near 100 s; everything else sits at 45–77 s), `compute_efficiency` 0.6575, the lowest of any clean run. Fully conformant, all perturbations held, reward 0.7805. Spending more wall clock than the class A point bought nothing.

**Class D — short qualifying budget with unchanged wall clock (attempts 9 and 6).** These are the only records where `qualifying_budget` is materially below `wall_clock_sec`: 49.8865 vs 74.3877 for attempt 9, and 45.8165 vs 70.3708 for attempt 6. Attempt 9 was otherwise clean and scored 0.8332, below the class A point. Attempt 6 carried the C-API-SURFACE failure and scored 0.7580. Reaching the qualifying point earlier, on its own, did not raise reward.

**Class E — the two perturbation-breaking variants (attempts 7 and 12).** These are the only records with `all_perturbations_held: false` and `conformance_fraction` 0.5, and they are the two worst results overall at 0.4911 and 0.4275. Their cost signatures differ from each other (attempt 7: `per_step_cost_ratio` 0.9657, `wall_clock_sec` 50.0477, `qualifying_budget` 50.0477 — the shortest run recorded; attempt 12: `per_step_cost_ratio` 0.8114, `compute_efficiency` 0.8464, `wall_clock_sec` 74.1098), so they are not one repeated idea, but they share the same consequence: the held-out variant ran out of budget.

**Class F — the module-surface violation (attempt 6).** Distinguished not by cost but by `rule_conformance` 0.8571 and the C-API-SURFACE failure described below. Its `task_pass` went to 0.0 despite `primary_target_reached` 1.0 and both perturbations holding.

# 3. Checks that failed

Two named checks failed, across three records.

**C-PERTURBATION-REACHED — failed twice**, in attempt 7 and attempt 12. The verifier's reason is identical both times: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* Both records show `conformance_fraction` 0.5, `all_perturbations_held: false`, and `task_pass` 0.0, and both are the two lowest rewards on record (0.4911 and 0.4275). Because this check has now failed twice under two different cost signatures — attempt 7 at `per_step_cost_ratio` 0.9657 and a 50.0477 s wall clock, attempt 12 at 0.8114 and a 74.1098 s wall clock — **whatever was changed between those two attempts is not what is causing this failure.** The per-step cost and the total wall clock were both varied between them and the check failed regardless. Note also that in both records `primary_target_reached` is 1.0 and `rule_conformance` is 1.0: the primary run and the rule surface were fine, and only the held-out work failed.

**C-API-SURFACE — failed once**, in attempt 6. Reason: *"module-level statements outside imports, constants, and permitted definitions."* This dropped `rule_conformance` to 0.8571 and `task_pass` to 0.0 even though `primary_target_reached` was 1.0 and both perturbation units held cleanly. The fix is mechanical: keep the submission module to imports, constants and permitted definitions, with no executable statements at module scope — no top-level configuration calls, no top-level prints, no computation performed at import time. Move any such work inside the permitted function or class bodies.

Nine records — attempts 1, 2, 3, 4, 5, 8, 9, 10, 11 — have an empty `failed_checks` list. Conformance is a solved problem for the class A/B/C/D shapes; it is only the two perturbation-breaking variants and the one module-surface variant that broke it.

# 4. Ruled-out directions

**Maximising `compute_efficiency` / minimising per-step cost.** Ruled out by attempts 4 and 11. Attempt 11 reached `compute_efficiency` 1.0000 exactly and `per_step_cost_ratio` 0.6947, was fully conformant, held both perturbations, and scored 0.8067 — below the 0.8658 incumbent. Attempt 4 at 0.9681 efficiency scored 0.7740, lower still. Two independent tries at the same lever both regressed, so reward is not monotone in efficiency and driving the per-step cost toward 0.69 is a losing move at this operating point.

**Spending more wall clock.** Ruled out by attempt 8, the only run near 98.6 s. It was clean on every check with all perturbations held, and it scored 0.7805 — well below the ~74 s class A runs. Extra time does not convert into reward here.

**Shortening the qualifying budget while leaving wall clock alone.** Ruled out by attempt 9: `qualifying_budget` 49.8865 against `wall_clock_sec` 74.3877, clean on every check, and 0.8332 — still below 0.8658. Reaching the qualifying point sooner is not itself rewarded.

**Any change that compresses the budget available to the held-out variant.** Ruled out by attempts 7 and 12, which lost roughly 0.38 to 0.44 of reward relative to the incumbent purely from C-PERTURBATION-REACHED. The cost of failing this check dwarfs any efficiency gain that has ever been measured, so it must not be traded against.

**Executable statements at module scope.** Ruled out by attempt 6's C-API-SURFACE failure; it zeroed `task_pass` for a purely structural reason and cost 0.1078 of reward against the incumbent.

**Repeating the class A point unchanged.** Attempts 3 and 5 differ by 0.0001 in reward (0.8657 vs 0.8658), which is inside the noise of a single re-run. Re-submitting that exact operating point again is not a way to make progress; it is a way to redraw the same number.

# 5. Open leads

**Per-run outcomes by kind, since this is where the loss is concentrated.** Twenty-four perturbation units were run in total, two per record, `perturbations_declared: 2.0` throughout, one of kind `seed` and one of kind `held_out_variant` in every record. The runs are not identified by name, number or position, and nothing in the terms links a run in one record to a run in another, so no such identification should be assumed.

- **`seed` kind: 12 of 12 reached their threshold, with no failed checks anywhere.** This kind has never once failed. Seed robustness is not the problem.
- **`held_out_variant` kind: 10 of 12 reached; 2 did not.** One of the failures stopped on `C-BUDGET-RESPECTED` alone; the other stopped on both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. In aggregate, `C-BUDGET-RESPECTED` is the check that stopped a held-out-variant run on both occasions, and `C-TARGET-REACHED` accompanied it once.

That is the single clearest lead: **every perturbation failure on record is a held-out-variant run running out of budget, and the seed kind has never failed.** The primary run reached its target in both of those records, so the algorithm is not broken — it is tuned so tightly to the primary configuration that the variant has no budget headroom. Build in explicit headroom for the held-out variant: converge with margin rather than exactly at the budget line, and prefer schedules that reach threshold well before the budget rather than schedules that land on it.

**Lead 1 — return to the class A operating point and vary something other than cost.** Re-establish `per_step_cost_ratio` in the 0.95–0.99 band with `compute_efficiency` around 0.69–0.70 and `wall_clock_sec` near 74, which is exactly the attempts 3 and 5 signature and the only signature that has ever led. Then change the learning algorithm itself — optimiser, schedule shape, initialisation, regularisation, data ordering — while holding the cost signature fixed. Every lever tried so far since attempt 5 moved cost; none of the clean regressions tested a quality change at constant cost.

**Lead 2 — read the non-monotonicity as a ridge and probe it locally.** Across the clean runs, reward peaks at `compute_efficiency` ≈ 0.69 (0.8658) and falls off in both directions: down to 0.7805 at 0.6575 and down to 0.7740 / 0.8067 at 0.9681 / 1.0000. The interior peak means small local perturbations around the attempt-5 point are more informative than large ones. Do not step further than the 0.94–1.08 `per_step_cost_ratio` band already sampled; the excursions outside it are all measured losses.

**Lead 3 — bank the two conformance fixes for free.** Keep the module to imports, constants and permitted definitions (C-API-SURFACE), and size the run so the held-out variant has slack (C-BUDGET-RESPECTED / C-PERTURBATION-REACHED). Neither is a scoring idea, but the three records that missed them gave up between 0.1078 and 0.4383 of reward, which is one to two orders of magnitude more than the entire measured spread among the leading clean runs.

**Lead 4 — attempt 1's high-cost variant is under-explored on the upper side of the ridge.** It scored 0.8630 at `per_step_cost_ratio` 1.0723, essentially matching attempts 3 and 5 from the expensive side, while attempt 8 at 1.0848 fell to 0.7805. There is a narrow region between 1.07 and 1.08 where behaviour changes sharply. If a quality improvement needs a little more per-step cost, 1.07 is demonstrably affordable and 1.08 is not.

## Call: exploit

Exploit. The class A operating point already scores 0.8658 and is the incumbent to beat; the losses since are all attributable to identified causes — two moved the cost off the ridge in one direction or the other, two broke the held-out variant's budget, one put statements at module scope. Every one of those is a known, fixable thing rather than evidence that the approach is exhausted. Reproduce the attempt-5 signature, apply the C-API-SURFACE and held-out-variant-headroom fixes so they can never cost anything again, and then vary the training algorithm at constant cost.

One caution about how earlier work behaved, since it bears on what not to repeat: the loop has already tried the pure-efficiency lever twice (attempts 4 and 11) and got a regression both times, and has broken C-PERTURBATION-REACHED twice (attempts 7 and 12) while varying cost between them, which is exactly the pattern of re-running a losing idea without changing what made it lose. Moving the cost ratio again, in either direction, is not a new experiment.
