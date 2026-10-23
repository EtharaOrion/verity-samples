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

    All five attempts since have scored lower than it.
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
  4 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 8 -- reward 0.7551, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 78
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.0000, worse than an earlier attempt
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

    attempt 10 -- reward 0.0000, worse than an earlier attempt
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 4 attempts (3, 7, 9, 10). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 4 attempts (3, 7, 9, 10). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 4 attempts (3, 7, 9, 10). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# Summary for the next attempt

All ten graded records carry `measurement_status: "measured"`, so every one of them has a real reward. None of them is an unmeasured record, and the four zeros below are genuine measured zeros (`zero_reason_code: 4`), not absent measurements. `validity` was 1.0 and `red_line_crossed` was 0.0 in every single record — nothing has ever tripped a validity or red-line condition.

## 1. Results so far

Worst to best by reward:

| Rank | Attempt | reward | Notes from its own terms |
|---|---|---|---|
| = worst | 3 | 0.0000 | wall_clock 1692.52 s, `qualifying_budget` not-measured, task_pass 0.0, conformance_fraction 0.0 |
| = worst | 7 | 0.0000 | wall_clock 1692.21 s, `qualifying_budget` not-measured, conformance_fraction 0.0 |
| = worst | 9 | 0.0000 | wall_clock 1692.97 s, `qualifying_budget` not-measured, conformance_fraction 0.0 |
| = worst | 10 | 0.0000 | wall_clock 1690.96 s, `qualifying_budget` not-measured, conformance_fraction 0.0 |
| 5 | 6 | 0.5615 | primary target reached, but rule_conformance 0.857, task_pass 0.0, wall_clock 204.09 s, per_step_cost_ratio 1.3778 |
| 6 | 8 | 0.7551 | fully conformant, task_pass 1.0, qualifying_budget 78.14 s but wall_clock 151.50 s |
| 7 | 1 | 0.7684 | primary target reached, rule_conformance 0.857, task_pass 0.0, wall_clock 25.46 s |
| 8 | 2 | 0.8385 | fully conformant, task_pass 1.0, wall_clock 73.62 s, per_step_cost_ratio 0.9162 |
| 9 | 4 | 0.8719 | fully conformant, task_pass 1.0, wall_clock 50.03 s, compute_efficiency 1.0, per_step_cost_ratio 0.7115 |
| **1 (best)** | **5** | **0.9128** | fully conformant, task_pass 1.0, wall_clock 25.34 s, per_step_cost_ratio 0.9887, compute_efficiency 0.7728 |

**Attempt 5, at reward 0.9128, holds the highest reward and is the attempt to beat.**

Direction of movement, stated plainly and not softened: attempt 6 (0.5615) is lower than the best that preceded it and `standing_against_best_so_far` records it as worse than an earlier attempt. Attempt 8 (0.7551) is likewise lower than the then-best 0.9128 and is recorded as worse than an earlier attempt. Attempts 3, 7, 9 and 10 (0.0000 each) are each recorded as worse than an earlier attempt. After attempt 5 set 0.9128, no later attempt (6, 7, 8, 9, 10) improved on it, and four of those five scored zero or near-zero. The recent trend is regression, not progress.

## 2. Approach classes tried

Only the graded terms were carried forward, not the code, so these classes are grouped by the measured signature each attempt left behind. Three distinct classes appear.

**Class A — fast, fully conformant trainer that crosses the primary threshold well inside budget.** Attempts 2, 4, 5, 8. In all four: `primary_target_reached` 1.0, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `all_perturbations_held` true, no failed checks at all. This is the only class that has ever scored above 0.80. Within the class, reward tracks how cheaply and quickly the qualifying row was obtained: attempt 5 (qualifying_budget 25.34 s, wall_clock 25.34 s) → 0.9128; attempt 4 (50.03 s) → 0.8719; attempt 2 (73.62 s) → 0.8385; attempt 8 (qualifying_budget 78.14 s but wall_clock 151.50 s) → 0.7551. Attempt 8 is the only record in the whole set where `wall_clock_sec` (151.50) exceeds `qualifying_budget` (78.14) — roughly a factor of two of work performed after the qualifying row was already in hand — and it is also the lowest-scoring member of the class. Note that `compute_efficiency` does not order this class: attempt 4 had `compute_efficiency` 1.0 and still scored below attempt 5 at 0.7728, so wall-clock/qualifying-budget economy, not the reported efficiency figure alone, is what separates them.

