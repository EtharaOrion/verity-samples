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

    All four attempts since have scored lower than it.
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
  18 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 22 -- reward 0.8594, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 70
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 23 -- reward 0.8170, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 95
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 24 -- reward 0.8426, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 96
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-BUDGET-RESPECTED failed on attempt 21.
    C-PERTURBATION-REACHED has failed on 4 attempts (7, 12, 19, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 21.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

All twenty-four records carry `measurement_status: "measured"`, so every one has a reward and none is a "no measurement" case. Ordered worst to best by reward:

| Rank | Attempt | Reward | Note |
|---|---|---|---|
| 1 | 21 | 0.0000 | true measured zero (`zero_reason_code` 4), not a missing measurement |
| 2 | 12 | 0.4275 | held-out variant did not hold |
| 3 | 19 | 0.4278 | held-out variant did not hold |
| 4 | 7 | 0.4911 | held-out variant did not hold |
| 5 | 16 | 0.7005 | all checks held |
| 6 | 6 | 0.7580 | `C-API-SURFACE` failure |
| 7 | 4 | 0.7740 | all checks held |
| 8 | 8 | 0.7805 | all checks held |
| 9 | 11 | 0.8067 | all checks held |
| 10 | 2 | 0.8079 | all checks held |
| 11 | 23 | 0.8170 | all checks held |
| 12 | 9 | 0.8332 | all checks held |
| 13 | 18 | 0.8368 | all checks held |
| 14 | 24 | 0.8426 | all checks held |
| 15 | 10 | 0.8503 | all checks held |
| 16 | 14 | 0.8513 | all checks held |
| 17 | 15 | 0.8579 | all checks held |
| 18 | 22 | 0.8594 | all checks held |
| 19 | 1 | 0.8630 | all checks held |
| 20 | 17 | 0.8655 | all checks held |
| 21 | 13 | 0.8657 | full precision 0.86565613 |
| 22 | 3 | 0.8657 | full precision 0.86571101 |
| 23 | 5 | 0.8658 | all checks held |
| 24 | 20 | **0.8670** | best of all; `standing_against_best_so_far: better_than_every_earlier_attempt` |

**Attempt 20 holds the highest reward at 0.8670 and is the one to beat.** Its measured profile: `per_step_cost_ratio` 0.7013, `compute_efficiency` 0.9633, `wall_clock_sec` 73.66, `qualifying_budget` 73.66, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, both declared perturbations reached, no failed checks.

Only four attempts ever improved on everything before them: 1 (first measured), 3 (0.8657), 5 (0.8658), 20 (0.8670). Every other attempt carries `standing_against_best_so_far: worse_than_an_earlier_attempt` — that is a regression against the running best, and it should be read as exactly that and not as progress. In particular attempts 21 through 24, all of which came after the best result, scored 0.0000, 0.8594, 0.8170 and 0.8426 — all lower than 0.8670. Nothing since attempt 20 has matched it.

The reward ceiling of the clean cluster sits in a tight band: attempts 17, 13, 3, 5 and 20 span 0.8655–0.8670, a spread of 0.0015 across five structurally different-looking configurations. Movement now is in the third and fourth decimal.

## 2. Approach classes tried

Grouping by the measured fingerprints (cost ratio, compute efficiency, budget, and which checks held), the distinct classes are:

**Class A — baseline-cost, all-checks-held runs.** `per_step_cost_ratio` in the 0.94–1.08 band, `compute_efficiency` 0.657–0.751, wall clock clustered near 70–76 s. Attempts 1, 2, 3, 5, 9, 10, 13, 15, 17, 22 and 24 sit here. Rewards 0.8079–0.8658. This class contains most of the top of the table (3, 5, 13, 17, 22, 1) and is the reliable regime: it never failed a check.

**Class B — aggressive per-step cost reduction.** `per_step_cost_ratio` pushed down to 0.688–0.767 with `compute_efficiency` 0.88–1.00. Attempts 4, 11, 14, 16, 18, 19, 20 and 23 sit here. Rewards are the widest-spread of any class: the single best result (20, 0.8670) and also 0.8513, 0.8368, 0.8170, 0.8067, 0.7740, 0.7005, plus the perturbation failure at 0.4278. Cheapening the step is not itself harmful — the best result lives here — but it is clearly not sufficient, since attempt 11 hit `compute_efficiency` 1.0 for only 0.8067 and attempt 16 hit 0.9805 for only 0.7005.

**Class C — extended-budget runs.** `qualifying_budget` and wall clock pushed to 94–99 s: attempts 8 (98.60 s, 0.7805), 23 (94.75 s, 0.8170), 24 (96.18 s, 0.8426). All three held every check and all three landed below the 0.865 band. Spending more wall clock bought nothing.

**Class D — module-level code at import time.** Attempt 6 only. `rule_conformance` dropped to 0.8571, `task_pass` 0, reward 0.7580, with the `C-API-SURFACE` failure described below. Notably both perturbation units still reached, so this was a surface-shape defect, not a learning defect.

**Class E — configurations whose held-out variant run does not finish inside its own budget.** Attempts 7, 12 and 19. Rewards 0.4911, 0.4275, 0.4278. In all three the primary run passed (`primary_target_reached` 1.0) and `rule_conformance` stayed 1.0, but `conformance_fraction` fell to 0.5 and reward roughly halved. This is the single most expensive failure mode measured.

**Class F — the runaway.** Attempt 21 only. `wall_clock_sec` 1691.67 against a normal ~74 s, `qualifying_budget` "not-measured", `primary_target_reached` 0.0, `conformance_fraction` 0.0, reward 0.0000 with `zero_reason_code` 4. Both declared perturbation units failed as well. Whatever this configuration was, it never produced a qualifying evaluation row at all.

## 3. Checks that failed

Four distinct check identifiers appear across the records.

**`C-PERTURBATION-REACHED` — failed four times (attempts 7, 12, 19, 21).** Reason on 7, 12 and 19: "1 of 2 declared perturbations reached their own threshold inside their own budget". Reason on 21: "0 of 2 declared perturbations reached their own threshold inside their own budget". This is the finding that matters most. It has now failed four separate times, across attempts that differ substantially in their other measured terms — attempt 7 ran 50.05 s with `per_step_cost_ratio` 0.9657 and `compute_efficiency` 0.6954; attempt 12 ran 74.11 s at 0.8114 / 0.8464; attempt 19 ran 73.65 s at 0.6884 / 1.0000. Those are three different cost regimes and three different efficiency levels producing the identical failure, so **whatever was being changed between those attempts is not what is causing this check to fail.** The lever that moves it has not been touched yet.

**`C-BUDGET-RESPECTED` — failed at the perturbation-unit level in attempts 7, 12, 19 and 21, and additionally at the top level in attempt 21** with reason "no qualifying row, so no budget position exists". This is the proximate check inside every single failing held-out-variant run; it is the one check present in all four.

**`C-TARGET-REACHED` — failed at the perturbation-unit level in attempts 12, 19 and 21, and at the top level in attempt 21** with reason "no evaluation row crosses the threshold in the declared direction". Note attempt 7's failing unit stopped on `C-BUDGET-RESPECTED` alone, without `C-TARGET-REACHED`: there the variant was on track but ran out of budget, whereas in 12 and 19 it neither reached the threshold nor stayed in budget.

**`C-API-SURFACE` — failed once (attempt 6),** reason "module-level statements outside imports, constants, and permitted definitions". `rule_conformance` 0.8571 and `task_pass` 0 followed from it even though both perturbation units reached and the primary target was met. One occurrence, cheap to avoid, and it must not recur.

## Perturbation-unit outcomes

Every record declared exactly two perturbation units, one of kind `held_out_variant` and one of kind `seed`. Aggregate across the twenty-four records: 48 units, of which 5 failed to reach.

By kind:
- **`held_out_variant`: 4 failures out of 24.** Stopped by `C-BUDGET-RESPECTED` in all four cases, and additionally by `C-TARGET-REACHED` in three of the four. This is the fragile kind.
- **`seed`: 1 failure out of 24,** and that one occurred only in the attempt that also failed everything at top level, stopped by both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. Outside that collapse, the seed perturbation has held every time.

The held-out runs are not identified in the records — there is no name, number or position for any of them — so nothing here claims that a particular run recurred across attempts. The statement that holds is by kind: it is the `held_out_variant` kind that fails, and it fails on `C-BUDGET-RESPECTED`, sometimes together with `C-TARGET-REACHED`.

## 4. Ruled-out directions

**Module-level executable code in the submission.** Ruled out by attempt 6's `C-API-SURFACE` failure, reason "module-level statements outside imports, constants, and permitted definitions". Keep the module body to imports, constants and permitted definitions; put all work inside the required entry points.

**Buying reward with a larger time budget.** Ruled out by Class C: attempts 8, 23 and 24 ran `qualifying_budget` at 98.60, 94.75 and 96.18 s and scored 0.7805, 0.8170 and 0.8426 — every one below the 0.865 band that ~70–76 s runs reach. Longer runs measured strictly worse; `compute_efficiency` on those was 0.657, 0.886 and 0.696 respectively.

**Treating `compute_efficiency` as the thing to maximise.** Ruled out because the correlation breaks in both directions. `compute_efficiency` 1.0 produced 0.8067 (attempt 11) and 0.4278 (attempt 19); 0.9805 produced 0.7005 (attempt 16); 0.9681 produced 0.7740 (attempt 4). Meanwhile `compute_efficiency` 0.6926 produced 0.8658 (attempt 5) and 0.6922 produced 0.8657 (attempt 3). Efficiency contributes, but a configuration that trades away primary quality for it loses more than it gains.

**Whatever produced attempt 21.** A 1691.67 s wall clock, `qualifying_budget` "not-measured", no evaluation row crossing the threshold in the declared direction, both perturbation units failed, reward 0.0000. Ruled out unconditionally: it is the only true zero on the board and it is 22× the normal wall clock.

**Shipping any configuration whose held-out variant is near its budget edge.** Ruled out by Class E: attempts 7, 12 and 19 all kept `primary_target_reached` 1.0 and `rule_conformance` 1.0 yet dropped to 0.4911, 0.4275 and 0.4278 because `conformance_fraction` halved. The cost of a single unreached perturbation is on the order of 0.44 reward — roughly half of everything the primary run earned. No primary-side gain measured anywhere in this record set is within an order of magnitude of that.

**Simply re-running Class A at baseline cost and hoping.** Not ruled out as unsafe, but ruled out as an improvement path: attempts 1, 3, 5, 13, 17 and 22 span 0.8630–0.8658 and have stopped separating. Repeating that regime unchanged reproduces the plateau.

## 5. Open leads

**Rebuild attempt 20's regime exactly and treat it as the base.** Its measured signature is `per_step_cost_ratio` ≈ 0.701, `compute_efficiency` ≈ 0.963, `wall_clock_sec` ≈ 73.7, `qualifying_budget` ≈ 73.7, all checks held, both perturbations reached, reward 0.8670. Attempt 14 (ratio 0.6997, efficiency 0.9705, 74.15 s, 0.8513) and attempt 18 (ratio 0.7671, efficiency 0.8827, 73.82 s, 0.8368) are near-neighbours in cost space that scored materially lower, which says the cost setting alone does not reproduce 0.8670 — something on the quality side differed. Reconstruct the cheap-step regime and then vary only the primary-quality knob, one change at a time.

**Buy margin on the held-out variant, not on the primary.** `C-BUDGET-RESPECTED` inside a `held_out_variant` unit is the single check that has stopped four attempts, and `C-PERTURBATION-REACHED` is its top-level consequence. The concrete lead: make the training loop's stopping condition budget-aware in wall-clock or step terms with headroom, so a variant that converges more slowly than the primary still terminates inside its own budget and still emits a qualifying evaluation row. Attempt 7 is the informative case — its variant failed only `C-BUDGET-RESPECTED`, not `C-TARGET-REACHED`, meaning it was converging and simply ran out of time. Cheap insurance here is worth far more than a fourth-decimal primary gain, given the ~0.44 penalty.

**Hold the budget in the 70–76 s band.** Every reward above 0.85 came from a run whose `qualifying_budget` was between 70.30 and 75.53 s. Nothing outside that band has ever scored above 0.8426. Treat drift toward 95 s as a bug.

**Attack the quality term with cost held fixed.** The top six clean results have `per_step_cost_ratio` ranging from 0.701 to 0.971 while their rewards agree to within 0.0015. That says cost is roughly saturated as a lever in this band and the remaining headroom is in whatever drives the primary-quality component — schedule, initialisation, regularisation or the evaluation-margin the target is crossed by. Aim for a larger margin over the threshold rather than a faster crossing, since a larger margin is also what would protect the held-out variant.

**Sanity guards worth adding regardless.** A hard wall-clock ceiling so no configuration can repeat attempt 21's 1691 s, and a lint pass confirming the module body contains only imports, constants and permitted definitions so `C-API-SURFACE` cannot recur.

## Call: exploit

Exploit. The best measured result, attempt 20 at 0.8670, is a fully conforming run with both perturbations held, and the clean regime around it is still producing 0.855–0.867 reliably, so the scoring approach has not exhausted itself. The action is to rebuild attempt 20's cheap-step, ~74 s configuration and change exactly one thing: give the held-out variant budget headroom so `C-BUDGET-RESPECTED` cannot be the check that stops it. That is the one failure that has recurred, across attempts whose other measured terms differed, and it has never been addressed directly — the changes made between attempts 7, 12 and 19 were not the cause of it. Explore is not warranted while a 0.8670 configuration exists and its known failure mode is untried.
