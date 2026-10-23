# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 2 -- reward 0.8385, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2 *      0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                

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

    attempt 1 -- reward 0.7684, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 3 -- reward 0.0000, worse than an earlier attempt
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
    C-API-SURFACE failed on attempt 1.
    C-BUDGET-RESPECTED failed on attempt 3.
    C-PERTURBATION-REACHED failed on attempt 3.
    C-TARGET-REACHED failed on attempt 3.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Three graded attempts, all with measurement_status `measured`, so all three carry a reward. Ordered worst to best:

- **Attempt 3 — reward 0.0000.** Zeroed out (`zero_reason_code` 4). `primary_target_reached` 0.0, `task_pass` 0.0, `conformance_fraction` 0.0, `all_perturbations_held` false. `wall_clock_sec` 1692.5153577327728; `qualifying_budget` is `not-measured` because no qualifying row existed. `rule_conformance` was a clean 1.0 and `validity` 1.0, and `red_line_crossed` 0.0 — nothing was malformed; it simply never hit the target. `standing_against_best_so_far`: worse_than_an_earlier_attempt. This is a plain regression from attempt 2, not partial progress: it went from 0.8385 to 0.0000.
- **Attempt 1 — reward 0.7684495494479875 (0.7684).** `primary_target_reached` 1.0, `all_perturbations_held` true, `conformance_fraction` 1.0, `validity` 1.0, `red_line_crossed` 0.0, but `task_pass` 0.0 and `rule_conformance` 0.8571428571428571 because one check failed. `compute_efficiency` 0.8160403297407965, `per_step_cost_ratio` 1.0638707778973995, `wall_clock_sec` / `qualifying_budget` 25.461896419525146. `standing_against_best_so_far`: first_measured_attempt.
- **Attempt 2 — reward 0.8385437894774304 (0.8385).** `failed_checks` empty. `primary_target_reached` 1.0, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `validity` 1.0, `all_perturbations_held` true, `red_line_crossed` 0.0, `zero_reason_code` 0. `compute_efficiency` 0.9164113991335355, `per_step_cost_ratio` 0.916173415836911, `wall_clock_sec` / `qualifying_budget` 73.62353277206421. `standing_against_best_so_far`: better_than_every_earlier_attempt.

**Attempt 2 holds the highest reward, 0.8385, and it is the one to beat.**

# 2. Approach classes tried

The records describe three distinct behaviours, not three variations of one:

**Class A — target-reaching but non-conformant module surface (attempt 1).** This class solved the learning task within a tight 25.46 s budget and held both held-out runs, but the submission file placed executable work at module level. Its cost profile is the *expensive-per-step, few-steps* corner: `per_step_cost_ratio` 1.0639 (above 1.0, i.e. each step cost more than the reference step) yet the shortest wall clock of any attempt. `compute_efficiency` 0.8160. It scored despite the conformance defect, because `primary_target_reached` was 1.0 and both perturbations held; the defect cost it `rule_conformance` (0.8571 instead of 1.0) and `task_pass` (0.0), and that gap is essentially the whole 0.0701 difference between it and attempt 2.

**Class B — conformant, target-reaching, moderate budget (attempt 2).** Same successful learning outcome, with the module-surface defect removed: every check passed, `rule_conformance` 1.0, `task_pass` 1.0. Cost profile moved to the *cheaper-per-step, more-steps* corner: `per_step_cost_ratio` dropped to 0.9162 and `compute_efficiency` rose to 0.9164, while wall clock rose from 25.46 s to 73.62 s. Both held-out runs reached their thresholds inside their own budgets. This is the reference implementation the next attempt should reconstruct.

**Class C — aggressive per-step cost reduction that lost convergence (attempt 3).** This class pushed the efficiency lever further: `per_step_cost_ratio` fell to 0.8484 and `compute_efficiency` rose to 0.9672, the best per-step and efficiency numbers of any attempt. But total wall clock exploded to 1692.52 s — roughly 23× attempt 2 — and no evaluation row ever crossed the threshold in the declared direction, on the primary run or on either held-out run. The lesson is direct: the cheapening that improved `per_step_cost_ratio` destroyed convergence, so the run burned an enormous number of cheap steps and qualified nowhere. Efficiency terms improved and the reward went to zero, which means efficiency is not a term you can buy at the cost of `primary_target_reached`.

# 3. Checks that failed

**C-API-SURFACE** — verifier reason: "module-level statements outside imports, constants, and permitted definitions". Failed once, in attempt 1 only. Attempt 2 passed it and attempt 3 passed it, so the fix is known-good and must be preserved: the submission file may contain imports, constants, and permitted definitions at module level and nothing else — no top-level calls, no top-level training/setup/print/config-mutation statements. Put every executable line inside the permitted function or class definitions.

**C-TARGET-REACHED** — verifier reason: "no evaluation row crosses the threshold in the declared direction". Failed three times inside attempt 3: once on the primary run and once on each of the two held-out perturbation runs. It has never failed in attempts 1 or 2.

