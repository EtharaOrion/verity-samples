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

    All 11 attempts since have scored lower than it.
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

    attempt 14 -- reward 0.6955, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 100
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 15 -- reward 0.0000, worse than an earlier attempt
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

    attempt 16 -- reward 0.0000, worse than an earlier attempt
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

Every record below carries `measurement_status: "measured"`, so every one has a real reward; none is missing a measurement. Ordered worst to best by reward:

- **Attempt 3 — reward 0.0000.** `zero_reason_code` 4, wall clock 1692.52 s, `primary_target_reached` 0, `conformance_fraction` 0.0, both perturbations failed. Worse than an earlier attempt.
- **Attempt 7 — reward 0.0000.** Same signature: wall clock 1692.21 s, target not reached, both perturbations failed. Worse than an earlier attempt.
- **Attempt 9 — reward 0.0000.** Wall clock 1692.97 s, same failure signature. Worse than an earlier attempt.
- **Attempt 10 — reward 0.0000.** Wall clock 1690.96 s, same failure signature. Worse than an earlier attempt.
- **Attempt 12 — reward 0.0000.** Wall clock 1690.45 s, same failure signature. Worse than an earlier attempt.
- **Attempt 15 — reward 0.0000.** Wall clock 1690.48 s, same failure signature. Worse than an earlier attempt.
- **Attempt 16 — reward 0.0000.** Wall clock 1691.53 s, same failure signature. Worse than an earlier attempt.
- **Attempt 6 — reward 0.5615.** Primary target reached and both perturbations held, but `C-API-SURFACE` failed: `rule_conformance` 0.8571, `task_pass` 0. Qualifying budget 204.09 s, `per_step_cost_ratio` 1.3778, `compute_efficiency` 0.6091. Worse than an earlier attempt.
- **Attempt 14 — reward 0.6955.** Fully clean (no failed checks, `task_pass` 1), qualifying budget 99.74 s, `per_step_cost_ratio` 0.9155, `compute_efficiency` 0.9220. Lower than earlier clean attempts — worse than an earlier attempt.
- **Attempt 8 — reward 0.7551.** Clean, `task_pass` 1, qualifying budget 78.14 s but wall clock 151.50 s (the only record where those two diverge materially), `per_step_cost_ratio` 1.0291. Worse than an earlier attempt.
- **Attempt 1 — reward 0.7684.** First measured attempt. Primary target reached, both perturbations held, but `C-API-SURFACE` failed: `rule_conformance` 0.8571, `task_pass` 0. Qualifying budget 25.46 s, `per_step_cost_ratio` 1.0639.
- **Attempt 2 — reward 0.8385.** Clean, `task_pass` 1, qualifying budget 73.62 s, `per_step_cost_ratio` 0.9162. Best at the time it ran.
- **Attempt 13 — reward 0.8451.** Clean, `task_pass` 1, qualifying budget 71.31 s, `per_step_cost_ratio` 1.0266. Worse than an earlier attempt.
- **Attempt 4 — reward 0.8719.** Clean, `task_pass` 1, qualifying budget 50.03 s, `per_step_cost_ratio` 0.7115, `compute_efficiency` 1.0. Best at the time it ran.
- **Attempt 11 — reward 0.8980.** Clean, `task_pass` 1, qualifying budget 25.35 s, `per_step_cost_ratio` 1.0502, `compute_efficiency` 0.7043. Still lower than the best — worse than an earlier attempt.
- **Attempt 5 — reward 0.9128.** Clean, `task_pass` 1, `primary_target_reached` 1, both perturbations held, qualifying budget 25.34 s, `per_step_cost_ratio` 0.9887, `compute_efficiency` 0.7728, `rule_conformance` 1.0.

**Attempt 5, at reward 0.9128, holds the highest reward and is the one to beat.** No attempt after it has matched it: attempts 6, 8, 13 and 14 scored below it, attempt 11 came closest at 0.8980 and was still below it, and attempts 7, 9, 10, 12, 15 and 16 all scored 0.0000. `red_line_crossed` is 0.0 and `validity` is 1.0 in every record, so nothing has ever been invalidated outright.

# 2. Approach classes tried

The measured terms do not carry source code, so these classes are grouped by their measured signature. Sixteen records collapse into four distinct classes.

**Class A — fast conformant convergence (~25 s qualifying budget).** Attempts 5 (0.9128), 11 (0.8980) and 1 (0.7684). All three reach the primary target and hold both perturbations with a qualifying budget of 25.3–25.5 s. Attempts 5 and 11 are fully clean; attempt 1 carries the `C-API-SURFACE` failure that cost it `task_pass` and dropped `rule_conformance` to 0.8571, which is the whole gap between its 0.7684 and attempt 5's 0.9128 at essentially identical budget. This class contains the two highest rewards ever recorded and is the productive region.

