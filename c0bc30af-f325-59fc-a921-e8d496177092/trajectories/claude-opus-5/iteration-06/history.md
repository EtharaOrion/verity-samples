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

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4        0.8719   1.000             2 of 2         yes             50                
  5 *      0.9128   1.000             2 of 2         yes             25                
  6        0.5615   0.857             2 of 2         yes             204               

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
  2 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 2 -- reward 0.8385, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.8719, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 6 -- reward 0.5615, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 204
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED failed on attempt 3.
    C-PERTURBATION-REACHED failed on attempt 3.
    C-TARGET-REACHED failed on attempt 3.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Six graded submissions, all with `measurement_status: measured`, so all six carry a reward. Listed worst to best:

- **Attempt 3 — reward 0.0000.** Zeroed out (`zero_reason_code: 4`). `primary_target_reached: 0.0`, `conformance_fraction: 0.0`, `all_perturbations_held: false`, `qualifying_budget: not-measured`, `wall_clock_sec: 1692.52` (by far the longest run recorded). `rule_conformance` was a clean 1.0 and `validity` 1.0 — the submission was well-formed; it simply never crossed the target threshold. Standing: worse than an earlier attempt.
- **Attempt 6 — reward 0.5615.** `primary_target_reached: 1.0` and both perturbations held, but `task_pass: 0.0` and `rule_conformance: 0.857` because of one failed check. `wall_clock_sec: 204.09`, `compute_efficiency: 0.609`, `per_step_cost_ratio: 1.3778`. Standing: worse than an earlier attempt — this is a regression, not progress, and it is the second-lowest score on record.
- **Attempt 1 — reward 0.7684.** First measured attempt. `primary_target_reached: 1.0`, both perturbations held, but `task_pass: 0.0` and `rule_conformance: 0.857` from one failed check. `wall_clock_sec: 25.46`, `compute_efficiency: 0.816`, `per_step_cost_ratio: 1.0639`.
- **Attempt 2 — reward 0.8385.** No failed checks, `task_pass: 1.0`, `rule_conformance: 1.0`, both perturbations held. `wall_clock_sec: 73.62`, `compute_efficiency: 0.916`, `per_step_cost_ratio: 0.9162`. Standing: better than every earlier attempt at the time.
- **Attempt 4 — reward 0.8719.** No failed checks, `task_pass: 1.0`, `compute_efficiency: 1.0` (the only perfect value recorded), `per_step_cost_ratio: 0.7115` (the lowest recorded), `wall_clock_sec: 50.03`. Standing: better than every earlier attempt at the time.
- **Attempt 5 — reward 0.9128.** No failed checks, `task_pass: 1.0`, `rule_conformance: 1.0`, both perturbations held. `wall_clock_sec: 25.34` (the shortest qualifying run recorded), `compute_efficiency: 0.773`, `per_step_cost_ratio: 0.9887`. Standing: better than every earlier attempt.

**Attempt 5, at reward 0.9128, holds the highest reward and is the one to beat.**

A relation worth carrying forward: among the three fully conformant, target-reaching attempts, reward tracks wall-clock time inversely and almost perfectly — 25.34 s → 0.9128, 50.03 s → 0.8719, 73.62 s → 0.8385. It does *not* track `compute_efficiency`: attempt 4 posted `compute_efficiency: 1.0` and still scored below attempt 5, which posted 0.773. Whatever `compute_efficiency` measures, it is not the thing being maximised; short qualifying wall-clock with the target reached and no failed checks is what has produced the top scores.

# 2. Approach classes tried

The measured terms describe outcomes, not source, so these classes are grouped by their measured signature. Four distinct classes appear across the six records.

