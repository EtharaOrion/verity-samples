# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 2 -- reward 0.6387, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 16
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All two attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.5513   1.000             2 of 2         yes             23                
  2 *      0.6387   1.000             2 of 2         yes             16                
  3        0.6043   1.000             2 of 2         yes             20                
  4        0.4776   1.000             2 of 2         yes             28                

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

    attempt 1 -- reward 0.5513, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 23
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

- Attempt 4: reward 0.4776, the lowest measured result. It reached the primary target, remained valid and fully conformant, and held all perturbations, but was plainly worse than the earlier best. Qualifying budget and wall-clock time were 28.4730 seconds; compute efficiency was 0.9723 and per-step cost ratio was 0.9534.
- Attempt 1: reward 0.5513. It reached the primary target, remained valid and fully conformant, and held all perturbations. Qualifying budget and wall-clock time were 22.9821 seconds; compute efficiency was 1.0000 and per-step cost ratio was 0.9652.
- Attempt 3: reward 0.6043. It reached the primary target, remained valid and fully conformant, and held all perturbations, but its reward was lower than attempt 2’s earlier reward. Qualifying budget and wall-clock time were 19.5786 seconds; compute efficiency was 0.8281 and per-step cost ratio was 1.0323.
- Attempt 2: reward 0.6387, the highest reward so far and the one to beat. It reached the primary target, remained valid and fully conformant, and held all perturbations. Qualifying budget and wall-clock time were 16.4412 seconds; compute efficiency was 0.8426 and per-step cost ratio was 1.1242.

2. Approach classes tried

The supplied records do not describe algorithm structures or code changes, so distinct architectural approaches cannot be reconstructed. At the measurable level, all four attempts belong to one broad class: valid, rule-conformant training algorithms that reached the primary target and generalized successfully to both declared perturbation kinds. The differences are performance-tuning variants within that successful class.

Within that class:

- Attempt 2 produced the strongest balance under the grading formula: reward 0.6387 with the shortest qualifying budget and wall-clock time, 16.4412 seconds.
- Attempt 3 remained successful on every binary requirement but regressed to reward 0.6043 and 19.5786 seconds.
- Attempt 1 was also completely successful but slower at 22.9821 seconds, yielding reward 0.5513.
- Attempt 4 had the best per-step cost ratio, 0.9534, and relatively high compute efficiency, 0.9723, but took 28.4730 seconds and fell to reward 0.4776. This shows that those favorable component metrics did not compensate for its longer qualifying budget under the actual reward.

Across all records, 8 of 8 perturbation runs reached threshold:

- `held_out_variant`: 4 of 4 reached threshold; none was stopped by a check.
- `ruleset`: 4 of 4 reached threshold; none was stopped by a check.

3. Checks that failed

No named check failed in any attempt. Every record has an empty `failed_checks` list, full conformance fraction, full rule conformance, validity, task pass, primary-target attainment, no red-line crossing, and all perturbations held.

No perturbation check failed. Both perturbation kinds reached their thresholds in every measured record, so there is no recurring failed check to diagnose.

4. Ruled-out directions

- Reusing the attempt 3 configuration unchanged is ruled out as an improvement direction because it scored reward 0.6043, plainly below attempt 2’s 0.6387, while preserving the same successful conformance and perturbation outcomes.
- Reusing the attempt 4 configuration unchanged is ruled out because it regressed further to reward 0.4776, the worst measured result. Its lower per-step cost ratio and higher compute efficiency did not overcome its 28.4730-second qualifying budget.
- Optimizing per-step cost ratio or compute efficiency in isolation is not supported as the main direction. Attempt 4 had the best per-step cost ratio and better compute efficiency than attempts 2 and 3, yet had the lowest reward because its qualifying budget was much longer.
- There is no reason to trade away validity, conformance, primary-target attainment, or perturbation robustness: all attempts already held these requirements, and the records provide no evidence that relaxing them would be acceptable or beneficial.
- No structural algorithm family can be ruled out from these terms alone because the actual implementation differences were not supplied.

5. Open leads

Exploit attempt 2, the current best at reward 0.6387. Preserve its full validity, conformance, primary-target success, lack of red-line crossing, and 4-of-4 aggregate perturbation success while tuning for an even shorter qualifying budget or otherwise improving the measured reward.

Use attempt 2’s measurable profile as the baseline: 16.4412-second qualifying budget and wall-clock time, compute efficiency 0.8426, and per-step cost ratio 1.1242. The strongest evidence is that lower time to qualification aligned with higher reward across these attempts, whereas improving per-step cost ratio alone did not. Changes should therefore prioritize faster target attainment without breaking either `held_out_variant` or `ruleset` robustness.

The call is **exploit**: refine the already highest-scoring, fully successful attempt 2 rather than explore a structurally different approach.
