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

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3        0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                
  5 *      0.8658   1.000             2 of 2         yes             74                
  6        0.7580   0.857             2 of 2         yes             46                

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

    attempt 4 -- reward 0.7740, worse than an earlier attempt
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Six graded submissions, all six with `measurement_status: "measured"`. Every one carries a reward; none is missing a measurement. Ordered worst to best:

| Rank | Attempt | reward | Standing as reported |
|---|---|---|---|
| 1 (worst) | 6 | 0.7580 | worse_than_an_earlier_attempt |
| 2 | 4 | 0.7740 | worse_than_an_earlier_attempt |
| 3 | 2 | 0.8079 | worse_than_an_earlier_attempt |
| 4 | 1 | 0.8630 | first_measured_attempt |
| 5 | 3 | 0.8657 | better_than_every_earlier_attempt |
| 6 (best) | 5 | 0.8658 | better_than_every_earlier_attempt |

**Attempt 5 holds the highest reward, 0.8658, and it is the one to beat.** Attempt 3, at 0.8657, is a hair below it — a gap of about 0.0001, which should be read as the same plateau rather than as an improvement over attempt 3.

Three attempts scored *below* an earlier attempt and must be recorded as regressions, not progress: attempt 2 (0.8079) fell below attempt 1 (0.8630); attempt 4 (0.7740) fell below attempts 1, 2 and 3; attempt 6 (0.7580) is the lowest reward recorded and fell below every prior attempt.

Supporting terms, for grounding the classes below:

- Attempt 1: compute_efficiency 0.6784, per_step_cost_ratio 1.0723, qualifying_budget 76.337 s, wall_clock 76.337 s, task_pass 1.0, rule_conformance 1.0.
- Attempt 2: compute_efficiency 0.7226, per_step_cost_ratio 0.9441, qualifying_budget 74.257 s, wall_clock 74.257 s, task_pass 1.0, rule_conformance 1.0.
- Attempt 3: compute_efficiency 0.6922, per_step_cost_ratio 0.9835, qualifying_budget 74.368 s, wall_clock 74.368 s, task_pass 1.0, rule_conformance 1.0.
- Attempt 4: compute_efficiency 0.9681, per_step_cost_ratio 0.6934, qualifying_budget 73.744 s, wall_clock 73.744 s, task_pass 1.0, rule_conformance 1.0.
- Attempt 5: compute_efficiency 0.6926, per_step_cost_ratio 0.9581, qualifying_budget 74.378 s, wall_clock 74.378 s, task_pass 1.0, rule_conformance 1.0.
- Attempt 6: compute_efficiency 0.4942, per_step_cost_ratio 1.4094, qualifying_budget 45.817 s against wall_clock 70.371 s, task_pass 0.0, rule_conformance 0.8571.

Constant across all six records: `validity` 1.0, `red_line_crossed` 0.0, `primary_target_reached` 1.0, `zero_reason_code` 0, `perturbations_declared` 2.0, `all_perturbations_held` true. No attempt has ever failed to reach the primary target, and no attempt has ever been zeroed.

## 2. Approach classes tried

The measured terms describe outcomes, not source code, so these classes are grouped by their measured cost/efficiency signature. Where I name a distinguishing feature I name only what the terms actually record.

**Class A — baseline, slower-than-reference per step (attempt 1, reward 0.8630).** per_step_cost_ratio 1.0723, i.e. each step cost about 7% more than the harness reference; compute_efficiency 0.6784, the second-lowest among conformant runs. Longest wall clock of the set at 76.34 s. Fully conformant, both perturbation units held. This was the first measured attempt and set the bar at 0.8630.

**Class B — moderate cost trim (attempt 2, reward 0.8079).** per_step_cost_ratio pulled down to 0.9441 and compute_efficiency raised to 0.7226 relative to class A, wall clock cut by ~2.1 s. Fully conformant. The reward fell 0.055 below class A. Whatever cheapening produced the cost gain cost more in the reward's dominant term than the efficiency term returned.

