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

    All 13 attempts since have scored lower than it.
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
  13 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

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

All eighteen records carry `measurement_status: "measured"`, so every one has a reward. Listed worst to best:

- **Attempt 3 — reward 0.0000.** Wall clock 1692.5 s; `qualifying_budget` not measured; zero_reason_code 4.
- **Attempt 7 — reward 0.0000.** Wall clock 1692.2 s; zero_reason_code 4.
- **Attempt 9 — reward 0.0000.** Wall clock 1693.0 s; zero_reason_code 4.
- **Attempt 10 — reward 0.0000.** Wall clock 1691.0 s; zero_reason_code 4.
- **Attempt 12 — reward 0.0000.** Wall clock 1690.4 s; zero_reason_code 4.
- **Attempt 15 — reward 0.0000.** Wall clock 1690.5 s; zero_reason_code 4.
- **Attempt 16 — reward 0.0000.** Wall clock 1691.5 s; zero_reason_code 4.
- **Attempt 6 — reward 0.5615.** Target reached (`primary_target_reached` 1.0) but `task_pass` 0.0, `rule_conformance` 0.8571, qualifying budget 204.09 s. Worse than earlier attempts.
- **Attempt 14 — reward 0.6955.** Clean conformance, qualifying budget 99.74 s. Worse than the best at the time.
- **Attempt 8 — reward 0.7551.** Clean conformance, qualifying budget 78.14 s, wall clock 151.50 s. Worse than the best at the time.
- **Attempt 1 — reward 0.7684.** First measured attempt. Qualifying budget 25.46 s — among the fastest ever recorded — but `rule_conformance` 0.8571 and `task_pass` 0.0 because of a failed check.
- **Attempt 17 — reward 0.7919.** Clean conformance, qualifying budget 73.80 s. Worse than earlier attempts.
- **Attempt 2 — reward 0.8385.** Clean conformance, qualifying budget 73.62 s. Better than every earlier attempt at the time.
- **Attempt 13 — reward 0.8451.** Clean conformance, qualifying budget 71.31 s. Worse than an earlier attempt.
- **Attempt 4 — reward 0.8719.** Clean conformance, qualifying budget 50.03 s, `compute_efficiency` 1.0. Better than every earlier attempt at the time.
- **Attempt 18 — reward 0.8794.** Clean conformance, qualifying budget 49.33 s. Worse than an earlier attempt.
- **Attempt 11 — reward 0.8980.** Clean conformance, qualifying budget 25.35 s. Worse than an earlier attempt.
- **Attempt 5 — reward 0.9128.** Clean conformance, `task_pass` 1.0, both perturbations held, qualifying budget 25.34 s, `per_step_cost_ratio` 0.9887, `compute_efficiency` 0.7728.

**Attempt 5 holds the highest reward, 0.9128. That is the mark to beat.** No record is unmeasured; no record should be read as a missing measurement.

The clearest regularity across measured, target-reaching attempts is that reward falls as `qualifying_budget` (time to the qualifying evaluation row) rises: ~25.3 s → 0.9128 / 0.8980; ~49–50 s → 0.8794 / 0.8719; ~71–74 s → 0.8451 / 0.8385 / 0.7919; ~78 s → 0.7551; ~100 s → 0.6955; ~204 s → 0.5615 (that last also carrying a conformance penalty). Time-to-qualify is not the whole story: attempts 5 and 11 sat within 0.01 s of each other yet differed by 0.0148 reward, and attempts 2 and 17 sat within 0.2 s of each other yet differed by 0.0466, so a second quality/margin term exists on top of speed. Note also that `compute_efficiency` alone does not drive reward — attempt 4 scored a perfect 1.0 on it and still finished below attempt 5, which scored 0.7728 there.

# 2. Approach classes tried

Only the harness metrics are available, not the source of each submission, so these classes are grouped by their measured signatures; the grouping is an inference from budget, conformance and convergence behaviour.

**Class A — fast-qualifying configurations that cross the target at the earliest evaluation point (attempts 1, 5, 11).** All three landed with a qualifying budget of 25.34–25.46 s, tightly clustered, which strongly suggests a floor set by the harness's first (or earliest usable) evaluation checkpoint rather than by anything the submission chose. Both attempts in this class with clean conformance (5 and 11) produced the two highest rewards on record, 0.9128 and 0.8980. The third (attempt 1) reached the target just as fast but lost reward to a conformance failure. This is the only class that has ever exceeded 0.89.

