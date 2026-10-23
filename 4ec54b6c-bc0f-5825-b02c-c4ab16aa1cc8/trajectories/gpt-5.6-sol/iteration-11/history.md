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

    All five attempts since have scored lower than it.
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
  5 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 9 -- reward 0.3601, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 28
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 10 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 51
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget
        C-PER-STEP-COST-CEILING -- per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0

    attempt 11 -- reward 0.3385, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 32
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 2 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (10, 11). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING failed on attempt 10.
    C-PERTURBATION-REACHED has failed on 2 attempts (10, 11). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Measured attempts, ordered from worst to best reward:

- Attempt 10: reward `0.0000`. This was lower than an earlier result. It reached the primary target, but validity was `0.0`, task pass was `0.0`, only one of two perturbation kinds reached its threshold, the qualifying budget was `50.5532` seconds against a `31.1`-second ceiling, and per-step cost was `4.6619` times the seed anchor.
- Attempt 11: reward `0.3385`. This was lower than the best earlier result. It reached the primary target and remained valid, but task pass was `0.0`; only one of two perturbation kinds reached its threshold, with qualifying budget `31.6532` seconds against the `31.1`-second ceiling.
- Attempt 9: reward `0.3601`. This was lower than the best earlier result. It passed all checks and both perturbation kinds, but had qualifying budget `28.3438` seconds, wall clock `31.3334` seconds, and per-step cost ratio `2.0655`.
- Attempt 4: reward `0.4776`. This was lower than the best earlier result. It passed all checks and both perturbation kinds; qualifying budget and wall clock were `28.4730` seconds.
- Attempt 1: reward `0.5513`, the first measured result. It passed all checks and both perturbation kinds, with qualifying budget `22.9821` seconds and per-step cost ratio `0.9652`.
- Attempt 3: reward `0.6043`. This was lower than attempt 2’s earlier reward. It passed all checks and both perturbation kinds, with qualifying budget `19.5786` seconds and per-step cost ratio `1.0323`.
- Attempt 2: reward `0.6387`, better than attempt 1. It passed all checks and both perturbation kinds, with qualifying budget `16.4412` seconds and per-step cost ratio `1.1242`.
- Attempt 8: reward `0.6481`. This was lower than attempt 6’s earlier best. It passed all checks and both perturbation kinds, with qualifying budget `20.2729` seconds and per-step cost ratio `2.0341`.
- Attempt 7: reward `0.6506`. This was lower than attempt 6’s earlier best. It passed all checks and both perturbation kinds, with qualifying budget `19.6597` seconds and per-step cost ratio `1.5308`.
- Attempt 5: reward `0.6687`, better than every earlier attempt at that point. It passed all checks and both perturbation kinds, with qualifying budget `19.4243` seconds and per-step cost ratio `1.0830`.
- Attempt 6: reward `0.6964`, better than every earlier attempt and the highest reward overall. Attempt 6 is the one to beat. It passed all checks and both perturbation kinds, with qualifying budget `19.6077` seconds, compute efficiency `0.5781`, and per-step cost ratio `1.5374`.

All eleven submissions were measured; none produced no measurement.

2. Approach classes tried

The records do not describe algorithm code or hyperparameters, so exact implementation distinctions cannot be reconstructed. The observable approaches fall into two outcome classes:

- Fully conforming, perturbation-robust target-reaching configurations: attempts 1–9 all reached the primary target, passed every named check, had validity and task pass equal to `1.0`, and reached both the held-out-variant and ruleset thresholds. Rewards varied substantially from `0.3601` to `0.6964`, so merely preserving conformance and target attainment is not enough to identify the strongest configuration. Within this class, attempt 6’s measured profile is strongest.
- Budget-risking configurations: attempts 10 and 11 still reached the primary target and the ruleset threshold, but their held-out-variant runs did not reach threshold inside budget. Attempt 10 combined a large budget overrun with excessive per-step cost and became invalid, yielding `0.0000`. Attempt 11 reduced per-step cost to an acceptable level and missed the budget ceiling only narrowly, yielding `0.3385`, but still failed task pass and remained much worse than attempt 6.

Across all perturbation units, 20 of 22 reached threshold. By kind:

- `held_out_variant`: 9 of 11 reached threshold; 2 of 11 failed, both stopped by `C-BUDGET-RESPECTED`.
- `ruleset`: 11 of 11 reached threshold; none failed.
- Aggregate: 20 of 22 perturbation units reached threshold. The only failing kind was `held_out_variant`, and its stopping check was always `C-BUDGET-RESPECTED`.

