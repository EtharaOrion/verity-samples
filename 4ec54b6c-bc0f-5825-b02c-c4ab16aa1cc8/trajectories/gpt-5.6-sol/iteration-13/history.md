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

    All seven attempts since have scored lower than it.
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
  7 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 13 -- reward 0.4070, worse than an earlier attempt
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

Graded attempts, ordered from worst to best by reward:

- Attempt 10: reward **0.0000**. This was measured, but validity was 0.0, task_pass was 0.0, the red line was crossed, and only one of two perturbations reached its threshold. It was worse than the earlier best.
- Attempt 11: reward **0.3385**. Validity held, but task_pass was 0.0 because only one of two perturbations reached within budget. This was lower than the earlier best.
- Attempt 9: reward **0.3601**. All checks and perturbations held, but this was lower than the earlier best.
- Attempt 13: reward **0.4070**. All checks and perturbations held, but this was lower than the earlier best.
- Attempt 4: reward **0.4776**. All checks and perturbations held, but this was lower than an earlier result.
- Attempt 12: reward **0.4779**. All checks and perturbations held, but this was lower than the earlier best.
- Attempt 1: reward **0.5513**. This was the first measured baseline; all checks and perturbations held.
- Attempt 3: reward **0.6043**. All checks and perturbations held, but this was lower than attempt 2.
- Attempt 2: reward **0.6387**. This improved over attempt 1, with all checks and perturbations holding.
- Attempt 8: reward **0.6481**. All checks and perturbations held, but this was lower than the earlier best established by attempt 6.
- Attempt 7: reward **0.6506**. All checks and perturbations held, but this was lower than attempt 6.
- Attempt 5: reward **0.6687**. This improved over every earlier attempt, with all checks and perturbations holding.
- Attempt 6: reward **0.6964**. This is the highest reward and is the one to beat. It reached the primary target and both perturbation thresholds, with validity, rule conformance, and task_pass all equal to 1.0.

Attempts 3, 4, 7, 8, and 9 were explicitly lower than an earlier result. Attempts 10–13 also failed to recover the best reward from attempt 6, even where full conformance was restored.

2. Approach classes tried

- **Fully conformant, moderate-cost scoring approaches:** Attempts 1–5 all reached the primary target and both perturbation thresholds without failed checks. Rewards ranged from 0.4776 to 0.6687. Attempts 2 and 5 set new best rewards, while attempts 3 and 4 were regressions.
- **Higher per-step-cost approaches that still remained conformant:** Attempts 6–9 all held every perturbation and passed all checks. Attempt 6 achieved the best reward, 0.6964, at a per-step cost ratio of 1.5374 and qualifying budget of 19.6077 seconds. Attempts 7 and 8 used similarly high or higher per-step cost but scored less, while attempt 9 combined a 2.0655 cost ratio with 31.3334 seconds of wall-clock time and fell sharply to 0.3601.
- **Over-budget and perturbation-failing approaches:** Attempts 10 and 11 both missed the held-out-variant threshold because of `C-BUDGET-RESPECTED`, while the ruleset perturbation continued to reach its threshold. Attempt 10 additionally exceeded the per-step cost ceiling and became invalid. Attempt 11 reduced the per-step cost ratio from 4.6619 to 1.5815 and avoided the red line, but still crossed the 31.1-second declared ceiling and did not pass the task.
- **Conformance-recovery approaches after the budget failures:** Attempts 12 and 13 restored full validity, task passage, and both perturbations. However, their rewards were only 0.4779 and 0.4070, both plainly below attempt 6. Attempt 13 was also lower than attempt 12 despite having a higher per-step cost ratio.

The records do not describe the underlying algorithmic or code changes, so the approach classes can only be reconstructed from their measured cost, budget, conformance, perturbation, and reward behavior.

3. Checks that failed

- `C-BUDGET-RESPECTED` failed **twice**:
  - Attempt 10 reason: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11 reason: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Because this check failed in both attempts, whatever changed between attempts 10 and 11 is not what is causing the persistent failure. The changes substantially reduced elapsed time and per-step cost, but did not eliminate the underlying budget overrun.
