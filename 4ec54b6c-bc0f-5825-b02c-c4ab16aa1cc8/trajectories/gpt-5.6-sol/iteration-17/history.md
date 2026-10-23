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

    All 11 attempts since have scored lower than it.
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
  11 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 17 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 26
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-PER-STEP-COST-CEILING -- per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 3 attempts (10, 11, 16). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 3 attempts (10, 16, 17). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 2 attempts (10, 11). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Worst to best by reward:

- Attempts 10, 16, and 17: reward **0.0000**. All were measured and were worse than an earlier attempt. Each crossed a red line and was invalid.
- Attempt 11: reward **0.3385**, lower than the earlier best.
- Attempt 9: reward **0.3601**, lower than the earlier best.
- Attempt 15: reward **0.4034**, lower than the earlier best.
- Attempt 13: reward **0.4070**, lower than the earlier best.
- Attempt 14: reward **0.4201**, lower than the earlier best.
- Attempt 4: reward **0.4776**, lower than the earlier best.
- Attempt 12: reward **0.4779**, lower than the earlier best.
- Attempt 1: reward **0.5513**, the first measured baseline.
- Attempt 3: reward **0.6043**, lower than the then-best attempt 2.
- Attempt 2: reward **0.6387**, better than attempt 1.
- Attempt 8: reward **0.6481**, lower than the then-best attempt 6.
- Attempt 7: reward **0.6506**, lower than the then-best attempt 6.
- Attempt 5: reward **0.6687**, better than every earlier attempt at that point.
- Attempt 6: reward **0.6964**, the highest reward and the one to beat.

Every submission produced a measurement. The primary target was reached in every attempt. Attempts 1–9 and 12–15 passed the task with full conformance and validity. Attempt 11 remained valid but did not pass because a perturbation missed its threshold within budget. Attempts 10, 16, and 17 were invalid after crossing red-line checks.

Across all perturbation units, held-out variants reached threshold in 15 of 17 measured attempts; the two failures were held-out-variant runs stopped by `C-BUDGET-RESPECTED`. Ruleset runs reached threshold in all 17 attempts. Thus 32 of 34 perturbation units reached their thresholds. All perturbations held in 15 of 17 attempts.

2. Approach classes tried

- **Fully conforming, relatively low-to-moderate-cost runs:** Attempts 1–8 all reached the primary target and both perturbation thresholds, with qualifying budgets from 16.4412 to 28.4730 seconds and per-step cost ratios from 0.9534 to 2.0341. Rewards varied substantially, from 0.4776 to 0.6964. This class contains all of the strongest results, including attempts 5 and 6. Attempt 6 combined reward 0.6964 with a 19.6077-second qualifying budget and a 1.5374 per-step cost ratio.
- **Fully conforming but slower or weaker-reward runs:** Attempts 9 and 12–15 also reached the primary target and both perturbations without failed checks, but rewards were only 0.3601–0.4779. Their qualifying budgets were 24.8389–28.3438 seconds, with per-step cost ratios of 1.4145–2.0655. These records show that merely preserving conformance and allowing more wall-clock time did not improve on attempt 6.
- **Budget-edge runs with a held-out-variant miss:** Attempts 10 and 11 reached the primary target and the ruleset threshold, but the held-out-variant kind failed `C-BUDGET-RESPECTED`; consequently only 1 of 2 perturbations reached its own threshold in each attempt. Attempt 10 was far over budget and over the per-step ceiling, yielding reward 0.0000 and invalidity. Attempt 11 narrowly exceeded the budget, remained valid, and received reward 0.3385, still lower than the earlier best.
- **Red-line per-step-cost runs:** Attempts 16 and 17 reached the primary target and both perturbation thresholds, but violated `C-PER-STEP-COST-CEILING`. Attempt 16 also violated the overall budget. Both were invalid and received reward 0.0000. Passing perturbations does not rescue a submission that crosses these red lines.

