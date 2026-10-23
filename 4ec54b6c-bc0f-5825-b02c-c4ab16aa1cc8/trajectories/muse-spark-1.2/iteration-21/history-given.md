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

    All one attempts since have scored lower than it.
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

    attempt 22 -- reward 0.6376, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (9, 17, 20). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-two graded records exist. Twenty carry a reward; two (attempts 6 and 7) have `measurement_status: harbor_exception` and therefore **produced no measurement at all** — they are not zeros, and nothing about the code they carried can be inferred from them either way.

Ranked worst to best by reward:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 | 12 | 0.4962 | failed C-PERTURBATION-REACHED; task_pass 0 |
| 2 | 20 | 0.5107 | failed C-API-SURFACE; task_pass 0 |
| 3 | 9 | 0.5164 | failed C-API-SURFACE; task_pass 0 |
| 4 | 17 | 0.5274 | failed C-API-SURFACE; task_pass 0 |
| 5 | 8 | 0.5444 | clean; wall_clock 26.098 s, per_step_cost_ratio 0.9674 |
| 6 | 13 | 0.5590 | clean; 20.600 s, ratio 1.2404 |
| 7 | 16 | 0.5701 | clean; 20.984 s, ratio 1.1256 |
| 8 | 18 | 0.5755 | clean; 20.626 s, ratio 1.5846 |
| 9 | 4 | 0.5792 | clean; 17.512 s, ratio 1.1656, compute_efficiency 0.8832 |
| 10 | 15 | 0.5830 | clean; 23.702 s, ratio 1.6313 |
| 11 | 10 | 0.5983 | clean; 20.150 s, ratio 1.5152 |
| 12 | 3 | 0.6279 | clean; 20.300 s, ratio 1.5225 |
| 13 | 22 | 0.6376 | clean; 17.372 s, ratio 1.5983 |
| 14 | 14 | 0.6426 | clean; 17.780 s, ratio 1.6303 |
| 15 | 5 | 0.6587 | clean; 20.529 s, ratio 1.6262 |
| 16 | 11 | 0.6639 | clean; 20.057 s, ratio 1.0166, compute_efficiency 0.8424 |
| 17 | 1 | 0.6694 | clean; 17.426 s, ratio 1.5134 (first measured attempt) |
| 18 | 19 | 0.7134 | clean; 17.487 s, ratio 1.5834 |
| 19 | 2 | 0.7155 | clean; 17.453 s, ratio 1.5175 |
| 20 | **21** | **0.7322** | clean; **14.390 s**, ratio 1.5700, compute_efficiency 0.6162 |

**Attempt 21 holds the highest reward, 0.7322. That is the score to beat.**

Only two records were ever marked `better_than_every_earlier_attempt`: attempt 2 (0.7155) and attempt 21 (0.7322). Every other measured record after attempt 2 is marked `worse_than_an_earlier_attempt`, and that is what it is — attempts 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 and 22 each scored below the standing best at the time. Attempt 22 (0.6376) came immediately after the best-ever attempt 21 and is a regression of 0.0946 against it, not progress. Attempt 19 (0.7134) is likewise below attempt 2 (0.7155) despite being close.

`primary_target_reached` is 1.0, `validity` is 1.0, `red_line_crossed` is 0.0 and `zero_reason_code` is 0 in all twenty measured records. Nothing has ever been invalidated or hit a red line; the whole reward spread lives in efficiency and in the four conformance failures.

# 2. Approach classes tried

The records supply no source, so approaches are grouped by their measured operating signature (`per_step_cost_ratio`, `compute_efficiency`, `wall_clock_sec`), which separates cleanly into distinct families.

**A. Baseline-cost, moderate-length run (ratio ≈ 1.51–1.63, wall clock ≈ 17.4–17.8 s).** Attempts 1, 2, 14, 19, 22. Rewards 0.6376, 0.6426, 0.6694, 0.7134, 0.7155. This is the most productive family found and contains the second- and third-best results. Compute_efficiency in this family sits ≈ 0.60–0.67 — not high — yet it outscores every high-efficiency family.

