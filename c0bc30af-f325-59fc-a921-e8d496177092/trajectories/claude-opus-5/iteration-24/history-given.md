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

    All 18 attempts since have scored lower than it.
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
  20       0.8661   1.000             2 of 2         yes             62                
  21       0.0000   1.000             0 of 2         no              --                
  22       0.0000   1.000             0 of 2         no              --                
  23       0.8768   1.000             2 of 2         yes             50                

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

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.9121, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 46
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 21 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 22 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 2 of your last 4 attempts
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same seed run has now failed on 2 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 23 -- reward 0.8768, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

All twenty-three graded records carry `measurement_status: "measured"`, so every one of them has a real reward. None produced "no measurement"; the nine zeros below are measured zeros (`zero_reason_code: 4`), not missing data.

Ordered worst to best by reward:

- Attempts 3, 7, 9, 10, 12, 15, 16, 21, and 22 — reward **0.0000** each. Nine attempts, all with the same signature: `primary_target_reached: 0.0`, `conformance_fraction: 0.0`, `all_perturbations_held: false`, and wall clock pinned in a narrow band of 1690.32–1692.97 s. Every one of these is recorded as `worse_than_an_earlier_attempt`.
- Attempt 6 — reward **0.5615**. `task_pass: 0.0`, `rule_conformance: 0.8571`, wall clock 204.09 s, `per_step_cost_ratio: 1.3778`. Lower than every scoring attempt before it; recorded as worse than an earlier attempt.
- Attempt 14 — reward **0.6955**. Clean checks, wall clock 99.74 s. Lower than the then-best (0.9128 at attempt 5); worse than an earlier attempt.
- Attempt 8 — reward **0.7551**. Clean checks, but `qualifying_budget` 78.14 s against `wall_clock_sec` 151.50 s — the only record where the two diverge. Worse than an earlier attempt.
- Attempt 1 — reward **0.7684**. First measured attempt. Target reached and both perturbations held, but `task_pass: 0.0` and `rule_conformance: 0.8571` from a failed check; wall clock 25.46 s.
- Attempt 17 — reward **0.7919**. Clean checks, wall clock 73.80 s. Worse than an earlier attempt.
- Attempt 2 — reward **0.8385**. Clean checks, wall clock 73.62 s. At the time, better than every earlier attempt.
- Attempt 13 — reward **0.8451**. Clean checks, wall clock 71.31 s. Worse than an earlier attempt.
- Attempt 20 — reward **0.8661**. Clean checks, `compute_efficiency: 1.0`, `per_step_cost_ratio: 0.6146` (the lowest recorded), wall clock 62.46 s. Worse than an earlier attempt.
- Attempt 4 — reward **0.8719**. Clean checks, `compute_efficiency: 1.0`, wall clock 50.03 s. At the time, better than every earlier attempt.
- Attempt 23 — reward **0.8768**. Clean checks, wall clock 49.67 s. Worse than an earlier attempt.
- Attempt 18 — reward **0.8794**. Clean checks, wall clock 49.33 s. Worse than an earlier attempt.
- Attempt 11 — reward **0.8980**. Clean checks, wall clock 25.35 s. Worse than an earlier attempt.
- Attempt 19 — reward **0.9121**. Clean checks, wall clock 45.81 s, `compute_efficiency: 0.9345`, `per_step_cost_ratio: 0.7669`. Worse than an earlier attempt, but only by 0.0007.
- **Attempt 5 — reward 0.9128. This is the highest reward recorded and the one to beat.** Clean checks, `task_pass: 1.0`, `rule_conformance: 1.0`, both perturbations held, wall clock 25.34 s, `compute_efficiency: 0.7728`, `per_step_cost_ratio: 0.9887`.

Nothing after attempt 5 has beaten it. Attempts 6 through 23 are all recorded as `worse_than_an_earlier_attempt`, and the closest anything has come since is attempt 19 at 0.9121.

An important structural reading of the scoring: among the fourteen attempts that reached the primary target, reward falls almost monotonically as `qualifying_budget` / wall clock rises — 25.3 s → ~0.90–0.91, 45–50 s → ~0.87–0.91, 62–74 s → ~0.84–0.87, 99.7 s → 0.6955, 204.1 s → 0.5615. Time-to-target is the dominant lever. But it is not the only one: attempt 19 at 45.81 s (efficiency 0.9345, per-step 0.7669) scored 0.9121, statistically level with attempt 5 at 25.34 s (efficiency 0.7728, per-step 0.9887), and attempt 11 at 25.35 s scored 0.8980 — 0.0148 below attempt 5 at essentially identical wall clock, with worse efficiency (0.7043) and worse per-step cost (1.0502). So reward blends time-to-target with compute efficiency and per-step cost, and conformance gates the whole thing.

