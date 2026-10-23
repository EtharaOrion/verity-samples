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

    All four attempts since have scored lower than it.
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
  28       0.8841   1.000             2 of 2         yes             25                
  29       0.9128   1.000             2 of 2         yes             25                

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
  24 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 5 -- reward 0.9128, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 27 -- reward 0.7552, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 28 -- reward 0.8841, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 29 -- reward 0.9128, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

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

Twenty-nine graded records, all with `measurement_status: measured`, so every one carries a reward. Listed worst to best.

Ten attempts produced a measured reward of exactly **0.0000**: attempts **3, 7, 9, 10, 12, 15, 16, 21, 22, 26**. Every one of them has `zero_reason_code: 4`, `primary_target_reached: 0.0`, `conformance_fraction: 0.0`, and a wall-clock time pinned in a very narrow band around 1690–1693 seconds (1692.52, 1692.21, 1692.97, 1690.96, 1690.45, 1690.48, 1691.53, 1691.00, 1690.32, 1691.57). Their `qualifying_budget` is `not-measured` in every case, because no qualifying row existed. `rule_conformance` was 1.0 in all ten and `validity` 1.0 — these were not malformed submissions; they simply never crossed the target.

The remaining nineteen, ascending by reward:

| Attempt | reward | wall_clock_sec | qualifying_budget | compute_efficiency | per_step_cost_ratio | task_pass |
|---|---|---|---|---|---|---|
| 6 | 0.5615 | 204.09 | 204.09 | 0.6091 | 1.3778 | 0.0 |
| 14 | 0.6955 | 99.74 | 99.74 | 0.9220 | 0.9155 | 1.0 |
| 8 | 0.7551 | 151.50 | 78.14 | 0.8703 | 1.0291 | 1.0 |
| 27 | 0.7552 | 25.26 | 25.26 | 0.9740 | 0.7111 | 0.0 |
| 1 | 0.7684 | 25.46 | 25.46 | 0.8160 | 1.0639 | 0.0 |
| 17 | 0.7919 | 73.80 | 73.80 | 0.9221 | 0.7318 | 1.0 |
| 2 | 0.8385 | 73.62 | 73.62 | 0.9164 | 0.9162 | 1.0 |
| 13 | 0.8451 | 71.31 | 71.31 | 0.7726 | 1.0266 | 1.0 |
| 20 | 0.8661 | 62.46 | 62.46 | 1.0000 | 0.6145 | 1.0 |
| 4 | 0.8719 | 50.03 | 50.03 | 1.0000 | 0.7115 | 1.0 |
| 23 | 0.8768 | 49.67 | 49.67 | 0.7186 | 0.9384 | 1.0 |
| 18 | 0.8794 | 49.33 | 49.33 | 0.7378 | 0.9260 | 1.0 |
| 28 | 0.8841 | 24.62 | 24.62 | 0.9772 | 0.6818 | 1.0 |
| 24 | 0.8979 | 25.37 | 25.37 | 0.7330 | 1.1078 | 1.0 |
| 11 | 0.8980 | 25.35 | 25.35 | 0.7043 | 1.0502 | 1.0 |
| 19 | 0.9121 | 45.81 | 45.81 | 0.9345 | 0.7669 | 1.0 |
| 29 | 0.9128 | 25.33 | 25.33 | 0.6950 | 0.9590 | 1.0 |
| 5 | 0.9128 | 25.34 | 25.34 | 0.7728 | 0.9887 | 1.0 |
| 25 | **0.9130** | 25.32 | 25.32 | 0.8277 | 0.8726 | 1.0 |

**Attempt 25 holds the highest reward, 0.9130. That is the score to beat.**

The trajectory is not one of steady progress and must not be read as one. Attempt 2 (0.8385) improved on attempt 1 (0.7684); attempt 4 (0.8719) improved on 2; attempt 5 (0.9128) improved on 4; attempt 25 (0.9130) improved on 5. Every other record carries `standing_against_best_so_far: worse_than_an_earlier_attempt`. In particular: attempt 6 at 0.5615 is **lower** than attempt 5's 0.9128 and is the worst non-zero result recorded; attempt 8 at 0.7551, attempt 14 at 0.6955, attempt 17 at 0.7919 and attempt 27 at 0.7552 are all **lower** than the best that preceded them; and the four most recent conforming records — 27 (0.7552), 28 (0.8841), 29 (0.9128) — are all **below** attempt 25's 0.9130. Attempt 29 comes within 0.0002 of the best but does not exceed it. Ten attempts scored a measured 0.0000, which is a regression to nothing, not a partial result.

# 2. Approach classes tried

Grouping by the measured signature rather than by record count, five distinct classes appear.

