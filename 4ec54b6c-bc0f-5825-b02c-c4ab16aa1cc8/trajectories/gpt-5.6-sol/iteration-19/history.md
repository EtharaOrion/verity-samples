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

    All 13 attempts since have scored lower than it.
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
  13 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 17 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 26
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-PER-STEP-COST-CEILING -- per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0

    attempt 18 -- reward 0.4085, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 30
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

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 4 attempts (10, 11, 16, 19). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 3 attempts (10, 16, 17). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 3 attempts (10, 11, 19). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Every graded attempt, ordered worst to best by reward:

- Attempt 10: reward **0.0000**. This was lower than earlier attempts. Invalid and task-failing after crossing the red line; it failed budget, perturbation-reach, and per-step-cost checks.
- Attempt 16: reward **0.0000**. This was lower than earlier attempts. Invalid and task-failing after crossing the red line; it failed budget and per-step-cost checks.
- Attempt 17: reward **0.0000**. This was lower than earlier attempts. Invalid and task-failing after crossing the red line; it failed the per-step-cost ceiling.
- Attempt 19: reward **0.1470**. This was lower than an earlier attempt. It remained valid but failed the task because only one of two perturbation kinds reached its threshold within budget.
- Attempt 11: reward **0.3385**. This was lower than an earlier attempt. It remained valid but failed the task because only one of two perturbation kinds reached its threshold within budget.
- Attempt 9: reward **0.3601**. This was lower than an earlier attempt despite passing the task and all perturbations.
- Attempt 15: reward **0.4034**. This was lower than an earlier attempt despite full conformance and task success.
- Attempt 13: reward **0.4070**. This was lower than an earlier attempt despite full conformance and task success.
- Attempt 18: reward **0.4085**. This was lower than an earlier attempt despite full conformance and task success.
- Attempt 14: reward **0.4201**. This was lower than an earlier attempt despite full conformance and task success.
- Attempt 4: reward **0.4776**. This was lower than an earlier attempt despite full conformance and task success.
- Attempt 12: reward **0.4779**. This was lower than an earlier attempt despite full conformance and task success.
- Attempt 1: reward **0.5513**. This was the first measured baseline; it passed the primary target and both perturbation kinds.
- Attempt 3: reward **0.6043**. This was lower than attempt 2 despite full conformance and task success.
- Attempt 2: reward **0.6387**. This improved on attempt 1 while retaining full conformance and task success.
- Attempt 8: reward **0.6481**. This was lower than attempt 6 despite full conformance and task success.
- Attempt 7: reward **0.6506**. This was lower than attempt 6 despite full conformance and task success.
- Attempt 5: reward **0.6687**. This improved on every earlier attempt while retaining full conformance and task success.
- Attempt 6: reward **0.6964**. This is the highest reward and is the one to beat. It reached the primary target and both perturbation thresholds, with qualifying budget 19.6077 seconds and per-step cost ratio 1.5374.

All 19 submissions produced measurements; none had an unmeasured status.

2. Approach classes tried

The records do not include algorithm or code descriptions, so the approaches can only be reconstructed by their measured operating profiles:

- **Fast, fully conforming, competitive profile — attempts 1–8.** Every attempt reached the primary target and both perturbation kinds without failed checks. Rewards ranged from 0.4776 to 0.6964. Attempts 2, 5, and 6 successively established new best rewards. Attempt 6 was best with reward 0.6964, qualifying budget 19.6077, per-step cost ratio 1.5374, and compute efficiency 0.5781. Increasing apparent cost beyond that did not automatically help: attempts 7 and 8 had per-step ratios 1.5308 and 2.0341 but lower rewards of 0.6506 and 0.6481.

- **Slow but technically passing profile — attempt 9.** It reached all targets and had no failed checks, but used qualifying budget 28.3438 seconds, wall clock 31.3334 seconds, and per-step cost ratio 2.0655. Its reward fell to 0.3601, well below the earlier best.

- **Over-budget held-out-variant profile — attempts 11 and 19, with attempt 10 as a more extreme version.** The ruleset perturbation reached its threshold, but the held-out variant did not reach within its own budget because of `C-BUDGET-RESPECTED`. Attempts 11 and 19 exceeded the 31.1-second ceiling narrowly, at 31.6532 and 31.8889 seconds. Attempt 10 exceeded it severely at 50.5532 seconds and also exceeded the per-step-cost ceiling.

- **Conforming but lower-reward later profile — attempts 12–15 and 18.** All targets and perturbations held, no checks failed, and per-step ratios stayed between 1.3138 and 1.7019. Nevertheless, rewards remained between 0.4034 and 0.4779, substantially below attempt 6. Full conformance alone did not recover competitiveness.

