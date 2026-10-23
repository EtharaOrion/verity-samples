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

    It is also the most recent attempt, so this is where the work stands.

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
  17 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 20 -- reward 0.5107, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (9, 17, 20). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Twenty-one graded records. Nineteen produced a measurement; two did not. Ordered worst to best by `reward`:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 12 | 0.4962 | failed `C-PERTURBATION-REACHED`; `task_pass` 0.0 |
| 2 | 20 | 0.5107 | failed `C-API-SURFACE`; `task_pass` 0.0, `rule_conformance` 0.8571 |
| 3 | 9 | 0.5164 | failed `C-API-SURFACE`; `task_pass` 0.0, `rule_conformance` 0.8571 |
| 4 | 17 | 0.5274 | failed `C-API-SURFACE`; `task_pass` 0.0, `rule_conformance` 0.8571 |
| 5 | 8 | 0.5444 | clean; wall clock 26.10 s (longest), compute_efficiency 0.9679 |
| 6 | 13 | 0.5590 | clean; wall clock 20.60 s |
| 7 | 16 | 0.5701 | clean; wall clock 20.98 s |
| 8 | 18 | 0.5755 | clean; wall clock 20.63 s |
| 9 | 4 | 0.5792 | clean; wall clock 17.51 s, compute_efficiency 0.8832 |
| 10 | 15 | 0.5830 | clean; wall clock 23.70 s |
| 11 | 10 | 0.5983 | clean; wall clock 20.15 s |
| 12 | 3 | 0.6279 | clean; wall clock 20.30 s |
| 13 | 14 | 0.6426 | clean; wall clock 17.78 s |
| 14 | 5 | 0.6587 | clean; wall clock 20.53 s |
| 15 | 11 | 0.6639 | clean; wall clock 20.06 s, per_step_cost_ratio 1.0166 |
| 16 | 1 | 0.6694 | clean; wall clock 17.43 s; first measured attempt |
| 17 | 19 | 0.7134 | clean; wall clock 17.49 s |
| 18 | 2 | 0.7155 | clean; wall clock 17.45 s |
| 19 (best) | 21 | **0.7322** | clean; wall clock 14.39 s (shortest of all records) |

**Attempt 21 holds the highest reward at 0.7322 and is the score to beat.** Attempt 2 (0.7155) had held the lead from early on; every attempt between 3 and 20 was marked `worse_than_an_earlier_attempt`, i.e. eighteen consecutive attempts failed to improve on the standing best before attempt 21 finally did. That is a long regression stretch and should be read as such, not as gradual progress.

Attempts 6 and 7 carry `measurement_status: harbor_exception`. **They produced no measurement at all** — no reward, no efficiency, no perturbation units. They are not zeros and must not be treated as evidence that whatever they contained is bad; nothing is known about their quality.

No record crossed a red line (`red_line_crossed` 0.0 everywhere it was measured) and `validity` was 1.0 in every measured record. `primary_target_reached` was 1.0 in every measured record, including the three `C-API-SURFACE` failures and attempt 12 — the primary task always solved; what varied was cost and conformance.

The dominant measured relationship across the clean records is between `wall_clock_sec` (identical to `qualifying_budget` in every record) and reward. Sorted by wall clock, the clean runs read: 14.39 s → 0.7322; 17.43–17.51 s → 0.6694, 0.7155, 0.7134, 0.5792; 17.78 s → 0.6426; 20.06–20.98 s → 0.6639, 0.5983, 0.6279, 0.6587, 0.5590, 0.5755, 0.5701; 23.70 s → 0.5830; 26.10 s → 0.5444. Faster is better, strongly and consistently. Note also that attempts 1, 2 and 19 sit within 0.06 s of each other on wall clock yet span 0.6694 to 0.7155 — about 0.046 of reward spread at effectively matched cost. Treat differences smaller than ~0.05 between two single runs as unresolvable.

## 2. Approach classes tried

Only measured terms were supplied for this summary — no source, no diffs, no verifier logs beyond the named checks. The groupings below are therefore by the measured cost/conformance signature each attempt produced, which is what is actually knowable. Each group is one entry regardless of how many records fall into it.

