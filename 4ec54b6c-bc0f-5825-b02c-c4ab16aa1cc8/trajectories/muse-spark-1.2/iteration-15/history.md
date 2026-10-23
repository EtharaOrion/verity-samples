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

    All 13 attempts since have scored lower than it.
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
  16       0.5701   1.000             2 of 2         yes             21                
  17       0.5274   0.857             2 of 2         yes             24                

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
  11 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 15 -- reward 0.5830, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 24
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 16 -- reward 0.5701, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 17 -- reward 0.5274, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 24
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (9, 17). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Fifteen of the seventeen attempts carry a measured reward. Listed worst to best:

| Rank | Attempt | reward | Standing recorded by the harness |
|---|---|---|---|
| 1 (worst) | 12 | 0.4962 | worse than an earlier attempt |
| 2 | 9 | 0.5164 | worse than an earlier attempt |
| 3 | 17 | 0.5274 | worse than an earlier attempt |
| 4 | 8 | 0.5444 | worse than an earlier attempt |
| 5 | 13 | 0.5590 | worse than an earlier attempt |
| 6 | 16 | 0.5701 | worse than an earlier attempt |
| 7 | 4 | 0.5792 | worse than an earlier attempt |
| 8 | 15 | 0.5830 | worse than an earlier attempt |
| 9 | 10 | 0.5983 | worse than an earlier attempt |
| 10 | 3 | 0.6279 | worse than an earlier attempt |
| 11 | 14 | 0.6426 | worse than an earlier attempt |
| 12 | 5 | 0.6587 | worse than an earlier attempt |
| 13 | 11 | 0.6639 | worse than an earlier attempt |
| 14 | 1 | 0.6694 | first measured attempt |
| 15 (best) | 2 | 0.7155 | better than every earlier attempt |

**Attempt 2 holds the highest reward, 0.7155. That is the number to beat.**

Attempts 6 and 7 have measurement_status `harbor_exception`. They produced **no measurement at all** — no reward, no conformance, no perturbation units. They did not score zero and must not be treated as failures of the approach they carried; nothing about their content can be inferred from the record.

The plain shape of the record is that every attempt after the second was worse than the second. Attempts 3, 4, 5, 8, 10, 11, 12, 13, 14, 15, 16 and 17 are each recorded as `worse_than_an_earlier_attempt`; the loop peaked at attempt 2 and has been descending or wandering below it ever since. That is a regression against the best, not slow progress.

Supporting terms worth carrying forward for every measured record: `validity` = 1.0, `red_line_crossed` = 0.0, and `zero_reason_code` = 0 in all fifteen. `qualifying_budget` is numerically identical to `wall_clock_sec` in all fifteen, so the budget term reports elapsed time and nothing else. `task_pass` = 1.0 everywhere except attempts 9, 12 and 17, which recorded `task_pass` = 0.0 alongside a failed check.

The full per-attempt cost signature, which is the only handle on what each submission actually did, is:

| Attempt | wall_clock_sec | compute_efficiency | per_step_cost_ratio | reward |
|---|---|---|---|---|
| 1 | 17.426 | 0.5488 | 1.5134 | 0.6694 |
| 2 | 17.453 | 0.6205 | 1.5175 | **0.7155** |
| 3 | 20.300 | 0.6033 | 1.5225 | 0.6279 |
| 4 | 17.512 | 0.8832 | 1.1656 | 0.5792 |
| 5 | 20.529 | 0.6098 | 1.6262 | 0.6587 |
| 8 | 26.098 | 0.9679 | 0.9674 | 0.5444 |
| 9 | 17.122 | 0.6647 | 1.4988 | 0.5164 |
| 10 | 20.150 | 0.5686 | 1.5152 | 0.5983 |
| 11 | 20.057 | 0.8424 | 1.0166 | 0.6639 |
| 12 | 16.781 | 0.6278 | 1.4886 | 0.4962 |
| 13 | 20.600 | 0.7642 | 1.2404 | 0.5590 |
| 14 | 17.780 | 0.6320 | 1.6303 | 0.6426 |
| 15 | 23.702 | 0.6165 | 1.6313 | 0.5830 |
| 16 | 20.984 | 0.8684 | 1.1256 | 0.5701 |
| 17 | 23.581 | 0.8228 | 1.2123 | 0.5274 |

# 2. Approach classes tried

No source code carries forward between attempts, so the approaches below are grouped by the measured signature each one left — `per_step_cost_ratio`, `compute_efficiency` and `wall_clock_sec` — which is the only evidence of what the submission did. Records with the same signature and the same outcome are treated as one entry.

**Class A — baseline-cost training loop, short budget.** `per_step_cost_ratio` clustered tightly at 1.49–1.52 with `compute_efficiency` 0.55–0.66 and wall clock at or just under 17.5 s. Attempts 1 and 2 are the clean members. This class produced the two highest rewards on record, 0.6694 and 0.7155. Attempt 2 sits at `compute_efficiency` 0.6205 with the same wall clock as attempt 1 (17.45 s vs 17.43 s) and a materially higher reward, so within this class doing somewhat more useful work per second of the same envelope was rewarded.