**Class C — balanced mid-cost configuration (attempts 3 and 5, rewards 0.8657 and 0.8658).** These two records are near-identical in every measured term: compute_efficiency 0.6922 / 0.6926, per_step_cost_ratio 0.9835 / 0.9581, qualifying_budget 74.368 s / 74.378 s, full conformance, both perturbation units held in each. This is the best class and it produced both of the only two "better_than_every_earlier_attempt" standings. The 0.0001 separation between them says the class has flattened out: whatever differed between attempt 3 and attempt 5 moved per_step_cost_ratio by 0.025 and moved reward essentially not at all.

**Class D — aggressive compute reduction (attempt 4, reward 0.7740).** The extreme of the cost axis: per_step_cost_ratio 0.6934 (about 31% cheaper per step than reference) and compute_efficiency 0.9681, by far the highest efficiency recorded, with the shortest wall clock at 73.74 s. Fully conformant, both perturbation units held, primary target still reached. Reward nonetheless dropped to 0.7740, 0.092 below class C. This is the cleanest single data point in the set: maximising compute_efficiency actively destroys reward.

**Class E — heavier per-step work plus module-level execution (attempt 6, reward 0.7580, the worst recorded).** per_step_cost_ratio 1.4094 (about 41% more expensive per step than reference) and compute_efficiency 0.4942, both the worst of the set. Uniquely, this attempt failed a conformance check (see section 3), drove rule_conformance to 0.8571 and task_pass to 0.0, and is the only record where qualifying_budget (45.82 s) diverges from wall_clock (70.37 s) — roughly 24.5 s of the run did not qualify. Its perturbation units still both reached their thresholds.

**Reward structure, as far as the terms support it.** Reward is not monotone in compute_efficiency. Ranking the five conformant attempts by efficiency gives 0.6784 (A, 0.8630), 0.6922 (C, 0.8657), 0.6926 (C, 0.8658), 0.7226 (B, 0.8079), 0.9681 (D, 0.7740) — the two best rewards sit in the middle of the efficiency range, and the highest efficiency gives the second-worst reward. Wall clock across all conformant runs spans only 73.74–76.34 s, a 2.6 s spread, while reward spans 0.092; speed alone therefore cannot explain the ranking. The inescapable reading is that reward is dominated by a task-quality term that is not exposed in these records, with compute cost a secondary contributor. I cannot say from these terms which code change moved that quality term, and the next attempt should not assume it can be inferred from the cost numbers alone.

## 3. Checks that failed

One check has ever failed, in one record.

**C-API-SURFACE** — attempt 6. Verifier reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions"*. This has failed once, in attempt 6 only; attempts 1 through 5 recorded empty `failed_checks` and rule_conformance 1.0. The failure took rule_conformance from 1.0 to 0.8571 (six of seven checks held) and drove `task_pass` from 1.0 to 0.0 even though `primary_target_reached` remained 1.0 — the model trained and hit its target, and the submission was still marked as not passing because of the module surface. It is also the only record where qualifying_budget (45.82 s) is far below wall_clock (70.37 s), so roughly a third of the run's elapsed time did not count toward the qualifying budget.

Concretely, this check requires that the submission module, at import time, contain nothing but imports, constant assignments, and permitted definitions (function and class definitions). Any executable statement at module scope — a print, a call, a loop, a device probe, a seed call, a dataset load, an `if`/`try` block, or configuration built by running code at top level — trips it. Every piece of setup must live inside the entry-point function or another permitted definition.

No perturbation-related check has ever failed, and no other named check appears anywhere in the records.

## 4. Ruled-out directions

