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

    All one attempts since have scored lower than it.
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

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

All graded attempts, ordered from worst to best by reward:

- Attempt 4: reward 0.4776. It reached the primary target, passed all conformance and validity checks, and held both perturbation kinds, but was worse than an earlier attempt. Qualifying budget and wall-clock time were 28.4730 seconds, the highest observed; compute efficiency was 0.9723 and per-step cost ratio was 0.9534.
- Attempt 1: reward 0.5513. It reached the primary target and established the initial measured baseline. Qualifying budget and wall-clock time were 22.9821 seconds; compute efficiency was 1.0000 and per-step cost ratio was 0.9652.
- Attempt 3: reward 0.6043. It was lower than the earlier best from attempt 2. Qualifying budget and wall-clock time were 19.5786 seconds; compute efficiency was 0.8281 and per-step cost ratio was 1.0323.
- Attempt 2: reward 0.6387. It improved over attempt 1. Qualifying budget and wall-clock time were 16.4412 seconds, the lowest observed; compute efficiency was 0.8426 and per-step cost ratio was 1.1242.
- Attempt 7: reward 0.6506. This was lower than the earlier best from attempt 6, so it did not represent progress. Qualifying budget and wall-clock time were 19.6597 seconds; compute efficiency was 0.6084 and per-step cost ratio was 1.5308.
- Attempt 5: reward 0.6687. It improved over every earlier attempt through attempt 4. Qualifying budget and wall-clock time were 19.4243 seconds; compute efficiency was 0.8764 and per-step cost ratio was 1.0830.
- Attempt 6: reward 0.6964. This is the highest reward and the one to beat. Qualifying budget and wall-clock time were 19.6077 seconds; compute efficiency was 0.5781 and per-step cost ratio was 1.5374.

Every attempt was measured, reached the primary target, passed the task, remained valid and rule-conformant, avoided the red line, and held all declared perturbations.

2. Approach classes tried

The records do not describe implementation details, model structure, optimizer choices, schedules, or other algorithmic changes, so distinct algorithm classes cannot be reconstructed faithfully. The measurable outcomes nevertheless form three performance regimes:

- Initial and regressive measured variants: attempts 1, 3, and 4 scored from 0.4776 to 0.6043. Attempt 4 combined a low per-step cost ratio with the longest qualifying budget and produced the lowest reward.
- Faster-budget variant: attempt 2 reached qualification in 16.4412 seconds and scored 0.6387. It was the fastest measured attempt but did not achieve the best reward.
- Higher-reward variants: attempts 5, 6, and 7 scored 0.6687, 0.6964, and 0.6506. Attempt 6 set the best reward despite the lowest compute-efficiency value and highest per-step cost ratio among the measured attempts. Attempt 7 remained in a similar measured metric regime but fell below attempt 6; because no implementation descriptions are supplied, the exact change responsible cannot be identified.

Across all seven attempts, there were 14 held-out perturbation runs in aggregate: seven of kind `held_out_variant` and seven of kind `ruleset`. Every `held_out_variant` run reached its threshold, and every `ruleset` run reached its threshold. No perturbation run was stopped by a failed check.

3. Checks that failed

No named checks failed in any attempt. Each record has an empty `failed_checks` list.

In aggregate:

- `held_out_variant`: 7 of 7 runs reached threshold; none failed a check.
- `ruleset`: 7 of 7 runs reached threshold; none failed a check.
- Overall: 14 of 14 perturbation runs reached threshold.
- Conformance fraction, rule conformance, validity, task pass, and primary-target reach were all 1.0 for every attempt.
- No repeated failed check exists to diagnose.

4. Ruled-out directions

- Repeating the attempt-4 outcome without a material change is ruled out: it produced the lowest reward, 0.4776, and the longest qualifying budget and wall-clock time, 28.4730 seconds.
- Treating minimum wall-clock time alone as the objective is ruled out: attempt 2 was fastest at 16.4412 seconds but scored 0.6387, below attempts 5 and 6.
- Treating higher reported compute efficiency alone as a reliable route to higher reward is ruled out by the measurements: attempt 1 had compute efficiency 1.0000 and attempt 4 had 0.9723, yet their rewards were only 0.5513 and 0.4776. Attempt 6 had the lowest compute efficiency, 0.5781, while achieving the highest reward, 0.6964.
- Treating lower per-step cost ratio alone as a reliable route to higher reward is also ruled out: attempt 4 had the lowest ratio, 0.9534, but the lowest reward, whereas attempt 6 had the highest ratio, 1.5374, and the highest reward.
- Repeating the change that led from attempt 6 to attempt 7 without understanding or altering it is ruled out: reward fell plainly from 0.6964 to 0.6506. The supplied terms do not identify what implementation change caused that regression.
- Chasing verifier or perturbation fixes is not supported: no check failed, and all 14 perturbation runs reached their thresholds.

5. Open leads

- Use attempt 6’s algorithmic configuration as the primary baseline, because its reward of 0.6964 is the one to beat. Preserve its successful primary-target, validity, conformance, and perturbation behavior while making controlled changes.
- Recover the missing implementation-level distinction between attempts 5, 6, and 7. The measurements show that attempt 6 improved on attempt 5, while attempt 7 regressed, but they do not reveal which hyperparameter, schedule, or structural change was responsible.
- Test small, isolated modifications around attempt 6 rather than optimizing proxy metrics independently. The observed reward does not rank monotonically with compute efficiency, per-step cost ratio, or wall-clock time.
- Attempt 5 is a useful secondary reference: it scored 0.6687 with substantially higher compute efficiency and lower per-step cost ratio than attempt 6. If implementation details can be recovered, selectively combining attempt 5’s efficiency characteristics with the reward-producing behavior of attempt 6 may be worth testing, while recognizing that the current records do not establish causality.
- Continue preserving both perturbation kinds. All measured approaches were robust on `held_out_variant` and `ruleset`, so a candidate that sacrifices those guarantees would introduce a new failure mode rather than address an existing one.

Call: exploit. Refine the highest-scoring attempt-6 approach with controlled changes; the scored approaches are still differentiated by reward, and there is no failed check requiring a structural reset.
