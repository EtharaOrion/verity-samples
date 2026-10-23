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

    All six attempts since have scored lower than it.
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

    attempt 10 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 51
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget
        C-PER-STEP-COST-CEILING -- per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0

    attempt 11 -- reward 0.3385, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 32
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 2 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 12 -- reward 0.4779, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (10, 11). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING failed on attempt 10.
    C-PERTURBATION-REACHED has failed on 2 attempts (10, 11). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Worst to best by reward:

- Attempt 10: reward 0.0000. This was lower than an earlier attempt. The primary target was reached, but the submission was invalid, crossed the red line, exceeded the budget and per-step-cost ceilings, and held only one of two perturbations.
- Attempt 11: reward 0.3385. This was lower than an earlier attempt. It remained valid and reached the primary target, but failed the held-out variant by slightly exceeding the declared wall-clock ceiling; only one of two perturbations held.
- Attempt 9: reward 0.3601. This was lower than an earlier attempt despite full conformance and both perturbations holding. Qualifying budget was 28.3438 seconds, wall clock was 31.3334 seconds, and per-step cost ratio was 2.0655.
- Attempt 4: reward 0.4776. This was lower than an earlier attempt despite full conformance and both perturbations holding. Qualifying budget and wall clock were 28.4730 seconds.
- Attempt 12: reward 0.4779. This was lower than an earlier attempt despite full conformance and both perturbations holding. Qualifying budget and wall clock were 27.7851 seconds, with per-step cost ratio 1.5528.
- Attempt 1: reward 0.5513. This was the first measured attempt. It reached the primary target, passed both perturbations, and had full validity and conformance.
- Attempt 3: reward 0.6043. This was lower than the then-best earlier attempt. It nevertheless reached the primary target and passed both perturbations with full validity and conformance.
- Attempt 2: reward 0.6387. This improved on every earlier attempt at that point. It reached the primary target and passed both perturbations with full validity and conformance.
- Attempt 8: reward 0.6481. This was lower than the best earlier attempt at that point. It reached the primary target and passed both perturbations, although its per-step cost ratio was 2.0341.
- Attempt 7: reward 0.6506. This was lower than the best earlier attempt at that point. It reached the primary target and passed both perturbations with full validity and conformance.
- Attempt 5: reward 0.6687. This improved on every earlier attempt at that point. It reached the primary target and passed both perturbations with full validity and conformance.
- Attempt 6: reward 0.6964. This is the highest reward and the one to beat. It reached the primary target, passed both perturbations, retained full validity and conformance, used a qualifying budget and wall clock of 19.6077 seconds, and had a per-step cost ratio of 1.5374.

Across all measured attempts, the held-out-variant perturbation reached its threshold in 10 of 12 runs and failed in 2 of 12, both times on `C-BUDGET-RESPECTED`. The ruleset perturbation reached its threshold in all 12 of 12 runs. Both perturbation kinds held together in 10 of 12 attempts.

2. Approach classes tried

The records do not describe the algorithms or hyperparameter changes, so no specific implementation can be reconstructed. The observable approach classes are:

- Fully conforming, moderate-budget approaches: Attempts 1–8 and 12 all reached the primary target and both perturbation thresholds with validity, rule conformance, and conformance fraction equal to 1.0. Their rewards ranged from 0.4776 to 0.6964. Within this class, attempts 5 and 6 were the strongest, and attempt 6 is the current best.
- Fully conforming but slower/high-cost approach: Attempt 9 still passed the primary target and both perturbations, but used 31.3334 seconds of wall clock and had a per-step cost ratio of 2.0655. Its reward fell to 0.3601.
- Budget-breaking held-out-variant approaches: Attempts 10 and 11 reached the primary target and passed the ruleset perturbation, but the held-out variant did not reach its threshold within budget. Attempt 10 was a severe overrun with excessive per-step cost; attempt 11 reduced the overrun substantially but still missed the same budget and perturbation checks.
- Best observed scoring regime: Attempt 6 combined complete conformance and perturbation success with reward 0.6964. Its exact algorithm is not supplied, but its measured operating point—19.6077-second qualifying budget, 1.5374 per-step cost ratio, and all thresholds reached—is the strongest basis for refinement.

3. Checks that failed

- `C-BUDGET-RESPECTED` failed twice:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  
  This check has now failed 2 times. Whatever was changed between attempts 10 and 11 is not what is causing the remaining failure: the held-out-variant qualifying row was still above the same declared ceiling, although the excess was much smaller in attempt 11.

- `C-PERTURBATION-REACHED` failed twice:
  - Attempt 10: “1 of 2 declared perturbations reached their own threshold inside their own budget”
  - Attempt 11: “1 of 2 declared perturbations reached their own threshold inside their own budget”
  
  This check has now failed 2 times. Whatever was changed between attempts 10 and 11 is not what is causing it: in both cases the held-out-variant run failed on `C-BUDGET-RESPECTED`, while the ruleset run reached its threshold.

- `C-PER-STEP-COST-CEILING` failed once:
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”

No named checks failed in attempts 1–9 or 12.

4. Ruled-out directions

- Do not repeat the attempt-10 operating regime. Its 50.5532-second qualifying row exceeded the 31.1-second ceiling, its per-step cost ratio of 4.6619 exceeded the 3.0 ceiling, the held-out variant failed, validity was 0.0, and reward was 0.0000.
- Do not accept a merely near-ceiling version of the attempt-11 regime. Reducing the qualifying row to 31.6532 seconds and the per-step cost ratio to 1.5815 removed the per-step-cost failure and retained validity, but it still exceeded the 31.1-second budget, still failed the held-out variant, and produced reward 0.3385.
- Do not trade threshold reliability for runtime that sits at or above the budget boundary. The held-out variant was the only perturbation kind that failed, and both failures were specifically stopped by `C-BUDGET-RESPECTED`.
- Do not assume full conformance alone guarantees a competitive reward. Attempts 4, 9, and 12 passed the primary target and both perturbations with full conformance but scored only 0.4776, 0.3601, and 0.4779 respectively.
- No particular algorithmic family can be ruled out from these terms because implementation details were not supplied. Only the measured operating regimes above are ruled out.

5. Open leads

- Exploit attempt 6, the current best at reward 0.6964. Preserve primary-target success, validity, full conformance, and both perturbation successes while making controlled changes around its measured operating point.
- Use attempts 5 and 6 as the strongest successful region: both had qualifying budgets near 19.5–19.6 seconds and rewards of 0.6687 and 0.6964. Attempt 6 is preferable because it is the one to beat.
- Keep substantial margin below the 31.1-second ceiling, especially for the held-out variant. The successful best attempt qualified at 19.6077 seconds, whereas attempts 10 and 11 failed when their qualifying rows exceeded 31.1 seconds.
- Treat per-step cost as a hard safety constraint rather than assuming that lowering it alone raises reward. Attempt 10 proves that exceeding 3.0 is unacceptable, but the successful rewards do not vary monotonically with per-step cost or compute efficiency.
- Preserve ruleset robustness, which held in all 12 measured attempts, while specifically protecting held-out-variant runtime.
- Make one controlled refinement at a time and compare reward directly against 0.6964; the supplied measurements do not identify which unreported code changes produced the differences.

Call: exploit. Refine the fully conforming attempt-6-style regime rather than exploring a structurally different approach, because it already has the highest measured reward and no failed checks.
