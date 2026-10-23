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

    All eight attempts since have scored lower than it.
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

Thirteen attempts, all with `measurement_status: "measured"`. Every one therefore carries a reward. Listed worst to best:

- **Attempt 3 — reward 0.0000.** Wall clock 1692.52 s, `qualifying_budget` not measured, `primary_target_reached` 0, `zero_reason_code` 4. Worse than an earlier attempt.
- **Attempt 7 — reward 0.0000.** Wall clock 1692.21 s, same zero signature. Worse than an earlier attempt.
- **Attempt 9 — reward 0.0000.** Wall clock 1692.97 s, same zero signature. Worse than an earlier attempt.
- **Attempt 10 — reward 0.0000.** Wall clock 1690.96 s, same zero signature. Worse than an earlier attempt.
- **Attempt 12 — reward 0.0000.** Wall clock 1690.45 s, same zero signature. Worse than an earlier attempt.
- **Attempt 6 — reward 0.5615.** Wall clock 204.09 s, `rule_conformance` 0.8571, `task_pass` 0, one failed check. Worse than an earlier attempt.
- **Attempt 8 — reward 0.7551.** Qualifying budget 78.14 s but wall clock 151.50 s, no failed checks, `task_pass` 1. Worse than an earlier attempt.
- **Attempt 1 — reward 0.7684.** Wall clock 25.46 s, `rule_conformance` 0.8571, `task_pass` 0, one failed check. First measured attempt.
- **Attempt 2 — reward 0.8385.** Wall clock 73.62 s, clean, `task_pass` 1. Better than every earlier attempt at the time.
- **Attempt 13 — reward 0.8451.** Wall clock 71.31 s, clean, `task_pass` 1. Worse than an earlier attempt.
- **Attempt 4 — reward 0.8719.** Wall clock 50.03 s, clean, `compute_efficiency` 1.0. Better than every earlier attempt at the time.
- **Attempt 11 — reward 0.8980.** Wall clock 25.35 s, clean. Worse than an earlier attempt.
- **Attempt 5 — reward 0.9128.** Wall clock 25.34 s, `compute_efficiency` 0.7728, `per_step_cost_ratio` 0.9887, no failed checks, all perturbations held. **Attempt 5 holds the highest reward, 0.9128, and it is the one to beat.**

Note the ordering plainly: the last four graded records (10, 11, 12, 13) are all `worse_than_an_earlier_attempt`. Attempts 11 (0.8980) and 13 (0.8451) are below attempt 5 (0.9128), and attempts 10 and 12 produced 0.0000. Nothing since attempt 5 has improved on it. `red_line_crossed` is 0 and `validity` is 1.0 in every record, including the zeros.

# 2. Approach classes tried

The measured terms distinguish three classes. Records sharing a signature are one entry.

**Class A — conformant runs that converge quickly (attempts 2, 4, 5, 8, 11, 13).** `task_pass` 1, `rule_conformance` 1.0, `conformance_fraction` 1.0, no failed checks, both perturbation runs reached. All six scored between 0.7551 and 0.9128. Within this class reward tracks the qualifying budget almost perfectly and inversely: 25.34 s → 0.9128 (attempt 5), 25.35 s → 0.8980 (attempt 11), 50.03 s → 0.8719 (attempt 4), 71.31 s → 0.8451 (attempt 13), 73.62 s → 0.8385 (attempt 2), 78.14 s → 0.7551 (attempt 8). This is the only approach class that has ever scored above 0.5615, and it is where the best result lives.

**Class B — runs that reached the target but broke the API surface rule (attempts 1 and 6).** `primary_target_reached` 1, both perturbations reached, but `rule_conformance` 0.8571 (i.e. one rule of seven not held), `conformance_fraction` still 1.0, and `task_pass` forced to 0. Rewards 0.7684 and 0.5615. Attempt 1 ran in 25.46 s — essentially the same budget as the best-scoring attempt 5 — yet scored 0.7684 instead of 0.9128. That gap of roughly 0.14 is the price of the single failed check, holding budget constant. Attempt 6 combined the same failed check with a 204.09 s budget and a `per_step_cost_ratio` of 1.3778, giving the worst non-zero reward, 0.5615.

**Class C — long runs that never crossed the threshold (attempts 3, 7, 9, 10, 12).** Five records, all reward 0.0000, all `zero_reason_code` 4, all `primary_target_reached` 0, all `conformance_fraction` 0.0, `qualifying_budget` reported as not measured. Wall clocks were 1692.52, 1692.21, 1692.97, 1690.96 and 1690.45 s — a tight cluster just under 1693 s, consistent with these runs consuming the full allowed wall clock without ever producing a qualifying evaluation row. Notably `rule_conformance` was 1.0 in all five and `compute_efficiency` was high (0.9761–1.0), so these were rule-clean and cheap per step; what they failed to do was reach the target at all. Five separate attempts landed in this class, which is the largest single block of wasted work in the record.

# 3. Checks that failed

**C-API-SURFACE** — reason: "module-level statements outside imports, constants, and permitted definitions." Failed **twice**, in attempt 1 and attempt 6. Whatever was changed between attempts 1 and 6 is not what causes this check to fail: it reappeared unchanged across a submission whose budget went from 25.46 s to 204.09 s and whose `per_step_cost_ratio` went from 1.0639 to 1.3778. The fix is structural, not a matter of training configuration — the module must contain nothing at top level except imports, constants, and permitted definitions, with all executable work moved inside functions. Both times this check fired, `task_pass` was driven to 0 and `rule_conformance` to 0.8571 even though the target itself was reached and both perturbation runs held.