**Class B — mid-length conformant convergence (50–100 s qualifying budget).** Attempts 4 (0.8719, 50.03 s), 13 (0.8451, 71.31 s), 2 (0.8385, 73.62 s), 8 (0.7551, 78.14 s qualifying / 151.50 s wall) and 14 (0.6955, 99.74 s). All clean, all `task_pass` 1, all perturbations held. Reward falls monotonically as the budget grows across this class. Attempt 4 is notable as the only record with `compute_efficiency` 1.0 and the lowest `per_step_cost_ratio` observed among scoring runs (0.7115); it beat the 71–74 s runs despite not being the fastest wall-clock class.

**Class C — long conformant run with an API-surface violation.** Attempt 6 alone (0.5615). It reached the target and held both perturbations, but ran to a 204.09 s qualifying budget with `per_step_cost_ratio` 1.3778 and also tripped `C-API-SURFACE`. It is the worst of the scoring attempts and combines both penalties: long budget and lost conformance.

**Class D — non-converging long runs that hit the ~1690 s ceiling.** Attempts 3, 7, 9, 10, 12, 15 and 16, all reward 0.0000, all `zero_reason_code` 4. Wall clock in this class is 1690.45–1692.97 s — a band under 2.6 s wide across seven independent runs, which is the signature of a hard time ceiling being struck rather than of seven different algorithms happening to be slow. In every one of them `conformance_fraction` is 0.0, `primary_target_reached` is 0, `qualifying_budget` is `not-measured`, and both perturbation units failed. `compute_efficiency` in this class is high (0.9033–1.0) and `per_step_cost_ratio` is low (0.7237–0.8901), which shows cheap fast steps are not the binding constraint — these runs were efficient per step and still never crossed the threshold before the ceiling. This class was entered seven separate times and produced 0.0000 every time.

# 3. Checks that failed

**`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction". Failed 7 times** (attempts 3, 7, 9, 10, 12, 15, 16). This is the single most repeated finding in the record. Seven attempts, presumably differing from one another in their training code, all failed this identical check with the identical reason; whatever was changed between those seven attempts is not what is causing this failure. The common measurable property is the ~1690 s wall clock, not any per-step quality metric.

**`C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists". Failed 7 times**, in exactly the same seven attempts. This is a consequence check, not an independent one: it fires because `C-TARGET-REACHED` produced no qualifying row for a budget position to be measured against. Fixing `C-TARGET-REACHED` should clear it; targeting it directly is meaningless.

