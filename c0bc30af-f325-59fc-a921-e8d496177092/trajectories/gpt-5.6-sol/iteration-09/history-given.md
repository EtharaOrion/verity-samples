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

    All three attempts since have scored lower than it.
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
  2 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 6 -- reward 0.7580, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 46
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 7 -- reward 0.4911, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 8 -- reward 0.7805, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 99
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED failed on attempt 7.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Eight graded submissions, all with `measurement_status: "measured"`, so every one carries a reward. Ordered worst to best:

| Rank (worst→best) | Attempt | reward | Notes |
|---|---|---|---|
| 1 | Attempt 7 | 0.4911 | worse than an earlier attempt; `task_pass` 0.0; a held-out perturbation did not hold |
| 2 | Attempt 6 | 0.7580 | worse than an earlier attempt; `task_pass` 0.0; `rule_conformance` 0.8571 |
| 3 | Attempt 4 | 0.7740 | worse than an earlier attempt; clean conformance |
| 4 | Attempt 8 | 0.7805 | worse than an earlier attempt; clean conformance |
| 5 | Attempt 2 | 0.8079 | worse than an earlier attempt; clean conformance |
| 6 | Attempt 1 | 0.8630 | first measured attempt |
| 7 | Attempt 3 | 0.8657 | better than every earlier attempt at the time |
| 8 | Attempt 5 | **0.8658** | better than every earlier attempt; **highest reward, this is the one to beat** |

Exact values to four decimals: attempt 1 = 0.8630, attempt 2 = 0.8079, attempt 3 = 0.8657, attempt 4 = 0.7740, attempt 5 = 0.8658, attempt 6 = 0.7580, attempt 7 = 0.4911, attempt 8 = 0.7805.

Attempt 5 (0.8658) is the target to beat. Note plainly that five of the eight attempts scored *lower* than an attempt that preceded them — attempts 2, 4, 6, 7 and 8 all carry `standing_against_best_so_far: "worse_than_an_earlier_attempt"`, and that is a regression in each case, not incremental progress. Attempt 7 in particular is the worst result recorded, roughly 0.375 below the best. No record is missing a measurement; none of these should be read as a zero.

Supporting terms worth carrying forward, since reward does not track any single one of them:

