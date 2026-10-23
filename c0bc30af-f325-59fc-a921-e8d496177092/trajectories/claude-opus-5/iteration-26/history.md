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

    All one attempts since have scored lower than it.
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
  21 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 24 -- reward 0.8979, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-six graded submissions, all with `measurement_status: "measured"`, so every one carries a reward. Ordered worst to best:

| Reward | Attempt(s) | Notes |
|---|---|---|
| 0.0000 | 3, 7, 9, 10, 12, 15, 16, 21, 22, 26 | ten attempts, `zero_reason_code` 4, wall clock 1690–1693 s each, no qualifying evaluation row |
| 0.5615 | 6 | `rule_conformance` 0.8571, `task_pass` 0, qualifying budget 204.09 s |
| 0.6955 | 14 | clean checks, qualifying budget 99.74 s |
| 0.7551 | 8 | clean checks, qualifying budget 78.14 s, wall clock 151.50 s |
| 0.7684 | 1 | `rule_conformance` 0.8571, `task_pass` 0, qualifying budget 25.46 s |
| 0.7919 | 17 | clean, 73.80 s |
| 0.8385 | 2 | clean, 73.62 s |
| 0.8451 | 13 | clean, 71.31 s |
| 0.8661 | 20 | clean, 62.46 s, `compute_efficiency` 1.0 |
| 0.8719 | 4 | clean, 50.03 s, `compute_efficiency` 1.0 |
| 0.8768 | 23 | clean, 49.67 s |
| 0.8794 | 18 | clean, 49.33 s |
| 0.8979 | 24 | clean, 25.37 s (0.8979099) |
| 0.8980 | 11 | clean, 25.35 s (0.8979842) |
| 0.9121 | 19 | clean, 45.81 s |
| 0.9128 | 5 | clean, 25.34 s |
| **0.9130** | **25** | **clean, 25.32 s — highest reward recorded; this is the one to beat** |

Attempt 25 holds the highest reward at 0.9130 and is the mark any next attempt must exceed. Attempts 5 (0.9128) and 19 (0.9121) are statistically adjacent to it; attempts 11 and 24 (0.8980, 0.8979) sit just below.

Direction of movement, stated plainly and not softened: the record is not a rising line. `standing_against_best_so_far` reads `better_than_every_earlier_attempt` at only four points — attempts 2, 4, 5 and 25 — and reads `worse_than_an_earlier_attempt` at every other attempt from 3 onward. Attempts 6, 8, 14 and 17 were all regressions against the then-standing best, and the ten zero-reward attempts were regressions to nothing at all. After attempt 5 (0.9128) reached what is essentially the current plateau, twenty further attempts produced exactly one improvement, and that improvement was 0.0002 in size (attempt 25 over attempt 5). The plateau near 0.913 has not been meaningfully broken.

A structural note that the numbers support and that the next attempt should carry: among conformant, target-reaching runs, reward tracks the qualifying budget almost monotonically downward. Every reward at or above 0.898 came from a run whose qualifying budget was 25.3–45.8 s; every reward below 0.80 came from a run whose qualifying budget was 73.8 s or longer (0.7919 at 73.80 s, 0.7551 at 78.14 s, 0.6955 at 99.74 s, 0.5615 at 204.09 s). Faster qualification is worth more than any other lever measured.

Second-order effect: at a fixed qualifying budget the reward still separates by `compute_efficiency`. The four runs that qualified in the 25.31–25.37 s cluster ranked in efficiency order — 0.7043 → 0.8980 (attempt 11), 0.7330 → 0.8979 (24), 0.7728 → 0.9128 (5), 0.8277 → 0.9130 (25). Meanwhile the two runs that achieved `compute_efficiency` 1.0 (attempts 4 and 20) scored only 0.8719 and 0.8661 because they took 50.03 s and 62.46 s to qualify. Efficiency does not buy back a slow qualification.

# 2. Approach classes tried

Five distinguishable classes emerge from the measured signatures. Records sharing a signature are one entry.

