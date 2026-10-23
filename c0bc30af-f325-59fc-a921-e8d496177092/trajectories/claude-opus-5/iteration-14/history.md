# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.9128, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All nine attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4        0.8719   1.000             2 of 2         yes             50                
  5 *      0.9128   1.000             2 of 2         yes             25                
  6        0.5615   0.857             2 of 2         yes             204               
  7        0.0000   1.000             0 of 2         no              --                
  8        0.7551   1.000             2 of 2         yes             78                
  9        0.0000   1.000             0 of 2         no              --                
  10       0.0000   1.000             0 of 2         no              --                
  11       0.8980   1.000             2 of 2         yes             25                
  12       0.0000   1.000             0 of 2         no              --                
  13       0.8451   1.000             2 of 2         yes             71                
  14       0.6955   1.000             2 of 2         yes             100               

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
  8 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 4 -- reward 0.8719, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 12 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 3 of your last 4 attempts
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same seed run has now failed on 3 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 13 -- reward 0.8451, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 71
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 14 -- reward 0.6955, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 100
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 5 attempts (3, 7, 9, 10, 12). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 5 attempts (3, 7, 9, 10, 12). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 5 attempts (3, 7, 9, 10, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All fourteen records carry `measurement_status: "measured"`, so every one has a real reward. Five of them are measured zeros (reward exactly 0.0000 with `zero_reason_code: 4`), not absent measurements. Listed worst to best by reward:

- **Attempt 3 — reward 0.0000.** No target reached; wall clock 1692.52 s; `qualifying_budget` not measured.
- **Attempt 7 — reward 0.0000.** Same failure signature; wall clock 1692.21 s.
- **Attempt 9 — reward 0.0000.** Same failure signature; wall clock 1692.97 s.
- **Attempt 10 — reward 0.0000.** Same failure signature; wall clock 1690.96 s.
- **Attempt 12 — reward 0.0000.** Same failure signature; wall clock 1690.45 s.
- **Attempt 6 — reward 0.5615.** Target reached and both perturbations held, but `C-API-SURFACE` failed; `rule_conformance` 0.8571, `task_pass` 0.0; wall clock 204.09 s.
- **Attempt 14 — reward 0.6955.** Fully clean (no failed checks), wall clock 99.74 s.
- **Attempt 8 — reward 0.7551.** Fully clean, `qualifying_budget` 78.14 s but wall clock 151.50 s — the only record where those two numbers differ.
- **Attempt 1 — reward 0.7684.** `C-API-SURFACE` failed; `rule_conformance` 0.8571, `task_pass` 0.0; wall clock 25.46 s.
- **Attempt 2 — reward 0.8385.** Fully clean, wall clock 73.62 s.
- **Attempt 13 — reward 0.8451.** Fully clean, wall clock 71.31 s.
- **Attempt 4 — reward 0.8719.** Fully clean, wall clock 50.03 s, `compute_efficiency` 1.0.
- **Attempt 11 — reward 0.8980.** Fully clean, wall clock 25.35 s.
- **Attempt 5 — reward 0.9128.** Fully clean, wall clock 25.34 s, `per_step_cost_ratio` 0.9887.

**Attempt 5 holds the highest reward at 0.9128. That is the score to beat.**

Direction of travel must not be dressed up: attempt 5 was the last improvement. Every record after it is marked `worse_than_an_earlier_attempt` — attempt 6 (0.5615), attempt 7 (0.0000), attempt 8 (0.7551), attempt 9 (0.0000), attempt 10 (0.0000), attempt 11 (0.8980), attempt 12 (0.0000), attempt 13 (0.8451), attempt 14 (0.6955). Attempt 11 at 0.8980 is the closest anything has come since, and it is still a regression against 0.9128. Only attempts 2, 4 and 5 were ever marked `better_than_every_earlier_attempt`; attempt 1 was the `first_measured_attempt`.

`validity` is 1.0 and `red_line_crossed` is 0.0 on every single record, including the zeros. Nothing has ever been ruled invalid or tripped a red line, so no effort should go into that.

# 2. Approach classes tried

The code from earlier attempts is not carried forward, so these classes are grouped by their measured signature — budget consumed, conformance, and whether the target was reached. Records with identical signatures are one entry.

**Class A — fast conforming solve, ~25 s (attempts 5, 11; also attempt 1 in its timing but not its conformance).** Qualifying budget 25.34 s and 25.35 s, both fully clean, rewards 0.9128 and 0.8980. `compute_efficiency` for these was only 0.7728 and 0.7043 and `per_step_cost_ratio` 0.9887 and 1.0502 — i.e. these are *not* the cheapest-per-step runs, yet they score highest. This is the winning class and the only one that has produced a reward above 0.89.

**Class B — mid-budget conforming solve, ~50–100 s (attempts 4, 13, 2, 14).** All fully clean, all reaching target with both perturbations holding. Rewards fall monotonically as budget rises: 50.03 s → 0.8719, 71.31 s → 0.8451, 73.62 s → 0.8385, 99.74 s → 0.6955. Attempt 4 achieved `compute_efficiency` 1.0 and `per_step_cost_ratio` 0.7115 — the best per-step economy on record — and still scored 0.0409 below attempt 5, which had worse per-step economy but half the wall clock. That comparison is the single most informative pair in the whole set: **per-step economy does not buy reward; elapsed budget does.**

**Class C — conforming solve with wall clock exceeding the qualifying budget (attempt 8).** `qualifying_budget` 78.14 s against `wall_clock_sec` 151.50 s, fully clean, reward 0.7551. Attempt 2 had a near-identical qualifying budget (73.62 s) and scored 0.8385. The 0.0834 gap between them, with the same conformance and the same perturbation outcomes, is best explained by the extra ~73 s of wall clock beyond the qualifying row. Work that continues after the qualifying row appears to be charged.

**Class D — conforming solve that leaves module-level statements in the file (attempts 1, 6).** Both reached the primary target and both had all perturbations hold, so the learning side worked; both were docked by `C-API-SURFACE` to `rule_conformance` 0.8571 and `task_pass` 0.0. Attempt 1 at 25.46 s scored 0.7684 where the equivalently fast clean attempt 5 scored 0.9128 — the conformance penalty is worth roughly 0.14 of reward. Attempt 6 combined the same penalty with a 204.09 s budget and landed at 0.5615, the worst non-zero result.

**Class E — long-running approach that never crosses the threshold (attempts 3, 7, 9, 10, 12).** Five records, wall clock 1690.45–1692.97 s in every case, a spread of about 2.5 seconds across five runs. That tight clustering says these runs were cut off at a hard ceiling rather than converging and failing on merit. All five score 0.0000 with `zero_reason_code: 4`, `conformance_fraction` 0.0, `primary_target_reached` 0.0 and `qualifying_budget` not measured. Notably their `compute_efficiency` readings are the highest in the set (1.0, 1.0, 1.0, 0.9833, 0.9762) and `per_step_cost_ratio` the lowest (0.7757–0.8901): these were the cheapest-per-step runs and they scored nothing. This class has now been re-run five times with the same outcome.

# 3. Checks that failed

**`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction". Failed 5 times** (attempts 3, 7, 9, 10, 12), and additionally recorded against every held-out run in those same five attempts. In each case the run burned ~1690 s of wall clock. Whatever was changed between attempts 3, 7, 9, 10 and 12 is not what is causing this check to fail — five separate submissions produced the identical triple failure with the identical time signature.

**`C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists". Failed 5 times**, always in the same five records and always alongside `C-TARGET-REACHED`. This is a consequence, not an independent defect: with no row crossing the threshold there is no qualifying row to place against the budget. Fixing `C-TARGET-REACHED` should clear it.

**`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed 5 times**, in those same five records. It has never failed partially — never 1 of 2 — which reinforces that the primary and held-out runs fail together as one systemic problem rather than a robustness gap.

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions". Failed 2 times** (attempts 1 and 6). This one is separable from the learning behaviour: both those attempts reached the primary target and both held all perturbations. Whatever was changed between attempt 1 and attempt 6 is not what is causing this check — the same module-level-statement violation survived the change. The fix is structural and mechanical: everything that executes at import time must be moved inside a function or method; only imports, constant assignments, and permitted definitions may sit at module level. Nine records have passed this check, so it is demonstrably satisfiable.

**Perturbation outcomes.** Every attempt declared 2 perturbations, one of kind `held_out_variant` and one of kind `seed`. Across 14 attempts that is 28 held-out runs: **18 reached their threshold and 10 did not.** By kind: `held_out_variant` reached in 9 of 14, failed in 5; `seed` reached in 9 of 14, failed in 5. The two kinds have identical records. Every failure of either kind was on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, and every failure occurred inside one of the five ~1690 s zero-reward attempts. In all nine attempts that reached the primary target, both kinds held with no failed checks — `all_perturbations_held` is true for every scoring record. There is no evidence of a kind-specific weakness: neither seed variation nor held-out variation has ever broken an otherwise-working submission. The runs are not identified across records and no claim is made that any particular run recurs.

# 4. Ruled-out directions

**The long-running approach of class E.** Ruled out. Five submissions, all terminating at ~1690 s, all scoring 0.0000, all failing the same three checks. Whatever it is doing, it does not reach the threshold before it runs out of time, and re-running it without changing the thing that makes it exceed the ceiling has produced nothing five times over. Repeating it again would be neither exploring nor exploiting — and it is worth naming plainly that earlier work did repeat it, four times after its first zero.

**Optimising `compute_efficiency` or `per_step_cost_ratio` as the objective.** Ruled out by direct counter-evidence. The five zero-reward records hold the best `compute_efficiency` figures in the set (up to 1.0) and the lowest per-step costs (down to 0.7757). Attempt 4 posted `compute_efficiency` 1.0 and `per_step_cost_ratio` 0.7115 and scored 0.8719, below attempt 5's 0.9128 which had `compute_efficiency` 0.7728 and `per_step_cost_ratio` 0.9887. Making each step cheaper while taking more of them loses reward.

**Budgets above ~75 s in a conforming run.** Ruled out as a route to the top score. Class B shows a clean monotone decay with elapsed budget: 25 s ≈ 0.90–0.91, 50 s ≈ 0.87, 71–74 s ≈ 0.84–0.85, 100 s ≈ 0.70, 204 s ≈ 0.56 (that last also carrying the conformance penalty). Nothing above 50 s has ever beaten 0.8719.

**Leaving executable statements at module scope.** Ruled out. It cost attempt 1 roughly 0.14 of reward against the otherwise comparable attempt 5, forces `task_pass` to 0.0 and `rule_conformance` to 0.8571, and it delivers nothing in return — both attempts that carried it had already solved the task.

**Chasing robustness against seed or held-out variation as a separate concern.** Ruled out on evidence: `all_perturbations_held` is true in every attempt that reached the primary target, and the two perturbation kinds have identical 9-of-14 records. Perturbations have never been the marginal failure. Effort spent hardening against them is effort not spent on budget.

**Worrying about validity or red lines.** Ruled out: `validity` 1.0 and `red_line_crossed` 0.0 on all fourteen records, zeros included.

# 5. Open leads

**Rebuild the ~25 s conforming solve first and confirm it lands near 0.9128.** This is the reference point and the next attempt starts from a pristine stub with no memory of it. Its signature: qualifying budget ≈ 25.3 s, wall clock equal to the qualifying budget, no failed checks, `primary_target_reached` 1.0, `task_pass` 1.0, `rule_conformance` 1.0, both perturbations holding, `per_step_cost_ratio` near 1.0 and `compute_efficiency` around 0.77. Do not chase a lower per-step cost while rebuilding it — attempts 4 and 5 show that trade runs the wrong way.

**Push the qualifying budget below 25 s.** The three fast records cluster at 25.34, 25.35 and 25.46 s and the two clean ones score 0.9128 and 0.8980. Nothing has ever been measured below 25 s. The reward-versus-budget curve through 25 s / 50 s / 71 s / 100 s is steep and consistent, so the first genuinely sub-25-second conforming solve is the most likely thing to beat 0.9128. Concretely: reach the threshold with fewer steps, stop the moment an evaluation row crosses in the declared direction, and do not train past it.

**Stop all work at the qualifying row.** Attempt 8 is the evidence: its qualifying budget of 78.14 s was close to attempt 2's 73.62 s, but its wall clock ran to 151.50 s and it scored 0.7551 against attempt 2's 0.8385. Every other record has `wall_clock_sec` identical to `qualifying_budget`. Ensure no evaluation, checkpointing, extra epochs, or cleanup continues after the crossing row is produced.

**Enforce the API surface mechanically before submitting.** Nothing may execute at module import time. Only imports, constant assignments, and permitted definitions at module level; every call, loop, print, seed-setting statement, device selection, data load and training invocation goes inside a function or under the harness's entry point. This has cost two attempts and is fully within control.

**Explain the ~1690 s ceiling only far enough to avoid it.** Five runs stopped within 2.5 s of each other at that figure, which reads as a hard cutoff rather than a converged failure. There is no need to diagnose that approach further; what matters is that the next submission's design cannot drift into it. A safe pattern: keep the training loop short and bounded by construction, and make the threshold-crossing evaluation happen early and often rather than once at the end.

**Watch the 0.8980-versus-0.9128 gap.** Attempts 5 and 11 had budgets within 0.01 s of each other (25.34 vs 25.35 s), identical conformance and identical perturbation outcomes, yet differ by 0.0148 in reward. Their `compute_efficiency` (0.7728 vs 0.7043) and `per_step_cost_ratio` (0.9887 vs 1.0502) differ, so at fixed budget the cheaper-per-step of the two won. That suggests per-step cost is a genuine but strictly second-order term: worth taking once the budget is already minimal, never worth trading budget for.

**Call: exploit.** The fast conforming solve of class A has scored twice, holds the top result at 0.9128, and has a clear untested margin below 25 s. The zero-scoring long-run class has been repeated five times without changing what makes it score zero and must not be repeated again. Rebuild the 25 s clean solve, keep the API surface clean, terminate at the qualifying row, and drive the budget down from there.
