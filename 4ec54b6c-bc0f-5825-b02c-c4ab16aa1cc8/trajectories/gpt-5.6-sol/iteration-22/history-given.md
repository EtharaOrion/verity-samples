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

    All 15 attempts since have scored lower than it.
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
  22       0.0000   1.000             1 of 2         yes             36                

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
  16 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 20 -- reward --
      approach: not measured -- the unverified prose below is the only account of it
      measured: nothing. This attempt produced no measurement.
      narrative: no run was graded, so the verifier recorded no check.

    attempt 21 -- reward 0.3488, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 22 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 36
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 2 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 35.771381855010986 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget
        C-PER-STEP-COST-CEILING -- per-step cost is 3.402 times the seed anchor, above the ceiling of 3.0

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 5 attempts (10, 11, 16, 19, 22). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING has failed on 4 attempts (10, 16, 17, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 4 attempts (10, 11, 19, 22). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

All measured attempts, ordered from worst to best by reward:

- Attempts 10, 16, 17, and 22: reward **0.0000** each. All were lower than an earlier attempt. Attempts 10, 16, 17, and 22 were invalid and crossed a red line.
- Attempt 19: reward **0.1470**. Lower than an earlier attempt.
- Attempt 11: reward **0.3385**. Lower than an earlier attempt.
- Attempt 21: reward **0.3488**. Lower than an earlier attempt.
- Attempt 9: reward **0.3601**. Lower than an earlier attempt.
- Attempt 15: reward **0.4034**. Lower than an earlier attempt.
- Attempt 13: reward **0.4070**. Lower than an earlier attempt.
- Attempt 18: reward **0.4085**. Lower than an earlier attempt.
- Attempt 14: reward **0.4201**. Lower than an earlier attempt.
- Attempt 4: reward **0.4776**. Lower than an earlier attempt.
- Attempt 12: reward **0.4779**. Lower than an earlier attempt.
- Attempt 1: reward **0.5513**, the first measured result.
- Attempt 3: reward **0.6043**. Although above attempt 1, it was lower than the earlier best established by attempt 2.
- Attempt 2: reward **0.6387**, then better than every earlier attempt.
- Attempt 8: reward **0.6481**. Lower than the earlier best established by attempt 6.
- Attempt 7: reward **0.6506**. Lower than the earlier best established by attempt 6.
- Attempt 5: reward **0.6687**, then better than every earlier attempt.
- Attempt 6: reward **0.6964**, better than every earlier attempt and still the highest reward. **Attempt 6 is the one to beat.**

Attempt 20 had measurement status `harbor_exception` and produced **no measurement**; it has no reward and cannot be ranked among the measured attempts.

2. Approach classes tried

- **Fully conforming, perturbation-robust measured configurations:** Attempts 1–9, 12–15, 18, and 21 reached the primary target and both declared perturbation thresholds, had full conformance, remained valid, and produced positive rewards. Their rewards ranged from **0.3488** to **0.6964**. Within this class, attempt 6 was best at **0.6964**, with qualifying budget 19.6077 seconds, per-step cost ratio 1.5374, and compute efficiency 0.5781. Attempt 5 was the next-best record at **0.6687**, with qualifying budget 19.4243 seconds, per-step cost ratio 1.0830, and compute efficiency 0.8764.
- **Over-budget configurations that lost the held-out variant:** Attempts 11 and 19 exceeded the 31.1-second ceiling, causing the held-out-variant perturbation not to reach its threshold, while the ruleset perturbation still reached. They remained valid but did not pass the task and scored **0.3385** and **0.1470**, both lower than the earlier best.
- **Over-budget, excessive-per-step-cost configurations:** Attempts 10 and 22 combined qualifying-budget overruns, held-out-variant failures, and per-step cost above the 3.0 ceiling. Both became invalid, crossed a red line, and scored **0.0000**.
- **Configurations whose perturbations reached but whose global cost limits failed:** Attempt 16 reached both perturbations but exceeded both the qualifying-budget ceiling and per-step-cost ceiling. Attempt 17 reached both perturbations and stayed within the qualifying budget but exceeded the per-step-cost ceiling by a large margin. Both were invalid and scored **0.0000**.
- **Execution failure:** Attempt 20 ended in a `harbor_exception`, produced no perturbation data, and produced no measurement.

No algorithmic or source-level descriptions were supplied, so the approaches can only be reconstructed from these measured behavioral classes, not from specific model architecture, optimizer, schedule, or implementation changes.

3. Checks that failed

Three named checks failed:

- **`C-BUDGET-RESPECTED` failed 5 times**, in attempts 10, 11, 16, 19, and 22:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 16: “the qualifying row sits at 32.978039026260376 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 19: “the qualifying row sits at 31.8888943195343 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  - Attempt 22: “the qualifying row sits at 35.771381855010986 on the wall_clock_sec axis, above the declared ceiling of 31.1”
  
  Because this check failed across five changed submissions, whatever changed between those attempts is not what is causing the recurring failure; the common unresolved fact is that the qualifying row remained above the fixed 31.1-second ceiling.

- **`C-PERTURBATION-REACHED` failed 4 times**, in attempts 10, 11, 19, and 22. The verifier gave the same reason each time: “1 of 2 declared perturbations reached their own threshold inside their own budget.” Because this persisted across four changed submissions, whatever changed between them is not what is causing the recurring failure. In every such record, the failing kind was `held_out_variant`, stopped by `C-BUDGET-RESPECTED`; the `ruleset` kind reached its threshold.

- **`C-PER-STEP-COST-CEILING` failed 4 times**, in attempts 10, 16, 17, and 22:
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”
  - Attempt 16: “per-step cost is 3.152 times the seed anchor, above the ceiling of 3.0”
  - Attempt 17: “per-step cost is 8.382 times the seed anchor, above the ceiling of 3.0”
  - Attempt 22: “per-step cost is 3.402 times the seed anchor, above the ceiling of 3.0”
  
  Because this check failed across four changed submissions, whatever changed between them is not what is causing the recurring failure; per-step cost still exceeded the explicit 3.0 ceiling.

Perturbation outcomes in aggregate across the 21 measured submissions:

- `held_out_variant`: reached in **17 of 21** measured submissions and failed in **4 of 21**. Every failure was stopped by `C-BUDGET-RESPECTED`.
- `ruleset`: reached in **21 of 21** measured submissions and was never stopped by a failed check.
- Overall: **38 of 42** declared perturbation units reached their thresholds.
- Attempt 20 produced no perturbation measurement and is excluded from those totals.

4. Ruled-out directions

- **Allowing qualifying time to approach or exceed 31.1 seconds is ruled out.** Even small overruns failed `C-BUDGET-RESPECTED`: 31.6532 seconds in attempt 11 and 31.8889 seconds in attempt 19 were already too high. Larger overruns also failed, and in attempts 10, 11, 19, and 22 the overrun prevented the held-out variant from reaching.
- **Allowing per-step cost ratio above 3.0 is ruled out.** Ratios of 3.1522, 3.4022, 4.6619, and 8.3821 all failed `C-PER-STEP-COST-CEILING`; the associated attempts were invalid and scored **0.0000**.
- **Trading away the held-out variant is ruled out.** Whenever only one of the two perturbations reached, `C-PERTURBATION-REACHED` failed and task pass was 0. The affected rewards were **0.0000**, **0.3385**, **0.1470**, and **0.0000**, all below the best.
- **Merely reaching both perturbations is insufficient if a red-line cost check fails.** Attempts 16 and 17 reached the primary target and both perturbations but still scored **0.0000** because cost ceilings were violated.
- **Repeating slower fully conforming configurations without a demonstrated reward gain is not competitive with attempt 6.** Attempts 12–15, 18, and 21 all remained conforming and robust but scored only **0.3488–0.4779**, plainly below **0.6964**. The supplied measurements do not identify which source-level changes caused those lower rewards, so only their observed performance profiles—not their unknown algorithmic ideas—can be ruled out.

5. Open leads

- Use attempt 6’s successful profile as the anchor: preserve primary-target success, full rule conformance, both perturbations reaching, validity, qualifying budget comfortably below 31.1 seconds, and per-step cost comfortably below 3.0.
- Compare against attempt 5 as the strongest nearby alternative. Attempt 5 had lower reward (**0.6687** versus **0.6964**) but better compute efficiency (0.8764 versus 0.5781), lower per-step cost ratio (1.0830 versus 1.5374), and a slightly lower qualifying budget (19.4243 versus 19.6077). A refinement should retain attempt 6’s reward advantage while avoiding movement toward either ceiling.
- Keep explicit safety margins rather than targeting the limits. The records show budget failures just above 31.1 seconds and per-step-cost failures just above 3.0, so a candidate should not rely on timing or cost landing exactly at a ceiling.
- Preserve the consistently successful `ruleset` behavior and focus robustness work on the `held_out_variant`, since all four perturbation failures were of that kind and were stopped by `C-BUDGET-RESPECTED`.
- Do not repeat the zero-reward cost-heavy profiles unless the specific failed cost checks are changed: repeating them without fixing the budget or per-step-cost breach would be neither exploration nor exploitation.

**Call: exploit.** Attempt 6 already provides the strongest scored, fully conforming, perturbation-robust result. The next direction should refine that successful class and try to exceed **0.6964**, rather than move to another structurally unknown cost-heavy configuration.