**B. Same per-step cost, shortened run (ratio 1.5700, wall clock 14.390 s).** Attempt 21 alone, reward 0.7322, the best result on record. It is family A with roughly 3 seconds of wall clock removed and identical conformance, and it produced the only improvement over attempt 2.

**C. Same per-step cost, lengthened run (ratio ≈ 1.51–1.63, wall clock ≈ 20.1–23.7 s).** Attempts 3, 5, 10, 15, 18. Rewards 0.5755, 0.5830, 0.5983, 0.6279, 0.6587. Uniformly below family A. Extending the run at unchanged per-step cost strictly costs reward.

**D. Cheap-per-step / high-compute-efficiency runs (ratio ≈ 0.97–1.24, compute_efficiency 0.76–0.97).** Attempts 4, 8, 11, 13, 16 (and 17, which additionally failed conformance). Rewards 0.5444, 0.5590, 0.5701, 0.5792, 0.6639. Attempt 8 is the extreme case: compute_efficiency 0.9679 and per_step_cost_ratio 0.9674, the best efficiency numbers ever recorded, and a reward of 0.5444 — near the bottom of the clean field — because it spent 26.098 s of wall clock. Attempt 4 reached compute_efficiency 0.8832 at 17.512 s, an A-family wall clock, and still only scored 0.5792, well under the 0.6694–0.7155 that family A got at the same duration.

**E. Aggressively trimmed run that broke the held-out perturbation (attempt 12).** Wall clock 16.781 s, ratio 1.4886, and the held-out_variant perturbation unit did not reach: it failed C-TARGET-REACHED and C-BUDGET-RESPECTED. task_pass 0, reward 0.4962, the lowest on record.

**F. Submissions carrying module-level executable code (attempts 9, 17, 20).** Spread across otherwise different operating points (17.122 s / ratio 1.4988; 23.581 s / ratio 1.2123; 17.393 s / ratio 1.5804). All three failed C-API-SURFACE, all three had rule_conformance 0.8571 and task_pass 0, and all three scored 0.5107–0.5274 — below every clean attempt at comparable wall clock.

**G. Two attempts (6, 7) whose runs ended in a harbor exception.** No measurement of any kind was produced, so no approach conclusion can be drawn from them.

# 3. Checks that failed

**C-API-SURFACE — failed three times**, in attempts 9, 17 and 20, with the identical verifier reason each time: *"module-level statements outside imports, constants, and permitted definitions."* This is the single most repeated finding in the whole record. The three attempts differ substantially in operating point (compute_efficiency 0.6647, 0.8228, 0.6658; wall clock 17.122 s, 23.581 s, 17.393 s), so **whatever was changed between those attempts is not what is causing this failure**. The cause is structural: the submission module executes statements at import time that are neither imports, nor constants, nor permitted definitions. Each occurrence drove rule_conformance from 1.0 to 0.8571 (six of seven rules) and task_pass from 1.0 to 0.0.

**C-PERTURBATION-REACHED — failed once**, in attempt 12, reason: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This is a consequence of the two unit-level failures below.

**C-TARGET-REACHED and C-BUDGET-RESPECTED — failed once each**, both inside the same non-reaching perturbation unit of attempt 12. That unit is of kind `held_out_variant`: it did not reach its threshold and it did not respect its budget.

No other check has ever failed. rule_conformance is 1.0 in all sixteen clean measured records; conformance_fraction is 1.0 everywhere except attempt 12 (0.5).

# 4. Ruled-out directions

**Maximising compute_efficiency / pushing per_step_cost_ratio toward or below 1.0.** Ruled out by family D. The clean attempts with the lowest per-step cost and highest efficiency are the clean attempts with the lowest rewards: attempt 8 (ratio 0.9674, efficiency 0.9679) → 0.5444; attempt 13 (1.2404) → 0.5590; attempt 16 (1.1256) → 0.5701; attempt 4 (1.1656, efficiency 0.8832) → 0.5792. Meanwhile family A runs at ratio ≈ 1.51–1.63 and efficiency ≈ 0.60–0.67 and scores 0.6376–0.7155. Cheapening the per-step cost has never bought reward, and when it was paid for with extra wall clock (attempt 8, 26.098 s) it produced the worst clean score on record. The one partial exception, attempt 11 (ratio 1.0166 → 0.6639), still landed below every family A result and below attempt 21.

