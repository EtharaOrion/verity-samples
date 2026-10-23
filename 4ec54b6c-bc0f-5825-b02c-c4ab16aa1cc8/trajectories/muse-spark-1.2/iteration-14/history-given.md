# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 2 -- reward 0.7155, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All 11 attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2 *      0.7155   1.000             2 of 2         yes             17                
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
  9 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.6639, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 13 -- reward 0.5590, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 14 -- reward 0.6426, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 18
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 15 -- reward 0.5830, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 24
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 9.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Fifteen submissions were graded. Thirteen produced a measurement; two (attempts 6 and 7) came back with `measurement_status: harbor_exception` and therefore produced **no measurement at all** — they carry no reward and must not be read as zeros or as failures of the algorithm. No `failed_checks` were recorded for them either, so nothing about their content can be inferred from the record.

The thirteen measured attempts, ordered worst to best by reward:

| Rank | Attempt | reward | wall_clock_sec (= qualifying_budget) | compute_efficiency | per_step_cost_ratio | task_pass |
|---|---|---|---|---|---|---|
| 1 (worst) | 12 | 0.4962 | 16.78 | 0.6278 | 1.4886 | 0.0 |
| 2 | 9 | 0.5164 | 17.12 | 0.6647 | 1.4988 | 0.0 |
| 3 | 8 | 0.5444 | 26.10 | 0.9679 | 0.9674 | 1.0 |
| 4 | 13 | 0.5590 | 20.60 | 0.7642 | 1.2404 | 1.0 |
| 5 | 4 | 0.5792 | 17.51 | 0.8832 | 1.1656 | 1.0 |
| 6 | 15 | 0.5830 | 23.70 | 0.6165 | 1.6313 | 1.0 |
| 7 | 10 | 0.5983 | 20.15 | 0.5686 | 1.5152 | 1.0 |
| 8 | 3 | 0.6279 | 20.30 | 0.6033 | 1.5225 | 1.0 |
| 9 | 14 | 0.6426 | 17.78 | 0.6320 | 1.6303 | 1.0 |
| 10 | 5 | 0.6587 | 20.53 | 0.6098 | 1.6262 | 1.0 |
| 11 | 11 | 0.6639 | 20.06 | 0.8424 | 1.0166 | 1.0 |
| 12 | 1 | 0.6694 | 17.43 | 0.5488 | 1.5134 | 1.0 |
| 13 (best) | **2** | **0.7155** | 17.45 | 0.6205 | 1.5175 | 1.0 |

**Attempt 2 holds the highest reward at 0.7155 and is the one to beat.**

Attempt 1 (0.6694) was the first measured attempt. Attempt 2 (0.7155) is the only record marked `better_than_every_earlier_attempt`. **Every single measured attempt after attempt 2 — that is attempts 3, 4, 5, 8, 9, 10, 11, 12, 13, 14 and 15 — is marked `worse_than_an_earlier_attempt`, and each of those rewards is lower than 0.7155.** That is eleven consecutive measured regressions against the standing best; none of them is progress and none should be described as such. The closest any of them came was attempt 11 at 0.6639, still below attempt 1's 0.6694 and 0.0516 below the best.

Other invariants across all thirteen measured records: `validity` = 1.0, `red_line_crossed` = 0.0, `zero_reason_code` = 0. `primary_target_reached` = 1.0 in all thirteen — the primary target has never been the obstacle. `qualifying_budget` is numerically identical to `wall_clock_sec` in every record, so budget consumption is wall-clock time.

## 2. Approach classes tried

No source code carries forward, so the classes below are identified by their measured cost fingerprints (`per_step_cost_ratio`, `compute_efficiency`, `wall_clock_sec`). These are the axes the work has actually been moving along, and the next attempt should reconstruct its configuration in these terms.

**Class A — moderate per-step cost, short run (`per_step_cost_ratio` ≈ 1.49–1.52, `compute_efficiency` ≈ 0.55–0.66).** Attempts 1, 2, 3, 9, 10, 12. This class contains both the best result (attempt 2, 0.7155) and the second-best (attempt 1, 0.6694), and also the two worst (attempts 12 at 0.4962 and 9 at 0.5164, both of which failed a conformance check — see section 3). Within the class, the two members that ran in ~17.4 s and held every check scored highest (0.7155, 0.6694), while the two that ran ~20.2 s scored 0.6279 and 0.5983. This is the productive class.

**Class B — heavier per-step cost (`per_step_cost_ratio` ≈ 1.63, `compute_efficiency` ≈ 0.61–0.63).** Attempts 5 (0.6587, 20.53 s), 14 (0.6426, 17.78 s), 15 (0.5830, 23.70 s). All held every check. All three land below attempt 2. Spending more per step bought nothing above the Class A ceiling.