## 2. Approach classes tried

The measured terms describe outcomes, not source, so these classes are grouped by their measured signature. Records that failed identically are collapsed into one entry.

**Class A — fast conformant convergence, ~25 s to target.** Attempts 5 (0.9128) and 11 (0.8980), plus attempt 1 (0.7684) which had the same 25 s timing but was disqualified on a rule check. This class holds the top of the board. Within it, the difference between 0.9128 and 0.8980 tracks `compute_efficiency` (0.7728 vs 0.7043) and `per_step_cost_ratio` (0.9887 vs 1.0502), not wall clock, which was 25.34 s vs 25.35 s.

**Class B — mid-length conformant convergence, 45–78 s to target.** Attempts 19 (0.9121, 45.81 s), 18 (0.8794, 49.33 s), 23 (0.8768, 49.67 s), 4 (0.8719, 50.03 s), 20 (0.8661, 62.46 s), 13 (0.8451, 71.31 s), 2 (0.8385, 73.62 s), 17 (0.7919, 73.80 s), 8 (0.7551, 78.14 s qualifying / 151.50 s wall). Every one is fully conformant with both perturbations held. This class contains the second-best result overall (attempt 19), obtained with high `compute_efficiency` (0.9345) rather than raw speed — the one existing demonstration that efficiency can substitute for wall clock.

**Class C — slow conformant convergence, 99–204 s.** Attempts 14 (0.6955, 99.74 s) and 6 (0.5615, 204.09 s, also non-conformant). Reaching the target is not enough; at these budgets the reward collapses to the 0.56–0.70 range. This class is strictly dominated.

**Class D — non-converging long runs.** Nine attempts (3, 7, 9, 10, 12, 15, 16, 21, 22), all reward 0.0000. Every one ran 1690–1693 s — a band so tight across nine records that it reads as a hard ceiling being hit, not as nine independent coincidences — and produced no evaluation row crossing the threshold. Their `compute_efficiency` values are high (0.9033–1.0) and `per_step_cost_ratio` low (0.6826–0.8901): cheap per step, but the run never converges within the allowed horizon, so the cheapness buys nothing. This class has now been re-entered nine separate times, spread across the whole run of attempts (3, 7, 9, 10, 12, 15, 16, 21, 22), each time scoring exactly zero.

**Class E — module-level executable code.** Attempts 1 and 6. Orthogonal to the speed axis: attempt 1 was fast (25.46 s) and attempt 6 was slow (204.09 s), and both were docked identically, `rule_conformance` 0.8571 (6 of 7) and `task_pass` 0.0, while still reaching the primary target and holding both perturbations. Attempt 1 would plausibly have been in contention for the top had it been conformant.

## 3. Checks that failed

Four distinct named checks have failed, across thirteen records.

**C-API-SURFACE** — "module-level statements outside imports, constants, and permitted definitions". Failed **twice**, at attempts 1 and 6. Those two attempts differ enormously in every other respect (25.46 s vs 204.09 s; per-step cost 1.0639 vs 1.3778), so whatever was changed in the training algorithm between them is not what causes this check to fail. It is caused solely by executable statements at module top level, and it is fixable by moving all such work inside functions and leaving only imports, constant assignments and definitions at module scope. It cost `rule_conformance` 0.8571 and `task_pass` 0.0 both times even though the target was reached and every perturbation held.

**C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction". Failed **nine times**, at attempts 3, 7, 9, 10, 12, 15, 16, 21, 22. This is the single most repeated failure in the record and the only cause of a zero reward. Across those nine attempts `per_step_cost_ratio` varied from 0.6826 to 0.8901 and `compute_efficiency` from 0.9033 to 1.0, so whatever was varied between them is not what causes this check to fail. The common factor is that each ran to the ~1690 s ceiling without ever registering a threshold crossing.

**C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". Failed **nine times**, in exactly the same nine records. It is downstream of C-TARGET-REACHED: with no crossing row there is nothing to measure a budget against. Fixing the target crossing fixes this automatically; it is not a separate defect.

**C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed **nine times**, in the same nine records, always at 0 of 2. Never a partial failure.

Every scoring attempt (all fourteen with nonzero reward) had `red_line_crossed: 0.0` and `validity: 1.0`; in fact all twenty-three records have `validity: 1.0` and no red line crossed. Validity has never been the problem.

