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

    All four attempts since have scored lower than it.
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
  3 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 7 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 3 attempts (3, 7, 9). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 3 attempts (3, 7, 9). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 3 attempts (3, 7, 9). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Nine graded attempts, all with `measurement_status: measured`, so every one carries a reward. Ordered worst to best:

- **Attempt 3 — reward 0.0000.** Zero-reason code 4. Ran 1692.52 s wall clock; no qualifying row, so `qualifying_budget` was not measured.
- **Attempt 7 — reward 0.0000.** Zero-reason code 4. Ran 1692.21 s wall clock; no qualifying row.
- **Attempt 9 — reward 0.0000.** Zero-reason code 4. Ran 1692.97 s wall clock; no qualifying row.
- **Attempt 6 — reward 0.5615** (0.5614595915946324). Primary target reached, both perturbations held, but `rule_conformance` 0.8571 (6 of 7) and `task_pass` 0 because of a conformance failure. Wall clock 204.09 s; per-step cost ratio 1.3778; compute efficiency 0.6091. This is **lower than attempts 1, 2, 4 and 5 that preceded it** — a regression, not progress.
- **Attempt 8 — reward 0.7551** (0.7551378151147599). Fully conformant (`rule_conformance` 1.0, no failed checks), `task_pass` 1, both perturbations held. Qualifying budget 78.14 s but total wall clock 151.50 s. **Lower than attempts 2, 4 and 5** — a regression.
- **Attempt 1 — reward 0.7684** (0.7684495494479875). Primary target reached and both perturbations held, but one conformance check failed; `rule_conformance` 0.8571, `task_pass` 0. Wall clock 25.46 s; compute efficiency 0.8160; per-step cost ratio 1.0639. First measured attempt.
- **Attempt 2 — reward 0.8385** (0.8385437894774304). Clean: no failed checks, `task_pass` 1, `rule_conformance` 1.0, both perturbations held. Qualifying budget and wall clock both 73.62 s; compute efficiency 0.9164; per-step cost ratio 0.9162.
- **Attempt 4 — reward 0.8719** (0.8718974477208268). Clean, `task_pass` 1, both perturbations held. Qualifying budget and wall clock both 50.03 s; compute efficiency 1.0000 (the maximum seen); per-step cost ratio 0.7115.
- **Attempt 5 — reward 0.9128** (0.9128129743237858). Clean, `task_pass` 1, both perturbations held. Qualifying budget and wall clock both 25.34 s — the fastest qualifying run recorded; compute efficiency 0.7728; per-step cost ratio 0.9887.

**Attempt 5, at reward 0.9128, holds the highest reward and is the attempt to beat.** No attempt has crossed 0.92. `validity` was 1.0 and `red_line_crossed` was 0.0 in every single record, so nothing has ever been invalidated or tripped a red line.

# 2. Approach classes tried

I was given measured terms only, not source, so these classes are grouped by their measured signature. There are three distinct classes across the nine records.

**Class A — fast, fully conformant, target reached (attempts 2, 4, 5, 8).** Every check held, `task_pass` 1, `primary_target_reached` 1, `conformance_fraction` 1.0, both declared perturbations reached. These are the only attempts that produced a passing, penalty-free run. Their rewards were 0.8385, 0.8719, 0.9128 and 0.7551 respectively. Within this class reward tracks time almost perfectly and inversely: 25.34 s → 0.9128, 50.03 s → 0.8719, 73.62 s → 0.8385, and attempt 8 (qualifying at 78.14 s but running on to 151.50 s of wall clock) → 0.7551. Note that attempt 8 qualified only 4.5 s later than attempt 2 yet scored 0.0834 lower, and the one term that separates them is total wall clock (151.50 vs 73.62). The working hypothesis this supports is that the score is charged for the whole run, not merely for the moment the threshold is crossed — stopping promptly after qualifying appears to matter as much as qualifying quickly.

Compute efficiency is *not* the driver. Attempt 4 achieved `compute_efficiency` 1.0 and still scored 0.8719, below attempt 5's 0.9128 at `compute_efficiency` 0.7728. Per-step cost ratio likewise shows no clean relationship to reward inside this class (0.9162, 0.7115, 0.9887, 1.0291 against rewards 0.8385, 0.8719, 0.9128, 0.7551). Wall-clock/qualifying budget is the term that orders this class.

