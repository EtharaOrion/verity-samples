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

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.5513   1.000             2 of 2         yes             23                
  2 *      0.6387   1.000             2 of 2         yes             16                

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

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

- Attempt 1: reward **0.5513**. It reached the primary target, passed the task, remained valid and rule-conformant, and held both perturbations. Wall-clock and qualifying budget were 22.9821 seconds; compute efficiency was 1.0000 and per-step cost ratio was 0.9652.
- Attempt 2: reward **0.6387**. It outperformed Attempt 1 and every earlier attempt. It reached the primary target, passed the task, remained valid and rule-conformant, and held both perturbations. Wall-clock and qualifying budget improved to 16.4412 seconds, although compute efficiency fell to 0.8426 and per-step cost ratio rose to 1.1242. **Attempt 2 holds the highest reward and is the one to beat.**

Across both measured attempts, held-out perturbations succeeded in aggregate:
- `held_out_variant`: reached its threshold in 2 of 2 measured submissions; no check stopped it.
- `ruleset`: reached its threshold in 2 of 2 measured submissions; no check stopped it.
- Overall: all declared perturbations held in both attempts, for 4 successful perturbation-unit outcomes out of 4.

2. Approach classes tried

The supplied measurements do not describe the underlying algorithmic or implementation changes, so distinct structural approach classes cannot be reconstructed reliably. The measurable progression is one successful, fully conformant training approach followed by a faster-scoring refinement:

- Attempt 1 established a valid baseline that reached all primary and held-out thresholds.
- Attempt 2 preserved all successful behavior while reducing wall-clock and qualifying budget from 22.9821 to 16.4412 seconds, raising reward from 0.5513 to 0.6387. This came with a higher per-step cost ratio and lower reported compute efficiency, so its gain is supported by lower total qualifying time rather than cheaper individual steps.

3. Checks that failed

No named checks failed in either attempt. Both submissions had:
- `primary_target_reached = 1.0`
- `task_pass = 1.0`
- `validity = 1.0`
- `rule_conformance = 1.0`
- `conformance_fraction = 1.0`
- `red_line_crossed = 0.0`
- `all_perturbations_held = true`

There is therefore no recurring failed check to diagnose.

4. Ruled-out directions

- Do not trade away validity, rule conformance, the primary target, or perturbation robustness merely to reduce runtime. Both measured rewards depend on preserving these fully successful outcomes.
- Do not revert to Attempt 1’s performance profile unchanged: it scored **0.5513**, plainly below Attempt 2’s **0.6387**, and took substantially longer.
- No structural algorithm family can be ruled out from the supplied evidence because the records contain measurements but no descriptions of the submitted implementations.

5. Open leads

- **Exploit Attempt 2**, the current best, while preserving its complete conformance and 4-of-4 aggregate perturbation success.
- Reduce total wall-clock and qualifying budget below 16.4412 seconds without losing the primary target or either perturbation kind.
- Investigate reducing Attempt 2’s 1.1242 per-step cost ratio, provided that doing so does not increase the number of steps or total runtime.
- Seek to recover compute efficiency from 0.8426 toward or beyond Attempt 1’s 1.0000 while retaining Attempt 2’s lower total qualifying time.
- Because every measured check already holds and reward improved substantially, the next move should be **exploit**, not explore.
