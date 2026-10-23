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

    All two attempts since have scored lower than it.
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

    attempt 22 -- reward 0.6376, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 23 -- reward 0.6877, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (9, 17, 20). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-three graded records. Twenty-one carry a reward; two (attempts 6 and 7) came back with `measurement_status: harbor_exception` and produced **no measurement at all** — they are not zeros and must not be treated as evidence about the code they contained.

Ranked worst to best by reward:

| Rank | Attempt | reward | wall_clock_sec | compute_efficiency | per_step_cost_ratio | failed checks |
|---|---|---|---|---|---|---|
| 1 | 12 | 0.4962 | 16.78 | 0.6278 | 1.4886 | C-PERTURBATION-REACHED |
| 2 | 20 | 0.5107 | 17.39 | 0.6658 | 1.5804 | C-API-SURFACE |
| 3 | 9 | 0.5164 | 17.12 | 0.6647 | 1.4988 | C-API-SURFACE |
| 4 | 17 | 0.5274 | 23.58 | 0.8228 | 1.2123 | C-API-SURFACE |
| 5 | 8 | 0.5444 | 26.10 | 0.9679 | 0.9674 | none |
| 6 | 13 | 0.5590 | 20.60 | 0.7642 | 1.2404 | none |
| 7 | 16 | 0.5701 | 20.98 | 0.8684 | 1.1256 | none |
| 8 | 18 | 0.5755 | 20.63 | 0.6466 | 1.5846 | none |
| 9 | 4 | 0.5792 | 17.51 | 0.8832 | 1.1656 | none |
| 10 | 15 | 0.5830 | 23.70 | 0.6165 | 1.6313 | none |
| 11 | 10 | 0.5983 | 20.15 | 0.5686 | 1.5152 | none |
| 12 | 3 | 0.6279 | 20.30 | 0.6033 | 1.5225 | none |
| 13 | 22 | 0.6376 | 17.37 | 0.6629 | 1.5983 | none |
| 14 | 14 | 0.6426 | 17.78 | 0.6320 | 1.6303 | none |
| 15 | 5 | 0.6587 | 20.53 | 0.6098 | 1.6262 | none |
| 16 | 11 | 0.6639 | 20.06 | 0.8424 | 1.0166 | none |
| 17 | 1 | 0.6694 | 17.43 | 0.5488 | 1.5134 | none |
| 18 | 23 | 0.6877 | 20.11 | 0.6081 | 1.5949 | none |
| 19 | 19 | 0.7134 | 17.49 | 0.6001 | 1.5834 | none |
| 20 | 2 | 0.7155 | 17.45 | 0.6205 | 1.5175 | none |
| 21 | **21** | **0.7322** | **14.39** | 0.6162 | 1.5700 | none |

**Attempt 21 holds the highest reward, 0.7322. That is the number to beat.**

Attempt 2 (0.7155) was the only other record marked `better_than_every_earlier_attempt`. Every single record after attempt 2 other than attempt 21 carries `standing_against_best_so_far: worse_than_an_earlier_attempt`. Stating that plainly: attempts 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22 and 23 all scored **lower** than a result already achieved. Attempt 23 (0.6877) is the most recent measured record and it is **below** attempt 21's 0.7322 — the last move was a regression, not progress. In particular the sequence 21 → 22 → 23 went 0.7322 → 0.6376 → 0.6877: two consecutive results beneath the peak.

Invariants across every measured record: `validity` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, `primary_target_reached` 1.0, `perturbations_declared` 2.0. No attempt has ever failed validity or crossed a red line, and the primary target was reached even in the four records that failed a conformance check. `task_pass` is 1.0 in every record except 9, 12, 17 and 20, which are exactly the four records carrying a failed check.

# 2. Approach classes tried

The records do not carry source, so these classes are inferred from the measured cost signature (`wall_clock_sec`, which equals `qualifying_budget` in every record, plus `compute_efficiency` and `per_step_cost_ratio`). Distinct classes, not distinct records:

**Class A — short-schedule, high-per-step-cost configurations.** Signature: `per_step_cost_ratio` roughly 1.49–1.63 with `compute_efficiency` roughly 0.55–0.67, wall clock 14.4–20.6 s. This class contains essentially every top result: attempts 21 (0.7322), 2 (0.7155), 19 (0.7134), 23 (0.6877), 1 (0.6694), 5 (0.6587), 14 (0.6426), 22 (0.6376), 3 (0.6279). The reading is that each optimisation step does substantially more work than the harness baseline (ratio ~1.5–1.6) but far fewer steps are taken, so total wall clock stays low. This is the productive class.

