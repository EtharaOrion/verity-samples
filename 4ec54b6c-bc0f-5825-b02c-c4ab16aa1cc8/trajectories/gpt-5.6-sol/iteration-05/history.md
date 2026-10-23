# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.6687, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 19
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.5513   1.000             2 of 2         yes             23                
  2        0.6387   1.000             2 of 2         yes             16                
  3        0.6043   1.000             2 of 2         yes             20                
  4        0.4776   1.000             2 of 2         yes             28                
  5 *      0.6687   1.000             2 of 2         yes             19                

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
  1 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 2 -- reward 0.6387, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 16
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 3 -- reward 0.6043, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.4776, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Measured attempts, ranked worst to best by reward:

- Attempt 4: reward **0.4776**. This was lower than the earlier best. It reached the primary target and both perturbation thresholds, with compute efficiency 0.9723, per-step cost ratio 0.9534, and qualifying budget/wall-clock time 28.4730 seconds.
- Attempt 1: reward **0.5513**. It reached the primary target and both perturbation thresholds, with compute efficiency 1.0000, per-step cost ratio 0.9652, and qualifying budget/wall-clock time 22.9821 seconds.
- Attempt 3: reward **0.6043**. This was lower than the earlier best established by attempt 2. It reached the primary target and both perturbation thresholds, with compute efficiency 0.8281, per-step cost ratio 1.0323, and qualifying budget/wall-clock time 19.5786 seconds.
- Attempt 2: reward **0.6387**. It improved on every earlier attempt. It reached the primary target and both perturbation thresholds, with compute efficiency 0.8426, per-step cost ratio 1.1242, and qualifying budget/wall-clock time 16.4412 seconds.
- Attempt 5: reward **0.6687**. It improved on every earlier attempt and holds the highest reward; **attempt 5 is the one to beat**. It reached the primary target and both perturbation thresholds, with compute efficiency 0.8764, per-step cost ratio 1.0830, and qualifying budget/wall-clock time 19.4243 seconds.

All five attempts were valid, passed the task, fully conformed to the rules, avoided the red line, and reached the primary target.

2. Approach classes tried

The records do not describe implementation details, hyperparameters, or algorithmic structure, so distinct code-level approach classes cannot be reconstructed safely. At the measured-outcome level, all five attempts belong to one successful and robust class: every submission reached the primary target, maintained full conformance, and held both declared perturbation kinds.

Within that class, the attempts explored different measured efficiency profiles:

- Attempt 1 provided the compute-efficiency baseline at 1.0000.
- Attempt 2 favored the smallest qualifying budget/wall-clock time, 16.4412 seconds, and improved reward to 0.6387 despite lower compute efficiency and a higher per-step cost ratio.
- Attempt 3 had a lower per-step cost ratio than attempt 2 but also lower compute efficiency, longer runtime, and lower reward.
- Attempt 4 had relatively high compute efficiency and the lowest per-step cost ratio, but the longest runtime and the lowest reward.
- Attempt 5 produced the best measured balance so far, raising reward to 0.6687 while preserving every target, validity, conformance, and perturbation result.

Across all perturbation units in aggregate:

- `held_out_variant`: 5 of 5 reached the threshold; none was stopped by a check.
- `ruleset`: 5 of 5 reached the threshold; none was stopped by a check.
- Overall: 10 of 10 perturbation units reached their thresholds, and all perturbations held in every measured attempt.

3. Checks that failed

No named check failed in any attempt. Every `failed_checks` list was empty, both globally and within every perturbation unit. Therefore, there is no repeated failed check to diagnose or attribute to changes between attempts.

4. Ruled-out directions

- Do not reproduce attempt 4’s measured profile unchanged. Its reward was only 0.4776, lower than the earlier best, despite compute efficiency 0.9723 and per-step cost ratio 0.9534. Its 28.4730-second qualifying budget was the longest observed, so favorable compute-efficiency and per-step-cost figures alone did not yield a competitive reward.
- Do not reproduce attempt 3’s measured profile unchanged. Its reward of 0.6043 was lower than attempt 2’s 0.6387. The reduction in per-step cost ratio from 1.1242 to 1.0323 did not compensate for its lower compute efficiency and longer qualifying budget.
- Do not revert unchanged to attempt 1’s baseline profile. Although fully successful and robust, its reward of 0.5513 was surpassed by attempts 2, 3, and 5.
- Optimizing any single reported efficiency metric in isolation is not supported. Attempt 1 had the highest compute efficiency, attempt 4 had the lowest per-step cost ratio, and attempt 2 had the shortest runtime, yet attempt 5 had the highest reward. The evidence supports balancing the measured terms rather than maximizing one of them alone.

5. Open leads

- **Exploit attempt 5**, the current best at reward 0.6687. Preserve its demonstrated validity, full rule conformance, primary-target success, red-line avoidance, and complete robustness across both perturbation kinds.
- Seek a local improvement to attempt 5’s measured efficiency balance. Attempt 2 shows that a shorter qualifying budget is possible—16.4412 versus 19.4243 seconds—while still retaining all success and robustness checks. A useful lead is to reduce attempt 5’s runtime without surrendering the characteristics that gave it the higher reward.
- Attempt 5 also improved compute efficiency over attempt 2, from 0.8426 to 0.8764, while reducing the per-step cost ratio from 1.1242 to 1.0830. Preserve those gains while testing whether the qualifying budget can move toward attempt 2’s lower value.
- Continue checking both `held_out_variant` and `ruleset` behavior after every optimization. They currently have perfect aggregate results, so no robustness repair is needed; the opportunity is reward improvement without regression.
- Because a fully conforming approach is still improving and attempt 5 established a new best, the correct next move is **exploit**, not explore.
