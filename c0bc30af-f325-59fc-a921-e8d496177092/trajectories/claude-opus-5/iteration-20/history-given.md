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

    All 14 attempts since have scored lower than it.
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
  15       0.0000   1.000             0 of 2         no              --                
  16       0.0000   1.000             0 of 2         no              --                
  17       0.7919   1.000             2 of 2         yes             74                
  18       0.8794   1.000             2 of 2         yes             49                
  19       0.9121   1.000             2 of 2         yes             46                

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
  14 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 17 -- reward 0.7919, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 18 -- reward 0.8794, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 49
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.9121, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 46
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 7 attempts (3, 7, 9, 10, 12, 15, 16). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 7 attempts (3, 7, 9, 10, 12, 15, 16). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 7 attempts (3, 7, 9, 10, 12, 15, 16). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All nineteen graded records carry `measurement_status: "measured"`, so every one has a reward. None is missing a measurement; the seven records at 0.0000 are genuine measured zeros (`zero_reason_code: 4`), not absent measurements. `validity` is 1.0 and `red_line_crossed` is 0.0 in every record — nothing was ever invalidated or tripped a red line.

Ordered worst to best by reward:

| Reward | Attempt(s) | Notes |
|---|---|---|
| 0.0000 | 3, 7, 9, 10, 12, 15, 16 | seven attempts, all identical failure signature; wall clock 1690.4–1693.0 s; `qualifying_budget` "not-measured" |
| 0.5615 | 6 | `C-API-SURFACE` failed; `rule_conformance` 0.8571; `task_pass` 0; budget 204.09 s |
| 0.6955 | 14 | clean checks; budget 99.74 s |
| 0.7551 | 8 | clean checks; qualifying budget 78.14 s but total wall clock 151.50 s |
| 0.7684 | 1 | `C-API-SURFACE` failed; `rule_conformance` 0.8571; `task_pass` 0; budget 25.46 s |
| 0.7919 | 17 | clean checks; budget 73.80 s |
| 0.8385 | 2 | clean checks; budget 73.62 s |
| 0.8451 | 13 | clean checks; budget 71.31 s |
| 0.8719 | 4 | clean checks; budget 50.03 s; `compute_efficiency` 1.0 |
| 0.8794 | 18 | clean checks; budget 49.33 s |
| 0.8980 | 11 | clean checks; budget 25.35 s |
| 0.9121 | 19 | clean checks; budget 45.81 s; `compute_efficiency` 0.9345 |
| 0.9128 | 5 | clean checks; budget 25.34 s; `compute_efficiency` 0.7728 |

**Attempt 5 holds the highest reward at 0.9128, and it is the one to beat.** Attempt 19 at 0.9121 is effectively tied with it; attempt 11 at 0.8980 is third.

Direction of travel, stated plainly rather than softened: attempts 1, 2, 4 and 5 each improved on everything before them, and after attempt 5 **no attempt has beaten it**. Every record from 6 onward is marked `worse_than_an_earlier_attempt`. Attempt 6 (0.5615) was worse than attempt 5. Attempt 8 (0.7551) was worse. Attempt 11 (0.8980), 13 (0.8451), 14 (0.6955), 17 (0.7919), 18 (0.8794) and 19 (0.9121) were all worse than attempt 5. Attempts 7, 9, 10, 12, 15 and 16 scored 0.0000 outright. The last fourteen graded attempts produced no new high-water mark.

What the numbers say about how reward is earned. Among the twelve attempts that reached the primary target with full rule conformance, reward tracks the qualifying budget closely: ~25 s budgets returned 0.8980–0.9128, ~46–50 s returned 0.8719–0.9121, ~71–79 s returned 0.7551–0.8451, ~100 s returned 0.6955, ~204 s returned 0.5615. Speed to target is the dominant lever. It is not the only one: attempts 5 and 11 had near-identical budgets (25.34 s vs 25.35 s) but rewards of 0.9128 and 0.8980, differing in `compute_efficiency` (0.7728 vs 0.7043) and `per_step_cost_ratio` (0.9887 vs 1.0502); and attempt 19 at 45.81 s nearly matched attempt 5 at 25.34 s while carrying a much better `compute_efficiency` (0.9345) and `per_step_cost_ratio` (0.7669). So budget, compute efficiency and per-step cost all contribute, and conformance gates the whole thing.

# 2. Approach classes tried

The next attempt starts from a pristine stub and will not see any earlier source, so these classes are described by their measured signature; the underlying code is not carried forward and is not recoverable from the terms supplied.

