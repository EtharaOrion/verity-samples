# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.8658, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All six attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3        0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                
  5 *      0.8658   1.000             2 of 2         yes             74                
  6        0.7580   0.857             2 of 2         yes             46                
  7        0.4911   1.000             1 of 2         yes             50                
  8        0.7805   1.000             2 of 2         yes             99                
  9        0.8332   1.000             2 of 2         yes             50                
  10       0.8503   1.000             2 of 2         yes             75                
  11       0.8067   1.000             2 of 2         yes             74                

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
  5 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.8630, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.8332, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 10 -- reward 0.8503, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 75
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.8067, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED failed on attempt 7.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Eleven graded submissions, all with `measurement_status: "measured"`; every one carries a reward, none was invalid, and `red_line_crossed` is 0.0 and `zero_reason_code` is 0 throughout. Ordered worst to best by reward:

| Rank | Attempt | reward | Notes from its own terms |
|---|---|---|---|
| 1 (worst) | 7 | 0.4911 | `task_pass` 0.0; failed `C-PERTURBATION-REACHED`; `conformance_fraction` 0.5; wall clock 50.05 s |
| 2 | 6 | 0.7580 | `task_pass` 0.0; failed `C-API-SURFACE`; `rule_conformance` 0.8571; `per_step_cost_ratio` 1.4094; `compute_efficiency` 0.4942 |
| 3 | 4 | 0.7740 | clean; `per_step_cost_ratio` 0.6934; `compute_efficiency` 0.9681 |
| 4 | 8 | 0.7805 | clean; `per_step_cost_ratio` 1.0848; wall clock 98.60 s (longest run) |
| 5 | 11 | 0.8067 | clean; `compute_efficiency` 1.0000 (highest observed); `per_step_cost_ratio` 0.6947 |
| 6 | 2 | 0.8079 | clean; `per_step_cost_ratio` 0.9441; wall clock 74.26 s |
| 7 | 9 | 0.8332 | clean; `per_step_cost_ratio` 0.9516; `qualifying_budget` 49.89 s against wall clock 74.39 s |
| 8 | 10 | 0.8503 | clean; `per_step_cost_ratio` 0.9615; wall clock 74.54 s |
| 9 | 1 | 0.8630 | clean; `per_step_cost_ratio` 1.0723; wall clock 76.34 s; first measured attempt |
| 10 | 3 | 0.8657 | clean; `per_step_cost_ratio` 0.9835; wall clock 74.37 s |
| 11 (best) | 5 | **0.8658** | clean; `per_step_cost_ratio` 0.9581; `compute_efficiency` 0.6926; wall clock 74.38 s |

**Attempt 5 holds the highest reward at 0.8658, and it is the one to beat.**

Directional facts that must not be softened. Attempt 2 (0.8079) is **lower** than attempt 1 (0.8630); its `standing_against_best_so_far` is `worse_than_an_earlier_attempt`. Attempt 3 (0.8657) beat everything before it. Attempt 4 (0.7740) is **lower** than attempt 3. Attempt 5 (0.8658) beat everything before it, by 0.0001 over attempt 3 — a margin small enough that attempts 3 and 5 should be treated as the same performance level, not as an improvement. Every attempt after 5 — 6 (0.7580), 7 (0.4911), 8 (0.7805), 9 (0.8332), 10 (0.8503), 11 (0.8067) — is marked `worse_than_an_earlier_attempt`. Six consecutive regressions followed the best score; nothing since attempt 5 has improved on it.

Secondary terms: `primary_target_reached` is 1.0 in all eleven records, including the two with `task_pass` 0.0. `validity` is 1.0 in all eleven. `task_pass` is 1.0 in nine records and 0.0 in attempts 6 and 7. So the primary target is not the binding constraint — conformance and the perturbation runs are, and beyond that the reward differences among the nine clean attempts come from the cost/efficiency terms.

# 2. Approach classes tried

I was given measured terms only, not source, so these classes are defined by the cost and conformance signatures the harness reported. Five distinct classes appear.

**Class A — baseline-cost configuration, per-step cost near parity, ~74 s wall clock.** Attempts 1, 2, 3, 5, 9, 10. `per_step_cost_ratio` in the band 0.9441–1.0723, `compute_efficiency` 0.6784–0.7505, wall clock 74.26–76.34 s. This class contains every one of the six highest rewards (0.8079, 0.8332, 0.8503, 0.8630, 0.8657, 0.8658) and all of the clean, `task_pass` 1.0 records at the top of the table. Within the class, reward does not track `compute_efficiency`: attempt 5 has the *lowest* efficiency in the class (0.6926) and the highest reward, while attempt 9 has the highest efficiency in the class (0.7505) and a lower reward (0.8332). The class's spread of 0.058 reward is real but unstructured with respect to the reported cost terms.

