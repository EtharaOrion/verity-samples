# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.8255, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All seven attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.0000   1.000             0 of 2         no              --                
  2        0.8037   1.000             2 of 2         yes             13                
  3        0.8042   1.000             2 of 2         yes             14                
  4        0.8042   1.000             2 of 2         yes             14                
  5 *      0.8255   1.000             2 of 2         yes             14                
  6        0.8059   1.000             2 of 2         yes             13                
  7        0.7994   1.000             2 of 2         yes             14                
  8        0.7843   1.000             2 of 2         yes             17                
  9        0.7891   1.000             2 of 2         yes             14                
  10       0.7393   1.000             2 of 2         yes             17                
  11       0.7997   1.000             2 of 2         yes             17                
  12       0.7443   1.000             2 of 2         yes             17                

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
  6 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 3 -- reward 0.8042, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 6 -- reward 0.8059, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 13
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 10 -- reward 0.7393, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.7997, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 12 -- reward 0.7443, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Twelve graded records, all of which carry a `measurement_status` of either `measured` or `measured_phase_cut`, and all twelve therefore carry a reward. Listed worst to best:

| Rank | Attempt | reward | standing |
|---|---|---|---|
| 1 (worst) | 1 | 0.0000 | first measured attempt |
| 2 | 10 | 0.7393 | worse than an earlier attempt |
| 3 | 12 | 0.7443 | worse than an earlier attempt |
| 4 | 8 | 0.7843 | worse than an earlier attempt |
| 5 | 9 | 0.7891 | worse than an earlier attempt |
| 6 | 7 | 0.7994 | worse than an earlier attempt |
| 7 | 11 | 0.7997 | worse than an earlier attempt |
| 8 | 2 | 0.8037 | better than every earlier attempt |
| 9 | 4 | 0.8042 | worse than an earlier attempt |
| 10 | 3 | 0.8042 | better than every earlier attempt |
| 11 | 6 | 0.8059 | worse than an earlier attempt |
| 12 (best) | 5 | 0.8255 | better than every earlier attempt |

Attempts 4 and 3 both round to 0.8042 at four places; unrounded, attempt 4 (0.80418873) is below attempt 3 (0.80423634), and attempt 4 is explicitly marked worse than an earlier attempt.

**Attempt 5 holds the highest reward, 0.8255. That is the mark to beat.**

Every attempt after 5 came in below it, and the records say so directly: attempts 6, 7, 8, 9, 10, 11 and 12 each carry `standing_against_best_so_far = worse_than_an_earlier_attempt`. Seven consecutive attempts after the peak were regressions, not progress. The immediate successor, attempt 6, fell to 0.8059; the deepest regressions were attempt 10 at 0.7393 and attempt 12 at 0.7443, roughly 0.086 and 0.081 below the peak.

Attempt 1 is the only genuine zero: it is `measured` (as `measured_phase_cut`) and carries `reward: 0.0` with `zero_reason_code: 4`, `task_pass: 0.0`, `primary_target_reached: 0.0`, `conformance_fraction: 0.0`. No record in this set is unmeasured, so there is no attempt here to report as having produced no measurement.

Supporting terms, for orientation. Every attempt from 2 onward has `task_pass: 1.0`, `validity: 1.0`, `rule_conformance: 1.0`, `conformance_fraction: 1.0`, `primary_target_reached: 1.0`, `red_line_crossed: 0.0`, `all_perturbations_held: true`, and an empty `failed_checks`. Attempt 1 had `rule_conformance: 1.0` and `validity: 1.0` but `conformance_fraction: 0.0` and `qualifying_budget: "not-measured"`.

## 2. Approach classes tried

I was given metrics only, not source. The approaches below are grouped by the operating point their exposed terms describe — `per_step_cost_ratio`, `compute_efficiency`, and `wall_clock_sec` / `qualifying_budget` (which are identical for every attempt from 2 on, so the qualifying row is the last row of the run). Records with the same signature are collapsed into one entry.

**Class A — long run that never crossed the threshold (attempt 1).** `wall_clock_sec` 89.98, roughly six times any later attempt, with `per_step_cost_ratio` 1.0194 and `compute_efficiency` 1.0. Despite the cheap per-step cost and the long run, no evaluation row crossed the target in the declared direction, so no qualifying row existed and no budget position could be computed. Reward 0.0000. Whatever changed between attempt 1 and attempt 2 solved this completely and it has never recurred.