**`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed 7 times**, again the same seven attempts, and again with 0 of 2 every time — never 1 of 2. The perturbations fail as a block with the primary run, not independently of it.

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions". Failed 2 times** (attempts 1 and 6). Both times `rule_conformance` dropped to 0.8571 (six of seven rules) and `task_pass` went to 0 even though `primary_target_reached` was 1, `conformance_fraction` was 1.0 and both perturbations held. Whatever was changed between attempt 1 and attempt 6 is not what is causing this check to fail: the reason string is byte-identical across both. The fix is structural and specific — the submission module must contain nothing at module scope except imports, constant assignments, and permitted definitions (functions/classes). Any top-level call, top-level loop, top-level `print`, top-level conditional, or `if __name__ == "__main__"`-style execution block, or any computation performed at import time, trips it. Every one of the nine attempts that scored above 0.69 had this check clean, and attempt 1 shows the cost directly: 25.46 s budget, target reached, perturbations held, and still only 0.7684 because of this one check.

# 4. Ruled-out directions

**Anything that lands in Class D — the non-converging ~1690 s run.** Ruled out because it was entered seven times (attempts 3, 7, 9, 10, 12, 15, 16) and returned reward 0.0000 every single time, with the identical triple of failed checks each time. Re-entering this class without changing the thing that prevents the threshold from being crossed is neither exploring nor exploiting; that is precisely what the run of attempts 9, 10, 12, 15 and 16 did after attempts 3 and 7 had already demonstrated the outcome. Seven zeros with the same three check identifiers is a settled result, not noise.

**Optimising `per_step_cost_ratio` or `compute_efficiency` as the route to crossing the threshold.** Ruled out by the Class D numbers themselves: those runs achieved `compute_efficiency` up to 1.0 and `per_step_cost_ratio` as low as 0.7237 — better on both metrics than the 0.9128-scoring attempt 5 (0.7728 and 0.9887) — and still scored 0.0000. Cheap steps do not buy threshold crossing.

**Letting the qualifying budget grow past ~100 s in exchange for anything.** Ruled out by the monotone trend inside Class B and by Class C: 50.03 s → 0.8719, 71.31 s → 0.8451, 73.62 s → 0.8385, 78.14 s → 0.7551, 99.74 s → 0.6955, 204.09 s → 0.5615. Longer budgets have never once bought a higher reward.

**Leaving any module-level execution in the submission.** Ruled out by attempts 1 and 6: both reached the target and held both perturbations and both were capped at `task_pass` 0 and `rule_conformance` 0.8571 by `C-API-SURFACE`. Attempt 1 had a top-class 25.46 s budget and still lost roughly 0.14 of reward against attempt 5's comparable budget.

**Running extra work after the qualifying row is found.** Suggested as costly by attempt 8, the only record where wall clock (151.50 s) far exceeds the qualifying budget (78.14 s); its 0.7551 is below every other clean attempt with a comparable qualifying budget (attempt 2 at 73.62 s scored 0.8385, attempt 13 at 71.31 s scored 0.8451). Treat post-qualification work as pure cost.

# 5. Open leads

**Reproduce Class A and stop there.** The target to beat is attempt 5's 0.9128: clean checks, `primary_target_reached` 1, both perturbations held, qualifying budget 25.34 s, `per_step_cost_ratio` 0.9887, `compute_efficiency` 0.7728. Attempt 11 shows the shape is reproducible (25.35 s, 0.8980), so a ~25 s conformant convergence is a stable regime rather than a lucky run. The first job of the next attempt is to land in this regime again.

**Attack `per_step_cost_ratio` while holding the ~25 s budget.** This is the clearest unexploited combination in the data. Attempt 4 demonstrated that `per_step_cost_ratio` 0.7115 and `compute_efficiency` 1.0 are achievable, but it paid a 50.03 s budget for them (0.8719). Attempts 5 and 11 achieved the 25.3 s budget but at ratios of 0.9887 and 1.0502. Between the two ~25 s runs, the one with the lower ratio (attempt 5, 0.9887) scored higher than the one with the higher ratio (attempt 11, 1.0502) at essentially identical budget — a 0.0148 reward difference tracking the ratio difference. No record has ever combined a ~25 s qualifying budget with a sub-0.8 `per_step_cost_ratio`; that is the specific untried point and the most likely way past 0.9128.

**Guarantee `C-API-SURFACE` by construction.** Before anything else, structure the file so that module scope contains only imports, constant assignments, and function/class definitions — no top-level calls, no top-level control flow, no import-time computation, no main-guard execution block. This check has cost two attempts their `task_pass` and is fully deterministic, so it is a free fix rather than an experiment.

**Cap the run so Class D cannot recur.** Since every zero shares the ~1690 s ceiling, the algorithm should be shaped so it cannot run open-endedly: converge and qualify early, and do not let a configuration that has not crossed the threshold by a small multiple of 25 s continue burning to the ceiling. A run that qualifies at 25 s and then stops scores ~0.91; a run that never qualifies scores 0.0000 regardless of how efficient its steps were.

**On the held-out runs.** Two perturbation kinds are declared in every record: one of kind `held_out_variant` and one of kind `seed`. Across the sixteen records, the nine attempts that reached the primary target had both kinds reach their thresholds with no failed checks — 18 of 32 units held. The seven zero attempts had both kinds fail, each on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` — 14 of 32 units failed, split evenly, 7 failures of kind `held_out_variant` and 7 of kind `seed`. In aggregate, neither kind has ever failed while the other held, and neither kind has ever failed while the primary run succeeded. There is no evidence of a perturbation-specific weakness: the held-out runs track the primary run exactly, so hardening against variant or seed sensitivity is not indicated by anything measured — making the primary run qualify is sufficient to make both kinds hold.

**Call: exploit.** Class A has scored twice (0.9128 and 0.8980) and its known deficiency — `per_step_cost_ratio` near or above 1.0 — has a demonstrated remedy from Class B (attempt 4's 0.7115). The right move is to rebuild the ~25 s conformant convergence, keep module scope free of executable statements so `C-API-SURFACE` holds, and drive `per_step_cost_ratio` down without letting the qualifying budget drift upward. Exploring a structurally different idea is not warranted: the structurally different things already tried are the Class D non-converging runs, and they have produced seven consecutive 0.0000s.
