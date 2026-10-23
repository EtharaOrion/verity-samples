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

    All seven attempts since have scored lower than it.
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

    attempt 25 -- reward 0.7757, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 70
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 26 -- reward 0.7607, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 70
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 27 -- reward 0.7394, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 124
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

Twenty-seven graded records, all with `measurement_status: "measured"`; every one carries a reward, so none are absent-measurement cases. Ranked worst to best:

| Rank | Attempt | reward |
|---|---|---|
| 1 | 21 | 0.0000 |
| 2 | 12 | 0.4275 |
| 3 | 19 | 0.4278 |
| 4 | 7 | 0.4911 |
| 5 | 16 | 0.7005 |
| 6 | 27 | 0.7394 |
| 7 | 6 | 0.7580 |
| 8 | 26 | 0.7607 |
| 9 | 4 | 0.7740 |
| 10 | 25 | 0.7757 |
| 11 | 8 | 0.7805 |
| 12 | 11 | 0.8067 |
| 13 | 2 | 0.8079 |
| 14 | 23 | 0.8170 |
| 15 | 9 | 0.8332 |
| 16 | 18 | 0.8368 |
| 17 | 24 | 0.8426 |
| 18 | 10 | 0.8503 |
| 19 | 14 | 0.8513 |
| 20 | 15 | 0.8579 |
| 21 | 22 | 0.8594 |
| 22 | 1 | 0.8630 |
| 23 | 17 | 0.8655 |
| 24 | 13 | 0.8657 |
| 25 | 3 | 0.8657 |
| 26 | 5 | 0.8658 |
| 27 | 20 | 0.8670 |

**Attempt 20 holds the highest reward at 0.8670 and is the one to beat.** It is the only record whose `standing_against_best_so_far` is `better_than_every_earlier_attempt` in the later half of the run; the only other records with that standing are attempt 3 (0.8657) and attempt 5 (0.8658), plus attempt 1 as `first_measured_attempt` (0.8630).

Twenty-two of the twenty-seven records after attempt 1 carry `standing_against_best_so_far: worse_than_an_earlier_attempt`. That is the plain direction of the record: most changes made things worse, not better. In particular, every attempt after 20 (21 at 0.0000, 22 at 0.8594, 23 at 0.8170, 24 at 0.8426, 25 at 0.7757, 26 at 0.7607, 27 at 0.7394) scored **below** 20, and the trend across those last six measured attempts is downward, not upward. Attempt 21 scored 0.0000 outright with `zero_reason_code: 4`.

Auxiliary quantities worth carrying forward, because they are the only observable fingerprints of what each attempt did (the code itself is not in the record):

- `primary_target_reached` = 1.0 in 26 of 27 records; only attempt 21 failed it (0.0).
- `validity` = 1.0 and `red_line_crossed` = 0.0 in all 27 records. Nothing has ever tripped a red line or been ruled invalid.
- `rule_conformance` = 1.0 everywhere except attempt 6 (0.8571).
- `task_pass` = 0.0 in attempts 6, 7, 12, 19, 21; 1.0 in the other 22.
- Attempt 20's shape: `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013, `wall_clock_sec` 73.66, `qualifying_budget` 73.66.
- The dense cluster at 0.8655–0.8658 (attempts 17, 13, 3, 5) all share `per_step_cost_ratio` 0.9424–0.9835, `compute_efficiency` 0.6922–0.7320, and `wall_clock_sec` 74.25–75.53.

## 2. Approach classes tried

The records give no source text, so these classes are defined by their measured signature — per-step cost, compute efficiency, wall clock, and qualifying budget. Records with the same signature and the same outcome are one entry.

**Class A — baseline per-step cost, standard ~74 s budget.** `per_step_cost_ratio` ≈ 0.94–1.09, `compute_efficiency` ≈ 0.66–0.75, `wall_clock_sec` ≈ 70–76, `qualifying_budget` tracking wall clock. Attempts 1, 2, 3, 5, 9, 10, 13, 17, 22, 25. This is the workhorse regime and it produced the stable plateau: attempts 3, 5, 13, 17 all land within 0.0003 of 0.8657 despite differing in cost ratio, which says the quality term saturates here and small parameter jiggles inside this class do nothing. Outliers inside the class (2 at 0.8079, 25 at 0.7757) show the class can still be degraded by whatever was varied. All perturbations held for every member.

**Class B — reduced per-step cost / high compute efficiency at the same ~74 s wall clock.** `per_step_cost_ratio` ≈ 0.69–0.77, `compute_efficiency` ≈ 0.88–1.00. Attempts 4 (0.7740), 11 (0.8067), 14 (0.8513), 15 (0.8579, cost 0.9424 with efficiency 0.9355), 16 (0.7005), 18 (0.8368), 20 (0.8670), 26 (0.7607). This class contains both the best result and several of the worst non-failing results — spread 0.7005 to 0.8670. Cheapening the step is where the headroom is, but only some members of the class preserved whatever quality the reward also prices. Note `compute_efficiency` saturates at 1.0 (attempt 11) and attempt 11 still scored only 0.8067, below attempt 20's 0.9633/0.8670: driving cost below ≈0.69 buys nothing on the efficiency term and evidently costs something else.

