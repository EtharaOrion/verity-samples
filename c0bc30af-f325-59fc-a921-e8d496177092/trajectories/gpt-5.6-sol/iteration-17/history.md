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

    All 12 attempts since have scored lower than it.
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
  11 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 15 -- reward 0.8579, worse than an earlier attempt
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED has failed on 2 attempts (7, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All seventeen records carry `measurement_status: "measured"`, so every one has a reward. None produced an absent measurement, and none crossed a red line (`red_line_crossed` is 0.0 throughout, `zero_reason_code` is 0 throughout, `validity` is 1.0 throughout).

Ordered worst to best by reward:

| Rank | Attempt | reward | Standing as reported |
|---|---|---|---|
| 1 (worst) | 12 | 0.4275 | worse than an earlier attempt |
| 2 | 7 | 0.4911 | worse than an earlier attempt |
| 3 | 16 | 0.7005 | worse than an earlier attempt |
| 4 | 6 | 0.7580 | worse than an earlier attempt |
| 5 | 4 | 0.7740 | worse than an earlier attempt |
| 6 | 8 | 0.7805 | worse than an earlier attempt |
| 7 | 11 | 0.8067 | worse than an earlier attempt |
| 8 | 2 | 0.8079 | worse than an earlier attempt |
| 9 | 9 | 0.8332 | worse than an earlier attempt |
| 10 | 10 | 0.8503 | worse than an earlier attempt |
| 11 | 14 | 0.8513 | worse than an earlier attempt |
| 12 | 15 | 0.8579 | worse than an earlier attempt |
| 13 | 1 | 0.8630 | first measured attempt |
| 14 | 17 | 0.8655 | worse than an earlier attempt |
| 15 | 13 | 0.8657 | worse than an earlier attempt |
| 16 | 3 | 0.8657 | better than every earlier attempt (at the time) |
| 17 (best) | 5 | 0.8658 | better than every earlier attempt |

**Attempt 5 holds the highest reward, 0.8658. That is the number to beat.**

Two things must be stated plainly rather than softened. First, only three records ever improved on the running best: attempt 1 (first measurement, 0.8630), attempt 3 (0.8657), and attempt 5 (0.8658). Every other record — thirteen of the remaining fourteen, and all twelve that came after attempt 5 — is marked `worse_than_an_earlier_attempt`. That is regression, not progress, and includes the most recent record, attempt 17 at 0.8655, which sits below attempt 5's 0.8658. Second, the improvement from attempt 3 (0.8657110) to attempt 5 (0.8658084) is under 0.0001 and should not be read as a real gain; attempts 3, 5, 13 and 17 (0.8657, 0.8658, 0.8657, 0.8655) form a single flat cluster within 0.0003 of each other. The top of this search is a plateau, not a rising curve.

Secondary terms worth carrying forward for the best attempts: attempt 5 had `compute_efficiency` 0.6926, `per_step_cost_ratio` 0.9581, `wall_clock_sec` 74.38, `qualifying_budget` 74.38, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `all_perturbations_held` true. Attempts 3, 13 and 17 sit in the same band (`per_step_cost_ratio` 0.94–0.98, `compute_efficiency` 0.68–0.73, wall clock 74–76 s).

# 2. Approach classes tried

I have only the graded numeric terms, not the source of any submission, so these classes are grouped by their measured signature. Records with the same signature and the same outcome are one entry.

**Class A — mid-cost configurations, `per_step_cost_ratio` ≈ 0.94–0.99 with `compute_efficiency` ≈ 0.68–0.75.** Attempts 2 (0.8079), 3 (0.8657), 5 (0.8658), 9 (0.8332), 10 (0.8503), 13 (0.8657), 17 (0.8655). This class contains every attempt in the top cluster and the best result overall. All passed `task_pass` 1.0 with full conformance and both perturbations held. Note the spread inside the class is wide (0.8079 to 0.8658) despite near-identical cost signatures, which means the ranking inside this class is driven by something the cost terms do not expose — the quality/target-margin side, not the speed side.

**Class B — aggressive speed-up, `per_step_cost_ratio` ≈ 0.69–0.71 with `compute_efficiency` 0.96–1.00.** Attempts 4 (0.7740), 11 (0.8067, `compute_efficiency` exactly 1.0), 14 (0.8513), 16 (0.7005). Every member is below the plateau despite maximal or near-maximal efficiency. Attempt 11 is the decisive datum: perfect `compute_efficiency` of 1.0 bought only 0.8067, well under attempt 5's 0.8658 at `compute_efficiency` 0.6926. Cutting per-step cost to ~0.70 of reference trades away more reward than the efficiency term returns.

**Class C — high per-step cost, `per_step_cost_ratio` > 1.0.** Attempts 1 (1.0723, 0.8630), 8 (1.0848, wall clock 98.60 s, 0.7805), 6 (1.4094, 0.7580, and the only `C-API-SURFACE` failure). Attempt 1 is respectable but never matched by later members; attempt 8's 98.60 s wall clock — the longest recorded, against a ~74 s norm — corresponds to the class's worst conforming score.

**Class D — tightened qualifying budget / earlier stopping, where `qualifying_budget` falls well below `wall_clock_sec`.** Attempt 9 (budget 49.89 vs wall clock 74.39, reward 0.8332) and attempt 6 (budget 45.82 vs wall clock 70.37, reward 0.7580). Both are below the plateau. Shrinking the qualifying budget while the run still consumes ~74 s of wall clock did not convert into reward.

**Class E — configurations that broke the held-out perturbation's budget.** Attempts 7 (0.4911) and 12 (0.4275), the two worst results on record. Both show `all_perturbations_held: false`, `conformance_fraction` 0.5, `task_pass` 0.0, and the primary target still reached (`primary_target_reached` 1.0). This class costs roughly 0.37–0.44 reward relative to the plateau and is the single largest destroyer of score observed.

**Class F — the middle-efficiency compromise.** Attempt 15 alone: `per_step_cost_ratio` 0.9424 (Class A band) together with `compute_efficiency` 0.9355 (Class B band), reward 0.8579. This is the best result any high-efficiency configuration achieved, and it is still below the plateau — but it is much closer than the rest of Class B, and it is the only sample in that corner of the space.

# 3. Checks that failed

Fifteen of seventeen records have an empty `failed_checks`. Three distinct check identifiers failed, across three records.

- **`C-API-SURFACE`** — failed once, at attempt 6. Verifier's reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions."* This drove `rule_conformance` down to 0.8571 and `task_pass` to 0.0, yet the record still measured 0.7580. Because it appears only once, nothing can be inferred about which edit caused it beyond the reason given: the submitted module executed statements at import time that were not imports, constants, or permitted definitions.

- **`C-PERTURBATION-REACHED`** — **failed twice**, at attempts 7 and 12. Verifier's reason both times, verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This is the finding that matters most. Two attempts separated by four other records failed the identical check with the identical reason, and both had `rule_conformance` 1.0 and `primary_target_reached` 1.0 — the primary run was fine both times. Whatever was changed between attempt 7 and attempt 12 is **not** what causes this failure; the cause survived that change untouched and must be addressed directly rather than by further variation on the surrounding configuration.

- **`C-BUDGET-RESPECTED`** — failed twice, once inside attempt 7's perturbation set and once inside attempt 12's. In both records it is attached to a perturbation unit of kind `held_out_variant`, never to a `seed` unit. Again: two failures of the same named check across two attempts means the intervening changes did not touch its cause.

- **`C-TARGET-REACHED`** — failed once, inside attempt 12's perturbation set, on a `held_out_variant` unit, alongside `C-BUDGET-RESPECTED` on that same unit.

**Perturbation outcomes by kind and in aggregate.** Every record declared 2 perturbations (`perturbations_declared` 2.0), one of kind `seed` and one of kind `held_out_variant`, giving 34 units across the seventeen records. Aggregate: 32 of 34 units reached their threshold; 2 did not. By kind: **`seed` units reached in all seventeen records, with no failed check ever recorded against a unit of that kind.** **`held_out_variant` units reached in fifteen of seventeen records and failed in two** — at attempt 7 on `C-BUDGET-RESPECTED`, and at attempt 12 on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` together. The held-out-variant kind is the only kind that has ever failed, and `C-BUDGET-RESPECTED` is the check it fails on in both instances. The runs are not identified beyond their kind, so nothing here asserts that the failing unit in attempt 7 is the same underlying run as the failing unit in attempt 12; only the kind and the check are known.

# 4. Ruled-out directions

- **Maximising `compute_efficiency` / driving `per_step_cost_ratio` down to ~0.70 (Class B).** Ruled out as a scoring strategy. Attempt 11 reached `compute_efficiency` 1.0 and scored 0.8067; attempt 16 reached 0.9805 and scored 0.7005 — the fourth-worst result on record. Meanwhile the best result, attempt 5, ran at `compute_efficiency` 0.6926. Four independent samples in this band all landed below the plateau, so the efficiency term does not compensate for what the speed-up gives away.

- **Running slower / longer than the reference (Class C at `per_step_cost_ratio` ≥ 1.08).** Ruled out. Attempt 8 at ratio 1.0848 and 98.60 s wall clock scored 0.7805, and attempt 6 at ratio 1.4094 scored 0.7580. The only decent member is attempt 1 at ratio 1.0723 (0.8630), and it was superseded by the cheaper Class A cluster. Spending more per step is not where the remaining 0.13 of headroom lives.

- **Shrinking `qualifying_budget` below wall clock (Class D).** Ruled out on two samples: attempt 9 (budget 49.89, reward 0.8332) and attempt 6 (budget 45.82, reward 0.7580). Neither approached the plateau, and the budget reduction did not reduce actual wall clock, which stayed near 74 s and 70 s respectively.

- **Any configuration that risks the held-out variant's budget (Class E).** Ruled out absolutely. Attempts 7 and 12 are the two worst records at 0.4911 and 0.4275, roughly 0.38–0.44 below the plateau, purely because one of two perturbations missed its threshold inside its own budget. Both had a perfectly healthy primary run (`primary_target_reached` 1.0). Protecting the held-out-variant run dominates every other consideration; no efficiency or quality gain observed anywhere in these records is worth a fraction of that loss.

- **Module-level executable code.** Ruled out by attempt 6's `C-API-SURFACE` failure with the reason "module-level statements outside imports, constants, and permitted definitions." The submission module must contain only imports, constants, and permitted definitions at top level; all work belongs inside the defined entry points.

- **Further blind re-sampling inside the Class A plateau.** Ruled out as a source of gain, though not as a fallback. Attempts 3, 5, 13 and 17 span 0.8655–0.8658, a range of 0.0003. Additional draws from that same band are indistinguishable from measurement noise and cannot be expected to move the number.

# 5. Open leads

- **Rebuild the Class A regime as the floor, then vary one thing.** The target profile is attempt 5's: `per_step_cost_ratio` in 0.95–0.98, `compute_efficiency` 0.69–0.73, wall clock ≈ 74 s, `qualifying_budget` equal to wall clock (no artificial budget squeeze), `task_pass` 1.0, `rule_conformance` 1.0, both perturbations held. Anything that leaves this regime has, on the evidence of thirteen records, lost reward.

- **The unexplained spread inside Class A is the real lead.** Attempts 2 (0.8079), 9 (0.8332) and 10 (0.8503) share the plateau's cost signature yet score 0.015–0.058 below it. Since `compute_efficiency` and `per_step_cost_ratio` are nearly matched across those and the plateau members, the difference is coming from the quality/margin side of the reward — how far past the primary and held-out thresholds the run lands, not how fast it gets there. Work the optimisation/schedule quality at fixed cost, and read `compute_efficiency` and `per_step_cost_ratio` only as guardrails confirming you stayed in the regime.

- **Attempt 15's corner is the one under-sampled region.** It combined a Class A cost ratio (0.9424) with a Class B efficiency (0.9355) and scored 0.8579 — the best of any high-efficiency configuration and only 0.008 under the plateau, on a single sample. If any efficiency gain is to be had without paying for it, this is the corner: keep `per_step_cost_ratio` above ~0.94 and let `compute_efficiency` rise, rather than buying efficiency by pushing the cost ratio to 0.70.

- **Harden the held-out-variant path against `C-BUDGET-RESPECTED` explicitly.** This is the twice-repeated failure and the biggest single lever. Because the check has now failed on two separate attempts with the same reason and the same unit kind, treat it as an unaddressed structural cause, not a tuning artefact: the held-out variant must reach its own threshold within its own budget, and it will be slower or harder than the primary run. Concretely, do not size step counts, schedules or stopping rules from the primary run's timing; give the per-run loop an internal budget check that adapts (fewer steps, earlier convergence criterion) rather than one that assumes the primary run's cost profile carries over. A conforming run that holds both perturbations at 0.8503 beats a faster one that drops a perturbation at 0.4275 by a factor of two.

- **Keep the module surface clean.** Only imports, constants, and permitted definitions at top level, so `C-API-SURFACE` cannot recur.

- **Determinism and seed handling need no work.** The `seed` perturbation kind reached its threshold in all seventeen records and has never failed a check. Do not spend effort there.

**Call: exploit.** The reason is not that the plateau is still climbing — it is not; attempts 3, 5, 13 and 17 are flat within 0.0003, and every record after attempt 5 regressed. The reason is that every structurally different direction already tried scored strictly worse: the speed-up class capped at 0.8513, the high-cost class at 0.8630 and falling, the budget-squeeze class at 0.8332, and the perturbation-breaking class collapsed to 0.4275–0.4911. So the move is to restore the attempt-5 regime exactly, hold both perturbations, and push on the one axis with visible unexplained variance — the quality margin at fixed cost — plus attempt 15's untested efficiency corner. What must not be repeated is another undifferentiated draw from the plateau, or another configuration that lets the held-out variant miss its budget; the latter has now failed twice on the same named check and the changes made between those two attempts demonstrably did not address it.