**Class B — target reached but the module-level API-surface rule broken (attempts 1 and 6).** Both hit the primary target and both had all perturbations hold, but each failed `C-API-SURFACE` and was scored with `rule_conformance` 0.8571 (six of seven rules) and `task_pass` 0. Attempt 1 ran in 25.46 s — essentially the same budget as best-scoring attempt 5 at 25.34 s — and scored 0.7684 against attempt 5's 0.9128. That pairing gives a fairly direct read on the size of the penalty: roughly 0.14 of reward for the single conformance violation, at matched budget. Attempt 6 stacked the same violation on top of a slow 204.09 s run and landed at 0.5615, the worst non-zero score recorded.

**Class C — long-running, never crossed the threshold (attempts 3, 7, 9).** All three scored 0.0000 with zero-reason code 4. All three ran 1692.5, 1692.2 and 1692.97 s of wall clock respectively — within a second of each other, which strongly suggests all three hit the same hard time ceiling of roughly 1692–1693 s and were cut off rather than converging and failing. In all three, `rule_conformance` was 1.0 and `validity` 1.0, so these were *legal* submissions that simply never reached the target. Their compute-efficiency figures (0.9672, 1.0000, 1.0000) and per-step cost ratios (0.8484, 0.8407, 0.8901) were good — cheap per step, but far too many steps, or a configuration that never converges. Whatever these three did, they did it three separate times with the same outcome.

# 3. Checks that failed

Four distinct named checks have failed across the nine records.

