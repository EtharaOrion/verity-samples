# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 25 -- reward 0.9130, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All three attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4        0.8719   1.000             2 of 2         yes             50                
  5        0.9128   1.000             2 of 2         yes             25                
  6        0.5615   0.857             2 of 2         yes             204               
  7        0.0000   1.000             0 of 2         no              --                
  8        0.7551   1.000             2 of 2         yes             78                
  9        0.0000   1.000             0 of 2         no              --                
  10       0.0000   1.000             0 of 2         no              --                
  11       0.8980   1.000             2 of 2         yes             25                
  12       0.0000   1.000             0 of 2         no              --                
  13       0.8451   1.000             2 of 2         yes             71                
  14       0.6955   1.000             2 of 2         yes             100               
  15       0.0000   1.000             0 of 2         no              --                
  16       0.0000   1.000             0 of 2         no              --                
  17       0.7919   1.000             2 of 2         yes             74                
  18       0.8794   1.000             2 of 2         yes             49                
  19       0.9121   1.000             2 of 2         yes             46                
  20       0.8661   1.000             2 of 2         yes             62                
  21       0.0000   1.000             0 of 2         no              --                
  22       0.0000   1.000             0 of 2         no              --                
  23       0.8768   1.000             2 of 2         yes             50                
  24       0.8979   1.000             2 of 2         yes             25                
  25 *     0.9130   1.000             2 of 2         yes             25                
  26       0.0000   1.000             0 of 2         no              --                
  27       0.7552   0.857             2 of 2         yes             25                
  28       0.8841   1.000             2 of 2         yes             25                

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
  22 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 5 -- reward 0.9128, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.9121, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 46
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 26 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 27 -- reward 0.7552, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 28 -- reward 0.8841, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (1, 6, 27). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All 28 graded records carry `measurement_status: "measured"`, so every one has a reward. None is a "no measurement" case. Ranked worst to best:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1–10 (tied, worst) | 3, 7, 9, 10, 12, 15, 16, 21, 22, 26 | 0.0000 each | `zero_reason_code` 4; wall clock 1690–1693 s in every case; target never crossed |
| 11 | 6 | 0.5615 | C-API-SURFACE failed; wall clock 204.09 s |
| 12 | 14 | 0.6955 | clean checks; budget 99.74 s |
| 13 | 8 | 0.7551 | clean checks; qualifying budget 78.14 s but wall clock 151.50 s |
| 14 | 27 | 0.7552 | C-API-SURFACE failed; budget 25.26 s |
| 15 | 1 | 0.7684 | C-API-SURFACE failed; budget 25.46 s |
| 16 | 17 | 0.7919 | clean; budget 73.80 s |
| 17 | 2 | 0.8385 | clean; budget 73.62 s |
| 18 | 13 | 0.8451 | clean; budget 71.31 s |
| 19 | 20 | 0.8661 | clean; budget 62.46 s; `compute_efficiency` 1.0 |
| 20 | 4 | 0.8719 | clean; budget 50.03 s; `compute_efficiency` 1.0 |
| 21 | 23 | 0.8768 | clean; budget 49.67 s |
| 22 | 18 | 0.8794 | clean; budget 49.33 s |
| 23 | 28 | 0.8841 | clean; budget 24.62 s — the *lowest* budget of any record |
| 24 | 24 | 0.8979 | clean; budget 25.37 s |
| 25 | 11 | 0.8980 | clean; budget 25.35 s |
| 26 | 19 | 0.9121 | clean; budget 45.81 s |
| 27 | 5 | 0.9128 | clean; budget 25.34 s |
| 28 (best) | 25 | 0.9130 | clean; budget 25.32 s |

**Attempt 25 holds the highest reward, 0.9130. That is the score to beat.**

Direction of travel, stated plainly rather than softened: the record does *not* show steady progress. `standing_against_best_so_far` reads `better_than_every_earlier_attempt` for only four attempts — 2 (0.8385), 4 (0.8719), 5 (0.9128) and 25 (0.9130). Every other attempt from 3 onward is marked `worse_than_an_earlier_attempt`. Attempt 6 (0.5615) was worse than attempt 5. Attempt 8 (0.7551) was worse than 5. Attempts 13, 14, 17, 18, 20, 23, 24, 27, 28 all scored below the standing best at the time they ran. Ten attempts scored 0.0000. The gain from attempt 5 (0.9128) to attempt 25 (0.9130) is 0.0002 — the scoring frontier has been essentially flat across a long stretch of work.

