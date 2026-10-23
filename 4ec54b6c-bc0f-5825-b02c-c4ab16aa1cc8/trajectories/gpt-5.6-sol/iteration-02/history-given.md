# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 1 -- reward 0.5513, first measured attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 23
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1 *      0.5513   1.000             2 of 2         yes             23                

  reward  = what the attempt scored, in the closed interval 0 to 1. No value of it is a pass:
            task pass is a separate conjunction and is reported beside the reward, not inferred
            from it. A high reward with a failed pass, or the reverse, is a real outcome.
  rule conformance = the fraction of the static conformance rules the submitted bytes held.
  perturbation runs = the held-out runs beside the primary one. They are described by kind
            and are deliberately not individually named, so no run has a label you can
            iterate against; what each one measured is not published either.
  --      = the run did not produce this measurement. It is not a zero.
  *       = the best reward so far, and the one to beat.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

- Attempt 1: reward **0.5513**. This is the highest reward so far and the one to beat. It reached the primary target, passed the task, achieved full validity, rule conformance, and conformance fraction, and crossed no red line. Compute efficiency was 1.0, per-step cost ratio was 0.9652, qualifying budget and wall-clock time were both 22.9821 seconds.
- Both declared perturbation units reached their thresholds: one `held_out_variant` kind and one `ruleset` kind. Aggregate outcome: **2 of 2 reached**, with no perturbation checks failing. Therefore, all perturbations held.

2. Approach classes tried

- One successful approach class has been measured. Its implementation details were not supplied in the measured terms, so the algorithm cannot be reconstructed more specifically from this record. It reached the primary target and all held-out thresholds while maintaining complete conformance and validity.

3. Checks that failed

- None. Attempt 1 had an empty `failed_checks` list.
- The `held_out_variant` perturbation reached its threshold with no failed checks.
- The `ruleset` perturbation reached its threshold with no failed checks.

4. Ruled-out directions

- No direction is ruled out by the available evidence. There are no failed checks, unmeasured submissions, zero-reward outcomes, or regressions in the supplied record.

5. Open leads

- Preserve the properties already demonstrated: primary-target success, full task pass, full validity, full rule conformance, no red-line crossing, and success on both `held_out_variant` and `ruleset` perturbation kinds.
- Improve the already-scoring approach rather than replacing it without evidence. The available quantitative optimization lead is to reduce cost or wall-clock usage while retaining every successful check and threshold outcome; the current per-step cost ratio is 0.9652 and wall-clock time is 22.9821 seconds.
- **Call: exploit.** Attempt 1 already scores **0.5513** and has no identified failure to repair, so the next work should refine this successful approach and seek a reward above the current one to beat.