**Class B — aggressive per-step cost reduction.** Attempts 4 and 11. Both drove `per_step_cost_ratio` down to ~0.694 (0.6934 and 0.6947) and pushed `compute_efficiency` to 0.9681 and 1.0000 respectively — attempt 11 hit the ceiling of that term. Both stayed fully conformant with `task_pass` 1.0 and all perturbations held. Both scored below class A: 0.7740 and 0.8067. Maximising `compute_efficiency` cost roughly 0.06–0.09 reward relative to attempt 5.

**Class C — increased per-step cost with a longer run.** Attempt 8: `per_step_cost_ratio` 1.0848, wall clock 98.60 s, `compute_efficiency` 0.6575 (lowest among clean runs), reward 0.7805. Clean and `task_pass` 1.0, but paying more time per step and running ~24 s longer than class A produced a clear regression. Attempt 1 sits at the boundary (ratio 1.0723) but with a class-A wall clock of 76.34 s and reward 0.8630, which is the evidence that the wall-clock extension, not the ratio alone, is what hurt attempt 8.

**Class D — heavy compute with module-level program structure.** Attempt 6: `per_step_cost_ratio` 1.4094, `compute_efficiency` 0.4942 (lowest overall), `qualifying_budget` 45.82 s against wall clock 70.37 s. It failed the `C-API-SURFACE` check, `rule_conformance` fell to 0.8571, `task_pass` went to 0.0, and reward was 0.7580. Both perturbation runs still reached their thresholds.

**Class E — compressed budget.** Attempt 7: wall clock and `qualifying_budget` both 50.05 s, `per_step_cost_ratio` 0.9657, `compute_efficiency` 0.6954 — i.e. class-A per-step economics but roughly two thirds of the class-A run length. It failed `C-PERTURBATION-REACHED`, `conformance_fraction` dropped to 0.5, `task_pass` went to 0.0, and it produced the worst reward on record, 0.4911. Note that attempt 9 also reported a `qualifying_budget` of 49.89 s but a full 74.39 s wall clock and was clean at 0.8332, which distinguishes "reached the target early" from "was given only 50 s of wall clock."

# 3. Checks that failed

Two named checks failed, each in exactly one record. Nine of eleven records had an empty `failed_checks` list.

**`C-API-SURFACE` — attempt 6.** Verifier reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions."* This is a structural check on the submission file: the module body may contain imports, constant assignments, and permitted definitions (functions/classes) and nothing else. Attempt 6 placed executable statements at module level. Consequence in the record: `rule_conformance` 0.8571 (six of seven rules held), `task_pass` 0.0, reward 0.7580 despite both perturbation runs reaching their thresholds and `primary_target_reached` being 1.0. This check has failed once.

**`C-PERTURBATION-REACHED` — attempt 7.** Verifier reason, verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* `conformance_fraction` 0.5, `all_perturbations_held` false, `task_pass` 0.0, reward 0.4911. This check has failed once.

**`C-BUDGET-RESPECTED` — inside a perturbation unit of attempt 7.** This is the check that stopped the individual held-out run, and it is the proximate cause of the `C-PERTURBATION-REACHED` failure above. It has failed once, at the unit level.

Because each named check has failed exactly once, no check is yet a repeat finding, and no claim can be made that any of them is insensitive to what was changed between attempts. What can be said is the converse and it is important: the nine clean attempts show that a fully conformant submission in this family is routinely achievable, so both failures were self-inflicted departures from a known-conformant shape rather than an unavoidable property of the task.

# 4. Ruled-out directions

**Maximising `compute_efficiency` by cutting per-step cost to ~0.69.** Ruled out by attempts 4 (0.7740) and 11 (0.8067), a two-record replication. Attempt 11 reached `compute_efficiency` 1.0000, the ceiling of that term, and still scored 0.0591 below attempt 5. The efficiency term is not what the reward is dominated by, and buying it at the price of per-step work is a net loss. Do not chase `per_step_cost_ratio` below ~0.94.

**Extending the run to ~99 s wall clock at above-parity per-step cost.** Ruled out by attempt 8 (0.7805), which was fully clean and `task_pass` 1.0 yet regressed 0.0853 from attempt 5. More wall clock did not convert into reward.

