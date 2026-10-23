# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.8658, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All 13 attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3        0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                
  5 *      0.8658   1.000             2 of 2         yes             74                
  6        0.7580   0.857             2 of 2         yes             46                
  7        0.4911   1.000             1 of 2         yes             50                
  8        0.7805   1.000             2 of 2         yes             99                
  9        0.8332   1.000             2 of 2         yes             50                
  10       0.8503   1.000             2 of 2         yes             75                
  11       0.8067   1.000             2 of 2         yes             74                
  12       0.4275   1.000             1 of 2         yes             74                
  13       0.8657   1.000             2 of 2         yes             74                
  14       0.8513   1.000             2 of 2         yes             74                
  15       0.8579   1.000             2 of 2         yes             74                
  16       0.7005   1.000             2 of 2         yes             75                
  17       0.8655   1.000             2 of 2         yes             76                
  18       0.8368   1.000             2 of 2         yes             74                

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
  12 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 13 -- reward 0.8657, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 16 -- reward 0.7005, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 75
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 17 -- reward 0.8655, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 18 -- reward 0.8368, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED has failed on 2 attempts (7, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Eighteen graded records, all with `measurement_status: "measured"`; every one carries a reward. Listed worst to best:

| Rank | Attempt | reward | Notes from the record |
|---|---|---|---|
| 1 (worst) | 12 | 0.4275 | `C-PERTURBATION-REACHED` failed; `task_pass` 0.0; `conformance_fraction` 0.5 |
| 2 | 7 | 0.4911 | `C-PERTURBATION-REACHED` failed; `task_pass` 0.0; `conformance_fraction` 0.5 |
| 3 | 16 | 0.7005 | clean checks; `compute_efficiency` 0.9805, `per_step_cost_ratio` 0.7055 |
| 4 | 6 | 0.7580 | `C-API-SURFACE` failed; `task_pass` 0.0; `rule_conformance` 0.8571 |
| 5 | 4 | 0.7740 | clean; ce 0.9681, psc 0.6934 |
| 6 | 8 | 0.7805 | clean; ce 0.6575, psc 1.0848, wall clock 98.60 s (the longest run recorded) |
| 7 | 11 | 0.8067 | clean; ce 1.0000 (the maximum observed), psc 0.6947 |
| 8 | 2 | 0.8079 | clean; ce 0.7226, psc 0.9441 |
| 9 | 9 | 0.8332 | clean; ce 0.7505, psc 0.9516 |
| 10 | 18 | 0.8368 | clean; ce 0.8827, psc 0.7671 |
| 11 | 10 | 0.8503 | clean; ce 0.7433, psc 0.9615 |
| 12 | 14 | 0.8513 | clean; ce 0.9705, psc 0.6997 |
| 13 | 15 | 0.8579 | clean; ce 0.9355, psc 0.9424 |
| 14 | 1 | 0.8630 | clean; ce 0.6784, psc 1.0723; `standing_against_best_so_far: first_measured_attempt` |
| 15 | 17 | 0.8655 | clean; ce 0.7320, psc 0.9464 |
| 16 | 13 | 0.8657 | clean; ce 0.6829, psc 0.9710 |
| 17 | 3 | 0.8657 | clean; ce 0.6922, psc 0.9835 |
| 18 (best) | 5 | **0.8658** | clean; ce 0.6926, psc 0.9581 |

**Attempt 5 holds the highest reward at 0.8658 and is the score to beat.** Attempt 3 (0.8657) and attempt 13 (0.8657) are within 0.0002 of it, and attempt 17 (0.8655) within 0.0004; these four are effectively a single plateau.

Direction of travel, stated plainly and not softened: only three records improved on everything before them (`standing_against_best_so_far: "better_than_every_earlier_attempt"` for attempts 3 and 5; attempt 1 was the first measurement). **Every other record — attempts 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 — is marked `worse_than_an_earlier_attempt`.** Everything after attempt 5 has been a regression against attempt 5, including the near-ties at 0.8657 and 0.8655: they are lower, not progress. Nothing has beaten 0.8658 since it was set.

No record produced a zero. `zero_reason_code` is 0 and `red_line_crossed` is 0.0 in all eighteen; `validity` is 1.0 in all eighteen. `primary_target_reached` is 1.0 in all eighteen — the primary run has never been the problem.

# 2. Approach classes tried

Only the graded metrics are carried forward, not the source, so the classes below are grouped by the measured configuration signature (`per_step_cost_ratio`, `compute_efficiency`, `wall_clock_sec`) and by which checks held.

**Class A — baseline-cost training runs (psc ≈ 0.94–1.09, ce ≈ 0.66–0.75, wall clock ≈ 74–76 s).** Attempts 1, 2, 3, 5, 8, 9, 10, 13, 17. This class contains every top score: 0.8658, 0.8657, 0.8657, 0.8655, 0.8630, and also 0.8503, 0.8332, 0.8079, 0.7805. All clean on checks; all perturbations held. The plateau at ~0.8655–0.8658 lives here, at psc ≈ 0.946–0.984 with ce ≈ 0.68–0.73. This is the productive family.

**Class B — aggressive cost-cutting / speed-first configurations (psc ≈ 0.69–0.81, ce ≈ 0.88–1.00).** Attempts 4 (0.7740), 11 (0.8067), 14 (0.8513), 16 (0.7005), 18 (0.8368). Every member is below the Class A plateau, and the class is high-variance: attempt 11 reached the maximum recorded `compute_efficiency` of 1.0000 and still only scored 0.8067; attempt 16 reached ce 0.9805 and scored 0.7005, the lowest of any clean-check record. Attempt 14 is the best of the class at 0.8513 with essentially the same signature as attempt 4 (ce 0.9705 vs 0.9681, psc 0.6997 vs 0.6934) which scored 0.7740 — a 0.077 spread across a nearly identical cost profile, so cost profile alone does not determine reward inside this class.

**Class C — high efficiency held at near-baseline per-step cost.** Attempt 15 alone: ce 0.9355 *and* psc 0.9424, reward 0.8579. This is the only record that raised compute efficiency substantially without cutting per-step cost, and it is the closest any non-Class-A record came to the plateau. It is still below attempt 5.

**Class D — over-budget / longer-training variant.** Attempt 8: wall clock 98.60 s, psc 1.0848, ce 0.6575, reward 0.7805. Spending materially more wall clock than the ~74 s norm did not buy reward; it cost about 0.085 against attempt 5.

**Class E — submissions that broke the module API surface.** Attempt 6 only: `C-API-SURFACE` failed, `task_pass` went to 0.0 and `rule_conformance` to 0.8571, reward 0.7580. Notably the perturbation runs still both reached in this record; the damage was purely conformance.

**Class F — submissions that broke the held-out perturbation budget.** Attempts 7 (0.4911) and 12 (0.4275), the two worst records. Both have `all_perturbations_held: false` and `conformance_fraction: 0.5`.

# 3. Checks that failed

**`C-PERTURBATION-REACHED` — failed twice** (attempts 7 and 12). Verifier reason, identical in both: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This is the single most costly finding: it is the only check whose failure roughly halved reward (0.4911 and 0.4275 versus a 0.8658 best), and it drove `conformance_fraction` to 0.5 and `task_pass` to 0.0 in both. Two attempts, two failures, same reason. **Whatever was changed between attempts 7 and 12 is not what causes this check to fail** — the change did not touch the cause, and it must not be tried again as a fix.

**`C-API-SURFACE` — failed once** (attempt 6). Verifier reason: *"module-level statements outside imports, constants, and permitted definitions."* This zeroed `task_pass` and dropped `rule_conformance` to 0.8571 while the perturbations still held. The fix is mechanical and precise: at module scope the submission may contain only imports, constant assignments, and the permitted definitions (function/class defs). Anything executable at import time — a call, a print, a loop, an `if`, a computed setup expression — must be moved inside a function. This is not "a conformance issue" in general; it is exactly that one rule.

No other check has ever failed. In the fifteen clean records `rule_conformance` and `conformance_fraction` are both 1.0.

# 4. Ruled-out directions

**Aggressive per-step cost cutting (psc down to ~0.69–0.71) to buy compute efficiency.** Ruled out as a route past 0.8658: five records tried it and all five landed below the plateau (0.7005, 0.7740, 0.8067, 0.8368, 0.8513). Pushing `compute_efficiency` to its ceiling was actively counterproductive — attempt 11 hit ce 1.0000 and scored 0.8067, attempt 16 hit ce 0.9805 and scored 0.7005, both far below attempt 5's 0.8658 achieved at ce 0.6926. Whatever quality term dominates reward loses more from the cheap configuration than the efficiency term gives back.

**Spending more wall clock than the ~74 s norm.** Ruled out by attempt 8: 98.60 s, the longest run, produced 0.7805 — worse than a dozen ~74 s records. Extra budget is not converted into reward.

**Any module-level executable statement in the submission.** Ruled out by attempt 6's `C-API-SURFACE` failure, which set `task_pass` to 0.0 outright. The stub's module scope must stay limited to imports, constants and permitted definitions.

**Whatever was varied between attempts 7 and 12 as a remedy for the held-out perturbation failure.** Ruled out because the check failed identically both times, and in attempt 12 it failed harder (`C-TARGET-REACHED` joined `C-BUDGET-RESPECTED` on the failing unit). Repeating that class of change is neither exploration nor exploitation.

**Re-running the plateau configuration unchanged.** Attempts 3, 5, 13 and 17 span 0.8655–0.8658 — a spread of 0.0003. Another sample from that same regime is very unlikely to exceed 0.8658 by more than noise; it needs a substantive quality improvement, not a resample.

# 5. Open leads

**Perturbation outcomes, by kind and in aggregate.** Every record declares 2 perturbations (`perturbations_declared: 2.0`), one of kind `seed` and one of kind `held_out_variant`. Across all eighteen records that is 36 held-out units. Thirty-four reached their threshold; two did not, and **both failures were on a `held_out_variant` unit** (in attempts 7 and 12). **Every `seed` unit reached its threshold in every record without exception — 18 of 18.** Of the `held_out_variant` units, 16 of 18 reached. The failing check on the variant unit was `C-BUDGET-RESPECTED` both times, joined by `C-TARGET-REACHED` in attempt 12. The runs are not identified, so nothing here says the same underlying variant failed twice — only that it is the `held_out_variant` kind that fails, and that it fails on budget. Lead: whatever adaptive or data-dependent element makes the run's cost depend on the variant needs a hard, self-imposed step or time cap derived from the *declared* budget rather than from the primary run's observed timing, so the variant cannot overrun even when it converges more slowly. Note also that attempts 7 and 12 had `qualifying_budget` 50.05 and 74.11 with `wall_clock_sec` 50.05 and 74.11 — the primary run was comfortably inside budget while the variant was not, so per-run budget accounting, not global timing, is the place to look.

**The strongest concrete lead: attempt 15's regime.** It is the only record that achieved high `compute_efficiency` (0.9355) *without* cutting `per_step_cost_ratio` (0.9424), and it scored 0.8579 — the best result outside the plateau family and outside Class A entirely. The plateau (attempt 5: ce 0.6926, psc 0.9581, 0.8658) and attempt 15 differ by +0.24 in efficiency for −0.008 in reward. Closing that last 0.008 while keeping attempt 15's efficiency would clear 0.8658 if the efficiency term contributes at all. Try attempt 5's training configuration with attempt 15's efficiency mechanism layered on, rather than either in isolation.

**Interrogate the quality term directly.** Reward is clearly not a monotone function of efficiency: attempt 4 (ce 0.9681, psc 0.6934) scored 0.7740 while attempt 14 (ce 0.9705, psc 0.6997) scored 0.8513 on a near-identical cost profile. That 0.077 gap must come from the task-quality side. The plateau's tightness (0.8655–0.8658 across four attempts) says quality has saturated at the Class A settings. Worth trying: better final-model selection (averaging the last few checkpoints, or picking the best-validation state rather than the last), stronger but cheap regularisation, and a learning-rate schedule that anneals harder at the end — all changes that raise final quality at unchanged per-step cost, keeping psc in the 0.95–0.98 band that every top score occupies.

**Do not chase `per_step_cost_ratio` above 1.0.** Attempt 1 (psc 1.0723) reached 0.8630 and attempt 8 (psc 1.0848) only 0.7805, so exceeding baseline cost is survivable but not rewarding. The 0.94–0.98 band is where four of the top five scores sit.

**Free wins to lock in regardless of approach.** Keep module scope free of executable statements (`C-API-SURFACE`), keep the declared perturbation count at 2 with a hard per-run budget cap (`C-PERTURBATION-REACHED`), and keep total wall clock near 74 s. These three cost nothing and protect against the only two failure modes ever observed.

---

**Call: exploit.** Take attempt 5's configuration — the 0.8658 holder, psc ≈ 0.958, ce ≈ 0.693, ~74 s wall clock, all checks clean — as the base and make it better on the quality side, with attempt 15's high-efficiency-at-baseline-cost mechanism as the specific modification to graft on. The plateau is tight but the approaches that scored have not been shown to be exhausted along the quality axis, and the one structurally different direction that has been sampled repeatedly (aggressive cost cutting) is already ruled out by five below-plateau results. Explore is not warranted yet. Whatever is done, do not resubmit the two configurations that failed `C-PERTURBATION-REACHED` with only incidental changes: that pattern has already been repeated once without addressing the held-out variant's budget overrun, and repeating it again would be neither explore nor exploit.
