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

    All eight attempts since have scored lower than it.
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
  8 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 14 -- reward 0.4201, worse than an earlier attempt
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

Every graded attempt, ordered from worst to best reward:

- Attempt 10: reward 0.0000. It was measured, but task_pass and validity were both 0.0; not all perturbations held, and three checks failed. This was lower than the earlier best.
- Attempt 11: reward 0.3385. It was measured and valid, but task_pass was 0.0 because not all perturbations held. This was lower than the earlier best.
- Attempt 9: reward 0.3601. Fully conforming and all targets reached, but this was lower than the earlier best.
- Attempt 13: reward 0.4070. Fully conforming and all targets reached, but this was lower than the earlier best.
- Attempt 14: reward 0.4201. Fully conforming and all targets reached, but this was lower than the earlier best.
- Attempt 4: reward 0.4776. Fully conforming and all targets reached, but this was lower than the earlier best.
- Attempt 12: reward 0.4779. Fully conforming and all targets reached, but this was lower than the earlier best.
- Attempt 1: reward 0.5513. Fully conforming and all targets reached; this was the first measured attempt.
- Attempt 3: reward 0.6043. Fully conforming and all targets reached, but this was lower than attempt 2.
- Attempt 2: reward 0.6387. Fully conforming and all targets reached; it improved on attempt 1.
- Attempt 8: reward 0.6481. Fully conforming and all targets reached, but this was lower than the earlier best held by attempt 6.
- Attempt 7: reward 0.6506. Fully conforming and all targets reached, but this was lower than attempt 6.
- Attempt 5: reward 0.6687. Fully conforming and all targets reached; it improved on every earlier attempt.
- Attempt 6: reward 0.6964. Fully conforming, valid, task-passing, and successful on the primary target and both perturbation kinds. Attempt 6 has the highest reward and is the one to beat.

Across all attempts, 26 of 28 perturbation units reached their thresholds. By kind, all 14 ruleset units reached their thresholds. Twelve of 14 held_out_variant units reached; the two failures were each stopped by C-BUDGET-RESPECTED. No anonymous perturbation run can be identified as the same run across records.

2. Approach classes tried

- Efficient, fully conforming scoring regime: attempts 1–8 all reached the primary target and both perturbation thresholds with validity, task_pass, conformance_fraction, and rule_conformance equal to 1.0. Rewards ranged from 0.4776 to 0.6964. This class contains all four successive bests: attempt 1 at 0.5513, attempt 2 at 0.6387, attempt 5 at 0.6687, and attempt 6 at 0.6964. Attempts 3, 4, 7, and 8 were regressions relative to an earlier best, so changes within this broad regime did not consistently improve reward.
- Higher-cost but still conforming regime: attempts 9 and 12–14 reached every target and passed every check, but rewarded only 0.3601–0.4779. Their per_step_cost_ratio values were 1.5528–2.0655, and their qualifying budgets were 27.7851–28.3438 seconds. These outcomes were all substantially below attempt 6.
- Budget-edge or budget-breaching regime: attempts 10 and 11 reached the primary target and the ruleset perturbation but missed the held_out_variant threshold within its budget. Attempt 10 qualified at 50.5532 seconds against a ceiling of 31.1 and also had per_step_cost_ratio 4.6619, producing reward 0.0000 and invalidity. Attempt 11 reduced the qualifying time to 31.6532 seconds and per_step_cost_ratio to 1.5815, restoring validity and reward 0.3385, but it remained above the same 31.1 ceiling and still failed the held-out perturbation.
- The supplied measurements do not describe the actual algorithmic or code changes, so no more specific optimizer, architecture, schedule, or implementation class can be reconstructed without inventing unsupported details.

3. Checks that failed

- C-BUDGET-RESPECTED failed twice:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  Whatever changed between attempts 10 and 11 was not sufficient to eliminate this failure. The overrun became much smaller, but the named check still did not hold.
- C-PERTURBATION-REACHED failed twice:
  - Attempt 10: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  - Attempt 11: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  Whatever changed between attempts 10 and 11 is not what resolves this repeated failure. In both records, the failing kind was held_out_variant, stopped by C-BUDGET-RESPECTED; the ruleset kind reached its threshold.
- C-PER-STEP-COST-CEILING failed once:
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”.
  This specific check did hold in attempt 11, whose per_step_cost_ratio was 1.5815.
- In aggregate, the only perturbation failures were two held_out_variant outcomes, both failing C-BUDGET-RESPECTED. Ruleset perturbations reached their thresholds in all 14 records. The other 12 held_out_variant outcomes also reached their thresholds.

4. Ruled-out directions

- Do not repeat the attempt-10 cost regime unchanged. Its qualifying time of 50.5532 seconds exceeded the 31.1 ceiling, its per-step cost was 4.6619 times the seed anchor and above the 3.0 ceiling, its held_out_variant failed, validity fell to 0.0, and reward was 0.0000. Repeating it without changing those causes would be neither exploration nor exploitation.
- Do not treat the attempt-11 near-budget result as acceptable merely because it was valid and much closer to the ceiling. At 31.6532 seconds it still exceeded 31.1, still failed C-BUDGET-RESPECTED and C-PERTURBATION-REACHED, still missed the held_out_variant threshold, and rewarded only 0.3385.
- Do not continue the measured high-cost conforming regime represented by attempts 9 and 12–14 without a concrete change aimed at reward. Although it passed every check, all four rewards, 0.3601–0.4779, were lower than the already established 0.6964 best.
- Do not assume that merely passing all checks is enough to improve reward. Attempts 1–9 and 12–14 all passed all checks, yet their rewards varied from 0.3601 to 0.6964.
- Do not assume higher compute_efficiency alone predicts the winner. Attempt 6 had compute_efficiency 0.5781 and the highest reward 0.6964, while several attempts with compute_efficiency 1.0 scored materially lower. This does not establish a causal inverse relationship; it only rules out optimizing that reported term in isolation.

5. Open leads

- Exploit attempt 6’s successful regime. It is the one to beat at reward 0.6964 and already satisfies every hard requirement: primary_target_reached 1.0, all perturbations held, conformance_fraction 1.0, rule_conformance 1.0, task_pass 1.0, validity 1.0, and no red-line crossing.
- Preserve ample protection against the known hard failures: keep qualifying time below 31.1 seconds, keep per_step_cost_ratio below 3.0, and explicitly ensure the held_out_variant reaches its threshold within its own budget. Attempt 6 already had qualifying_budget 19.6077 seconds and per_step_cost_ratio 1.5374, so it had substantial measured margin on both ceilings.
- Use attempts 5 and 6 as the strongest local comparison. Attempt 5 rewarded 0.6687 with qualifying_budget 19.4243, compute_efficiency 0.8764, and per_step_cost_ratio 1.0830; attempt 6 rewarded 0.6964 with qualifying_budget 19.6077, compute_efficiency 0.5781, and per_step_cost_ratio 1.5374. The next change should preserve the shared success conditions while seeking a reward improvement over 0.6964, rather than blindly minimizing one auxiliary metric.
- Treat attempts 7 and 8 as warnings against uncontrolled continuation: both remained fully conforming but fell to 0.6506 and 0.6481. Any modification to the attempt-6 family should therefore be narrow and reversible.
- Call: exploit. Refine the attempt-6 class while preserving its conformance and perturbation success; the scored approaches have not exhausted the best-performing regime, and structurally different exploration is less justified than improving the current 0.6964 leader.
