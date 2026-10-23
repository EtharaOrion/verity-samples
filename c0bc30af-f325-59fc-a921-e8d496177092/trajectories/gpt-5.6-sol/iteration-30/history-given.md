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

    All nine attempts since have scored lower than it.
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
  23 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 27 -- reward 0.7394, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 124
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-BUDGET-RESPECTED failed on attempt 21.
    C-PERTURBATION-REACHED has failed on 4 attempts (7, 12, 19, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 21.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-nine graded records, all with `measurement_status: measured`; every one therefore carries a reward. Ordered worst to best:

| Rank | Attempt | Reward | Notes |
|---|---|---|---|
| 1 | 21 | 0.0000 | `zero_reason_code` 4; primary target not reached; wall clock 1691.67 s; both perturbation units failed |
| 2 | 12 | 0.4275 | held-out-variant perturbation not reached |
| 3 | 19 | 0.4278 | held-out-variant perturbation not reached; `compute_efficiency` 1.0 |
| 4 | 7 | 0.4911 | held-out-variant perturbation not reached |
| 5 | 16 | 0.7005 | all checks held |
| 6 | 28 | 0.7387 | all checks held |
| 7 | 27 | 0.7394 | qualifying budget 123.74 s, wall clock 148.19 s |
| 8 | 6 | 0.7580 | `C-API-SURFACE` failed; `rule_conformance` 0.8571 |
| 9 | 26 | 0.7607 | all checks held |
| 10 | 29 | 0.7667 | qualifying budget 95.38 s |
| 11 | 4 | 0.7740 | all checks held; `compute_efficiency` 0.9681 |
| 12 | 25 | 0.7757 | all checks held |
| 13 | 8 | 0.7805 | qualifying budget 98.60 s |
| 14 | 11 | 0.8067 | all checks held; `compute_efficiency` 1.0 |
| 15 | 2 | 0.8079 | all checks held |
| 16 | 23 | 0.8170 | qualifying budget 94.75 s |
| 17 | 9 | 0.8332 | all checks held |
| 18 | 18 | 0.8368 | all checks held |
| 19 | 24 | 0.8426 | qualifying budget 96.18 s |
| 20 | 10 | 0.8503 | all checks held |
| 21 | 14 | 0.8513 | all checks held |
| 22 | 15 | 0.8579 | all checks held |
| 23 | 22 | 0.8594 | all checks held |
| 24 | 1 | 0.8630 | first measured attempt |
| 25 | 17 | 0.8655 | all checks held |
| 26 | 13 | 0.8657 | (0.8656561) all checks held |
| 27 | 3 | 0.8657 | (0.8657110) all checks held |
| 28 | 5 | 0.8658 | all checks held |
| 29 | **20** | **0.8670** | **highest reward recorded; this is the one to beat** |

Attempt 20 holds the highest reward, 0.8670, and is the target to beat. Only four attempts ever set a new high-water mark: 1 (first measured), 3, 5, and 20. Every other record carries `standing_against_best_so_far: worse_than_an_earlier_attempt`, and those are genuine regressions against the then-best, not progress: attempts 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28 and 29 all scored below an earlier attempt. Attempt 21 scored 0.0000, the single lowest result, and it is the only record with `primary_target_reached: 0.0`.

The plateau is the dominant fact: seven separate attempts (1, 3, 5, 13, 17, 20, 22) land inside the band 0.8594–0.8670, a spread of 0.0076. Nothing since attempt 20 has re-entered that band's top; the four records after it (22–29 excluding 22's 0.8594) run 0.7387–0.8594.

# 2. Approach classes tried

The measured terms describe each submission only by its cost and conformance signature (`compute_efficiency`, `per_step_cost_ratio`, `qualifying_budget`, `wall_clock_sec`), not by its source. The classes below are therefore defined by those signatures, which is what is verifiable and what the next attempt can steer to directly.

**Class A — baseline-cost, mid-efficiency (`per_step_cost_ratio` ≈ 0.94–1.08, `qualifying_budget` ≈ 70–77 s).** Attempts 1 (1.0723 / 76.34 / 0.8630), 2 (0.9441 / 74.26 / 0.8079), 3 (0.9835 / 74.37 / 0.8657), 5 (0.9581 / 74.38 / 0.8658), 13 (0.9710 / 74.26 / 0.8657), 17 (0.9464 / 75.53 / 0.8655), 22 (0.9380 / 70.30 / 0.8594), 9 (0.9516 / 74.39 wall / 0.8332), 10 (0.9615 / 74.54 / 0.8503), 25 (0.9472 / 70.17 / 0.7757). This class produced most of the top band and also the widest internal spread (0.7757 to 0.8658) at nearly identical cost profiles — meaning per-step cost is not the only reward driver here; something about task quality moves the reward by ~0.09 while cost stays flat.