**Class A — fast-qualifying conformant runs (the winning class).** Attempts 5, 11, 24, 25. Qualifying budget clusters tightly at 25.317–25.370 s, all checks held, `task_pass` 1, `validity` 1, both perturbation units reached. Rewards 0.8979, 0.8980, 0.9128, 0.9130. Notably, no attempt in the entire record ever qualified faster than 25.317 s, and four separate attempts landed within 0.06 s of each other. That cluster looks like a floor imposed by the harness — most plausibly the time of the first evaluation row the harness will consider, meaning the earliest a run can possibly cross the threshold. If so, Class A is already sitting on the qualification-time floor and the only remaining lever within it is `compute_efficiency` and `per_step_cost_ratio`. Attempt 25 got there with efficiency 0.8277 and cost ratio 0.8726; attempt 5 with 0.7728 and 0.9887.

**Class B — mid-budget conformant runs.** Attempts 2, 4, 8, 13, 17, 18, 19, 20, 23. Qualifying budgets 45.81–78.14 s, all checks held, `task_pass` 1. Rewards 0.7551–0.9121. This class contains the best non-floor result (attempt 19, 0.9121 at 45.81 s, efficiency 0.9345, cost ratio 0.7669) and also the two `compute_efficiency` = 1.0 runs (attempts 4 and 20) which nonetheless underperformed Class A. Attempt 8 is a marker worth remembering: its qualifying budget was 78.14 s but its wall clock was 151.50 s — the only conformant record where those two diverge substantially — and it scored 0.7551. Whatever it did spent roughly half its wall clock after the qualifying point without being paid for it.

**Class C — slow conformant runs.** Attempts 14 (99.74 s, 0.6955) and 6 (204.09 s, 0.5615, which also broke conformance). Longer training before qualification, and the reward penalty is severe and roughly linear in the extra time. This class is dominated by Class A and B on every measured axis.

**Class D — submissions with module-level executable code.** Attempts 1 and 6. Both failed `C-API-SURFACE` and both dropped `rule_conformance` to 0.8571 (six of seven rules) and `task_pass` to 0, even though `primary_target_reached` was 1 and both perturbation units reached in both records. Attempt 1 shows the cost cleanly: it qualified at 25.46 s — squarely in the Class A time cluster — and scored only 0.7684 instead of the ~0.91 that time band otherwise pays. The API-surface violation costs roughly 0.14 reward outright.

**Class E — long-running non-qualifying runs.** Attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26. Ten attempts, all with wall clock pinned between 1690.32 s and 1692.97 s — a spread of under 3 s across ten independent runs, which is the unmistakable signature of a hard time ceiling being hit rather than of ten distinct convergence failures. All scored 0.0000 with `zero_reason_code` 4, `conformance_fraction` 0.0, and `primary_target_reached` 0. Interestingly `rule_conformance` was 1.0 and `validity` 1.0 in all ten, and `compute_efficiency` was high (0.9033–1.0) and `per_step_cost_ratio` low (0.6827–0.8901). These were not malformed or rule-breaking submissions and they were not slow per step; they were runs whose training simply never crossed the threshold before the harness cut them off. Cheap steps that never reach the target are worth nothing. This class was re-entered ten times across the run — attempts 3, 7, 9, 10, 12, 15, 16, 21, 22 and 26 — which is well over a third of all work, and it is the single largest waste in the record.

# 3. Checks that failed

**`C-TARGET-REACHED`** — "no evaluation row crosses the threshold in the declared direction". Failed **ten times** on the primary run: attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26. This is the dominant failure in the entire record. Every one of those attempts also carried a wall clock of ~1690–1693 s, and every one had `rule_conformance` 1.0 and `validity` 1.0. Whatever was changed between those ten attempts is not what is causing this failure — ten separate submissions, spanning `compute_efficiency` from 0.9033 to 1.0 and `per_step_cost_ratio` from 0.6827 to 0.8901, all landed identically on it. The cause is not per-step cost, not efficiency, and not rule conformance; it is that the configuration does not reach the threshold at all within the time the harness allows.

**`C-BUDGET-RESPECTED`** — "no qualifying row, so no budget position exists". Failed **ten times**, on exactly the same attempts and always alongside `C-TARGET-REACHED`. This is a consequence, not an independent fault: with no row crossing the threshold there is no budget position to evaluate. Fixing `C-TARGET-REACHED` fixes this one automatically. It should not be treated as a separate problem to solve.

**`C-PERTURBATION-REACHED`** — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed **ten times**, on the same ten attempts. Also always 0 of 2, never 1 of 2 — the perturbation runs fail together with the primary and never independently of it.

