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

    All two attempts since have scored lower than it.
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
  4 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 8 -- reward 0.6481, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Worst to best by reward:

- Attempt 4: reward 0.4776. This was lower than the earlier best. It reached the primary target, remained valid and conformant, held both perturbation kinds, and had qualifying budget/wall clock 28.4730 seconds.
- Attempt 1: reward 0.5513. This was the first measured attempt. It reached the primary target and held both perturbation kinds.
- Attempt 3: reward 0.6043. This was lower than the earlier best established by attempt 2.
- Attempt 2: reward 0.6387. This improved on every earlier attempt.
- Attempt 8: reward 0.6481. This was lower than the earlier best established by attempt 6; it was also lower than attempt 7.
- Attempt 7: reward 0.6506. This was lower than the earlier best established by attempt 6.
- Attempt 5: reward 0.6687. This improved on every earlier attempt.
- Attempt 6: reward 0.6964. This is the highest reward and is the one to beat.

All eight attempts were measured, valid, fully conformant, passed the task, reached the primary target, avoided the red line, and held all declared perturbations.

2. Approach classes tried

The records contain no implementation or algorithm descriptions, so the exact training approaches cannot be reconstructed. They can only be grouped by observed operating regime:

- Efficiency-favoring regime: attempts 1 and 4 had compute efficiency near 1.0 and per-step cost ratios below 1.0. Their rewards were 0.5513 and 0.4776, respectively.
- Intermediate regime: attempts 2, 3, and 5 had compute efficiency from 0.8281 to 0.8764 and per-step cost ratios from 1.0323 to 1.1242. Their rewards were 0.6387, 0.6043, and 0.6687.
- Higher-cost regime: attempts 6, 7, and 8 had compute efficiency from 0.4238 to 0.6084 and per-step cost ratios from 1.5308 to 2.0341. Attempt 6 produced the overall best reward, 0.6964, while attempts 7 and 8 fell to 0.6506 and 0.6481.

These are empirical metric groupings, not claims about unreported algorithm structure.

3. Checks that failed

No named check failed in any attempt, so there is no verifier failure reason to fix and no repeated failed check.

Perturbation outcomes were uniformly successful:

- `held_out_variant`: reached its threshold in all 8 measured attempts; none was stopped by a check.
- `ruleset`: reached its threshold in all 8 measured attempts; none was stopped by a check.
- Aggregate: all 16 perturbation units reached their thresholds, with 0 failed units and 0 associated failed checks.

4. Ruled-out directions

- Selecting solely for higher compute efficiency is ruled out as a sufficient strategy. Attempt 4 had compute efficiency 0.9723 but the lowest reward, 0.4776, whereas attempt 6 had compute efficiency 0.5781 and the highest reward, 0.6964.
- Selecting solely for a lower per-step cost ratio is ruled out as sufficient. Attempt 4 had the lowest ratio, 0.9534, but the lowest reward; attempt 6 had a ratio of 1.5374 and the highest reward.
- Selecting solely for the shortest wall clock or qualifying budget is ruled out as sufficient. Attempt 2 was fastest at 16.4412 seconds but scored 0.6387, below attempts 5 and 6.
- Escalating per-step cost beyond attempt 6’s regime is not supported. Attempt 8 increased the ratio to 2.0341 but fell to reward 0.6481, lower than the earlier best 0.6964.
- Repeating the broad regime of attempt 6 without preserving what generated its advantage is not enough: attempts 7 and 8 occupied similarly high-cost, lower-efficiency territory but both had lower rewards. The supplied terms do not identify which unreported implementation change caused that loss.

5. Open leads

Use attempt 6 as the baseline because it has the best measured reward, 0.6964, while preserving the properties that already hold universally: primary-target success, full validity and conformance, no red-line crossing, and successful `held_out_variant` and `ruleset` perturbations.

Investigate controlled changes around attempt 6 rather than optimizing any single efficiency metric. In particular, test whether its reward can be retained while modestly reducing its 1.5374 per-step cost ratio or improving its 0.5781 compute efficiency. Avoid moving as far as attempt 8’s 2.0341 cost ratio, since that produced a lower reward. Because implementation details were not supplied, change one algorithmic factor at a time and record it explicitly so the successful element of attempt 6 can be identified.

Call: exploit. Improve the highest-scoring attempt-6 approach rather than switching to a structurally unrelated idea.