**Class A — fast, fully conformant, target-reaching (attempts 5 and 4; attempt 2 is the slower member of the same family).** Zero failed checks, `task_pass: 1.0`, `validity: 1.0`, `rule_conformance: 1.0`, both declared perturbations reached. These three occupy the top three reward slots. Within the class the only thing that moves reward is the qualifying wall-clock/budget position: 25.34 s scored 0.9128, 50.03 s scored 0.8719, 73.62 s scored 0.8385. Attempt 4 pushed `per_step_cost_ratio` down to 0.7115 and `compute_efficiency` to 1.0 but took twice the wall-clock of attempt 5 and scored lower for it — cheaper steps bought at the price of more of them was a losing trade.

**Class B — conformant training content but with an illegal module surface (attempts 1 and 6).** Both reached the primary target and both held all perturbations, so the learning algorithm itself worked in each case. Both were docked to `rule_conformance: 0.857` and `task_pass: 0.0` by the same single check, `C-API-SURFACE`. Attempt 1 was fast (25.46 s, comparable to the best-scoring attempt 5) and still only scored 0.7684; attempt 6 was slow (204.09 s, `per_step_cost_ratio: 1.3778`) and scored 0.5615. The lesson: this class caps out well below the conformant class even when its runtime is competitive — attempt 1 ran essentially as fast as attempt 5 and lost roughly 0.14 reward purely to the surface violation.

**Class C — long-horizon / heavy training that never crossed the threshold (attempt 3).** 1692.52 s of wall clock, `per_step_cost_ratio: 0.8484`, `compute_efficiency: 0.967` — the per-step economics looked fine, but no evaluation row ever crossed the target in the declared direction, so nothing qualified and the reward was 0.0000. This is the single hard zero on record.

**Class D — high-cost-per-step variants (attempt 6, and attempt 1 to a lesser degree).** `per_step_cost_ratio` above 1.0 (1.3778 and 1.0639). Both members of this class are also Class B members, so the two effects are confounded in the data; what is clear is that no attempt with `per_step_cost_ratio > 1.0` has ever passed all checks.

# 3. Checks that failed

Four distinct named checks have failed across the six records.

- **`C-API-SURFACE`** — reason given by the verifier, identically both times: *"module-level statements outside imports, constants, and permitted definitions."* **This check has now failed twice, in attempt 1 and again in attempt 6.** Everything that was changed to the training algorithm between those two attempts — and the two are very different in runtime, cost ratio and efficiency — is demonstrably *not* what causes this failure. The cause is structural: the submission file contains executable statements at module level that are neither imports, nor constant assignments, nor permitted definitions (function/class defs). It is fixable by moving every top-level statement inside a function or under the permitted-definition forms, and by nothing else. Each occurrence cost `task_pass` outright (1.0 → 0.0) and dropped `rule_conformance` to 0.857 while leaving the target reached, which is a large, purely avoidable reward loss.
- **`C-TARGET-REACHED`** — *"no evaluation row crosses the threshold in the declared direction."* Failed once, in attempt 3, at the primary level.
- **`C-BUDGET-RESPECTED`** — *"no qualifying row, so no budget position exists."* Failed once, in attempt 3. This is a downstream consequence of `C-TARGET-REACHED`: with nothing qualifying, there is no budget position to evaluate. Fixing the target reach should clear this too.
- **`C-PERTURBATION-REACHED`** — *"0 of 2 declared perturbations reached their own threshold inside their own budget."* Failed once, in attempt 3.

