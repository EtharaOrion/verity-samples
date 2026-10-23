# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.8255, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.0000   1.000             0 of 2         no              --                
  2        0.8037   1.000             2 of 2         yes             13                
  3        0.8042   1.000             2 of 2         yes             14                
  4        0.8042   1.000             2 of 2         yes             14                
  5 *      0.8255   1.000             2 of 2         yes             14                
  6        0.8059   1.000             2 of 2         yes             13                

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

    attempt 3 -- reward 0.8042, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.8042, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 6 -- reward 0.8059, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 13
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Six graded records, all with `measurement_status` of `measured` or `measured_phase_cut`; every one of them therefore carries a reward, and none must be read as missing. Listed worst to best:

- **Attempt 1 — reward 0.0000.** `measurement_status: measured_phase_cut`, `zero_reason_code: 4`, `task_pass 0.0`, `primary_target_reached 0.0`, `conformance_fraction 0.0`, `all_perturbations_held false`. `qualifying_budget` was `"not-measured"` because no row qualified. Wall clock 89.9778 s — roughly 6.6× the wall clock of every later attempt. `per_step_cost_ratio 1.0194`, `compute_efficiency 1.0` (both meaningless here: with no qualifying row there is no budget position to be efficient against). `validity 1.0` and `rule_conformance 1.0`, so the submission was well-formed and legal — it simply never reached the target.
- **Attempt 2 — reward 0.8037.** `measured_phase_cut`, `task_pass 1.0`, `primary_target_reached 1.0`, `conformance_fraction 1.0`, no failed checks, both perturbations held. `qualifying_budget 13.4877` s, `wall_clock_sec 13.4877`, `compute_efficiency 0.6203`, `per_step_cost_ratio 1.4966`. `standing_against_best_so_far: first improvement over everything earlier`.
- **Attempt 4 — reward 0.8042** (0.8041887 unrounded). `measured`, clean, both perturbations held. `qualifying_budget 13.6584` s, `compute_efficiency 0.5835`, `per_step_cost_ratio 1.4974`. **This is a regression:** `standing_against_best_so_far` reads `worse_than_an_earlier_attempt`. It is worse than attempt 3, which preceded it. Do not read the shared 4-decimal rendering as parity — attempt 4 lost ground.
- **Attempt 3 — reward 0.8042** (0.8042363 unrounded). `measured`, clean, both perturbations held. `qualifying_budget 13.6621` s, `compute_efficiency 0.6051`, `per_step_cost_ratio 1.5320`. Best-so-far at the time it was measured.
- **Attempt 6 — reward 0.8059.** `measured`, clean, both perturbations held. `qualifying_budget 13.4266` s (the lowest of any qualifying attempt), `compute_efficiency 0.9465` (the highest of any attempt with a real budget), `per_step_cost_ratio 0.9711` (the only sub-1.0 ratio recorded). **This is a regression:** `standing_against_best_so_far` reads `worse_than_an_earlier_attempt`. Despite being by far the cheapest and most compute-efficient qualifying run, it scored below attempt 5. Cheapness did not buy reward.
- **Attempt 5 — reward 0.8255.** `measured`, clean, `task_pass 1.0`, `primary_target_reached 1.0`, `conformance_fraction 1.0`, `red_line_crossed 0.0`, both perturbations held. `qualifying_budget 13.7398` s (the largest of any qualifying attempt), `compute_efficiency 0.7476`, `per_step_cost_ratio 1.2599`.

**Attempt 5, at reward 0.8255, holds the highest reward and is the attempt to beat.** The next-best is attempt 6 at 0.8059; the gap of ~0.020 is larger than the entire spread across attempts 2, 3, 4 and 6 (0.8037–0.8059), so attempt 5 is not noise-adjacent to the cluster.

# 2. Approach classes tried

The records carry only measured terms, not source, so the approaches are distinguishable by their metric signature rather than by any description I was handed. Grouping by signature, three distinct classes appear:

**Class A — the non-converging long run (attempt 1).** Ran 89.98 s of wall clock, roughly 6.6× everything that followed, and still produced no evaluation row crossing the threshold in the declared direction. It was valid and rule-conformant (`validity 1.0`, `rule_conformance 1.0`), so the failure was one of learning/convergence and of harness-contract detail on the perturbation side, not of legality. Its `per_step_cost_ratio` of 1.0194 says the per-step cost was near baseline; the run was slow because it took many steps, not because each step was expensive. Whatever it did, it did not get the model to the target within a very generous amount of time.

