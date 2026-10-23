# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 2 -- reward 0.7155, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All two attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2 *      0.7155   1.000             2 of 2         yes             17                
  3        0.6279   1.000             2 of 2         yes             20                
  4        0.5792   1.000             2 of 2         yes             18                

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

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 3 -- reward 0.6279, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.5792, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 18
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Four graded submissions, all with `measurement_status: measured`, listed worst to best by reward:

- **Attempt 4 — reward 0.5792.** Lower than attempts 1, 2 and 3. The verifier records it as `worse_than_an_earlier_attempt`. This is a regression, not progress.
- **Attempt 3 — reward 0.6279.** Lower than attempts 1 and 2; also marked `worse_than_an_earlier_attempt`. A regression against the then-best.
- **Attempt 1 — reward 0.6694.** The first measured attempt, the baseline the rest are measured against.
- **Attempt 2 — reward 0.7155.** Marked `better_than_every_earlier_attempt`. **Attempt 2 holds the highest reward and is the one to beat.**

Every attempt passed the task: `task_pass` 1.0, `validity` 1.0, `primary_target_reached` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, `all_perturbations_held` true. No attempt failed to produce a measurement, and no attempt scored zero. So the entire spread between 0.5792 and 0.7155 comes from the graded quality/cost terms, not from correctness or conformance gating.

The secondary terms, per attempt:

| Attempt | reward | compute_efficiency | per_step_cost_ratio | wall_clock_sec / qualifying_budget |
|---|---|---|---|---|
| 1 | 0.6694 | 0.5488 | 1.5134 | 17.426 |
| 2 | 0.7155 | 0.6205 | 1.5175 | 17.453 |
| 3 | 0.6279 | 0.6033 | 1.5225 | 20.300 |
| 4 | 0.5792 | 0.8832 | 1.1656 | 17.512 |

Two facts stand out and should drive the next attempt. First, attempt 4 raised `compute_efficiency` sharply (0.5488 → 0.8832) and cut `per_step_cost_ratio` (≈1.52 → 1.1656), and reward *fell* to its lowest value of the four. Compute efficiency alone therefore does not buy reward; something else — the task-quality term that the reward aggregates beyond the pass/fail flags — was traded away to get it. Second, attempt 3 was the only run whose wall clock exceeded the ~17.4–17.5 s band (20.300 s, and `qualifying_budget` equals wall clock in every record), and it scored below both attempts 1 and 2 despite compute efficiency close to attempt 2's. Spending more wall clock did not pay.

# 2. Approach classes tried

The records carry no source, so these classes are grouped by their measured cost signature; the next attempt should treat them as cost/quality operating points rather than as named algorithms.

**Class A — the baseline-cost family (attempts 1, 2, 3).** All three sit at `per_step_cost_ratio` 1.5134 / 1.5175 / 1.5225, i.e. essentially one per-step cost regime, with compute efficiency varying from 0.5488 to 0.6205. This family produced the top three rewards, including the best (attempt 2 at 0.7155). Within the family, moving compute efficiency from 0.5488 to 0.6205 at unchanged wall clock (attempt 1 → attempt 2) gained +0.0461 reward. Moving to 0.6033 efficiency but stretching wall clock from ~17.45 s to 20.300 s (attempt 2 → attempt 3) lost −0.0876. So inside class A, efficiency gains at constant wall clock help and wall-clock inflation hurts.

**Class B — the aggressively cheap family (attempt 4, alone).** Per-step cost ratio dropped to 1.1656 and compute efficiency rose to 0.8832 at the same ~17.5 s wall clock. Reward 0.5792, the worst of the four. This is a distinct operating point, and it is the only evidence about it: cutting per-step cost by roughly a quarter cost about 0.136 reward relative to attempt 2.

**No third class exists in the data.** Four records, two classes.

# 3. Checks that failed

None. `failed_checks` is empty in all four records, and it is empty in all eight perturbation units as well. There is no repeated check, no named identifier, and no verifier reason to report, because the verifier raised none. Conformance was full (`conformance_fraction` 1.0, `rule_conformance` 1.0) in every attempt and no red line was crossed in any attempt.

