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

    All two attempts since have scored lower than it.
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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED failed on attempt 7.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

All seven graded records carry `measurement_status: "measured"`, so all seven have a reward. None produced an absent measurement, and none was a zero: `zero_reason_code` is 0 and `red_line_crossed` is 0.0 in every record, and `validity` is 1.0 in every record.

Ordered worst to best by reward:

| Rank | Attempt | reward | Notes from the record |
|---|---|---|---|
| 1 (worst) | 7 | 0.4911 | `failed_checks`: C-PERTURBATION-REACHED. `task_pass` 0.0, `conformance_fraction` 0.50, `wall_clock_sec` 50.05. Worse than an earlier attempt. |
| 2 | 6 | 0.7580 | `failed_checks`: C-API-SURFACE. `task_pass` 0.0, `rule_conformance` 0.857, `per_step_cost_ratio` 1.4094, `compute_efficiency` 0.4942. Worse than an earlier attempt. |
| 3 | 4 | 0.7740 | Clean: no failed checks, `task_pass` 1.0. `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934 — the cheapest per step of any attempt. Worse than an earlier attempt. |
| 4 | 2 | 0.8079 | Clean. `compute_efficiency` 0.7226, `per_step_cost_ratio` 0.9441. Worse than an earlier attempt. |
| 5 | 1 | 0.8630 | Clean. First measured attempt. `compute_efficiency` 0.6784, `per_step_cost_ratio` 1.0723, `wall_clock_sec` 76.34 (the longest). |
| 6 | 3 | 0.8657 | Clean. `compute_efficiency` 0.6922, `per_step_cost_ratio` 0.9835, `wall_clock_sec` 74.37. Better than every earlier attempt at the time. |
| 7 (best) | **5** | **0.8658** | Clean. `compute_efficiency` 0.6926, `per_step_cost_ratio` 0.9581, `wall_clock_sec` 74.38. Better than every earlier attempt at the time. |

**Attempt 5 holds the highest reward, 0.8658. That is the number to beat.**

Three attempts scored lower than an attempt that came before them, and this must not be read as progress: attempt 2 (0.8079) fell below attempt 1 (0.8630); attempt 4 (0.7740) fell below attempt 3 (0.8657); attempt 6 (0.7580) and attempt 7 (0.4911) both fell below attempt 5 (0.8658). Attempt 7 is the lowest score recorded, roughly 0.375 below the best. The whole span of measured rewards is 0.4911 to 0.8658, and the entire top cluster (attempts 1, 3, 5) sits within 0.0028 of each other — attempt 5 beats attempt 3 by 0.0001, which is not a meaningful improvement.

## 2. Approach classes tried

The records supply metrics, not source, so these classes are grouped by their measured cost/efficiency signature and their check outcomes. The signature is reproducible even where the code is not.

**Class A — baseline, cost above parity (attempt 1, reward 0.8630).** `per_step_cost_ratio` 1.0723 (the only attempt above 1.0), lowest `compute_efficiency` of the clean runs at 0.6784, longest wall clock at 76.34 s and `qualifying_budget` 76.34. Fully conformant: `rule_conformance` 1.0, `conformance_fraction` 1.0, `task_pass` 1.0, both perturbations reached. This established that a slow, expensive configuration still scores in the high 0.86 band.

**Class B — moderate per-step cost reduction (attempt 2, reward 0.8079).** `per_step_cost_ratio` cut to 0.9441 and `compute_efficiency` raised to 0.7226, wall clock 74.26 s. Fully clean, no failed checks. Reward fell 0.0551 below attempt 1. Cheapening the step by ~12 % relative to class A cost more in reward than it gained in efficiency.

**Class C — near-parity cost, the scoring plateau (attempts 3 and 5, rewards 0.8657 and 0.8658).** Both sit at `per_step_cost_ratio` 0.9835 and 0.9581, `compute_efficiency` 0.6922 and 0.6926, wall clock 74.37 s and 74.38 s, `qualifying_budget` identical to wall clock. Both fully clean on every check and both perturbations reached. These are the two best results and they are effectively indistinguishable from each other (Δ = 0.0001). This class is where the reward lives: cost ratio in the 0.95–0.99 window, ~74.4 s of wall clock, compute efficiency near 0.69.

**Class D — aggressive compute reduction (attempt 4, reward 0.7740).** Pushed `compute_efficiency` to 0.9681 (by far the highest measured) and `per_step_cost_ratio` down to 0.6934 (by far the lowest), wall clock 73.74 s. Completely clean — no failed checks, `task_pass` 1.0, both perturbations reached — and yet reward dropped 0.0918 below attempt 3. This is the clearest signal in the data: reward is not monotone in compute efficiency, and the efficiency term is not what is being paid for.

**Class E — module restructuring with work at import scope (attempt 6, reward 0.7580).** Failed C-API-SURFACE. `per_step_cost_ratio` ballooned to 1.4094 and `compute_efficiency` collapsed to 0.4942, the worst of both on those axes. `rule_conformance` fell to 0.857 (six of seven rules), `task_pass` 0.0. Note the divergence between `wall_clock_sec` 70.37 and `qualifying_budget` 45.82: less of the elapsed time counted as qualifying than in the clean runs, where the two are equal. Both perturbations still reached their thresholds.

**Class F — short/early-terminating run (attempt 7, reward 0.4911).** Finished in 50.05 s with `qualifying_budget` 50.05, roughly a third less than the class C runs. `per_step_cost_ratio` 0.9657 and `compute_efficiency` 0.6954 look like class C, but the run ended far sooner. `task_pass` 0.0, `conformance_fraction` 0.50, `all_perturbations_held` false. Failed C-PERTURBATION-REACHED because one of the two declared perturbations blew its own budget. Worst result recorded.

## 3. Checks that failed

Five of the seven records passed every check. Two checks have failed, each once, in the primary run:

- **C-API-SURFACE** — attempt 6. Verifier reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions."* This is a submission-surface rule, not a learning-quality one: the module executed statements at import scope that the harness does not permit there. It dropped `rule_conformance` to 0.857 and `task_pass` to 0.0.
- **C-PERTURBATION-REACHED** — attempt 7. Verifier reason, verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* It dropped `conformance_fraction` to 0.50, `all_perturbations_held` to false, and `task_pass` to 0.0.

At the perturbation-unit level, one further check failed:

- **C-BUDGET-RESPECTED** — recorded against a held-out-variant unit in attempt 7. That unit did not reach its threshold; it is the direct cause of the C-PERTURBATION-REACHED failure above.

Neither C-API-SURFACE nor C-PERTURBATION-REACHED has failed more than once, so no single check has yet shown itself to be independent of what was changed between attempts. Both are single-record failures tied to a specific structural change, which is the good case: each looks fixable at its point of origin rather than being a persistent, cause-unknown failure.

**Perturbation outcomes.** Every record declares `perturbations_declared: 2.0`, and every record contains exactly one unit of kind `seed` and one of kind `held_out_variant`. Across all seven records that is 14 held-out runs, of which 13 reached their threshold and 1 did not.

- By kind, `seed`: 7 of 7 reached, zero failed checks in any record. The seed perturbation has never been a problem.
- By kind, `held_out_variant`: 6 of 7 reached. The single failure is the one described above, stopped by **C-BUDGET-RESPECTED** — the variant run exceeded its own budget rather than failing on correctness. The runs are not identified in the records beyond their kind, so nothing here should be read as any particular run recurring across attempts; the correct statement is that a held-out-variant run, in one attempt, overran its budget.

In aggregate: `all_perturbations_held` is true in six of seven records and false in one, and the sole aggregate failure is a budget overrun on a held-out-variant kind.

## 4. Ruled-out directions

- **Maximising compute efficiency / minimising per-step cost.** Ruled out by attempt 4: `compute_efficiency` 0.9681 and `per_step_cost_ratio` 0.6934, with a perfectly clean verification — no failed checks, `task_pass` 1.0, both perturbations reached — yet reward 0.7740, well below the 0.8657 of the near-parity attempt 3. Reinforced by attempt 2, whose smaller cut to 0.9441 already cost 0.0551 against attempt 1. Cheaper steps do not buy reward on this harness; they cost it. Do not spend the next attempt shaving per-step cost.
- **Running above cost parity for extra work.** Attempt 1 sat at `per_step_cost_ratio` 1.0723 with the longest wall clock, 76.34 s, and scored 0.8630 — below both class C attempts, which ran cheaper and shorter. Extra per-step spend is not rewarded either. The band that has actually produced the top scores is 0.9581–0.9835.
- **Doing work at module scope / restructuring the submission surface.** Ruled out by attempt 6's C-API-SURFACE failure with the verifier's stated reason "module-level statements outside imports, constants, and permitted definitions." Beyond the check failure, it also degraded every cost metric (`per_step_cost_ratio` 1.4094, `compute_efficiency` 0.4942) and zeroed `task_pass`. Keep the module to imports, constants, and permitted definitions; put all execution inside the permitted entry points.
- **Shortening the run / early termination.** Ruled out by attempt 7, the worst result at 0.4911. Cutting qualifying time to 50.05 s from the ~74.4 s of the scoring configurations did not merely fail to help; it left a held-out-variant perturbation unable to reach its threshold inside its own budget (C-BUDGET-RESPECTED), which cascaded into C-PERTURBATION-REACHED, `conformance_fraction` 0.50 and `task_pass` 0.0. Whatever schedule or budget-splitting produced that must not be reused: the perturbation runs need enough of their own budget to converge, and the primary run finishing early does not exempt them.
- **Treating attempt 5 as a real improvement over attempt 3 and tuning along that axis.** The gap is 0.0001, with essentially identical efficiency and wall clock. Whatever differed between them is inside the noise of this harness. Chasing that difference further is not a direction; class C has plateaued as tuned.

## 5. Open leads

- **Anchor the compute profile at the class C operating point and stop varying it.** Target `per_step_cost_ratio` ≈ 0.96–0.98, `compute_efficiency` ≈ 0.69, wall clock ≈ 74.4 s, with `qualifying_budget` equal to wall clock (as it is in all five clean runs). Both 0.8657 and 0.8658 came from exactly this envelope. Hold it fixed and change something else, so that any reward movement is attributable.
- **Attack the quality term, not the cost term.** The strongest inference available from the data: attempt 4 improved compute efficiency by 40 % relative to attempt 3 with full conformance and still lost 0.0918 of reward, while `primary_target_reached` was 1.0 in every single record including both failing ones. Reward therefore tracks something about how well the target is reached — margin, accuracy, or convergence quality — rather than how fast or cheaply. Candidate moves at fixed budget: better optimizer schedule (warmup plus decay rather than a flat rate), light regularisation or averaging of the final iterate, better initialisation, or ensembling/averaging across the steps already being paid for. All of these raise quality without changing per-step cost.
- **Give the held-out-variant perturbation headroom in its own budget.** The only unit-level failure in fourteen runs was a held-out-variant overrunning its budget under the short-run configuration. Since the variant is the more fragile of the two kinds (the seed kind has never failed), any change to the training length or schedule should be checked against the variant's budget specifically, and should leave the ~74.4 s profile intact rather than compressing it.
- **Keep the module surface strictly clean.** Imports, constants and permitted definitions only, with no executed statements at import scope. This costs nothing and removes the only rule-conformance failure seen so far.
- **Preserve robustness invariants that have never broken.** `validity` 1.0, `red_line_crossed` 0.0 and `zero_reason_code` 0 hold in all seven records; whatever the submission does about determinism and seed handling is working and should not be disturbed while chasing quality.

**Call: exploit.** Take the class C configuration that produced 0.8658 — near-parity per-step cost, ~74.4 s of qualifying budget, all checks clean, both perturbations reached — and improve the quality of the solution it reaches within that same budget, rather than moving its cost. Class C has plateaued on the axes tried so far (0.8657 → 0.8658), but the untried axis inside it is the one the evidence points at, and every structural departure attempted so far (classes D, E, F) has scored strictly worse than the class C best, twice by breaking a check. That is the honest read: earlier work has already spent three attempts exploring away from the scoring configuration and lost reward each time, so the value now is in the one thing that has not been varied at a fixed budget — solution quality.