**Class C — reduced per-step cost, mid efficiency (`per_step_cost_ratio` ≈ 1.17–1.24, `compute_efficiency` ≈ 0.76–0.88).** Attempts 4 (0.5792, 17.51 s) and 13 (0.5590, 20.60 s). Both held every check. Both are markedly worse than Class A at comparable wall clock: attempt 4 ran in essentially the same 17.5 s as attempt 2 yet scored 0.1363 lower.

**Class D — cheapest per-step cost, highest compute efficiency (`per_step_cost_ratio` ≈ 0.97–1.02, `compute_efficiency` ≈ 0.84–0.97).** Attempts 8 (0.5444, 26.10 s, efficiency 0.9679 — the highest recorded) and 11 (0.6639, 20.06 s). Both held every check. Attempt 8 achieved the best compute efficiency and the best (lowest) per-step cost ratio of the whole series and returned the third-lowest reward, at the longest wall clock recorded.

**Class E — unmeasurable submissions.** Attempts 6 and 7, both `harbor_exception`. No reward, no checks recorded, no cost terms. Nothing distinguishes them in the data beyond the fact that the harness did not complete a measurement on them.

The cross-class reading that the numbers support: reward is **not** monotone in `compute_efficiency` and **not** monotone in `per_step_cost_ratio`. The highest-efficiency, cheapest-per-step run (attempt 8) is near the bottom, and the best run (attempt 2) sits at middling efficiency 0.6205. Nor is reward a pure function of wall clock: attempts 1 and 2 ran 17.43 s and 17.45 s — indistinguishable — and scored 0.6694 versus 0.7155. Something in the submission other than these cost terms is carrying roughly 0.05–0.17 of reward and is what actually separates attempt 2 from the rest. Short wall clock (~17.4 s) appears necessary for the top band but is demonstrably not sufficient: attempts 4, 9 and 12 all ran under 17.6 s and scored 0.5792, 0.5164 and 0.4962.

## 3. Checks that failed

Only two of the thirteen measured records failed any check, and **no check has failed more than once.** There is no repeat offender in this series.

- **`C-API-SURFACE`**, attempt 9, verifier reason: *"module-level statements outside imports, constants, and permitted definitions."* This dropped `rule_conformance` to 0.8571 and `task_pass` to 0.0, with reward 0.5164. Note that `conformance_fraction` was still 1.0 and both perturbation units still reached — the failure was purely in the shape of the submitted module, not in what the algorithm did. Concretely: everything at module level must be an import, a constant, or a permitted definition (function/class). Any executable statement at module scope — a call, a print, a loop, an `if __name__` block, a computed assignment that isn't a plain constant — trips this.

- **`C-PERTURBATION-REACHED`**, attempt 12, verifier reason: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This dropped `conformance_fraction` to 0.5, set `all_perturbations_held` to false and `task_pass` to 0.0, with reward 0.4962 — the worst of the series. Notably `rule_conformance` stayed at 1.0 and `primary_target_reached` stayed at 1.0 here, so the primary run was fine and only a held-out run failed.

- Inside attempt 12, the failing perturbation unit additionally reported **`C-TARGET-REACHED`** and **`C-BUDGET-RESPECTED`** at the unit level. Both fired on the same unit, each once across the whole series.

## 4. Ruled-out directions