**Class A — fast run, high per-step cost ratio.** `wall_clock_sec` 14.4–17.8 s with `per_step_cost_ratio` roughly 1.50–1.63 and `compute_efficiency` roughly 0.55–0.67. Records: 1, 2, 14, 19, 21, plus the conformance-failing 9, 20 and the perturbation-failing 12. This class contains every one of the top four rewards (21 at 0.7322, 2 at 0.7155, 19 at 0.7134, 1 at 0.6694). It spends more per step but finishes in far less total time, and total time is what the reward tracks.

**Class B — cost-per-step minimised / efficiency maximised.** `per_step_cost_ratio` driven down to 0.97–1.24 with `compute_efficiency` pushed up to 0.76–0.97. Records: 4 (1.1656 / 0.8832), 8 (0.9674 / 0.9679), 11 (1.0166 / 0.8424), 13 (1.2404 / 0.7642), 16 (1.1256 / 0.8684), and the conformance-failing 17 (1.2123 / 0.8228). Rewards: 0.5792, 0.5444, 0.6639, 0.5590, 0.5701, 0.5274. Best member 0.6639, well short of the leaders. The cheapest-per-step run in the whole record set (attempt 8, ratio 0.9674, efficiency 0.9679) also had the longest wall clock (26.10 s) and one of the lowest clean rewards (0.5444).

**Class C — mid-length run, high per-step cost ratio.** 20.1–23.7 s with `per_step_cost_ratio` 1.51–1.63. Records: 3 (0.6279), 5 (0.6587), 10 (0.5983), 15 (0.5830), 18 (0.5755). This is Class A's step profile stretched over a longer run; it costs roughly 0.06–0.15 of reward relative to Class A. Ceiling 0.6587.

**Class D — module-level executable code.** Records 9, 17 and 20, spanning wildly different cost profiles (per_step_cost_ratio 1.4988, 1.2123, 1.5804; compute_efficiency 0.6647, 0.8228, 0.6658), all tripped the same conformance check and all had `task_pass` forced to 0.0.

**Class E — a configuration the held-out variant could not complete.** Record 12 alone: the primary run passed (`primary_target_reached` 1.0) but one perturbation unit did not reach its threshold within its own budget, taking `conformance_fraction` to 0.5 and `task_pass` to 0.0. Lowest reward of all, 0.4962.

**Class F — attempts that never reached measurement.** Records 6 and 7, both `harbor_exception`. Nothing about their content is measurable from what was supplied.

## 3. Checks that failed

**`C-API-SURFACE`** — reason given verbatim by the verifier each time: *"module-level statements outside imports, constants, and permitted definitions"*. **This check has now failed three separate times: attempts 9, 17 and 20.** Those three attempts differed substantially from one another in every other measured dimension — compute_efficiency 0.6647 vs 0.8228 vs 0.6658, per_step_cost_ratio 1.4988 vs 1.2123 vs 1.5804, wall clock 17.12 s vs 23.58 s vs 17.39 s — and the check failed identically in all three. **Whatever was being changed between those attempts is not what causes this failure.** The cause is executable code at module scope. Each occurrence dropped `rule_conformance` from 1.0 to 0.8571 and `task_pass` from 1.0 to 0.0, and all three rank in the bottom four by reward (0.5107, 0.5164, 0.5274).

**`C-PERTURBATION-REACHED`** — one occurrence, attempt 12. Reason: *"1 of 2 declared perturbations reached their own threshold inside their own budget"*. `conformance_fraction` 0.5, `task_pass` 0.0, reward 0.4962 — the worst record in the set.

**`C-TARGET-REACHED`** and **`C-BUDGET-RESPECTED`** — one occurrence each, both on the same non-reaching perturbation unit inside attempt 12 (see section on perturbation outcomes below). These are the unit-level checks underlying the `C-PERTURBATION-REACHED` failure.

No other named check failed in any record. Sixteen of the nineteen measured records had an empty `failed_checks` list.

## 4. Ruled-out directions

**Minimising per-step cost / maximising compute efficiency as the optimisation target — ruled out.** Class B is six records that pushed `per_step_cost_ratio` down to 0.97–1.24 and `compute_efficiency` up to 0.76–0.97. Its best result is 0.6639 (attempt 11) and its mean is around 0.57. The extreme case, attempt 8, achieved the best efficiency numbers in the entire record set (0.9679 efficiency, 0.9674 ratio) and returned 0.5444 — lower than fourteen other measured attempts — because it took 26.10 s, the longest run recorded. The efficiency gain was purchased with wall clock, and wall clock is what the reward punishes. Do not spend effort here.

