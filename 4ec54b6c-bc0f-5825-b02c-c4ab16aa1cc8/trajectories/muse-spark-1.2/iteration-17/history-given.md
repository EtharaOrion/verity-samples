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

    All 14 attempts since have scored lower than it.
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
  18       0.5755   1.000             2 of 2         yes             21                

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
  12 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 18 -- reward 0.5755, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (9, 17). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Eighteen submissions were graded. Sixteen produced a measurement; two did not. Listed worst to best by `reward`:

| Attempt | reward | note |
|---|---|---|
| 12 | 0.4962 | failed C-PERTURBATION-REACHED; task_pass 0.0 |
| 9 | 0.5164 | failed C-API-SURFACE; task_pass 0.0 |
| 17 | 0.5274 | failed C-API-SURFACE; task_pass 0.0 |
| 8 | 0.5444 | clean; wall 26.098 s, per_step_cost_ratio 0.9674 |
| 13 | 0.5590 | clean |
| 16 | 0.5701 | clean |
| 18 | 0.5755 | clean |
| 4 | 0.5792 | clean; compute_efficiency 0.8832 |
| 15 | 0.5830 | clean |
| 10 | 0.5983 | clean |
| 3 | 0.6279 | clean |
| 14 | 0.6426 | clean |
| 5 | 0.6587 | clean |
| 11 | 0.6639 | clean |
| 1 | 0.6694 | clean; first measured attempt |
| 2 | **0.7155** | clean; best |

**Attempt 2 holds the highest reward, 0.7155, and it is the one to beat.** Its operating point: wall_clock_sec 17.4531, qualifying_budget 17.4531, per_step_cost_ratio 1.5175, compute_efficiency 0.6205, conformance_fraction 1.0, rule_conformance 1.0, validity 1.0, task_pass 1.0, primary_target_reached 1.0, both declared perturbations held, red_line_crossed 0.0.

Attempts 6 and 7 have `measurement_status: harbor_exception`. **They produced no measurement at all — no reward, no efficiency, no perturbation outcomes. They must not be read as scores of zero**; nothing is known about the quality of what they contained, only that the harness did not complete a measurement on them.

Every attempt after 2 that carries a reward is marked `worse_than_an_earlier_attempt`, and that is what the numbers say: attempts 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 and 18 all scored **below** the 0.7155 set at attempt 2. This is a run of fifteen consecutive graded submissions that regressed against the standing best. No attempt scored zero (`zero_reason_code` is 0 in every measured record) and no attempt crossed a red line (`red_line_crossed` 0.0 throughout, `validity` 1.0 throughout).

## 2. Approach classes tried

The measured terms do not carry source code, so the classes below are grouped by the cost/efficiency signature each submission produced. Distinct approaches, not distinct records:

**A. Baseline-cost configuration, ~17.4 s wall clock, per-step cost ratio ~1.51.** Attempts 1 (0.6694) and 2 (0.7155). Nearly identical cost profiles (wall 17.4264 vs 17.4531; per_step 1.5134 vs 1.5175), but compute_efficiency rose 0.5488 → 0.6205 and reward rose with it. This is the only class that ever exceeded 0.70, and the only transition in the whole record that improved on the standing best.

**B. Same per-step cost, longer run (~20–20.5 s).** Attempts 3 (0.6279, per_step 1.5225, wall 20.3003), 10 (0.5983, per_step 1.5152, wall 20.1500). Same per-step economics as class A but ~3 s more wall clock; both landed 0.09–0.12 below attempt 2.

**C. Raised per-step cost (per_step_cost_ratio 1.58–1.63).** Attempts 5 (0.6587, 1.6262, wall 20.5293), 14 (0.6426, 1.6303, wall 17.7803), 15 (0.5830, 1.6313, wall 23.7018), 18 (0.5755, 1.5846, wall 20.6261). Best of these, attempt 14, kept wall clock near the class-A value (17.78 s) and got closest to attempt 2; the two that ran ≥20.5 s fell furthest.