**Class B — same style of trainer, but with module-level executable code in the submission.** Attempts 1 and 6. Both reached the primary target (`primary_target_reached` 1.0) and both held all perturbations, but both failed `C-API-SURFACE` and consequently carried `rule_conformance` 0.857 (six of seven rule checks) and `task_pass` 0.0. Attempt 1 was fast (25.46 s) and still only reached 0.7684; attempt 6 was slow (204.09 s, per_step_cost_ratio 1.3778) and reached 0.5615. The lesson from the pair: the API-surface violation costs roughly 0.14–0.15 of reward relative to an otherwise comparable Class A run at similar cost, and it is a pure loss — nothing about it bought any speed.

**Class C — long-running configuration that never produces a qualifying evaluation row.** Attempts 3, 7, 9, 10. Every one of these burned essentially the same wall clock, 1690.96–1692.97 s, which is tight enough across four independent runs to read as a hard ceiling being consumed rather than a training schedule completing. In all four, no evaluation row crossed the threshold in the declared direction, `qualifying_budget` is "not-measured", `conformance_fraction` is 0.0, and both declared perturbation runs failed. Reward 0.0000 each. This class was run four separate times and produced the identical failure signature every time.

## 3. Checks that failed

**`C-API-SURFACE`** — reason given by the verifier, identically both times: *"module-level statements outside imports, constants, and permitted definitions."* This check has now failed **twice**, in attempts 1 and 6. Those two attempts differ substantially in everything else measured — attempt 1 ran in 25.46 s with per_step_cost_ratio 1.0639, attempt 6 ran in 204.09 s with per_step_cost_ratio 1.3778 — so whatever was changed between them is not what is causing this check to fail. The cause is structural in the submission file: there is executable code at module scope. Only imports, constant assignments, and permitted definitions (functions/classes) may sit at module level; anything else — a print, a call, a loop, a config-building expression, a seeding statement, an `if`/`try` block, a device query, a dataset construction, a guarded `__main__` body if that form is not permitted — must be moved inside a function body. Each failure dropped `rule_conformance` to 0.857 and forced `task_pass` to 0.0 despite the primary target being reached.

**`C-TARGET-REACHED`** — reason: *"no evaluation row crosses the threshold in the declared direction."* Failed **four times**, in attempts 3, 7, 9 and 10, on the primary run, and additionally on every held-out run in those same four records. Four attempts, four identical failures: whatever was changed between attempts 3, 7, 9 and 10 is not what is causing this check to fail. Two candidate roots are consistent with the terms and cannot be separated from them: the model genuinely never reaches the metric threshold, or the evaluation rows are being emitted in the wrong direction/format so no row is recognised as crossing. The near-constant ~1692 s wall clock in all four says the run was still going when it was cut off, which favours "never converged inside the ceiling" — but the direction wording in the reason means the declared-direction bookkeeping must also be re-verified before assuming it is purely a convergence problem.

**`C-BUDGET-RESPECTED`** — reason: *"no qualifying row, so no budget position exists."* Failed **four times**, in attempts 3, 7, 9 and 10, and on every held-out run in those records. This is a strict consequence of `C-TARGET-REACHED` failing — there is no qualifying row to place against a budget — so it carries no independent information and will clear automatically the moment a qualifying row exists. It is not a separate bug to chase.

**`C-PERTURBATION-REACHED`** — reason: *"0 of 2 declared perturbations reached their own threshold inside their own budget."* Failed **four times**, in attempts 3, 7, 9 and 10, at the top level of those records. Again a consequence of the same non-convergence, and note it is a total wipeout each time (0 of 2, never 1 of 2), which says the failure is systematic to the configuration rather than a marginal run that happened to miss on one variant.

## 4. Ruled-out directions

**Any module-level executable code in the submission.** Ruled out because `C-API-SURFACE` fired on it twice, in attempts 1 and 6, with the same verbatim reason, and in both cases it forced `task_pass` to 0.0 and `rule_conformance` to 0.857 even though the primary target had been reached and all perturbations held. Attempt 1 in particular reached the target in 25.46 s — essentially the same speed as the best-ever attempt 5 at 25.34 s — and still landed 0.1444 below it, and the only measured difference is this check. Keep the module body to imports, constants, and function/class definitions; put everything else inside the entry-point function.

**The Class C configuration, whatever produced the ~1692 s non-converging runs.** Ruled out because it was tried four separate times (attempts 3, 7, 9, 10) and produced reward 0.0000 every time with an identical three-check failure signature and an identical wall clock at the ceiling. Re-running this shape without changing the thing that stops a qualifying row from appearing is neither exploiting nor exploring; the earlier work did exactly that four times and gained nothing from any of the repeats.