**Class B — the converging expensive-step configuration (attempts 2, 3, 4).** All three land in a tight band: wall clock 13.49–13.66 s, `per_step_cost_ratio` 1.4966–1.5320 (each step costs ~1.5× the reference step), `compute_efficiency` 0.5835–0.6203, reward 0.8037–0.8042. All pass every check and hold both perturbations. The internal variation across these three is small and non-monotone in efficiency: attempt 4 had the lowest efficiency of the three (0.5835) yet scored between the other two, and attempt 3's marginally higher reward over attempt 4 came with higher efficiency but also a higher per-step ratio. Practically, these three are one operating point with jitter, and whatever was changed between them moved reward by less than 0.0006.

**Class C — the cheap-step configuration (attempt 6).** Drove `per_step_cost_ratio` below 1.0 (0.9711) and `compute_efficiency` to 0.9465, finishing in 13.4266 s. Fully clean, both perturbations held. Reward 0.8059 — barely above the Class B band and clearly below attempt 5. This is the informative negative: pushing per-step cost to its minimum recovered almost nothing.

**Class D — the intermediate-cost configuration (attempt 5).** `per_step_cost_ratio 1.2599`, `compute_efficiency 0.7476`, and the largest qualifying budget consumed (13.7398 s). Reward 0.8255, the best recorded. It sits between Class B and Class C on cost per step, and above both on reward.

The cross-class reading that matters: reward is **not** monotone in `compute_efficiency`. Ordering the qualifying attempts by efficiency gives 0.5835 → 0.8042, 0.6051 → 0.8042, 0.6203 → 0.8037, 0.7476 → 0.8255, 0.9465 → 0.8059. The peak is interior, at ~0.75 efficiency / ~1.26 cost ratio. Since `task_pass`, `validity`, `rule_conformance`, `conformance_fraction` and `primary_target_reached` are all pinned at their maxima for every qualifying attempt, none of those terms explains the 0.020 spread. The spread must come from a term not saturated in these records — most plausibly a quality-of-solution or margin-above-threshold component, or a budget-position term that rewards using the budget productively rather than merely finishing early. Attempt 6 finished earliest and scored worse; attempt 5 used the most budget and scored best. That is the shape of the evidence.

# 3. Checks that failed

Every named check failure in the entire record set belongs to **attempt 1**. Attempts 2 through 6 have empty `failed_checks` at the top level and empty `failed_checks` on every perturbation unit.

At the top level of attempt 1:

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction."
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists." This is a downstream consequence of the target failure, not an independent overspend: there was nothing to measure a budget against.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget."

Within attempt 1's perturbation units:

- On the **ruleset** run: **C-LOG-WELL-FORMED**, **C-TARGET-REACHED**, **C-BUDGET-RESPECTED**, **C-NO-LATCH-CARRYOVER**.
- On the **held_out_variant** run: **C-TARGET-REACHED**, **C-BUDGET-RESPECTED**.

Two of these are worth isolating because they are the only failures that are *not* explained by "the model never converged." **C-LOG-WELL-FORMED** and **C-NO-LATCH-CARRYOVER** appeared only on the ruleset-kind run, and only in attempt 1. C-LOG-WELL-FORMED points at the emitted evaluation log's structure under the ruleset perturbation; C-NO-LATCH-CARRYOVER points at state being latched from the primary run and carried into the perturbation run instead of being reset. Neither has recurred, so whatever attempt 2 changed fixed both — but the fix is unrecorded in these terms and must be preserved rather than rediscovered.

On repetition across records: **no check failed in more than one graded attempt.** C-TARGET-REACHED and C-BUDGET-RESPECTED each failed three times *within* attempt 1 (once at the top level, once on each perturbation unit), but that is one attempt's cascade, not a finding that survived a code change. Because attempts 2–6 are check-clean, there is no standing conformance problem to chase; the entire remaining question is reward magnitude among fully-passing runs.

# 4. Ruled-out directions