**Perturbation outcomes by kind.** Across the thirteen measured records, each declared two perturbations, giving 26 held-out units in total: 13 of kind `ruleset` and 13 of kind `held_out_variant`. Aggregate: 25 of 26 units reached their threshold. By kind, **`ruleset`: 13 of 13 reached, never failed a check.** **`held_out_variant`: 12 of 13 reached; the single failure was a `held_out_variant` unit that did not reach, stopped by `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.** So the only kind of held-out run that has ever failed is the `held_out_variant` kind, and it failed on target-reached and budget-respected together — it neither hit its threshold nor stayed inside its own budget. The runs are not individually identified in the data; there is no way to tell whether any particular unit is "the same" run across two records, and no such claim is made here.

Ruled out, with the measurement that rules it out:

- **Maximising `compute_efficiency` / minimising `per_step_cost_ratio` (Class D).** Attempt 8 reached efficiency 0.9679 and per-step ratio 0.9674, the best on both axes, and scored 0.5444 — third worst — while running 26.10 s, the longest of the series. Attempt 11 in the same class scored 0.6639. Neither beat attempt 2 at efficiency 0.6205. Driving these terms is not what the reward rewards; it appears to trade against wall clock and against whatever quality term separates the top attempts.

- **Cutting per-step cost into the 1.17–1.24 band (Class C).** Attempts 4 and 13 scored 0.5792 and 0.5590. Attempt 4 in particular matched attempt 2's wall clock almost exactly (17.51 s vs 17.45 s) and still lost 0.1363 of reward. Cheaper steps at equal runtime is a demonstrated loss.

- **Raising per-step cost into the ~1.63 band (Class B).** Attempts 5, 14 and 15 scored 0.6587, 0.6426 and 0.5830 — all below attempt 2, and the worst of them was also the longest at 23.70 s. Spending more per step does not recover the gap either.

- **Letting wall clock drift past ~20 s.** Every run over 20 s scored at or below 0.6639 (attempts 3, 5, 8, 10, 11, 13, 15). The top two rewards both came in at ~17.4 s. Long runs have never produced a top-band score.

- **Any module-level executable code.** Ruled out by `C-API-SURFACE` on attempt 9, which zeroed `task_pass` despite a fully successful run on both perturbation units and a perfectly ordinary 17.12 s / 0.6647-efficiency profile. The algorithm was fine; the file layout was not.

- **Tuning that satisfies only the primary run.** Ruled out by attempt 12: `primary_target_reached` = 1.0 and `rule_conformance` = 1.0, yet a `held_out_variant` unit missed both its threshold and its budget, halving `conformance_fraction` to 0.5, zeroing `task_pass`, and producing the series' lowest reward. Whatever was tightened for speed there (it also had the shortest wall clock recorded, 16.78 s) left no margin for the varied run.

- **Not ruled out but worth stating: the changes made between attempts 3–15 are not what caused the two check failures.** `C-API-SURFACE` and `C-PERTURBATION-REACHED` each appeared exactly once, in different attempts, and every other attempt with wildly different cost profiles held all checks. These are two independent, one-off defects, not a systemic property of any approach class.

## 5. Open leads

1. **Rebuild the attempt-2 profile and treat it as the floor.** Target the measured signature: wall clock ≈ 17.4–17.5 s, `per_step_cost_ratio` ≈ 1.51–1.52, `compute_efficiency` ≈ 0.62. Attempts 1 and 2 both sat in this window and are the only two above 0.66. Do not "improve" efficiency away from it.

2. **Isolate the attempt-1 → attempt-2 delta.** These two are the cleanest natural experiment in the data: near-identical wall clock (17.43 vs 17.45), near-identical per-step ratio (1.5134 vs 1.5175), yet reward moved 0.6694 → 0.7155. The +0.046 came from something that costs nothing in time or per-step compute — a quality-side change (optimiser/schedule/regularisation/seed-robustness class of change), not a budget-side one. That axis is the one still unexplored and the only one that has ever produced a gain.

3. **Guard the module surface before anything else.** Keep every module-level line to imports, plain literal constants, and function/class definitions. No calls, no loops, no conditionals, no `__main__` block, no computed module-level assignments. This is a free 0.0 → 1.0 on `task_pass` relative to attempt 9's failure mode and costs nothing.

4. **Validate against variation, not just the primary run.** The one perturbation failure was on a `held_out_variant` unit and hit `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` simultaneously. Leave headroom: an approach that finishes the primary run in 16.8 s with no slack is exactly the one that blew its budget on the varied run. Prefer a configuration whose convergence does not depend on a tightly-fitted step count or schedule length, and leave a visible time margin inside the per-unit budget. `ruleset` perturbations have never failed and need no special defence.

5. **Keep the submission plain and self-contained.** Two attempts returned `harbor_exception` and yielded no measurement at all. The records give no cause, so nothing can be diagnosed — but an unmeasured attempt is a total loss regardless of the algorithm in it. Avoid anything exotic in imports, I/O, or process behaviour that could stop the harness completing.

**Call: exploit.** The best approach class (Class A: per-step ratio ≈ 1.51, ~17.4 s) has never been beaten by any structural alternative — Classes B, C and D were each a genuine structural departure and all three came back below it, with the most extreme departure (attempt 8, maximum efficiency) landing near the bottom. The right move is to reconstruct attempt 2's cost profile exactly, apply the two zero-cost conformance fixes (no module-level statements; budget slack for the `held_out_variant` run), and then vary only the quality-side dimension that separated attempt 1 from attempt 2. Note plainly for the record: attempts 3 through 15 repeatedly re-tuned the cost axes — the very axes the data shows are flat or negatively related to reward — and produced eleven consecutive results below attempt 2. Continuing to move `compute_efficiency` or `per_step_cost_ratio` without changing the quality-side content would be repeating that.