**Perturbation-unit outcomes.** Every record declared 2 perturbations, and in every record the two units were of kind `held_out_variant` and kind `seed`. Across all six records that is 12 held-out runs beside the primary. **Ten of the twelve reached their threshold; two did not, both of them in attempt 3.** By kind: `held_out_variant` runs reached in 5 of 6 records; `seed` runs reached in 5 of 6 records. The two failures — one of kind `held_out_variant`, one of kind `seed` — each failed on the same pair of checks, `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. In every record where the primary target was reached, both perturbation kinds also reached; the only record where they failed is the record where the primary failed as well. There is no evidence of a perturbation kind that is selectively fragile: `held_out_variant` and `seed` have behaved identically in all six records. The runs are not individually identified, so nothing links a run in one record to a run in another.

# 4. Ruled-out directions

- **Any submission that leaves executable statements at module scope.** Ruled out because `C-API-SURFACE` has fired twice on exactly that reason and cost `task_pass` both times. Attempt 1 proves the point cleanly: it ran in 25.46 s, nearly identical to the 25.34 s of the best attempt, and still scored 0.7684 against 0.9128, with the surface violation the only recorded difference in check status.
- **Long-horizon training runs in the thousand-second range (the attempt-3 shape).** Ruled out: 1692.52 s produced no evaluation row crossing the threshold, zeroed the reward, and dragged both perturbation kinds down with it. Spending more wall clock did not buy target reach; it forfeited it.
- **Optimising `compute_efficiency` or `per_step_cost_ratio` as the objective.** Ruled out by direct comparison: attempt 4 achieved `compute_efficiency: 1.0` and the record-low `per_step_cost_ratio: 0.7115` and still scored 0.8719, below attempt 5's 0.9128 at `compute_efficiency: 0.773` and `per_step_cost_ratio: 0.9887`. These metrics are reported but are not the ranking quantity; total qualifying wall-clock is what separated them.
- **Trading step count for cheaper steps.** Ruled out for the same reason — attempt 4's cheaper steps came with double the wall-clock of attempt 5 and a lower reward.
- **Accepting `per_step_cost_ratio` above 1.0.** Both records above 1.0 (1.0639, 1.3778) scored in the bottom half of the non-zero results. Not proven causal on its own, since both are confounded with the `C-API-SURFACE` failure, but there is no measured case of it helping.

# 5. Open leads

- **Rebuild the attempt-5 shape and drive qualifying wall-clock below 25.34 s.** This is the highest-value lead. The three conformant records give a near-linear reward-versus-time relation (73.62 s → 0.8385, 50.03 s → 0.8719, 25.34 s → 0.9128), and attempt 5 sits at the fast end of what has been tried. Extrapolating that trend, further reductions in time-to-threshold should continue to pay, and there is headroom above 0.9128.
- **Reach the threshold sooner rather than training longer.** The evidence says the target is reachable quickly and reliably: it was reached in five of six records, including one at 25.34 s. Whatever schedule/epoch budget attempt 5 used, shrink it further and stop as soon as the evaluation row crosses in the declared direction — but keep a safety margin, because attempt 3 shows the cliff on the other side is a hard 0.0000, not a graceful degradation.
- **Guarantee module-surface conformance mechanically before submitting.** Every top-level statement must be an import, a constant assignment, or a permitted definition. Wrap any setup, seeding, configuration or demo code inside the entry-point function. This check has cost two attempts already and it is orthogonal to the algorithm, so it should be treated as a fixed structural constraint on the stub rather than something re-derived each time.
- **Keep `per_step_cost_ratio` at or below roughly 1.0 as a guardrail, not a target.** Attempt 5 scored best at 0.9887; do not spend wall-clock buying it lower.
- **Do not weaken robustness in the pursuit of speed.** Both perturbation kinds, `held_out_variant` and `seed`, have reached their threshold in every record where the primary did. That margin is currently free; a speed cut aggressive enough to make the primary marginal would risk `C-PERTURBATION-REACHED` on both kinds at once, which is what turned attempt 3 into a zero.

**Call: exploit.** The top three rewards all come from one approach class (fully conformant, target-reaching, fast), that class is still improving with each reduction in qualifying wall-clock, and the single largest measured loss — `C-API-SURFACE`, twice — is a known, named, mechanical fix rather than an open research question. Reproduce attempt 5's configuration, eliminate any module-level statements, and tighten time-to-threshold below 25.34 s. Note for the record that attempts 1 and 6 repeated the same `C-API-SURFACE` failure without changing the thing that caused it; that pattern should not be repeated.