**Class B — aggressive cost reduction (`per_step_cost_ratio` ≤ 0.77, `compute_efficiency` ≥ 0.87).** Attempts 4 (0.6934 / eff 0.9681 / 0.7740), 11 (0.6947 / eff 1.0000 / 0.8067), 14 (0.6997 / eff 0.9705 / 0.8513), 16 (0.7055 / eff 0.9805 / 0.7005), 18 (0.7671 / eff 0.8827 / 0.8368), 20 (0.7013 / eff 0.9633 / **0.8670**), 23 (0.7375 / eff 0.8859 / 0.8170), 26 (0.7182 / eff 0.9881 / 0.7607), 28 (0.7322 / eff 0.9133 / 0.7387), plus the failing 12 (0.8114 / eff 0.8464) and 19 (0.6884 / eff 1.0000). This class contains both the single best result (20) and a long tail of mid-0.7 results, and it contains three of the four perturbation failures. Pushing `compute_efficiency` to its ceiling did not pay: attempt 11 reached `compute_efficiency` 1.0 and scored 0.8067; attempt 19 reached 1.0 and failed its held-out perturbation outright for 0.4278. Attempt 20 sits *below* the efficiency ceiling (0.9633) and above the cost floor (0.7013) and is the best result on record.

**Class C — long-budget / long-run variants (`qualifying_budget` > 90 s).** Attempts 8 (98.60 s / 0.7805), 23 (94.75 s / 0.8170), 24 (96.18 s / 0.8426), 27 (123.74 s budget, 148.19 s wall / 0.7394), 29 (95.38 s / 0.7667). Every member of this class scored below the top band. No long-budget run has ever exceeded 0.8426.

**Class D — the runaway.** Attempt 21 alone: wall clock 1691.67 s, `qualifying_budget: not-measured`, `primary_target_reached` 0.0, reward 0.0000, `zero_reason_code` 4. Its `compute_efficiency` reads 0.9829 and `per_step_cost_ratio` 0.6727, but with no qualifying row those cost numbers describe a run that never crossed the threshold at all.

**Class E — the surface violation.** Attempt 6 alone: the only record to fail `C-API-SURFACE`, with `rule_conformance` 0.8571 and `compute_efficiency` 0.4942 / `per_step_cost_ratio` 1.4094. It still scored 0.7580, so the surface violation degraded rather than zeroed the reward, but it also carried `task_pass` 0.0.

Across all classes `validity` is 1.0 and `red_line_crossed` is 0.0 in every record; nothing has tripped a red line.

# 3. Checks that failed

Four distinct check identifiers appear in the records.

**`C-PERTURBATION-REACHED` — failed 4 times** (attempts 7, 12, 19, 21). Reason given in 7, 12 and 19: "1 of 2 declared perturbations reached their own threshold inside their own budget." Reason in 21: "0 of 2 declared perturbations reached their own threshold inside their own budget." This is the single most repeated failure and the most consequential one: each of its occurrences dropped `conformance_fraction` to 0.5 (0.0 for 21), set `task_pass` to 0.0, and put the reward at 0.4275, 0.4278, 0.4911 and 0.0000 — roughly half the top band or less. These four attempts span very different cost profiles (`per_step_cost_ratio` 0.6727, 0.6884, 0.8114, 0.9657; `compute_efficiency` 0.8464 to 1.0000), so **whatever was varied in cost and efficiency between those attempts is not what is causing this check to fail.** The cause lies in something common to all four that the cost terms do not capture.

**`C-BUDGET-RESPECTED` — failed at the primary level once** (attempt 21, reason: "no qualifying row, so no budget position exists") **and at the perturbation-unit level in four attempts** (7, 12, 19, and both units of 21).

**`C-TARGET-REACHED` — failed at the primary level once** (attempt 21, reason: "no evaluation row crosses the threshold in the declared direction") **and at the perturbation-unit level in three attempts** (12, 19, and both units of 21).

**`C-API-SURFACE` — failed once** (attempt 6), reason: "module-level statements outside imports, constants, and permitted definitions." One occurrence only; it has not recurred in any attempt after 6, so whatever was changed after attempt 6 did fix that one. The next attempt must keep the module body limited to imports, constants and permitted definitions — no top-level executable statements.

Twenty-four of the twenty-nine records carry an empty `failed_checks` list with `conformance_fraction` 1.0 and `rule_conformance` 1.0. Conformance is not the general obstacle; the reward ceiling is.

# 4. Ruled-out directions

**Maximising `compute_efficiency` to its ceiling.** Attempt 11 reached `compute_efficiency` 1.0 with all checks holding and scored 0.8067 — below attempts 1, 3, 5, 13, 17, 20 and 22, all of which had lower efficiency. Attempt 19 also reached 1.0 and scored 0.4278 after failing `C-PERTURBATION-REACHED`. Efficiency at the ceiling does not buy reward and coincides with perturbation fragility.

