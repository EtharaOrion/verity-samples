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

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4        0.8719   1.000             2 of 2         yes             50                
  5 *      0.9128   1.000             2 of 2         yes             25                

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
  1 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 2 -- reward 0.8385, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

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

    attempt 4 -- reward 0.8719, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 1.
    C-BUDGET-RESPECTED failed on attempt 3.
    C-PERTURBATION-REACHED failed on attempt 3.
    C-TARGET-REACHED failed on attempt 3.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Five graded submissions, all with `measurement_status: "measured"`, so every one carries a reward. Ordered worst to best:

- **Attempt 3 — reward 0.0000.** `zero_reason_code` 4, `primary_target_reached` 0.0, `task_pass` 0.0, `conformance_fraction` 0.0, `all_perturbations_held` false. `wall_clock_sec` 1692.5153 (roughly 33× to 67× every other attempt), `qualifying_budget` "not-measured" because no row qualified. `rule_conformance` was 1.0 and `validity` 1.0 — the code was well-formed and rule-conformant; it simply never crossed the threshold. `standing_against_best_so_far`: worse_than_an_earlier_attempt. This is plainly a regression, not progress.
- **Attempt 1 — reward 0.7684.** `primary_target_reached` 1.0 but `task_pass` 0.0, `rule_conformance` 0.8571, `conformance_fraction` 1.0, `validity` 1.0. `wall_clock_sec` 25.4619, `compute_efficiency` 0.8160, `per_step_cost_ratio` 1.0639. Both perturbations held. `standing_against_best_so_far`: first_measured_attempt.
- **Attempt 2 — reward 0.8385.** No failed checks, `rule_conformance` 1.0, `task_pass` 1.0, `primary_target_reached` 1.0. `wall_clock_sec` 73.6235, `compute_efficiency` 0.9164, `per_step_cost_ratio` 0.9162. Better than every earlier attempt.
- **Attempt 4 — reward 0.8719.** No failed checks, `task_pass` 1.0, `compute_efficiency` 1.0000 (the only perfect value seen), `per_step_cost_ratio` 0.7115, `wall_clock_sec` 50.0341. Better than every earlier attempt.
- **Attempt 5 — reward 0.9128. This is the highest reward recorded and the one to beat.** No failed checks, `rule_conformance` 1.0, `conformance_fraction` 1.0, `task_pass` 1.0, `primary_target_reached` 1.0, both perturbations held. `wall_clock_sec` 25.3436 (the fastest of all five), `qualifying_budget` 25.3436, `compute_efficiency` 0.7728, `per_step_cost_ratio` 0.9887. Better than every earlier attempt.

`red_line_crossed` was 0.0 and `validity` 1.0 in all five records; nothing has ever tripped a red line or been ruled invalid.

# 2. Approach classes tried

Only the measured terms are available, so these classes are characterised by what the harness recorded, not by source code. Four distinct classes appear:

**Class A — fast solver, non-conformant module layout (attempt 1).** Reached the primary target in 25.46 s and held both perturbations, but the submission carried module-level statements outside imports, constants and permitted definitions. `rule_conformance` fell to 0.8571 (6 of 7 rules) and `task_pass` was forced to 0.0 despite `primary_target_reached` 1.0. Reward 0.7684. The lesson embedded in this record: reaching the target is not sufficient; a single rule violation drops `task_pass` to zero and costs roughly 0.07 of reward even when the run itself is fine.

**Class B — same solving behaviour with the module layout repaired (attempt 2).** All checks passed, `rule_conformance` 1.0, `task_pass` 1.0, reward 0.8385. Wall clock grew to 73.62 s, nearly 3× attempt 1, and `per_step_cost_ratio` fell to 0.9162 while `compute_efficiency` rose to 0.9164. Conformance was bought and the target was still reached, but the run became slow.

**Class C — long-horizon / heavy-compute variant (attempt 3).** Ran 1692.52 s and never crossed the threshold in the declared direction on the primary run or on either perturbation. Rule-conformant and valid, but scored 0.0000. Whatever the change was — more steps, a larger model, a different optimiser regime, a different schedule — it traded away the thing the grade depends on. `per_step_cost_ratio` 0.8484 and `compute_efficiency` 0.9672 look healthy in isolation, which is the trap: the per-step numbers can improve while the run as a whole fails to converge inside its budget.

**Class D — conformant solver tuned for cost, two settings (attempts 4 and 5).** Both pass everything. Attempt 4 sits at 50.03 s with `per_step_cost_ratio` 0.7115 and `compute_efficiency` 1.0000 for reward 0.8719. Attempt 5 sits at 25.34 s with `per_step_cost_ratio` 0.9887 and `compute_efficiency` 0.7728 for reward 0.9128. These two are the informative pair: attempt 5 has *worse* `compute_efficiency` and *worse* `per_step_cost_ratio` than attempt 4 yet a higher reward, while having half the wall clock and half the `qualifying_budget`. Across the four passing records the monotone relationship is with wall clock / qualifying budget, not with `compute_efficiency`: 73.62 s → 0.8385, 50.03 s → 0.8719, 25.34 s → 0.9128. Attempt 1 at 25.46 s would fit that curve too but was docked to 0.7684 by its rule violation. The working hypothesis the data supports is that once every check passes, reward rises as total qualifying budget (wall clock to threshold) falls, and that maximising `compute_efficiency` or minimising `per_step_cost_ratio` in isolation is not the lever.

# 3. Checks that failed

