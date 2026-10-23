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

    All six attempts since have scored lower than it.
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
  6 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 4 -- reward 0.8719, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
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

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

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

## 1. Results so far

Eleven graded records, all with `measurement_status: "measured"`; every one therefore carries a reward. None of the records is unmeasured, so no attempt below should be read as "absent" and none of the zeros should be read as a missing measurement — the four zeros are genuine measured zeros.

Worst to best by reward:

| Rank | Attempt | Reward | Notes |
|---|---|---|---|
| 1 (worst) | 3 | 0.0000 | zero_reason_code 4; wall clock 1692.52 s; primary target not reached; 0 of 2 perturbations reached |
| 1= | 7 | 0.0000 | zero_reason_code 4; wall clock 1692.21 s; same failure signature |
| 1= | 9 | 0.0000 | zero_reason_code 4; wall clock 1692.97 s; same failure signature |
| 1= | 10 | 0.0000 | zero_reason_code 4; wall clock 1690.96 s; same failure signature |
| 5 | 6 | 0.5615 | target and both perturbations reached, but C-API-SURFACE failed; rule_conformance 0.8571, task_pass 0; qualifying budget 204.09 s, per_step_cost_ratio 1.3778 |
| 6 | 8 | 0.7551 | fully conforming, task_pass 1; qualifying budget 78.14 s but wall clock 151.50 s (the only record where the two diverge) |
| 7 | 1 | 0.7684 | C-API-SURFACE failed; rule_conformance 0.8571, task_pass 0; qualifying budget 25.46 s |
| 8 | 2 | 0.8385 | fully conforming; qualifying budget 73.62 s; per_step_cost_ratio 0.9162 |
| 9 | 4 | 0.8719 | fully conforming; qualifying budget 50.03 s; compute_efficiency 1.0000; per_step_cost_ratio 0.7115 |
| 10 | 11 | 0.8980 | fully conforming; qualifying budget 25.35 s; per_step_cost_ratio 1.0502; compute_efficiency 0.7043 |
| 11 (best) | 5 | **0.9128** | fully conforming; qualifying budget 25.34 s; per_step_cost_ratio 0.9887; compute_efficiency 0.7728 |

**Attempt 5 holds the highest reward at 0.9128 and is the one to beat.**

Direction of movement, stated plainly. Attempt 2 (0.8385) improved on attempt 1 (0.7684). Attempt 3 (0.0000) was worse than every earlier attempt. Attempt 4 (0.8719) improved on all earlier. Attempt 5 (0.9128) improved again and set the standing best. Attempt 6 (0.5615) was **worse** than the then-best 0.9128 — a large regression, not progress. Attempts 7, 9 and 10 (all 0.0000) were **worse** than earlier attempts. Attempt 8 (0.7551) was **worse** than earlier attempts, scoring below attempts 2, 4, 5 and even below attempt 1. Attempt 11 (0.8980) was **worse** than attempt 5, not an improvement. Since attempt 5, nothing has beaten it: the six records after it are four zeros, one 0.5615, one 0.7551 and one 0.8980.

Constant across every record: `validity` 1.0 and `red_line_crossed` 0.0. No attempt has ever been invalid and no attempt has ever crossed a red line. `perturbations_declared` is 2.0 in every record.

## 2. Approach classes tried

The records collapse into four distinct classes by their measured signature. Records with the same signature are one entry.

**Class A — fast conforming solver, ~25 s to threshold (attempts 5 and 11; attempt 1 is the same speed class but non-conforming).** Qualifying budget clusters tightly at 25.34 s, 25.35 s and 25.46 s. Fully conforming instances scored 0.9128 (attempt 5) and 0.8980 (attempt 11). Both reached the primary target and both perturbations. This class contains the best result. The two conforming members differ only in cost terms: attempt 5 had per_step_cost_ratio 0.9887 and compute_efficiency 0.7728 for 0.9128; attempt 11 had per_step_cost_ratio 1.0502 and compute_efficiency 0.7043 for 0.8980. That ~0.015 reward gap at identical wall clock is the cleanest signal in the data that per-step cost, not just total time, moves the reward.

**Class B — conforming solver at 50–78 s to threshold (attempts 2, 4, 8).** All three reached the primary target and both perturbations with rule_conformance 1.0 and task_pass 1. Rewards fall monotonically with time-to-threshold: 50.03 s → 0.8719 (attempt 4, compute_efficiency 1.0000, per_step_cost_ratio 0.7115), 73.62 s → 0.8385 (attempt 2, per_step_cost_ratio 0.9162), 78.14 s → 0.7551 (attempt 8, per_step_cost_ratio 1.0291). Attempt 8 is the informative outlier: its qualifying budget was 78.14 s but its wall clock was 151.50 s, roughly double, and it scored 0.0834 below attempt 2 which had a nearly identical qualifying budget of 73.62 s. Work performed after the qualifying row appears to be paid for.