**Driving `per_step_cost_ratio` below roughly 0.70.** The four records at or under 0.6947 are attempts 4 (0.6934 → 0.7740), 11 (0.6947 → 0.8067), 19 (0.6884 → failed `C-PERTURBATION-REACHED`, 0.4278) and 21 (0.6727 → 0.0000, target never reached). None of them beat the top band; two of them broke. The best result, attempt 20, sits at 0.7013.

**Long qualifying budgets (> 90 s).** Five attempts in Class C — 8, 23, 24, 27, 29 — all held every check and none exceeded 0.8426, against a top band of 0.8594–0.8670 obtained at 70–77 s. Attempt 27, the longest at 123.74 s budget / 148.19 s wall, scored 0.7394. Spending more wall clock has never converted into reward here.

**Whatever produced attempt 21's 1691.67 s run.** It is the only record with `primary_target_reached` 0.0, `qualifying_budget: not-measured` and reward 0.0000 (`zero_reason_code` 4). A configuration that never crosses the threshold in the declared direction scores nothing regardless of how good its cost terms look.

**Module-level executable code.** Ruled out by the one `C-API-SURFACE` failure in attempt 6, which cost `task_pass` and cut `rule_conformance` to 0.8571.

**Re-running the Class A baseline profile unchanged.** Attempts 3, 5, 13 and 17 all land within 0.0003 of each other (0.8657, 0.8658, 0.8657, 0.8655). Repeating that profile reproduces the same number; it has stopped improving on its own terms.

# 5. Open leads

**Reproduce attempt 20's operating point precisely, then vary one thing.** Attempt 20 is the unique best: `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013, `qualifying_budget` 73.66 s, `wall_clock_sec` 73.66 s, all checks held, both perturbation units reached. It is the only attempt that combined Class B's cost reduction with a top-band reward. That combination — moderate cost reduction (ratio ~0.70) held *short of* the efficiency ceiling, with budget in the low-70s — is the most valuable single data point on record and has been hit once. Re-derive it and hold it fixed as the base.

**Explain the ~0.09 reward spread at constant cost.** Within Class A, attempts 2 (0.8079) and 25 (0.7757) sit at essentially the same `per_step_cost_ratio` and `qualifying_budget` as attempts 5 (0.8658) and 13 (0.8657). Within Class B, attempts 4 (0.7740), 16 (0.7005) and 26 (0.7607) share attempt 20's cost signature but score 0.09–0.17 lower. Reward therefore carries a component the cost terms do not express — task quality at the threshold. Improving that component, at attempt 20's cost point, is the only route that has ever raised the ceiling.

**Harden the held-out-variant run specifically.** Of 58 perturbation units across 29 records (29 `held_out_variant`, 29 `seed`), 5 failed. Every one of the four `held_out_variant` failures (attempts 7, 12, 19, 21) failed `C-BUDGET-RESPECTED`, and three of them (12, 19, 21) additionally failed `C-TARGET-REACHED`. The `seed` kind failed exactly once, in attempt 21, and only there did it fail alongside the primary target — i.e. `seed` has never failed on its own. So the fragile kind is the held-out variant, and the check that stops it is `C-BUDGET-RESPECTED`, sometimes together with `C-TARGET-REACHED`. Any configuration must leave the held-out variant enough budget headroom to cross its own threshold inside its own budget; the primary run reaching its target (`primary_target_reached` 1.0 in 7, 12 and 19) is no protection, since those three still lost roughly half their reward.

**Leave margin rather than trimming it.** The pattern across attempts 4, 11, 16, 19 and 21 is that each further cut in per-step cost or budget either failed to raise the reward or pushed the held-out variant over its budget line. Attempt 20 kept margin and scored highest. Treat ~0.70 as a floor for `per_step_cost_ratio` and ~70–75 s as the budget band, and do not push past either.

**Confirmed-safe invariants to preserve.** `validity` 1.0 and `red_line_crossed` 0.0 in all 29 records; `rule_conformance` 1.0 in all but attempt 6. Two perturbations are declared each time. Keep module scope clean (imports, constants, permitted definitions only) so `C-API-SURFACE` stays held.

**Call: exploit.** The right move is to rebuild attempt 20's operating point — `per_step_cost_ratio` ≈ 0.70, `compute_efficiency` ≈ 0.96 (deliberately not 1.0), qualifying budget ≈ 73–74 s, both perturbation units reaching with budget headroom — and then improve only the task-quality component that the cost terms do not capture, which is what separates 0.8670 from the 0.70–0.78 results at the same cost signature. Exploration has been tried in both directions and closed off: pushing cost and efficiency to their limits (attempts 11, 19, 21) and extending budget (attempts 8, 23, 24, 27, 29) both produced strictly worse rewards. One caution about past behaviour: the loop has repeatedly re-run the same Class A profile (attempts 3, 5, 13, 17, all within 0.0003 of each other) and repeatedly re-entered the low-cost regime that fails `C-PERTURBATION-REACHED` (attempts 7, 12, 19) without changing what made it fail — that check has now failed four times and is not caused by anything varied in cost or efficiency across those attempts. Do not repeat either loop.
