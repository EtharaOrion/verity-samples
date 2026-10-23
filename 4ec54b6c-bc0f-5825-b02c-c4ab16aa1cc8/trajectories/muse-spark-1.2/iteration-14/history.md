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

    All 12 attempts since have scored lower than it.
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
  10 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 16 -- reward 0.5701, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 9.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Every graded record, ordered worst to best by `reward`. Sixteen records exist; fourteen carry a measurement.

| Rank (worst→best) | Attempt | reward | Notes |
|---|---|---|---|
| 1 | 12 | 0.4962 | task_pass 0.0; failed C-PERTURBATION-REACHED |
| 2 | 9 | 0.5164 | task_pass 0.0; failed C-API-SURFACE; rule_conformance 0.8571 |
| 3 | 8 | 0.5444 | clean; compute_efficiency 0.9679, per_step_cost_ratio 0.9674, wall 26.098 s |
| 4 | 13 | 0.5590 | clean; eff 0.7642, psc 1.2404, wall 20.600 s |
| 5 | 16 | 0.5701 | clean; eff 0.8684, psc 1.1256, wall 20.984 s |
| 6 | 4 | 0.5792 | clean; eff 0.8832, psc 1.1656, wall 17.512 s |
| 7 | 15 | 0.5830 | clean; eff 0.6165, psc 1.6313, wall 23.702 s |
| 8 | 10 | 0.5983 | clean; eff 0.5686, psc 1.5152, wall 20.150 s |
| 9 | 3 | 0.6279 | clean; eff 0.6033, psc 1.5225, wall 20.300 s |
| 10 | 14 | 0.6426 | clean; eff 0.6320, psc 1.6303, wall 17.780 s |
| 11 | 5 | 0.6587 | clean; eff 0.6098, psc 1.6262, wall 20.529 s |
| 12 | 11 | 0.6639 | clean; eff 0.8424, psc 1.0166, wall 20.057 s |
| 13 | 1 | 0.6694 | clean; eff 0.5488, psc 1.5134, wall 17.426 s |
| 14 | 2 | **0.7155** | clean; eff 0.6205, psc 1.5175, wall 17.453 s |

**Attempt 2 holds the highest reward, 0.7155. That is the score to beat.**

Attempts 6 and 7 have `measurement_status: harbor_exception`. They produced **no measurement at all** — no reward, no efficiency, no perturbation units. They are not zeros and must not be counted as failures of the algorithm; nothing can be inferred from them about what their code did.

Every attempt after attempt 2 that was measured is marked `worse_than_an_earlier_attempt`. That is twelve consecutive measured regressions against the attempt-2 high-water mark. Attempt 1 was `first_measured_attempt`; attempt 2 was `better_than_every_earlier_attempt`; nothing since has matched it. Stated plainly: the run has been going backwards since attempt 2, not forwards.

Other invariants worth carrying: `red_line_crossed` is 0.0 in every measured record, `validity` is 1.0 in every measured record, and `rule_conformance` is 1.0 everywhere except attempt 9 (0.8571). `primary_target_reached` is 1.0 in all fourteen measured records — including attempts 9 and 12, whose `task_pass` is 0.0 for conformance/perturbation reasons rather than for missing the primary target.

# 2. Approach classes tried

The source code of prior attempts is not carried forward and was not supplied to me; what is available is each attempt's measured operating point. The approaches therefore have to be identified by their measured signature — wall-clock, per-step cost ratio, and compute efficiency — which is enough to re-derive the *regime* each one occupied, if not its line-by-line implementation.

**Class A — moderate per-step cost, short wall clock (psc ≈ 1.51–1.53, wall ≈ 17.4–17.5 s, eff ≈ 0.55–0.62).** Attempts 1 (0.6694) and 2 (0.7155). This is the only regime that has produced anything above 0.67. It spends noticeably more than baseline per step but finishes the whole run in the fastest observed bucket, and it accepts a low-to-middling compute_efficiency figure to do it. **Attempt 2 is the single best point ever measured and sits inside this class.**

**Class B — same moderate per-step cost, but a longer wall clock (psc ≈ 1.51–1.53, wall ≈ 20.1–20.3 s).** Attempts 3 (0.6279) and 10 (0.5983). Structurally the same cost profile as Class A, roughly 2.7–2.9 s slower end-to-end, and reward drops by 0.04–0.12. This is the cleanest controlled contrast in the whole record: holding per-step cost fixed and letting wall-clock grow costs reward.

**Class C — high per-step cost (psc ≈ 1.63) with varying wall clock.** Attempts 5 (0.6587, wall 20.529 s), 14 (0.6426, wall 17.780 s), 15 (0.5830, wall 23.702 s). Pushing per-step cost above the Class A level did not beat Class A. Within this class reward again tracks wall-clock loosely, and attempt 15's 23.7 s is the worst of the three.

