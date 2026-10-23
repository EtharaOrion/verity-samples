# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 25 -- reward 0.9130, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All five attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4        0.8719   1.000             2 of 2         yes             50                
  5        0.9128   1.000             2 of 2         yes             25                
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
  24       0.8979   1.000             2 of 2         yes             25                
  25 *     0.9130   1.000             2 of 2         yes             25                
  26       0.0000   1.000             0 of 2         no              --                
  27       0.7552   0.857             2 of 2         yes             25                
  28       0.8841   1.000             2 of 2         yes             25                
  29       0.9128   1.000             2 of 2         yes             25                
  30       0.8775   1.000             2 of 2         yes             49                

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
  25 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 5 -- reward 0.9128, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 28 -- reward 0.8841, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 29 -- reward 0.9128, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 30 -- reward 0.8775, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 49
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (1, 6, 27). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 10 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22, 26). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# Summary for the next attempt

## 1. Results so far

Thirty graded records, all with `measurement_status: measured`; every one carries a reward. Listed worst to best.

**Scored zero (ten attempts, identical failure signature):** attempts 3, 7, 9, 10, 12, 15, 16, 21, 22 and 26 each scored **0.0000**, with `zero_reason_code: 4`, `conformance_fraction: 0.0`, `task_pass: 0.0`, `primary_target_reached: 0.0` and `qualifying_budget` reported as `not-measured`. Every one of these ran for essentially the same wall clock: 1690.3, 1690.4, 1690.5, 1690.9, 1691.0, 1691.5, 1691.6, 1692.2, 1692.5, 1692.97 seconds. Note that `validity` was 1.0 and `rule_conformance` was 1.0 in all ten — the code was accepted, it simply never produced a qualifying row.

Then, ascending by reward:

- Attempt 6 — **0.5615** (worse than an earlier attempt). `qualifying_budget` 204.09 s, `per_step_cost_ratio` 1.3778, `compute_efficiency` 0.6091, `rule_conformance` 0.8571, `task_pass` 0.0, failed C-API-SURFACE.
- Attempt 8 — **0.7551** (worse than an earlier attempt). `qualifying_budget` 78.14 s while `wall_clock_sec` was 151.50 s, `per_step_cost_ratio` 1.0291, clean checks, `task_pass` 1.0.
- Attempt 27 — **0.7552** (worse than an earlier attempt). `qualifying_budget` 25.26 s — as fast as the best attempts — but failed C-API-SURFACE, `rule_conformance` 0.8571, `task_pass` 0.0.
- Attempt 1 — **0.7684** (first measured attempt). `qualifying_budget` 25.46 s, failed C-API-SURFACE, `rule_conformance` 0.8571, `task_pass` 0.0.
- Attempt 17 — **0.7919** (worse than an earlier attempt). 73.80 s, `per_step_cost_ratio` 0.7318, clean.
- Attempt 2 — **0.8385** (better than every earlier attempt at the time). 73.62 s, `per_step_cost_ratio` 0.9162, clean, `task_pass` 1.0.
- Attempt 13 — **0.8451** (worse than an earlier attempt). 71.31 s, `per_step_cost_ratio` 1.0266, clean.
- Attempt 20 — **0.8661** (worse than an earlier attempt). 62.46 s, `compute_efficiency` 1.0, `per_step_cost_ratio` 0.6145, clean.
- Attempt 4 — **0.8719** (better than every earlier attempt at the time). 50.03 s, `compute_efficiency` 1.0, `per_step_cost_ratio` 0.7115, clean.
- Attempt 23 — **0.8768** (worse than an earlier attempt). 49.67 s, `per_step_cost_ratio` 0.9384, clean.
- Attempt 30 — **0.8775** (worse than an earlier attempt). 49.14 s, `per_step_cost_ratio` 0.7406, clean.
- Attempt 18 — **0.8794** (worse than an earlier attempt). 49.33 s, `per_step_cost_ratio` 0.9260, clean.
- Attempt 28 — **0.8841** (worse than an earlier attempt). 24.62 s — the lowest qualifying budget of any record — `compute_efficiency` 0.9772, `per_step_cost_ratio` 0.6818, clean.
- Attempt 24 — **0.8979** (worse than an earlier attempt). 25.37 s, `per_step_cost_ratio` 1.1078, clean.
- Attempt 11 — **0.8980** (worse than an earlier attempt). 25.35 s, `per_step_cost_ratio` 1.0502, clean.
- Attempt 19 — **0.9121** (worse than an earlier attempt). 45.81 s, `compute_efficiency` 0.9345, `per_step_cost_ratio` 0.7669, clean.
- Attempt 29 — **0.9128** (worse than an earlier attempt). 25.33 s, `compute_efficiency` 0.6950, `per_step_cost_ratio` 0.9590, clean.
- Attempt 5 — **0.9128** (better than every earlier attempt at the time). 25.34 s, `compute_efficiency` 0.7728, `per_step_cost_ratio` 0.9887, clean.
- Attempt 25 — **0.9130** (better than every earlier attempt). 25.32 s, `compute_efficiency` 0.8277, `per_step_cost_ratio` 0.8726, clean, `task_pass` 1.0, both perturbations held.

