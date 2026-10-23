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

    All five attempts since have scored lower than it.
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
  26       0.6518   1.000             2 of 2         yes             17                

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
  20 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 26 -- reward 0.6518, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (9, 17, 20). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING failed on attempt 25.
    C-PERTURBATION-REACHED has failed on 2 attempts (12, 25). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Twenty-six graded records exist. Twenty-four carry a reward; two (attempts 6 and 7) have `measurement_status: harbor_exception` and produced **no measurement at all** — they are not zeros and must not be counted as such, since every one of their terms is `not-measured`.

Ranked worst to best by reward:

| Attempt | reward | Notes |
|---|---|---|
| 25 | 0.0000 | red line crossed, `validity` 0, `zero_reason_code` 1 |
| 12 | 0.4962 | `task_pass` 0, perturbation failure |
| 20 | 0.5107 | `task_pass` 0, C-API-SURFACE |
| 9 | 0.5164 | `task_pass` 0, C-API-SURFACE |
| 17 | 0.5274 | `task_pass` 0, C-API-SURFACE |
| 8 | 0.5444 | clean; cost ratio 0.967, wall 26.10 s |
| 13 | 0.5590 | clean |
| 16 | 0.5701 | clean |
| 18 | 0.5755 | clean |
| 4 | 0.5792 | clean; cost ratio 1.166 |
| 15 | 0.5830 | clean |
| 10 | 0.5983 | clean |
| 3 | 0.6279 | clean |
| 22 | 0.6376 | clean |
| 14 | 0.6426 | clean |
| 26 | 0.6518 | clean |
| 5 | 0.6587 | clean |
| 11 | 0.6639 | clean; cost ratio 1.017 |
| 1 | 0.6694 | first measured attempt |
| 24 | 0.6833 | clean |
| 23 | 0.6877 | clean |
| 19 | 0.7134 | clean |
| 2 | 0.7155 | was `better_than_every_earlier_attempt` at the time |
| **21** | **0.7322** | **highest reward; the one to beat** |

**Attempt 21 holds the highest reward, 0.7322, and is the attempt to beat.** It is one of only two records marked `better_than_every_earlier_attempt` (the other is attempt 2 at 0.7155). Every other measured record after attempt 2 carries `standing_against_best_so_far: worse_than_an_earlier_attempt` — that is a regression relative to the standing best in each case and should be read as such, not as incremental progress. In particular attempts 22, 23, 24 and 26, which all came after the 0.7322 peak, scored 0.6376, 0.6877, 0.6833 and 0.6518 respectively: all four are **lower** than attempt 21.

Attempt 21's full metric signature, which is the target to reproduce: `wall_clock_sec` 14.3905 (the shortest of any measured record), `qualifying_budget` 14.3905, `per_step_cost_ratio` 1.5700, `compute_efficiency` 0.6162, `task_pass` 1.0, `validity` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, both perturbations reached, `red_line_crossed` 0.

## 2. Approach classes tried

No source was carried forward, so the classes below are reconstructed from the measured terms. Records with the same metric signature and the same outcome are collapsed into one entry.

**Class A — mid-cost baseline band (attempts 1, 2, 3, 10).** `per_step_cost_ratio` clustered tightly at 1.513–1.523, `compute_efficiency` 0.549–0.620, wall clock 17.4–20.3 s. Rewards 0.5983, 0.6279, 0.6694, 0.7155. Fully conformant every time. This band produced the early best (attempt 2, 0.7155). Within the band, the two runs at ~17.4 s wall clock scored higher (0.6694, 0.7155) than the two at ~20.2–20.3 s (0.5983, 0.6279), at essentially identical cost ratio.

**Class B — drive per-step cost down toward the seed anchor (attempts 4, 8, 11, 13, 16, 17).** `per_step_cost_ratio` pushed from ~1.5 down to 0.967–1.240, with `compute_efficiency` correspondingly high at 0.764–0.968. Rewards 0.5444, 0.5274 (that one also failing C-API-SURFACE), 0.5590, 0.5701, 0.5792, 0.6639. **This class never once beat the standing best.** Its extreme point, attempt 8, achieved the highest `compute_efficiency` of any record (0.9679) and the lowest `per_step_cost_ratio` (0.9674) and scored 0.5444 — near the bottom of the clean runs — while also incurring the longest wall clock of any record (26.0978 s). The measured relationship is the opposite of the intuitive one: cheaper per step correlated with *lower* reward and *longer* total wall clock, not shorter. Attempt 11 (ratio 1.0166, reward 0.6639) is the sole respectable result in this class and still fell short of 0.7155.