**Class C — extended wall clock / larger budget.** `wall_clock_sec` ≥ 90. Attempts 8 (98.60 s, 0.7805), 23 (94.75 s, 0.8170), 24 (96.18 s, 0.8426), 27 (148.19 s with `qualifying_budget` 123.74, 0.7394). Uniformly worse than the ~74 s cluster. Buying more wall clock has never paid.

**Class D — very long run.** Attempt 21, `wall_clock_sec` 1691.67, roughly 23× the working regime. It failed the primary target outright, `qualifying_budget` came back `not-measured`, and the reward was 0.0000 with `zero_reason_code: 4`. This is the single structural blow-up.

**Class E — module-level structure change.** Attempt 6, the only record with `rule_conformance` 0.8571. It failed `C-API-SURFACE` and `task_pass` went to 0.0, yet the reward was still 0.7580 (both perturbations held). So a conformance breach here scaled the reward down rather than zeroing it.

**Class F — configurations that broke a held-out perturbation while the primary still passed.** Attempts 7 (0.4911), 12 (0.4275), 19 (0.4278). All three have `primary_target_reached` 1.0 and `task_pass` 0.0. Their signatures differ (7: cost 0.9657/efficiency 0.6954 — a Class A shape; 12: cost 0.8114/efficiency 0.8464; 19: cost 0.6884/efficiency 1.0000 — the most aggressive Class B shape), so this failure is not confined to one cost regime. The penalty is roughly a halving of reward.

## 3. Checks that failed

**`C-PERTURBATION-REACHED` — failed 4 times** (attempts 7, 12, 19, 21). Reason on 7, 12 and 19: "1 of 2 declared perturbations reached their own threshold inside their own budget". Reason on 21: "0 of 2 declared perturbations reached their own threshold inside their own budget". This is the most repeated check and the most costly one: it drove `conformance_fraction` to 0.5 (or 0.0 on 21), set `task_pass` to 0.0, and put those rewards at 0.4911, 0.4275, 0.4278 and 0.0000 — all far under the ~0.86 plateau. Because it recurs across three quite different cost/efficiency signatures (a baseline-cost attempt, a mid-cost attempt, and a maximum-efficiency attempt), **whatever was being changed between those attempts is not what is causing this failure.** The cause lies in something common to all of them — the margin with which a run converges under a shifted setting — not in the per-step cost knob that varied.

**`C-BUDGET-RESPECTED` — failed 6 times** across perturbation units and once at the top level. It is the sole unit-level failure on the held-out-variant run in attempt 7; it appears together with `C-TARGET-REACHED` on the held-out-variant runs in attempts 12, 19 and 21 and on the seed run in attempt 21; and it appears at the top level in attempt 21 with reason "no qualifying row, so no budget position exists". It is the check that most often stops a held-out run.

**`C-TARGET-REACHED` — failed 5 times.** At the top level once, on attempt 21: "no evaluation row crosses the threshold in the declared direction". At unit level on the held-out-variant runs of attempts 12, 19 and 21 and on the seed run of attempt 21.

**`C-API-SURFACE` — failed once**, attempt 6: "module-level statements outside imports, constants, and permitted definitions". Single occurrence; no later record repeats it, so whatever was written at module scope in that attempt has not recurred.

**Perturbation-unit outcomes.** Every record declares exactly 2 perturbations, one of kind `held_out_variant` and one of kind `seed`. Across 27 records that is 54 unit runs; 49 reached their threshold and 5 did not.

- By kind, `held_out_variant`: 4 failures out of 27 (in attempts 7, 12, 19, 21). Stopping checks: `C-BUDGET-RESPECTED` alone in one case; `C-TARGET-REACHED` together with `C-BUDGET-RESPECTED` in three cases.
- By kind, `seed`: 1 failure out of 27, in attempt 21 only, stopped by `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` — the same attempt in which the primary target also failed, i.e. a total blow-up rather than a seed-specific fragility.

In aggregate the held-out-variant kind is four times more fragile than the seed kind, and outside the one total blow-up it is the *only* kind that has ever failed. The runs are not identified beyond their kind, so nothing here should be read as tracking one particular run across records. The finding to carry forward is: **the held-out-variant kind of run is what fails, and it fails on `C-BUDGET-RESPECTED`, sometimes together with `C-TARGET-REACHED`.**

## 4. Ruled-out directions

**Extending wall clock or budget beyond about 80 seconds.** Every record with `wall_clock_sec` ≥ 90 scored below the plateau: 8 at 0.7805 (98.60 s), 23 at 0.8170 (94.75 s), 24 at 0.8426 (96.18 s), 27 at 0.7394 (148.19 s, budget 123.74 s). Four independent tries, none reached 0.8630, let alone 0.8670. The reward penalises the extra time more than the extra time buys.

**Very long runs.** Attempt 21 at 1691.67 s did not merely score low, it scored 0.0000 with `zero_reason_code: 4`, failed `C-TARGET-REACHED` at the top level, and returned `qualifying_budget: "not-measured"`. Do not go near this regime.