**Module-level executable statements.** Ruled out by attempt 6 via `C-API-SURFACE`. Restrict the module body to imports, constants, and function/class definitions; put all execution inside the permitted entry points. This is a hard structural constraint, not a tunable.

**Compressing the run to ~50 s wall clock.** Ruled out by attempt 7, the worst record at 0.4911. The held-out variant run could not respect its budget at that length and `C-BUDGET-RESPECTED` stopped it, which dropped `conformance_fraction` to 0.5. The per-perturbation budgets need the ~74 s-class envelope.

**Very high per-step cost (ratio ~1.41).** Ruled out by attempt 6, which combined it with the `C-API-SURFACE` violation; even setting the conformance failure aside, `compute_efficiency` collapsed to 0.4942 and the reward was 0.7580.

**Re-running the class-A configuration unchanged in the hope of a better number.** Attempts 3 and 5 differ by 0.0001 in reward with near-identical cost terms; that is the observed noise floor of a repeated class-A configuration. Another identical run is not an improvement strategy.

# 5. Open leads

**Restore the attempt-5 operating point exactly, as the floor.** Target signature: `per_step_cost_ratio` ≈ 0.958, `compute_efficiency` ≈ 0.693, wall clock ≈ 74.4 s, all module-level code confined to imports/constants/definitions, both declared perturbations reaching threshold within their own budgets. That reproduces 0.8658 and everything else must be measured against it. Attempt 3 (ratio 0.9835, 0.8657) shows the point is not knife-edge in the ratio.

**Search only inside the ratio band 0.94–1.08 at ~74 s.** The six class-A records span rewards 0.8079–0.8658 with ratios 0.9441–1.0723, and the mapping from ratio to reward inside that band is not monotone: 0.9441→0.8079, 0.9516→0.8332, 0.9581→0.8658, 0.9615→0.8503, 0.9835→0.8657, 1.0723→0.8630. That non-monotonicity means the ratio is a symptom, not the lever; the 0.058 spread inside class A is being driven by something the reported terms do not name. The lead is to change the learning algorithm's quality at approximately fixed cost — better optimisation schedule, better initialisation, better regularisation — and confirm the cost terms stay in band rather than trying to move the cost terms themselves.

**Exploit the headroom that `primary_target_reached` = 1.0 everywhere implies.** The primary target was met in all eleven runs, including both non-`task_pass` ones. Nothing is gained by making the primary objective easier or by finishing it sooner: attempt 9 reached its qualifying budget at 49.89 s inside a 74.39 s run and scored 0.8332, below attempt 5's 0.8658 at a 74.38 s qualifying budget. Reward is not paying for early completion, so use the full envelope for solution quality.

**Guard both failure modes explicitly in the next submission.** Before submitting, assert that the module body contains no statements other than imports, constant assignments and definitions (`C-API-SURFACE`), and that the per-perturbation work fits each unit's own budget at the ~74 s envelope (`C-BUDGET-RESPECTED`, which is what gates `C-PERTURBATION-REACHED`). Each of these cost a full `task_pass` when violated, and `task_pass` 0.0 accompanied the two lowest-but-one and lowest rewards on record.

**Perturbation outcomes, reported by kind and in aggregate.** Two perturbation units were declared in every record, one of kind `seed` and one of kind `held_out_variant`, giving 22 held-out runs across the eleven records. In aggregate, 21 of 22 reached their threshold. By kind: all 11 `seed` runs reached, with no failed checks recorded on any of them — the seed kind has never been a problem. The `held_out_variant` kind reached in 10 of 11 records; the single failure was in attempt 7, stopped by `C-BUDGET-RESPECTED`. The runs are not identified across records, so nothing here should be read as the same individual run recurring; the finding is at the level of kind. The kind that is failing is `held_out_variant`, and the check it fails on is `C-BUDGET-RESPECTED`, and it did so only in the compressed-budget configuration.

**Call: exploit.** The best-scoring family, class A, is well characterised and cheap to re-establish, and the last six attempts regressed by wandering outside it — into cost-minimisation (4, 11), a longer run (8), a heavier non-conformant structure (6) and a compressed budget (7). Return to the attempt-5 operating point and make one substantive change to the learning algorithm's quality per attempt while holding `per_step_cost_ratio` in 0.94–1.08 and wall clock near 74 s. Explore is not warranted yet: class A has produced 0.8658 and has never been probed by anything other than cost-side tuning, so its ceiling is untested. What must not be repeated is the pattern of the last six attempts — changing the cost envelope, which is the one dimension already shown to be the wrong lever.