**Class C — higher per-step cost, ~1.58–1.63 band (attempts 5, 14, 15, 18, 19, 21, 22, 23, 24, 26).** `per_step_cost_ratio` 1.554–1.631, `compute_efficiency` 0.585–0.666. Rewards span 0.5755 to 0.7322 and this class contains both the best (21, 0.7322) and second-best-by-a-hair (19, 0.7134) results, plus 23 (0.6877) and 24 (0.6833). Within this class reward again tracks wall clock inversely: 14.39 s → 0.7322, 17.49 s → 0.7134, 17.37 s → 0.6376, 20.11 s → 0.6877, 20.63 s → 0.5755, 23.70 s → 0.5830. The correlation is real but noisy — attempt 22 at 17.37 s scored only 0.6376 while attempt 23 at 20.11 s scored 0.6877 — so wall clock alone does not determine the score.

**Class D — aggressive scaling past the cost ceiling (attempt 25).** `per_step_cost_ratio` 3.2459, `compute_efficiency` 0.3005. Crossed the red line, `validity` 0, reward 0.0000.

**Class E — submissions carrying module-level executable code (attempts 9, 17, 20).** Spread across cost bands (ratios 1.499, 1.212, 1.580), so this is a code-shape class, not a hyperparameter class. All three failed C-API-SURFACE, all three had `task_pass` driven to 0 and `rule_conformance` clipped to 0.857, rewards 0.5164, 0.5274, 0.5107.

**Class F — non-completing submissions (attempts 6, 7).** Both returned `harbor_exception` with every term `not-measured` and an empty `perturbation_units` list. These produced no measurement whatsoever; nothing about their algorithmic content can be inferred from the terms, and they cannot be ranked.

## 3. Checks that failed

**C-API-SURFACE — failed 3 times** (attempts 9, 17, 20). Verifier reason, identical in all three: *"module-level statements outside imports, constants, and permitted definitions."* This is the single most repeated finding in the record. It appeared in attempts spanning three different per-step cost regimes (1.499, 1.212, 1.580) and three different wall clocks (17.12, 23.58, 17.39 s), which means **whatever was changed between those attempts in the training algorithm, the schedule, or the cost profile is not what is causing this check to fail.** It is caused by the module having executable statements at import scope. Each occurrence forced `task_pass` to 0.0 and `rule_conformance` to 0.857 (6 of 7 rules), and each landed in the bottom five rewards. The fix is mechanical and independent of the learning algorithm: every statement at module level must be an import, a constant assignment, or a permitted definition (function/class); all setup, seeding, device selection, logging configuration, `print`, and any `if __name__ == "__main__"` style work must live inside a function body.

**C-PERTURBATION-REACHED — failed 2 times** (attempts 12 and 25). Verifier reason, identical in both: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* Both times `conformance_fraction` fell to 0.5 and `task_pass` to 0.0. Again this recurred across quite different cost regimes (ratio 1.489 vs 3.246), so the differences between those two submissions are not the cause; the cause is that the algorithm's convergence does not generalise to one of the held-out settings within its own budget.

**C-PER-STEP-COST-CEILING — failed once** (attempt 25). Reason: *"per-step cost is 3.246 times the seed anchor, above the ceiling of 3.0."* This is a hard red line: `red_line_crossed` 1, `validity` 0, `zero_reason_code` 1, reward 0.0000. The ceiling is explicitly 3.0× the seed anchor and is the only numeric bound the verifier has ever quoted back.

**C-TARGET-REACHED and C-BUDGET-RESPECTED** — these appear only inside perturbation units (attempts 12 and 25), never at top level. See section on perturbation units below.

Twenty of the twenty-four measured records had an empty `failed_checks` list, `rule_conformance` 1.0 and `task_pass` 1.0. Conformance is therefore the normal state; the failures above are the exceptions, and all seven bottom-ranked measured results are explained by them.

## 4. Ruled-out directions

**Minimising per-step cost / maximising compute efficiency.** Ruled out as a route to a higher reward. Six attempts (Class B) pushed `per_step_cost_ratio` from ~1.51 down as far as 0.9674 and `compute_efficiency` up as far as 0.9679; the resulting rewards were 0.5274–0.6639, every one of them below the then-standing best, and the most extreme point scored 0.5444 while simultaneously producing the longest wall clock in the whole record (26.10 s). Reward is not being paid for cheap steps.

