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

    All eight attempts since have scored lower than it.
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

    attempt 28 -- reward 0.7387, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 70
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

All 28 records carry `measurement_status: "measured"`, so every attempt produced a measurement; none must be read as "no measurement". Exactly one of them scored a genuine zero (attempt 21), and that is a measured 0.0000, not an absent result.

Ranked worst to best by `reward`:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 | 21 | 0.0000 | `zero_reason_code` 4; `primary_target_reached` 0; wall clock 1691.6668 s; `qualifying_budget` "not-measured"; both perturbation runs failed |
| 2 | 12 | 0.4275 | held-out-variant perturbation not reached; `task_pass` 0 |
| 3 | 19 | 0.4278 | held-out-variant perturbation not reached; `task_pass` 0; `compute_efficiency` 1.0000 |
| 4 | 7 | 0.4911 | held-out-variant perturbation not reached; `task_pass` 0 |
| 5 | 16 | 0.7005 | all checks held; efficiency 0.9805, per-step cost 0.7055 |
| 6 | 28 | 0.7387 | all checks held; efficiency 0.9133 |
| 7 | 27 | 0.7394 | all checks held; qualifying budget 123.7429 s, wall clock 148.1882 s |
| 8 | 6 | 0.7580 | `C-API-SURFACE` failed; `rule_conformance` 0.8571; `task_pass` 0 |
| 9 | 26 | 0.7607 | all checks held; efficiency 0.9881 |
| 10 | 4 | 0.7740 | all checks held; efficiency 0.9681, per-step cost 0.6934 |
| 11 | 25 | 0.7757 | all checks held; budget 70.1666 s |
| 12 | 8 | 0.7805 | all checks held; budget 98.5950 s, per-step cost 1.0848 |
| 13 | 11 | 0.8067 | all checks held; efficiency 1.0000, per-step cost 0.6947 |
| 14 | 2 | 0.8079 | all checks held |
| 15 | 23 | 0.8170 | all checks held; budget 94.7474 s |
| 16 | 9 | 0.8332 | all checks held; qualifying budget 49.8865 s vs wall clock 74.3877 s |
| 17 | 18 | 0.8368 | all checks held; per-step cost 0.7671 |
| 18 | 24 | 0.8426 | all checks held; budget 96.1754 s, per-step cost 1.0041 |
| 19 | 10 | 0.8503 | all checks held |
| 20 | 14 | 0.8513 | all checks held; efficiency 0.9705, per-step cost 0.6997 |
| 21 | 15 | 0.8579 | all checks held; efficiency 0.9355 |
| 22 | 22 | 0.8594 | all checks held; budget 70.2965 s |
| 23 | 1 | 0.8630 | first measured attempt; per-step cost 1.0723 |
| 24 | 17 | 0.8655 | all checks held (raw 0.8655132) |
| 25 | 13 | 0.8657 | all checks held (raw 0.8656561) |
| 26 | 3 | 0.8657 | all checks held (raw 0.8657110) |
| 27 | 5 | 0.8658 | all checks held (raw 0.8658084) |
| 28 | **20** | **0.8670** | **best; all checks held; efficiency 0.9633, per-step cost 0.7013, budget 73.6617 s** |

**Attempt 20 holds the highest reward at 0.8670 and is the score to beat.** Only three records were ever marked `better_than_every_earlier_attempt`: attempt 3 (0.8657), attempt 5 (0.8658), attempt 20 (0.8670). Every other record after attempt 1 carries `standing_against_best_so_far: "worse_than_an_earlier_attempt"`, and that must be read as stated: attempts 2, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27 and 28 were all regressions against the best standing at the time, not progress. Note in particular that the two most recent records, attempts 27 (0.7394) and 28 (0.7387), are both well below the best and below the 0.8655–0.8670 cluster; the trajectory at the end of the run is downward, not upward.

The top of the distribution is a tight plateau: 0.8655, 0.8657, 0.8657, 0.8658, 0.8670. The best attempt beats the next best by only 0.0012.

# 2. Approach classes tried

The records contain no source code, so these classes are grouped by the measured cost and qualification signature each submission produced (`per_step_cost_ratio`, `compute_efficiency`, `qualifying_budget`, `wall_clock_sec`) together with which checks held. Two records with the same signature and the same outcome are one entry.

**Class A — baseline-cost training runs, ~74 s budget, all checks holding.** `per_step_cost_ratio` roughly 0.94–1.08, `compute_efficiency` 0.66–0.75, `qualifying_budget` 70–77 s. Attempts 1, 2, 3, 5, 9, 10, 13, 17, 22, 25. This class contains four of the five plateau scores (3 = 0.8657, 5 = 0.8658, 13 = 0.8657, 17 = 0.8655) but also 0.8079 (attempt 2), 0.7757 (attempt 25) and 0.8332 (attempt 9). Same nominal cost profile, reward spread of 0.09 — so whatever differs inside this class dominates the score and it is not the cost profile.