- **Whatever attempt 1 did (Class A).** Ruled out because it never crossed the target threshold in 89.98 s — roughly 6.6× the wall clock any successful attempt needed — and simultaneously tripped C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER on the ruleset perturbation. Reverting toward it costs the only zero on record. Do not reintroduce whatever caused state to carry over into the ruleset run, and do not reintroduce whatever made the ruleset run's log malformed.
- **Minimising per-step cost as the route to reward (Class C).** Ruled out empirically. Attempt 6 achieved `per_step_cost_ratio 0.9711` — the only sub-baseline step cost recorded — and `compute_efficiency 0.9465`, the highest of any qualifying attempt, and its reward was 0.8059, a regression against attempt 5's 0.8255. Buying speed at the apparent expense of solution quality loses roughly 0.020 of reward. The cheap-step direction is spent.
- **The ~1.5× per-step-cost operating point (Class B).** Ruled out as a place to keep tuning. Three attempts (2, 3, 4) sat there with `per_step_cost_ratio` 1.4966–1.5320 and produced rewards spanning 0.8037–0.8042 — a total spread of 0.0006, with attempt 4 an outright regression against attempt 3. Three samples of near-identical reward from a band that is 0.021 below the best say that local edits at that operating point do not move the number.
- **Treating `compute_efficiency` as the objective.** Ruled out because the reward-versus-efficiency relation is demonstrably non-monotone across the five qualifying attempts, with the maximum at an interior efficiency of 0.7476 and the *lowest* reward among qualifiers at efficiency 0.6203. Optimising efficiency directly would push toward attempt 6's regressed point.
- **Chasing conformance fixes.** Ruled out as a source of headroom. `validity`, `rule_conformance`, `conformance_fraction`, `task_pass`, `primary_target_reached` and `all_perturbations_held` are all at their maxima for attempts 2–6, and `red_line_crossed` is 0.0 everywhere including attempt 1. There is no conformance ground left to gain.

# 5. Open leads

- **Reconstruct attempt 5's operating point first, then perturb around it.** The target signature is `per_step_cost_ratio ≈ 1.26`, `compute_efficiency ≈ 0.75`, qualifying budget ≈ 13.74 s, all checks clean, both perturbations held. That is the 0.8255 point and it is the thing to beat. Reproducing it is the floor for the next attempt, not the goal.
- **Sweep the per-step-cost axis finely between 1.0 and 1.5.** The three data points at ~1.50 (0.8037–0.8042), one at 1.26 (0.8255) and one at 0.97 (0.8059) describe a single-peaked curve with a maximum near 1.26 and steep falloff on both sides. The intervals 1.05–1.20 and 1.30–1.45 are entirely unsampled and are the highest-information places to spend the next measurement. A point at ~1.15 and a point at ~1.35 would locate the peak far better than any further work at 1.50.
- **Identify the unsaturated reward term.** Every conformance-flavoured term is pinned at 1.0 across attempts 2–6 while reward moves by 0.021, so the moving term is something else — most likely margin above the primary target, or a budget-utilisation term. Attempt 5 consumed the *largest* qualifying budget (13.7398 s) and scored best; attempt 6 consumed the smallest (13.4266 s) and regressed. A deliberate test — hold the training recipe fixed and spend the extra budget on additional refinement/eval quality rather than exiting early — would confirm or kill the margin hypothesis in one measurement.
- **Push margin at constant cost.** If margin is the driver, the win is in making the crossing more decisive rather than cheaper: more effective steps, better schedule, better final-model selection, at a per-step cost held near 1.26. This is the direction attempt 6 went the wrong way down.
- **Protect the two one-off perturbation fixes.** C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER failed once each, on the ruleset-kind run in attempt 1, and have held ever since. Any restructuring of how state is reset between the primary and perturbation runs, or of how the evaluation log is emitted, risks reopening them. Explicitly reset per-run state and emit a well-formed log for the perturbation runs even if the change seems orthogonal.

**Perturbation-unit outcomes, by kind and in aggregate.** Two perturbations were declared in every record; the kinds present are `ruleset` and `held_out_variant`, one of each per record. Across the six records that is twelve held-out runs. Ten reached their threshold — the five clean records each had both kinds reach. The two that did not reach both belong to attempt 1. By kind: the **ruleset** kind failed once, stopped by C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER; the **held_out_variant** kind failed once, stopped by C-TARGET-REACHED and C-BUDGET-RESPECTED. The ruleset kind is the stricter of the two, being the only kind ever to fail C-LOG-WELL-FORMED or C-NO-LATCH-CARRYOVER. The runs are not identified beyond their kind, so nothing here should be read as tracking a particular run across records.

**Call: exploit.** The best-scoring approach has not plateaued — it has been sampled exactly once, at 0.8255, and the axis it lives on (per-step cost ratio) is sampled at only three widely-spaced values with a clear interior peak and two unexplored intervals on either side of the best point. Reproduce attempt 5's configuration and move its per-step cost ratio in small steps toward 1.15 and 1.35 while keeping every check clean and both perturbations reaching. Do not return to the ~1.50 band, which three attempts have shown to be flat and 0.021 below the peak, and do not return to sub-1.0 step cost, which regressed. Note for the record that attempts 3, 4 and 6 each re-visited a region already characterised without changing the factor that bounded it, and two of the three came back as regressions; that pattern is neither exploration nor exploitation and should not be repeated.