- **Maximising compute_efficiency / minimising per-step cost.** Attempt 4 reached compute_efficiency 0.9681 and per_step_cost_ratio 0.6934, the best cost figures recorded, and scored 0.7740 — 0.092 below the best. Cutting per-step work to roughly two-thirds of reference is a large net loss.
- **Moderate cost trimming toward per_step_cost_ratio ≈ 0.94.** Attempt 2 sits at 0.9441 with efficiency 0.7226 and scored 0.8079, 0.055 below attempt 1 and 0.058 below the best. The cost axis below about 0.95 is losing territory.
- **Any module-level executable statement in the submission file.** Attempt 6 failed C-API-SURFACE on exactly this and took task_pass to 0.0, rule_conformance to 0.8571, and lost about 24.5 s of qualifying budget. There is no version of this that is worth retrying.
- **Raising per-step cost well above reference (per_step_cost_ratio ≈ 1.41).** Attempt 6 also carried the worst efficiency, 0.4942, and the worst reward, 0.7580. Attempt 1's 1.0723 was tolerable at 0.8630; 1.41 was not.
- **Optimising wall clock as such.** Conformant wall clocks range 73.74–76.34 s while rewards range 0.7740–0.8658; the fastest run scored second-worst. Shaving seconds is not the lever.
- **Anything aimed at perturbation robustness or at the validity / red-line terms.** See section 5 for the aggregate; all of these are already saturated and there is no headroom to buy there.

## 5. Open leads

**Perturbation status first, because it constrains what is worth spending effort on.** Every record declared 2 perturbation units, and every record reports both as reached with empty `failed_checks`. By kind: all `held_out_variant` runs across all six records reached their thresholds, with no check stopping any of them; all `seed` runs across all six records likewise reached their thresholds, with no check stopping any of them. In aggregate that is 12 of 12 units held, and `all_perturbations_held` is true in all six records — including attempt 6, whose primary run failed C-API-SURFACE. The held-out runs are not identified in any record, so nothing links a unit in one record to a unit in another; the safe statement is by kind, and by kind there is nothing failing. No effort should go into generalisation or seed-stability hardening, and no reward should be traded away to buy robustness that is already fully paid for.

Leads worth taking:

1. **Re-establish the class C configuration as the floor, and do it exactly.** Target the attempt-5 signature: per_step_cost_ratio in the 0.95–0.99 band, compute_efficiency near 0.69, wall clock near 74.4 s, full conformance. Reproducing 0.8658 is the first milestone; every variation should be measured against it, not against 0.8630.

2. **Move on the quality term, not the cost term.** The cost axis has been mapped at 0.69, 0.94, 0.96, 0.98, 1.07 and 1.41, and the best two results are both at ~0.96–0.98 with rewards separated by 0.0001. Class C has stopped improving along cost. Any further gain has to come from the unreported task-quality component: better final metric at the primary target, at roughly unchanged per-step cost. Concretely, that means spending the *same* compute better — schedule shape, optimiser/momentum settings, augmentation or regularisation, batch composition, initialisation, EMA or weight averaging at the end of training — rather than spending less of it.

3. **Probe the untested band between class C and class A.** per_step_cost_ratio 0.98 (attempt 3, 0.8657) and 1.07 (attempt 1, 0.8630) bracket a region with no sample in it. Spending slightly more per step than class C, up to about ratio 1.02–1.05, is the one cost direction not yet shown to be harmful; attempt 1 shows it degrades only mildly, so if extra per-step work buys a real quality gain it may net positive. Keep it below the 1.41 that produced the worst result.

4. **Hold the module surface clean by construction.** Top level of the submission: `import` statements, plain constant assignments, `def` and `class` only. All device selection, seeding, data loading, config assembly, logging and any conditional logic go inside the entry-point function. This alone is what separates attempt 6's task_pass 0.0 from the rest of the set.

5. **Do not chase validity, red-line or primary-target terms.** `validity` is 1.0, `red_line_crossed` is 0.0 and `primary_target_reached` is 1.0 in every record including the failing one. There is no headroom in any of them.

**Call: exploit.** The best-scoring class (attempt 5, 0.8658, and attempt 3, 0.8657) is intact, fully conformant, and its one adjacent failure mode — C-API-SURFACE — is precisely identified and trivially avoidable. Rebuild that configuration, keep the module surface to imports, constants and definitions, and spend the improvement effort on training quality at roughly constant per-step cost. The one caution is that class C is already flat along the cost axis, so an exploit that only re-tunes cost will reproduce 0.8658 and no more; the exploit has to touch the quality term. Repeating a cost-reduction sweep of the kind that produced attempts 2 and 4, or resubmitting anything with module-level execution, would be neither exploration nor exploitation — those are the two things already shown to lose reward.