**C-BUDGET-RESPECTED** — verifier reason: "no qualifying row, so no budget position exists". Failed three times inside attempt 3, on the primary run and on both held-out runs. This is a downstream consequence of C-TARGET-REACHED, not an independent budget overrun: with no row crossing the threshold there is no qualifying row against which a budget position can be computed. Fixing convergence should clear it automatically.

**C-PERTURBATION-REACHED** — verifier reason: "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed once, in attempt 3, as the aggregate roll-up of the two held-out failures.

On repetition: **C-TARGET-REACHED and C-BUDGET-RESPECTED each failed three times, but all six of those failures are inside the single attempt 3** (primary plus both held-out runs). No named check has yet failed across two different attempts, so there is no evidence here of a defect that survived a code change. C-API-SURFACE failed once and was subsequently fixed and stayed fixed.

# 4. Ruled-out directions

- **Leaving executable statements at module scope.** Ruled out because it triggers C-API-SURFACE with reason "module-level statements outside imports, constants, and permitted definitions", which cut `rule_conformance` to 0.8571 and `task_pass` to 0.0 in attempt 1 even though the run reached its target and held both perturbations. Cost: 0.0701 of reward relative to the otherwise-equivalent attempt 2.
- **Driving `per_step_cost_ratio` down to ~0.85 by whatever means attempt 3 used.** Ruled out as configured: it produced the best `compute_efficiency` seen (0.9672) and a reward of exactly 0.0000, because no evaluation row crossed the threshold on the primary run or either held-out run. Cheap steps that do not converge are worth nothing.
- **Very long runs as a route to the target.** Ruled out on the evidence of attempt 3's 1692.52 s wall clock producing no qualifying row at all. Length alone did not rescue a configuration that had lost its convergence; the two successful attempts qualified in 25.46 s and 73.62 s respectively.
- **Treating attempt 3 as a partial success worth incremental repair of its cost settings.** Ruled out: `conformance_fraction` 0.0 and `all_perturbations_held` false mean nothing in that run qualified anywhere. There is no measured evidence that any part of its configuration is salvageable, and no reason to prefer it as a base over attempt 2.

# 5. Open leads

- **Reconstruct attempt 2 exactly first, and confirm 0.8385 before changing anything.** The stub is pristine and the next attempt cannot see prior code, so the first job is re-deriving a submission that is fully conformant (nothing executable at module scope) and that reaches the primary target and both held-out thresholds within budget. Everything below is a delta on top of that.
- **Recover attempt 1's step count without recovering its non-conformance.** Attempt 1 reached the target in 25.46 s with `per_step_cost_ratio` 1.0639; attempt 2 took 73.62 s with `per_step_cost_ratio` 0.9162. Both reached the target and both held perturbations, but attempt 2 scored higher, so the reward favoured the lower per-step cost / higher `compute_efficiency` (0.9164 vs 0.8160) even at 3× the wall clock. The unexplored corner is *both* at once: attempt 1's short trajectory combined with attempt 2's cheaper step. Target a wall clock between 25 s and 73 s while keeping `per_step_cost_ratio` at or below 0.9162.
- **Move `per_step_cost_ratio` from 0.9162 toward 0.8484 in small, guarded increments.** Attempt 3 proved the endpoint is reachable in cost terms; what it did not do is keep convergence. Take the step-cost reduction in a fraction of the way, and treat any run whose evaluation rows are not visibly crossing the threshold at attempt-2-like wall clocks as a failed variant to back out of, not to run longer.
- **Add an explicit convergence guard so a cheapened configuration cannot silently produce zero.** The failure signature of attempt 3 is "no evaluation row crosses the threshold in the declared direction" combined with a 1692 s wall clock. A conservative fallback — e.g. reverting to known-good step settings if the evaluation metric has not moved in the declared direction by an early checkpoint — converts a 0.0000 into something near 0.8385 rather than a total loss. Any such logic must live inside permitted definitions to avoid re-triggering C-API-SURFACE.
- **Do not trade robustness for efficiency.** Both held-out kinds — `held_out_variant` and `seed` — reached their thresholds in attempts 1 and 2 and both failed on C-TARGET-REACHED and C-BUDGET-RESPECTED in attempt 3. In aggregate across the three attempts, four of six held-out runs reached and two did not, and both non-reaching runs came from the same aggressive-cost attempt, one of each kind. There is no sign that either kind is intrinsically harder; the same convergence loss took both down together. Any efficiency change should be validated as holding for both kinds, since a single non-reaching held-out run trips C-PERTURBATION-REACHED and clears `all_perturbations_held`.

**Call: exploit.** The scoring approach (class B, attempt 2, 0.8385) has been improved on exactly once and has not been shown to have plateaued — the unexplored short-wall-clock / low-per-step-cost corner between attempts 1 and 2 is a concrete, measured-in gap. Attempt 3 was the one structural departure and it scored 0.0000 by breaking the very condition the reward is gated on. Rebuild attempt 2, then push efficiency in guarded increments with convergence verified at every step; do not repeat attempt 3's cost settings without adding the convergence guard, because re-running an approach that scored zero without changing what made it score zero is neither exploring nor exploiting.
