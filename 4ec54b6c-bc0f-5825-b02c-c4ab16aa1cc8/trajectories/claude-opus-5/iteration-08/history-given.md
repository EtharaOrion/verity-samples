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

    All two attempts since have scored lower than it.
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
  3 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 7 -- reward 0.7994, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Seven graded submissions. Every one of them carries a `measurement_status` of either `measured` or `measured_phase_cut`, and every one carries a `reward`, so there is no record here that failed to produce a measurement. Attempt 1's 0.0000 is a genuine measured zero (`zero_reason_code` 4), not an absent measurement.

Ordered worst to best by reward:

- **Attempt 1 — reward 0.0000.** `measured_phase_cut`. `task_pass` 0, `primary_target_reached` 0, `conformance_fraction` 0.0, `qualifying_budget` "not-measured", both declared perturbations failed. `red_line_crossed` 0, `validity` 1.0, `rule_conformance` 1.0, `compute_efficiency` 1.0, `per_step_cost_ratio` 1.0194, wall clock 89.9778 s. Standing: `first_measured_attempt`.
- **Attempt 7 — reward 0.7994.** `measured`. All checks held, both perturbations held. `compute_efficiency` 0.5579, `per_step_cost_ratio` 1.5958, `qualifying_budget`/wall clock 14.1032 s. Standing: `worse_than_an_earlier_attempt`. This is a regression — the lowest reward of any conforming attempt, and the highest per-step cost and longest wall clock of the conforming set.
- **Attempt 2 — reward 0.8037.** `measured_phase_cut`, all checks held, both perturbations held. `compute_efficiency` 0.6203, `per_step_cost_ratio` 1.4966, wall clock 13.4877 s. Standing at the time: `better_than_every_earlier_attempt`.
- **Attempt 4 — reward 0.8042** (0.80418873 unrounded). `measured`, all checks held. `compute_efficiency` 0.5835, `per_step_cost_ratio` 1.4974, wall clock 13.6584 s. Standing: `worse_than_an_earlier_attempt` — it is a regression against attempt 3, by about 5e-5, i.e. the two are effectively indistinguishable and attempt 4 is on the wrong side of that.
- **Attempt 3 — reward 0.8042** (0.80423634 unrounded). `measured`, all checks held. `compute_efficiency` 0.6051, `per_step_cost_ratio` 1.5320, wall clock 13.6621 s. Standing: `better_than_every_earlier_attempt`.
- **Attempt 6 — reward 0.8059.** `measured`, all checks held. `compute_efficiency` 0.9465 (the highest recorded among conforming runs), `per_step_cost_ratio` 0.9711 (the only conforming run at or below the reference cost), wall clock 13.4266 s (the shortest conforming run). Standing: `worse_than_an_earlier_attempt` — a regression against attempt 5 despite strictly better compute numbers.
- **Attempt 5 — reward 0.8255. This is the highest reward recorded and the one to beat.** `measured`, all checks held, both perturbations held. `compute_efficiency` 0.7476, `per_step_cost_ratio` 1.2599, `qualifying_budget`/wall clock 13.7398 s. Standing: `better_than_every_earlier_attempt`.

The two attempts that came after the best one (6 and 7) both scored lower than it. Nothing since attempt 5 has improved on it.

# 2. Approach classes tried

The measured terms record each submission's metrics, not its source, so these classes are defined by their measured signatures. Group them as follows; two records with the same signature are one entry.

**Class A — the non-conforming first cut (attempt 1).** Ran 89.9778 s of wall clock, roughly 6.6× the wall clock of every later attempt, and never crossed the primary threshold in the declared direction. `conformance_fraction` 0.0, no qualifying row at all, so no budget position existed to evaluate. Both perturbation runs failed too. Notably its `compute_efficiency` reads 1.0 and its `per_step_cost_ratio` 1.0194 — these are not evidence of a good solution, because with no qualifying row they describe an evaluation that never reached the scored regime. This class scored 0.0000 and was abandoned after one attempt.

**Class B — conforming, per-step cost well above reference (attempts 2, 3, 4, 7).** All hold every check, reach the primary target, hold both perturbations, finish in 13.49–14.10 s of wall clock, and sit in a per-step cost band of roughly 1.50–1.60 with compute efficiency 0.558–0.620. Rewards 0.7994, 0.8037, 0.8042, 0.8042 — a spread of under 0.005 across four submissions. Within this class, higher cost ratio tracks lower reward: attempt 7 at ratio 1.5958 is the worst conforming result; attempts 2 and 4 at ratio ≈1.497 and attempt 3 at 1.5320 are bunched together within noise.

**Class C — conforming, per-step cost at or below reference (attempt 6).** Ratio 0.9711, efficiency 0.9465, the shortest wall clock at 13.4266 s. Reward 0.8059. This class proved the cost floor is reachable while holding every check, but it did not translate into the top reward.

**Class D — conforming, intermediate per-step cost (attempt 5).** Ratio 1.2599, efficiency 0.7476, wall clock 13.7398 s. Reward 0.8255, clear of every other attempt by about 0.020. This is the single best-performing class and it has been sampled exactly once.

The critical cross-class observation: reward is **not** monotone in `compute_efficiency`. Class C has the best efficiency by a wide margin (0.9465 vs 0.7476) and a worse reward (0.8059 vs 0.8255). Meanwhile efficiency across the conforming set spans 0.558 to 0.946 while reward spans only 0.7994 to 0.8255. Cost is a real but weak lever, and something else — a task-quality term not itemised in these fields, since `task_pass`, `validity`, `rule_conformance`, `conformance_fraction` and `red_line_crossed` are pinned at their ideal values for all six conforming runs — accounts for attempt 5's 0.020 lead.

