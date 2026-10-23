# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 3 -- reward 0.8657, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3 *      0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                

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

    attempt 1 -- reward 0.8630, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 2 -- reward 0.8079, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.7740, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Four graded submissions, all with `measurement_status: "measured"`, so all four carry a reward. Listed worst to best:

- **Attempt 4 — reward 0.7740** (0.7740073037731968). `standing_against_best_so_far: worse_than_an_earlier_attempt`. This is a regression, not progress: it is the lowest reward of the four despite having by far the highest `compute_efficiency` (0.9681) and the lowest `per_step_cost_ratio` (0.6934).
- **Attempt 2 — reward 0.8079** (0.8079100417108986). `standing_against_best_so_far: worse_than_an_earlier_attempt`. Lower than attempt 1, which preceded it. A regression.
- **Attempt 1 — reward 0.8630** (0.8629926448235584). `standing_against_best_so_far: first_measured_attempt` — the baseline the rest are measured against.
- **Attempt 3 — reward 0.8657** (0.8657110107695606). `standing_against_best_so_far: better_than_every_earlier_attempt`. **Attempt 3 holds the highest reward and is the one to beat.**

The margin at the top is thin: attempt 3 beats attempt 1 by 0.0027. Attempt 4 sits 0.0917 below attempt 3.

Common to all four records: `task_pass: 1.0`, `validity: 1.0`, `rule_conformance: 1.0`, `conformance_fraction: 1.0`, `primary_target_reached: 1.0`, `red_line_crossed: 0.0`, `zero_reason_code: 0`, `all_perturbations_held: true`, `perturbations_declared: 2.0`. No attempt has ever failed to reach the primary target, and no attempt has ever been zeroed.

The varying quantities, per attempt (ordinal: `compute_efficiency` / `per_step_cost_ratio` / `wall_clock_sec`, which equals `qualifying_budget` in every record):

- Attempt 1: 0.6784 / 1.0723 / 76.3367
- Attempt 2: 0.7226 / 0.9441 / 74.2572
- Attempt 3: 0.6922 / 0.9835 / 74.3681
- Attempt 4: 0.9681 / 0.6934 / 73.7442

Wall clock is essentially flat across all four (73.74 s to 76.34 s, a spread of 2.6 s), so total runtime is not what separates them.

# 2. Approach classes tried

The measured terms supplied do not record the source of any submission, so the approaches can only be characterised by the cost/efficiency signature each produced. Grouped by that signature, three distinct classes were exercised:

**Class A — high per-step cost, low compute efficiency (attempts 1 and 3).** `per_step_cost_ratio` at or near 1.0 (1.0723 and 0.9835), `compute_efficiency` in the 0.68–0.69 band. These two are the top two rewards (0.8630 and 0.8657). They are effectively the same class: attempt 3 is a slight refinement of the attempt-1 operating point, trading a little per-step cost (1.0723 → 0.9835) for a little efficiency (0.6784 → 0.6922) and gaining 0.0027 of reward.

**Class B — mildly cheapened per step (attempt 2).** `per_step_cost_ratio` 0.9441, `compute_efficiency` 0.7226. Cheaper and more efficient than attempt 1, yet reward fell from 0.8630 to 0.8079, a loss of 0.0551.

**Class C — aggressively cheapened per step (attempt 4).** `per_step_cost_ratio` 0.6934, `compute_efficiency` 0.9681. The most efficient run by a wide margin and the worst reward of the four, 0.7740.

The ordering across these classes is monotone and is the central empirical finding of the work so far: as `per_step_cost_ratio` falls and `compute_efficiency` rises, reward falls. 0.6934 → 0.7740; 0.9441 → 0.8079; 0.9835 → 0.8657; 1.0723 → 0.8630. The single non-monotone point is the very top (attempt 1 at 1.0723 is marginally below attempt 3 at 0.9835), which suggests the optimum sits near `per_step_cost_ratio` ≈ 0.98–1.07 rather than at either extreme. Reward here is clearly dominated by a quality term, not by efficiency; efficiency gains have been paid for out of that quality term at an unfavourable exchange rate every time.

# 3. Checks that failed

None. `failed_checks` is an empty list in all four records, and there is no named check to report. No attempt has a check that failed once, let alone repeatedly, so there is no recurring conformance finding to isolate.