**`C-API-SURFACE`** — "module-level statements outside imports, constants, and permitted definitions". Failed **twice**: attempts 1 and 6. Two attempts separated by four intervening submissions both reintroduced module-level executable code, so whatever else was changed between attempt 1 and attempt 6 is not what causes this check to fail — the cause is specifically that the submission file executes statements at import time beyond imports, constant assignments, and permitted function/class definitions. The fix is mechanical: every statement at module scope must be an import, a constant assignment, or a `def`/`class`; all setup, seeding, device selection, data loading, and any print or assertion must move inside the entrypoint function. This check has not failed since attempt 6 and the discipline that avoided it in attempts 7 onward should be preserved verbatim.

Note that `red_line_crossed` is 0.0 and `validity` is 1.0 in all twenty-six records. No submission has ever tripped a red line or been ruled invalid. Those are not risk areas.

# 4. Ruled-out directions

**Anything landing in Class E — long-running configurations that never cross the threshold.** Ten attempts produced 0.0000 with the identical `C-TARGET-REACHED` / `C-BUDGET-RESPECTED` / `C-PERTURBATION-REACHED` triple and a wall clock pinned at the ~1690 s ceiling. This was repeated ten times without the thing that caused it being changed, which is neither exploration nor exploitation — it is the same null result re-purchased ten times. Whatever family of settings produces a ~1690 s non-qualifying run must not be re-entered. Concretely: the next attempt must verify that its configuration crosses the threshold quickly, and must not ship a configuration whose expected time-to-threshold is unknown or unbounded.

**Optimising `per_step_cost_ratio` or `compute_efficiency` in isolation.** The ten zero-reward attempts had the *best* cost ratios in the whole record (0.6827–0.8901, versus 0.8726–1.3778 among scoring attempts) and high efficiency, and they scored nothing. Cheaper or more efficient steps that push the threshold crossing past the ceiling are strictly worse than more expensive steps that cross it at 25 s. Efficiency is a tiebreaker within a time band, never a substitute for reaching the target.

**Chasing `compute_efficiency` = 1.0 as the objective.** Achieved twice, at attempts 4 and 20, scoring 0.8719 and 0.8661 — both below the 25 s cluster's 0.913 despite perfect efficiency, because they took 50.03 s and 62.46 s to qualify. Perfect efficiency does not compensate for a slow qualification. Ruled out as a primary target.

**Module-level executable code (Class D).** Costs `C-API-SURFACE`, drops `rule_conformance` to 0.8571 and `task_pass` to 0, and cost attempt 1 roughly 0.14 reward relative to its time band. There is no upside; the same work runs identically inside the entrypoint. Ruled out.

**Long-training conformant runs (Class C).** Attempts 14 and 6 at 99.74 s and 204.09 s scored 0.6955 and 0.5615. Reward falls steeply with qualifying budget. Any approach requiring more than ~50 s to reach the threshold is dominated and should not be pursued.

**Continuing to compute after the qualifying row.** Attempt 8 is the evidence: qualifying budget 78.14 s against a 151.50 s wall clock, reward 0.7551. The extra 73 s bought nothing. The run should stop as soon as it has produced a qualifying evaluation row.

**Treating `C-BUDGET-RESPECTED` and `C-PERTURBATION-REACHED` as independent bugs.** In all ten records where they appear they appear only together with `C-TARGET-REACHED`, and the verifier's own reason for `C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists" — states the dependency. No effort should be spent on them separately.

**Robustness/generalisation work aimed at the perturbation runs.** See section 5 for the aggregate, but the short form is that no perturbation run has ever failed while the primary succeeded. Spending an attempt hardening against seed or variant shift addresses a failure mode that has not occurred.

# 5. Open leads