**Class D — per-step cost driven down toward or below parity (psc ≈ 0.97–1.24), compute efficiency driven up (eff ≈ 0.76–0.97).** Attempts 8 (0.5444, psc 0.9674, eff 0.9679, wall 26.098 s), 11 (0.6639, psc 1.0166, eff 0.8424, wall 20.057 s), 13 (0.5590, psc 1.2404, eff 0.7642), 16 (0.5701, psc 1.1256, eff 0.8684), 4 (0.5792, psc 1.1656, eff 0.8832, wall 17.512 s). This is the largest class by record count and the most consistently disappointing. Attempt 8 achieved the best compute_efficiency ever measured, 0.9679, and the best per-step cost ratio ever measured, 0.9674 — and scored 0.5444, third-worst overall, on a 26.098 s wall clock. Attempt 4 shows the same lesson without the wall-clock confound: at 17.512 s, essentially the same end-to-end time as attempt 2's 17.453 s, its cheap-per-step profile (psc 1.1656) scored 0.5792 against attempt 2's 0.7155. Attempt 11 is the one respectable result in this class at 0.6639, still short of attempt 2.

**Class E — attempts that broke a conformance or perturbation check.** Attempts 9 and 12, detailed in section 3. Both have `task_pass` 0.0 and hold the two lowest rewards in the record, 0.5164 and 0.4962.

**Class F — attempts that did not survive to measurement.** Attempts 6 and 7, harbor_exception. No approach information can be recovered from them.

# 3. Checks that failed

Two named checks have ever failed, each in exactly one record. Neither is a recurring finding, so there is no check here whose repetition indicates the changes between attempts are irrelevant to it — but both are cheap to re-break and must be actively guarded against.

**C-API-SURFACE — attempt 9, one failure.** Verifier's reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions."* This dropped `rule_conformance` to 0.8571 and `task_pass` to 0.0, and attempt 9 scored 0.5164 despite `primary_target_reached` 1.0 and both perturbation units reaching. Concretely: the submission module must contain nothing at module level except imports, constant assignments, and permitted definitions (functions/classes). No bare expressions, no execution at import, no prints, no `if __name__ == "__main__"` side effects, no computed globals, no calls at module scope, no module-level seeding or device setup. Move all of that inside the required function bodies.

**C-PERTURBATION-REACHED — attempt 12, one failure.** Verifier's reason, verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* `conformance_fraction` fell to 0.5, `all_perturbations_held` to false, `task_pass` to 0.0, and attempt 12 scored 0.4962, the lowest reward in the record. The underlying unit failure is described in the perturbation section below.

Both failing attempts still received a reward. A failed check is not an automatic zero here — but the two failures are the two lowest scores measured, so the checks are worth roughly 0.05–0.20 of reward and must be held.

**Perturbation units.** Every measured record declares 2 perturbations, of exactly two kinds: one `held_out_variant` and one `ruleset`. Across the fourteen measured records that is fourteen `held_out_variant` units and fourteen `ruleset` units, twenty-eight in total.

- `ruleset` kind: fourteen of fourteen reached. No `ruleset` unit has ever failed any check.
- `held_out_variant` kind: thirteen of fourteen reached. One did not reach, in attempt 12, and it failed two checks: **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**.
- Aggregate: twenty-seven of twenty-eight units reached; the single aggregate failure is a `held_out_variant`.

The runs are not identified beyond their kind, so nothing can be said about which particular held-out run this was or whether it recurs as the same run in other records. What can be said is precise and sufficient: **the kind that fails is `held_out_variant`, and it fails by not hitting its target within its own budget** — both C-TARGET-REACHED and C-BUDGET-RESPECTED went down together, which is the signature of a configuration that is too slow to converge on the variant rather than one that diverges. Whatever attempt 12 did to shave its primary wall clock to 16.781 s — the shortest ever measured — plausibly left the held-out variant without enough budget to reach threshold. Do not tune the primary run so tight that the variant run starves.

# 4. Ruled-out directions

**Maximising compute_efficiency / minimising per_step_cost_ratio as the objective.** Ruled out by direct measurement. Attempt 8 reached compute_efficiency 0.9679 and per_step_cost_ratio 0.9674, both the best values ever recorded on those axes, and scored 0.5444 — worse than nine other measured attempts and 0.171 below attempt 2. The whole of Class D (attempts 4, 8, 11, 13, 16) sits at eff ≥ 0.76 and psc ≤ 1.25, and its best member (11, 0.6639) still loses to attempt 2. These metrics are reported but they are not the reward; driving them up has cost reward every time except once, and even that once did not win.

**Trading wall-clock for cheaper steps.** Ruled out. Attempt 8's low psc came with a 26.098 s wall clock, the longest measured and the third-worst reward. Attempt 15 at 23.702 s scored 0.5830. Every attempt above 0.64 finished in 17.4–20.6 s. Long runs do not pay, whatever they buy per step.

