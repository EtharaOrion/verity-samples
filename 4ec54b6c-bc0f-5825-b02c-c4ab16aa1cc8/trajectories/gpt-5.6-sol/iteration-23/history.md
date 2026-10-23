# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 6 -- reward 0.6964, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All 17 attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.5513   1.000             2 of 2         yes             23                
  2        0.6387   1.000             2 of 2         yes             16                
  3        0.6043   1.000             2 of 2         yes             20                
  4        0.4776   1.000             2 of 2         yes             28                
  5        0.6687   1.000             2 of 2         yes             19                
  6 *      0.6964   1.000             2 of 2         yes             20                
  7        0.6506   1.000             2 of 2         yes             20                
  8        0.6481   1.000             2 of 2         yes             20                
  9        0.3601   1.000             2 of 2         yes             28                
  10       0.0000   1.000             1 of 2         yes             51                
  11       0.3385   1.000             1 of 2         yes             32                
  12       0.4779   1.000             2 of 2         yes             28                
  13       0.4070   1.000             2 of 2         yes             28                
  14       0.4201   1.000             2 of 2         yes             28                
  15       0.4034   1.000             2 of 2         yes             25                
  16       0.0000   1.000             2 of 2         yes             33                
  17       0.0000   1.000             2 of 2         yes             26                
  18       0.4085   1.000             2 of 2         yes             30                
  19       0.1470   1.000             1 of 2         yes             32                
  20       --       --                --             --              --                
  21       0.3488   1.000             2 of 2         yes             28                
  22       0.0000   1.000             1 of 2         yes             36                
  23       0.1671   1.000             1 of 2         yes             32                
  24       0.1337   1.000             2 of 2         yes             38                

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
  18 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 5 -- reward 0.6687, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 19
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 7 -- reward 0.6506, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 22 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 36
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 2 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 35.771381855010986 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget
        C-PER-STEP-COST-CEILING -- per-step cost is 3.402 times the seed anchor, above the ceiling of 3.0

    attempt 23 -- reward 0.1671, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 32
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 3 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 31.9768545627594 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 24 -- reward 0.1337, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 38
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 38.10749435424805 on the wall_clock_sec axis, above the declared ceiling of 31.1

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 7 attempts (10, 11, 16, 19, 22, 23, 24). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 4 attempts (10, 16, 17, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 5 attempts (10, 11, 19, 22, 23). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Every graded attempt, ordered from worst to best by reward:

- Attempts 10, 16, 17, and 22: reward **0.0000** each. All were worse than an earlier attempt. Attempts 10, 16, 17, and 22 were invalid after crossing a red line; attempt 10 also failed one perturbation, while attempts 16 and 17 still reached both perturbations.
- Attempt 24: reward **0.1337**, worse than an earlier attempt.
- Attempt 19: reward **0.1470**, worse than an earlier attempt; only one of two perturbations reached its threshold within budget.
- Attempt 23: reward **0.1671**, worse than an earlier attempt; only one of two perturbations reached its threshold within budget.
- Attempt 11: reward **0.3385**, worse than an earlier attempt; only one of two perturbations reached its threshold within budget.
- Attempt 21: reward **0.3488**, worse than an earlier attempt.
- Attempt 9: reward **0.3601**, worse than an earlier attempt.
- Attempt 15: reward **0.4034**, worse than an earlier attempt.
- Attempt 13: reward **0.4070**, worse than an earlier attempt.
- Attempt 18: reward **0.4085**, worse than an earlier attempt.
- Attempt 14: reward **0.4201**, worse than an earlier attempt.
- Attempt 4: reward **0.4776**, lower than the earlier best held by attempt 2.
- Attempt 12: reward **0.4779**, worse than an earlier attempt.
- Attempt 1: reward **0.5513**, the first measured result.
- Attempt 3: reward **0.6043**, lower than attempt 2’s earlier reward.
- Attempt 2: reward **0.6387**, better than attempt 1.
- Attempt 8: reward **0.6481**, lower than the earlier best held by attempt 6.
- Attempt 7: reward **0.6506**, lower than attempt 6’s earlier reward.
- Attempt 5: reward **0.6687**, better than every earlier attempt at that point.
- Attempt 6: reward **0.6964**, better than every earlier attempt and the highest reward overall. **Attempt 6 is the one to beat.**
- Attempt 20 had measurement status `harbor_exception` and produced **no measurement**; it must not be treated as a zero-reward result.

Chronologically, only attempts 2, 5, and 6 improved the best-so-far reward after the initial measurement. Every measured attempt after attempt 6 was lower than that earlier best.

Across the 23 measured submissions, there were 46 declared perturbation units:

- `held_out_variant`: 18 reached their thresholds and 5 did not. Every failure of this kind was stopped by `C-BUDGET-RESPECTED`.
- `ruleset`: all 23 reached their thresholds; none failed a check.
- Aggregate: 41 of 46 perturbation units reached their thresholds. Eighteen measured submissions held both perturbations, while five held only one.
- Attempt 20 supplied no measured perturbation outcomes.

2. Approach classes tried

The submission code and hyperparameter changes are not present in the measured terms, so exact algorithms cannot be reconstructed. The observable approach classes are:

- **Fully conforming, relatively strong runs:** Attempts 1–8 all reached the primary target and both perturbation thresholds, had no failed checks, and earned rewards from **0.4776** to **0.6964**. Attempts 5 and 6 were the strongest instances. Attempt 6 combined reward **0.6964**, qualifying budget 19.6077 seconds, per-step cost ratio 1.5374, and full perturbation coverage. Attempt 5 was the nearest strong predecessor at **0.6687**, with a 19.4243-second qualifying budget and per-step cost ratio 1.0830.
- **Fully conforming but lower-reward runs:** Attempts 9, 12–15, 18, and 21 reached the primary target and both perturbations with no failed checks, but all scored below the best. Their rewards ranged from **0.3488** to **0.4779**. These runs generally used qualifying budgets around 24.8389–30.0896 seconds, except attempt 9, whose qualifying budget was 28.3438 seconds and wall clock was 31.3334 seconds.
- **Near-ceiling runs that lost the held-out variant:** Attempts 11, 19, and 23 reached the primary target and the `ruleset` perturbation, but the `held_out_variant` failed `C-BUDGET-RESPECTED`. Their qualifying times were 31.6532, 31.8889, and 31.9769 seconds against a 31.1-second ceiling. Rewards were only **0.3385**, **0.1470**, and **0.1671**.
- **Hard cost or budget violations:** Attempts 10, 16, 17, and 22 crossed a red line and earned **0.0000**. Attempts 10 and 22 exceeded both the wall-clock ceiling and per-step cost ceiling and also lost the held-out perturbation. Attempt 16 exceeded both ceilings despite reaching both perturbations. Attempt 17 stayed within the wall-clock ceiling but had a per-step cost ratio of 8.3821.
- **Budget-only overrun despite complete perturbation coverage:** Attempt 24 reached the primary target and both perturbations and remained valid, but its qualifying row was at 38.1075 seconds, above the 31.1-second ceiling. It earned only **0.1337**.
- **Infrastructure or execution failure:** Attempt 20 ended in `harbor_exception` and produced no measurement, so no algorithmic conclusion can be drawn from it.

3. Checks that failed

- **`C-BUDGET-RESPECTED` failed 7 times**, on attempts 10, 11, 16, 19, 22, 23, and 24.
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 16: “the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 19: “the qualifying row sits at 31.8888943195343 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 22: “the qualifying row sits at 35.771381855010986 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 23: “the qualifying row sits at 31.9768545627594 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 24: “the qualifying row sits at 38.10749435424805 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - This repeated check is the dominant failure. It has now failed seven times; whatever was changed between those attempts is not what is causing the recurring budget violation, because the same boundary is repeatedly exceeded.

- **`C-PERTURBATION-REACHED` failed 5 times**, on attempts 10, 11, 19, 22, and 23. In every case the verifier’s reason was: “1 of 2 declared perturbations reached their own threshold inside their own budget.”
  - The failing perturbation kind was always `held_out_variant`, stopped by `C-BUDGET-RESPECTED`.
  - The `ruleset` perturbation reached its threshold in every measured submission.
  - This check has now failed five times; whatever changed among those attempts is not what is causing the repeated failure. The observable recurring condition is that the held-out variant misses its budget while the ruleset succeeds.

- **`C-PER-STEP-COST-CEILING` failed 4 times**, on attempts 10, 16, 17, and 22.
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”
  - Attempt 16: “per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0”
  - Attempt 17: “per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0”
  - Attempt 22: “per-step cost is 3.402 times the seed anchor, above the ceiling of 3.0”
  - This check has now failed four times; whatever changed between those attempts is not what is causing the recurring excess per-step cost. Ratios above 3.0 repeatedly trigger the same red-line failure.

4. Ruled-out directions

- **Running near or above the 31.1-second wall-clock ceiling without substantial safety margin is ruled out.** Attempts 11, 19, and 23 missed it by less than one second, yet each lost the held-out perturbation and scored far below the best. Attempts 10, 16, 22, and 24 exceeded it more substantially and also performed poorly or became invalid.
- **Using per-step work above 3.0 times the seed anchor is ruled out.** Attempts 10, 16, 17, and 22 all failed `C-PER-STEP-COST-CEILING`; the invalid attempts earned **0.0000**. Attempt 19’s ratio of 2.9956 technically stayed below the ceiling, but its tiny margin did not protect it from the separate wall-clock failure.
- **Trading perturbation robustness for more primary-run work is ruled out under the observed outcomes.** Whenever the held-out variant failed, the reward was at most **0.3385**, well below the **0.6964** best. The ruleset was never the weak point; the held-out variant’s budget is the constraint requiring protection.
- **Simply spending more wall-clock time is ruled out as a reward-improvement strategy.** Attempt 24 used 38.1075 seconds and earned **0.1337**; attempt 10 used 50.5532 seconds and earned **0.0000**. Meanwhile, the best attempt qualified in 19.6077 seconds.
- **Repeating later fully conforming but slower/lower-reward configurations is not justified.** Attempts 12–15, 18, and 21 all passed the primary and perturbation requirements but remained between **0.3488** and **0.4779**, substantially below attempts 5 and 6.
- **Repeating a zero-reward high-cost configuration without changing the budget or per-step-cost failure is neither exploration nor exploitation.** The recurring red-line checks already identify why those attempts cannot compete.

5. Open leads

- Return to the observable operating region of attempts 5 and 6: approximately 19.4–19.6 seconds to qualification, complete primary and perturbation success, and per-step cost comfortably below 3.0. Attempt 6’s **0.6964** is the benchmark.
- Prefer refinements around the attempt-6 approach rather than later slower families. Although attempt 7 had similar qualifying time and per-step cost, its reward fell to **0.6506**, so merely matching coarse timing is insufficient; preserve the specific algorithmic choices of attempt 6 if they can be recovered.
- Keep explicit safety margins. A target below roughly 30 seconds is safer than tuning to 31.1 seconds, and a per-step cost ratio materially below 3.0 is safer than attempt 19’s 2.9956.
- Preserve the consistently successful `ruleset` behavior while specifically ensuring the `held_out_variant` qualifies inside its own budget. No evidence supports spending effort on ruleset robustness because it succeeded in all 23 measured runs.
- Investigate changes that improve reward without adding runtime: cheaper update calculations, fewer expensive operations per step, or earlier attainment of the same target. The measurements support the constraint objective, but they do not reveal which concrete implementation changes will achieve it.
- Treat attempt 20 only as an execution exception to avoid, not as evidence about model quality.

**Call: exploit.** Refine the already successful attempt-6 class while preserving full perturbation coverage and ample wall-clock and per-step-cost headroom.
