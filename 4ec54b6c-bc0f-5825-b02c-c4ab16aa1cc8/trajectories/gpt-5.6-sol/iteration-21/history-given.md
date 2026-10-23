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

    All 14 attempts since have scored lower than it.
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
  15 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 19 -- reward 0.1470, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 32
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 31.8888943195343 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 20 -- reward --
      approach: not measured -- the unverified prose below is the only account of it
      measured: nothing. This attempt produced no measurement.
      narrative: no run was graded, so the verifier recorded no check.

    attempt 21 -- reward 0.3488, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 4 attempts (10, 11, 16, 19). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 3 attempts (10, 16, 17). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 3 attempts (10, 11, 19). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

All measured attempts, ranked worst to best by reward:

- Attempts 10, 16, and 17: reward 0.0000. Each was worse than an earlier attempt and invalid after crossing a red line.
- Attempt 19: reward 0.1470. Lower than the earlier best.
- Attempt 11: reward 0.3385. Lower than the earlier best.
- Attempt 21: reward 0.3488. Lower than the earlier best.
- Attempt 9: reward 0.3601. Lower than the earlier best.
- Attempt 15: reward 0.4034. Lower than the earlier best.
- Attempt 13: reward 0.4070. Lower than the earlier best.
- Attempt 18: reward 0.4085. Lower than the earlier best.
- Attempt 14: reward 0.4201. Lower than the earlier best.
- Attempt 4: reward 0.4776. Lower than the earlier best.
- Attempt 12: reward 0.4779. Lower than the earlier best.
- Attempt 1: reward 0.5513, the initial measured baseline.
- Attempt 3: reward 0.6043. Although above attempt 1, it was lower than the then-best attempt 2.
- Attempt 2: reward 0.6387, which improved on attempt 1.
- Attempt 8: reward 0.6481. Lower than the earlier best, which by then was attempt 6.
- Attempt 7: reward 0.6506. Lower than the earlier best, which by then was attempt 6.
- Attempt 5: reward 0.6687, which improved on every earlier attempt at that point.
- Attempt 6: reward 0.6964. This is the highest reward and the one to beat.

Attempt 20 produced no measurement because its measurement status was `harbor_exception`; it must not be ranked as a zero-reward result.

Every measured attempt reached the primary target. Seventeen of 20 measured attempts held both perturbations; the other three failed the held-out variant while the ruleset perturbation still reached its threshold.

2. Approach classes tried

The records do not include source code, hyperparameters, model structure, or descriptions of the changes between attempts, so exact algorithms cannot be reconstructed. The observable approach classes are:

- Fully conforming, perturbation-robust runs: Attempts 1–9, 12–15, 18, and 21 reached the primary target, reached both perturbation thresholds, passed all named checks, stayed below the red lines, and earned rewards from 0.3488 to 0.6964. Attempt 6 is the strongest representative: reward 0.6964, qualifying budget 19.6077 seconds, per-step cost ratio 1.5374, and both perturbation kinds reached.
- Near-budget runs that lost held-out robustness: Attempts 11 and 19 exceeded the 31.1-second ceiling by relatively small amounts, failed the held-out variant on `C-BUDGET-RESPECTED`, and consequently failed `C-PERTURBATION-REACHED`. They earned only 0.3385 and 0.1470, respectively.
- Severe budget-and-cost overrun: Attempt 10 took 50.5532 seconds and had a per-step cost ratio of 4.6619. It failed budget, perturbation reach, and per-step cost checks, producing reward 0.0000.
- Runs whose perturbations reached but whose primary execution crossed red lines: Attempt 16 exceeded both the total budget and per-step cost ceiling; attempt 17 stayed within the total budget but exceeded the per-step cost ceiling badly. Both had reward 0.0000 even though both perturbation kinds reached.
- Infrastructure or execution failure: Attempt 20 ended in `harbor_exception` and produced no measurement.

Perturbation outcomes in aggregate across the 20 measured records:

- `held_out_variant`: reached in 17 of 20 measured attempts. It failed in three attempts, each stopped by `C-BUDGET-RESPECTED`.
- `ruleset`: reached in all 20 measured attempts and was never stopped by a named check.
- Both declared perturbations reached in 17 of 20 measured attempts.
- Across the three attempts where not all perturbations held, exactly one of two perturbations reached: the ruleset reached and the held-out variant did not.