**Class A — short-budget conforming run, roughly 25 seconds, all checks held.** Attempts 5, 11, 24, 25, 28, 29. `qualifying_budget` between 24.62 and 25.37, `primary_target_reached: 1.0`, `task_pass: 1.0`, `rule_conformance: 1.0`, no failed checks, both perturbation runs reached. This class contains every one of the top four scores and the single best result (25 at 0.9130). Within the class, reward is *not* ordered by compute efficiency: attempt 28 has the shortest wall clock of any record (24.62 s) and the highest compute efficiency in the class (0.9772) but scores 0.8841, below 25's 0.9130 at 25.32 s and efficiency 0.8277. What separates the class internally tracks `per_step_cost_ratio`: the 0.913 band (25 at 0.8726, 29 at 0.9590, 5 at 0.9887) sits between the 0.898 band (11 at 1.0502, 24 at 1.1078) and the 0.884 outlier (28 at 0.6818). The association is observed, not proven, but it is consistent across six records: a per-step cost ratio in roughly 0.87–0.99 accompanies the best scores, ratios above parity cost about 0.015 of reward, and pushing the ratio down to 0.68 cost about 0.029.

**Class B — mid-budget conforming run, roughly 45–75 seconds, all checks held.** Attempts 2, 4, 13, 17, 18, 19, 20, 23, spanning 0.7919 to 0.9121. Attempt 19 (45.81 s, 0.9121) is the strongest result outside Class A and is nearly competitive with the best, so budget alone does not fully determine the outcome. Attempts 4 and 20 both achieved `compute_efficiency: 1.0` yet scored 0.8719 and 0.8661, below several Class A runs with efficiency near 0.70. Maximised compute efficiency did not buy reward here.

**Class C — long-budget conforming run, roughly 100–205 seconds.** Attempts 14 (99.74 s, 0.6955), 8 (151.50 s wall clock, 0.7551), 6 (204.09 s, 0.5615, also failing C-API-SURFACE). This class holds the three lowest non-zero rewards. Attempt 8 is the only record where `wall_clock_sec` (151.50) exceeds `qualifying_budget` (78.14) — roughly 73 seconds of work continued after the qualifying row already existed.

**Class D — runs that consumed the full ~1690-second envelope and never crossed the threshold.** Ten attempts: 3, 7, 9, 10, 12, 15, 16, 21, 22, 26. All measured 0.0000. Their per-step cost ratios (0.6827–0.8901) and compute efficiencies (0.9033–1.0) look healthy in isolation, which is exactly why they are misleading: with `primary_target_reached: 0.0` and `qualifying_budget: not-measured`, those numbers describe work that never qualified for anything.

**Class E — a submission body carrying executable statements at module level.** Attempts 1, 6, 27. This is a property that cuts across the budget classes rather than a budget strategy of its own: attempt 27 is otherwise a textbook Class A run (25.26 s, `compute_efficiency: 0.9740`, `per_step_cost_ratio: 0.7111`, target reached, both perturbations reached) yet scored only 0.7552 because of it. Attempt 1 is likewise a 25.46 s run scoring 0.7684. Attempt 6 combines the fault with a 204 s budget for the worst non-zero score, 0.5615.

# 3. Checks that failed

**C-API-SURFACE** — reason given by the verifier, identically in each instance: *"module-level statements outside imports, constants, and permitted definitions."* This has now failed **three times**, in attempts 1, 6 and 27. Those three attempts differ substantially in every other measured dimension — budgets of 25.46 s, 204.09 s and 25.26 s, per-step cost ratios of 1.0639, 1.3778 and 0.7111, compute efficiencies of 0.8160, 0.6091 and 0.9740 — so whatever was varied between them is demonstrably not what causes this check to fail. It is caused by the shape of the module body itself: something is executing at import time that is not an import, a constant, or a permitted definition. In each case `rule_conformance` fell to 0.8571428571 (six of seven rules) and `task_pass` fell to 0.0 even though `primary_target_reached` was 1.0 and both perturbation runs reached. The cost is large and consistent: attempt 27, a run whose budget and efficiency profile match the 0.913 band, scored 0.7552.

**C-TARGET-REACHED** — *"no evaluation row crosses the threshold in the declared direction."* Failed **ten times**, in attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26. Again the ten differ in per-step cost ratio (0.6827 to 0.8901) and compute efficiency (0.9033 to 1.0000) while failing identically; the varied knobs are not the cause. The invariant they share is the ~1690 s wall clock and the absence of any qualifying row.

**C-BUDGET-RESPECTED** — *"no qualifying row, so no budget position exists."* Failed the same **ten times**, always alongside C-TARGET-REACHED. This is a consequence of the target failure, not an independent budget violation: no attempt in the record set has ever failed a budget check while having a qualifying row.

**C-PERTURBATION-REACHED** — *"0 of 2 declared perturbations reached their own threshold inside their own budget."* Failed the same **ten times**, in the same records, always 0 of 2.

No record ever failed on validity (`validity: 1.0` throughout) and no record ever crossed a red line (`red_line_crossed: 0.0` throughout).

# 4. Ruled-out directions

**Executable statements at module scope.** Ruled out by three independent failures of C-API-SURFACE (attempts 1, 6, 27) with the verifier's reason unchanged each time. It forces `task_pass` to 0.0 and `rule_conformance` to 0.8571 regardless of how good the run is underneath — attempt 27 reached the target in 25.26 s with compute efficiency 0.9740 and still scored 0.7552, roughly 0.158 below the best. Everything must live inside imports, module-level constants, and function or class definitions.