**Class B — the ~1.5× per-step-cost, ~13.5s baseline (attempts 2, 3, 4, 7).** `per_step_cost_ratio` clustered at 1.4966 / 1.5320 / 1.4974 / 1.5958, `compute_efficiency` 0.5580–0.6203, qualifying budget 13.49 / 13.66 / 13.66 / 14.10 s. Rewards 0.8037, 0.8042, 0.8042, 0.7994. This is the stable, reliable plateau: four variants inside a 0.005 band. The variation within the class tracks cost ratio inversely — attempt 7, the most expensive per step at 1.5958 and the lowest efficiency at 0.5579, is the worst of the four.

**Class C — driving per-step cost down toward or below parity (attempts 5, 6, 9, 10).** `per_step_cost_ratio` 1.2599, 0.9711, 1.1920, 1.0702; `compute_efficiency` 0.7476, 0.9465, 1.0000, 0.8355. Rewards 0.8255, 0.8059, 0.7891, 0.7393. This class contains the best result (attempt 5) but is not monotone in efficiency: attempt 9 reached the maximum `compute_efficiency` of 1.0 and scored 0.7891, well below attempt 5's 0.7476 efficiency and 0.8255 reward; attempt 6 at 0.9465 efficiency scored 0.8059, also below attempt 5. Cheapening the step past attempt 5's 1.2599 ratio bought efficiency and lost reward. Attempt 10 combined a cheap step (1.0702) with a long budget (16.90 s) and produced the second-worst non-zero reward in the set.

**Class D — longer qualifying budget at baseline cost (attempts 8, 11, 12, and attempt 10 by budget).** Qualifying budget 16.51, 17.00, 16.94, 16.90 s against the 13.4–14.2 s of classes B and C; `per_step_cost_ratio` 1.4960, 1.4791, 1.4930, 1.0702. Rewards 0.7843, 0.7997, 0.7443, 0.7393. Every attempt whose qualifying budget exceeded 16.5 s scored at or below 0.7997, and three of the four scored below 0.785. Every attempt whose budget stayed at or under 14.2 s scored 0.7891 or better. This is the strongest single regularity in the data.

The one clean cross-class reading: with `task_pass`, `validity`, `rule_conformance` and `conformance_fraction` all pinned at 1.0 for attempts 2–12, the spread from 0.7393 to 0.8255 is being produced by the cost/budget terms alone, and short budget is worth more than cheap steps. Attempt 5 sits at the joint sweet spot — budget 13.74 s (short) with cost ratio 1.2599 (moderately cheap, not maximally cheap).

## 3. Checks that failed

Only attempt 1 has a non-empty `failed_checks`. Attempts 2 through 12 each have an empty `failed_checks`, `conformance_fraction: 1.0` and `all_perturbations_held: true`.

At the primary level, attempt 1 failed:

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction".
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". This is a downstream consequence of the line above: with nothing crossing the target there is no row against which a budget can be assessed, which is also why `qualifying_budget` is the literal string `"not-measured"` for that attempt.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget".

Within attempt 1's held-out runs, the same two identifiers recur plus two more:

- **C-TARGET-REACHED** failed on both held-out runs as well as on the primary — three occurrences inside that one record.
- **C-BUDGET-RESPECTED** likewise failed on both held-out runs and on the primary — three occurrences inside that one record.
- **C-LOG-WELL-FORMED** failed on the `ruleset` run only.
- **C-NO-LATCH-CARRYOVER** failed on the `ruleset` run only.

The repetition of C-TARGET-REACHED and C-BUDGET-RESPECTED is confined to attempt 1; neither has failed in any subsequent record, so whatever was changed between attempt 1 and attempt 2 is exactly what fixed them, and nothing changed since has disturbed them. C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER have each failed exactly once, on the `ruleset` run of attempt 1, and have held on every `ruleset` run since.

**Perturbation units.** Each record declares 2 perturbations. Across all twelve records that is 24 held-out runs, one of kind `ruleset` and one of kind `held_out_variant` per record. Aggregate: 22 of 24 reached their threshold, 2 did not, and both failures are in attempt 1. By kind: `ruleset` reached in 11 of 12 records, failing once on C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER together; `held_out_variant` reached in 11 of 12 records, failing once on C-TARGET-REACHED and C-BUDGET-RESPECTED. The `ruleset` kind is the one that failed on the two extra checks — log well-formedness and latch carryover — that the `held_out_variant` kind did not. The runs are not identified beyond their kind and I make no claim that any run in one record is the same run as any run in another.

## 4. Ruled-out directions

**Whatever attempt 1 did — the long-run, ~90-second, nothing-crosses-the-threshold configuration.** Ruled out by `reward: 0.0000` with `zero_reason_code: 4`, `primary_target_reached: 0.0`, `task_pass: 0.0`, and both held-out runs failing C-TARGET-REACHED. It produced no qualifying row at all. Note that this attempt had `compute_efficiency: 1.0` and `per_step_cost_ratio: 1.0194` — the best cost terms in the whole set — and still scored zero. Cost terms are worthless if the target is not crossed.

