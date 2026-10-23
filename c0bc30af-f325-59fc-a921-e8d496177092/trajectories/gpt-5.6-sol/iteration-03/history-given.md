# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 1 -- reward 0.8630, first measured attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1 *      0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                

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

    attempt 2 -- reward 0.8079, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Two graded submissions exist, both with `measurement_status: "measured"`, so both carry a reward. Ranked worst to best:

- **Attempt 2 — reward 0.8079.** (`reward` = 0.8079100417108986.) `standing_against_best_so_far` is `worse_than_an_earlier_attempt`. This is a regression against attempt 1, not progress: reward fell by 0.0551 from 0.8630 to 0.8079.
- **Attempt 1 — reward 0.8630.** (`reward` = 0.8629926448235584.) `standing_against_best_so_far` is `first_measured_attempt`.

**Attempt 1 holds the highest reward, 0.8630, and it is the score to beat.**

Full measured terms for context, because the reward movement runs opposite to the cost terms and the next attempt needs to know that:

| term | attempt 1 | attempt 2 |
|---|---|---|
| reward | 0.8630 | 0.8079 |
| task_pass | 1.0 | 1.0 |
| validity | 1.0 | 1.0 |
| rule_conformance | 1.0 | 1.0 |
| conformance_fraction | 1.0 | 1.0 |
| primary_target_reached | 1.0 | 1.0 |
| all_perturbations_held | true | true |
| perturbations_declared | 2.0 | 2.0 |
| red_line_crossed | 0.0 | 0.0 |
| zero_reason_code | 0 | 0 |
| compute_efficiency | 0.6784 | 0.7226 |
| per_step_cost_ratio | 1.0723 | 0.9441 |
| wall_clock_sec / qualifying_budget | 76.3367 | 74.2572 |

The important and non-obvious fact: attempt 2 was **cheaper and more efficient on every cost term** — compute_efficiency rose from 0.6784 to 0.7226, per_step_cost_ratio fell from 1.0723 (above reference) to 0.9441 (below reference), wall clock fell from 76.34 s to 74.26 s — and yet reward went **down**. Both attempts passed the task, were fully valid and fully conformant, and reached the primary target. So within the range explored, the reward is not being driven by cost or speed; whatever attempt 2 traded away to get cheaper cost more reward than the cost saving returned. The next attempt should not read "faster and cheaper" as "better."

## 2. Approach classes tried

Only two distinct configurations have been graded, and they differ in a way that is visible in the cost terms rather than in any conformance term.

**Class A — baseline training run that clears the target with per-step cost slightly above the reference (attempt 1, reward 0.8630).** Its signature is `per_step_cost_ratio` = 1.0723, i.e. it spent about 7% more per step than the reference, consumed 76.34 s of the qualifying budget, and scored `compute_efficiency` 0.6784. It reached `primary_target_reached` = 1.0, passed the task, was fully valid and fully rule-conformant, held both declared perturbations, and crossed no red line. This is the best-scoring class and the reference point for everything that follows.

**Class B — cost-reduced / throughput-oriented variant of the same pipeline (attempt 2, reward 0.8079).** Its signature is `per_step_cost_ratio` driven below 1.0 to 0.9441, `compute_efficiency` up to 0.7226, wall clock down to 74.26 s. Everything qualitative stayed identical to class A: task_pass 1.0, validity 1.0, rule_conformance 1.0, conformance_fraction 1.0, primary_target_reached 1.0, all perturbations held, red_line_crossed 0.0, zero_reason_code 0. The only thing that moved in the wrong direction was the reward itself, which lost 0.0551. This class is a measured regression.

There is no third class. Both graded records are functionally the same algorithm evaluated at two points on a cost/quality trade-off, and the cheaper point is the worse point.

## 3. Checks that failed

**No checks failed in either record.** `failed_checks` is the empty list in attempt 1 and the empty list in attempt 2, and it is also empty for every one of the four held-out perturbation runs across the two records. `conformance_fraction` is 1.0 in both, `rule_conformance` is 1.0 in both, `validity` is 1.0 in both, `red_line_crossed` is 0.0 in both, and `zero_reason_code` is 0 in both.

There is therefore no repeated failing check to isolate, and no conformance defect standing between the current work and a higher score. The gap between 0.8079 and 0.8630, and whatever gap remains above 0.8630, is entirely a matter of the graded quantity itself and not of any check being violated. The next attempt should not spend effort hardening conformance: conformance is already saturated and cannot yield further reward.

**Perturbation units.** Each record declared 2 perturbations (`perturbations_declared` = 2.0) and each supplied exactly two held-out runs beside the primary one: one of kind `held_out_variant` and one of kind `seed`. In both records, both runs have `reached: true` and empty `failed_checks`, and `all_perturbations_held` is true.