**Class B — Class A stretched to a longer budget.** Same cost ratio band (1.5152–1.5225) but wall clock pushed to roughly 20.2–20.3 s: attempts 3 and 10, rewards 0.6279 and 0.5983. Both are below attempt 2 despite the near-identical per-step signature. Holding the per-step regime fixed and spending three more seconds cost roughly 0.09–0.12 reward.

**Class C — heavier per-step work.** `per_step_cost_ratio` at 1.626–1.631, the most expensive step regime tried: attempts 5, 14 and 15, rewards 0.6587, 0.6426 and 0.5830. The two short-budget members (14 at 17.78 s, 5 at 20.53 s) landed in the 0.64–0.66 band; the long member (15 at 23.70 s) fell to 0.5830. This class never reached attempt 2 but its short members are competitive with Class B.

**Class D — cheapened step, mid efficiency.** `per_step_cost_ratio` 1.13–1.24 with `compute_efficiency` 0.76–0.88: attempts 4, 13 and 16, rewards 0.5792, 0.5590 and 0.5701. All three are far below attempt 2, including attempt 4, which achieved this at essentially attempt 2's wall clock (17.51 s). This is the cleanest controlled comparison in the whole record: same budget, much better compute_efficiency, reward down by 0.1363.

**Class E — cheapest step, efficiency maximised.** `per_step_cost_ratio` at or below 1.02 with `compute_efficiency` 0.84–0.97: attempts 8 and 11, rewards 0.5444 and 0.6639. Attempt 8 pushed `compute_efficiency` to 0.9679 and `per_step_cost_ratio` to 0.9674 — the best efficiency numbers ever measured — and produced the lowest reward of any conformant attempt, 0.5444, at the longest wall clock on record, 26.10 s. Attempt 11 is the interesting outlier: `per_step_cost_ratio` 1.0166 at 20.06 s returned 0.6639, third-best overall and within 0.052 of attempt 2. So cheap steps are not uniformly fatal; attempt 11 is the one cheap-step configuration that nearly competed.

**Class F — submissions with module-level executable code.** Attempts 9 and 17. Both failed `C-API-SURFACE`, both recorded `rule_conformance` 0.857 and `task_pass` 0.0, rewards 0.5164 and 0.5274. These span two different cost regimes (1.4988 and 1.2123), so the file-structure defect is orthogonal to the training approach they carried.

**Class G — budget trimmed below what the held-out variant needs.** Attempt 12, the shortest run on record at 16.78 s, `per_step_cost_ratio` 1.4886 — a Class A cost regime with the budget squeezed. It failed `C-PERTURBATION-REACHED` and scored the lowest reward measured, 0.4962.

**Unclassifiable.** Attempts 6 and 7 raised harbor exceptions and left no measured terms; whatever they tried is unrecoverable from this record and should not be assumed to have failed on its merits.

# 3. Checks that failed

Twelve of the fifteen measured attempts recorded an empty `failed_checks` list, `conformance_fraction` 1.0 and `rule_conformance` 1.0. Three did not.

**`C-API-SURFACE` — reason: "module-level statements outside imports, constants, and permitted definitions".** This check has now failed **twice**, at attempt 9 and at attempt 17. Both times it drove `rule_conformance` to 0.8571 and `task_pass` to 0.0. The two attempts sat in visibly different training regimes (`per_step_cost_ratio` 1.4988 versus 1.2123; `compute_efficiency` 0.6647 versus 0.8228; wall clock 17.12 s versus 23.58 s), and both perturbation units reached their thresholds in both records. **Whatever was changed in the algorithm between those two attempts is not what causes this failure.** The cause is the shape of the submission file itself: executable statements were left at module scope. Only imports, constants and permitted definitions may appear there; everything else must live inside a function or method body. This is a mechanical fix and it is worth roughly 0.05–0.15 of reward given where those two attempts landed.

**`C-PERTURBATION-REACHED` — reason: "1 of 2 declared perturbations reached their own threshold inside their own budget".** Failed once, at attempt 12. It set `conformance_fraction` to 0.5, `all_perturbations_held` to false and `task_pass` to 0.0, while `rule_conformance` stayed at 1.0 and the primary target was still reached. Attempt 12 was the shortest run measured, 16.78 s.

