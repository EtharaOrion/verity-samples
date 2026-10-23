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

    All ten attempts since have scored lower than it.
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
  9 earlier attempt(s) are not detailed here; their measured row is above.

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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 6 attempts (3, 7, 9, 10, 12, 15). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 6 attempts (3, 7, 9, 10, 12, 15). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 6 attempts (3, 7, 9, 10, 12, 15). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# Summary for the next attempt

## 1. Results so far

Fifteen graded records, all with `measurement_status: "measured"` — every one carries a reward, including the six that scored exactly 0.0000. None of these is a missing measurement; they are measured zeros with `zero_reason_code: 4`.

Ordered worst to best by reward:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| = | 3 | 0.0000 | measured zero; wall clock 1692.52 s |
| = | 7 | 0.0000 | measured zero; wall clock 1692.21 s |
| = | 9 | 0.0000 | measured zero; wall clock 1692.97 s |
| = | 10 | 0.0000 | measured zero; wall clock 1690.96 s |
| = | 12 | 0.0000 | measured zero; wall clock 1690.45 s |
| = | 15 | 0.0000 | measured zero; wall clock 1690.48 s |
| 7 | 6 | 0.5615 | conformance 0.857 (C-API-SURFACE), 204.09 s |
| 8 | 14 | 0.6955 | clean, 99.74 s |
| 9 | 8 | 0.7551 | clean, qualifying budget 78.14 s but wall clock 151.50 s |
| 10 | 1 | 0.7684 | conformance 0.857 (C-API-SURFACE), 25.46 s |
| 11 | 2 | 0.8385 | clean, 73.62 s |
| 12 | 13 | 0.8451 | clean, 71.31 s |
| 13 | 4 | 0.8719 | clean, 50.03 s, compute_efficiency 1.0 |
| 14 | 11 | 0.8980 | clean, 25.35 s |
| 15 | **5** | **0.9128** | clean, 25.34 s — **highest reward; this is the one to beat** |

Attempt 5 (reward 0.9128) holds the high-water mark. Attempts 2, 4 and 5 were each `better_than_every_earlier_attempt` at the time they ran; everything after attempt 5 was `worse_than_an_earlier_attempt`. Stated plainly: attempts 6 through 15 all scored below attempt 5, and six of them (3, 7, 9, 10, 12, 15) collapsed to 0.0000. The trajectory after attempt 5 is regression, not progress — attempt 11 (0.8980) came closest and still fell short of 5, and attempts 13 (0.8451), 14 (0.6955) and 8 (0.7551) were substantially worse.

Secondary quantities worth carrying forward: `validity` was 1.0 in every record and `red_line_crossed` was 0.0 in every record, so nothing has ever been invalidated or tripped a red line. `compute_efficiency` does **not** track reward — attempt 4 scored 1.0 efficiency for reward 0.8719 while attempt 5 scored 0.7728 efficiency for the best reward 0.9128, and the zero-scoring attempts 7 and 9 both reported efficiency 1.0. Do not optimise that number.

## 2. Approach classes tried

The records supply measured terms only, not source, so these classes are grouped by their measurable signature — budget consumed, conformance, and which checks held.

**Class A — conformant, fast, ~25 s budget.** Attempts 5 (0.9128), 11 (0.8980). Full conformance (`rule_conformance` 1.0, `conformance_fraction` 1.0), `task_pass` 1.0, `primary_target_reached` 1.0, both perturbation units held, qualifying budget 25.34 s and 25.35 s. This class produced the two best scores in the whole run. Within it, attempt 5 had `per_step_cost_ratio` 0.9887 and attempt 11 had 1.0502; the cheaper per-step figure went with the higher reward, and the near-identical wall clocks make per-step cost the only visible discriminator between them.