**Letting the run consume the full ~1690-second envelope.** Ruled out by ten measured zeros. This is not a near-miss regime; `qualifying_budget` is `not-measured` in every one, meaning no evaluation row ever crossed the threshold in the declared direction, and both perturbation runs collapsed with it. Nothing in these ten records suggests the approach was close.

**Repeating the long-envelope configuration with a different cost knob.** The ten zeros span per-step cost ratios from 0.6827 to 0.8901 and compute efficiencies from 0.9033 to 1.0000. Adjusting those did not change the outcome once. This is the pattern to name plainly: earlier work re-ran the zero-scoring configuration repeatedly without changing the thing that made it score zero, and each repetition cost a graded attempt for no information.

**Budgets above roughly 80 seconds.** Ruled out by monotone evidence in Class C: 78.14 s → 0.7551, 99.74 s → 0.6955, 204.09 s → 0.5615. No attempt above 80 seconds has ever scored above 0.7551.

**Maximising compute efficiency as the objective.** Ruled out because it does not track reward. Attempts 4 and 20 both reached `compute_efficiency: 1.0` and scored 0.8719 and 0.8661; attempt 29 at efficiency 0.6950 scored 0.9128. Attempt 28 combined the shortest wall clock in the record set (24.62 s) with efficiency 0.9772 and a very low per-step cost ratio (0.6818) and still landed at 0.8841, below three slower Class A siblings. Driving per-step cost far below parity appears to cost more than the time it saves.

# 5. Open leads

**Reconstruct the Class A short-budget profile and hold the per-step cost ratio near 0.87–0.96.** This is the only region that has produced scores above 0.91: attempts 25 (0.9130, ratio 0.8726), 5 (0.9128, ratio 0.9887), 29 (0.9128, ratio 0.9590). The neighbouring bands are measurably worse in both directions — 1.05 and 1.11 gave 0.8980 and 0.8979, and 0.68 gave 0.8841. Aim for a qualifying budget near 25 seconds with the ratio landing just under parity.

**Recover attempt 27's run by removing the module-level statements.** That run had a 25.26 s qualifying budget, compute efficiency 0.9740, target reached and both perturbation runs reached, and lost roughly 0.16 of reward to C-API-SURFACE alone. Whatever configuration produced it, expressed with all execution confined to function bodies, is the single most concrete untried improvement in the record set. Practically: no top-level calls, no top-level loops, no top-level prints or seeding, no top-level training invocation — only imports, literal constants, `def` and `class`.

**Close attempt 8's gap between wall clock and qualifying budget.** It is the only record where the two diverge (151.50 s versus 78.14 s), and it scored 0.7551. If work continues after the qualifying row is produced, terminating immediately on threshold crossing should convert that record's profile into a Class B or Class A one at no accuracy cost. Worth confirming that the training loop breaks out as soon as the declared threshold is crossed rather than running a fixed schedule to completion.

**Probe the 45-second shoulder.** Attempt 19 scored 0.9121 at 45.81 s with compute efficiency 0.9345 and per-step cost ratio 0.7669 — essentially tied with the 25-second band despite nearly twice the budget. That suggests the reward surface has a second good region and that quality, not time, is what is binding there. A run at ~25 s with attempt 19's quality settings, if they can be separated from its budget, is the most plausible route past 0.9130.

**Treat the 0.9128–0.9130 cluster as a plateau of one configuration.** Three separate attempts (5, 25, 29) land within 0.0002 of each other. That tightness says the remaining variation in that configuration is noise, and that beating 0.9130 requires changing the quality term — what the model actually achieves on the evaluation rows — rather than re-tuning the budget or cost knobs, which have now been swept fairly thoroughly across 25, 45, 50, 62, 71, 74, 78, 100 and 204 seconds.

**Perturbation posture.** Two held-out runs are declared per attempt, one of kind `held_out_variant` and one of kind `seed`. Across the twenty-nine records that is fifty-eight held-out runs: thirty-eight reached their threshold and twenty did not. Every failure is confined to the ten Class D attempts, and in those the pattern is uniform by kind — the `held_out_variant` run failed on C-TARGET-REACHED and C-BUDGET-RESPECTED in all ten, and the `seed` run failed on exactly the same two checks in all ten. Neither kind has ever failed while the primary run succeeded, and neither has ever failed on a check the primary did not also fail. No robustness-specific weakness is visible in the data: fixing the primary target has, every time it happened, brought both held-out kinds with it. The runs are not identified across records and nothing here should be read as tracking any individual run from one attempt to the next.

**Call: exploit.** The scoring approaches have not stopped improving — attempt 25 raised the best mark, and there are two identified, unexercised gains sitting inside already-scoring runs: the C-API-SURFACE fix on attempt 27's fast profile, and the per-step-cost sweet spot around 0.87–0.96 at a ~25-second budget. Exploration in this record set has meant the ~1690-second envelope, which has returned a measured 0.0000 ten times with no sign of approaching the threshold; re-entering it without changing what causes C-TARGET-REACHED to fail would be neither exploration nor exploitation, and that is what much of the earlier work amounted to.