Four distinct check identifiers have failed, across two attempts.

- **C-API-SURFACE** — reason given by the verifier: "module-level statements outside imports, constants, and permitted definitions." Failed once, in attempt 1 only. It has not recurred in any later record.
- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction." Failed in attempt 3 only, but within that attempt it failed three times over: on the primary run and on both held-out perturbation units.
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists." Failed in attempt 3 only, again on the primary run and on both perturbation units. This is a consequence of C-TARGET-REACHED, not an independent budget overrun: with no row crossing the threshold there is no budget position to evaluate, which is also why `qualifying_budget` reads "not-measured" rather than a number.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget." Failed in attempt 3 only.

No check identifier appears in more than one attempt record. C-API-SURFACE was fixed after attempt 1 and has stayed fixed through four subsequent attempts; the attempt-3 cluster is a single event and did not recur in attempts 4 or 5. There is therefore no standing failure that survived a change — every failure so far has been eliminated by the following attempt.

# 4. Ruled-out directions

- **Leaving executable statements at module scope (Class A).** Ruled out by C-API-SURFACE with reason "module-level statements outside imports, constants, and permitted definitions." It cost `rule_conformance` (0.8571) and zeroed `task_pass` even though the primary target was reached and both perturbations held; reward 0.7684 versus 0.9128 for the same-speed conformant attempt 5. Keep all logic inside permitted definitions; only imports, constants and definitions at module level.
- **The long-horizon / heavy-compute regime of attempt 3.** Ruled out by direct measurement: 1692.52 s of wall clock, C-TARGET-REACHED failed on the primary and on both perturbations, reward 0.0000. Rule conformance and validity were perfect, so the failure is in the training configuration, not in the code's shape. Do not re-enter this regime without changing what made it fail to converge, and do not read its healthy `per_step_cost_ratio` (0.8484) or `compute_efficiency` (0.9672) as evidence it was close.
- **Optimising `compute_efficiency` as the objective.** Ruled out by the attempt 4 versus attempt 5 comparison: attempt 4 achieved `compute_efficiency` 1.0000 and scored 0.8719, while attempt 5 at 0.7728 scored 0.9128. A perfect `compute_efficiency` is not the top of the reward surface.
- **Driving `per_step_cost_ratio` down as the objective.** Same comparison: attempt 4's 0.7115 lost to attempt 5's 0.9887. Cheaper steps that require more of them do not pay.
- **The attempt 2 operating point (73.62 s).** Superseded twice; it is conformant and passing but its budget is ~2.9× attempt 5's for a reward 0.0743 lower. There is no reason to return to it.

# 5. Open leads

- **Start from the attempt 5 configuration.** It is the only record combining a full pass (all checks, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, both perturbations held) with the lowest observed budget (25.34 s). Reproduce that first, then perturb one thing at a time.
- **Push qualifying budget below ~25 s while keeping every check green.** This is the lever the four passing records agree on: 73.62 → 0.8385, 50.03 → 0.8719, 25.34 → 0.9128. Reward has risen monotonically as wall clock to threshold has fallen. Fewer steps, earlier stopping the moment the declared threshold is crossed in the declared direction, cheaper data loading or evaluation cadence, and avoiding any work after the qualifying row is produced are all candidates.
- **Stop as soon as the threshold is crossed.** `qualifying_budget` equals `wall_clock_sec` exactly in every measured record (25.4619, 73.6235, 50.0341, 25.3436). The budget being scored is total wall clock, so any post-threshold work is pure cost. If the current code trains a fixed number of steps and evaluates at the end, converting to evaluate-and-exit is the highest-value cheap change.
- **Guard the margin on C-TARGET-REACHED while cutting cost.** Attempt 3 shows what the floor looks like: miss the threshold and reward is 0.0000 outright, with C-BUDGET-RESPECTED and C-PERTURBATION-REACHED cascading from it. Any speed cut should leave visible headroom above the threshold rather than sitting on it, because the same configuration must also clear the threshold independently under a re-seeded run and under a held-out variant.
- **Re-check the module surface after every edit.** C-API-SURFACE is cheap to re-break when refactoring for speed, and it costs `task_pass` entirely — a fast, correct run scored 0.7684 because of it.
- **Perturbation outcomes to design against.** Ten held-out units were run in total, two per attempt, of kinds `held_out_variant` and `seed`. Eight reached their threshold (attempts 1, 2, 4 and 5, both kinds each time). Two did not, both in attempt 3 — one of kind `held_out_variant` and one of kind `seed` — and each failed on C-TARGET-REACHED and C-BUDGET-RESPECTED. By kind: `held_out_variant` reached in 4 of 5 records, `seed` reached in 4 of 5 records. The failure is not specific to either kind; the run that failed to converge failed on both, which says the problem was the configuration itself rather than sensitivity to seed or to variant. The units are unidentified across records and no claim is made that any given unit recurs.

**Call: exploit.** The passing family (Class D) is still improving — 0.8385 → 0.8719 → 0.9128 across successive conformant attempts — and the mechanism behind the improvement is legible in the data: lower qualifying budget with all checks held. The next attempt should take the attempt 5 operating point and reduce its wall clock to threshold further, holding C-API-SURFACE, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-PERTURBATION-REACHED green, rather than reaching for a structurally new method. Explore is not warranted yet, and the one structural excursion already made (attempt 3's long-horizon regime) scored 0.0000; re-running anything resembling it without changing why it missed the threshold would be neither exploration nor exploitation.
