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

    All nine attempts since have scored lower than it.
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
  9 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 15 -- reward 0.4034, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
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

Every submission produced a measurement. Ranked from worst to best by reward:

- Attempt 10: reward **0.0000**. This was lower than an earlier attempt. It reached the primary target but was invalid, crossed the red line, failed two of the perturbation/conformance requirements, and exceeded the per-step cost ceiling.
- Attempt 11: reward **0.3385**. This was lower than an earlier attempt. It reached the primary target and remained valid, but only one of two perturbation kinds reached its threshold within budget.
- Attempt 9: reward **0.3601**. This was lower than an earlier attempt despite full conformance and both perturbation kinds reaching.
- Attempt 15: reward **0.4034**. This was lower than an earlier attempt despite full conformance and both perturbation kinds reaching.
- Attempt 13: reward **0.4070**. This was lower than an earlier attempt despite full conformance and both perturbation kinds reaching.
- Attempt 14: reward **0.4201**. This was lower than an earlier attempt despite full conformance and both perturbation kinds reaching.
- Attempt 4: reward **0.4776**. This was lower than an earlier attempt despite full conformance and both perturbation kinds reaching.
- Attempt 12: reward **0.4779**. This was lower than an earlier attempt despite full conformance and both perturbation kinds reaching.
- Attempt 1: reward **0.5513**. This was the first measured result, with full conformance and both perturbation kinds reaching.
- Attempt 3: reward **0.6043**. This was lower than the earlier attempt 2.
- Attempt 2: reward **0.6387**. At that point it was better than every earlier attempt.
- Attempt 8: reward **0.6481**. This was lower than the earlier attempt 6.
- Attempt 7: reward **0.6506**. This was lower than the earlier attempt 6.
- Attempt 5: reward **0.6687**. At that point it was better than every earlier attempt.
- Attempt 6: reward **0.6964**. This is the highest reward and is the one to beat.

Attempt 6 combined a qualifying budget of 19.6077 seconds with per-step cost ratio 1.5374 and compute efficiency 0.5781. Attempt 5 is the closest alternative at reward 0.6687, qualifying budget 19.4243, per-step cost ratio 1.0830, and compute efficiency 0.8764.

2. Approach classes tried

The records do not describe algorithm implementations or parameter changes, so exact training approaches cannot be reconstructed. Only outcome-based classes can be carried forward:

- **Fully conforming, perturbation-robust configurations:** Attempts 1–9 and 12–15 all reached the primary target, passed both declared perturbation kinds, had conformance fraction 1.0, rule conformance 1.0, validity 1.0, and no failed checks. Rewards nevertheless ranged widely from 0.3601 to 0.6964. Within this class, attempts 5–8 formed the strongest measured region, with rewards from 0.6481 to 0.6964 and qualifying budgets around 19.4–20.3 seconds. Attempt 6 was best.
- **Budget-bound configurations that did not hold the held-out variant:** Attempts 10 and 11 reached the primary target and the ruleset perturbation, but the held-out-variant kind failed `C-BUDGET-RESPECTED`. Attempt 10 was far over budget and also exceeded the per-step cost ceiling. Attempt 11 substantially reduced the runtime and per-step cost relative to attempt 10, but remained above the declared budget and still failed the same perturbation kind.
- **Later fully conforming but lower-reward configurations:** Attempts 12–15 restored both perturbations after attempts 10–11, but rewards of 0.4034–0.4779 were all plainly lower than the earlier best of 0.6964. Their qualifying budgets were 24.8389–28.1833 seconds, slower than the strongest attempts 5–8.

Across all measured submissions, 28 of 30 perturbation units reached their thresholds. By kind, all 15 ruleset units reached, while 13 of 15 held-out-variant units reached. The two held-out-variant failures were both stopped by `C-BUDGET-RESPECTED`. Thirteen submissions held both perturbations; two did not.

3. Checks that failed

- `C-BUDGET-RESPECTED` failed **twice**:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  
  This repeated failure affected the held-out-variant kind in both records. Whatever was changed between attempts 10 and 11 did not eliminate this check and therefore is not what distinguishes whether the held-out variant passes; the qualifying row still had to move below 31.1 seconds.

- `C-PERTURBATION-REACHED` failed **twice**, in attempts 10 and 11, for the same verifier reason: “1 of 2 declared perturbations reached their own threshold inside their own budget”. Whatever changed between those attempts did not eliminate this failure. In both records, the ruleset kind reached while the held-out-variant kind did not.

- `C-PER-STEP-COST-CEILING` failed **once**, in attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”. Attempt 11 reduced the per-step cost ratio to 1.5815, so this particular check no longer failed there.

No other named checks failed. All primary runs reached their target.

4. Ruled-out directions

- **Do not repeat attempt 10’s high-cost regime unchanged.** Its qualifying row was at 50.5532 seconds against a 31.1-second ceiling, its per-step cost ratio was 4.6619 against a ceiling of 3.0, the held-out variant failed, validity was 0.0, and reward was 0.0000.
- **Do not treat merely reducing attempt 10 toward attempt 11 as sufficient.** Attempt 11 fixed the per-step cost-ceiling violation and reduced qualifying time to 31.6532 seconds, but that was still above 31.1. Consequently, `C-BUDGET-RESPECTED` and `C-PERTURBATION-REACHED` persisted, and reward 0.3385 remained lower than the earlier best.
- **Do not continue the later attempts 12–15 unchanged.** They restored full perturbation success and conformance, but every reward was lower than the earlier best: 0.4779, 0.4070, 0.4201, and 0.4034 respectively. Their 24.8389–28.1833-second qualifying budgets were also well above the roughly 19.4–19.7-second budgets of attempts 5–7.
- **Do not assume compute efficiency alone predicts reward.** Attempt 6 had compute efficiency 0.5781 yet achieved the best reward, 0.6964. Several configurations with compute efficiency 1.0 scored much lower, including attempts 9, 12, 13, and 15.
- **Do not assume lower per-step cost alone predicts reward.** Attempt 4 had per-step cost ratio 0.9534 but reward 0.4776, while attempt 6 had ratio 1.5374 and reward 0.6964. Any optimization must preserve the properties responsible for reaching the target effectively rather than minimizing this ratio in isolation.

5. Open leads

- Recover or reconstruct the configuration represented by attempt 6 and optimize locally around it. It already passed every check, reached the primary target and both perturbation kinds, and produced the best reward of 0.6964.
- Compare attempts 5 and 6 to isolate the change that raised reward from 0.6687 to 0.6964. Attempt 5 had better reported compute efficiency and a lower per-step cost ratio, while attempt 6 still won on reward; preserving attempt 6’s effective behavior while reducing unnecessary cost is the clearest improvement path.
- Use the attempts 5–8 runtime region as the viable operating envelope: all fully conformed, all held both perturbations, and qualifying budgets were 19.4243–20.2729 seconds. Attempts 5 and 6 were the strongest within that region.
- Keep a safety margin below the 31.1-second declared ceiling for every perturbation, especially the held-out-variant kind. Attempt 11’s 31.6532 seconds demonstrates that being close but above the ceiling still fails both `C-BUDGET-RESPECTED` and the aggregate `C-PERTURBATION-REACHED`.
- Preserve the invariant that the ruleset and held-out-variant kinds both reach. The ruleset kind has reached in every measured submission; the held-out-variant kind is the only observed perturbation weakness.

**Exploit:** return to attempt 6’s already successful class and make controlled local improvements. Exploring a structurally different approach is not justified while the best fully conforming approach remains substantially ahead of the later alternatives.
