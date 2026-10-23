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

    All 12 attempts since have scored lower than it.
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
  12 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 16 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 33
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PER-STEP-COST-CEILING -- per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0

    attempt 17 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 26
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-PER-STEP-COST-CEILING -- per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0

    attempt 18 -- reward 0.4085, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 30
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 3 attempts (10, 11, 16). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 3 attempts (10, 16, 17). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 2 attempts (10, 11). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Every submission produced a measurement. Ranked worst to best by reward:

- Attempt 10: reward 0.0000. Lower than the earlier best; invalid and task failed after crossing the red line.
- Attempt 16: reward 0.0000. Lower than the earlier best; invalid and task failed after crossing the red line.
- Attempt 17: reward 0.0000. Lower than the earlier best; invalid and task failed after crossing the red line.
- Attempt 11: reward 0.3385. Lower than the earlier best; valid, but task failed and only half of declared perturbations conformed.
- Attempt 9: reward 0.3601. Lower than the earlier best despite full conformance and both perturbations reaching.
- Attempt 15: reward 0.4034. Lower than the earlier best despite full conformance and both perturbations reaching.
- Attempt 13: reward 0.4070. Lower than the earlier best despite full conformance and both perturbations reaching.
- Attempt 18: reward 0.4085. Lower than the earlier best despite full conformance and both perturbations reaching.
- Attempt 14: reward 0.4201. Lower than the earlier best despite full conformance and both perturbations reaching.
- Attempt 4: reward 0.4776. Lower than the earlier best despite full conformance and both perturbations reaching.
- Attempt 12: reward 0.4779. Lower than the earlier best despite full conformance and both perturbations reaching.
- Attempt 1: reward 0.5513. First measured baseline; fully conforming.
- Attempt 3: reward 0.6043. Lower than attempt 2’s earlier best.
- Attempt 2: reward 0.6387. Improved over attempt 1 and established a new best at that point.
- Attempt 8: reward 0.6481. Lower than attempt 6’s earlier best.
- Attempt 7: reward 0.6506. Lower than attempt 6’s earlier best.
- Attempt 5: reward 0.6687. Improved over every earlier attempt and established a new best at that point.
- Attempt 6: reward 0.6964. This is the highest reward and the one to beat.

Attempt 6’s measured profile was: primary target reached, both perturbation kinds reached, full rule conformance, qualifying budget and wall clock 19.6077 seconds, compute efficiency 0.5781, and per-step cost ratio 1.5374.

Across all perturbation units, held_out_variant runs reached threshold in 16 of 18 submissions and failed in 2 of 18, both stopped by C-BUDGET-RESPECTED. Ruleset runs reached threshold in all 18 of 18 submissions. Both kinds reached in aggregate for 16 submissions; attempts 10 and 11 were the exceptions.

2. Approach classes tried

- Fully conforming, relatively low-cost configurations: Attempts 1–5 used per-step cost ratios from 0.9534 to 1.1242 and all reached the primary target and both perturbation thresholds. Their rewards varied from 0.4776 to 0.6687. Attempt 5 was strongest in this class at 0.6687, with a 19.4243-second qualifying budget and per-step cost ratio 1.0830.
- Fully conforming, moderately higher-cost configurations around the current best: Attempts 6 and 7 had nearly identical wall-clock times near 19.6 seconds and per-step cost ratios near 1.53. Attempt 6 scored 0.6964, while attempt 7 was lower at 0.6506. Attempt 8 increased per-step cost to 2.0341 and scored only 0.6481. Thus the measured sweet spot is closest to attempt 6 rather than further cost escalation.
- Slower fully conforming configurations: Attempts 9 and 12–15 and 18 generally had qualifying budgets from 24.8389 to 30.0896 seconds and rewards from 0.3601 to 0.4779. All held both perturbations, but none approached the best. Attempt 9 additionally had wall clock 31.3334 seconds and reward 0.3601.
- Budget- or cost-violating configurations: Attempts 10, 11, 16, and 17 explored substantially slower or more expensive behavior. Attempt 10 took 50.5532 seconds with per-step cost ratio 4.6619 and scored 0.0000. Attempt 11 reduced cost to 1.5815 but still qualified at 31.6532 seconds, missed the held_out_variant budget, and scored 0.3385. Attempt 16 qualified at 32.9780 seconds with per-step cost ratio 3.1522 and scored 0.0000. Attempt 17 stayed within the overall time ceiling at 26.0670 seconds but had per-step cost ratio 8.3821 and scored 0.0000.
- The records contain no implementation or hyperparameter descriptions, so the exact algorithms cannot be reconstructed. The actionable distinctions available are timing, per-step cost, conformance, perturbation reach, and reward.