**Pushing `per_step_cost_ratio` below ≈0.69 to chase compute efficiency.** `compute_efficiency` saturates at 1.0 and there is nothing left to win. Attempt 11 hit efficiency 1.0000 at cost 0.6947 and scored 0.8067 — clearly worse than attempt 20's 0.9633/0.7013 at 0.8670. Attempt 19 hit efficiency 1.0000 at cost 0.6884 and lost the held-out variant entirely (0.4278). Attempt 4 at cost 0.6934 scored 0.7740 and attempt 16 at cost 0.7055 scored 0.7005. The cheapest steps are not the best rewards.

**Further jiggling inside the Class A baseline regime.** Attempts 17, 13, 3 and 5 span cost ratios 0.9424–0.9835 and efficiencies 0.6922–0.7320 and all return 0.8655–0.8658. Four distinct configurations landing within 0.0003 of each other means this regime is at its own ceiling; more variation of the same kind will reproduce ~0.8657 and will not beat 0.8670.

**Writing executable statements at module scope.** `C-API-SURFACE` on attempt 6 cost `task_pass` and dropped `rule_conformance` to 0.8571 for a reward of 0.7580. Keep the module body to imports, constants and permitted definitions.

**Not ruled out but note the pattern:** the loop has repeatedly re-entered Class A and Class B without changing what causes `C-PERTURBATION-REACHED` to fail, and has re-produced the ~0.8657 plateau many times over. Rebuilding a plateau configuration and hoping for a different number is neither exploiting nor exploring.

## 5. Open leads

**Lead 1 — reconstruct attempt 20's operating point exactly.** The target signature is `per_step_cost_ratio` ≈ 0.70, `compute_efficiency` ≈ 0.96, `wall_clock_sec` ≈ 73.7 with `qualifying_budget` equal to it, both perturbation units reaching, `rule_conformance` 1.0. That combination — cheap steps *without* saturating efficiency, at the standard budget — is the only thing that has ever cleared 0.8658. Aim for that shape first and verify by the reported terms, then improve on it.

**Lead 2 — the reward has two visibly separable ingredients; move the efficiency one while holding the other.** The 0.8655–0.8658 plateau is reached at efficiency ≈0.69–0.73, and attempt 20 exceeded it at efficiency 0.9633 with an essentially identical wall clock. But high efficiency alone does not confer reward (16: 0.9805 → 0.7005; 26: 0.9881 → 0.7607; 4: 0.9681 → 0.7740). So the winning move is to take a configuration that lands on the plateau's quality and cut its per-step cost from ~0.95 toward ~0.70 without disturbing anything else. Change one thing; if the reward falls below 0.8655, the cut damaged quality, not efficiency.

**Lead 3 — protect the held-out-variant run.** The held-out-variant kind has failed four times, stopped by `C-BUDGET-RESPECTED` (once alone, three times with `C-TARGET-REACHED`). It fails from baseline-cost and from aggressive-cost configurations alike, so cost is not the lever. The lever is convergence margin: the held-out variant must cross its own threshold comfortably inside its own budget, not just barely. Practically, prefer a schedule that converges early and holds, add headroom rather than trimming steps to the minimum that works on the primary, and make any adaptivity respond to the run it is actually in rather than being tuned to the primary's trajectory. Any candidate that beats 0.8670 on the primary but loses this unit lands near 0.43, which is far worse than the plateau — the downside is asymmetric.

**Lead 4 — 0.8670 vs 0.8658 is a narrow margin; do not mistake noise for progress.** Attempts 3, 5, 13 and 17 differ by under 0.0003. Treat a candidate as an improvement only if it clears attempt 20's 0.8670 by more than that, and only with `all_perturbations_held: true` and `conformance_fraction: 1.0`.

**Lead 5 — mid-range cost, unexplored band.** Attempt 18 (cost 0.7671, efficiency 0.8827, 0.8368) and attempt 15 (cost 0.9424, efficiency 0.9355, 0.8579) sit between the plateau and attempt 20 and are the only samples in that band. The region around cost 0.70–0.75 with efficiency 0.93–0.97 at ~74 s contains attempt 20 and is thinly sampled; a careful sweep there is the most defensible place to look for a gain.

**Lead 6 — invariants to keep, since they have never failed.** `validity` 1.0, `red_line_crossed` 0.0, `primary_target_reached` 1.0 (26 of 27), `perturbations_declared` 2.0, module scope clean. Nothing suggests any of these needs changing, and changing them has only ever cost reward.

**Call: exploit.** Attempt 20 at 0.8670 is the standing best and only barely above a four-way plateau at ~0.8657, so the ceiling of the approaches that scored has not been convincingly probed at attempt 20's operating point — that point was reached once and has not been revisited. Rebuild attempt 20's signature (Lead 1), then apply Lead 2's single-knob cost reduction with Lead 3's held-out-variant margin in place. Do not explore into long-wall-clock or maximum-efficiency territory: both are measured dead ends, and the last six measured attempts all fell below 20 while wandering there.