## 4. Ruled-out directions

**Any configuration that runs to the ~1690 s ceiling.** Nine attempts have now done this and every one scored 0.0000 on C-TARGET-REACHED plus its two downstream checks. The reason is that no evaluation row ever crosses the threshold in the declared direction, so no reward accrues at all — good per-step economy (0.68–0.89) and near-perfect `compute_efficiency` (up to 1.0) do not compensate. Re-entering this class without changing whatever makes the run fail to converge is not exploration and not exploitation; it is a repeat of a known zero, and the record shows it has been repeated nine times.

**Module-level executable statements.** Ruled out by two independent failures of C-API-SURFACE (attempts 1 and 6), each costing `rule_conformance` 0.8571 and `task_pass` 0.0. Attempt 1 reached the target in 25.46 s — top-tier timing — and still scored only 0.7684 because of it. There is no benefit on record and a large measured cost.

**Trading wall clock for per-step cost.** Attempt 20 achieved the lowest `per_step_cost_ratio` in the whole record (0.6146) with `compute_efficiency: 1.0`, and still scored only 0.8661 because it took 62.46 s. Attempt 6 pushed per-step cost the other way (1.3778) over 204.09 s for 0.5615. Cheap steps that lengthen time-to-target lose reward.

**Letting the run continue past the crossing.** Attempt 8 is the only record where `wall_clock_sec` (151.50 s) exceeds `qualifying_budget` (78.14 s); it scored 0.7551, well below same-era conformant runs. Trailing compute after the target is crossed is pure loss.

**Budgets above ~100 s.** Attempts 14 (99.74 s → 0.6955) and 6 (204.09 s → 0.5615) are both dominated by every run under 80 s. There is no reward regime up there worth exploring.

**Hardening for perturbation robustness as a priority.** Ruled out as a target of effort, not as a requirement. In all twenty-three records there is not one case where the primary target was reached but a perturbation failed. Perturbation outcomes are perfectly coupled to the primary outcome, so spending budget on robustness margin buys nothing measurable.

## 5. Open leads

**Combine attempt 5's speed with attempt 19's efficiency.** These are the two best results and they got there by different routes: attempt 5 at 25.34 s with `compute_efficiency` 0.7728 and `per_step_cost_ratio` 0.9887 (0.9128), attempt 19 at 45.81 s with efficiency 0.9345 and per-step 0.7669 (0.9121). Both axes visibly contribute. A configuration that reaches the target in ~25 s *and* carries `compute_efficiency` in the 0.93–1.0 band with `per_step_cost_ratio` at or below ~0.77 has never been measured, and it is the clearest untried point above the current frontier. Attempt 11 shows the sensitivity: same 25 s, worse efficiency and per-step above 1.0, and it lost 0.0148 of reward.

**Stop the instant the threshold is crossed.** Attempt 8 lost roughly half its wall clock to work done after the qualifying row. Emitting the crossing row and terminating immediately should convert any given convergence speed into its best available reward, and it is a mechanical change independent of the learning algorithm.

**Bound the run so a non-converging configuration still emits a qualifying row.** The nine-times-repeated C-TARGET-REACHED failure always coincides with hitting the ~1690 s ceiling. Whatever schedule or hyperparameter choice sends a run into that regime should be capped: an iteration or time cap that forces evaluation rows to be written well before the ceiling would at worst yield a slow-but-scoring result in Class B or C rather than a hard 0.0000. Even a 0.5615 is infinitely better than a zero.

**Keep module scope clean by construction.** Given C-API-SURFACE has fired twice, put every statement inside a function or method and leave module level to imports, constant assignments and `def`/`class` definitions only. This is a precondition on any of the leads above, not an alternative to them.

**Retire the ~1690 s class entirely.** If the next attempt would land there, it should not be run in that form. The measured evidence is nine identical zeros with no variation in outcome across wide variation in cost metrics.

**Call: exploit.** The scoring approaches have not stopped improving — the top of the board is a two-point frontier (attempt 5 at 0.9128 by speed, attempt 19 at 0.9121 by efficiency) whose combination has never been measured, and there is a known mechanical loss (post-crossing compute, attempt 8) still on the table. Take the Class A fast-convergence configuration that produced attempt 5's 25.34 s, hold module scope conformant, stop on crossing, and pull `compute_efficiency` and `per_step_cost_ratio` toward attempt 19's and attempt 20's values without letting wall clock rise. The number to beat is 0.9128.
