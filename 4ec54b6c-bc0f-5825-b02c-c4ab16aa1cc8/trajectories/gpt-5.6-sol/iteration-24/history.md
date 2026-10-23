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

    All 18 attempts since have scored lower than it.
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
  25       0.5053   1.000             2 of 2         yes             24                

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
  19 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 25 -- reward 0.5053, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 24
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 7 attempts (10, 11, 16, 19, 22, 23, 24). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 4 attempts (10, 16, 17, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 5 attempts (10, 11, 19, 22, 23). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Worst to best by reward:

- Attempts 10, 16, 17, and 22: reward **0.0000**. Each was worse than an earlier attempt and invalid after crossing at least one red line.
- Attempt 24: reward **0.1337**, worse than an earlier attempt.
- Attempt 19: reward **0.1470**, worse than an earlier attempt.
- Attempt 23: reward **0.1671**, worse than an earlier attempt.
- Attempt 11: reward **0.3385**, worse than an earlier attempt.
- Attempt 21: reward **0.3488**, worse than an earlier attempt.
- Attempt 9: reward **0.3601**, worse than an earlier attempt.
- Attempt 15: reward **0.4034**, worse than an earlier attempt.
- Attempt 13: reward **0.4070**, worse than an earlier attempt.
- Attempt 18: reward **0.4085**, worse than an earlier attempt.
- Attempt 14: reward **0.4201**, worse than an earlier attempt.
- Attempt 4: reward **0.4776**, worse than an earlier attempt.
- Attempt 12: reward **0.4779**, worse than an earlier attempt.
- Attempt 25: reward **0.5053**, worse than an earlier attempt.
- Attempt 1: reward **0.5513**, the first measured result.
- Attempt 3: reward **0.6043**, lower than the earlier reward from attempt 2.
- Attempt 2: reward **0.6387**, better than attempt 1.
- Attempt 8: reward **0.6481**, lower than the earlier best from attempt 6.
- Attempt 7: reward **0.6506**, lower than the earlier best from attempt 6.
- Attempt 5: reward **0.6687**, better than every earlier attempt at that point.
- Attempt 6: reward **0.6964**, the highest reward overall and the one to beat.

Attempt 20 produced no measurement because its measurement status was `harbor_exception`; it did not score zero.

Across the 24 measured submissions, all 24 ruleset perturbation units reached their thresholds. The held-out-variant units reached in 19 submissions and failed in 5 submissions. Thus, 43 of 48 measured perturbation units reached in aggregate. Every failed held-out variant was stopped by `C-BUDGET-RESPECTED`.

2. Approach classes tried

- **Fully conformant, threshold-reaching configurations:** Attempts 1–9, 12–15, 18, 21, and 25 reached the primary target and both perturbation thresholds without failed checks. Their rewards ranged from **0.3488** to **0.6964**. The strongest region was represented by attempts 5–8, especially attempt 6 at **0.6964**. The supplied records do not describe the underlying algorithm or hyperparameters, so the implementation details of this class cannot be reconstructed from the measurements alone.
- **Configurations that reached both perturbations but exceeded global limits:** Attempts 16, 17, and 24 reached both perturbation kinds. Attempts 16 and 17 nevertheless became invalid because of red-line failures; attempt 24 remained valid but exceeded the declared wall-clock ceiling and received only **0.1337**. Perturbation success by itself therefore did not guarantee a competitive or passing submission.
- **Configurations whose held-out variant missed its budget:** Attempts 10, 11, 19, 22, and 23 reached the ruleset threshold but not the held-out-variant threshold. All five failed `C-BUDGET-RESPECTED` on that kind, and all five consequently failed `C-PERTURBATION-REACHED`. Rewards ranged from **0.0000** to **0.3385**, all below the established best.
- **Execution failure:** Attempt 20 ended in a `harbor_exception` and produced no measurement. No measured algorithmic conclusion can be drawn from it.

3. Checks that failed

- `C-BUDGET-RESPECTED` failed **7 times**, in attempts 10, 11, 16, 19, 22, 23, and 24. The verifier’s reasons were:
  - Attempt 10: qualifying row at 50.55317974090576 seconds, above the declared ceiling of 31.1.
  - Attempt 11: qualifying row at 31.65315580368042 seconds, above 31.1.
  - Attempt 16: qualifying row at 32.978039026260376 seconds, above 31.1.
  - Attempt 19: qualifying row at 31.8888943195343 seconds, above 31.1.
  - Attempt 22: qualifying row at 35.771381855010986 seconds, above 31.1.
  - Attempt 23: qualifying row at 31.9768545627594 seconds, above 31.1.
  - Attempt 24: qualifying row at 38.10749435424805 seconds, above 31.1.
  
  This check has now failed seven times. Whatever changed among those attempts is not what is eliminating the wall-clock overrun. Even small overruns, such as 31.6532 or 31.8889 against 31.1, still fail.

- `C-PERTURBATION-REACHED` failed **5 times**, in attempts 10, 11, 19, 22, and 23. In every case, the verifier’s reason was: “1 of 2 declared perturbations reached their own threshold inside their own budget.” The failing kind was always `held_out_variant`, stopped by `C-BUDGET-RESPECTED`; the `ruleset` kind reached every time. This check has now failed five times. Whatever changed among those attempts is not what is fixing held-out-variant completion within budget.

- `C-PER-STEP-COST-CEILING` failed **4 times**, in attempts 10, 16, 17, and 22. The verifier’s reasons were:
  - Attempt 10: per-step cost was 4.662 times the seed anchor, above the ceiling of 3.0.
  - Attempt 16: 3.152 times the seed anchor, above 3.0.
  - Attempt 17: 8.382 times the seed anchor, above 3.0.
  - Attempt 22: 3.402 times the seed anchor, above 3.0.
  
  This check has now failed four times. Whatever changed among those attempts is not what is reliably controlling per-step cost below the hard ceiling.

No ruleset perturbation failed. Attempt 20 had no failed checks reported, but that was because it produced no measurement, not because the checks were demonstrated to hold.

4. Ruled-out directions

- **Any configuration expected to qualify above 31.1 seconds:** Ruled out because `C-BUDGET-RESPECTED` fails whenever the qualifying row exceeds that ceiling, including overruns of less than one second.
- **Any configuration with per-step cost near or above 3.0 times the seed anchor:** Ruled out as unsafe. Ratios of 3.152, 3.402, 4.662, and 8.382 all failed `C-PER-STEP-COST-CEILING` and produced reward **0.0000** in the affected attempts.
- **Treating primary-target and ruleset success as sufficient:** Ruled out because the held-out variant can still miss its own threshold inside its budget. Attempts 10, 11, 19, 22, and 23 all reached the primary target and ruleset perturbation but failed the held-out variant and `C-PERTURBATION-REACHED`.
- **Trading substantial extra runtime for threshold attainment:** Ruled out by attempts such as 24, which reached both perturbations but qualified at 38.1075 seconds and earned only **0.1337**, and by attempts 16 and 22, which crossed hard red lines and earned **0.0000**.
- **Continuing the post-attempt-6 pattern without recovering the best configuration:** No later measured attempt beat **0.6964**. Repeating configurations that retain the same budget or per-step-cost failure is neither useful exploration nor exploitation.

5. Open leads

- Recover and exploit the approach represented by attempt 6, which achieved reward **0.6964**, reached the primary target and both perturbations, had no failed checks, qualified in 19.6077 seconds, and stayed below the per-step ceiling with a ratio of 1.5374. This is the one to beat.
- Use attempts 5–8 as the empirically strongest measured neighborhood. Attempts 5, 7, and 8 scored **0.6687**, **0.6506**, and **0.6481**, respectively, while preserving full conformance and perturbation success. However, only attempt 6 set the best reward.
- Preserve hard safety margins rather than targeting the exact limits: keep qualifying wall time comfortably below 31.1 seconds and per-step cost comfortably below 3.0. The repeated failures show that near-boundary configurations are fragile and noncompetitive.
- Ensure the held-out variant reaches within its own budget, not merely that the primary and ruleset runs succeed. Aggregate evidence isolates the held-out variant as the only perturbation kind that has failed.
- Because the supplied measurements contain no algorithm descriptions or hyperparameters, do not infer which implementation change caused attempt 6’s advantage. Restore its known design if available externally, then make controlled modifications while retaining its passing profile.

**Exploit**: return to the attempt-6 approach and improve it while guarding the wall-clock, per-step-cost, and held-out-variant constraints.