**C-TARGET-REACHED** — reason: "no evaluation row crosses the threshold in the declared direction." Failed **five** times, in attempts 3, 7, 9, 10 and 12. Five distinct submissions produced this identical failure, so whatever was varied between them is not what causes it.

**C-BUDGET-RESPECTED** — reason: "no qualifying row, so no budget position exists." Failed **five** times, in the same attempts 3, 7, 9, 10 and 12. This is downstream of C-TARGET-REACHED: with no row crossing the threshold there is no qualifying row to position against a budget. Fixing the target check should clear this one.

**C-PERTURBATION-REACHED** — reason: "0 of 2 declared perturbations reached their own threshold inside their own budget." Failed **five** times, in attempts 3, 7, 9, 10 and 12, always alongside the two checks above.

Aggregate: four distinct named checks have ever failed. The three-check bundle (C-TARGET-REACHED, C-BUDGET-RESPECTED, C-PERTURBATION-REACHED) always appears together and always with reward 0.0000. C-API-SURFACE appears alone and costs roughly 0.14 of reward without zeroing the run.

# 4. Ruled-out directions

Each perturbation record declares 2 units per attempt, one of kind `held_out_variant` and one of kind `seed`. Across 13 attempts that is 26 held-out runs.

- **By kind, `held_out_variant`:** 13 runs, 8 reached their threshold, 5 did not. Every failure was on **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**, and every one occurred in an attempt from Class C.
- **By kind, `seed`:** 13 runs, 8 reached their threshold, 5 did not. Identical failure pattern — **C-TARGET-REACHED** and **C-BUDGET-RESPECTED** — again confined to Class C attempts.
- **Aggregate:** 16 of 26 held-out runs reached; 10 did not, split evenly between the two kinds. `all_perturbations_held` was true in the eight scoring attempts and false in the five zeros.

The runs are not identified beyond their kind, so nothing here should be read as tracing one particular run across records. What the aggregate says is clear and kind-independent: **no perturbation run has ever failed while the primary run succeeded.** In all eight attempts where the primary target was reached, both kinds reached; in all five where it was not, neither kind reached. Perturbation robustness is therefore not a separate problem to solve — it is entirely determined by whether the method converges on the primary run at all. The failing kinds are `held_out_variant` and `seed` equally, and the check that stops them is C-TARGET-REACHED (with C-BUDGET-RESPECTED following from it).

The directions ruled out:

- **Any submission with executable statements at module level.** Ruled out by two independent C-API-SURFACE failures (attempts 1, 6). Attempt 1 shows this costs ~0.14 reward even when the run is otherwise as fast as the best attempt. There is no configuration of training that compensates.
- **Whatever training configuration produced the ~1690 s non-converging runs (attempts 3, 7, 9, 10, 12).** Ruled out by five separate zero-reward measurements with identical failed-check sets. Repeating this shape without changing what prevents a threshold crossing is not exploration and not exploitation — and the record shows earlier work did exactly that five times, spending roughly 8,459 seconds of wall clock for zero total reward. High `compute_efficiency` (up to 1.0) in these records is not evidence of progress; it coexists with `primary_target_reached` 0.
- **Spending more budget in hope of a better result.** Within the scoring class the relation is monotone and negative across six points: every increase in qualifying budget lowered reward. Attempt 4 reached `compute_efficiency` 1.0 at 50.03 s and still scored 0.8719, below attempt 5's 0.9128 at 25.34 s, so maximising `compute_efficiency` is not the same as maximising reward.
- **Letting total wall clock exceed the qualifying budget.** Attempt 8 is the only record where these differ (151.50 s wall clock against a 78.14 s qualifying budget) and it scored 0.7551, below attempt 2's 0.8385 at a comparable 73.62 s budget. Work performed after the qualifying row appears to be charged without benefit.

# 5. Open leads

- **Rebuild attempt 5's shape: clean module surface, converge in roughly 25 seconds.** Attempts 5 (0.9128) and 11 (0.8980) both qualified at ~25.34 s, and attempt 1 also qualified at 25.46 s but lost ~0.14 to C-API-SURFACE. The ~25 s band is where every high score sits. The gap between 5 and 11 at essentially identical budget (0.0148) is the residual worth chasing, and the differing `per_step_cost_ratio` values there — 0.9887 for attempt 5 versus 1.0502 for attempt 11 — are the only other term that separates them. A ratio at or just below 1.0 accompanied the best score.
- **Push the qualifying budget below 25 s while keeping the target crossed.** The fitted trend across the six scoring runs suggests reward continues to rise as budget falls. No attempt has yet qualified faster than 25.34 s; that is unexplored territory on the side the gradient points to. The risk is falling into Class C, so any reduction must be validated as still crossing the threshold before being submitted.
- **Treat C-API-SURFACE as a hard structural precondition.** Write every statement inside a function or permitted definition; leave only imports, constants and definitions at module scope. This is cheap and has twice cost a graded attempt its `task_pass`.
- **Do not build a separate mechanism for perturbation robustness.** All 16 successful held-out runs succeeded as a consequence of the primary run succeeding, across both `held_out_variant` and `seed` kinds. Effort belongs on primary convergence speed.
- **Keep total wall clock equal to the qualifying budget.** Avoid any post-qualification work, given attempt 8's penalty relative to attempt 2 at similar qualifying budget.

**Call: exploit.** Class A has scored six times and still has an unexplored direction that the measurements point at directly — the sub-25-second qualifying budget. The correct next move is to reconstruct the attempt 5 configuration exactly (clean module surface, ~25 s to threshold, `per_step_cost_ratio` near 1.0), confirm it reproduces at or near 0.9128, and then shave the budget. Exploration is not warranted: the scoring class has not stopped improving, and every structurally different thing tried so far either scored zero five times over or lost reward to a known, fixable check.