**Unit-level checks inside that failure: `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.** Both were recorded against the same non-reaching perturbation unit in attempt 12. They have failed once each, together, in that one record.

No other check has ever been named. `red_line_crossed` is 0.0 and `validity` is 1.0 in every measured record, so nothing has ever tripped a red line or been ruled invalid.

# 4. Ruled-out directions

**Maximising `compute_efficiency` / minimising `per_step_cost_ratio` as the route to reward.** Ruled out by direct measurement. The best efficiency ever achieved, attempt 8 at `compute_efficiency` 0.9679 and `per_step_cost_ratio` 0.9674, produced the lowest reward among conformant attempts, 0.5444. The whole cheap-step band (Classes D and E, cost ratio ≤ 1.24) spans rewards 0.5444–0.6639 and never once matched attempt 2's 0.7155, which was earned at cost ratio 1.5175. Attempt 4 is the decisive control: at attempt 2's wall clock, 17.51 s versus 17.45 s, it raised `compute_efficiency` from 0.6205 to 0.8832 and reward fell from 0.7155 to 0.5792. Reward is not monotone in efficiency, and pushing efficiency up is not a way to climb.

**Spending more wall clock.** Ruled out. Every attempt at or above 20.9 s scored 0.5830 or less (16 at 20.98 s → 0.5701; 15 at 23.70 s → 0.5830; 17 at 23.58 s → 0.5274; 8 at 26.10 s → 0.5444). Holding the per-step regime fixed and lengthening the run cost reward directly: Class A at ~17.45 s gave 0.6694 and 0.7155, the same regime at ~20.2–20.3 s gave 0.6279 and 0.5983.

**Leaving executable statements at module scope.** Ruled out by two independent failures of `C-API-SURFACE`, attempts 9 and 17, each zeroing `task_pass`.

**Trimming the budget below the held-out variant's requirement.** Ruled out by attempt 12: the shortest run measured, 16.78 s, failed `C-PERTURBATION-REACHED` with the held-out variant missing both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, and produced the worst reward on record, 0.4962. The floor on runtime is set by the perturbation runs, not by the primary target — the primary target was reached in that same attempt. Roughly 17.1 s (attempt 9, where both units reached) is demonstrably survivable; 16.78 s is not.

**Re-running Class C's heavy-step regime at long budgets.** Ruled out: attempt 15 at cost ratio 1.6313 and 23.70 s returned 0.5830, well under its own short-budget siblings 14 (0.6426) and 5 (0.6587).

# 5. Open leads

**The perturbation picture, reported by kind.** Every measured attempt declared exactly two perturbation units: one of kind `held_out_variant` and one of kind `ruleset`. In aggregate that is 30 unit runs across the fifteen measured records, of which 29 reached their threshold. The `ruleset` kind reached its threshold in all fifteen records with no failed checks — it has never been a problem. The `held_out_variant` kind reached in fourteen of fifteen; the single failure was in attempt 12, where that unit failed `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. The units are not individually identified in the records, so nothing links a unit in one record to a unit in another beyond its kind. The lead: the binding runtime constraint comes from the `held_out_variant` kind, and the safe operating point is a wall clock comfortably above 17.1 s.

**Rebuild attempt 2's operating point exactly.** The target signature is wall clock 17.4–17.5 s, `per_step_cost_ratio` ≈ 1.52, `compute_efficiency` ≈ 0.62, both perturbation units reaching, no module-level statements. Nothing since has come within 0.045 of it. Reconstructing that regime and confirming it reproduces near 0.7155 is the highest-value single action available, because the loop has not held that point since attempt 2 and eleven subsequent attempts drifted away from it in cost ratio, in budget, or both.

**Probe the untested efficiency band 0.63–0.84 at a ~17.5 s budget.** Measured points at short budget are 0.5488 → 0.6694, 0.6205 → 0.7155, 0.6320 (at 17.78 s) → 0.6426, and 0.8832 → 0.5792. The interior of that range at exactly attempt 2's budget has never been sampled cleanly; attempt 9 sat at 0.6647 but was voided by `C-API-SURFACE`, so its underlying algorithm is untested rather than disproven. Re-submitting attempt 9's regime with the module-level statements moved inside function bodies is a concrete, cheap experiment: it is the one configuration in the record whose training merit was never measured because of a mechanical defect.

**Re-examine attempt 11.** It is the only cheap-step configuration that competed, 0.6639 at `per_step_cost_ratio` 1.0166 and 20.06 s. Its neighbours in Class E and D are all 0.54–0.58. Shortening attempt 11's budget from 20.06 s toward 17.5 s while keeping its cost ratio is an untested combination — every cheap-step run except attempt 4 was also a long run, so budget and cost ratio were confounded across that class.

**Guard against the two known conformance failures on every submission.** Before shipping: verify that the module contains only imports, constants and permitted definitions at top level (`C-API-SURFACE`, failed twice), and keep the runtime above ~17.1 s so the `held_out_variant` unit clears `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` (`C-PERTURBATION-REACHED`, failed once).

**Note on the two unmeasured attempts.** Attempts 6 and 7 both raised harbor exceptions. Nothing is known about what they attempted or whether it was promising; they should not be counted as evidence against any direction.

**Call: exploit.** The scoring approach — Class A, the baseline-cost loop at a ~17.5 s budget — has not been revisited since attempt 2, and the fourteen attempts since have explored away from it rather than refining it. Two of the last nine attempts were also lost to a mechanical `C-API-SURFACE` violation that has nothing to do with the algorithm, which is repetition of a known-void configuration rather than either exploration or exploitation. The next attempt should reconstruct attempt 2's regime, fix the module-level-statement defect by construction, and vary only `compute_efficiency` within 0.62–0.75 at that fixed budget.