**Lengthening the run.** Ruled out by family C. Every clean attempt above 20 s scored 0.5444–0.6639; every clean attempt at or below 17.8 s scored 0.5792–0.7322, and the four best clean results all sit at ≤ 17.49 s. There is no measured case of extra wall clock paying for itself.

**Leaving any executable statement at module level.** Ruled out by three separate C-API-SURFACE failures with an identical reason. It caps task_pass at 0 and rule_conformance at 0.8571 regardless of how good the training configuration is — attempt 17 ran at compute_efficiency 0.8228 and still scored 0.5274. All work must live inside permitted definitions; only imports, constants and definitions may appear at module scope.

**Trimming the schedule without protecting the held-out variant.** Ruled out by attempt 12, the lowest reward on record (0.4962). Cutting to 16.781 s left the `held_out_variant` unit failing both C-TARGET-REACHED and C-BUDGET-RESPECTED, which took conformance_fraction to 0.5 and task_pass to 0. Shortening is the winning axis, but it must not be done blindly: attempt 21 shortened to 14.390 s with both units still reaching, and attempt 12 shortened to 16.781 s and broke one — so the failure was in *how* the budget was allocated per variant, not merely in the total being small.

**Re-running attempts 6 and 7's configuration on the assumption they were bad.** Not ruled out and not ruled in: those runs produced no measurement, so there is no evidence about them in either direction. Treating them as failures would be an error.

# 5. Open leads

**Rebuild attempt 21's configuration and shave wall clock further.** Attempt 21 is the only thing that ever beat attempt 2, and it did so by holding the family A per-step profile (ratio 1.5700, compute_efficiency 0.6162 — deliberately *not* efficiency-optimised) while cutting wall clock to 14.390 s. Nothing has been tried below 14.4 s that still held both perturbations. That is the clearest unexplored region: same per-step cost, fewer total steps, with the held-out variant's own budget protected.

**Give each perturbation unit its own reaching guarantee rather than a shared fixed schedule.** Attempt 12 is the warning: a global trim starved the `held_out_variant` unit of both target and budget. A schedule that stops on a per-unit convergence criterion — rather than a fixed step count that happens to be enough for the primary task and the ruleset variant but not the held-out one — would let the total shrink without repeating C-TARGET-REACHED / C-BUDGET-RESPECTED.

**Treat single measurements as noisy.** Five clean attempts (1, 2, 14, 19, 22) sat in a narrow 17.37–17.78 s band at ratio 1.51–1.63 and returned 0.6376, 0.6426, 0.6694, 0.7134 and 0.7155 — a spread of about 0.078 across near-identical operating points. A configuration should not be abandoned on one low draw, and attempt 21's 0.7322 should be expected to vary on repetition. If a fast configuration lands near 0.70, that is not evidence against it.

**Audit the module scope mechanically before submitting.** Since C-API-SURFACE has now bitten three times with the same reason, the next attempt should explicitly confirm that the top level of the submission file contains nothing but imports, constant assignments and function/class definitions — no calls, no prints, no guarded setup blocks, no `if`/loop statements at module level. This alone recovers roughly 0.15 of reward relative to the comparable clean attempts at the same wall clock.

**Look at the primary/perturbation budget split.** `qualifying_budget` equals `wall_clock_sec` in every measured record, so the reward is being paid out of total elapsed time; attempt 21's 14.390 s is the cheapest qualifying budget ever recorded and is also the best reward. Reducing total elapsed time while all three of task_pass, rule_conformance and all_perturbations_held stay at their maxima is the single lever with measured support.

**Call: exploit.** Take attempt 21 — the family A per-step profile at a shortened schedule — reproduce it faithfully, keep every statement out of module scope, keep the held-out variant's budget explicitly satisfied, and push the wall clock below 14.39 s. The efficiency-maximising family (D) and the long-run family (C) have both been sampled repeatedly and have never approached 0.7322, so there is nothing left to explore there. Note also that C-API-SURFACE has now been re-incurred three separate times across three different configurations; repeating a submission with module-level statements is neither exploration nor exploitation, and that pattern should stop.
