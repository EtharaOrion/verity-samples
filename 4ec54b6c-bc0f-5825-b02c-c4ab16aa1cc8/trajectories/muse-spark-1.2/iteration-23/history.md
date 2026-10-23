# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 21 -- reward 0.7322, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All four attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2        0.7155   1.000             2 of 2         yes             17                
  3        0.6279   1.000             2 of 2         yes             20                
  4        0.5792   1.000             2 of 2         yes             18                
  5        0.6587   1.000             2 of 2         yes             21                
  6        --       --                --             --              --                
  7        --       --                --             --              --                
  8        0.5444   1.000             2 of 2         yes             26                
  9        0.5164   0.857             2 of 2         yes             17                
  10       0.5983   1.000             2 of 2         yes             20                
  11       0.6639   1.000             2 of 2         yes             20                
  12       0.4962   1.000             1 of 2         yes             17                
  13       0.5590   1.000             2 of 2         yes             21                
  14       0.6426   1.000             2 of 2         yes             18                
  15       0.5830   1.000             2 of 2         yes             24                
  16       0.5701   1.000             2 of 2         yes             21                
  17       0.5274   0.857             2 of 2         yes             24                
  18       0.5755   1.000             2 of 2         yes             21                
  19       0.7134   1.000             2 of 2         yes             17                
  20       0.5107   0.857             2 of 2         yes             17                
  21 *     0.7322   1.000             2 of 2         yes             14                
  22       0.6376   1.000             2 of 2         yes             17                
  23       0.6877   1.000             2 of 2         yes             20                
  24       0.6833   1.000             2 of 2         yes             20                
  25       0.0000   1.000             1 of 2         yes             21                

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
  19 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 2 -- reward 0.7155, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.7134, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 23 -- reward 0.6877, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 24 -- reward 0.6833, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 25 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget
        C-PER-STEP-COST-CEILING -- per-step cost is 3.246 times the seed anchor, above the ceiling of 3.0

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (9, 17, 20). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING failed on attempt 25.
    C-PERTURBATION-REACHED has failed on 2 attempts (12, 25). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-five attempts were graded. Twenty-three produced a measurement; attempts 6 and 7 returned `measurement_status: harbor_exception` and therefore produced **no measurement at all** — they have no reward, and must not be read as scores of zero, as failures, or as evidence about the code they contained.

Measured attempts, ordered worst to best by reward:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 | 25 | 0.0000 | validity 0, red_line_crossed 1, zero_reason_code 1 |
| 2 | 12 | 0.4962 | task_pass 0 |
| 3 | 20 | 0.5107 | task_pass 0, rule_conformance 0.8571 |
| 4 | 9 | 0.5164 | task_pass 0, rule_conformance 0.8571 |
| 5 | 17 | 0.5274 | task_pass 0, rule_conformance 0.8571 |
| 6 | 8 | 0.5444 | all checks held |
| 7 | 13 | 0.5590 | all checks held |
| 8 | 16 | 0.5701 | all checks held |
| 9 | 18 | 0.5755 | all checks held |
| 10 | 4 | 0.5792 | all checks held |
| 11 | 15 | 0.5830 | all checks held |
| 12 | 10 | 0.5983 | all checks held |
| 13 | 3 | 0.6279 | all checks held |
| 14 | 22 | 0.6376 | all checks held |
| 15 | 14 | 0.6426 | all checks held |
| 16 | 5 | 0.6587 | all checks held |
| 17 | 11 | 0.6639 | all checks held |
| 18 | 1 | 0.6694 | all checks held; first measured attempt |
| 19 | 24 | 0.6833 | all checks held |
| 20 | 23 | 0.6877 | all checks held |
| 21 | 19 | 0.7134 | all checks held |
| 22 | 2 | 0.7155 | all checks held |
| 23 | **21** | **0.7322** | all checks held; best of every attempt |

**Attempt 21 holds the highest reward at 0.7322. That is the mark to beat.** Its measured signature: `wall_clock_sec` 14.3905 (the shortest of any attempt), `qualifying_budget` 14.3905, `per_step_cost_ratio` 1.5700, `compute_efficiency` 0.6162, `conformance_fraction` 1.0, `rule_conformance` 1.0, `task_pass` 1.0, `validity` 1.0, both declared perturbations reached.

Only two attempts ever carried `standing_against_best_so_far: better_than_every_earlier_attempt` — attempt 2 (0.7155) and attempt 21 (0.7322). Every other measured attempt from 3 onward was recorded as `worse_than_an_earlier_attempt`. That is the plain state of the record: after attempt 2, twenty further measured submissions were made and exactly one of them improved on the standing best. Attempts 22, 23 and 24, which came directly after the best result, scored 0.6376, 0.6877 and 0.6833 — all three are **lower** than attempt 21, not incremental progress toward it. Attempt 25 then scored 0.0000, the single worst outcome in the record.

# 2. Approach classes tried

The records carry telemetry, not source. The classes below are therefore grouped by their measured signatures, which separate cleanly and are reproducible targets in themselves.