# 3. Checks that failed

All check failures are confined to attempt 1. Attempts 2 through 7 each report an empty `failed_checks` and empty `failed_checks` on both perturbation units. No named check has failed in more than one record, so there is no recurring conformance finding to isolate; whatever changed between attempt 1 and attempt 2 cleared all five named checks at once and they have stayed clear across six subsequent submissions.

On the primary run of attempt 1:

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction".
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". This is a consequence of the previous failure, not an independent budget overrun: with nothing qualifying, there was nothing to position against the budget.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget".

Counting the perturbation runs as well, within attempt 1 **C-TARGET-REACHED** failed three times (primary run plus both held-out runs) and **C-BUDGET-RESPECTED** failed three times (same three runs). **C-PERTURBATION-REACHED** failed once, on the primary run. **C-LOG-WELL-FORMED** and **C-NO-LATCH-CARRYOVER** each failed once, and only on the ruleset-kind run — the verifier supplied no separate reason strings for the per-unit checks beyond the identifiers.

# 4. Ruled-out directions

**The attempt-1 configuration in its entirety.** It scored 0.0000 with `zero_reason_code` 4 and `conformance_fraction` 0.0. Its wall clock of 89.9778 s against 13.4–14.1 s for everything that scored suggests a fundamentally different and far slower execution shape that never produced a qualifying evaluation row. Do not reconstruct it. Anything resembling it fails C-TARGET-REACHED on the primary run and on both held-out runs.

**Maximising compute efficiency / minimising per-step cost as the primary lever.** Attempt 6 pushed `per_step_cost_ratio` to 0.9711 and `compute_efficiency` to 0.9465 — the best cost profile anywhere in the record — and returned 0.8059, below attempt 5's 0.8255. Driving cost to the floor is not what the reward is paying for, and pursuing it further is ruled out as a route to first place.

**Raising per-step cost above roughly 1.5.** Attempt 7 sat at ratio 1.5958 with wall clock 14.1032 s and produced 0.7994, the worst conforming reward. Spending more per step buys nothing.

**Further sampling of the 1.49–1.53 cost band.** Attempts 2, 3 and 4 all live there and returned 0.8037, 0.8042 and 0.8042. Attempt 4's ratio of 1.4974 was essentially attempt 2's 1.4966 and its reward differs from attempt 3's by roughly 5e-5 in the losing direction. That band is exhausted; differences inside it are indistinguishable from noise and none of it approaches 0.8255.

# 5. Open leads

**Rebuild the attempt-5 operating point.** It holds the highest reward, 0.8255, and the next attempt starts from a pristine stub, so it will not have that code. Its measured signature is the specification to aim at: `per_step_cost_ratio` 1.2599, `compute_efficiency` 0.7476, wall clock 13.7398 s, every check held, both perturbation runs held. Land in the intermediate cost band around 1.25–1.30 rather than at the ≈1.50 plateau of class B or the ≈0.97 floor of class C. That band has been sampled once and it is where the only above-0.81 result lives.

**Find the quality lever that is not compute cost.** Across the six conforming attempts, `task_pass`, `validity`, `rule_conformance`, `conformance_fraction` and `red_line_crossed` are constant at their ideal values, and `qualifying_budget` equals wall clock and varies by only 0.68 s. Efficiency varies by a factor of 1.7 while reward varies by 0.026. Attempt 5 therefore beat attempt 6 on something these fields do not name — most plausibly the margin or quality of the qualifying evaluation row rather than its cost. Vary that, holding cost near 1.26, and measure whether reward moves more than the ~0.005 that cost tuning has been worth.

**Keep the wall clock in the 13.4–13.8 s window.** The best result sat at 13.7398 s; the worst conforming result was the longest at 14.1032 s. There is no evidence that shortening below 13.43 s helps (attempt 6 was the shortest and did not win), and evidence that lengthening past 14 s hurts.

**Preserve the two ruleset-specific behaviours.** C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER failed only on the ruleset-kind held-out run in attempt 1, and only there — the held-out-variant run of the same attempt did not fail them. Whatever the conforming attempts do about log formatting and about clearing latched state between runs, keep it. These two checks are ruleset-sensitive and will not be exercised by the primary run alone.

**Perturbation-unit picture, by kind and in aggregate.** Each record declares two perturbations and reports exactly two units, one of kind `ruleset` and one of kind `held_out_variant`. Across all seven records that is 14 unit runs: 12 reached their threshold and 2 did not, both of the failures inside attempt 1 — one ruleset run and one held-out-variant run. By kind: `ruleset` reached in six of seven records, failing once on C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER; `held_out_variant` reached in six of seven records, failing once on C-TARGET-REACHED and C-BUDGET-RESPECTED. `all_perturbations_held` is true for attempts 2 through 7. The units are not identified across records, so nothing here should be read as one particular run recurring. The generalisation gap is currently closed and is not the binding constraint on reward.

**Call: exploit.** The conforming class is the only class that scores, and inside it one operating point — attempt 5's intermediate-cost configuration — leads the field by 0.020 while the cost extremes on either side of it (attempt 6 below, attempt 7 above) both regressed. The task is to re-derive that operating point and then push on the non-cost quality term, not to introduce a structurally different algorithm. Note for the record that attempts 3, 4, 6 and 7 collectively re-sampled the cost dimension four times for a total spread of 0.007 and two outright regressions; repeating that sweep again without changing the quality term would be neither exploit nor explore.