**D. Cheap-step / high-compute-efficiency configuration (per_step_cost_ratio 0.97–1.24, compute_efficiency 0.76–0.97).** Attempts 4 (0.5792, per_step 1.1656, ceff 0.8832), 8 (0.5444, per_step 0.9674, ceff 0.9679, wall 26.0978), 11 (0.6639, per_step 1.0166, ceff 0.8424, wall 20.0571), 13 (0.5590, per_step 1.2404, ceff 0.7642), 16 (0.5701, per_step 1.1256, ceff 0.8684). This class drove the reported efficiency metrics to their best values in the whole record and produced *lower* reward across the board. Attempt 8 is the extreme case: the cheapest steps and the highest compute_efficiency of any submission, and the fourth-worst reward.

**E. Submissions carrying module-level statements.** Attempts 9 (0.5164) and 17 (0.5274). Both failed C-API-SURFACE, both scored task_pass 0.0 and rule_conformance 0.8571 (6 of 7 rules). They sat in different cost classes from each other (9: per_step 1.4988, ceff 0.6647, wall 17.12; 17: per_step 1.2123, ceff 0.8228, wall 23.58), so this is a file-structure property that cut across two different training configurations.

**F. Short-budget submission that lost a held-out perturbation.** Attempt 12 (0.4962), the shortest run measured (wall 16.7808) and the lowest reward. `conformance_fraction` 0.5, task_pass 0.0.

**G. Two submissions that never reached measurement.** Attempts 6 and 7, harbor_exception. No cost, efficiency or perturbation data exists for them; nothing can be inferred about the approach they encoded.

## 3. Checks that failed

**C-API-SURFACE — "module-level statements outside imports, constants, and permitted definitions."** Failed twice: attempt 9 and attempt 17. **This is the finding that matters most in the record.** The two attempts differed substantially in their training configuration — per_step_cost_ratio 1.4988 vs 1.2123, compute_efficiency 0.6647 vs 0.8228, wall clock 17.12 s vs 23.58 s — and the check failed identically in both. **Whatever was changed between those two attempts is not what causes this check to fail.** The cause is executable code sitting at module scope in the submitted file. Both times it dropped rule_conformance from 1.0 to 0.8571 and forced task_pass to 0.0, and both times the reward landed in the bottom three of the record. The fix is structural, not numerical: the module must contain only imports, constant assignments, and permitted definitions, with all work moved inside the required function/class bodies.

**C-PERTURBATION-REACHED — "1 of 2 declared perturbations reached their own threshold inside their own budget."** Failed once, at attempt 12. It set `conformance_fraction` to 0.5 and task_pass to 0.0, and the record carries the lowest reward measured, 0.4962.

**C-TARGET-REACHED and C-BUDGET-RESPECTED.** Both failed once, on the held-out perturbation unit inside attempt 12. They are the sub-checks underneath the C-PERTURBATION-REACHED failure above: that unit neither hit its target nor stayed inside its own budget.

No other check failed in any record. Notably, the primary run passed every time a measurement existed: `primary_target_reached` is 1.0 and `validity` is 1.0 in all sixteen measured records, including 9, 12 and 17.

## 4. Ruled-out directions

**Optimising for cheaper steps / higher reported compute_efficiency (class D).** Ruled out because it is anti-correlated with reward in every instance. Five submissions pushed per_step_cost_ratio from ~1.52 down to 0.97–1.24 and compute_efficiency up to 0.76–0.97; their rewards were 0.5444, 0.5590, 0.5701, 0.5792 and 0.6639 — all below attempt 2's 0.7155, and the single most aggressive one (attempt 8, per_step 0.9674, compute_efficiency 0.9679) produced 0.5444. Making each step cheaper is buying an efficiency number the grade does not pay for while giving up whatever the reward actually measures.

**Extending wall clock past roughly 20 s.** Every submission at ≥20.0 s scored between 0.5444 and 0.6639 (attempts 3, 5, 8, 10, 11, 13, 15, 16, 18); the two best results in the record, 0.6694 and 0.7155, both ran at 17.43–17.45 s. The longest run in the record, attempt 8 at 26.0978 s, is the fourth-worst reward. `qualifying_budget` equals `wall_clock_sec` in every measured record, so time spent is directly the budget consumed.

**Leaving any executable statement at module scope.** Ruled out by two independent C-API-SURFACE failures (attempts 9, 17), each of which zeroed task_pass and cost roughly 0.15–0.20 of reward relative to the standing best regardless of how good the underlying configuration was.

**Whatever attempt 12 did to compress the run to 16.78 s.** Ruled out: it produced the shortest budget in the record and the only perturbation failure, with the held-out variant missing both C-TARGET-REACHED and C-BUDGET-RESPECTED. Cutting cost below the attempt-2 operating point breaks the held-out unit before it improves anything.

