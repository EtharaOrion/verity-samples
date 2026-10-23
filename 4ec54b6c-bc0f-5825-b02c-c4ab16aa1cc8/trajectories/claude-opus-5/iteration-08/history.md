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

    All three attempts since have scored lower than it.
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

    attempt 8 -- reward 0.7843, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Eight graded records, every one of them carrying a reward. Listed worst to best:

| Rank | Attempt | reward | measurement_status | Notes |
|---|---|---|---|---|
| 1 (worst) | 1 | 0.0000 | measured_phase_cut | zero_reason_code 4; task_pass 0, primary_target_reached 0; three primary checks failed |
| 2 | 8 | 0.7843 | measured | wall_clock 16.5068 s, the longest of any run; per_step_cost_ratio 1.4960 |
| 3 | 7 | 0.7994 | measured | per_step_cost_ratio 1.5958, the highest of any run; wall_clock 14.1032 s |
| 4 | 2 | 0.8037 | measured_phase_cut | per_step_cost_ratio 1.4966; wall_clock 13.4877 s |
| 5 | 4 | 0.8042 | measured | 0.8041887 exactly; per_step_cost_ratio 1.4974; wall_clock 13.6584 s |
| 6 | 3 | 0.8042 | measured | 0.8042363 exactly, a hair above attempt 4; per_step_cost_ratio 1.5320 |
| 7 | 6 | 0.8059 | measured | best compute_efficiency of all runs, 0.9465; per_step_cost_ratio 0.9711; shortest wall_clock 13.4266 s |
| 8 (best) | 5 | 0.8255 | measured | compute_efficiency 0.7476; per_step_cost_ratio 1.2599; wall_clock 13.7398 s |

**Attempt 5 holds the highest reward, 0.8255. That is the attempt to beat.**

Every record here is measured; none is missing a measurement, so nothing in this set needs to be reported as "no measurement". Attempts 1 and 2 carry status `measured_phase_cut` rather than plain `measured`, but both produced rewards and are reported as such.

Directional facts that must not be softened:

- Attempt 4 (0.8042) is **worse than an earlier attempt**; `standing_against_best_so_far` says so directly.
- Attempt 6 (0.8059) is **worse than an earlier attempt** — specifically it fell below attempt 5's 0.8255, a drop of 0.0196, despite having the best compute_efficiency and lowest wall clock of the whole set.
- Attempt 7 (0.7994) is **worse than an earlier attempt**, down 0.0261 from the best.
- Attempt 8 (0.7843) is **worse than an earlier attempt**, and is the worst of the seven scoring runs, down 0.0412 from the best.

So the last three graded attempts all regressed against attempt 5. The trajectory after attempt 5 is downward, not upward.

Supporting terms held constant across all eight: `validity` 1.0, `rule_conformance` 1.0, `red_line_crossed` 0.0, `perturbations_declared` 2.0. Attempts 2–8 all have `conformance_fraction` 1.0, `task_pass` 1.0, `primary_target_reached` 1.0, `all_perturbations_held` true, and an empty `failed_checks`. In every measured row `qualifying_budget` equals `wall_clock_sec` to the digit, so the budget position and the wall clock are the same quantity.

# 2. Approach classes tried

The records supply numeric fingerprints (per-step cost ratio, compute efficiency, wall clock) rather than source, so the classes below are grouped by those fingerprints. Two records with the same fingerprint and the same outcome are one entry.

**Class A — the non-converging first cut (attempt 1).** The only approach that never reached the primary target. `per_step_cost_ratio` 1.0194 and `compute_efficiency` 1.0 — i.e. it was cheap per step, but no evaluation row ever crossed the threshold in the declared direction, so cheapness bought nothing. Both perturbation runs also failed, and one of them additionally failed log formatting and latch-carryover checks. Cost 89.98 s of wall clock while producing no qualifying row. This class is dead as configured; see section 4.