**Spending more wall clock in pursuit of a better metric.** Ruled out on the measured ordering within Class A: the four fully conformant attempts rank strictly by how little time was consumed to obtain the qualifying row — 25.34 s → 0.9128, 50.03 s → 0.8719, 73.62 s → 0.8385, and 78.14 s qualifying with 151.50 s total → 0.7551. Longer training has never bought reward here; it has cost reward monotonically across every fully conformant record.

**Continuing to run after the qualifying row is produced.** Ruled out by attempt 8, the only record where `wall_clock_sec` (151.50) far exceeds `qualifying_budget` (78.14). It was fully conformant with `task_pass` 1.0 and all perturbations held, and still scored 0.7551, the lowest of any conformant attempt. Work performed after qualification is charged and returns nothing.

**Optimising `compute_efficiency` as a proxy for reward.** Ruled out because it inverts: attempt 4 reported `compute_efficiency` 1.0 and scored 0.8719, while attempt 5 reported 0.7728 and scored 0.9128; and the zero-reward attempts 7 and 9 reported `compute_efficiency` 1.0 and 1.0 respectively. This field must not be used as the steering signal.

## 5. Open leads

**Rebuild from the Class A shape and drive the qualifying budget below 25 s.** The best record, attempt 5, qualified at 25.34 s of wall clock with `per_step_cost_ratio` 0.9887 and full conformance. The measured ordering inside Class A says reward rises as the time-to-qualifying-row falls, and nothing has yet been measured below ~25 s. This is the single most direct lead: same conformant structure, same convergence behaviour, but reach the threshold sooner — fewer steps to threshold, larger effective step early, cheaper data pipeline, smaller model or shorter warmup — while keeping enough margin that the held-out runs still clear their own thresholds.

**Stop immediately once the threshold is crossed.** Attempts 5 and 4 have `wall_clock_sec` exactly equal to `qualifying_budget`, which is the desired behaviour; attempt 8 does not, and it is the worst conformant record. Whatever early-exit logic attempts 4 and 5 had should be reinstated and made unconditional: evaluate, and on the first row that crosses the threshold in the declared direction, return.

**Watch the cost-per-step figure.** `per_step_cost_ratio` above 1.0 has coincided with the weaker records (attempt 6 at 1.3778 → 0.5615; attempt 8 at 1.0291 → 0.7551; attempt 1 at 1.0639 → 0.7684), while the strongest conformant records sat at or below roughly 1.0 (attempt 5 at 0.9887, attempt 4 at 0.7115, attempt 2 at 0.9162). Keeping per-step cost at or under parity is a cheap guardrail even though the relationship to reward is not exact.

**Audit the evaluation-row emission against the declared direction before submitting.** Four records failed `C-TARGET-REACHED` with the phrase "in the declared direction". Even though the ~1692 s ceiling suggests non-convergence, it costs nothing to confirm that the metric is logged with the sign/comparison the harness expects, since a direction mismatch would produce exactly this signature regardless of how well the model trained.

**Guard the margin on the held-out runs, not just the primary one.** Reported by kind and in aggregate: across the ten records there were 20 held-out runs, two per record — one of kind `held_out_variant` and one of kind `seed` in each. Twelve reached their thresholds (six of kind `held_out_variant`, six of kind `seed`, in the six records that had a qualifying primary run) with no failed checks. Eight did not reach (four of kind `held_out_variant`, four of kind `seed`), and every one of those eight failed on the same pair, `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. Neither kind is more fragile than the other: they have always succeeded together and failed together, and no record shows a split of one kind reaching while the other did not. That means held-out robustness has never been the isolated problem — when the primary run qualifies, both kinds qualify. Pushing the primary budget down aggressively is the one thing that could break that pattern, so any speed-up should retain enough headroom that a different seed and a variant still cross.

## Call: exploit

Exploit. Class A has scored four times and holds the top four conformant results, with a clear, monotone relationship between time-to-qualification and reward, and the best point (attempt 5, 0.9128) sits at the fastest qualification yet measured with no failed checks whatsoever. The remaining headroom is in that same direction and has not been exhausted. The two things that have destroyed reward are both known and both fixable without leaving this class: module-level statements tripping `C-API-SURFACE`, and the non-converging ~1692 s Class C configuration that has now returned 0.0000 four times in a row. Reconstruct attempt 5's conformant, early-exiting shape, keep the module body to imports/constants/definitions only, and spend the effort on qualifying in under 25 s while leaving margin for the seed and held-out-variant runs.