**Re-submitting anything resembling attempts 6 or 7.** Not ruled out on merit — they produced no measurement, so there is no evidence either way — but there is no signal to build on, and reproducing them yields no reward information.

## 5. Open leads

**Perturbation picture, by kind and in aggregate.** Across the sixteen measured records, 2 perturbations were declared each time: 32 held-out units in total, of which 31 reached their threshold. Units of kind `ruleset`: 16 declared, 16 reached, zero failures — this kind has never once been a problem. Units of kind `held_out_variant`: 16 declared, 15 reached, 1 failure, and that failure was on C-TARGET-REACHED and C-BUDGET-RESPECTED. The held-out-variant kind is the only kind that has ever failed, and it fails on target-reached and budget-respected together. The runs are not identified individually, so nothing links a unit in one record to a unit in another; the statement that holds is about the kind, not about any particular run. Any change that shortens the budget or narrows the margin on the primary target should be checked against the held-out-variant kind specifically, since that is where the single failure occurred.

**Lead 1 — rebuild the attempt-2 operating point exactly, then hold it.** Target wall_clock_sec ≈ 17.45 s, per_step_cost_ratio ≈ 1.52, compute_efficiency ≈ 0.62. Attempts 1 and 2 are the only two submissions in that box and they are ranks 2 and 1. Everything since has drifted out of it. Re-establishing it should reproduce ~0.67–0.72 before any further change is attempted.

**Lead 2 — repeat the attempt-1 → attempt-2 move, which is the only improvement ever measured.** Between them, cost was held essentially constant (wall +0.027 s, per_step +0.004) while compute_efficiency rose 0.5488 → 0.6205 and reward rose 0.6694 → 0.7155. The productive axis is *more useful work per unit of a fixed budget*, not *less budget*. Push compute_efficiency above 0.62 while pinning wall clock at ~17.4–17.5 s and per_step_cost_ratio at ~1.52. Note the sharp contrast with class D, which reached compute_efficiency 0.84–0.97 by cutting per-step cost and lost reward; the distinction to preserve is that the cost profile stays put.

**Lead 3 — the narrow region just above attempt 2 in per-step cost, at short wall clock.** Attempt 14 raised per_step_cost_ratio to 1.6303 while keeping wall clock at 17.7803 and scored 0.6426, the best result outside classes A and D. The other three attempts in that cost class all ran ≥20.5 s and scored 0.5755–0.6587. This suggests a modest per-step increase is survivable if and only if wall clock stays near 17.5–17.8 s; it is worth one probe, but only after Lead 1 has re-anchored the baseline.

**Lead 4 — guard C-API-SURFACE mechanically before submitting.** Since the stub is pristine each time and the check has already failed twice from unrelated configurations, treat it as a hard pre-submission invariant: scan the top level of the file and confirm every statement is an import, a constant assignment, or a permitted `def`/`class`. No guard clause, no `if __name__` block, no demo call, no logging setup, no computed module-level table built by a loop. This costs nothing and removes the single most repeated failure in the record.

**Lead 5 — declare the two perturbations and verify the held-out-variant unit has margin.** Keep `perturbations_declared` at 2 and do not tighten the budget below the attempt-2 value; the one time a submission came in under 17 s, the held-out-variant unit missed both its target and its budget.

**Caution on causal reading.** The measured terms report cost and efficiency but not the underlying task quality that the reward presumably also weighs. The relationships above are patterns across sixteen points, not a mechanism the data proves. What the data does establish unambiguously is: attempt 2's exact operating point produced the highest reward; the cheap-step direction produced consistently lower reward; and the two named checks cost task_pass outright when they fire.

**Call: exploit.** The best-scoring approach — class A, the ~17.45 s / per_step ~1.52 configuration of attempt 2 at 0.7155 — has not been revisited since attempt 2, and the fifteen graded submissions since then all moved away from it and all scored lower. This is not a case of a scoring approach that has stopped improving; it is a case of a scoring approach that was abandoned. Restore it, apply the C-API-SURFACE guard, and then push compute_efficiency upward at fixed cost as in Lead 2. Do not re-run class D: five submissions have now confirmed that cutting per-step cost lowers reward, and running it again without changing that premise would be neither exploration nor exploitation.