3. Checks that failed

- C-BUDGET-RESPECTED failed 3 times:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 16: “the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  This recurring failure across three changed submissions means whatever differed between those submissions was not sufficient to prevent the qualifying row from exceeding the fixed 31.1 ceiling.

- C-PERTURBATION-REACHED failed 2 times:
  - Attempts 10 and 11 each reported: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  In both cases, the failing kind was held_out_variant, stopped by C-BUDGET-RESPECTED; the ruleset kind reached its threshold. Whatever changed between attempts 10 and 11 was not what eliminated this issue, because the same check still failed for the same kind of run.

- C-PER-STEP-COST-CEILING failed 3 times:
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 16: “per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 17: “per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0”.
  This check has now failed three times despite changes among those submissions; those changes did not address the condition that per-step cost must remain at or below 3.0 times the seed anchor.

No named checks failed in attempts 1–9, 12–15, or 18.

4. Ruled-out directions

- Do not repeat configurations with per-step cost ratio above 3.0. Attempts 10, 16, and 17 all failed C-PER-STEP-COST-CEILING, became invalid, failed the task, and received reward 0.0000.
- Do not allow the qualifying row to exceed 31.1 seconds. Attempts 10, 11, and 16 failed C-BUDGET-RESPECTED. Attempt 11 shows that even a small overrun to 31.6532 seconds is enough to fail the check.
- Do not trade held_out_variant robustness for primary-target attainment. Attempts 10 and 11 reached the primary target and ruleset threshold but missed the held_out_variant threshold within its budget, triggering C-PERTURBATION-REACHED.
- Do not pursue slower fully conforming profiles merely because they preserve conformance. Attempts 12–15 and 18 all passed every check but scored only 0.4034–0.4779, well below attempt 6’s 0.6964. Attempt 9 likewise passed all checks but scored 0.3601.
- Do not assume higher per-step cost improves reward. Moving from the attempt-6 region of 1.5374 to attempt 8’s 2.0341 lowered reward from 0.6964 to 0.6481; ratios above 3.0 caused hard failures in attempts 10, 16, and 17.
- Do not simply repeat a zero-reward high-cost or over-budget approach without changing the condition responsible for the zero. That would be neither useful exploration nor exploitation.

5. Open leads

- Reconstruct and refine the attempt-6-style operating point: approximately 19.6 seconds qualifying time, per-step cost ratio around 1.54, full conformance, and successful held_out_variant and ruleset thresholds. It is the strongest measured region.
- Compare the attempt-6 and attempt-7 profiles closely. Their qualifying times and per-step cost ratios were nearly the same, yet rewards differed by 0.0458. Since implementation details are absent, preserve attempt 6’s exact algorithmic choices if recoverable rather than treating attempt 7 as equivalent.
- Test conservative local changes around attempt 6 rather than raising cost substantially. Keep a clear safety margin below both hard limits: per-step cost ratio below 3.0 and qualifying wall-clock time below 31.1 seconds.
- Consider whether attempt 5’s lower-cost profile can be combined with the beneficial feature of attempt 6: attempt 5 scored 0.6687 at per-step cost ratio 1.0830, while attempt 6 scored 0.6964 at 1.5374. Both completed in roughly 19.5 seconds and held every perturbation, making them the most promising measured neighborhoods.
- Preserve ruleset robustness, which succeeded in every measured submission, and ensure held_out_variant remains within its own budget, since that was the only perturbation kind ever observed to miss threshold.

Call: exploit. Improve the already successful attempt-6 approach or make a tightly controlled hybrid with attempt 5; the scored approaches have not exhausted local refinement, while structurally more expensive directions have performed worse or failed hard checks.