**Class A — fast conformant convergence, ~25 s qualifying budget.** Attempts 5 (0.9128) and 11 (0.8980). Target reached, both perturbation runs held, all checks clean, `per_step_cost_ratio` near or slightly above 1.0 (0.9887 and 1.0502), `compute_efficiency` in the 0.70–0.77 range. This class produced the top and third-best scores. Its weakness is that per-step cost is not reduced — it wins on wall clock alone.

**Class B — moderately fast conformant convergence with low per-step cost, ~45–50 s budget.** Attempts 19 (0.9121), 18 (0.8794), 4 (0.8719). All checks clean, both perturbation runs held. Attempt 19 combined a 45.81 s budget with `compute_efficiency` 0.9345 and `per_step_cost_ratio` 0.7669 and came within 0.0007 of the best score. Attempt 4 reached `compute_efficiency` 1.0 — the maximum observed — with `per_step_cost_ratio` 0.7115, but a 50.03 s budget held it to 0.8719. This class is the cheapest-per-step family that still scores well.

**Class C — mid-budget conformant convergence, ~70–100 s.** Attempts 13 (0.8451), 2 (0.8385), 17 (0.7919), 8 (0.7551), 14 (0.6955). All clean on checks with both perturbation runs holding, but the longer budget costs 0.06–0.22 reward relative to Class A. Attempt 8 is distinctive: its qualifying budget was 78.14 s yet its total wall clock was 151.50 s — the only record where those two diverge — and it scored 0.7551, below attempt 2 which reached target at a comparable 73.62 s and scored 0.8385. Work performed after the qualifying row appears not to be free.

**Class D — target reached but module-level statements present.** Attempts 1 (0.7684) and 6 (0.5615). Both reached the primary target and both held all perturbation runs, but both failed `C-API-SURFACE`, which drove `rule_conformance` to 0.8571 (6 of 7) and `task_pass` to 0. Attempt 1 reached target in 25.46 s — a Class A budget — and still scored only 0.7684 against attempt 5's 0.9128 at 25.34 s. The conformance failure alone costs roughly 0.14 reward at equal speed. Attempt 6 compounded it with a 204.09 s budget and `per_step_cost_ratio` 1.3778, giving the worst non-zero score on record.

**Class E — non-converging runs that exhaust the wall clock.** Attempts 3, 7, 9, 10, 12, 15, 16 — seven of nineteen, all 0.0000. Every one ran 1690.4–1693.0 s, which is plainly a hard ceiling, and produced no evaluation row crossing the threshold, hence no qualifying budget position at all. Their `per_step_cost_ratio` values were among the lowest recorded (0.7237–0.8901) and `compute_efficiency` among the highest (0.9033–1.0), which is consistent with configurations that were made cheap or aggressive per step and consequently never reached the target inside the ceiling. Cheap steps that do not converge score zero regardless of how cheap they are.

# 3. Checks that failed

**`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction". Failed 7 times**, in attempts 3, 7, 9, 10, 12, 15 and 16. This is the single most repeated finding on record. Whatever was changed between those seven attempts is not what is causing this failure: seven distinct submissions all hit the same ~1690 s wall clock without a single qualifying evaluation row. The variation between them touched something other than the cause.

**`C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists". Failed 7 times**, in the same attempts 3, 7, 9, 10, 12, 15, 16. This is strictly downstream of `C-TARGET-REACHED`: with no row crossing the threshold there is no budget position to evaluate. It is not an independent problem and fixing budget handling in isolation will not clear it.

