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

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.5513   1.000             2 of 2         yes             23                
  2        0.6387   1.000             2 of 2         yes             16                
  3        0.6043   1.000             2 of 2         yes             20                
  4        0.4776   1.000             2 of 2         yes             28                
  5        0.6687   1.000             2 of 2         yes             19                
  6 *      0.6964   1.000             2 of 2         yes             20                

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
  2 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 2 -- reward 0.6387, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 16
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.4776, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 5 -- reward 0.6687, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 19
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

All six submissions produced measurements. Ranked worst to best by reward:

- Attempt 4: reward 0.4776. This was lower than the earlier best. It reached the primary target and both perturbation thresholds, with compute efficiency 0.9723, per-step cost ratio 0.9534, and qualifying budget/wall time 28.4730 seconds.
- Attempt 1: reward 0.5513. It reached the primary target and both perturbation thresholds, with compute efficiency 1.0000, per-step cost ratio 0.9652, and qualifying budget/wall time 22.9821 seconds.
- Attempt 3: reward 0.6043. This was lower than the earlier best established by attempt 2. It reached the primary target and both perturbation thresholds, with compute efficiency 0.8281, per-step cost ratio 1.0323, and qualifying budget/wall time 19.5786 seconds.
- Attempt 2: reward 0.6387. It improved on every earlier attempt. It reached the primary target and both perturbation thresholds, with compute efficiency 0.8426, per-step cost ratio 1.1242, and qualifying budget/wall time 16.4412 seconds.
- Attempt 5: reward 0.6687. It improved on every earlier attempt. It reached the primary target and both perturbation thresholds, with compute efficiency 0.8764, per-step cost ratio 1.0830, and qualifying budget/wall time 19.4243 seconds.
- Attempt 6: reward 0.6964. It improved on every earlier attempt and holds the highest reward; it is the one to beat. It reached the primary target and both perturbation thresholds, with compute efficiency 0.5781, per-step cost ratio 1.5374, and qualifying budget/wall time 19.6077 seconds.

2. Approach classes tried

The supplied records contain no implementation or algorithm descriptions, so distinct structural training approaches cannot be reconstructed. At the measurable level, all attempts belong to one successful class: valid, rule-conforming submissions that passed the task, reached the primary target, avoided the red line, and generalized to every declared perturbation.

Within that class, the attempts explored different performance profiles. Attempts 2, 5, and 6 successively established new best rewards. Attempts 3 and 4 changed the profile but regressed relative to an earlier best. In particular, attempt 6 achieved the best reward despite having the lowest compute efficiency and highest per-step cost ratio, while attempt 4 combined comparatively strong compute efficiency and the lowest per-step cost ratio with the worst reward.

Across all six attempts, 12 of 12 perturbation units reached their thresholds:

- `held_out_variant`: 6 of 6 reached; none was stopped by a check.
- `ruleset`: 6 of 6 reached; none was stopped by a check.
- Aggregate: 12 of 12 reached, and every submission had `all_perturbations_held: true`.

3. Checks that failed

No named check failed in any attempt. Every `failed_checks` list was empty, both for the primary submissions and for all perturbation units.

All six attempts had full validity, task pass, rule conformance, and conformance fraction; all reached the primary target; none crossed the red line.

4. Ruled-out directions

- Treating better compute efficiency alone as a reliable route to higher reward is ruled out by these measurements. Attempt 4 had compute efficiency 0.9723 but the lowest reward, 0.4776, whereas attempt 6 had the lowest compute efficiency, 0.5781, but the highest reward, 0.6964.
- Treating a lower per-step cost ratio alone as a reliable route to higher reward is likewise ruled out. Attempt 4 had the lowest ratio, 0.9534, and the lowest reward, while attempt 6 had the highest ratio, 1.5374, and the highest reward.
- Increasing wall-clock or qualifying budget without preserving the properties responsible for reward is not supported. Attempt 4 used 28.4730 seconds, the longest measured duration, yet scored worst.
- Repeating the profiles represented by attempts 3 or 4 without a substantive change is not justified: both were plainly lower than an earlier best, despite remaining fully conformant and robust.

5. Open leads

Exploit attempt 6’s approach because it is the current best at reward 0.6964 and has no failed check to repair. Preserve its demonstrated validity, primary-target success, full rule conformance, lack of red-line crossing, and success on both `held_out_variant` and `ruleset` perturbations.

Improve reward directly rather than optimizing compute efficiency or per-step cost ratio in isolation; the observed rankings show those metrics are not monotonic proxies for reward. Attempts 2, 5, and 6 form the useful progression of new bests, with attempt 6 the one to beat. Because the records omit algorithm and hyperparameter details, the exact implementation differences responsible for that progression are unknown and must not be guessed.

Call: exploit.