**Attempt 25, at reward 0.9130, holds the highest reward and is the one to beat.** Attempts 5 and 29 sit at 0.9128 and attempt 19 at 0.9121 — statistically indistinguishable neighbours, so the top of the field is a plateau of roughly 0.912–0.913 rather than a single lucky point. Everything after attempt 25 (attempts 26 through 30: 0.0000, 0.7552, 0.8841, 0.9128, 0.8775) is marked `worse_than_an_earlier_attempt`; the recent work has been going backwards or sideways, not forwards, and that should be stated plainly rather than read as progress.

## 2. Approach classes tried

The records give measured terms only, not source, so the classes below are grouped by their measured signature — budget band, conformance, and failure mode. Two records that failed the same way are one entry.

**Class A — fast conformant solver, ~24–26 s qualifying budget.** Attempts 5, 11, 24, 25, 28, 29. All clean, `task_pass` 1.0, both perturbations held. Rewards 0.8841, 0.8979, 0.8980, 0.9128, 0.9128, 0.9130. This class contains the best result and five of the six highest scores. Within the class, `compute_efficiency` ranged 0.6950–0.9772 and `per_step_cost_ratio` 0.6818–1.1078, and the ordering of rewards does **not** follow either term monotonically: attempt 28 had the lowest budget of all (24.62 s) and the best per-step ratio in the class (0.6818) yet scored 0.8841, below attempt 25's 0.9130 at 25.32 s. That spread of ~0.029 at essentially equal budget is the signature of a residual quality/margin term in the reward that the supplied fields do not decompose.

**Class B — mid-budget conformant solver, ~45–63 s.** Attempts 4, 18, 19, 20, 23, 30. All clean, `task_pass` 1.0. Rewards 0.8661, 0.8719, 0.8768, 0.8775, 0.8794, 0.9121. Attempt 19 (45.81 s, 0.9121) is the outlier that nearly matches Class A, which again says budget is not the whole story; attempt 20 achieved `compute_efficiency` 1.0 and the lowest per-step ratio on record (0.6145) yet scored only 0.8661.

**Class C — long-budget conformant solver, ~71–100 s.** Attempts 2, 8, 13, 14, 17. All clean, `task_pass` 1.0. Rewards 0.6955 (attempt 14, 99.74 s), 0.7551 (attempt 8), 0.7919, 0.8385, 0.8451. Attempt 8 is instructive: its `wall_clock_sec` was 151.50 s but its `qualifying_budget` was 78.14 s, and its reward (0.7551) tracks the other ~73–78 s records, not the 151 s wall clock. The graded budget term appears to be the qualifying budget, not raw wall clock.

**Class D — variants carrying module-level statements.** Attempts 1, 6, 27. Each reached the primary target and held both perturbations, yet each failed C-API-SURFACE, took `rule_conformance` 0.8571 (six of seven), and had `task_pass` forced to 0.0. Rewards 0.7684, 0.5615, 0.7552. Attempt 27 is the sharpest measurement of the cost: at 25.26 s it was in the Class A budget band, where clean runs score 0.884–0.913, and it scored 0.7552. The violation costs roughly 0.14–0.16 of reward at equal budget.

**Class E — runaway configurations that never cross the threshold.** Attempts 3, 7, 9, 10, 12, 15, 16, 21, 22, 26 — ten records, one third of all graded work, all 0.0000. Their `compute_efficiency` values were often excellent (1.0 on attempts 7 and 9; 0.9033–0.9853 elsewhere) and `per_step_cost_ratio` was consistently good (0.6826–0.8901), so the per-step machinery was not slow. What failed is that no evaluation row ever crossed the threshold before the run ended at ~1690 s. The near-identical wall clocks (a 2.7-second spread across ten runs) point to a hard time cap being hit rather than ten independent convergence failures.

## 3. Checks that failed

**C-API-SURFACE** — "module-level statements outside imports, constants, and permitted definitions." Failed in attempts 1, 6 and 27: **three separate times**, with the identical verifier reason each time. Whatever was changed to the learning algorithm between those three attempts is not what causes this check to fail. It is a structural property of the submission file — executable statements sitting at module scope — and it survives independently of the training approach, because the target and both perturbations were still reached in all three of those runs. The next attempt must place every statement inside a function or other permitted definition; only imports, constants and definitions may sit at module level. This check alone converted an otherwise-Class-A run (attempt 27) into a 0.7552.

**C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction." Failed in attempts 3, 7, 9, 10, 12, 15, 16, 21, 22 and 26: **ten times**. Whatever was varied between those ten attempts is not what causes this check to fail; they differ in `compute_efficiency` (0.9033 to 1.0) and `per_step_cost_ratio` (0.6826 to 0.8901) yet all land on exactly the same three failed checks and the same ~1690 s wall clock.

**C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists." Failed in the same ten attempts, **ten times**. This is downstream of C-TARGET-REACHED, not an independent problem: with no row crossing the threshold there is no budget position to evaluate, which is why `qualifying_budget` is `not-measured` in those records.