On the held-out runs: each record declares `perturbations_declared` 2.0 and carries two `perturbation_units`, one of kind `held_out_variant` and one of kind `ruleset`. Across the four records that is eight units in total — four of kind `held_out_variant` and four of kind `ruleset`. Every one of them has `reached: true` and an empty `failed_checks`, and `all_perturbations_held` is true in all four records. In aggregate: 8/8 reached their thresholds, 4/4 by kind for each kind, and no check stopped any of them. No kind of held-out run is failing. The runs are not identified, so nothing here should be attributed to a particular run or treated as the same run across records.

The practical consequence: robustness is not the binding constraint. The next attempt does not need to spend anything defending conformance or the perturbations, and should spend its effort entirely on the reward's quality/cost terms.

# 4. Ruled-out directions

- **Chasing compute efficiency as the objective.** Ruled out by attempt 4: efficiency 0.8832 and per-step cost ratio 1.1656 — by far the cheapest run — produced the lowest reward, 0.5792, below the 0.5488-efficiency baseline of attempt 1 (0.6694). Reward is not monotone in compute efficiency, so any plan that mainly cuts per-step cost is expected to lose reward.
- **Driving `per_step_cost_ratio` down toward ~1.17.** Same evidence, stated as the lever: the only excursion away from the ~1.52 per-step cost band cost about 0.136 reward against the best. Stay in the ~1.51–1.52 band unless something else changes with it.
- **Buying quality with extra wall clock.** Ruled out by attempt 3: 20.300 s versus the ~17.43–17.51 s of the other three, and reward 0.6279, below both attempt 1 and attempt 2. Longer runs were penalised, not rewarded. Keep wall clock at or under roughly 17.5 s.
- **Hardening against conformance, ruleset or held-out-variant failures.** Ruled out because there is nothing to harden: zero failed checks across four records and eight perturbation units, all reached. Work spent here cannot raise reward and, if it costs time, will lower it.

# 5. Open leads

- **Rebuild attempt 2's operating point first and confirm 0.7155.** Its signature is the target to reproduce: `per_step_cost_ratio` ≈ 1.5175, `compute_efficiency` ≈ 0.6205, wall clock ≈ 17.45 s, full pass and conformance. The next attempt starts from a pristine stub and has none of this code, so re-establishing that point is prerequisite to beating it.
- **Push compute efficiency upward *within* the class-A cost band, holding wall clock at ~17.45 s.** The one clean comparison available (attempt 1 → attempt 2, efficiency 0.5488 → 0.6205 at identical per-step cost and wall clock, +0.0461 reward) says this axis pays. Attempt 4 says the payment stops somewhere before efficiency 0.88 / per-step cost 1.17. The unexplored region is efficiency roughly 0.62–0.75 with per-step cost still near 1.5. That interval has never been sampled and is the single most promising place to look.
- **Isolate which of the two changes in attempt 4 caused the loss.** Attempt 4 moved both per-step cost (1.52 → 1.17) and efficiency (0.60 → 0.88) at once, so the drop of 0.136 cannot be attributed. A run that changes only one of them — e.g. per-step cost held at ~1.52 while efficiency rises to ~0.75 — would tell the loop which lever is toxic and which is free.
- **Trim wall clock slightly below 17.4 s while keeping class-A per-step cost.** All four runs cluster at 17.43–17.51 s except the penalised 20.3 s run; sub-17.4 s has never been sampled, and `qualifying_budget` tracking wall clock exactly suggests time is scored directly. A small reduction that does not degrade the quality term is a cheap, low-risk gain.
- **Watch for the quality term explicitly.** Reward is clearly not explained by `compute_efficiency`, `per_step_cost_ratio`, `wall_clock_sec`, or any of the pass/conformance flags alone — the flags are saturated at 1.0 in every record and the cost terms move opposite to reward in attempt 4. There is an unobserved solution-quality component doing the work. Any change should be judged on whether it plausibly preserves or improves that component, not on its cost profile.

**Call: exploit.** Attempt 2 (reward 0.7155) is the standing best and it is not exhausted — the neighbourhood just above its compute efficiency, at its per-step cost band and its wall clock, has never been tested, and the two attempts that left that neighbourhood (3 and 4) both regressed for identifiable, reproducible reasons. Exploration is unwarranted while a scoring approach still has an untested improving direction and while nothing in the harness is blocking. Note also that attempts 3 and 4 each moved away from the best-known operating point and each came back worse; repeating that pattern — another excursion to cheaper per-step cost or longer wall clock without changing what caused those losses — would be neither exploit nor explore, and should not be done.