**Perturbation outcomes, reported by kind and in aggregate.** Each record declares two perturbation units, one of kind `held_out_variant` and one of kind `seed`; the runs are not otherwise identified and nothing here should be read as tracking a particular run across records. Across the twenty-six records that is 26 `held_out_variant` runs and 26 `seed` runs, 52 in total. By kind: `held_out_variant` reached its threshold in 16 records and failed in 10; `seed` reached in 16 and failed in 10. In aggregate, 32 of 52 reached and 20 failed. Every failing run of both kinds failed on the same pair, `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, and every such failure occurred in a record where the primary run also failed `C-TARGET-REACHED`. The counts are identical by kind and the co-occurrence is total: **neither the held-out-variant kind nor the seed kind has ever failed independently of the primary run**. Generalisation across variants and robustness across seeds are not binding constraints. The single constraint is reaching the target at all, and when the primary reaches it, both perturbation kinds reach it too, in all 16 such records. `all_perturbations_held` is true in exactly the 16 records where the primary succeeded.

**Lead 1 — reproduce attempt 25's shape exactly, then push `compute_efficiency` within the 25.3 s floor.** This is the highest-value lead. Attempt 25: qualifying budget 25.317 s, `compute_efficiency` 0.8277, `per_step_cost_ratio` 0.8726, all checks held, reward 0.9130. The 25.31–25.46 s cluster appears in five separate records (attempts 1, 5, 11, 24, 25) and nothing has ever qualified faster, so treat ~25.3 s as a hard floor on qualification time — probably the first evaluation row the harness will score. Within that floor, reward rose monotonically with efficiency across the four conformant members (0.7043→0.8980, 0.7330→0.8979, 0.7728→0.9128, 0.8277→0.9130). The unexplored corner is efficiency above 0.83 *at* the 25.3 s floor. Attempts 4 and 20 proved efficiency 1.0 is attainable; it has never been attained at the floor. Combining them is the clearest path past 0.9130. Note the gain from 0.7728 to 0.8277 efficiency was only 0.0002 reward, so the curve may be flattening near the top — but nothing at the floor has been measured above 0.8277 efficiency, so the shape there is genuinely unknown.

**Lead 2 — drive `per_step_cost_ratio` down while holding the 25.3 s qualification.** Attempt 25's cost ratio was 0.8726 and attempt 19's was 0.7669 (at 45.81 s, reward 0.9121). Cost ratios as low as 0.6145 have been achieved (attempt 20, at 62.46 s). A run at the 25.3 s floor with a cost ratio nearer 0.70 has never been measured and is the second untested corner. Cheaper steps are only worth pursuing if they do not push the threshold crossing past the first eligible evaluation row — that is precisely the trap that produced Class E ten times.

**Lead 3 — stop the run the moment a qualifying row is produced.** Attempt 8's 78.14 s qualifying budget against a 151.50 s wall clock, for 0.7551, is direct evidence that post-qualification compute is unpaid. If the current shape continues past the qualifying row for any reason, cutting it is free reward. Every top-scoring record has `wall_clock_sec` equal to `qualifying_budget` to the digit; attempt 8 is the sole exception among conformant records and it is the worst-scoring conformant record after the slow Class C runs.

**Lead 4 — preserve the API-surface discipline explicitly.** `C-API-SURFACE` has failed twice, at attempts 1 and 6, on module-level statements outside imports, constants, and permitted definitions. Because the next attempt starts from a pristine stub with no memory of the fix, this must be re-established deliberately: keep module scope to imports, constant assignments, and `def`/`class` only, and put every executable statement — seeding, device selection, data preparation, the training loop, any diagnostic output — inside the entrypoint function. This is worth roughly 0.14 reward and costs nothing.

**Lead 5 — attempt 19 as a fallback shape.** At 45.81 s with efficiency 0.9345 and cost ratio 0.7669 it scored 0.9121, essentially matching the 25 s cluster from a different point in the trade-off space. If the 25.3 s floor turns out to be unreachable for a given configuration, the 45–50 s band with high efficiency and low cost ratio is the next best measured region (attempts 18, 19, 23 at 0.8794, 0.9121, 0.8768).

**Call: exploit.** The approach that scores is known precisely — a conformant, fast-qualifying run that crosses the threshold at the ~25.3 s floor with all seven rules held and no module-level statements — and it has produced the top five rewards in the record (0.8979, 0.8980, 0.9121, 0.9128, 0.9130). It has not stopped improving in a way that justifies a structural change; rather, twenty attempts since attempt 5 were largely spent re-entering the zero-reward Class E rather than refining the winning shape, so the winning shape is under-explored, not exhausted. The specific exploit is: rebuild attempt 25's configuration, keep the qualification at the 25.3 s floor, and raise `compute_efficiency` toward the 1.0 that attempts 4 and 20 already demonstrated is achievable — while never shipping a configuration whose time-to-threshold is unverified, because that is the one mistake that has already produced 0.0000 ten times.