- By kind, `held_out_variant`: 2 runs across the two records, 2 reached their threshold, 0 stopped by any check.
- By kind, `seed`: 2 runs across the two records, 2 reached their threshold, 0 stopped by any check.
- In aggregate: 4 held-out runs, 4 reached, 0 failures, no check named anywhere.

No kind of held-out run is failing. Robustness to the seed perturbation and to the held-out variant is not the constraint. Note that the runs are not identified in the records, so nothing here should be read as tracking a particular run from attempt 1 into attempt 2; the only supportable statement is per-kind and aggregate, and the statement is that every kind held both times.

## 4. Ruled-out directions

- **Reducing per-step cost below the reference as a route to higher reward — ruled out by attempt 2.** Attempt 2 pushed `per_step_cost_ratio` from 1.0723 down to 0.9441 and `compute_efficiency` from 0.6784 up to 0.7226, and the reward fell from 0.8630 to 0.8079. The cheaper configuration is measurably worse. Do not re-run a variant whose distinguishing property is that it is cheaper per step than attempt 1.
- **Shaving wall-clock time — ruled out on the same evidence.** Wall clock went 76.34 s → 74.26 s and reward went down. Both runs sat inside the qualifying budget with room to spare (`qualifying_budget` equals `wall_clock_sec` in both records, and no budget check fired), so time was never the binding constraint. Trading model quality for 2 seconds is a losing trade at this operating point.
- **Fixing conformance, validity, or rule adherence — ruled out because there is nothing to fix.** `rule_conformance`, `conformance_fraction`, `validity`, and `task_pass` are all 1.0 in both records and `failed_checks` is empty everywhere. Effort here returns nothing.
- **Hardening against the seed or held-out-variant perturbations — ruled out because both kinds already reach their thresholds in every graded record**, 4 for 4 in aggregate, with no check stopping any of them. There is no robustness deficit to repair.
- **Re-submitting attempt 2 unchanged, or any close relative of it — ruled out.** It is a measured regression of 0.0551 against attempt 1 and repeating it changes nothing about why it lost.

## 5. Open leads

- **Restore the attempt-1 configuration exactly as the base and improve from there.** Attempt 1 at 0.8630 is the incumbent. The next attempt starts from a pristine stub and cannot see either earlier submission, so the first job is to reconstruct a class-A run: one that reaches the primary target, passes the task, and is content to spend a little more than reference per step (`per_step_cost_ratio` around 1.07, roughly 76 s) rather than optimising that number down.
- **Spend the available headroom on quality, not on savings.** The evidence says the reward at this operating point rewards whatever attempt 2 gave up. Since neither run was near a budget or red line, the productive direction is to spend *more* compute per step, not less — a larger effective model or wider layers, more optimisation steps or epochs, a longer or better-tuned learning-rate schedule, more careful warmup and decay, an ensemble or weight averaging (EMA / checkpoint averaging) over the final steps, or stronger regularisation and augmentation paid for with extra steps. Attempt 1 already ran above reference cost and still scored best; push further along that axis and measure whether reward continues to climb.
- **Establish the direction of the trade-off with a deliberate probe.** Two points are known: (1.0723 cost → 0.8630) and (0.9441 cost → 0.8079). A third point clearly above 1.0723 would tell the loop whether reward keeps rising with spend or turns over, which is the single most useful thing still unknown. Keep every conformance-relevant behaviour identical to attempt 1 so the probe is clean and the perturbation runs continue to hold.
- **Guard the invariants that are already saturated.** Whatever is changed, preserve: reaching the primary target, passing the task, full rule conformance, and holding both declared perturbations (one `held_out_variant`, one `seed`). Any change that risks these trades a certain 0.8630-class result for nothing, since none of these terms has ever cost a point.
- **Stay inside the qualifying budget.** Both graded runs finished around 74–76 s with no budget check firing. Extra spend is the lead, but it must not push the run past whatever budget ceiling exists; the ceiling has not been probed and its location is unknown from the terms given.

**Call: exploit.** The scoring approach — class A, the attempt-1 configuration at reward 0.8630 — has not been exhausted; it has been probed in exactly one direction, the cheap direction, and that direction lost 0.0551. Exploration is unwarranted while a scoring approach still has an untested axis with a clear prior. Take attempt 1's configuration, spend more per step rather than less, hold every conformance and perturbation property fixed, and try to beat 0.8630. Note for the record that attempt 2 did not repeat a zero-scoring approach — nothing has scored zero here — but it did move along the one axis the data now says moves reward the wrong way, and repeating that move would be neither exploration nor exploitation.