**`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed 7 times**, again in attempts 3, 7, 9, 10, 12, 15, 16. In every one of those records the count was 0 of 2 — never 1 of 2. The perturbation runs fail jointly with the primary run, not separately from it.

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions". Failed 2 times**, in attempts 1 and 6. Both of those attempts reached the primary target and held both perturbation runs, so this is purely a source-structure violation, not a learning failure. It has now failed twice across submissions that were otherwise very different in speed (25.46 s vs 204.09 s), so whatever was changed between attempt 1 and attempt 6 is not what is causing it: module-level executable statements were reintroduced. The fix is mechanical — every statement at module scope must be an import, a constant assignment, or a permitted definition (function or class); no calls, no loops, no conditionals, no seeding or configuration side effects at import time. Wrap all of it inside functions.

Twelve attempts — 2, 4, 5, 8, 11, 13, 14, 17, 18, 19 among the scorers — had an empty `failed_checks` list, `conformance_fraction` 1.0 and `rule_conformance` 1.0. Full conformance is a solved problem when module scope is kept clean; it has been achieved repeatedly.

# 4. Ruled-out directions

**Leaving executable statements at module scope.** Ruled out by `C-API-SURFACE` failing in attempts 1 and 6. It zeroes `task_pass` even when the target is reached and both perturbation runs hold, and it drops `rule_conformance` to 0.8571. Attempt 1 shows the price directly: a 25.46 s budget, which is best-in-class speed, returned only 0.7684 where the conformant attempt 5 at 25.34 s returned 0.9128.

**Whatever configuration family produced the ~1690 s non-converging runs.** Ruled out by seven measured zeros. Seven separate submissions in this family produced `reward` 0.0000 with `qualifying_budget` "not-measured". Notably these runs had the *best* `per_step_cost_ratio` figures on record (as low as 0.7237) and `compute_efficiency` up to 1.0, and it bought them nothing. Pushing per-step cost or step aggressiveness to the point where the target is never crossed is a total loss, not a trade.

**Continuing to run after the qualifying row is reached.** Attempt 8 reached target at a 78.14 s qualifying budget but burned 151.50 s of wall clock and scored 0.7551, below attempt 2 which qualified at a very similar 73.62 s with wall clock equal to its budget and scored 0.8385. Stop as soon as the target is crossed; trailing work is penalised.

**Budgets at or above ~100 s.** Ruled out on reward grounds, not on conformance. Attempt 14 (99.74 s, fully clean) scored 0.6955 and attempt 6 (204.09 s) scored 0.5615. Both are far below the ~25–50 s band. There is no evidence anywhere in the record that a longer budget buys back reward through any other term.

**Repeating a zero-scoring configuration without changing what makes it not converge.** This is what the record shows happened: seven attempts in Class E, each producing 0.0000 with the identical three-check signature. That is neither exploration nor exploitation and it must not be repeated.

# 5. Open leads

**Combine Class A's budget with Class B's per-step cost.** This is the clearest untried point. Attempt 5 scored 0.9128 with a 25.34 s budget but only 0.7728 `compute_efficiency` and 0.9887 `per_step_cost_ratio`. Attempt 19 scored 0.9121 with a 45.81 s budget but 0.9345 `compute_efficiency` and 0.7669 `per_step_cost_ratio`. Attempt 4 hit `compute_efficiency` 1.0 with `per_step_cost_ratio` 0.7115 but needed 50.03 s. No record has ever paired a ≤ 30 s qualifying budget with a `per_step_cost_ratio` below 0.90 or a `compute_efficiency` above 0.78. If those terms are separable — and the spread across attempts 4, 5, 11 and 19 suggests they are — the combination should clear 0.9128.

**Reduce per-step cost only as far as convergence still holds.** The Class E zeros show the floor exists somewhere below the working configurations. Class B demonstrates that `per_step_cost_ratio` around 0.71–0.77 converges fine at ~46–50 s. The untested territory is whether that same per-step cost converges at ~25 s; that is exactly the experiment worth running.

**Terminate immediately on target.** Attempt 8's 78.14 s qualifying budget against 151.50 s wall clock, scoring below the comparable attempt 2, is direct evidence that the run should exit as soon as an evaluation row crosses the threshold in the declared direction. Every top-scoring record has wall clock equal to its qualifying budget.

**Keep module scope clean from the outset.** Since the stub is pristine each time, the `C-API-SURFACE` requirement must be satisfied deliberately, not inherited: imports, constants, and function/class definitions only at module level, with all seeding, configuration and execution inside functions. This is worth roughly 0.14 reward relative to an otherwise-identical violating submission.

**Note on the held-out runs.** Each record declared 2 perturbation units, one of kind `held_out_variant` and one of kind `seed`. In aggregate across all nineteen records, 24 of 38 units reached their threshold. By kind: held-out-variant runs reached in 12 of 19 records and failed in 7; seed runs reached in 12 of 19 records and failed in 7. The two kinds behave identically — neither is differentially fragile. Where they failed, both kinds failed on `C-TARGET-REACHED` ("no evaluation row crosses the threshold in the declared direction") and `C-BUDGET-RESPECTED` ("no qualifying row, so no budget position exists"), and always alongside the primary run failing the same two checks in the same record, with the aggregate reported as 0 of 2. There is no record in which a perturbation run failed while the primary run reached its target, and no record in which one kind reached while the other did not. Conclusion: the perturbation runs are not an independent robustness problem to solve. Whenever the primary configuration converges within budget, both kinds hold; make the primary converge fast and the perturbations follow.

**Call: exploit.** The scoring band is well-mapped and has visible headroom. Attempt 5 at 0.9128 is the mark to beat, and the specific, un-run combination — a ~25 s qualifying budget carrying the low per-step cost demonstrated by attempts 4 and 19, with clean module scope and immediate termination on target — is a refinement of approaches that already scored rather than a new structure. Exploration is not warranted: the scoring approaches have not stopped improving so much as stopped being tried, with the last several attempts either re-entering the non-converging Class E or landing in the slower Class C band already known to score lower.
