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

    All 16 attempts since have scored lower than it.
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

    attempt 21 -- reward 0.3488, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
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

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 6 attempts (10, 11, 16, 19, 22, 23). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 4 attempts (10, 16, 17, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 5 attempts (10, 11, 19, 22, 23). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Measured attempts, ordered from worst to best by reward:

- Attempts 10, 16, 17, and 22: reward 0.0000. Each was worse than an earlier attempt and invalid after crossing a red line.
- Attempt 19: reward 0.1470, worse than an earlier attempt.
- Attempt 23: reward 0.1671, worse than an earlier attempt.
- Attempt 11: reward 0.3385, worse than an earlier attempt.
- Attempt 21: reward 0.3488, worse than an earlier attempt.
- Attempt 9: reward 0.3601, worse than an earlier attempt.
- Attempt 15: reward 0.4034, worse than an earlier attempt.
- Attempt 13: reward 0.4070, worse than an earlier attempt.
- Attempt 18: reward 0.4085, worse than an earlier attempt.
- Attempt 14: reward 0.4201, worse than an earlier attempt.
- Attempt 4: reward 0.4776, worse than an earlier attempt.
- Attempt 12: reward 0.4779, worse than an earlier attempt.
- Attempt 1: reward 0.5513, the first measured result.
- Attempt 3: reward 0.6043, lower than the earlier best from attempt 2.
- Attempt 2: reward 0.6387, better than attempt 1.
- Attempt 8: reward 0.6481, lower than the earlier best from attempt 6.
- Attempt 7: reward 0.6506, lower than the earlier best from attempt 6.
- Attempt 5: reward 0.6687, better than every earlier attempt at that point.
- Attempt 6: reward 0.6964, the highest reward overall and the one to beat.

Attempt 20 produced no measurement because its measurement status was `harbor_exception`; it has no reward and cannot be ranked.

All measured attempts reached the primary target. Attempts 1–9, 12–18, and 21 held both perturbations; attempts 10, 11, 19, 22, and 23 did not.

2. Approach classes tried

The records contain no source-code or algorithm descriptions, so the exact training methods, hyperparameters, and changes cannot be reconstructed. The observable approach classes are therefore grouped by measured behavior:

- Fully conforming, perturbation-robust approaches: attempts 1–9, 12–15, 18, and 21 reached the primary target and both perturbation thresholds without failed checks. Their rewards ranged from 0.3488 to 0.6964. The strongest region was attempts 5–8, especially attempt 6 at 0.6964. Attempt 6 combined a qualifying budget of 19.6077 seconds with a per-step cost ratio of 1.5374, although its reported compute efficiency was only 0.5781.
- Fully perturbation-reaching but red-line-crossing approaches: attempts 16 and 17 reached both perturbations but violated the per-step cost ceiling; attempt 16 also exceeded the wall-clock budget. Both received reward 0.0000.
- Budget-bound approaches that lost the held-out variant: attempts 11, 19, and 23 remained valid but exceeded the 31.1-second declared ceiling and consequently reached only one of two perturbations. Their rewards were 0.3385, 0.1470, and 0.1671 respectively.
- Budget-bound and cost-bound invalid approaches: attempts 10 and 22 exceeded both the declared wall-clock ceiling and per-step cost ceiling, failed the held-out variant, and received reward 0.0000.
- Infrastructure-exception approach: attempt 20 produced no measurement, so no performance conclusion can be drawn from it.

Across the 22 measured submissions, the ruleset perturbation reached its threshold 22 of 22 times. The held-out-variant perturbation reached its threshold 17 of 22 times and failed 5 of 22 times; every such failure was stopped by `C-BUDGET-RESPECTED`. Thus, in aggregate, 39 of 44 measured perturbation units reached their thresholds.

3. Checks that failed

- `C-BUDGET-RESPECTED` failed 6 times, in attempts 10, 11, 16, 19, 22, and 23. The verifier’s reasons were that the qualifying row sat above the declared ceiling of 31.1 seconds:
  - Attempt 10: 50.55317974090576 seconds.
  - Attempt 11: 31.65315580368042 seconds.
  - Attempt 16: 32.978039026260376 seconds.
  - Attempt 19: 31.8888943195343 seconds.
  - Attempt 22: 35.771381855010986 seconds.
  - Attempt 23: 31.9768545627594 seconds.
  This repeated failure shows that whatever changed among these attempts was not what was causing the budget-overrun condition; the fix must ensure the qualifying row is safely below 31.1 seconds rather than merely near it.

- `C-PERTURBATION-REACHED` failed 5 times, in attempts 10, 11, 19, 22, and 23. In every case, the verifier’s reason was: “1 of 2 declared perturbations reached their own threshold inside their own budget.” By kind, the held-out variant failed on `C-BUDGET-RESPECTED`, while the ruleset reached its threshold. Whatever changed among these five attempts was not what was causing this repeated perturbation failure; it remained coupled to the held-out variant’s budget overrun.

- `C-PER-STEP-COST-CEILING` failed 4 times:
  - Attempt 10: per-step cost was 4.662 times the seed anchor, above the ceiling of 3.0.
  - Attempt 16: 3.152 times the seed anchor, above 3.0.
  - Attempt 17: 8.382 times the seed anchor, above 3.0.
  - Attempt 22: 3.402 times the seed anchor, above 3.0.
  Whatever changed among these attempts was not what was causing this repeated excessive-cost condition. A ratio merely close to 3.0 is also risky: attempt 19 stayed under the check at 2.9956 but still had little margin.

No named checks failed in attempts 1–9, 12–15, 18, or 21. Attempt 20 produced no measurement, so its empty `failed_checks` list is not evidence that checks passed.

4. Ruled-out directions

- Do not repeat configurations with per-step cost ratios above 3.0. Attempts 10, 16, 17, and 22 all failed `C-PER-STEP-COST-CEILING`, crossed the red line, became invalid, and received reward 0.0000.
- Do not target qualification at or just below the 31.1-second ceiling without substantial safety margin. Attempts 11, 19, and 23 overran it by less than one second, yet still failed `C-BUDGET-RESPECTED`, lost the held-out variant, failed the task pass, and scored far below the best.
- Do not trade robustness for longer execution. Attempts 10 and 22 exceeded the budget, exceeded the per-step ceiling, and failed the held-out variant; both received reward 0.0000.
- Do not assume that reaching both perturbations is sufficient for a useful score. Attempts 16 and 17 reached both perturbations but were invalidated by red-line cost failures. Conversely, fully conforming attempts 12–15, 18, and 21 still scored only 0.3488–0.4779, well below attempt 6.
- Do not continue the later fully conforming performance regime unchanged. Attempts 12–15, 18, and 21 all passed every check but remained materially below the 0.6964 best. Repeating those measured characteristics without a change directed toward reward improvement is not progress.
- Attempt 20’s exception is not evidence for or against its underlying algorithm. It produced no measurement, so that direction cannot be rejected on reward, but it must not be treated as successful.

5. Open leads

- Reconstruct and exploit the behavior of attempt 6, which has reward 0.6964 and is the one to beat. Preserve its successful properties: primary target reached, both perturbations reached, full conformance, validity, qualifying budget around 19.6077 seconds, and per-step cost ratio around 1.5374.
- Compare the high-performing neighborhood represented by attempts 5–8. Attempts 5 and 6 improved the best reward to 0.6687 and 0.6964, while nearby attempts 7 and 8 fell to 0.6506 and 0.6481. Since the records omit implementation details, the next author should recover the actual code-level differences if available elsewhere and retain the attempt-6 choices rather than infer them from timing alone.
- Seek reward improvements while maintaining generous guardrails: qualifying time comfortably below 31.1 seconds and per-step cost comfortably below 3.0. The measured failures show that operating near either boundary is fragile and unnecessary because the best attempt already passed with substantial margin.
- If revisiting a budget-bound design, fix the held-out variant specifically: it is the only perturbation kind ever observed to fail, and all five such failures were stopped by `C-BUDGET-RESPECTED`. The ruleset perturbation has reached its threshold in every measured submission.
- Treat runtime and cost metrics as constraints rather than standalone optimization targets. Attempt 6 had lower reported compute efficiency than many lower-scoring attempts, while attempts with compute efficiency 1.0 often scored poorly. Likewise, a low per-step ratio alone did not guarantee a high reward.
- Avoid repeating zero-reward approaches unless the exact failed condition is changed. Repeating an approach that scored 0.0000 while leaving its budget or per-step violation intact would be neither exploration nor exploitation.

Exploit: refine the attempt-6 approach while preserving its full perturbation coverage and wide conformance margins.