- **`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions." Failed twice**, in attempt 1 and again in attempt 6. Both times it dropped `rule_conformance` to 0.8571 and forced `task_pass` to 0 even though the primary target was reached and every perturbation held. Because this same check failed in two attempts that otherwise differ substantially in runtime (25.46 s vs 204.09 s) and in reward (0.7684 vs 0.5615), whatever was changed between attempt 1 and attempt 6 is not what causes this failure. The fix is specific and mechanical: no executable statement may sit at module level. Only imports, constant assignments and permitted definitions (functions, classes) belong outside a function body. Any setup call, print, seeding call, config-building expression, `if __name__` block content or bare computation at module scope has to move inside a function.
- **`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction." Failed three times**, in attempts 3, 7 and 9.
- **`C-BUDGET-RESPECTED` — "no qualifying row, so no budget position exists." Failed three times**, in attempts 3, 7 and 9. This is a consequence of the preceding check rather than an independent fault: with no row crossing the threshold there is nothing to position against the budget.
- **`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget." Failed three times**, in attempts 3, 7 and 9.

These three checks always failed together, in all three zero-reward attempts, all three of which sat at the ~1692 s wall-clock ceiling. Three separate attempts produced this identical triple; whatever varied between attempts 3, 7 and 9 is not what causes it. The single upstream cause is failure to cross the threshold at all within the time available.

**Perturbation-unit outcomes.** Every record declared 2 perturbations and reported exactly two units: one of kind `held_out_variant` and one of kind `seed`. Across the nine records that is 18 perturbation runs, 9 of each kind.

- By kind, `held_out_variant`: 6 of 9 reached their threshold; 3 did not, each failing `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.
- By kind, `seed`: 6 of 9 reached their threshold; 3 did not, each failing `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.
- In aggregate: 12 of 18 reached, 6 did not, and every non-reaching run failed on exactly that same pair of checks.

The two kinds behave identically in the record: they succeed together and they fail together, and they fail only in the three attempts where the primary run also failed to reach its target. There is no instance anywhere of a perturbation failing while the primary succeeded — `all_perturbations_held` was true in all six attempts with `primary_target_reached` 1. So held-out robustness has never been the binding constraint; the primary run's convergence is. The runs are not individually identified, and nothing here lets one claim a given run is the same one across two records.

# 4. Ruled-out directions

- **Any module-level executable statement in the submission.** Ruled out because `C-API-SURFACE` caught it twice (attempts 1 and 6), costing about 0.14 of reward at matched budget and zeroing `task_pass` both times. There is no version of this that scores; it is a pure loss with no upside.
- **The Class C configuration — whatever produced the ~1692 s non-converging runs.** Ruled out because it was tried three times (attempts 3, 7, 9) and returned reward 0.0000 every time, with the identical triple of failed checks and a wall clock pinned to the same ceiling. Repeating this shape without changing what stops it from crossing the threshold is not exploration and not exploitation; the record shows it was already repeated twice after its first zero, and that pattern must not continue.
- **Optimising `compute_efficiency` or `per_step_cost_ratio` as the objective.** Ruled out as a proxy: attempt 4 reached `compute_efficiency` 1.0 and still scored below attempt 5 at 0.7728, and the three zero-reward attempts posted the best per-step cost ratios in the whole record (0.8484, 0.8407, 0.8901). Cheap steps that never converge score nothing.
- **Letting the run continue after the qualifying row is produced.** Ruled out by attempt 8, which qualified at 78.14 s — barely later than attempt 2's 73.62 s — but ran on to 151.50 s of wall clock and scored 0.7551 against attempt 2's 0.8385. The extra 73 s of post-qualification work bought nothing and appears to have cost roughly 0.08.
- **Longer training as a route to a higher reward.** Ruled out across both directions of the record: within the passing class, the four rewards fall monotonically as budget rises (25.34 s → 0.9128, 50.03 s → 0.8719, 73.62 s → 0.8385, 151.50 s → 0.7551), and the longest runs of all scored zero.

# 5. Open leads

- **Beat 25.34 s while staying clean.** Attempt 5 is the target at reward 0.9128 and it is the fastest qualifying run on record. Every clean attempt's reward is ordered by its budget, so the direct lead is to reach the same threshold in less wall clock — fewer epochs, a larger learning rate with a schedule that lands the threshold sooner, a smaller model or narrower data pass, early exit the instant the evaluation row crosses in the declared direction. The margin between 0.9128 and 1.0 is real headroom and the mechanism to close it is time.
- **Exit immediately on qualification.** Attempt 8's 151.50 s wall clock against a 78.14 s qualifying budget is the clearest waste in the record. Whatever loop structure allowed the run to continue past its qualifying row should be replaced with a hard break-and-return the moment the threshold is crossed. In every other passing attempt (2, 4, 5) `wall_clock_sec` equals `qualifying_budget` exactly, which is the shape to reproduce.
- **Keep the module surface clean by construction.** Put everything — seeding, config, data loading, training, evaluation — inside function bodies, with only imports, plain constant assignments and def/class statements at module scope. This is the cheapest 0.14 available and it has been lost twice.
- **Reduce time without falling into Class C.** The risk in pushing the budget down is crossing into the regime where no evaluation row ever qualifies, which returns 0.0000 outright. A safe way to explore that edge is to evaluate frequently and cheaply so that the earliest qualifying row is detected as soon as it exists, rather than shortening the schedule blindly and discovering after ~1692 s that nothing qualified. Frequent evaluation also protects the two perturbation runs, which have to reach their own thresholds inside their own budgets.
- **Robustness is not currently the constraint, but do not trade it away.** `held_out_variant` and `seed` runs have reached whenever the primary reached, 12 of 18 aggregate. Aggressive speed cuts could break that symmetry for the first time, so any budget reduction should leave enough margin that a different seed and a held-out variant still cross. A run that qualifies primarily but misses on the seed or variant would fail `C-PERTURBATION-REACHED` and lose everything.

**Call: exploit.** The highest-scoring approach (attempt 5, reward 0.9128, clean, 25.34 s) is still improving as budget falls, and the two loss mechanisms observed — the `C-API-SURFACE` module-level violation and post-qualification runtime — are both identified and mechanically fixable rather than exhausted. The next attempt should reproduce the Class A shape, keep all executable code inside functions, return immediately on the qualifying row, and drive wall clock below 25.34 s while keeping the seed and held-out-variant runs reaching their thresholds. Do not re-run the Class C long-training shape: it has scored 0.0000 three times with no change to what stopped it.
