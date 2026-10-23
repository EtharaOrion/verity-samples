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

    All three attempts since have scored lower than it.
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

    attempt 8 -- reward 0.6481, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.3601, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

All nine submissions were measured, valid, conformant, passed the task, reached the primary target, avoided the red line, and held both declared perturbations.

Worst to best by reward:

- Attempt 9: reward `0.3601`. This was lower than the earlier best. Qualifying budget `28.3438`, wall clock `31.3334` seconds, compute efficiency `1.0000`, and per-step cost ratio `2.0655`.
- Attempt 4: reward `0.4776`. This was lower than the earlier best. Qualifying budget and wall clock `28.4730` seconds, compute efficiency `0.9723`, and per-step cost ratio `0.9534`.
- Attempt 1: reward `0.5513`. This was the first measured attempt. Qualifying budget and wall clock `22.9821` seconds, compute efficiency `1.0000`, and per-step cost ratio `0.9652`.
- Attempt 3: reward `0.6043`. This was lower than the earlier best established by attempt 2. Qualifying budget and wall clock `19.5786` seconds, compute efficiency `0.8281`, and per-step cost ratio `1.0323`.
- Attempt 2: reward `0.6387`. This improved over every earlier attempt. Qualifying budget and wall clock `16.4412` seconds, compute efficiency `0.8426`, and per-step cost ratio `1.1242`.
- Attempt 8: reward `0.6481`. Despite exceeding attempts 1–4, this was lower than the earlier best established by attempt 6. Qualifying budget and wall clock `20.2729` seconds, compute efficiency `0.4238`, and per-step cost ratio `2.0341`.
- Attempt 7: reward `0.6506`. Despite exceeding attempts 1–4 and 8, this was lower than the earlier best established by attempt 6. Qualifying budget and wall clock `19.6597` seconds, compute efficiency `0.6084`, and per-step cost ratio `1.5308`.
- Attempt 5: reward `0.6687`. This improved over every earlier attempt through attempt 4. Qualifying budget and wall clock `19.4243` seconds, compute efficiency `0.8764`, and per-step cost ratio `1.0830`.
- Attempt 6: reward `0.6964`. This is the highest reward and is the one to beat. Qualifying budget and wall clock `19.6077` seconds, compute efficiency `0.5781`, and per-step cost ratio `1.5374`.

2. Approach classes tried

The records do not describe source-code changes or algorithm structures, so exact training approaches cannot be reconstructed. The measurable operating classes are:

- Lower per-step-cost configurations, attempts 1–5: per-step cost ratios ranged from `0.9534` to `1.1242`. Rewards varied widely from `0.4776` to `0.6687`. Attempt 5 was strongest in this class at `0.6687`; it combined a qualifying budget of `19.4243`, compute efficiency of `0.8764`, and per-step cost ratio of `1.0830`.
- Moderately higher per-step-cost configurations, attempts 6–7: ratios were about `1.53`, qualifying budgets were about `19.6`, and rewards were `0.6964` and `0.6506`. Attempt 6 was the overall best. Attempt 7 had a slightly lower per-step cost ratio and higher compute efficiency than attempt 6 but nevertheless had a lower reward, so those isolated metric improvements did not improve the grade.
- Very high per-step-cost configurations, attempts 8–9: ratios exceeded `2.03`. Attempt 8 remained competitive at `0.6481`, but attempt 9 fell to the worst reward, `0.3601`, alongside the largest wall clock and a much larger qualifying budget. High per-step cost alone therefore did not reliably improve reward.

Across all approaches, perturbation performance was perfect in aggregate: all 18 perturbation units reached their thresholds. All nine `held_out_variant` units reached, and all nine `ruleset` units reached. No perturbation run was stopped by any check.

3. Checks that failed

No named checks failed in any submission. Every `failed_checks` list was empty.

For every attempt, validity, task pass, rule conformance, and conformance fraction were all `1.0000`; the primary target was reached; the red line was not crossed; and all perturbations held. There is therefore no repeated failed check to diagnose or attribute to unchanged code.

4. Ruled-out directions

- Do not optimize compute efficiency in isolation. Attempts 1 and 9 both reported compute efficiency `1.0000`, yet their rewards were only `0.5513` and `0.3601`, below the best attempt’s `0.6964`.
- Do not simply maximize per-step cost. Attempt 6 succeeded with ratio `1.5374`, but pushing above `2.03` produced only `0.6481` in attempt 8 and the worst result, `0.3601`, in attempt 9.
- Do not assume a slightly cheaper or more compute-efficient version of the attempt-6 operating region is automatically better. Attempt 7 had a slightly lower per-step cost ratio (`1.5308` versus `1.5374`) and higher compute efficiency (`0.6084` versus `0.5781`) but scored lower: `0.6506` versus `0.6964`.
- Do not trade away the roughly `19.4`–`19.7` qualifying-budget region without a concrete benefit. The three highest rewards came from attempts 5–7 in that narrow region. Larger qualifying budgets in attempts 1, 4, and 9 produced materially lower rewards. This is an observed association, not evidence that qualifying budget alone caused the differences.
- Repeating an earlier configuration without changing the factor responsible for its reward would not be useful. The supplied records do not identify code-level changes, so they do not support claiming which specific implementation choice caused any score.

5. Open leads

- Exploit attempt 6, the `0.6964` result and current one to beat. Preserve its full validity, task pass, conformance, primary-target success, red-line safety, and perturbation robustness.
- Compare the implementation choices behind attempts 6 and 7. Their qualifying budgets and per-step cost ratios were very close, yet attempt 7 lost `0.0458` reward. The useful lead is whatever substantive algorithmic difference separated them, not merely compute efficiency or per-step cost.
- Also compare attempts 5 and 6. Attempt 5 achieved `0.6687` with substantially higher compute efficiency and lower per-step cost, while attempt 6 gained another `0.0277` reward. A controlled hybrid may retain the reward-producing behavior of attempt 6 while recovering some of attempt 5’s efficiency.
- Keep the qualifying budget near the empirically strongest region around `19.4`–`19.7` unless a controlled change demonstrates a reward gain.
- Continue testing both perturbation kinds on every revision. They currently provide no obstacle: `held_out_variant` reached in 9/9 measured submissions and `ruleset` reached in 9/9.

Call: **exploit**—refine attempt 6 or isolate the one substantive difference that made it outperform attempts 5 and 7, rather than switching to a structurally unrelated approach.