**Class B — mid-budget qualifying configurations (attempts 2, 4, 8, 13, 14, 17, 18).** Qualifying budgets of 49.33, 50.03, 71.31, 73.62, 73.80, 78.14 and 99.74 s, all with `rule_conformance` 1.0, `task_pass` 1.0, `validity` 1.0, both perturbations held. Rewards 0.6955–0.8794, monotone-ish in budget. This class is safe — it has never failed a check — but it has never reached attempt 5's mark. Attempt 8 is worth flagging separately: its qualifying budget was 78.14 s but its wall clock was 151.50 s, roughly double, meaning it kept spending time after the qualifying row; that extra spend bought nothing and it scored 0.7551.

**Class C — long-running, non-converging configurations (attempts 3, 7, 9, 10, 12, 15, 16).** Seven attempts, every one running 1690.4–1693.0 s — a band of under 2.6 s across seven runs, which reads as a hard wall-clock cap being hit rather than a natural stopping point. None of them produced a single evaluation row crossing the threshold in the declared direction. All seven scored 0.0000 with zero_reason_code 4. Their `per_step_cost_ratio` values (0.7237–0.8901) and `compute_efficiency` values (0.9033–1.0) were often *better* than the scoring attempts', which is the trap: these configurations were cheap per step and efficient, and simply never converged inside the budget. Cheapness per step was not the binding constraint.

**Class D — submissions with module-level statements at import time (attempts 1 and 6).** These are cross-cutting rather than a training strategy: attempt 1 is otherwise a Class A run and attempt 6 an especially slow Class B-style run (204.09 s, `per_step_cost_ratio` 1.3778). Both reached the primary target and held both perturbations, but both were docked to `rule_conformance` 0.8571 (6 of 7) and `task_pass` 0.0.

# 3. Checks that failed

**C-API-SURFACE — "module-level statements outside imports, constants, and permitted definitions".** Failed in attempts 1 and 6: **two failures**. This is the finding that matters most among the conformance checks. Attempts 1 and 6 are otherwise very different runs — one qualified in 25.46 s, the other in 204.09 s, with `per_step_cost_ratio` 1.0639 versus 1.3778 — so whatever was changed in the training strategy between them is *not* what causes this check to fail. The cause is structural: the submission file executes statements at module scope that are neither imports, nor constant assignments, nor permitted definitions (functions/classes). Both times the check fired, `rule_conformance` dropped from 1.0 to 0.8571 and `task_pass` dropped to 0.0 even though `primary_target_reached` was 1.0 and both perturbations held. Attempt 1 reached the target at essentially the same speed as attempt 5 (25.46 s vs 25.34 s) yet scored 0.7684 against 0.9128 — a gap of about 0.144 attributable to this check alone. Fixing it costs nothing in compute and is worth roughly that much reward.

**C-TARGET-REACHED — "no evaluation row crosses the threshold in the declared direction".** Failed in attempts 3, 7, 9, 10, 12, 15 and 16: **seven failures**. This is the single most repeated check failure on record and it is the direct cause of every 0.0000. Seven different submissions were changed between these runs and the check kept failing identically, so whatever was varied across them is not what is causing it; the common factor is that the run never gets the metric across the threshold before the ~1690 s cap.

**C-BUDGET-RESPECTED — "no qualifying row, so no budget position exists".** Failed in the same seven attempts: **seven failures**. This is downstream of C-TARGET-REACHED, not independent — with no qualifying row there is no budget position to score, and `qualifying_budget` is reported as not-measured for exactly those seven. Fixing C-TARGET-REACHED clears this one.

**C-PERTURBATION-REACHED — "0 of 2 declared perturbations reached their own threshold inside their own budget".** Failed in the same seven attempts: **seven failures**, always with the count 0 of 2. Also downstream: when the primary run fails to converge, both held-out runs fail with it.

No other check has ever failed. `validity` was 1.0 and `red_line_crossed` 0.0 in all eighteen records — nothing has ever tripped a red line or been ruled invalid.

# 4. Ruled-out directions

**Leaving module-level executable statements in the submission file.** Ruled out by two C-API-SURFACE failures (attempts 1, 6), each costing `task_pass` outright and about a seventh of `rule_conformance`. Attempt 1 demonstrates the cost precisely: fastest-tier convergence, 0.7684, versus 0.9128 for an equally fast run without the violation. Everything that must run has to live inside a function or class body; module scope gets imports, constant assignments and definitions only.

**Any configuration that does not cross the threshold well before the ~1690 s cap.** Ruled out seven times over with reward 0.0000 each time. There is no partial credit here: `conformance_fraction` goes to 0.0, `qualifying_budget` is not measured, and both perturbation runs fail with the primary. Note plainly that earlier work repeated this outcome seven separate times — attempts 3, 7, 9, 10, 12, 15 and 16 all scored zero for the identical reason, and re-running a long-horizon configuration without changing what makes it converge is neither exploiting nor exploring.