3. Checks that failed

- `C-BUDGET-RESPECTED` failed four times:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 16: “the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 19: “the qualifying row sits at 31.8888943195343 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  This check has now failed four times. Whatever was changed between those attempts is not what is causing the recurring finding: the directly measured issue is that each qualifying row remained above the declared 31.1-second ceiling.

- `C-PERTURBATION-REACHED` failed three times:
  - Attempts 10, 11, and 19 each received the reason: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  In all three cases, the failing kind was `held_out_variant`, stopped by `C-BUDGET-RESPECTED`; the `ruleset` kind reached. This check has now failed three times. Whatever changed between those attempts did not remove the recurring held-out budget failure.

- `C-PER-STEP-COST-CEILING` failed three times:
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 16: “per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 17: “per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0”.
  This check has now failed three times. Whatever changed between these attempts did not reliably constrain per-step cost below 3.0 times the seed anchor.

No named checks failed in attempts 1–9, 12–15, 18, or 21. Attempt 20 produced no measurement, so its empty `failed_checks` list is not evidence that checks passed.

4. Ruled-out directions

- Do not use configurations with per-step cost ratios above 3.0. Ratios of 4.6619, 3.1522, and 8.3821 triggered `C-PER-STEP-COST-CEILING`; all three corresponding attempts received reward 0.0000.
- Do not target the 31.1-second budget with only a narrow timing margin. Qualifying times of 31.6532, 31.8889, and 32.9780 seconds all failed `C-BUDGET-RESPECTED`; two of these still had per-step ratios below 3.0, showing that respecting the per-step ceiling alone does not guarantee budget compliance.
- Do not accept primary-target success as sufficient. Every measured attempt reached the primary target, including all zero-reward attempts and all attempts that failed perturbation or budget checks.
- Do not accept successful perturbations as sufficient when a red line is crossed. Attempts 16 and 17 reached both perturbations but were invalid, failed the task, and earned reward 0.0000 because of budget and/or per-step cost violations.
- Do not repeat the class represented by attempts 10, 16, or 17 without changing the measured cause of failure. Repeating a zero-reward approach while leaving its budget or per-step overrun intact is neither exploration nor exploitation.
- Do not infer that higher reported compute efficiency necessarily means higher reward. Attempt 6 achieved the best reward 0.6964 with compute efficiency 0.5781, while several attempts with compute efficiency 1.0000 earned materially lower rewards.
- Do not infer that lower per-step cost alone produces the best reward. Attempt 6’s ratio was 1.5374 and beat multiple valid attempts with lower ratios. The safe conclusion is only that the ratio must remain below the hard ceiling of 3.0.
- The exact algorithmic changes behind individual attempts cannot be ruled in or out because those changes were not supplied. Only the measured outcome classes above are supportable.

5. Open leads

- Exploit the approach corresponding to attempt 6, the current best at reward 0.6964. Preserve its demonstrated essentials: primary target reached, both perturbation kinds reached, full conformance, qualifying budget around 19.6077 seconds, no red-line crossing, and per-step cost ratio 1.5374.
- Compare any refinement against the other strong valid region represented by attempt 5 at reward 0.6687, attempt 7 at 0.6506, attempt 8 at 0.6481, and attempt 2 at 0.6387. These show that good rewards are attainable while staying comfortably inside the 31.1-second budget and below the 3.0 per-step ceiling.
- Keep substantial safety margins rather than merely satisfying the ceilings nominally. The best attempt was roughly 11.5 seconds below the budget ceiling and about half the per-step ceiling, whereas several later attempts failed near or above those boundaries.
- Preserve ruleset behavior, which reached its threshold in every measured run. Focus robustness work on the held-out variant because it is the only perturbation kind observed to fail, and all three such failures were caused by `C-BUDGET-RESPECTED`.
- If exploring a more expensive refinement, gate or shorten it so both total qualifying time and per-step cost remain safely bounded. The records do not support trading either hard ceiling for target quality because crossing the per-step red line yielded reward 0.0000.
- Treat attempt 20’s `harbor_exception` as an execution failure requiring basic reliability checks before grading; it produced no evidence about model quality.

Call: **exploit**. Attempt 6 already scored best and passed every check, so the next direction should refine or faithfully recover that successful class rather than adopt a structurally different, unproven approach.