`validity` is 1.0 and `red_line_crossed` is 0.0 in every record; nothing has ever been disqualified as invalid or tripped a red line.

# 2. Approach classes tried

The measured terms do not carry source code, so classes below are grouped by their metric signature, which is what distinguishes them.

**Class A — short-budget conforming run (~25 s).** Attempts 5, 11, 24, 25, 28 (and, with a conformance defect, 1 and 27). Qualifying budget 24.62–25.46 s, `task_pass` 1.0, both perturbations held, `compute_efficiency` 0.70–0.98, `per_step_cost_ratio` 0.68–1.11. This class contains the best result (25, 0.9130) and the second and third best clean results in the low-budget band (5, 0.9128; 11, 0.8980; 24, 0.8979; 28, 0.8841). It is the productive class.

**Class B — mid-budget conforming run (~45–63 s).** Attempts 4, 18, 19, 20, 23. Rewards 0.8661–0.9121. Attempt 19 at 45.81 s reached 0.9121, within 0.0009 of the overall best, showing this band is competitive but has not exceeded Class A.

**Class C — long-budget conforming run (~71–100 s, and one at 151 s wall).** Attempts 2, 8, 13, 14, 17. Rewards 0.6955–0.8451, monotonically worse as budget grows. Attempt 8 is the single record where `wall_clock_sec` (151.50) exceeds `qualifying_budget` (78.14); it scored 0.7551, below attempts 2 and 17 which had near-identical qualifying budgets (73.62 → 0.8385; 73.80 → 0.7919). Total wall clock, not just the qualifying row, appears to be priced in.

**Class D — very long conforming run (~204 s) with a conformance defect.** Attempt 6 only: 0.5615, the worst non-zero result. It combined the highest budget among scoring runs with the C-API-SURFACE failure, and `per_step_cost_ratio` 1.378 — the highest recorded.

**Class E — runaway / never-converging run.** Attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26. Ten records, all 0.0000, all with wall clock pinned at 1690–1693 s, all with `zero_reason_code` 4 and `conformance_fraction` 0.0. Notably these runs had *good* per-step economics — `compute_efficiency` 0.90–1.00 and `per_step_cost_ratio` 0.68–0.89 — so the cost per step was fine; what failed was ever crossing the threshold before the time ceiling. This class was re-entered ten separate times.

**Class F — module-level-statement variant.** Attempts 1, 6, 27, cutting across budget bands. Whatever else these did, they emitted module-level statements and lost the API-surface check.

# 3. Checks that failed

**C-API-SURFACE** — reason each time: "module-level statements outside imports, constants, and permitted definitions". **Failed 3 times**, in attempts 1, 6 and 27. These three span wildly different budgets (25.46 s, 204.09 s, 25.26 s) and different compute-efficiency figures (0.816, 0.609, 0.974). **Whatever was changed between those attempts is not what is causing this check to fail.** It is not a budget, speed or convergence problem: it is a purely structural property of the submitted module. Its cost is precise and large: it pins `rule_conformance` at 0.8571428571428571 (6 of 7) and forces `task_pass` to 0.0 *even when `primary_target_reached` is 1.0 and both perturbations held*. Attempt 27 (25.26 s, defect) scored 0.7552 while attempt 25 (25.32 s, clean) scored 0.9130 — approximately 0.158 of reward lost to this one check at equivalent budget.

**C-TARGET-REACHED** — reason: "no evaluation row crosses the threshold in the declared direction". **Failed 10 times**: attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26.

**C-BUDGET-RESPECTED** — reason: "no qualifying row, so no budget position exists". **Failed the same 10 times**, always alongside C-TARGET-REACHED. It is a consequence of the target miss, not an independent budget violation.

**C-PERTURBATION-REACHED** — reason: "0 of 2 declared perturbations reached their own threshold inside their own budget". **Failed the same 10 times.**

These three always co-occur and always with `wall_clock_sec` ≈ 1690 s. Across those ten attempts the `per_step_cost_ratio` varied from 0.683 to 0.890 and `compute_efficiency` from 0.903 to 1.000 — again, **whatever was varied between those ten attempts is not what is causing the failure.** Ten repetitions of a configuration that scores 0.0000 for the same three reasons, with no change to the thing producing the zero, is neither exploration nor exploitation.