**Optimising `per_step_cost_ratio` or `compute_efficiency` as the objective.** Ruled out because the zero-scoring class had the best values on both: `per_step_cost_ratio` down to 0.7237 and `compute_efficiency` up to 1.0 among attempts that scored 0.0000, while the best-scoring attempt 5 had 0.9887 and 0.7728 respectively. Attempt 4 hit `compute_efficiency` 1.0 and still finished 0.0409 below attempt 5. Cheap steps that never converge are worthless; the metric that tracks reward is time-to-qualifying-row.

**Continuing to train past the qualifying row.** Ruled out by attempt 8, whose wall clock (151.50 s) was nearly twice its qualifying budget (78.14 s) for a reward of 0.7551. The extra half of the run bought no reward. Stop as soon as the target is crossed.

**Mid-budget settling in the 70–205 s band.** Ruled out as a path to the top: seven such runs (attempts 2, 6, 8, 13, 14, 17) produced 0.5615–0.8451 and none approached 0.9128. The band is safe but capped.

# 5. Open leads

**Reproduce the attempt-5 profile exactly and treat it as the base.** Its signature: qualifying budget 25.34 s, `per_step_cost_ratio` 0.9887, `compute_efficiency` 0.7728, `rule_conformance` 1.0, `task_pass` 1.0, both perturbations held, reward 0.9128. Attempt 11 reproduced the timing (25.35 s) but scored 0.8980, so the timing alone is not sufficient — something about attempt 5's model quality or margin at the qualifying row was better. Whatever is written next should aim at the 25.3 s tier first and then at margin.

**Treat ~25.3 s as a hard floor and stop chasing it.** Three separate attempts (1, 5, 11) landed within 0.12 s of each other at 25.34–25.46 s. That clustering is very unlikely to be a coincidence of three different configurations and almost certainly marks the earliest evaluation row the harness will accept. Further speed work below that line probably yields nothing; the remaining headroom above 0.9128 is most likely in the secondary quality/margin term, not in shaving seconds.

**Push the margin at the first qualifying checkpoint.** Since two runs at identical budget differed by 0.0148 reward, and two runs at ~73.7 s differed by 0.0466, the reward carries a component beyond speed. The lead is to reach the same first checkpoint with a better metric value — stronger initialisation, a higher effective learning rate early, better preprocessing or a slightly larger effective batch — anything that improves the value at the first evaluation without pushing the evaluation later.

**Guarantee C-API-SURFACE before anything else.** Before submitting, confirm the module body contains only imports, constant assignments, and function/class definitions. No prints, no seed-setting calls, no device selection, no configuration objects being constructed, no `if __name__` side effects at import — move all of it inside the entry-point function. This is a free ~0.14 recovery on a fast run and it has already been paid for twice.

**Bound the run explicitly so C-TARGET-REACHED never fails.** Add an internal stopping discipline: fixed, modest step count sized to finish far under the cap, plus an early exit the moment the target metric is crossed in the declared direction. The seven zero-scoring attempts all ran to the cap; a submission that cannot reach the threshold at its chosen horizon should be structurally impossible rather than merely unlikely.

**Held-out run behaviour is not a separate problem.** Across all eighteen records there were two declared perturbation units per attempt, of kinds `held_out_variant` and `seed`. In aggregate, 36 perturbation runs: 22 reached their threshold (all in the eleven attempts whose primary run also reached), and 14 did not (the seven attempts whose primary run failed). By kind: the `held_out_variant` runs reached in 11 of 18 attempts, and the `seed` runs reached in 11 of 18 attempts — identical rates. Every failing run of either kind failed on C-TARGET-REACHED and C-BUDGET-RESPECTED, never on anything else, and never independently of the primary run. There is no evidence of a generalisation or seed-sensitivity problem: whenever the primary converged, both kinds converged. So robustness work aimed specifically at held-out variants or at seed variance is not indicated by anything measured; making the primary run converge fast and cleanly is sufficient to carry both kinds.

**Call: exploit.** The scoring approach has clear, unexhausted headroom and one identified free win. Take the Class A fast-qualifying configuration that produced 0.9128, keep the module surface clean so C-API-SURFACE cannot fire, keep an early exit so C-TARGET-REACHED cannot fire, and spend the remaining effort on improving the metric value at the ~25.3 s checkpoint rather than on a structurally new idea. Explicitly do not re-run a long-horizon configuration; that has scored 0.0000 seven times for the same reason and repeating it without changing convergence speed changes nothing.