**Class B — conformant, mid-length budget, 50–100 s.** Attempts 4 (0.8719, 50.03 s), 13 (0.8451, 71.31 s), 2 (0.8385, 73.62 s), 8 (0.7551, budget 78.14 s / wall 151.50 s), 14 (0.6955, 99.74 s). All fully conformant, all passed the task and both perturbations. Reward falls monotonically as the budget lengthens across this class. Attempt 8 is the informative case: its qualifying budget (78.14 s) sits between attempts 2 and 14, but its total wall clock was 151.50 s — roughly double its qualifying budget, the only record where the two diverge — and its reward (0.7551) is worse than attempt 2's at a comparable budget. Total wall clock, not just the qualifying row's budget, appears to cost reward.

**Class C — conformant target but very long budget.** Attempt 6 (0.5615, 204.09 s, `per_step_cost_ratio` 1.3778). It reached the primary target and both perturbations held, but the long budget plus a conformance failure (below) put it near the bottom of the scoring records.

**Class D — module-level statements at import scope.** Attempts 1 (0.7684) and 6 (0.5615). Both reached the target and held both perturbations, but both were docked to `rule_conformance` 0.857 (6 of 7) and `task_pass` 0.0 by C-API-SURFACE. Attempt 1 ran at a 25.46 s budget — essentially the same speed profile as the best-scoring class A — yet scored 0.7684 rather than ~0.91. The conformance penalty alone is worth roughly 0.14 of reward at that speed.

**Class E — never reaches the threshold, runs to the ~1690 s ceiling.** Attempts 3, 7, 9, 10, 12, 15, all 0.0000. Every one ran 1690.4–1693.0 s wall clock, a band so tight across six independent records that it is almost certainly a hard time ceiling rather than six coincidentally similar runtimes. In all six, `rule_conformance` was 1.0 — the code was legal — but `conformance_fraction` was 0.0, `primary_target_reached` 0.0, `qualifying_budget` "not-measured", and no evaluation row ever crossed the threshold. This class was entered six separate times and never once produced a non-zero reward.

## 3. Checks that failed

**C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction". Failed in **6 records** at the primary level (attempts 3, 7, 9, 10, 12, 15) and in **12 perturbation units** (both units in each of those six). This is the single most frequent failure in the whole history. Whatever was varied between attempts 3, 7, 9, 10, 12 and 15 is *not* what causes this check to fail — six differently-authored submissions produced the identical triple of failures and the identical ~1690 s runtime. The common factor is the training procedure never converging to the threshold inside the ceiling, not any local detail that was edited between them.

**C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". Failed in the same **6 records** and the same **12 perturbation units**. This is strictly downstream of C-TARGET-REACHED: with no row crossing the threshold, there is no qualifying row to locate a budget in. It is not an independent problem and does not need an independent fix.

**C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed in the same **6 records**, at the primary level only. Also downstream: in every case the perturbation runs failed for the same reason the primary did.

**C-API-SURFACE** — "module-level statements outside imports, constants, and permitted definitions". Failed **2 times**, in attempts 1 and 6. Both of those attempts otherwise reached the target and held both perturbations; the check cost them `rule_conformance` (0.857 instead of 1.0) and `task_pass` (0.0 instead of 1.0). The two attempts differ enormously in every other respect — 25.46 s versus 204.09 s, per-step cost 1.0639 versus 1.3778 — so whatever changed between them is not what causes this check to fail. The cause is executable code sitting at module scope. Everything outside imports, constant assignments and permitted definitions must live inside a function or class body.

## 4. Ruled-out directions

**Any configuration that runs to the ~1690 s ceiling without crossing the threshold.** Tried six times (attempts 3, 7, 9, 10, 12, 15), scored 0.0000 every time on C-TARGET-REACHED / C-BUDGET-RESPECTED / C-PERTURBATION-REACHED. Repeating this shape without changing what stops convergence is neither exploration nor exploitation — and the record shows it was done six times. If a design cannot demonstrably cross the threshold in tens of seconds, it should not be submitted.