- **Red-line per-step-cost profile — attempts 16 and 17.** Both reached the primary target and both perturbation kinds, but were invalidated by `C-PER-STEP-COST-CEILING`. Attempt 16 also exceeded the wall-clock budget. Their rewards were 0.0000.

Across all perturbation units, **35 of 38 reached their thresholds**. By kind:
- `ruleset`: **19 of 19 reached**, with no failed checks.
- `held_out_variant`: **16 of 19 reached**. Three held-out-variant units did not reach, each stopped by `C-BUDGET-RESPECTED`.
- At the submission level, **16 of 19 attempts held both perturbations**; attempts 10, 11, and 19 held only one of two.

3. Checks that failed

- **`C-BUDGET-RESPECTED` failed four times**: attempts 10, 11, 16, and 19.
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 16: “the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 19: “the qualifying row sits at 31.8888943195343 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Because this check has now failed four times across changed submissions, whatever changed between those attempts did not eliminate the recurring wall-clock overrun.

- **`C-PERTURBATION-REACHED` failed three times**: attempts 10, 11, and 19.
  - In every case, the verifier’s reason was: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  - The failing perturbation kind was always `held_out_variant`, stopped by `C-BUDGET-RESPECTED`; the `ruleset` kind reached every time.
  - Because this check has now failed three times across changed submissions, whatever changed between those attempts did not solve the held-out variant’s budget-limited threshold failure.

- **`C-PER-STEP-COST-CEILING` failed three times**: attempts 10, 16, and 17.
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 16: “per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 17: “per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0”.
  - Because this check has now failed three times across changed submissions, whatever changed between those attempts did not reliably control per-step cost below the hard ceiling.

4. Ruled-out directions

- **Any design with per-step cost above 3.0 times the seed anchor is ruled out.** Attempts 10, 16, and 17 crossed that explicit ceiling, became invalid, failed the task, and received reward 0.0000. Repeating this without directly reducing per-step cost would be neither useful exploration nor exploitation.

- **Operating close to or above the 31.1-second wall-clock ceiling is ruled out as unsafe.** Even modest overruns in attempts 11 and 19 caused the held-out variant to miss its in-budget threshold and caused task failure. Attempt 10’s much larger overrun additionally crossed the red line.

- **Increasing computation or per-step expense without demonstrated reward benefit is ruled out.** Attempt 8’s ratio of 2.0341 scored below attempts 5–7; attempt 9’s ratio of 2.0655 scored only 0.3601; ratios of 3.1522, 4.6619, and 8.3821 caused hard failures. More expensive steps are not, by themselves, a viable improvement strategy.

- **The later fully conforming profile represented by attempts 12–15 and 18 is not competitive in its observed form.** It safely passed every target, but rewards of 0.4034–0.4779 remained far below 0.6964. Repeating that profile unchanged would not address the reward gap.

- **Merely preserving primary-target and perturbation success is insufficient.** Attempts 4, 9, and 12–15 and 18 all passed every target but scored much less than attempt 6. Conformance is necessary for safety, but it does not distinguish the best-performing algorithm.

5. Open leads

- Reconstruct and exploit the operating regime closest to attempt 6: primary target reached, both perturbation kinds reached, no failed checks, wall clock around 19.6 seconds, and per-step cost safely below 3.0. Attempt 6’s reward **0.6964** is the one to beat.

- Use attempts 5–8 to identify a productive local range rather than assuming monotonicity. Attempt 5 scored 0.6687 at per-step ratio 1.0830; attempt 6 improved to 0.6964 at 1.5374; attempts 7 and 8 then fell to 0.6506 and 0.6481. The evidence supports tuning around the attempt-6 regime, not simply increasing cost.

- Maintain substantial wall-clock margin below 31.1 seconds. The best attempts qualified around 19.4–19.7 seconds, whereas attempts near 31.7–31.9 seconds lost the held-out variant. A target around the best regime provides much more perturbation safety than relying on a narrow sub-second margin.

- Preserve the universally successful ruleset behavior while specifically protecting held-out-variant speed. All ruleset units reached; every perturbation failure came from a held-out variant stopped by `C-BUDGET-RESPECTED`.

- Keep per-step cost comfortably below 3.0, not merely just below it. Attempt 19’s ratio of 2.9956 avoided that particular check but still had little safety margin and failed on budget. The successful attempt-6 ratio of 1.5374 is a better empirical target.

- Implementation details were not supplied in the measured records, so no unsupported claim can be made about which optimizer, schedule, architecture, or update rule produced attempt 6. The next work should use the best-known measured profile as its acceptance target and reject variants that drift toward the slow, over-budget, or red-line classes.

**Call: exploit.** Attempt 6 already scored highest, so the justified next move is to reproduce its safe, fully conforming regime and tune it locally for reward rather than explore a structurally different high-cost design.