**Class B — the ~1.50 cost-ratio baseline (attempts 2, 3, 4, 8).** Four records cluster tightly at `per_step_cost_ratio` 1.4960–1.5320 and `compute_efficiency` 0.5835–0.6242. All pass every check and hold both perturbations. Rewards 0.8037, 0.8042, 0.8042, 0.7843. Attempts 2, 3 and 4 are effectively the same point measured three times (cost ratios 1.4966 / 1.5320 / 1.4974, wall clocks 13.49 / 13.66 / 13.66 s, rewards spanning 0.0006). Attempt 8 shares the cost ratio (1.4960) but ran 16.51 s — nearly 3 s longer — and lost 0.0199 of reward relative to attempt 3. This class is the plateau the loop kept returning to.

**Class C — the high-cost excursion (attempt 7).** `per_step_cost_ratio` pushed up to 1.5958, `compute_efficiency` down to 0.5579, wall clock 14.10 s, reward 0.7994. Strictly worse than class B on every axis. Moving cost per step *up* from the 1.50 plateau loses reward.

**Class D — the aggressively cheap variant (attempt 6).** `per_step_cost_ratio` 0.9711 (the only sub-1.0 figure among the scoring runs), `compute_efficiency` 0.9465, wall clock 13.43 s — the cheapest and fastest scoring run in the set. Reward 0.8059. It beat the whole of class B, but it lost 0.0196 to attempt 5. This is the single most informative result after attempt 5: driving cost per step to its minimum does **not** maximise reward.

**Class E — the intermediate cost point (attempt 5), the current best.** `per_step_cost_ratio` 1.2599, `compute_efficiency` 0.7476, wall clock 13.74 s, reward 0.8255. It sits between class D (0.97) and class B (1.50) on cost ratio and beats both. Its wall clock is *not* the lowest in the set, so it did not win on budget; it won on the cost-ratio position.

Read together, classes B, C, D and E trace an interior optimum in `per_step_cost_ratio`: reward rises going from 1.60 → 1.50 → 1.26, then falls again going 1.26 → 0.97. The peak observed so far is at 1.26.

# 3. Checks that failed

All check failures in the entire set are confined to attempt 1. No named check appears in more than one record.

Primary-level failures on attempt 1:

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction".
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". This is a consequence of the previous failure, not an independent budget overrun: with nothing qualifying, there is no budget position to evaluate. `qualifying_budget` is recorded as "not-measured" for this attempt.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget".

Perturbation-level failures on attempt 1, by kind:

- The **ruleset** run failed **C-LOG-WELL-FORMED**, **C-TARGET-REACHED**, **C-BUDGET-RESPECTED** and **C-NO-LATCH-CARRYOVER**. Note that C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER are unique to this run and appear nowhere else in the set — the ruleset kind exposed a log-formatting defect and a latch that carried over between runs, neither of which the primary run surfaced.
- The **held_out_variant** run failed **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**, the same convergence-then-no-budget-position pair as the primary.

Because no check failed in a second record, there is no persistent check to attribute across attempts. The corollary is the useful one: whatever was changed between attempt 1 and attempt 2 fixed all of C-TARGET-REACHED, C-BUDGET-RESPECTED, C-PERTURBATION-REACHED, C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER at once, and none of them has recurred through six subsequent attempts. That fix must be preserved verbatim — in particular the log emission and the between-run state reset that cleared C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER on the ruleset perturbation, since those two checks were never exercised by the primary run and a regression in them would not show up in primary metrics.

# 4. Ruled-out directions

- **The attempt-1 configuration as a whole (class A).** Ruled out by C-TARGET-REACHED: no evaluation row crossed the threshold in the declared direction, so task_pass 0, primary_target_reached 0, reward 0.0000, zero_reason_code 4. Its `compute_efficiency` of 1.0 and cost ratio of 1.0194 are not evidence in its favour — those figures were earned by a run that never qualified.
- **Reading low per-step cost as a proxy for reward.** Ruled out twice over. Attempt 1 had cost ratio 1.0194 and scored 0.0000. Attempt 6 had cost ratio 0.9711 and compute_efficiency 0.9465 — the best cost figures of any scoring run, with the shortest wall clock — and still scored 0.8059, below attempt 5's 0.8255. Pushing cost per step below roughly 1.2 costs more reward than it saves.
- **Raising per-step cost above the ~1.50 plateau.** Ruled out by attempt 7: cost ratio 1.5958 produced 0.7994, worse than every class-B point at ~1.50 except attempt 8. There is no evidence of reward on the high-cost side.
- **Spending more wall clock at a fixed cost ratio.** Ruled out by attempt 8: at cost ratio 1.4960, essentially identical to attempts 2 and 4, it ran 16.5068 s instead of ~13.5–13.7 s and returned 0.7843, the worst scoring result. Roughly 2.85 extra seconds bought a 0.0199 loss against attempt 3 at the same cost ratio. Wall clock and cost ratio penalise reward independently.
- **Re-measuring the ~1.50 plateau (class B) again.** Attempts 2, 3 and 4 pin that point to within 0.0006 of reward (0.8037, 0.8042, 0.8042). It is well characterised and it is 0.021 below the best. Another sample there adds nothing.

