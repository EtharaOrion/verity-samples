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

    All 16 attempts since have scored lower than it.
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
  16 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 20 -- reward 0.8661, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 62
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 8 attempts (3, 7, 9, 10, 12, 15, 16, 21). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 8 attempts (3, 7, 9, 10, 12, 15, 16, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 8 attempts (3, 7, 9, 10, 12, 15, 16, 21). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-one graded submissions, all with `measurement_status: measured`; every one therefore carries a reward. Listed worst to best.

**Zero-reward group (eight attempts, all tied at 0.0000):** attempts 3, 7, 9, 10, 12, 15, 16 and 21 each scored **0.0000**, each with `zero_reason_code: 4`, `primary_target_reached: 0.0`, `conformance_fraction: 0.0`, and `all_perturbations_held: false`. These were measured runs that genuinely scored zero — not missing measurements. Every one of them ran to a wall clock of ~1690–1693 s (1692.52, 1692.21, 1692.97, 1690.96, 1690.45, 1690.48, 1691.53, 1690.996) and reported `qualifying_budget: "not-measured"`.

**Then, in ascending reward:**

- Attempt 6 — **0.5615** (0.5614595915946324). `rule_conformance` 0.8571, `task_pass` 0.0, budget 204.09 s, `per_step_cost_ratio` 1.3778. Worse than earlier attempts.
- Attempt 14 — **0.6955** (0.6954867988682387). Clean checks, budget 99.74 s. Worse than an earlier attempt.
- Attempt 8 — **0.7551** (0.7551378151147599). Clean checks, `qualifying_budget` 78.14 s but `wall_clock_sec` 151.50 s. Worse than an earlier attempt.
- Attempt 1 — **0.7684** (0.7684495494479875). First measured attempt. `rule_conformance` 0.8571, `task_pass` 0.0, budget 25.46 s.
- Attempt 17 — **0.7919** (0.7919387203224418). Clean checks, budget 73.80 s. Worse than an earlier attempt.
- Attempt 2 — **0.8385** (0.8385437894774304). Clean checks, budget 73.62 s. At the time, better than every earlier attempt.
- Attempt 13 — **0.8451** (0.8451024388686166). Clean checks, budget 71.31 s. Worse than an earlier attempt.
- Attempt 20 — **0.8661** (0.8661056513375137). Clean checks, `compute_efficiency` 1.0, `per_step_cost_ratio` 0.6145, budget 62.46 s. Worse than an earlier attempt.
- Attempt 4 — **0.8719** (0.8718974477208268). Clean checks, `compute_efficiency` 1.0, budget 50.03 s. At the time, better than every earlier attempt.
- Attempt 18 — **0.8794** (0.8794045780675980). Clean checks, budget 49.33 s. Worse than an earlier attempt.
- Attempt 11 — **0.8980** (0.8979842225762731). Clean checks, budget 25.35 s, `compute_efficiency` 0.7043, `per_step_cost_ratio` 1.0502. Worse than an earlier attempt.
- Attempt 19 — **0.9121** (0.9121101360711351). Clean checks, budget 45.81 s, `compute_efficiency` 0.9345, `per_step_cost_ratio` 0.7669. Worse than an earlier attempt.
- Attempt 5 — **0.9128** (0.9128129743237858). Clean checks, budget 25.34 s, `compute_efficiency` 0.7728, `per_step_cost_ratio` 0.9887.

**Attempt 5, at reward 0.9128, holds the highest score and is the one to beat.** Attempt 19 (0.9121) is within 0.0007 of it. Everything graded after attempt 5 was reported as `worse_than_an_earlier_attempt`; the loop has not improved on attempt 5 since it was measured, and later attempts 6, 8, 13, 14, 17, 18, 19, 20 and the six later zeros were all regressions against it, not progress.

Two invariants held in every single record: `validity` 1.0 and `red_line_crossed` 0.0. No submission was ever invalid, and no submission ever crossed a red line.

# 2. Approach classes tried

The measured terms describe configuration signatures rather than source code, so the classes below are defined by the signature each produced. Four distinct classes appear, and the twenty-one records collapse into them.

**Class A — short-budget conformant runs (the winners).** Target reached, both perturbations held, no failed checks, `qualifying_budget` in the 25–50 s band: attempts 5 (25.34 s, 0.9128), 11 (25.35 s, 0.8980), 19 (45.81 s, 0.9121), 18 (49.33 s, 0.8794), 4 (50.03 s, 0.8719). This class contains every reward above 0.87 and the best result overall. Within the class, reward is not a pure function of time: attempt 5 at 25.34 s and attempt 19 at 45.81 s are effectively tied (0.9128 vs 0.9121) despite attempt 19 taking 80% longer, because attempt 19 carried much higher `compute_efficiency` (0.9345 vs 0.7728) and much lower `per_step_cost_ratio` (0.7669 vs 0.9887). Attempt 11 ran at the same 25.35 s as attempt 5 but scored 0.0148 lower with worse efficiency (0.7043) and a `per_step_cost_ratio` above 1.0 (1.0502). The readable rule is that reward rewards both a short qualifying budget and cheap, efficient steps, and the two can trade against each other.

**Class B — mid-and-long-budget conformant runs.** Same clean-check signature, same both-perturbations-held signature, but `qualifying_budget` of 62–100 s: attempts 20 (62.46 s, 0.8661), 13 (71.31 s, 0.8451), 2 (73.62 s, 0.8385), 17 (73.80 s, 0.7919), 8 (78.14 s qualifying / 151.50 s wall, 0.7551), 14 (99.74 s, 0.6955). Across A and B together, reward declines almost monotonically as `qualifying_budget` rises: 25 s → ~0.90–0.91, 50 s → ~0.87–0.88, 62 s → 0.87, 71–74 s → 0.79–0.85, 78 s → 0.76, 100 s → 0.70, 204 s → 0.56. Notably attempt 20 achieved `compute_efficiency` 1.0 and the lowest `per_step_cost_ratio` ever recorded (0.6145) and still only reached 0.8661, because its budget was 62.46 s — maximal per-step efficiency did not compensate for the longer budget.

**Class C — runs that emitted module-level statements at import.** Attempts 1 and 6. Both reached the primary target and both held both perturbations, but both failed `C-API-SURFACE`, which dropped `rule_conformance` to 0.8571 (six of seven rule checks) and `task_pass` to 0.0 while leaving reward non-zero. Attempt 1 is the direct experiment here: at a budget of 25.46 s — essentially identical to attempt 5's 25.34 s — it scored 0.7684 against attempt 5's 0.9128. The `C-API-SURFACE` failure alone is worth roughly 0.14 of reward at matched budget. Attempt 6 compounded it with a 204.09 s budget and a `per_step_cost_ratio` of 1.3778 and landed at 0.5615, the worst non-zero result.

**Class D — runaway long runs that never crossed the threshold.** Eight attempts (3, 7, 9, 10, 12, 15, 16, 21), all 0.0000, all `zero_reason_code: 4`. Every one ran to ~1690–1693 s of wall clock, a band so tight across eight independent submissions that it is plainly a hard ceiling being hit rather than eight coincidental durations. All eight reported `qualifying_budget: "not-measured"` because no row ever qualified. Their `compute_efficiency` was high (0.9033–1.0) and their `per_step_cost_ratio` low (0.6826–0.8901), so the steps were cheap and efficient — the runs simply never produced an evaluation row on the correct side of the threshold before time ran out. This class was re-entered eight separate times without the thing that caused the zero being fixed; that is neither exploration nor exploitation, and the loop should not enter it a ninth time.

# 3. Checks that failed

Four named checks failed, and only four.

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions."** Failed **twice**, in attempts 1 and 6. These two attempts differ enormously in every other respect (budget 25.46 s vs 204.09 s, `compute_efficiency` 0.8160 vs 0.6091, `per_step_cost_ratio` 1.0639 vs 1.3778), yet both produced the identical failure with the identical reason. Whatever was changed between them is not what causes this check to fail. The cause is structural: executable code sitting at module scope. The fix is to move all module-level work inside function or class definitions, leaving only imports, constant assignments, and permitted definitions at the top level. This check has never failed in any attempt that scored above 0.79.

**`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction."** Failed **eight times**, in attempts 3, 7, 9, 10, 12, 15, 16 and 21, with the identical reason each time. Eight distinct submissions produced it, spread across the whole run history — early (3, 7), middle (9, 10, 12), and late (15, 16, 21). Whatever was varied between those eight submissions is not what causes this check to fail. Every one of them also burned ~1690 s of wall clock. The two facts together say the runs were training or searching without ever producing a qualifying evaluation row before the ceiling.

**`C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists."** Failed **eight times**, in exactly the same eight attempts. This reason is explicitly downstream of `C-TARGET-REACHED`: with no qualifying row there is no budget position to evaluate. It is not an independent defect and will resolve the moment a row crosses the threshold. Do not spend effort on it separately.

**`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget."** Failed **eight times**, in the same eight attempts, always with the count 0 of 2. Never a partial failure — never 1 of 2. The perturbations fail as a block precisely when the primary fails.

Across all twenty-one records there is no case of a submission failing a check while `primary_target_reached` was 1.0 other than the two `C-API-SURFACE` cases, and there is no case of `validity` or `red_line_crossed` being tripped.

# 4. Ruled-out directions

**Long-running search or training that pushes toward the ~1690 s wall clock.** Ruled out by eight measured zeros. Every submission in that band scored 0.0000 with `C-TARGET-REACHED`, `C-BUDGET-RESPECTED` and `C-PERTURBATION-REACHED` all failing and `qualifying_budget` unmeasurable. High `compute_efficiency` (up to 1.0) and low `per_step_cost_ratio` (down to 0.6826) did not rescue any of them. Whatever this class does, it does not produce a threshold-crossing evaluation row within the available time.

**Leaving executable statements at module scope.** Ruled out by attempts 1 and 6, both failing `C-API-SURFACE` for the same reason. Attempt 1 shows the direct cost: matched budget with attempt 5 (25.46 s vs 25.34 s) but 0.7684 against 0.9128. The check zeroes `task_pass` and knocks `rule_conformance` to 0.8571 while the run otherwise succeeds — pure lost reward for no benefit.

**Long-but-passing configurations, i.e. accepting a large `qualifying_budget` in exchange for a comfortable pass.** Ruled out by the clear monotone decay in Class B: 62.46 s → 0.8661, 71.31 s → 0.8451, 73.62 s → 0.8385, 73.80 s → 0.7919, 78.14 s → 0.7551, 99.74 s → 0.6955, 204.09 s → 0.5615. Passing all checks is necessary but nowhere near sufficient; every additional second of qualifying budget costs measurable reward.

**Optimising `per_step_cost_ratio` in isolation.** Ruled out by attempt 20, which achieved `compute_efficiency` 1.0 and `per_step_cost_ratio` 0.6145 — the cheapest steps ever recorded — and still scored only 0.8661, below attempts 5, 19, 11 and 18, all of which had costlier steps but shorter budgets. Cheap steps do not buy back a long budget.

**Letting wall clock run far past the qualifying budget.** Attempt 8 is the one clean-check case where `wall_clock_sec` (151.50 s) is roughly double `qualifying_budget` (78.14 s); it scored 0.7551, poorly for its class. Work performed after the qualifying row is charged somewhere and returns nothing.

# 5. Open leads

**Reproduce attempt 5's regime exactly and then push the budget below 25 s.** Attempt 5 is the standing best at 0.9128 with a 25.34 s qualifying budget, `compute_efficiency` 0.7728, and `per_step_cost_ratio` 0.9887. Nothing in the record has beaten a sub-30 s budget with clean checks. The 25 s band has been hit twice (attempts 5 and 11) and produced the two shortest budgets on record; no attempt has gone below it. That is the most obvious unexplored direction.

**Combine attempt 5's budget with attempt 19's efficiency.** These are the two best results and they got there differently. Attempt 19 reached 0.9121 at 45.81 s by carrying `compute_efficiency` 0.9345 and `per_step_cost_ratio` 0.7669; attempt 5 reached 0.9128 at 25.34 s with efficiency only 0.7728 and per-step cost 0.9887. Neither has been tried in combination. A run in the 25–30 s band with `compute_efficiency` near 0.93 and `per_step_cost_ratio` near 0.77 has strictly better inputs on both axes than either and is the single highest-value experiment available. Attempt 11 is the cautionary control: same 25 s band as attempt 5 but efficiency 0.7043 and per-step cost above 1.0 (1.0502), and it lost 0.0148.

**Keep `per_step_cost_ratio` below 1.0.** Every attempt with a ratio above 1.0 scored below 0.90: attempt 6 (1.3778, 0.5615), attempt 1 (1.0639, 0.7684), attempt 11 (1.0502, 0.8980), attempt 8 (1.0291, 0.7551), attempt 13 (1.0266, 0.8451). Only attempt 5 (0.9887) sits just under the line among the top results. Staying below 1.0 is a cheap constraint to respect.

**Hard-cap the run so the ~1690 s failure mode is structurally impossible.** All eight zeros share that ceiling. An explicit step or time cap well under it, with the best evaluation row emitted before the cap, converts the catastrophic 0.0000 outcome into at worst a low-but-positive score. This is a safety rail rather than an improvement, but it removes the single largest source of lost reward in the history.

**Keep module scope to imports, constants and definitions only.** `C-API-SURFACE` has cost roughly 0.14 of reward at matched budget and is entirely mechanical to avoid. Verify before submitting that no statement executes at import time.

**Perturbation coverage needs no separate work.** Across all twenty-one records, forty-two held-out runs were declared, two per submission, one of kind `held_out_variant` and one of kind `seed`. In the thirteen submissions that reached the primary target, every run of both kinds reached its threshold with no failed checks — thirteen `held_out_variant` runs held and thirteen `seed` runs held, twenty-six in aggregate. In the eight zero-reward submissions, every run of both kinds failed, each on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` — eight `held_out_variant` failures and eight `seed` failures, sixteen in aggregate. Neither kind has ever failed while the primary target was reached, and neither kind has ever held while the primary target was missed. The perturbations are not an independent robustness problem to solve; they track the primary run one-for-one. Fixing the primary threshold crossing fixes them.

**Call: exploit.** The top of the table is a tight cluster of clean-check, short-budget runs — 0.9128, 0.9121, 0.8980, 0.8794, 0.8719 — that differ only in `qualifying_budget`, `compute_efficiency` and `per_step_cost_ratio`, and the reward surface over those three quantities is legible from the records. The next attempt should rebuild the Class A configuration, drive the qualifying budget toward or below 25 s while holding `compute_efficiency` high and `per_step_cost_ratio` under 1.0, keep module scope clean to avoid `C-API-SURFACE`, and cap the run so it can never drift into the ~1690 s zero regime. The target to beat is attempt 5 at 0.9128.