**Class B — cheap-per-step, long-schedule configurations.** Signature: `per_step_cost_ratio` driven down toward or below 1.0 (0.97–1.24) with `compute_efficiency` pushed up to 0.76–0.97, and wall clock rising to 20.6–26.1 s. Attempts 8 (psc 0.9674, ce 0.9679, wall 26.10 s, reward 0.5444), 4 (psc 1.1656, ce 0.8832, reward 0.5792), 16 (psc 1.1256, ce 0.8684, reward 0.5701), 13 (psc 1.2404, ce 0.7642, reward 0.5590), 11 (psc 1.0166, ce 0.8424, reward 0.6639). Attempt 8 is the extreme of this class and produced nearly the worst clean reward on record. **Maximising `compute_efficiency` and minimising `per_step_cost_ratio` moves reward down, not up.** The single partial exception is attempt 11 at 0.6639, which reached that reward with a low per-step ratio but still fell short of every Class A leader.

**Class C — Class A shape with module-level executable code.** Attempts 9, 17 and 20. These sit inside the Class A cost envelope (9: psc 1.4988, wall 17.12 s; 20: psc 1.5804, wall 17.39 s) or between A and B (17: psc 1.2123, wall 23.58 s), but every one of them tripped C-API-SURFACE, dropped `task_pass` to 0.0 and `rule_conformance` to 0.8571, and landed at 0.5164, 0.5274 and 0.5107. Three of the four lowest rewards ever recorded belong to this class.

**Class D — Class A shape whose held-out variant run over-ran.** Attempt 12 alone: psc 1.4886, wall 16.78 s on the primary run, `conformance_fraction` 0.5, `all_perturbations_held` false, reward 0.4962 — the lowest measured result of the whole run. The primary target was still reached (1.0) and rule_conformance was a clean 1.0; the loss came entirely from the held-out variant.

**Class E — attempts that never reached measurement.** Attempts 6 and 7, both `harbor_exception`. No cost signature, no reward, no failed checks recorded. Nothing about the algorithm they contained can be inferred from these records in either direction.

# 3. Checks that failed

Two named checks have ever failed, plus the perturbation-level checks beneath one of them.

**C-API-SURFACE** — verifier reason, quoted identically in all three records: *"module-level statements outside imports, constants, and permitted definitions"*. **This check has now failed three times: attempts 9, 17 and 20.** It is the dominant recurring failure. Attempts 9, 17 and 20 differed from each other in their cost profile (17 ran 23.58 s with `per_step_cost_ratio` 1.2123 while 9 and 20 ran ~17.1–17.4 s with ratios near 1.50 and 1.58), which means whatever was varied between those three attempts is **not** what causes C-API-SURFACE. It is not a function of the schedule, the step cost, the runtime or the optimiser: it is caused by the submission module executing statements at import time that are neither imports, nor constant assignments, nor permitted definitions. Each failure cost `task_pass` (1.0 → 0.0) and dropped `rule_conformance` to 0.8571429, i.e. one of seven rules. The three affected rewards, 0.5164, 0.5274 and 0.5107, sit far below what their cost profiles would otherwise suggest — attempt 20's profile is close to attempt 19's (0.7134) and 2's (0.7155), so this check plausibly costs on the order of 0.2 reward.

**C-PERTURBATION-REACHED** — attempt 12 only, once. Verifier reason: *"1 of 2 declared perturbations reached their own threshold inside their own budget"*. `conformance_fraction` fell to 0.5, `all_perturbations_held` to false, `task_pass` to 0.0, and the reward, 0.4962, is the lowest ever measured.

**Perturbation-unit checks, beneath attempt 12:** the held-out run that failed was of kind `held_out_variant`, and it failed two checks — **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**. It both missed its threshold and exceeded its own budget. The other run in that record, of kind `ruleset`, reached its threshold with no failed checks.

**Aggregate over held-out runs.** Every measured record declares two perturbations, one of kind `held_out_variant` and one of kind `ruleset`. Across the twenty-one measured records that is 21 `ruleset` runs and 21 `held_out_variant` runs.
- Kind `ruleset`: 21 of 21 reached threshold, zero failed checks. This kind has never failed.
- Kind `held_out_variant`: 20 of 21 reached threshold; one did not, failing C-TARGET-REACHED and C-BUDGET-RESPECTED.
- Aggregate: 41 of 42 held-out runs reached threshold. `all_perturbations_held` is true in twenty of the twenty-one measured records.

The runs are not identified by name, number or position, so nothing here asserts that any particular run recurs across records — only that the failing kind is `held_out_variant` and the checks it failed are C-TARGET-REACHED and C-BUDGET-RESPECTED.

# 4. Ruled-out directions

**Pushing `compute_efficiency` toward 1.0 by cutting `per_step_cost_ratio` toward 1.0 or below.** Ruled out. Attempt 8 achieved the best `compute_efficiency` on record (0.9679) with `per_step_cost_ratio` 0.9674 and scored 0.5444 — near the bottom of the clean results — because it took 26.10 s of wall clock, the longest of any record. Attempts 4 (0.8832 / 1.1656 → 0.5792), 16 (0.8684 / 1.1256 → 0.5701) and 13 (0.7642 / 1.2404 → 0.5590) reproduce the same relation. `compute_efficiency` as reported is not the graded quantity and optimising it directly has cost reward every time it was tried.