**Class A — clean, short-wall-clock runs at roughly 1.5–1.63× seed per-step cost.** Attempts 1, 2, 3, 5, 10, 14, 15, 18, 19, 21, 22, 23, 24. `per_step_cost_ratio` between 1.5134 and 1.6313, `compute_efficiency` between 0.5487 and 0.6659, all checks held, `task_pass` 1.0, both perturbations reached. Rewards span 0.5755 to 0.7322. **Every one of the top five rewards in the whole record belongs to this class**, and so does the best result. Within the class, reward tracks wall clock closely and inversely: 14.39 s → 0.7322; 17.37–17.78 s → 0.6376, 0.6694, 0.7155, 0.7134, 0.6426; 19.98–20.63 s → 0.6833, 0.6877, 0.5983, 0.6279, 0.6587, 0.5755; 23.70 s → 0.5830. The wall-clock values themselves cluster tightly around discrete levels near 14.4, 17.4, 20.1–20.6, 23.6–23.7 and 26.1 seconds, which is consistent with a coarse step- or epoch-count knob rather than a continuous one.

**Class B — cost-reduced / per-step-cheapened configurations.** Attempts 4, 8, 11, 13, 16, distinguished by `per_step_cost_ratio` at or below 1.25 and `compute_efficiency` at or above 0.76. Attempt 8 pushed furthest: ratio 0.9674 (below the seed anchor) and `compute_efficiency` 0.9679, the highest efficiency ever measured — and scored 0.5444, the lowest of any attempt that passed all its checks. Attempt 11 (ratio 1.0166, efficiency 0.8424) reached 0.6639; attempt 16 (ratio 1.1256) 0.5701; attempt 4 (ratio 1.1656, efficiency 0.8832) 0.5792; attempt 13 (ratio 1.2404) 0.5590. The class ceiling is 0.6639, well below the Class A best of 0.7322.

**Class C — submissions with executable module-level code.** Attempts 9, 17, 20. Each failed `C-API-SURFACE`, each recorded `rule_conformance` 0.8571 and `task_pass` 0.0, with rewards 0.5164, 0.5274 and 0.5107. Their other telemetry varied widely (per-step ratios 1.4988, 1.2123, 1.5804; efficiencies 0.6647, 0.8228, 0.6658), so this class spans both of the classes above and is defined solely by the surface violation.

**Class D — configurations that broke a held-out perturbation run.** Attempts 12 and 25. Both failed `C-PERTURBATION-REACHED` with `conformance_fraction` 0.5 and `task_pass` 0.0. Attempt 12 scored 0.4962. Attempt 25 additionally failed `C-PER-STEP-COST-CEILING` at a per-step cost of 3.2459× the seed anchor, crossed the red line, lost validity, and scored 0.0000.

**Class E — no measurement.** Attempts 6 and 7, both `harbor_exception`. No reward, no telemetry, no failed checks recorded. Nothing can be concluded about the approaches they carried.

# 3. Checks that failed

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions". This check has now failed three times: attempts 9, 17 and 20.** Those three attempts differ substantially in their other measured terms — per-step cost ratios of 1.4988, 1.2123 and 1.5804 and compute efficiencies of 0.6647, 0.8228 and 0.6658 span both the Class A and Class B signatures — so whatever was changed between them in the training algorithm, cost profile or schedule is demonstrably **not** what causes this check to fail. It is caused by the module's top-level layout alone: something executes at import time that is neither an import, a constant assignment, nor a permitted definition. Each occurrence forced `rule_conformance` to 0.8571 and `task_pass` to 0.0 and cost roughly 0.15–0.2 of reward relative to comparable clean runs. Every piece of work must live inside the permitted function or class definitions; no bare calls, no top-level seeding, no top-level device or config probing, no `print`, no `if __name__ == "__main__"` guard body doing work, no module-level try/except around an import that runs a statement.

**`C-PERTURBATION-REACHED` — "1 of 2 declared perturbations reached their own threshold inside their own budget". Failed twice: attempts 12 and 25.** Both set `conformance_fraction` to 0.5 and `task_pass` to 0.0. Again the two attempts differ elsewhere (per-step ratios 1.4886 and 3.2459), so the difference between them is not the cause; both declared two perturbations and satisfied only one.

**`C-PER-STEP-COST-CEILING` — "per-step cost is 3.246 times the seed anchor, above the ceiling of 3.0". Failed once: attempt 25.** This is the only red line ever crossed (`red_line_crossed` 1.0, `validity` 0.0, `zero_reason_code` 1) and the only 0.0000 reward. The ceiling is hard at 3.0× the seed anchor.

Within the perturbation runs themselves, the failed sub-checks were **`C-TARGET-REACHED`** and **`C-BUDGET-RESPECTED`**, both raised together, on both occasions.

# Perturbation-unit outcomes

