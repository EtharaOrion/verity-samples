# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 1 -- reward 0.8630, first measured attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1 *      0.8630   1.000             2 of 2         yes             76                

  reward  = what the attempt scored, in the closed interval 0 to 1. No value of it is a pass:
            task pass is a separate conjunction and is reported beside the reward, not inferred
            from it. A high reward with a failed pass, or the reverse, is a real outcome.
  rule conformance = the fraction of the static conformance rules the submitted bytes held.
  perturbation runs = the held-out runs beside the primary one. They are described by kind
            and are deliberately not individually named, so no run has a label you can
            iterate against; what each one measured is not published either.
  --      = the run did not produce this measurement. It is not a zero.
  *       = the best reward so far, and the one to beat.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

One graded submission exists, and it carries a measurement.

- Attempt 1 — `measurement_status: measured`, **reward = 0.8630** (0.8629926448235584). `standing_against_best_so_far: first_measured_attempt`, so there is no earlier result it improves on or falls behind. Supporting terms: `task_pass = 1.0`, `validity = 1.0`, `rule_conformance = 1.0`, `conformance_fraction = 1.0000`, `primary_target_reached = 1.0`, `red_line_crossed = 0.0`, `zero_reason_code = 0`, `all_perturbations_held = true`, `perturbations_declared = 2.0`, `wall_clock_sec = 76.3367`, `qualifying_budget = 76.3367`, `compute_efficiency = 0.6784`, `per_step_cost_ratio = 1.0723`.

Attempt 1 holds the highest reward at 0.8630 and is the attempt to beat. Nothing has regressed against it, because nothing else has been measured.

2. Approach classes tried

Exactly one approach class has been graded, and it is the only thing carried forward. The measured terms describe its behaviour, not its source, so it must be re-derived from its observable profile rather than recalled:

- **Class A — a fully conforming, target-reaching training algorithm that is compute-inefficient relative to the harness's reference cost.** Every correctness-side gate it was measured against returned the maximum value: the task passed, the submission was valid, rule conformance was total (`conformance_fraction = 1.0`, i.e. every conformance check the harness applied was satisfied), the primary target was reached, and no red line was crossed. The entire shortfall from a perfect score sits on the cost/efficiency side: the run consumed 76.3367 seconds of wall clock, its whole qualifying budget was 76.3367 (budget consumed equals wall clock, so the run was timed out at exactly what it spent — there is no evidence of headroom being left unused nor of an overrun), `compute_efficiency` came in at 0.6784, and `per_step_cost_ratio` was 1.0723, meaning each optimisation step cost about 7.2% more than the reference step the harness prices against.

That is the whole space explored so far. There is no second approach class, no ablation, and no variant that failed.

3. Checks that failed

None. `failed_checks` is empty for the primary run of attempt 1, and empty for both perturbation units. There is consequently no repeated check, no identifier to name, and no reason string from the verifier to quote. Any future summary that reports a failing check will be reporting something genuinely new, not a recurrence.

For the held-out runs: `perturbations_declared = 2.0` and two perturbation units were reported, one of kind `held_out_variant` and one of kind `seed`. Both have `reached: true` and empty `failed_checks`. By kind: the `held_out_variant` kind reached its threshold with no check stopping it; the `seed` kind reached its threshold with no check stopping it. In aggregate, 2 of 2 held-out runs reached their thresholds and `all_perturbations_held` is true. No run is failing on any check at present, so there is no kind-specific fragility to chase. The runs are not individually identified and must not be treated as identifiable across records.

4. Ruled-out directions

Nothing has been ruled out by measurement. With a single measured record and no failed check, no direction has been shown to be unproductive. Two things are, however, established strongly enough that they should not be re-litigated as if they were open problems:

- **Chasing correctness, conformance, validity, or robustness gains is ruled out as a source of reward, because there is none left to gain.** `task_pass`, `validity`, `rule_conformance`, `conformance_fraction`, and `primary_target_reached` are all already at 1.0, `red_line_crossed` is 0.0, and both perturbation units held. Effort spent hardening any of these can at best preserve the current score and cannot raise it.
- **Interpreting the sub-1.0 reward as a hidden correctness defect is ruled out by `zero_reason_code = 0` and the empty `failed_checks`.** The gap between 0.8630 and 1.0 is not attributable to any check the verifier reported as unmet; the only terms not at their maximum are `compute_efficiency` (0.6784) and `per_step_cost_ratio` (1.0723, above the reference 1.0).

5. Open leads

All leads point at cost, since that is the only measured quantity with slack.

- **Cut per-step cost below the reference.** `per_step_cost_ratio = 1.0723` says the step is about 7.2% more expensive than the reference step. Bringing it to 1.0 or under is the most directly targeted change available: fuse or eliminate redundant per-step work, remove per-step host/device synchronisation, per-step logging, per-step metric computation, or per-step validation that could be amortised over many steps or hoisted out of the loop entirely; prefer in-place and pre-allocated buffers over per-step allocation; avoid recomputing anything constant across steps.
- **Cut total wall clock, which is the whole qualifying budget.** The run spent 76.3367 seconds and its qualifying budget equals that figure exactly. Total cost is steps × per-step cost, so the second lever is step count: reach the same primary target in fewer steps via a stronger learning-rate schedule, warmup plus decay, larger effective batch where it does not raise per-step cost proportionally, or early stopping the moment the primary target is provably reached rather than running a fixed step count to completion.
- **Stop as soon as the target is reached.** Since `primary_target_reached` is binary and already satisfied, any work performed after the target is met is pure cost with no reward. If the current algorithm runs a fixed schedule, adding a cheap target check and an immediate exit is a low-risk efficiency win.
- **Protect the margin while trimming.** Both held-out kinds (`held_out_variant`, `seed`) currently reach their thresholds. Aggressive step-count reduction is the change most likely to turn one of those `reached: true` into a failure, since a seed-perturbed or variant run may need slightly more optimisation to clear the same threshold. Trim in increments and keep a visible margin above the target rather than landing exactly on it.
- **Prefer per-step savings over step-count savings where both are available**, because per-step savings reduce cost without moving the run closer to the threshold, whereas step-count savings spend robustness margin to buy time.

Call: **exploit.** Attempt 1 scored 0.8630 with every correctness, conformance, and robustness term already maximal and both held-out runs holding; the single identified deficit is compute cost (`compute_efficiency = 0.6784`, `per_step_cost_ratio = 1.0723`, `wall_clock_sec = 76.3367`). The next attempt should reconstruct the same conforming, target-reaching algorithm and make it cheaper per step and shorter overall, verifying after each trim that the primary target is still reached with margin so the two perturbation kinds continue to hold. Exploration into a structurally different algorithm is not warranted: the one approach that has scored has not yet been shown to have stopped improving, and its improvement axis is precisely known.