The supplied terms do not describe the actual algorithmic or code changes, so the next attempt cannot reconstruct specific model, optimizer, schedule, or implementation choices from these records alone. The reproducible distinction available here is the measured runtime, per-step-cost, conformance, and perturbation behavior.

3. Checks that failed

- `C-BUDGET-RESPECTED` has failed **3 times**, in attempts 10, 11, and 16:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 16: “the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Because this check failed across three attempts with different measured cost profiles, whatever changed between those attempts is not what is causing the finding; the common fixable fact is that each qualifying row exceeded the declared 31.1-second ceiling.

- `C-PERTURBATION-REACHED` has failed **2 times**, in attempts 10 and 11:
  - In both cases, the verifier’s reason was: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  - The failing kind was a held-out variant, stopped by `C-BUDGET-RESPECTED`; the ruleset kind reached its threshold.
  - Because the same check failed in both attempts despite their very different total wall-clock and per-step costs, whatever changed between those attempts is not what is causing the finding. Both still allowed the held-out-variant kind to run beyond its own budget.

- `C-PER-STEP-COST-CEILING` has failed **3 times**, in attempts 10, 16, and 17:
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 16: “per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 17: “per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0”.
  - Because this check failed across three attempts, whatever changed between those attempts is not what is causing the finding; all three retained per-step cost above the explicit 3.0 ceiling.

No failed check appeared in attempts 1–9 or 12–15.

4. Ruled-out directions

- **Per-step cost above 3.0 times the seed anchor:** Ruled out because attempts 10, 16, and 17 all failed `C-PER-STEP-COST-CEILING`, crossed a red line, became invalid, and received reward 0.0000.
- **Qualifying beyond the 31.1-second ceiling:** Ruled out because attempts 10, 11, and 16 failed `C-BUDGET-RESPECTED`. Even the narrow overrun in attempt 11—31.6532 seconds—failed, so there is no evidence that operating near or slightly above the ceiling is acceptable.
- **Trading held-out robustness for primary-target success:** Ruled out because the primary target was already reached in every attempt, while attempts 10 and 11 still failed the task when the held-out-variant kind did not reach its threshold within its own budget.
- **Increasing runtime or per-step expense without demonstrated reward gain:** Ruled out by attempts 9 and 12–15, which remained conforming but scored only 0.3601–0.4779, well below attempt 6’s 0.6964. More qualifying time or a more expensive step did not by itself improve reward.
- **Repeating red-line approaches while retaining the offending cost:** Attempts 10, 16, and 17 repeatedly received reward 0.0000 for explicit ceiling violations. Repeating that class without bringing both wall-clock and per-step cost under their ceilings is neither useful exploration nor exploitation.

5. Open leads

- Use attempt 6’s measured operating region as the target: preserve full conformance, validity, primary-target success, both perturbation thresholds, qualifying budget near 19.6077 seconds, and per-step cost safely below 3.0. Its reward **0.6964** is the one to beat.
- Compare against nearby strong profiles rather than slower conforming profiles: attempt 5 achieved 0.6687 at 19.4243 seconds and a 1.0830 per-step ratio; attempts 7 and 8 achieved 0.6506 and 0.6481 around 19.66–20.27 seconds. The strongest observed reward region is therefore around 19–20 seconds, although the supplied terms do not establish that runtime itself causes the reward.
- Keep substantial safety margins instead of merely touching the ceilings. A qualifying budget below 31.1 is mandatory, and attempt 11 shows that a small overrun still fails. A per-step ratio below 3.0 is also mandatory, and attempt 16 shows that 3.152 is already disqualifying.
- Preserve the ruleset behavior, which succeeded in every measured attempt, while ensuring the held-out-variant kind qualifies inside its own budget. Do not optimize only the primary run.
- Since a fully conforming approach has already reached 0.6964 and later structurally unverified variants did not improve it, the next move should refine the best-scoring operating profile rather than pursue higher-cost designs.

**Exploit:** reproduce and improve the attempt 6 class while preserving its successful conformance and perturbation behavior.