**Runs longer than about 20 s — ruled out.** Eight clean records exceeded 20 s: 0.6639, 0.6587, 0.6279, 0.5983, 0.5830, 0.5755, 0.5701, 0.5590. None reached 0.67, let alone 0.7322. No configuration has ever scored above the mid-0.66s while taking over 20 s.

**Any executable statement at module scope — ruled out.** Three `C-API-SURFACE` failures with the identical reason. It caps reward in the low 0.51–0.53 range by zeroing `task_pass`, regardless of how good the run is otherwise. Attempt 17 in particular had a strong 0.8228 compute_efficiency and still scored 0.5274.

**Whatever attempt 12 did to its held-out configuration — ruled out** until it can complete inside its own budget. `C-BUDGET-RESPECTED` failing on that unit says the configuration overran, not that the method was wrong in principle, but as submitted it is the worst-scoring record.

Nothing in this record set scored zero, so no attempt has been a literal repeat of a zero-scoring approach. The nearest analogue to that pathology is `C-API-SURFACE`: it was hit at attempt 9, again at 17, and again at 20, with the module-level-statement cause evidently never addressed in between. That pattern must not continue.

## 5. Open leads

**Reproduce attempt 21's profile and cut wall clock further.** Attempt 21 is the only record under 17 s (14.39 s) and it holds the best reward, 0.7322. Its signature: `per_step_cost_ratio` 1.5700, `compute_efficiency` 0.6162, `wall_clock_sec` 14.39, clean conformance. Total elapsed time is the single measured quantity that tracks reward across the whole set. Target something under 14 s while keeping every conformance check clean.

**Keep the high per-step cost ratio; do not optimise it.** The top four rewards all sit at ratio 1.50–1.63. Accept an expensive step if it buys fewer steps or a shorter total run. This is the inverse of what Class B tried.

**Structure the module so nothing executes at import.** Imports and constants only at module level; every statement inside a function or other permitted definition. This alone recovers roughly 0.05–0.20 of reward relative to the three `C-API-SURFACE` records and is a precondition for any other improvement counting.

**Verify the held-out variant path completes within its own budget.** The `held_out_variant` unit is the only kind that has ever failed, and it failed on `C-TARGET-REACHED` plus `C-BUDGET-RESPECTED`. Any speedup that works by trimming iterations or tightening a stopping rule risks exactly this failure; ensure the shortened path still reaches its threshold under the variant, not just under the primary run.

**Expect roughly 0.05 of run-to-run noise.** Attempts 1, 2 and 19 sit at 17.43, 17.45 and 17.49 s and score 0.6694, 0.7155 and 0.7134. A change producing less than about 0.05 of apparent movement is not distinguishable from noise on a single run; prefer changes that cut wall clock by a visible margin.

**Perturbation outcomes, by kind and in aggregate.** Every measured record declared exactly two perturbation units, one of kind `ruleset` and one of kind `held_out_variant`. Across the nineteen measured records that is nineteen `ruleset` units and nineteen `held_out_variant` units, thirty-eight in total. All nineteen `ruleset` units reached their threshold; that kind has never failed. Eighteen of the nineteen `held_out_variant` units reached their threshold; the single failure, in attempt 12, did not reach and was stopped by `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. Aggregate: 37 of 38 units reached, one did not. **The kind that fails is `held_out_variant`, and the checks it fails on are `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.** The runs are not identified beyond their kind, so nothing here should be read as tracking a particular run across records. Attempts 6 and 7 contributed no perturbation units, having produced no measurement.

**Call: exploit.** The best-scoring approach class is identified and is still improving — attempt 21 set a new high just now, and it did so by being faster than anything before it, along the one axis the measurements consistently reward. The move is to rebuild the Class A profile (short wall clock, per-step cost ratio around 1.5–1.6, no module-level statements, held-out variant completing inside its budget) and push total elapsed time below 14.39 s. Exploration into efficiency-maximising variants has been tried six times and its ceiling, 0.6639, is below three separate Class A results.
