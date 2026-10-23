# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 20 -- reward 0.8670, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All ten attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3        0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                
  5        0.8658   1.000             2 of 2         yes             74                
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
  19       0.4278   1.000             1 of 2         yes             74                
  20 *     0.8670   1.000             2 of 2         yes             74                
  21       0.0000   1.000             0 of 2         no              --                
  22       0.8594   1.000             2 of 2         yes             70                
  23       0.8170   1.000             2 of 2         yes             95                
  24       0.8426   1.000             2 of 2         yes             96                
  25       0.7757   1.000             2 of 2         yes             70                
  26       0.7607   1.000             2 of 2         yes             70                
  27       0.7394   1.000             2 of 2         yes             124               
  28       0.7387   1.000             2 of 2         yes             70                
  29       0.7667   1.000             2 of 2         yes             95                
  30       0.8350   1.000             2 of 2         yes             76                

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
  24 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 5 -- reward 0.8658, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 28 -- reward 0.7387, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 70
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 29 -- reward 0.7667, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 95
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 30 -- reward 0.8350, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-BUDGET-RESPECTED failed on attempt 21.
    C-PERTURBATION-REACHED has failed on 4 attempts (7, 12, 19, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 21.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All thirty graded records carry `measurement_status: "measured"`, so every one has a reward. Ordered worst to best:

| Rank | Attempt | reward |
|---|---|---|
| 1 (worst) | 21 | 0.0000 |
| 2 | 12 | 0.4275 |
| 3 | 19 | 0.4278 |
| 4 | 7 | 0.4911 |
| 5 | 16 | 0.7005 |
| 6 | 28 | 0.7387 |
| 7 | 27 | 0.7394 |
| 8 | 6 | 0.7580 |
| 9 | 26 | 0.7607 |
| 10 | 29 | 0.7667 |
| 11 | 4 | 0.7740 |
| 12 | 25 | 0.7757 |
| 13 | 8 | 0.7805 |
| 14 | 11 | 0.8067 |
| 15 | 2 | 0.8079 |
| 16 | 23 | 0.8170 |
| 17 | 9 | 0.8332 |
| 18 | 30 | 0.8350 |
| 19 | 18 | 0.8368 |
| 20 | 24 | 0.8426 |
| 21 | 10 | 0.8503 |
| 22 | 14 | 0.8513 |
| 23 | 15 | 0.8579 |
| 24 | 22 | 0.8594 |
| 25 | 1 | 0.8630 |
| 26 | 17 | 0.8655 |
| 27 | 13 | 0.8657 |
| 28 | 3 | 0.8657 |
| 29 | 5 | 0.8658 |
| 30 (best) | 20 | 0.8670 |

**Attempt 20 holds the highest reward at 0.8670 and is the one to beat.** Its measured profile: `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013, `wall_clock_sec` 73.66, `qualifying_budget` 73.66, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, both declared perturbations reached, no failed checks.

Only four attempts ever set a new high: 1 (0.8630, first measured), 3 (0.8657), 5 (0.8658), 20 (0.8670). Every other record carries `standing_against_best_so_far: "worse_than_an_earlier_attempt"` — twenty-five of the thirty attempts were regressions against the standing best at the time they ran, and I am reporting them as regressions, not as progress. In particular attempt 21 (0.0000), attempt 12 (0.4275), attempt 19 (0.4278) and attempt 7 (0.4911) are large drops, and attempt 16 (0.7005) is a drop of roughly 0.166 from the then-best. The last ten attempts (21 through 30) produced nothing above 0.8670; the run has been flat-to-declining since attempt 20.

Distribution note that matters for ranking: rewards 0.8630–0.8670 recur across six independent attempts (1, 17, 13, 3, 5, 20) whose top-to-bottom spread is only 0.0040. That band looks like a ceiling for the configurations tried so far, and attempt 20 sits 0.0012 above the next-best. Treat any future gain under ~0.002 as inside that noise band.

# 2. Approach classes tried

I was given only measured terms, not source. The classes below are grouped by the cost/efficiency signature the harness reported, which is the only evidence of what each submission did. Records that behaved identically are collapsed into one entry.

**Class A — moderate per-step cost, ~74 s wall clock (the reliable band).**
Signature: `per_step_cost_ratio` 0.94–1.07, `compute_efficiency` 0.66–0.75, `wall_clock_sec` 70–77, `qualifying_budget` roughly equal to wall clock (~70–76). Attempts 1, 2, 3, 5, 9, 10, 13, 17, 22, 25, 30. Rewards: 0.8630, 0.8079, 0.8657, 0.8658, 0.8332, 0.8503, 0.8657, 0.8655, 0.8594, 0.7757, 0.8350. Every member passed every check and held both perturbations. This class is the most reproducible thing in the record: it never once failed a check, and eight of its eleven members landed between 0.8332 and 0.8658. It contains three of the four all-time highs (1, 3, 5). Its practical ceiling is ~0.8658.

**Class B — aggressive per-step cost reduction / high compute efficiency.**
Signature: `per_step_cost_ratio` 0.67–0.77, `compute_efficiency` 0.88–1.00. Attempts 4, 11, 12, 14, 16, 18, 19, 20, 23, 26, 28. Rewards: 0.7740, 0.8067, 0.4275, 0.8513, 0.7005, 0.8368, 0.4278, **0.8670**, 0.8170, 0.7607, 0.7387. This class produced the single best result (attempt 20) and also two of the three worst non-zero results (12 and 19, both of which lost a held-out perturbation). It is high-variance: its spread is 0.4275 to 0.8670. Two members reached `compute_efficiency` exactly 1.0 — attempt 11 (0.8067, all checks held) and attempt 19 (0.4278, held-out variant lost) — so maximal efficiency neither guarantees nor forbids a good score. Attempts 16 (efficiency 0.9805) and 26 (efficiency 0.9881) held every check and still scored only 0.7005 and 0.7607, which shows the reward is not a monotone function of compute efficiency: something the terms do not expose is also being scored, and squeezing per-step cost alone can move it the wrong way.

**Class C — mid-cost hybrid.**
Signature: `per_step_cost_ratio` 0.81–0.94 with `compute_efficiency` 0.80–0.94. Attempts 15 (0.8579), 27 (0.7394), 29 (0.7667), 12 (0.4275, and it lost a perturbation). Only attempt 15 was competitive. No member beat Class A's ceiling.

**Class D — extended wall clock / late qualification.**
Signature: `qualifying_budget` above 90 s. Attempts 8 (98.60 s, 0.7805), 23 (94.75 s, 0.8170), 24 (96.18 s, 0.8426), 27 (123.74 s qualifying inside 148.19 s wall, 0.7394), 29 (95.38 s, 0.7667). Every member scored below 0.8426 and all five are regressions. Taking longer to reach the qualifying row costs reward even when every check passes.

**Class E — restructured module surface.**
Attempt 6 alone. It is the only record with `rule_conformance` below 1.0 (0.8571) and the only one to fail `C-API-SURFACE`. Reward 0.7580 with `task_pass` 0.0, despite both perturbations reaching and `primary_target_reached` 1.0. Its `wall_clock_sec` was 70.37 against a `qualifying_budget` of 45.82 and a `per_step_cost_ratio` of 1.4094 — the highest per-step cost in the record.

**Class F — runaway / divergent configuration.**
Attempt 21 alone. `wall_clock_sec` 1691.67 (over twenty times the ~74 s norm), `qualifying_budget` "not-measured", `primary_target_reached` 0.0, `zero_reason_code` 4, reward 0.0000. Its `compute_efficiency` reads 0.9829 and `per_step_cost_ratio` 0.6727, i.e. cheap per step but never converging — the run burned its budget without any evaluation row crossing threshold. This is the only genuine zero and the only record where the seed perturbation also failed.

# 3. Checks that failed

Twenty-four of thirty records have an empty `failed_checks`. Four distinct check identifiers appear.

**`C-PERTURBATION-REACHED` — failed 4 times (attempts 7, 12, 19, 21).** This is the dominant finding.
- Attempts 7, 12, 19, reason verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget."*
- Attempt 21, reason verbatim: *"0 of 2 declared perturbations reached their own threshold inside their own budget."*

These four attempts sit in three different approach classes (7 is Class A's cost band, 12 is the mid-cost hybrid, 19 is aggressive Class B, 21 is the runaway). Their `per_step_cost_ratio` values are 0.9657, 0.8114, 0.6884 and 0.6727, and their `compute_efficiency` values are 0.6954, 0.8464, 1.0000 and 0.9829 — the full range. **Whatever was changed between those four attempts is not what is causing this check to fail.** Sweeping the cost/efficiency knob does not address it; the failure recurs at every setting of that knob and is absent at every setting of it too.

Note the reward consequence: this check failing drops `conformance_fraction` to 0.5 and `task_pass` to 0.0, and rewards collapse to 0.4275–0.4911 even though `primary_target_reached` stayed 1.0 and `rule_conformance` stayed 1.0. Losing one declared perturbation costs roughly half the reward. Fixing this check is worth more than any tuning gain observed anywhere in the record.

**`C-BUDGET-RESPECTED` — failed at the primary level once (attempt 21), reason: *"no qualifying row, so no budget position exists."*** It also appears at the perturbation-unit level 5 times (see section on units below).

**`C-TARGET-REACHED` — failed at the primary level once (attempt 21), reason: *"no evaluation row crosses the threshold in the declared direction."*** It also appears at the perturbation-unit level 4 times.

**`C-API-SURFACE` — failed once (attempt 6), reason verbatim: *"module-level statements outside imports, constants, and permitted definitions."*** This is a pure structural violation, not a learning failure: attempt 6 reached the primary target and both perturbations. It is the only record with `rule_conformance` < 1.0. The fix is mechanical — keep the module body to imports, constants, and permitted definitions only, and put all executable work inside the permitted function/class definitions. Twenty-nine of thirty records satisfied it, so the stub's default structure satisfies it; this failure came from something added at module scope in that one attempt.

**Perturbation-unit outcomes.** Every record declared 2 perturbations (`perturbations_declared` 2.0), one of kind `held_out_variant` and one of kind `seed`. Across the thirty records that is 60 held-out runs; 55 reached their threshold and 5 did not. By kind:

- **`held_out_variant`: reached in 26 of 30 records, failed in 4** — attempts 7, 12, 19, 21. Failing checks on those units: attempt 7 stopped on `C-BUDGET-RESPECTED` alone; attempts 12, 19 and 21 stopped on both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. This kind is where essentially all the fragility lives.
- **`seed`: reached in 29 of 30 records, failed in 1** — attempt 21 only, on both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, in the record where the whole run diverged. Seed robustness is otherwise total.

The instructive contrast is attempt 7: it failed the held-out variant on `C-BUDGET-RESPECTED` only — the variant was on track but ran out of budget before qualifying — while sitting squarely inside Class A's safe cost band (`per_step_cost_ratio` 0.9657). So held-out-variant failure is not caused solely by aggressive speed settings; attempts 12 and 19 are aggressive and failed, but attempt 11 at `compute_efficiency` 1.0 held both units cleanly. The pattern the terms support is that the held-out variant has less margin than the primary run and is the first thing to lose when either budget headroom or convergence margin is thin. The runs are not identified, so nothing here should be read as claiming any particular held-out run is the same one across two records.

# 4. Ruled-out directions

**Maximising `compute_efficiency` / minimising `per_step_cost_ratio` as the primary lever.** Ruled out as a reliable path. Attempt 11 hit `compute_efficiency` 1.0 with all checks held and scored 0.8067 — below the 0.8658 that Class A reached at `compute_efficiency` 0.6926. Attempt 16 at 0.9805 scored 0.7005 and attempt 26 at 0.9881 scored 0.7607, both with clean check sheets. The correlation between efficiency and reward is not positive across the record; pushing this knob alone has repeatedly produced regressions.

**Very low per-step cost (`per_step_cost_ratio` below ~0.70).** Ruled out as unsafe. The three records at 0.6727, 0.6884 and 0.6934 gave rewards 0.0000, 0.4278 and 0.7740; two of the three lost the held-out variant on `C-TARGET-REACHED`/`C-BUDGET-RESPECTED`. Attempt 20's 0.7013 is the lowest ratio that ever produced a top score, and it is right at the edge of the failure region.

**Extending wall clock or letting the qualifying row arrive late (`qualifying_budget` above ~90 s).** Ruled out. All five such records (8, 23, 24, 27, 29) scored 0.7394–0.8426, every one a regression, and none approached 0.8658. Attempt 27's 123.74 s qualifying budget inside a 148.19 s wall clock scored 0.7394 despite passing every check. Longer runs are penalised even when correct.

**High per-step cost (`per_step_cost_ratio` above ~1.09).** Ruled out. The only record above 1.09 is attempt 6 at 1.4094, which also carried the `C-API-SURFACE` violation, and attempts at 1.0722, 1.0848 and 1.0864 scored 0.8630, 0.7805 and 0.8350 — no upside over the 0.94–0.98 band.

**Adding executable statements at module scope.** Ruled out by `C-API-SURFACE` on attempt 6: *"module-level statements outside imports, constants, and permitted definitions."* This zeroes `task_pass` and drops `rule_conformance` to 0.8571 regardless of how well the model trains. Do not restructure the module surface at all.

**Whatever configuration produced attempt 21.** Ruled out absolutely. `wall_clock_sec` 1691.67, no qualifying row at all, `qualifying_budget` "not-measured", `zero_reason_code` 4, both perturbation kinds failing `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, reward 0.0000. Its per-step cost was low (0.6727) while it never converged, which is the signature of a step size, schedule or stopping condition that trains cheaply but does not move the metric in the declared direction. Any change that risks non-convergence must be guarded by a hard wall-clock cap near ~75 s.

**Re-running the Class A moderate band unchanged.** Not ruled out for safety, but ruled out as a route to a new high. Eleven attempts in that band produced a maximum of 0.8658 with three attempts clustered at 0.8655–0.8658. It has stopped improving; re-entering it reproduces ~0.865 and nothing more.

# 5. Open leads

**Lead 1 — reconstruct attempt 20's operating point exactly.** It is the only record that combined high `compute_efficiency` (0.9633) with a `per_step_cost_ratio` of 0.7013, a ~73.7 s wall clock, a `qualifying_budget` equal to the wall clock, and a fully clean check sheet. That combination beat the entire Class A plateau. The nearest neighbours in the fast band — attempts 14 (ratio 0.6997, efficiency 0.9705, 0.8513) and 4 (ratio 0.6934, efficiency 0.9681, 0.7740) — are close in cost signature but far apart in reward, so the differentiator is not the cost knob. Reproduce the fast configuration and vary only the learning-rate/schedule/regularisation side while holding `per_step_cost_ratio` near 0.70 and wall clock near 73.7 s.

**Lead 2 — buy margin for the held-out variant without slowing the primary run.** `C-PERTURBATION-REACHED` is the highest-value fix in the record: it cost roughly half the reward each of the four times it fired, and it fired at every point on the cost/efficiency spectrum. Attempt 7's unit failed on `C-BUDGET-RESPECTED` alone, meaning the variant was heading in the right direction but did not qualify in time. Practical moves: make the stopping rule adaptive rather than fixed-step so a slower-converging variant keeps training until it qualifies; ensure the qualifying evaluation is checked early and often enough that a run crossing threshold mid-training is recorded before its budget expires; and keep a safety factor between typical qualifying time (~70–75 s) and the budget. Records where `qualifying_budget` sat well under the wall clock while everything held — attempts 9 (49.89 s budget, 74.39 s wall, 0.8332) and 14 (74.15/74.15, 0.8513) — suggest early qualification is achievable and costs nothing.

**Lead 3 — separate the two things the reward is tracking.** `compute_efficiency` and `per_step_cost_ratio` cannot explain the spread between attempt 16 (efficiency 0.9805, reward 0.7005) and attempt 20 (efficiency 0.9633, reward 0.8670), both clean. There is a second scored quantity the terms do not name — most plausibly final metric quality or margin above threshold. The lead is to hold the cost profile fixed at attempt 20's values and move only quality-side choices (architecture width/depth, optimiser, augmentation, LR schedule shape, warmup, final-epoch averaging), so the next measurement isolates that dimension for the first time.

**Lead 4 — mild ensembling or weight averaging inside the existing time envelope.** Class A shows ~74 s runs reliably clear the target with room to spare (`qualifying_budget` ≈ wall clock ≈ 74 s, and 9's budget was 49.89 s). If the target is reached at ~50 s, the remaining ~24 s could go to EMA/SWA of weights or a short fine-tune at reduced LR, raising margin above threshold for both the primary and the held-out variant simultaneously — which serves Leads 2 and 3 at once. Any such change must keep the module surface untouched to avoid `C-API-SURFACE`, and must keep total wall clock near 74 s to avoid the Class D penalty.

**Guardrails for any attempt.** Keep all executable code inside permitted definitions (`C-API-SURFACE`). Cap wall clock near 75 s. Do not go below `per_step_cost_ratio` ≈ 0.70. Verify the qualifying row appears well before budget exhaustion so the held-out variant inherits the same headroom.

---

**Call: exploit.** The record contains a scoring approach that is not yet exhausted — attempt 20 at 0.8670, the fast/high-efficiency profile with a clean check sheet — and the single largest identified loss is a specific, named, four-times-repeated check failure (`C-PERTURBATION-REACHED`, driven by the `held_out_variant` unit missing `C-BUDGET-RESPECTED` and `C-TARGET-REACHED`) that no attempt has yet addressed directly. Exploiting means rebuilding attempt 20's operating point and adding held-out-variant margin, not re-scanning the cost knob. Earlier work repeatedly re-entered the same cost/efficiency sweep and re-measured the same 0.86 plateau or re-triggered the same perturbation failure without changing what causes it; that is neither exploration nor exploitation and should not be repeated.
