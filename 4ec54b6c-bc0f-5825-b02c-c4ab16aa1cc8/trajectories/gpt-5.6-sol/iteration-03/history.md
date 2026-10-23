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

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.5513   1.000             2 of 2         yes             23                
  2 *      0.6387   1.000             2 of 2         yes             16                
  3        0.6043   1.000             2 of 2         yes             20                

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

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

- Attempt 1: reward 0.5513. It reached the primary target, passed the task, remained valid and fully conformant, crossed no red line, and held both perturbation kinds. Wall-clock and qualifying budget were 22.9821 seconds; compute efficiency was 1.0000 and per-step cost ratio was 0.9652.
- Attempt 3: reward 0.6043. It reached the primary target, passed the task, remained valid and fully conformant, crossed no red line, and held both perturbation kinds. Wall-clock and qualifying budget were 19.5786 seconds; compute efficiency was 0.8281 and per-step cost ratio was 1.0323. Despite beating attempt 1, its reward was lower than the earlier attempt 2.
- Attempt 2: reward 0.6387. It reached the primary target, passed the task, remained valid and fully conformant, crossed no red line, and held both perturbation kinds. Wall-clock and qualifying budget were 16.4412 seconds; compute efficiency was 0.8426 and per-step cost ratio was 1.1242. Attempt 2 holds the highest reward and is the one to beat.

Across all measured attempts, held-out perturbations reached their thresholds in aggregate: held_out_variant reached in 3 of 3 submissions, and ruleset reached in 3 of 3 submissions. Overall, all 6 of 6 reported perturbation units reached their thresholds, with no stopping check.

2. Approach classes tried

The records do not describe the submitted algorithms or code changes, so distinct structural approach classes cannot be reconstructed. All three submissions belong only to the observable class of successful, valid, fully conformant training algorithms that reached the primary target and survived both perturbation kinds.

Within that observable class, the measured operating profiles differed:

- Attempt 1 had the strongest reported compute efficiency and the lowest per-step cost ratio, but the longest wall-clock time and lowest reward.
- Attempt 2 had the shortest wall-clock time and highest reward, despite a higher per-step cost ratio than the other attempts.
- Attempt 3 occupied the middle in wall-clock time but had the lowest compute efficiency; it scored below attempt 2.

3. Checks that failed

No named checks failed in any submission. Every attempt had an empty `failed_checks` list, full conformance, full rule conformance, validity, task passage, and no red-line crossing.

No perturbation was stopped by a check. Both perturbation kinds—`held_out_variant` and `ruleset`—reached their thresholds in every measured submission.

4. Ruled-out directions

- Treating attempt 3’s measured changes as an improvement over attempt 2 is ruled out: attempt 3’s reward was 0.6043, lower than attempt 2’s 0.6387, and its wall-clock time was also longer.
- Optimizing reported compute efficiency or per-step cost ratio alone is not supported as the route to the best reward. Attempt 1 had compute efficiency 1.0000 and per-step cost ratio 0.9652, both better than attempt 2 on those individual metrics, yet its reward was only 0.5513 because its qualifying wall-clock was substantially longer.
- There is no basis for pursuing a conformance or perturbation repair: no conformance check failed, and all perturbations held in all three submissions.
- No specific algorithmic direction can be ruled out from implementation details, because those details were not supplied.

5. Open leads

Exploit attempt 2, the current best at reward 0.6387. Preserve its demonstrated primary-target success, validity, full conformance, absence of red-line crossing, and robustness to both `held_out_variant` and `ruleset` perturbations while trying to reduce its 16.4412-second qualifying wall-clock.

The measurements suggest prioritizing end-to-end time to target rather than improving compute efficiency or per-step cost ratio in isolation. Any modification should be compared directly against attempt 2 and should retain all 6-of-6 aggregate perturbation outcomes represented across the records. This is an exploit call: refine the already highest-scoring approach rather than switch to an unsupported structural idea.