- `C-PERTURBATION-REACHED` failed **twice**:
  - Attempt 10 reason: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  - Attempt 11 reason: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  - This persisted across both attempts, so whatever changed between them is not what is causing the failure. In both records, the held-out-variant kind was stopped by `C-BUDGET-RESPECTED`, while the ruleset kind reached its threshold.
- `C-PER-STEP-COST-CEILING` failed **once**, on attempt 10:
  - Reason: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 11 reduced the ratio to 1.5815, so this particular failure did not persist.

Perturbation outcomes in aggregate:

- **held_out_variant:** reached in 11 of 13 measured attempts and failed in 2 of 13. Both failures were stopped by `C-BUDGET-RESPECTED`.
- **ruleset:** reached in all 13 of 13 measured attempts, with no failed checks.
- **All perturbation units combined:** 24 of 26 reached their thresholds. The only two failures were held-out-variant runs stopped by `C-BUDGET-RESPECTED`.
- Full perturbation holding occurred in 11 of 13 attempts. Attempts 10 and 11 each had only one of two declared perturbations reach.

4. Ruled-out directions

- **The attempt-10 high-cost configuration should not be repeated as-is.** Its per-step cost ratio was 4.6619, above the 3.0 ceiling; its qualifying row occurred at 50.5532 seconds against a 31.1-second ceiling; it crossed the red line, became invalid, missed the held-out-variant threshold, and received reward 0.0000.
- **Merely reducing attempt 10’s cost to the attempt-11 regime is insufficient.** Attempt 11 brought the per-step cost ratio down to 1.5815 and wall-clock time down to 31.6532 seconds, but that remained above the 31.1-second ceiling. The same held-out-variant and perturbation-reach failures remained, and reward was only 0.3385.
- **Operating just above the declared budget boundary is ruled out.** Attempt 11 exceeded the ceiling by roughly 0.5532 seconds and consequently failed both `C-BUDGET-RESPECTED` and `C-PERTURBATION-REACHED`. A robust approach needs margin below the ceiling, not a qualifying point near or above it.
- **Increasing per-step cost beyond the attempt-6 neighborhood without a reward gain is not supported.** Attempt 8 had a ratio of 2.0341 and scored 0.6481; attempt 9 had a ratio of 2.0655 and scored 0.3601. Both were lower than attempt 6’s 0.6964 at a ratio of 1.5374.
- **The attempt-12/13 conformance-recovery family should not be continued unchanged.** It successfully restored all checks and perturbations, but rewards of 0.4779 and 0.4070 remained far below the best. Attempt 13 increased the per-step cost ratio from 1.5528 to 1.7019 while lowering reward.
- **Repeating the attempt-7 or attempt-8 variants unchanged is not justified.** Both remained fully conformant, but rewards of 0.6506 and 0.6481 were lower than attempt 6 despite comparable or greater per-step cost.

5. Open leads

- **Exploit attempt 6**, the current best at reward 0.6964. Preserve the properties that held: primary target reached, both perturbation kinds reached, no failed checks, qualifying budget 19.6077 seconds, and no red-line crossing.
- Use attempt 5 as a secondary stable reference. It scored 0.6687 with a lower per-step cost ratio of 1.0830 and the same complete conformance. This suggests a useful comparison point when refining attempt 6’s higher-cost configuration.
- Seek improvements around the attempt-6 regime rather than increasing cost indiscriminately. Attempts 7 and 8 show that comparable or greater cost does not automatically improve reward.
- Maintain substantial budget margin. The best attempt qualified around 19.6 seconds, whereas attempts near or above 31.1 seconds either scored poorly or failed the held-out variant.
- Preserve the consistently successful ruleset behavior while specifically guarding held-out-variant completion. Every ruleset perturbation reached; the only perturbation weakness observed was the held-out-variant kind under budget overruns.
- Any refinement should retain per-step cost safely below the 3.0 ceiling and avoid the attempt-10 failure mode. Full conformance alone is not enough, as attempts 12 and 13 demonstrate; the refinement must also improve reward over 0.6964.

**Call: exploit.** Attempt 6 already provides a fully conformant, perturbation-robust best-scoring approach, so the next move should refine that regime rather than explore a structurally different family.