**Class C — module-level executable code (attempts 1 and 6).** These solved the problem correctly — primary_target_reached 1.0, both perturbations reached, all_perturbations_held true — but failed C-API-SURFACE, which pinned rule_conformance to 0.8571 (6 of 7) and task_pass to 0. Attempt 1 was otherwise a Class A run (25.46 s) and scored 0.7684 against attempt 5's 0.9128 for the same speed; attempt 6 was a slow instance (204.09 s qualifying budget, per_step_cost_ratio 1.3778) and scored 0.5615. The conformance failure costs roughly 0.14 reward at equal speed, on top of any speed penalty.

**Class D — long-running search that never crosses the threshold (attempts 3, 7, 9, 10).** All four ran to almost exactly the same wall clock — 1692.52 s, 1692.21 s, 1692.97 s, 1690.96 s — which looks like a hard time cap rather than a chosen stopping point. All four scored 0.0000 with zero_reason_code 4, conformance_fraction 0.0, primary_target_reached 0.0, and 0 of 2 perturbations reached. Their per_step_cost_ratio values (0.8484, 0.8407, 0.8901, 0.7961) and compute_efficiency values (0.9672, 1.0000, 1.0000, 0.9833) were good — cheap per step, but never producing an evaluation row that crosses the threshold in the declared direction. Cheap steps that never converge earn nothing. This class was tried four separate times and produced zero every time.

## 3. Checks that failed

**C-API-SURFACE** — "module-level statements outside imports, constants, and permitted definitions". Failed **twice**, in attempts 1 and 6. These attempts differ in essentially every performance term: attempt 1 had a 25.46 s qualifying budget and per_step_cost_ratio 1.0639, attempt 6 had 204.09 s and per_step_cost_ratio 1.3778. Whatever was changed between them — the solver speed, the step cost, the compute efficiency — is **not** what causes this check to fail. It is a purely structural property of the submission file: something executable sits at module scope. Each failure set rule_conformance to 0.8571 (6 of 7 rules) and task_pass to 0 while leaving the target and both perturbations reached. Notably, C-API-SURFACE never appears in any perturbation unit's failed_checks — it is evaluated once against the submission surface, not per run.

**C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction". Failed **four times** on the primary run (attempts 3, 7, 9, 10) and **eight further times** across the perturbation units of those same four records. This is the single most-repeated failure in the record set. The four attempts differ in their cost terms (per_step_cost_ratio 0.7961 to 0.8901, compute_efficiency 0.9833 to 1.0000) yet all fail identically, so whatever was varied between them is **not** what is causing it: none of those variations produced a threshold crossing.

**C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". Failed **four times** on the primary run and **eight times** across perturbation units, always in the same records as C-TARGET-REACHED. This is a consequence, not an independent problem: with no crossing row there is no qualifying row, so `qualifying_budget` is reported as "not-measured" in those four records. Fixing C-TARGET-REACHED fixes this one.

**C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed **four times**, in the same four records. Never a partial failure: it is always 0 of 2, never 1 of 2.

Perturbation outcomes. Every record declares 2 held-out runs beside the primary one, one of kind `held_out_variant` and one of kind `seed`, giving 22 held-out runs in total across the eleven records. **Aggregate: 14 of 22 reached their threshold, 8 did not.** By kind: of the 11 `held_out_variant` runs, 7 reached and 4 did not; of the 11 `seed` runs, 7 reached and 4 did not. Every one of the 8 failures was stopped by the same pair, C-TARGET-REACHED and C-BUDGET-RESPECTED, and all 8 occurred inside the four Class D records where the primary run also failed to reach the target. Both kinds fail at exactly the same rate and on exactly the same checks, so there is no kind-specific weakness — the held-out variant is not harder than the seed variation, or vice versa. There is no record in which the primary run reached the target and a held-out run did not; `all_perturbations_held` is true in all seven records where the primary target was reached. Generalisation to held-out runs has never been the bottleneck; reaching the threshold at all has been.

## 4. Ruled-out directions

**Long unbounded search to the wall-clock cap (Class D).** Ruled out: tried four times (attempts 3, 7, 9, 10), scored 0.0000 every time, each terminating at ~1691–1693 s, which is the cap rather than a convergence point. In all four, C-TARGET-REACHED failed on the primary run and on both held-out runs, and there is no partial credit — conformance_fraction was 0.0 despite rule_conformance being 1.0. Their good per-step economics (per_step_cost_ratio down to 0.7961, compute_efficiency up to 1.0000) bought nothing. Spending more wall clock is not how the threshold gets crossed, and repeating this class without changing what prevents the crossing is neither exploration nor exploitation — it is the loop's most repeated waste, four records for zero reward.

