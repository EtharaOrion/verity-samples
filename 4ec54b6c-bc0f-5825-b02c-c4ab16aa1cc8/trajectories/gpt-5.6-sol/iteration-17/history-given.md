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

    All ten attempts since have scored lower than it.
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

    attempt 14 -- reward 0.4201, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 15 -- reward 0.4034, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 16 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 33
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PER-STEP-COST-CEILING -- per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 3 attempts (10, 11, 16). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 2 attempts (10, 16). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 2 attempts (10, 11). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

All submissions were measured. Ranked worst to best by reward:

- Attempts 10 and 16: reward 0.0000. Both were worse than an earlier attempt and invalid after crossing red-line checks.
- Attempt 11: reward 0.3385. Worse than an earlier attempt.
- Attempt 9: reward 0.3601. Worse than an earlier attempt.
- Attempt 15: reward 0.4034. Worse than an earlier attempt.
- Attempt 13: reward 0.4070. Worse than an earlier attempt.
- Attempt 14: reward 0.4201. Worse than an earlier attempt.
- Attempt 4: reward 0.4776. Worse than an earlier attempt.
- Attempt 12: reward 0.4779. Worse than an earlier attempt.
- Attempt 1: reward 0.5513, the initial measured result.
- Attempt 3: reward 0.6043. This was lower than the earlier reward from attempt 2.
- Attempt 2: reward 0.6387, an improvement over attempt 1.
- Attempt 8: reward 0.6481. Despite exceeding attempts 1–3 by reward, it was lower than the then-best attempt 6.
- Attempt 7: reward 0.6506. This was lower than the earlier reward from attempt 6.
- Attempt 5: reward 0.6687, then the best result.
- Attempt 6: reward 0.6964. This is the highest reward and is the one to beat.

Attempt 6 reached the primary target and both perturbation thresholds with full conformance and validity. Its qualifying budget was 19.6077 seconds, compute efficiency 0.5781, and per-step cost ratio 1.5374.

2. Approach classes tried

The records do not describe implementation details, model architecture, optimizer settings, or training code, so the exact algorithmic approaches cannot be reconstructed. The measurable approach classes are:

- Fully conforming, perturbation-robust runs: attempts 1–9 and 12–15 reached the primary target, the held-out variant, and the ruleset threshold with no failed checks. Rewards varied widely from 0.3601 to 0.6964, showing that merely passing every check is not enough to reproduce the best reward.
- Moderate-runtime, higher-reward runs: attempts 2, 3, 5, 6, 7, and 8 qualified in roughly 16.4–20.3 seconds and scored from 0.6043 to 0.6964. Attempts 5 and 6 established successive best rewards. Attempt 6 remains strongest, while attempts 7 and 8 were lower than it.
- Slower fully conforming runs: attempts 4, 9, and 12–15 generally qualified around 24.8–28.5 seconds and scored only 0.3601–0.4779. These changes were plainly worse than the earlier best.
- Over-budget runs with a held-out perturbation failure: attempts 10 and 11 reached the primary target and ruleset threshold, but the held-out-variant kind did not reach its threshold within budget because of `C-BUDGET-RESPECTED`. Attempt 10 additionally exceeded the per-step ceiling and became invalid; attempt 11 remained valid but did not pass the task.
- Globally over-budget/high-cost run despite perturbation success: attempt 16 reached both perturbation thresholds but failed global `C-BUDGET-RESPECTED` and `C-PER-STEP-COST-CEILING`, yielding reward 0.0000.

Across all measured records and perturbation kinds:

- `held_out_variant`: reached in 14 of 16 submissions; failed in 2 of 16, both stopped by `C-BUDGET-RESPECTED`.
- `ruleset`: reached in all 16 submissions, with no perturbation-level failed check.
- Both declared perturbations held in 14 of 16 submissions. The two exceptions were attempts 10 and 11.
- In aggregate, 30 of 32 perturbation units reached their thresholds.

3. Checks that failed

- `C-BUDGET-RESPECTED` failed 3 times:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 16: “the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - This recurring check has now failed three times. Whatever was changed among those attempts is not what eliminates the over-budget behavior reliably.

- `C-PERTURBATION-REACHED` failed 2 times:
  - Attempts 10 and 11 both reported: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  - In each case, the failing perturbation kind was `held_out_variant`, stopped by `C-BUDGET-RESPECTED`; the `ruleset` kind reached its threshold.
  - This check has now failed twice. Whatever changed between attempts 10 and 11 did not fix the underlying held-out-variant budget failure.

- `C-PER-STEP-COST-CEILING` failed 2 times:
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 16: “per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0”.
  - This check has now failed twice. Whatever changed between those attempts reduced the reported ratio but did not reliably keep it below the ceiling.

No failed check was recorded for attempts 1–9 or 12–15.

4. Ruled-out directions

- Do not repeat the attempt-10 resource profile: a 50.5532-second qualifying point and 4.6619 per-step cost ratio failed the budget, perturbation-reach, and per-step-cost checks and produced reward 0.0000.
- Do not rely on narrowly exceeding the 31.1-second ceiling. Attempt 11 exceeded it by roughly 0.5532 seconds, but that was still enough to fail `C-BUDGET-RESPECTED`, prevent the held-out variant from qualifying, and reduce task pass to 0.
- Do not assume that both perturbations reaching is sufficient if global limits are violated. Attempt 16 reached both perturbations but exceeded both the wall-clock ceiling and per-step-cost ceiling, was invalid, and produced reward 0.0000.
- Do not favor the slower, fully conforming profiles represented by attempts 4, 9, and 12–15 without a structural change. They passed all checks but all were plainly below the 0.6964 best; their rewards topped out at only 0.4779.
- Do not pursue higher per-step cost without demonstrated reward benefit. Attempt 8 had a ratio of 2.0341 but scored below attempts 5–7, attempt 9 had a ratio of 2.0655 and scored 0.3601, and attempts 10 and 16 crossed the hard ceiling and scored 0.0000.
- Repeating an over-budget approach without changing what caused the budget or cost failure is neither useful exploration nor exploitation.

5. Open leads

- Exploit the attempt-6 regime because it already holds the best reward, 0.6964, while passing the primary target, both perturbation kinds, validity, conformance, and all resource checks.
- Preserve substantial safety margins under the hard limits. Attempt 6 qualified at 19.6077 seconds with a 1.5374 per-step cost ratio, well below the 31.1-second and 3.0-ratio ceilings.
- Compare the attempt-6 and attempt-5 regimes if their implementation details are recoverable outside these records. They are the two strongest results at 0.6964 and 0.6687. Attempt 7 had a similar measured runtime and per-step ratio to attempt 6 but fell to 0.6506, so the metrics supplied here do not identify which hidden algorithmic change made attempt 6 better.
- Optimize reward within the already successful moderate-runtime class rather than trading toward the slower 25–33-second class. The measured evidence favors qualifying around 16–20 seconds, although runtime alone does not explain reward.
- Keep the held-out variant explicitly protected: it is the only perturbation kind that ever failed, and both failures were due to its own budget check.
- Call: exploit. Refine the highest-scoring attempt-6 approach while preserving full perturbation coverage and comfortable budget and per-step-cost margins.