**Maximising `compute_efficiency` / pushing `per_step_cost_ratio` to parity or below.** Ruled out as a reward-improving direction. Attempt 9 achieved `compute_efficiency: 1.0` and scored 0.7891; attempt 6 achieved 0.9465 and scored 0.8059; attempt 10 achieved 0.8355 with a below-1.1 cost ratio and scored 0.7393. All three are below attempt 5's 0.8255 at efficiency 0.7476. Efficiency is not the objective, and beyond roughly the 1.26 cost ratio of attempt 5 more efficiency actively coincides with less reward.

**Extending the qualifying budget past ~16.5 seconds.** Ruled out. Attempts 8, 10, 11 and 12 all qualified at 16.51–17.00 s and returned 0.7843, 0.7393, 0.7997 and 0.7443 respectively — the four lowest non-zero rewards in the set are exactly these plus attempt 9. No attempt with a budget above 14.2 s has ever beaten any attempt with a budget below 14.2 s except that attempt 11 (17.00 s, 0.7997) edged attempt 7 (14.10 s, 0.7994) by 0.0003, which is noise beside the 0.086 spread. Buying more wall clock has never paid.

**Further re-runs of the class B baseline (cost ratio ≈1.50, budget ≈13.5 s).** Ruled out as a source of new gains, not as a failure. Four attempts (2, 3, 4, 7) landed in a 0.7994–0.8042 band; the class is well-characterised, it is reproducible, and it is capped roughly 0.021 below attempt 5. Re-sampling it again yields information that is already in hand.

**Chasing conformance.** Nothing to fix. `rule_conformance` is 1.0 in every record including attempt 1, and `conformance_fraction`, `validity`, `task_pass`, `primary_target_reached` and `all_perturbations_held` have been perfect in every record from attempt 2 onward, with `red_line_crossed: 0.0` throughout. There is no conformance headroom left; the remaining ~0.17 of reward is in the cost/budget terms.

## 5. Open leads

**Reconstruct attempt 5's operating point exactly and hold it.** Target signature: `per_step_cost_ratio` ≈ 1.2599, `compute_efficiency` ≈ 0.7476, qualifying budget ≈ 13.74 s, all conformance terms at 1.0, both perturbations reached. That combination produced 0.8255 and nothing since has come within 0.019 of it. This is the single most valuable thing the next attempt can do; anything else should be a perturbation around it, not a departure from it.

**Search the narrow gap between attempt 5 and attempt 6 on cost ratio.** The two bracketing points are 1.2599 → 0.8255 and 0.9711 → 0.8059, with attempt 9 at 1.1920 → 0.7891 sitting between them and below both. The reward surface in 0.97–1.26 is not monotone, so a probe at 1.30–1.40 — on the *other* side of attempt 5, between it and the class B cluster at ≈1.50/0.8037 — is the untested region and the more promising one. If reward at ≈1.35 lands between 0.8037 and 0.8255, the optimum is genuinely near 1.26 and there is little left; if it exceeds 0.8255, the peak is somewhere above 1.26 and worth walking up.

**Shorten the qualifying budget below 13.4 s while holding the cost ratio near 1.26.** The shortest budget observed is attempt 6's 13.43 s and the shortest in the winning cost band is attempt 2's 13.49 s. Budget correlates negatively with reward across the whole set, but no attempt has ever qualified under 13.4 s, so the direction is untested at its most favourable end. The constraint is that attempt 1 shows what happens when the run is not allowed to reach the target: reward collapses to zero on C-TARGET-REACHED. Any shortening must keep `primary_target_reached` at 1.0 and both perturbations reaching, and should be backed off immediately if either slips.

**Reduce variance rather than chase a new mean.** The class B cluster spans 0.7994–0.8042 across four attempts at nominally similar operating points, so there is on the order of 0.005 of run-to-run scatter at fixed configuration. Attempt 5's 0.8255 is roughly four times that scatter above the cluster, so it is very unlikely to be noise — but it also means small deltas around 0.8255 should not be over-read.

**Verdict: exploit.** The best approach is identified, its operating point is fully specified by the exposed terms, and it has not been revisited since attempt 5 — instead, seven consecutive attempts explored away from it (cheaper steps, longer budgets) and every one of them regressed. There is no case for a structurally new idea while the known peak has not been reproduced even once. Re-establish attempt 5's configuration first, confirm it reproduces near 0.8255, then probe the cost ratio upward toward 1.35 and the budget downward toward 13.4 s, one variable at a time, abandoning any probe that disturbs `primary_target_reached` or the perturbation outcomes.