**Executable statements at module scope.** Ruled out by two C-API-SURFACE failures. Attempt 1 shows the cost directly: same ~25 s speed class as the best attempts, but 0.7684 instead of ~0.91 because conformance dropped to 0.857 and task_pass to 0.0.

**Long training budgets as a route to a better score.** Every conformant record with a budget above 50 s scored below every conformant record at ~25 s. The ordering is unbroken: 25.34 s → 0.9128, 25.35 s → 0.8980, 50.03 s → 0.8719, 71.31 s → 0.8451, 73.62 s → 0.8385, 78.14 s → 0.7551, 99.74 s → 0.6955, 204.09 s → 0.5615. More compute has never bought reward here.

**Letting total wall clock exceed the qualifying budget.** Attempt 8 is the only record where wall clock (151.50 s) diverged from qualifying budget (78.14 s), and it underperformed attempt 2 (0.8385 at 73.62 s) despite a similar qualifying budget. Extra work outside the qualifying run appears to be charged.

**Maximising `compute_efficiency`.** Ruled out as a proxy target: it hit 1.0 in attempt 4 (reward 0.8719) and in the zero-scoring attempts 7 and 9, while the best attempt 5 sat at 0.7728.

## 5. Open leads

**Reconstruct the attempt-5 profile as the baseline.** Target a fully conformant submission whose qualifying budget and total wall clock are both ≈25 s, with `primary_target_reached` 1.0, `task_pass` 1.0, and both perturbation units held. That combination has been achieved twice (attempts 5 and 11) and is the only region of the space that has ever exceeded 0.89.

**Reduce `per_step_cost_ratio` while holding wall clock at ~25 s.** Attempts 5 and 11 have nearly identical budgets (25.34 vs 25.35 s) but rewards 0.9128 and 0.8980; the visible difference is per-step cost 0.9887 versus 1.0502, with the cheaper one scoring higher. Attempt 4 demonstrates a per-step ratio as low as 0.7115 is attainable, but it did so at a 50 s budget. Getting attempt-4-class per-step cost at attempt-5-class wall clock is the most concrete unexplored point, and is the clearest candidate for beating 0.9128.

**Try to shorten below 25 s while still crossing the threshold.** No record has ever qualified faster than 25.34 s. Since reward falls monotonically with budget across every conformant record, the region below 25 s is unmeasured and is where headroom would be if it exists. This must be balanced against the six-record evidence that failing to cross the threshold costs everything, so any shortening should be conservative and must preserve target attainment for both the seed run and the held-out-variant run.

**Guard the API surface explicitly before submitting.** All module-level content restricted to imports, constants, and function/class definitions; no top-level calls, no top-level prints, no top-level training invocation. Two prior attempts lost roughly 0.14 of reward to this alone.

**On the held-out runs.** Two perturbation units accompany every record, one of kind `held_out_variant` and one of kind `seed`; the identity of any individual run is not disclosed and no run can be tracked across records. Across all fifteen records that is 30 units: 18 reached their threshold and 12 did not. By kind, `held_out_variant` reached in 9 of 15 records and failed in 6; `seed` reached in 9 of 15 and failed in 6. Both kinds failed on C-TARGET-REACHED and C-BUDGET-RESPECTED, and in every single case they failed only in records where the primary run also failed on C-TARGET-REACHED. No perturbation unit of either kind has ever failed while the primary target was reached. The practical implication is that robustness across seeds and across the held-out variant has never been the binding constraint — convergence itself is. Fixing convergence has, historically, brought both kinds along with it.

**Call: exploit.** Attempt 5's approach class scored 0.9128 and its immediate neighbour attempt 11 scored 0.8980, so the class is live and has not been exhausted along its one visibly free dimension (per-step cost at fixed ~25 s wall clock). The structurally different ideas tried since — longer budgets and the six non-converging long runs — have all scored worse or zero. Rebuild the fast conformant trainer, keep every statement off module scope, hold the qualifying budget and total wall clock near 25 s, and push per-step cost down.
