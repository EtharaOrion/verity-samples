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

    All four attempts since have scored lower than it.
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

    attempt 9 -- reward 0.3601, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
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

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 10.
    C-PER-STEP-COST-CEILING failed on attempt 10.
    C-PERTURBATION-REACHED failed on attempt 10.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

- Attempt 10: reward 0.0000. It was measured, but was worse than an earlier attempt. The primary target was reached, while validity and task pass failed; only one of two perturbation kinds reached threshold.
- Attempt 9: reward 0.3601. This was lower than the earlier best.
- Attempt 4: reward 0.4776. This was lower than the earlier best.
- Attempt 1: reward 0.5513. This was the first measured attempt.
- Attempt 3: reward 0.6043. This was lower than the earlier best established by attempt 2.
- Attempt 2: reward 0.6387. This improved over attempt 1.
- Attempt 8: reward 0.6481. This was lower than the earlier best established by attempt 6.
- Attempt 7: reward 0.6506. This was lower than the earlier best established by attempt 6.
- Attempt 5: reward 0.6687. This improved over every earlier attempt.
- Attempt 6: reward 0.6964. This is the highest reward and is the one to beat.

Attempts 1–9 all reached the primary target, remained valid and conformant, passed the task, avoided the red line, and held both declared perturbations. Attempt 10 reached the primary target but crossed the red line and failed validity, task pass, and aggregate perturbation holding.

Across all attempts and perturbation kinds, 19 of 20 perturbation units reached threshold. Held-out-variant runs reached threshold in 9 of 10 records; the failing held-out-variant kind was stopped by `C-BUDGET-RESPECTED`. Ruleset runs reached threshold in all 10 records. Both kinds held together in 9 of 10 attempts.

2. Approach classes tried

- Fully conformant, moderate-runtime configurations: attempts 1–8 all reached every target and perturbation without failed checks. Within this broad class, rewards ranged from 0.4776 to 0.6964. The strongest observed profile was attempt 6: reward 0.6964, qualifying budget and wall clock 19.6077 seconds, compute efficiency 0.5781, and per-step cost ratio 1.5374.
- Fully conformant but slower configuration: attempt 9 still passed all targets and checks, but its qualifying budget was 28.3438 seconds, wall clock was 31.3334 seconds, and per-step cost ratio was 2.0655. Its reward fell to 0.3601, plainly below the earlier best.
- Over-budget, excessive-per-step-cost configuration: attempt 10 required 50.5532 seconds at the qualifying row and had a per-step cost ratio of 4.6619. Although the primary target and ruleset perturbation reached threshold, the held-out-variant kind did not, resulting in reward 0.0000.

The measured terms do not describe the underlying algorithms, model changes, schedules, or hyperparameters, so the exact implementation differences between attempts cannot be reconstructed. Only their measured performance profiles can be carried forward reliably.

3. Checks that failed

Only attempt 10 had named failed checks:

- `C-BUDGET-RESPECTED`: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”
- `C-PERTURBATION-REACHED`: “1 of 2 declared perturbations reached their own threshold inside their own budget”
- `C-PER-STEP-COST-CEILING`: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”

Each named check has failed once. For perturbations specifically, the held-out-variant kind failed `C-BUDGET-RESPECTED`, while the ruleset kind reached threshold without a failed check.

4. Ruled-out directions

- Do not repeat attempt 10’s high-cost profile without directly reducing both elapsed qualifying time and per-step cost. It exceeded the 31.1-second budget at 50.5532 seconds, exceeded the per-step ceiling with a ratio of 4.6619, and failed the held-out-variant threshold.
- Do not treat successful conformance alone as sufficient. Attempts 1–9 all passed every check and perturbation, yet rewards varied substantially from 0.3601 to 0.6964.
- The measured configurations behind attempts 3, 4, 7, 8, and 9 should not be reused unchanged: each produced a reward lower than an earlier best. Attempt 9 is especially unattractive because it combined relatively high wall time and per-step cost with the lowest nonzero reward.
- Lower per-step cost by itself is not an established route to higher reward. Attempt 4 had a low per-step cost ratio of 0.9534 and compute efficiency of 0.9723 but scored only 0.4776, whereas attempt 6 scored 0.6964 with a per-step cost ratio of 1.5374 and compute efficiency of 0.5781.
- Higher reported compute efficiency alone is likewise not an established route to higher reward. Attempts 1 and 9 reported compute efficiency 1.0000 but scored 0.5513 and 0.3601, both below attempt 6.

5. Open leads

- Exploit attempt 6’s configuration, which holds the best reward of 0.6964, rather than making a structurally unrelated change.
- Preserve the properties shared by attempts 1–9: primary-target success, full rule conformance, validity, task pass, no red-line crossing, and successful held-out-variant and ruleset perturbations.
- Make a controlled refinement around attempt 6’s measured operating region: approximately 19.6 seconds qualifying/wall-clock time and a per-step cost ratio near 1.54. Avoid drifting toward attempt 10’s budget and cost violations.
- Use attempt 5 as the secondary reference point: reward 0.6687 at 19.4243 seconds with per-step cost ratio 1.0830 and compute efficiency 0.8764. Comparing the actual implementation differences between attempts 5 and 6, if available outside these records, is the clearest empirical route to identifying which change raised reward.
- Optimize reward directly while treating conformance as a hard constraint; the records show that compute efficiency and per-step cost ratio do not individually rank the successful attempts.

Exploit: refine the attempt 6 approach while preserving all checks and both perturbation thresholds.