# 5. Open leads

**The dominant lead: bracket the interior optimum in `per_step_cost_ratio` between 0.97 and 1.50.** The four observed points are (0.9711 → 0.8059), (1.2599 → 0.8255), (1.4966 → 0.8037), (1.5958 → 0.7994). The curve is single-peaked with its maximum at or near 1.26. The unsampled intervals are 1.00–1.25 and 1.30–1.49. Target a cost ratio in the 1.15–1.35 band and, ideally, sample two points there so the peak is bracketed rather than merely re-hit.

**The measurement noise floor is small, so the 5-vs-6 gap is real signal.** Attempts 2 and 4 sit at cost ratios 1.4966 and 1.4974 with rewards 0.8037 and 0.8042 — a spread of about 0.0005. The 0.0196 gap between attempt 5 and attempt 6 is roughly forty times that, so it is a genuine property of the cost-ratio position and not run-to-run variation. Do not attribute attempt 6's shortfall to noise and do not chase sub-0.001 differences.

**Hold wall clock near 13.4–13.7 s while moving the cost ratio.** Every scoring run in that wall-clock band returned at least 0.8037; the one run that left it (attempt 8, 16.5068 s) returned 0.7843. Attempt 5 achieved the best reward at 13.7398 s, which is not the minimum wall clock in the set — so there is no need to shave wall clock further, but there is a clear cost to letting it grow. Treat ~13.5–13.8 s as the operating band and vary only the cost ratio.

**Preserve the attempt-2 conformance fix intact.** Six consecutive attempts have held all checks and both perturbations. Any change made in pursuit of the cost-ratio optimum must not touch log emission or the between-run state reset, since C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER were only ever exercised by the ruleset perturbation and would not be caught by primary metrics.

**Perturbation outcomes, reported by kind and in aggregate.** Sixteen held-out runs across the eight records, two per record, one of each kind. By kind: the **ruleset** kind reached its threshold in seven of eight records and failed in one, on C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER. The **held_out_variant** kind reached its threshold in seven of eight records and failed in one, on C-TARGET-REACHED and C-BUDGET-RESPECTED. In aggregate, 14 of 16 reached, with both failures belonging to attempt 1 and `all_perturbations_held` true for every attempt since. No individual run is identified across records and none should be assumed to be the same run twice. Since perturbation conformance is currently saturated, it is not a source of headroom — but it is a source of downside risk, and any new approach should be checked against the ruleset kind specifically, because that kind is the only one that has ever surfaced a formatting or carryover defect.

**Call: exploit.** Attempt 5's approach class scored 0.8255, the best in the set, and the cost-ratio curve around it is not yet exhausted — the 1.15–1.35 band is unsampled on both sides of 1.26 and the curve's shape says the peak lies inside it. This is not a case where the scoring approaches have stopped improving; it is a case where the loop wandered away from the peak. Attempts 6, 7 and 8 each moved the cost ratio further from 1.26 (to 0.97, 1.60 and 1.50) and each scored lower, which is a search that stepped off the optimum in three directions rather than refining it. Reproduce the attempt-5 configuration at cost ratio ≈ 1.26 and wall clock ≈ 13.7 s, then perturb the cost ratio by a small amount within 1.15–1.35 and keep whichever side improves. Do not re-run the ~1.50 plateau, do not push below 1.0, and do not let wall clock drift toward 16 s.