# 4. Ruled-out directions

- **Any configuration that runs to the ~1690 s ceiling.** Ten attempts did this and every one scored 0.0000 on C-TARGET-REACHED / C-BUDGET-RESPECTED / C-PERTURBATION-REACHED. Ruled out: the model never crosses the threshold within the allowed budget, and no amount of per-step efficiency rescues it — these runs had the *best* per-step cost ratios on record.
- **Emitting module-level statements.** Ruled out by three independent failures of C-API-SURFACE, with a measured cost of roughly 0.158 reward at matched budget (27 vs 25) and a forced `task_pass` of 0.0.
- **Long budgets in the 70–205 s band.** Ruled out on evidence: rewards there run 0.5615–0.8451, uniformly below the ~25 s and ~46–50 s bands. Attempt 14 (99.74 s) got 0.6955; attempt 6 (204.09 s) got 0.5615.
- **Letting total wall clock exceed the qualifying budget.** Attempt 8 qualified at 78.14 s but ran 151.50 s total and scored 0.7551, below both other ~74 s records. Ruled out as a free lunch — trailing compute after the qualifying row is not free.
- **Driving wall clock below ~25 s as the primary lever.** Attempt 28 had the lowest budget of any record (24.62 s) with strong economics (`compute_efficiency` 0.977, `per_step_cost_ratio` 0.682) and still scored 0.8841 — *below* attempt 25 at 25.32 s with worse economics (0.828 / 0.873). Ruled out as the remaining source of gain; time alone no longer explains the ranking at the frontier.

# 5. Open leads

- **Reproduce the attempt-25 configuration exactly as the floor, then vary one thing.** It is the only 0.9130 on record and attempts 5 (0.9128) and 19 (0.9121) sit within 0.001 of it, so the ~25 s clean-conformance shape is reproducible, not a fluke. Any new work should start from that shape and be measured against 0.9130.
- **Find the non-time component of reward.** Attempts 28 and 25 have nearly the same budget but differ by 0.0289, and 28 is the *better* one on both `compute_efficiency` and `per_step_cost_ratio`. Something other than speed and per-step cost separates them — plausibly the margin by which the evaluation row clears the threshold, or the quality of the final model. Deliberately increasing that margin while holding the ~25 s budget is the most promising untested lever.
- **Test the 45–50 s band once more with the attempt-25 recipe.** Attempt 19 reached 0.9121 at 45.81 s; that band is not exhausted and may trade a little time for a lot of margin.
- **Add a hard self-imposed stop well under the qualifying budget.** This directly prevents re-entering Class E, which cost ten attempts, and prevents the attempt-8 pattern of wall clock overrunning the qualifying row.
- **Mechanically audit the module before submitting: no statements at module level other than imports, constants and permitted definitions.** Wrap all execution inside functions. This is cheap, has failed three times already, and is worth about 0.158.

**Perturbation summary (no run is named, numbered or positionally identified, and none can be claimed to be the same run across records).** Each record declares 2 perturbation units, one of kind `held_out_variant` and one of kind `seed`, for 56 units in total. In the 18 attempts where the primary target was reached, all 36 units reached their thresholds with no failed checks — both kinds, every time, including the three attempts that failed C-API-SURFACE. In the 10 attempts where the primary target was missed, all 20 units failed, and every one failed on exactly the same pair: **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**. By kind, the record is identical: the `held_out_variant` kind failed on those two checks in 10 records and held in 18; the `seed` kind failed on those two checks in 10 records and held in 18. No unit has ever failed C-API-SURFACE, and no unit has ever failed while the primary run succeeded. The held-out runs therefore add no failure mode of their own — they mirror the primary outcome exactly, which means robustness across seeds and variants is not currently a limiting factor.

**Call: exploit.** The frontier approach (Class A, ~25 s, fully conforming, both perturbations held) already scores 0.9130 and is reproducible across several attempts, but its top three results span only 0.0009, so pure repetition will not move it. Exploit means holding that shape fixed and attacking the one measured discrepancy it cannot yet explain — the reward gap between equally fast runs — while mechanically guaranteeing C-API-SURFACE passes and never approaching the ~1690 s ceiling. Do not re-enter the runaway class; it has been tried ten times without changing what makes it score 0.0000.