**Class B — aggressive per-step cost reduction, all checks holding.** `per_step_cost_ratio` 0.69–0.77, `compute_efficiency` 0.88–1.00, budget still ~73–76 s. Attempts 4 (0.7740), 11 (0.8067), 14 (0.8513), 16 (0.7005), 18 (0.8368), 20 (0.8670), 26 (0.7607), 28 (0.7387), and 15 (0.8579, per-step 0.9424 at efficiency 0.9355) sits on the boundary. This class produced the single best result (attempt 20) and also several of the worst passing results. Attempt 11 reached `compute_efficiency` 1.0000 — the maximum observed — and scored only 0.8067, and attempt 16 reached 0.9805 for 0.7005. Driving efficiency up on its own does not raise reward.

**Class C — extended budget.** `qualifying_budget` above 90 s: attempts 8 (98.5950 s, 0.7805), 23 (94.7474 s, 0.8170), 24 (96.1754 s, 0.8426), 27 (123.7429 s qualifying / 148.1882 s wall, 0.7394). Every member is below the plateau; the class ceiling is 0.8426.

**Class D — cost pushed past the point where the held-out variant survives.** Attempts 7 (0.4911), 12 (0.4275), 19 (0.4278). Primary target still reached in all three (`primary_target_reached` 1.0) and `rule_conformance` 1.0, but the held-out-variant perturbation run failed, `conformance_fraction` dropped to 0.5, `task_pass` went to 0 and reward roughly halved. Attempt 19 had `compute_efficiency` 1.0000 and per-step cost 0.6884; attempt 12 had per-step cost 0.8114 and attempt 7 had 0.9657 — so the collapse is not confined to the very cheapest configurations.

**Class E — submission with module-level executable code.** Attempt 6 only, 0.7580. All perturbations held and the primary target was reached, but `C-API-SURFACE` failed, `rule_conformance` fell to 0.8571 and `task_pass` went to 0. Also the fastest-qualifying passing-perturbation record (`qualifying_budget` 45.8165 s) and the highest per-step cost seen (1.4094) at efficiency 0.4942.

**Class F — very long run that never qualified.** Attempt 21 only, 0.0000. 1691.6668 s of wall clock, `primary_target_reached` 0, `qualifying_budget` "not-measured", `zero_reason_code` 4, and both declared perturbation runs failed. This is the only record where the seed perturbation failed and the only record where nothing crossed the threshold at all.

Across every class, `validity` is 1.0 and `red_line_crossed` is 0.0 in all 28 records. No submission ever tripped a validity or red-line condition.

# 3. Checks that failed

**`C-PERTURBATION-REACHED` — failed 4 times** (attempts 7, 12, 19, 21). This is the finding that matters most. In attempts 7, 12 and 19 the verifier's reason was "1 of 2 declared perturbations reached their own threshold inside their own budget"; in attempt 21 it was "0 of 2 declared perturbations reached their own threshold inside their own budget". These four attempts sat in different cost regimes from each other (per-step cost 0.9657, 0.8114, 0.6884 and 0.6727; efficiency 0.6954, 0.8464, 1.0000, 0.9829), so **whatever was changed between them is not what is causing this check to fail.** The cost and efficiency knobs were varied across those four and the check kept failing; the cause lies elsewhere, in whatever makes the held-out variant miss its own threshold or overrun its own budget.

**`C-TARGET-REACHED` — failed once at the primary level** (attempt 21), reason "no evaluation row crosses the threshold in the declared direction". It also appears as the per-run failure inside held-out-variant units in attempts 12, 19 and 21 and inside the seed unit in attempt 21.

**`C-BUDGET-RESPECTED` — failed once at the primary level** (attempt 21), reason "no qualifying row, so no budget position exists". As a per-run failure it appears in every failing perturbation unit: attempts 7, 12, 19 and 21 (held-out variant) and attempt 21 (seed).

**`C-API-SURFACE` — failed once** (attempt 6), reason "module-level statements outside imports, constants, and permitted definitions". This one did not recur; a single submission put executable statements at module scope, and the fix is to keep the module body to imports, constants and permitted definitions with all work inside the entry point.

Perturbation-unit outcomes, reported by kind and in aggregate. Each record declared 2 perturbation units, one of kind `held_out_variant` and one of kind `seed`; the runs are not otherwise identified, and nothing here identifies any particular run across records.