**Pushing per-step cost far above the band.** Ruled out by the hard ceiling. Attempt 25 reached 3.2459× the seed anchor against a stated ceiling of 3.0, crossed the red line, lost validity and scored exactly 0.0000. Anything that lifts the ratio beyond 3.0 forfeits the entire reward regardless of task quality — note that attempt 25 still had `primary_target_reached` 1.0 and `rule_conformance` 1.0 and it did not matter.

**Any module with import-time side effects.** Ruled out by C-API-SURFACE, which has now rejected three separate submissions with the identical reason. There is no reward configuration that survives it: all three occurrences zeroed `task_pass` and landed in the bottom five.

**Simply re-running the Class A / Class C configuration and hoping for variance.** Attempts 22, 23, 24 and 26 all sat in the same 1.554–1.604 cost band as attempt 21 after attempt 21 had already scored 0.7322, and all four came in lower (0.6376, 0.6877, 0.6833, 0.6518). Re-sampling the band without changing what makes the run short is not producing improvement.

**Longer wall-clock runs as a way of buying quality.** Every measured record with `wall_clock_sec` above 23 s scored at or below 0.5830 (attempts 8, 15, 17). The best result is also the shortest run at 14.3905 s. Spending more wall clock has never once paid.

## 5. Open leads

**Reproduce attempt 21's operating point precisely, and treat wall clock as the lever.** The single strongest signal in the data is that attempt 21 combined the shortest wall clock ever measured (14.3905 s, well under the 17.4 s and 20.1 s clusters everything else falls into) with a per-step cost ratio in the productive 1.55–1.63 band and full conformance. Attempt 2 (17.4531 s, ratio 1.5175, 0.7155) and attempt 19 (17.4869 s, ratio 1.5834, 0.7134) are the next two best and are also on the short side of their band. Target: cost ratio ≈ 1.55–1.60, total wall clock at or under ~14.5 s, `compute_efficiency` around 0.61–0.62. Do not chase efficiency upward; the data says that direction costs reward.

**Understand what made attempt 21 short.** The `qualifying_budget` equals `wall_clock_sec` in every measured record, so the budget metric is just elapsed time — reward is being paid substantially for finishing fast while still reaching the primary target and both perturbation thresholds. Candidate mechanisms worth trying: an early-stopping criterion that halts as soon as the target metric clears its threshold rather than running a fixed epoch count; fewer, larger steps at the same per-step cost rather than more, cheaper ones (this is consistent with the Class B finding that cheaper steps produced *longer* total runs); and avoiding any fixed-length warmup or evaluation loop that runs after the target is already met.

**Harden the held-out variant path.** The perturbation results are unambiguous by kind. Across the 24 measured records, 48 perturbation units ran: 24 of kind `ruleset` and 24 of kind `held_out_variant`. **Every single `ruleset` unit reached its threshold — 24 of 24, zero failures.** The `held_out_variant` kind reached 22 of 24 times and is the only kind that has ever failed; on both failures (attempts 12 and 25) the unit failed the same pair of checks, **C-TARGET-REACHED and C-BUDGET-RESPECTED**, i.e. it did not hit its threshold and it also ran past its own budget. The units are not identified and must not be assumed to be the same run across records. The lead: whatever makes the run fast must not be tuned so tightly to the primary setting that a held-out variant needs more steps than its budget allows. A convergence criterion expressed as a target-met condition with a hard step cap, rather than a hand-tuned fixed step count, would satisfy both C-TARGET-REACHED and C-BUDGET-RESPECTED in the variant while keeping the primary run short.

**Free-throw checklist before submitting anything.** (a) No module-level statements beyond imports, constants and definitions — this alone accounts for three of the five worst measured rewards. (b) Keep per-step cost ratio comfortably below 3.0; the productive band is ~1.5–1.6 and there is no evidence that approaching 3.0 helps. (c) Make sure the submission actually runs to completion — two attempts returned `harbor_exception` and produced no measurement at all, forfeiting their information as well as their score.

**Call: exploit.** Attempt 21 at 0.7322 is the mark to beat and the top of the table is still moving (0.7155 → 0.7322), so the scoring approach has not plateaued. The exploit is to rebuild the Class C configuration at attempt 21's exact operating point — per-step cost ratio ~1.57, wall clock ~14.4 s, full conformance — and then attack the one lever that separates it from the rest of its own class, total wall clock, while keeping the held-out-variant budget satisfied. Note for the record that later attempts repeatedly re-sampled the same cost band without changing what made attempt 21 short, and came in lower each time; repeating that is neither exploiting nor exploring.