Every measured attempt declared exactly two perturbations and reported two perturbation units, one of kind `held_out_variant` and one of kind `ruleset` — 46 units across the 23 measured attempts. Forty-four reached their threshold.

By kind: **the `ruleset` runs reached their threshold in all 23 measured attempts, with no failed checks, ever.** The `held_out_variant` runs reached in 21 of 23 and **failed twice — in attempt 12 and in attempt 25 — and on both occasions the failure was `C-TARGET-REACHED` together with `C-BUDGET-RESPECTED`.** The records give these runs no name, number or position, so nothing here identifies a particular run, and there is no basis for saying the failing run in one record is the same run as the failing run in the other. What can be said is the kind and the checks: **it is the held-out-variant kind that fails, and it fails by not reaching its target within its own budget.** In aggregate the perturbation stage held in 21 of 23 measured attempts (`all_perturbations_held` true), and the two failures are exactly the two attempts that also failed `C-PERTURBATION-REACHED` at the top level.

# 4. Ruled-out directions

**Driving per-step cost down toward or below the seed anchor.** Every attempt with `per_step_cost_ratio` at or under 1.25 — 8 (0.9674 → 0.5444), 11 (1.0166 → 0.6639), 16 (1.1256 → 0.5701), 4 (1.1656 → 0.5792), 13 (1.2404 → 0.5590) — scored below the best clean runs at ratio 1.5–1.6. The cheapest per-step run in the record produced the worst all-checks-held reward. Cheapening each step is not rewarded on its own; the ceiling that matters is only the hard 3.0× red line.

**Maximising `compute_efficiency` as a proxy for reward.** The two highest efficiencies measured, 0.9679 (attempt 8) and 0.8832 (attempt 4), returned 0.5444 and 0.5792, while the best attempt, 21, ran at an efficiency of only 0.6162. Efficiency and reward move in opposite directions across this record; it is not the objective.

**Longer runs.** The three longest wall clocks — 26.0978 s (attempt 8), 23.7018 s (attempt 15), 23.5810 s (attempt 17) — returned 0.5444, 0.5830 and 0.5274. No attempt above 21 seconds ever exceeded 0.5830. Extra training time has never paid for itself here.

**Any module-level executable statement.** Ruled out by three separate `C-API-SURFACE` failures, each zeroing `task_pass`.

**Anything that pushes per-step cost above 3.0× the seed anchor.** Ruled out by attempt 25: reward 0.0000, validity 0, red line crossed. Whatever made that attempt expensive must not be re-attempted at that magnitude.

**Declaring perturbations the algorithm cannot satisfy under their own budgets.** Ruled out by attempts 12 and 25, both of which lost `task_pass` entirely for one unreached held-out-variant run despite `primary_target_reached` being 1.0 in both.

# 5. Open leads

**Rebuild attempt 21's operating point and improve on it.** Target signature: wall clock near or below 14.39 s, `per_step_cost_ratio` in the 1.5–1.6 band, all module-level code restricted to imports, constants and definitions, and a training procedure robust enough that the held-out-variant perturbation reaches its threshold inside its own budget. This is the only configuration that has exceeded 0.73.

**Cut wall clock further while holding the per-step cost band.** Within the clean Class A runs, reward and wall clock are strongly inversely related across 14.39–23.70 s, and 14.39 s is both the shortest observed and the highest scoring. The discrete clustering of wall clocks near 14.4, 17.4, 20.1 and 23.7 seconds suggests a coarse step- or epoch-count parameter; the lead is to take that parameter one notch below whatever produced 14.39 s and check that `primary_target_reached` and both perturbation units still hold. The risk to watch is exactly the failure in attempts 12 and 25 — cutting the schedule too far makes the held-out-variant run miss `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, which costs more than the time saved.

**Spend the saved time nowhere else.** Attempts 1, 2 and 10 share almost identical per-step ratios (1.5134, 1.5175, 1.5152) yet returned 0.6694, 0.7155 and 0.5983, with wall clocks of 17.43, 17.45 and 20.15 s. Most of that spread is explained by the wall clock; the residual between attempts 1 and 2 at essentially identical wall clocks (0.0461 of reward) is the scale of run-to-run variation to expect. Do not chase differences smaller than that.

**Treat the API surface as a fixed checklist before submitting.** Three failures on `C-API-SURFACE` across otherwise unrelated algorithms is the single most repeated defect in the record and the cheapest one to eliminate: it is a property of the file's top level, not of the method.

**Verdict: exploit.** The best-scoring class, Class A, has not been exhausted — its top result, 0.7322, came from the shortest run ever measured, and the wall-clock trend inside the class points to further headroom below that. The correct move is to reconstruct attempt 21's configuration, keep every check green, and push the run shorter. Note for the record that the loop's earlier behaviour repeatedly resubmitted the Class B low-per-step-cost idea (attempts 4, 8, 11, 13, 16) after it had already been shown to underperform, and re-committed the same `C-API-SURFACE` top-level violation three times without changing the thing that caused it; neither is exploration and neither is exploitation, and repeating either would be wasted.