3. Checks that failed

- `C-BUDGET-RESPECTED` failed twice:
  - Attempt 10: “the qualifying row sits at 50.55317974090576 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - Attempt 11: “the qualifying row sits at 31.65315580368042 on the wall_clock_sec axis, above the declared ceiling of 31.1”.
  - This check has now failed two times. Whatever changed between attempts 10 and 11 is not what is causing the budget failure: both configurations still placed the qualifying row above the same `31.1`-second ceiling. The held-out-variant run was the perturbation kind stopped by this check in both records.
- `C-PERTURBATION-REACHED` failed twice:
  - Attempt 10: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  - Attempt 11: “1 of 2 declared perturbations reached their own threshold inside their own budget”.
  - This check has now failed two times with the identical verifier reason. Whatever changed between attempts 10 and 11 is not what is causing this failure: the held-out variant still missed its threshold within budget, while the ruleset reached its threshold.
- `C-PER-STEP-COST-CEILING` failed once:
  - Attempt 10: “per-step cost is 4.662 times the seed anchor, above the ceiling of 3.0”.
  - Attempt 11 did not repeat this failure: its per-step cost ratio was `1.5815`. Thus the per-step-cost problem was fixed, but fixing it did not fix `C-BUDGET-RESPECTED` or `C-PERTURBATION-REACHED`.

4. Ruled-out directions

- Do not repeat attempt 10’s high-cost, long-running profile. Its per-step cost ratio of `4.6619` exceeded the `3.0` ceiling, its qualifying row occurred at `50.5532` seconds, the held-out variant failed within budget, validity fell to `0.0`, and reward was `0.0000`.
- Do not repeat attempt 11 unchanged. Although it fixed attempt 10’s per-step-cost-ceiling failure, its qualifying row still occurred at `31.6532` seconds, above the `31.1`-second ceiling. The same held-out-variant and aggregate perturbation checks still failed, and reward `0.3385` was lower than the earlier best.
- Do not optimize only for lower per-step cost. Attempt 6 achieved the best reward at per-step cost ratio `1.5374`, while several lower-cost attempts scored worse: attempt 5 at `1.0830` scored `0.6687`, attempt 3 at `1.0323` scored `0.6043`, and attempt 4 at `0.9534` scored `0.4776`.
- Do not optimize only for shorter qualifying time. Attempt 2 qualified fastest at `16.4412` seconds but scored `0.6387`, below attempt 6’s `0.6964` at `19.6077` seconds. Runtime matters at the hard ceiling, but the supplied measurements do not support treating minimum runtime as the reward objective by itself.
- Avoid the general late-qualification region represented by attempts 4, 9, 10, and 11. Their qualifying budgets ranged from `28.3438` to `50.5532` seconds and their rewards ranged only from `0.0000` to `0.4776`, with attempts 10 and 11 crossing the declared budget ceiling. This does not prove qualification time alone caused the low reward, but none of these profiles is competitive with attempt 6.

5. Open leads

- Exploit attempt 6’s approach. It is the one to beat at reward `0.6964`, passed every check, reached both perturbation thresholds, and retained roughly `11.49` seconds of margin beneath the `31.1`-second ceiling.
- Preserve the invariants shared by attempts 1–9: primary target reached, validity `1.0`, task pass `1.0`, rule conformance `1.0`, no red-line crossing, and successful held-out-variant and ruleset perturbations.
- Make controlled changes around attempt 6 rather than moving toward attempts 10–11. Attempt 7 had a very similar qualifying budget (`19.6597` versus `19.6077`) and per-step cost ratio (`1.5308` versus `1.5374`) yet scored only `0.6506`. Therefore, the measurements do not support assuming that those aggregate efficiency figures explain attempt 6’s advantage; preserve attempt 6’s unreported algorithmic details wherever possible.
- Attempt 5 is the strongest lower-cost reference: reward `0.6687`, qualifying budget `19.4243`, and per-step cost ratio `1.0830`. A useful refinement would retain attempt 6’s reward-producing behavior while testing whether some of attempt 5’s lower per-step cost can be recovered without changing target or perturbation success.
- Keep substantial budget margin for the held-out variant. A configuration only `0.5532` seconds over the ceiling still failed both `C-BUDGET-RESPECTED` and `C-PERTURBATION-REACHED`, so merely approaching the ceiling is unsafe.

Call: **exploit**. Refine the already successful attempt 6 profile while preserving all conformance and perturbation guarantees.