- Aggregate: 56 declared perturbation runs across 28 records; 51 reached their threshold inside their budget, 5 did not.
- Kind `seed`: reached in 27 of 28 records. The single failure was in attempt 21, the run that reached nothing at all, and it failed on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.
- Kind `held_out_variant`: reached in 24 of 28 records; failed in attempts 7, 12, 19 and 21. In attempt 7 the stopping check was `C-BUDGET-RESPECTED` alone; in attempts 12, 19 and 21 both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` were named.

The pattern is unambiguous: **the held-out-variant kind is the fragile one, and it fails on `C-BUDGET-RESPECTED` (every time) and usually also on `C-TARGET-REACHED`.** The seed kind is robust and only ever fell over when the whole submission collapsed. Any configuration that leaves the held-out variant with no budget headroom costs roughly half the reward.

# 4. Ruled-out directions

- **Extending the training budget beyond ~90 s (Class C).** Attempts 8, 23, 24 and 27 all qualified with budgets of 94.7–123.7 s and scored 0.7805, 0.8170, 0.8426 and 0.7394 — every one below the plateau, class ceiling 0.8426 against a best of 0.8670. Longer budgets did not buy accuracy that survived into reward.
- **Very long runs (attempt 21's regime).** 1691.6668 s of wall clock produced no qualifying row anywhere, `zero_reason_code` 4, reward 0.0000, and took both perturbation runs down with it. This is the worst outcome recorded.
- **Maximising `compute_efficiency` as an end in itself.** Attempt 11 hit efficiency 1.0000 with all checks holding and scored 0.8067; attempt 19 hit 1.0000 and lost the held-out variant for 0.4278; attempts 16 (0.9805 → 0.7005) and 26 (0.9881 → 0.7607) confirm it. Reward is clearly not monotone in efficiency at fixed conformance, so squeezing per-step cost further without regard to what it costs the model is ruled out.
- **Pushing per-step cost low enough that the held-out variant loses budget headroom (Class D).** Rewards 0.4911, 0.4275, 0.4278 against a plateau of ~0.866. Halving the reward to gain efficiency is never worth it.
- **Any module-level executable statement in the submission (Class E).** Attempt 6 lost `task_pass` and dropped `rule_conformance` to 0.8571 for a 0.7580, purely on `C-API-SURFACE`. Cheap and total to avoid; never reintroduce.
- **Very early qualification as a goal in itself.** Attempt 9 qualified at 49.8865 s (well inside its 74.3877 s wall clock) and scored 0.8332, below the plateau; attempt 6 qualified at 45.8165 s and scored 0.7580. Getting a qualifying row early does not by itself raise reward.

# 5. Open leads

- **Reproduce attempt 20's exact regime first and treat it as the floor.** Its signature: `compute_efficiency` 0.9633, `per_step_cost_ratio` 0.7013, `qualifying_budget` 73.6617 s equal to its wall clock, all checks held, both perturbation runs reached. That combination is the only one that has ever exceeded 0.8658. Land that before changing anything else.
- **The unexplained lever is model quality, not cost.** Within Class A the cost signature is essentially constant while reward ranges 0.7757–0.8658, and the plateau top (0.8658 at efficiency 0.6926) is matched by attempt 20 (0.8670 at efficiency 0.9633). So near-identical reward is reachable at very different costs, which means an accuracy-side term the metrics do not expose is what separates 0.78 from 0.866. The lead worth pursuing is: hold attempt 20's cheap per-step configuration and improve the final model quality — better schedule, better initialisation, better regularisation, more effective use of the same step budget — rather than touching cost at all.
- **Keep explicit budget headroom for the held-out variant.** `C-BUDGET-RESPECTED` inside the held-out-variant unit is the single most repeated per-run failure (4 occurrences). The passing records cluster at qualifying budgets of 70–77 s; every held-out-variant failure and every long-budget regression sits outside that band or was driven by an aggressive cost setting. Target a qualifying budget in the low 70s with a real margin, and make the stopping condition robust to a shifted data variant rather than tuned to the primary run.
- **Make the run adaptive to the variant rather than fixed-length.** Since `C-TARGET-REACHED` accompanies `C-BUDGET-RESPECTED` in three of the four held-out-variant failures, the variant is sometimes genuinely not converging, not merely running late. Early-stopping on a validated criterion, plus a conservative extra epoch or two when the criterion is not yet met but budget remains, addresses both named checks at once.
- **Mid-range per-step cost (~0.70–0.77) with efficiency ~0.88–0.96 is the productive band.** Attempts 20 (0.8670), 14 (0.8513) and 18 (0.8368) are the best of Class B; going below ~0.69 (attempts 11, 19) or above ~0.98 efficiency (16, 26) has consistently hurt. Stay in that band.
- **Do not re-run structural excursions unchanged.** The zero and the near-half rewards all came from directions whose failure mechanism is now named. Repeating a long run, or another module-level-statement submission, without changing the thing that caused the failure would be neither exploration nor exploitation.

**Call: exploit.** Take attempt 20's configuration — high compute efficiency near 0.96 at a per-step cost ratio near 0.70, qualifying budget in the low 70 s, all checks holding on both perturbation kinds — and improve the quality term inside it, while preserving budget headroom so the held-out variant keeps clearing `C-BUDGET-RESPECTED` and `C-TARGET-REACHED`. The top five results sit within 0.0015 of each other, so the plateau is real and the remaining gain from cost tuning is small; but no structurally different idea has yet scored above it either, and every excursion so far has cost between 0.09 and the entire reward. The highest-expected-value move is to re-land 0.8670 and push on the one dimension the metrics have never varied independently: what the model actually learns per unit of the budget already being spent.