**Raising per-step cost above the ~1.52 level.** Ruled out as a direction on its own. Class C at psc ≈ 1.63 produced 0.6587, 0.6426 and 0.5830 — none beat attempt 2's 0.7155 at psc 1.5175, including attempt 14 which matched attempt 2's short wall clock (17.780 s vs 17.453 s) and still landed 0.073 lower. Going further up this axis is not where the remaining reward is.

**Shaving the primary wall clock below ~17 s.** Ruled out by attempt 12. At 16.781 s, the shortest primary run measured, the `held_out_variant` perturbation failed both C-TARGET-REACHED and C-BUDGET-RESPECTED, C-PERTURBATION-REACHED failed, task_pass went to 0.0, and the reward was the lowest in the record at 0.4962. The floor on useful speed is set by the held-out variant, not by the primary run.

**Any module-level execution in the submission.** Ruled out by C-API-SURFACE on attempt 9. Cost: task_pass 0.0 and rule_conformance 0.8571 on a run that otherwise reached its primary target and held both perturbations.

**Treating attempts 6 and 7 as evidence about anything.** They are harbor_exceptions with no measurement. Whatever they contained is unknown and unscored; do not assume their approach was bad, and do not assume it was good.

# 5. Open leads

**Lead 1 — reconstruct the attempt-2 operating point exactly, and treat it as the target signature.** The single highest reward, 0.7155, has a very specific fingerprint: wall_clock 17.453 s, per_step_cost_ratio 1.5175, compute_efficiency 0.6205, all checks green, both perturbations reached. Attempt 1 sits 0.05 away at almost the same fingerprint (17.426 s, psc 1.5134, eff 0.5488, reward 0.6694). Aim the next submission at that regime deliberately: a moderately expensive per-step configuration — roughly 1.5× the reference per-step cost, not 1.0× and not 1.6× — with the whole run landing in the 17.4–17.6 s band. Do not optimise compute_efficiency; let it fall where it falls around 0.55–0.65.

**Lead 2 — resolve the residual between attempts 1 and 2.** These two are nearly indistinguishable on every exposed metric (wall clock differs by 0.027 s, psc by 0.004, eff by 0.072) yet differ by 0.046 in reward. That gap is not explained by any reported quantity, which means reward carries a quality/generalisation term the exposed metrics do not expose. Practically this means: after hitting the Class A cost regime, the remaining lever is model quality on the held-out evaluation, not timing. Spend the tuning effort there — schedule shape, regularisation, effective batch/step count within the same time budget — rather than on the cost ratios.

**Lead 3 — the wall-clock gradient inside a fixed cost regime is real and is worth about 0.04–0.12.** Class A (17.4 s) scored 0.6694 and 0.7155; Class B, at the same psc ≈ 1.52, scored 0.6279 at 20.300 s and 0.5983 at 20.150 s. If a Class A configuration currently lands near 20 s, pulling it back toward 17.5 s without changing per-step cost is the highest-confidence single improvement available. The hard floor is attempt 12's failure at 16.781 s — stay above roughly 17 s so the `held_out_variant` run keeps enough budget to reach its threshold.

**Lead 4 — verify the two named checks before optimising anything.** Before tuning, confirm (a) the module has no statements at module level beyond imports, constants and permitted definitions, closing C-API-SURFACE; and (b) whatever budget/step-count logic is used, it is expressed so that the `held_out_variant` run gets the same convergence headroom the primary run gets, closing C-TARGET-REACHED / C-BUDGET-RESPECTED and therefore C-PERTURBATION-REACHED. Both failures cost more reward than any tuning gain observed so far.

**Lead 5 — attempt 11 is the one anomaly worth a second look.** It scored 0.6639, fourth-best overall, from inside Class D (psc 1.0166, eff 0.8424) at a 20.057 s wall clock. Every other cheap-per-step attempt scored 0.54–0.58. If attempt 11's quality-side choices can be identified and grafted onto the Class A cost regime and the 17.5 s wall clock, that is the most plausible route past 0.7155. This is speculative — the code is not available — but the measured contrast between attempt 11 and its class-mates is large enough to be worth probing.

**Call: exploit.** The approach that scored highest, Class A at attempt 2's operating point, has not been revisited since attempt 2, and the twelve measured attempts since have all wandered into Class C, Class D or check failures and all scored lower. This is not a case of a scoring approach having stopped improving; it is a case of a scoring approach having been abandoned early and never returned to. The next attempt should reconstruct the attempt-2 regime — psc ≈ 1.52, wall ≈ 17.45 s, both checks held, both perturbations reached — and then vary only the quality-side choices that Lead 2 identifies. Do not spend the attempt pushing compute_efficiency or per-step cost; both axes have been explored across five records and neither has produced a win.