**Long wall clock as a way to buy quality.** Ruled out at the top end. The three longest runs — 8 at 26.10 s (0.5444), 15 at 23.70 s (0.5830) and 17 at 23.58 s (0.5274, also C-API-SURFACE) — occupy the lower half of the table, while the shortest run on record, 21 at 14.39 s, is the best result on record at 0.7322. Note this is a tendency, not a law: 23 ran 20.11 s for 0.6877 and 3 ran 20.30 s for only 0.6279, so runtime alone does not determine the score.

**Re-submitting the Class C module shape without removing module-level executable code.** Ruled out. Three attempts (9, 17, 20) hit C-API-SURFACE with the identical verifier reason and each forfeited `task_pass`. Attempting Class A again while leaving import-time statements in place will forfeit `task_pass` again regardless of how good the training algorithm is; the check fires before the algorithm's quality can be rewarded.

**Whatever attempt 12 did to the held-out variant's schedule or budget.** Ruled out. It produced the lowest reward on record by failing both C-TARGET-REACHED and C-BUDGET-RESPECTED on the `held_out_variant` run — the variant neither hit its threshold nor stayed inside its own budget. Any configuration that leaves no budget headroom on the variant run risks the same 0.5 `conformance_fraction`.

**Treating attempts 6 and 7 as evidence.** Ruled out as a source of signal, in both directions. They are `harbor_exception` records with no reward and no failed checks; they say nothing about the code, and should not be avoided *or* repeated on the strength of these records.

# 5. Open leads

**Lead 1 — rebuild the attempt-21 configuration and defend its runtime.** Attempt 21 is the only record under 15 s (14.39 s) and the only record above 0.73. Its profile is `per_step_cost_ratio` 1.5700, `compute_efficiency` 0.6162, clean on every check, both perturbation runs reached. The single most defensible target is: keep the Class A shape (per-step cost ratio ~1.5–1.6, i.e. do more work per step and take fewer steps) and drive total wall clock at or below 14.4 s. The four best results — 21 (14.39 s), 2 (17.45 s), 19 (17.49 s), 23 (20.11 s) — are all Class A, and among them the shortest wins.

**Lead 2 — eliminate C-API-SURFACE structurally, not incidentally.** The submission module must contain nothing at module scope beyond imports, constant assignments and permitted definitions. Every piece of setup — seeding, device selection, config construction, model or optimiser instantiation, any `print`, any `if`/`for`, any call — belongs inside a function or method body, or must be deferred to first use inside the entry point. Constants must be literal assignments, not computed at import time. This check has failed three times across three differently-configured attempts; scheduling and cost changes have never fixed it and will not.

**Lead 3 — reserve explicit headroom on the held-out variant run.** The only perturbation failure on record is a `held_out_variant` that failed C-TARGET-REACHED *and* C-BUDGET-RESPECTED together. Because the variant is graded against its own threshold inside its own budget, an early-exit or budget-aware stopping condition — stop when the target is met, and unconditionally stop before the budget is exhausted rather than running a fixed step count — protects `conformance_fraction` while still allowing Lead 1's aggressive schedule. The `ruleset` kind has never failed and needs no special handling.

**Lead 4 — treat the residual spread as run-to-run variance and reduce it.** Attempts with near-identical cost profiles produced materially different rewards: at ~17.4–17.5 s, attempt 2 scored 0.7155, attempt 19 0.7134, attempt 1 0.6694, attempt 22 0.6376, attempt 4 0.5792. Cost alone does not explain a 0.14 spread. Something in the training result varies between runs. Tightening determinism — fixed seeding inside the entry function, deterministic data ordering, deterministic reductions — would both raise the expected score and stop good configurations from being discarded on a bad draw.

**Lead 5 — the untested middle band.** No record exists between 14.39 s and 16.78 s other than the peak itself. If shaving wall clock is what carried attempt 21, the 12–14 s band is unexplored and is where the next gain most plausibly lies — provided the primary target and both perturbation thresholds are still reached, since attempt 12 shows that a fast primary run (16.78 s) is worthless if the variant run misses its own threshold.

**Call: exploit.** Attempt 21 (0.7322) is the standing best and the Class A shape it belongs to holds four of the top five results; that class has not been exhausted, and the last three measured records all fell below it rather than extending it. Reconstruct the Class A short-schedule / high-per-step-cost configuration, drive wall clock toward and below 14.4 s, and carry Leads 2 and 3 as hard constraints so the run cannot forfeit `task_pass`. Note for the record that Class C was attempted three separate times without ever addressing the module-level-statement cause of C-API-SURFACE — that pattern is neither exploration nor exploitation and must not be repeated.