- Attempt 1: `compute_efficiency` 0.6784, `per_step_cost_ratio` 1.0723, `wall_clock_sec` 76.34, reward 0.8630.
- Attempt 2: `compute_efficiency` 0.7226, `per_step_cost_ratio` 0.9441, `wall_clock_sec` 74.26, reward 0.8079.
- Attempt 3: `compute_efficiency` 0.6922, `per_step_cost_ratio` 0.9835, `wall_clock_sec` 74.37, reward 0.8657.
- Attempt 4: `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934, `wall_clock_sec` 73.74, reward 0.7740.
- Attempt 5: `compute_efficiency` 0.6926, `per_step_cost_ratio` 0.9581, `wall_clock_sec` 74.38, reward 0.8658.
- Attempt 6: `compute_efficiency` 0.4942, `per_step_cost_ratio` 1.4094, `wall_clock_sec` 70.37, `qualifying_budget` 45.82, reward 0.7580.
- Attempt 7: `compute_efficiency` 0.6954, `per_step_cost_ratio` 0.9657, `wall_clock_sec` 50.05, reward 0.4911.
- Attempt 8: `compute_efficiency` 0.6575, `per_step_cost_ratio` 1.0848, `wall_clock_sec` 98.60, reward 0.7805.

`validity` is 1.0 and `red_line_crossed` is 0.0 in every record; `zero_reason_code` is 0 throughout. Nothing has ever tripped a red line, and no attempt has been zeroed.

# 2. Approach classes tried

The measured terms do not name the code, so the classes below are grouped by their measurable operating signature. Records with the same signature and the same outcome are one entry.

**Class A — the mid-budget, near-parity-cost configuration (attempts 1, 3, 5; also 2 as a variant).** Wall clock lands at 74–76 s, `qualifying_budget` equals wall clock, `per_step_cost_ratio` sits between 0.94 and 1.07, and `compute_efficiency` sits between 0.68 and 0.72. This class produced every reward above 0.80 and all three of the top scores: 0.8630, 0.8657, 0.8658. Within the class, attempts 3 and 5 are separated by 0.0001 (0.8657 vs 0.8658) — that gap is at or below the run-to-run noise floor and should not be read as a real improvement of one over the other. Attempt 2 sits in the same wall-clock band (74.26 s) with `per_step_cost_ratio` 0.9441 yet scored only 0.8079, which is the one datum showing the class is not uniformly safe: something other than budget placement moved it down 0.058.

**Class B — aggressive per-step compute reduction (attempt 4).** Pushed `per_step_cost_ratio` down to 0.6934, the lowest recorded, and `compute_efficiency` up to 0.9681, the highest recorded, at a wall clock of 73.74 s. Conformance was perfect, all perturbations held, `task_pass` 1.0 — and reward *fell* to 0.7740, roughly 0.092 below the best. Cheapening each step is measurably not what the reward rewards.

**Class C — extended wall clock (attempt 8).** Ran 98.60 s, the longest recorded, with `per_step_cost_ratio` 1.0848 and `compute_efficiency` 0.6575. Fully conformant, all perturbations held, `task_pass` 1.0, reward 0.7805 — 0.085 below the best. Spending more wall clock did not buy quality; it cost reward.

**Class D — configuration with module-level executable code (attempt 6).** Distinctive signature: `qualifying_budget` 45.82 against `wall_clock_sec` 70.37 (the only record where these diverge), `per_step_cost_ratio` 1.4094, `compute_efficiency` 0.4942, the lowest recorded. It failed `C-API-SURFACE`, drove `rule_conformance` to 0.8571 and `task_pass` to 0.0, and scored 0.7580. Both perturbation runs still held.

**Class E — tightened/shortened budget configuration (attempt 7).** Wall clock 50.05 s with `per_step_cost_ratio` 0.9657. The primary run reached its target (`primary_target_reached` 1.0) but a held-out run blew its own budget, `conformance_fraction` dropped to 0.5, `all_perturbations_held` went false, `task_pass` 0.0, reward 0.4911 — the worst result on record.

# 3. Checks that failed

Three named failures across eight records; five records (attempts 1, 2, 3, 4, 5, 8 — six records) had `failed_checks: []` and `conformance_fraction` 1.0.

- **`C-API-SURFACE`** — reason given by the verifier: *"module-level statements outside imports, constants, and permitted definitions."* Failed **once**, in attempt 6. It pulled `rule_conformance` to 0.8571 and `task_pass` to 0.0.
- **`C-PERTURBATION-REACHED`** — reason: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* Failed **once**, in attempt 7. `conformance_fraction` 0.5, `task_pass` 0.0.
- **`C-BUDGET-RESPECTED`** — recorded at the perturbation-unit level, not the top level, **once**, in attempt 7, on a held-out-variant run. This is the underlying cause of that attempt's `C-PERTURBATION-REACHED` failure: the variant run did not reach its threshold because it did not respect its own budget.

No check has failed in more than one record. There is therefore no recurring conformance defect to isolate: each failure is tied to a single, distinct submission, and the two clean-conformance classes (A, B, C) have never tripped either of them. `validity` held at 1.0 and `red_line_crossed` at 0.0 in all eight records, including the two failing ones.

**Perturbation-unit outcomes.** Every record declared 2 perturbations (`perturbations_declared` 2.0), one of kind `seed` and one of kind `held_out_variant`, giving 16 held-out runs in aggregate across the eight records.

- By kind — `seed`: 8 of 8 reached their threshold; zero failed checks recorded on any seed run. Seed perturbation has never been a failure mode.
- By kind — `held_out_variant`: 7 of 8 reached; the single non-reaching run failed on `C-BUDGET-RESPECTED`.
- Aggregate: 15 of 16 reached, one failure, and it was a held-out-variant run failing `C-BUDGET-RESPECTED`. `all_perturbations_held` is true in seven records and false in exactly one.

The runs are not identified by name, number or position, so nothing here should be read as tracking a particular run across records. The finding is about *kind*: the vulnerability is in held-out-variant runs, and the check they fail on is `C-BUDGET-RESPECTED`.

# 4. Ruled-out directions

- **Driving `per_step_cost_ratio` well below 1.0 to raise `compute_efficiency`.** Ruled out by attempt 4: it achieved the best `compute_efficiency` (0.9681) and the cheapest steps (0.6934) with perfect conformance and all perturbations held, and reward still fell to 0.7740, about 0.092 under attempt 5's 0.8658. Cheap steps are not rewarded on their own; whatever was sacrificed to get them costs more than the efficiency gains.
- **Extending wall clock past the ~75 s band.** Ruled out by attempt 8: 98.60 s, fully conformant, `task_pass` 1.0, reward 0.7805, about 0.085 under the best. More time did not translate into a better score.
- **Any module-level executable statement in the submission.** Ruled out by attempt 6: `C-API-SURFACE` fired with the reason *"module-level statements outside imports, constants, and permitted definitions"*, zeroing `task_pass` and cutting `rule_conformance` to 0.8571. Keep the module body to imports, constants, and permitted definitions; put all execution inside the permitted entry points.
- **Squeezing the run down toward ~50 s.** Ruled out by attempt 7: the primary target was still reached at 50.05 s, but the held-out-variant run failed `C-BUDGET-RESPECTED` and never reached its threshold, halving `conformance_fraction` and producing the worst reward on record, 0.4911. A budget that fits the primary run does not necessarily fit a held-out variant's own budget; there must be headroom.
- **Treating attempt 3 versus attempt 5 as a resolved comparison.** The 0.0001 difference is not a signal, and re-running that micro-difference to decide between them is not a productive direction.

# 5. Open leads

- **Rebuild the attempt-5 operating point and vary only the quality-side lever.** Target the signature that produced 0.8658: wall clock ~74.4 s, `qualifying_budget` equal to wall clock, `per_step_cost_ratio` in the 0.95–0.99 band, `compute_efficiency` ~0.69, no module-level statements, both perturbations declared. That band contains all three top scores and is the safest platform to build on.
- **Explain the attempt-2 anomaly.** Attempt 2 sat in the same wall-clock band (74.26 s) and a similar cost band (0.9441) as attempts 3 and 5, yet scored 0.8079 — 0.058 lower. Since budget placement was comparable, the difference must be in the algorithm's quality-producing content rather than in its cost profile. Identifying what distinguished attempt 2 from attempts 3/5 would point directly at the lever that actually moves reward, because it is a same-budget, different-reward pair.
- **Reward is not monotone in cost.** Attempt 1 with `per_step_cost_ratio` 1.0723 scored 0.8630 while attempt 2 at 0.9441 scored 0.8079, and attempt 4 at 0.6934 scored 0.7740. Cost ratio alone does not order the results, so tuning it further is unlikely to pay. Look for changes that improve the trained model's measured outcome at an unchanged ~74 s budget.
- **Protect held-out-variant budget headroom explicitly.** The only perturbation failure ever recorded was a held-out variant failing `C-BUDGET-RESPECTED`. Any change that shortens or tightens the schedule should be checked against the variant's own budget, not just the primary run's; keeping the primary near 74 s rather than near 50 s is the configuration under which the variant has always held.
- **Respect the noise floor.** Differences at the 1e-4 scale (attempts 3 vs 5) carry no information. Only pursue changes with a plausible effect substantially larger than that, and do not chase re-orderings within the 0.8657–0.8658 pair.

**Call: exploit.** The best-scoring class (Class A, attempt 5 at 0.8658) has not been exhausted — the attempt-2 anomaly shows a ~0.058 same-budget spread inside that class that has never been explained, which is a concrete, unexploited lever. The structurally different directions that have been tried (cheaper steps, longer runs, shorter runs) all measured *worse*, so exploring further along the cost axis is not warranted. Rebuild attempt 5's operating point, keep the module surface clean of executable statements, keep the ~74 s budget so the held-out variant retains headroom, and vary the quality-side content only.