The per-record conformance evidence is uniformly clean: `rule_conformance: 1.0` and `conformance_fraction: 1.0` in all four, `validity: 1.0` in all four, `task_pass: 1.0` in all four, `red_line_crossed: 0.0` in all four, `zero_reason_code: 0` in all four.

Held-out runs (`perturbation_units`): every record declares 2.0 perturbations and reports exactly two units, one of kind `held_out_variant` and one of kind `seed`. In all four records both units have `reached: true` and an empty `failed_checks`, and `all_perturbations_held` is `true`. By kind: the `held_out_variant` kind reached its threshold on all four occasions it was run; the `seed` kind reached its threshold on all four occasions it was run. In aggregate, eight held-out runs, eight thresholds reached, zero stopped by any check. No kind of held-out run is failing, and no check has stopped one.

The gap to a higher reward is therefore entirely in the graded quality/efficiency trade-off, not in conformance or robustness. Nothing is being lost to a check.

# 4. Ruled-out directions

**Maximising `compute_efficiency` / driving `per_step_cost_ratio` down.** Ruled out by attempt 4, which pushed `per_step_cost_ratio` to 0.6934 and `compute_efficiency` to 0.9681 — the best efficiency figures seen — and returned 0.7740, the worst reward seen. Ruled out again, more mildly, by attempt 2 at `per_step_cost_ratio` 0.9441 / efficiency 0.7226, which returned 0.8079, below attempt 1's 0.8630 at a higher per-step cost. Two independent points on the same axis, both worse. Cheapening the per-step computation is not how reward is won on this task.

**Chasing wall-clock reduction.** Ruled out as a lever, not as harmful: total runtime moved only from 76.34 s to 73.74 s across the whole set while reward moved by 0.0917, and `qualifying_budget` equals `wall_clock_sec` in every record with no budget ever exceeded. There is no evidence of a runtime ceiling being approached, so time saved buys nothing directly and, per the point above, the quality cost of saving it is real.

**Conformance and robustness hardening.** Ruled out as a source of gain. All four attempts already score 1.0 on `rule_conformance`, `conformance_fraction`, `validity`, `task_pass` and `primary_target_reached`, with both the `held_out_variant` and `seed` runs holding every time. There is no headroom on these terms; work spent here cannot raise the reward.

Note for the record: no attempt has scored zero and no attempt has produced no measurement, so there is no zero-scoring approach that earlier work was repeating unchanged.

# 5. Open leads

1. **Rebuild the attempt-3 operating point and refine around it.** It is the best measurement (0.8657) and its signature is `per_step_cost_ratio` 0.9835, `compute_efficiency` 0.6922, wall clock 74.37 s. Since the next attempt starts from a pristine stub, the first job is to land back in that band — per-step cost near 1.0, compute efficiency near 0.69 — rather than anywhere cheaper.

2. **Probe the interval between attempt 3 and attempt 1 on the cost axis, and just above it.** The four points make reward a rising function of `per_step_cost_ratio` from 0.6934 up to 0.9835, then a slight fall by 1.0723. The peak is bracketed between roughly 0.98 and 1.07. Trying a point in the 1.00–1.05 range, or slightly above 1.07 to confirm the turn is real, is the cheapest informative experiment available. Attempt 1 vs attempt 3 differ by only 0.0027, which is small enough that the apparent turn could be noise; a third point in that region would settle it.

3. **Spend the slack budget on quality.** Wall clock has never exceeded 76.34 s and `qualifying_budget` has always equalled it with no overrun flagged, while every conformance and perturbation term is saturated at its maximum. The evidence says extra per-step work is rewarded. Increasing the work done per step — more capacity, more iterations, less aggressive approximation, whatever raised the cost ratio in attempts 1 and 3 — is the direction with support in the data, provided the run still completes in the same rough time envelope.

4. **Verify variance before concluding anything from a 0.0027 gap.** Attempts 1 and 3 are separated by less than a third of a percent of reward. If a re-run of the attempt-3 configuration reproduces near 0.8657, the operating point is real and worth refining; if it lands nearer 0.8630 or below, the top of the range is flat and effort should go to lead 3 instead.

**Call: exploit.** The best approach class (high per-step cost, low compute efficiency — attempts 1 and 3) is still improving, no check has ever failed, and the failure mode of every regression is understood and single-axis: efficiency was bought at the cost of reward. The move is to reproduce the attempt-3 configuration, beat 0.8657, and push per-step work up rather than down. Explore is not warranted while the scoring class still has an unexplored, well-bracketed optimum next to it.