**Any executable statement at module scope.** Ruled out: C-API-SURFACE failed on it twice (attempts 1 and 6), and the cost is severe even when the algorithm is correct — attempt 1 reached the target and both perturbations in 25.46 s, a Class A time, yet scored 0.7684 against 0.9128 for the conforming Class A attempt 5. Keep the module body to imports, constants, and function/class definitions only; put all work inside the entry points.

**Continuing to run after the qualifying row (attempt 8's pattern).** Ruled out: attempt 8 was fully conforming and passed, but its wall clock of 151.50 s was roughly double its 78.14 s qualifying budget, and it scored 0.7551 against attempt 2's 0.8385 at a comparable 73.62 s qualifying budget. Post-crossing work is charged against the score.

**Slow conforming solvers in the 50 s and up range (Class B) as a route to the top.** Ruled out as a path to beating 0.9128: the best of them, attempt 4, achieved a perfect compute_efficiency of 1.0000 and the lowest per_step_cost_ratio ever recorded (0.7115) and still only reached 0.8719, below both Class A conforming results. Time-to-threshold dominates.

**Reducing compute_efficiency in exchange for a lower per-step cost, at fixed wall clock.** Not ruled out outright, but attempt 11 is evidence against the way it was done there: at the same ~25.3 s budget as attempt 5, attempt 11 had a worse per_step_cost_ratio (1.0502 vs 0.9887) and worse compute_efficiency (0.7043 vs 0.7728) and lost 0.0148 reward. Whatever attempt 11 changed relative to the Class A recipe made both cost terms worse.

## 5. Open leads

**Rebuild the Class A conforming solver and drive per-step cost down at the ~25 s time-to-threshold.** This is the highest-value lead. Attempt 5 (best, 0.9128) reached the threshold in 25.34 s with per_step_cost_ratio 0.9887 and compute_efficiency 0.7728. Attempt 4 separately demonstrated that per_step_cost_ratio 0.7115 and compute_efficiency 1.0000 are achievable within this harness. Neither term is at its demonstrated ceiling in the best record. If the ~25 s crossing time can be held while per_step_cost_ratio moves toward 0.71 and compute_efficiency toward 1.0, the result should exceed 0.9128. Concretely: keep whatever schedule gets a crossing row at ~25 s, but make each step cheaper (smaller batches per step, fewer redundant forward passes, avoid recomputing evaluation metrics more often than the crossing detection requires).

**Treat ~25.3 s as a possible floor and probe below it carefully.** Three separate attempts (1, 5, 11) produced qualifying budgets of 25.46 s, 25.34 s and 25.35 s — a suspiciously tight cluster that may be a structural floor (a minimum evaluation cadence, or a fixed setup cost) rather than a coincidence. It is worth one probe at a deliberately more aggressive schedule to learn whether a crossing can be registered earlier than ~25 s at all. If the floor is real, all remaining headroom is in the cost terms, which redirects effort to the lead above.

**Stop the run the moment the qualifying row is produced.** Attempt 8's 151.50 s wall clock against a 78.14 s qualifying budget cost it roughly 0.08 reward relative to attempt 2. Whatever the entry point does, it should return as soon as the threshold has been crossed in the declared direction, with no trailing epochs, no final full-dataset evaluation, and no cleanup that touches the model.

**Guard the module surface mechanically.** C-API-SURFACE has now failed twice for the same structural reason. Before finalising, read the submission top to bottom and confirm the module body contains only imports, constant assignments, and `def`/`class` definitions — no calls, no `if` blocks, no logging setup, no seeding, no device selection, no `torch.set_*` at module scope. Move all of that inside the functions. This check is independent of every performance term and is free to satisfy.

**Verify a crossing row exists before optimising anything else.** The four zero-reward records all failed C-TARGET-REACHED with "no evaluation row crosses the threshold in the declared direction". Two things are worth checking explicitly in the next attempt: that evaluation rows are actually emitted at a cadence that lets one be seen, and that the metric is reported in the declared direction (a sign or minimise/maximise inversion would produce exactly this message even with a well-trained model). Since the held-out runs failed on the same check in the same records and never independently, one fix here restores all three of C-TARGET-REACHED, C-BUDGET-RESPECTED and C-PERTURBATION-REACHED at once.

**Recommendation: exploit.** Attempt 5's approach class is conforming, reaches the primary target, holds both the held-out variant and the seed perturbation, and stands at 0.9128 as the mark to beat. It has not stopped improving in the sense that matters — its own cost terms (compute_efficiency 0.7728, per_step_cost_ratio 0.9887) sit well below values already demonstrated elsewhere in the record set, so measurable headroom exists inside the approach that already scored. The next attempt should reconstruct the fast conforming Class A solver, keep every line of executable code out of module scope, return immediately on the crossing row, and spend its effort on lowering per-step cost at a fixed ~25 s time-to-threshold. Explore is not warranted while that headroom is unclaimed, and in particular the ~1692 s search class must not be re-run: it has been attempted four times without changing what prevents the threshold crossing, and it scored 0.0000 each time.