**C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget." Failed in the same ten attempts, **ten times**, always 0 of 2.

## 4. Ruled-out directions

- **Leaving any executable statement at module scope.** Ruled out by three C-API-SURFACE failures (attempts 1, 6, 27) with the same verbatim reason. It zeroes `task_pass` and caps `rule_conformance` at 0.8571 even when the target and both perturbations are reached, costing ~0.14–0.16 reward at matched budget. There is no upside anywhere in the data.

- **Whatever configuration produces the ~1690 s runaway.** Ruled out by ten 0.0000 records. Repeating it without changing what makes no row cross the threshold is neither exploring nor exploiting, and that is precisely what the earlier work kept doing: the zeros are spread across attempts 3, 7, 9, 10, 12, 15, 16, 21, 22 and 26, i.e. they recurred throughout the run rather than being cleared early. Any candidate that risks this signature must carry a hard internal wall-clock guard that forces an evaluation row to be emitted well before the cap.

- **Buying accuracy with a longer budget.** Ruled out by the Class C results: 71–100 s budgets score 0.6955–0.8451, strictly below every Class A result. Attempt 14 at 99.74 s scored 0.6955, well under half the field. The reward penalises budget hard enough that no observed quality gain compensates.

- **Optimising `per_step_cost_ratio` as the lever.** Ruled out by counter-example. Attempt 20 achieved the best per-step ratio on record (0.6145) with `compute_efficiency` 1.0 and scored 0.8661; attempt 28 achieved 0.6818 at the lowest budget on record and scored 0.8841; meanwhile the best result, attempt 25, had a middling 0.8726, and attempts 5 (0.9887) and 29 (0.9590) with much worse per-step ratios scored 0.9128 each. Driving this term down does not move reward.

- **Treating raw wall clock as the graded cost.** Ruled out by attempt 8, whose 151.50 s wall clock scored like its 78.14 s `qualifying_budget` (0.7551, in line with the 73–78 s band) rather than like the 100 s+ band. Effort spent shaving non-qualifying wall clock is not rewarded; effort spent lowering the budget at which a row first qualifies is.

## 5. Open leads

- **Reproduce the Class A shape exactly and vary only the residual quality term.** The 24–26 s band contains six clean records spanning 0.8841 to 0.9130 — a 0.029 spread at essentially constant budget, constant conformance and both perturbations held. That spread is not explained by `compute_efficiency` or `per_step_cost_ratio`, so it is the margin by which the evaluation row clears the threshold, or the accuracy attained, that separates 0.884 from 0.913. Rebuild a ~25 s conformant solver and push on how far past the threshold the qualifying row lands, holding budget fixed.

- **Probe the 26–45 s gap, which no record occupies.** Attempt 19 scored 0.9121 at 45.81 s, only 0.0009 below the best, while everything else in Class B sat at 0.866–0.879. If a genuinely better-quality run exists at 30–40 s, it could beat 0.9130 by trading a little budget for a lot of margin. The data cannot rule this in or out because the band is empty.

- **Add a hard time guard as a standing safety property, not a tuning knob.** Ten zeros all share a ~1690 s terminus. A guard that forces evaluation rows to be written on a schedule — so that at least one qualifying row exists early — converts the entire Class E failure mode into a low-but-nonzero score. Even a poor qualifying row beats 0.0000, and this alone would have salvaged a third of the graded work.

- **Audit the file for module-level statements before submitting, mechanically.** The C-API-SURFACE reason is specific and checkable by inspection: only imports, constants, and definitions at module level. Given it has now bitten three times across otherwise-different approaches, treat this as a pre-flight checklist item independent of the algorithm.

- **On the perturbation runs.** Two are declared in every record, of kinds `held_out_variant` and `seed`. In aggregate across the thirty records there are sixty perturbation runs: forty reached their threshold and twenty did not. Broken down by kind, the `held_out_variant` runs reached in twenty records and failed in ten; the `seed` runs reached in twenty records and failed in ten. Crucially, neither kind has ever failed on its own — both kinds fail together, in exactly the ten records where the primary also failed, and always on C-TARGET-REACHED and C-BUDGET-RESPECTED. There is no evidence of a robustness gap specific to held-out variants or to seed changes; when the primary run works, both kinds hold, including in every C-API-SURFACE record. So the perturbations are not currently a distinct problem to solve, and no effort should be spent hardening against them separately.

**Call: exploit.** The approach that scored highest — the fast, fully conformant ~25 s solver of Class A — is the one to rebuild and improve, not to replace. Two failure modes are fully characterised and both are avoidable by construction: keep every statement out of module scope, and guarantee a qualifying evaluation row lands long before any time cap. With those two held, the whole remaining question is the residual quality margin that separates 0.884 from 0.913 inside an otherwise identical budget, plus the untested 30–45 s window that attempt 19's 0.9121 suggests may be viable. Explore is not yet warranted: the scoring approaches have plateaued only in the sense that recent attempts stopped beating attempt 25, while a third of all work was consumed by a repeated zero-scoring configuration whose cause was never removed — that budget is better spent on the shape that already scores.
