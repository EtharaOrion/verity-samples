# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 1 -- reward 0.6694, first measured attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1 *      0.6694   1.000             2 of 2         yes             17                

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

## 1. Results so far

One graded record exists, and it carries a measurement.

- **Attempt 1 — reward 0.6694** (`measurement_status: measured`, `standing_against_best_so_far: first_measured_attempt`). Every correctness-side term is at its ceiling: `task_pass` 1.0000, `validity` 1.0000, `primary_target_reached` 1.0000, `rule_conformance` 1.0000, `conformance_fraction` 1.0000, `red_line_crossed` 0.0000, `zero_reason_code` 0, `failed_checks` empty, `all_perturbations_held` true. The cost-side terms are the ones that are not at ceiling: `compute_efficiency` 0.5488, `per_step_cost_ratio` 1.5134, `wall_clock_sec` 17.4264, `qualifying_budget` 17.4264.

**Attempt 1, at reward 0.6694, is the highest reward on record and is the attempt to beat.** There is no second measured record, so there is no attempt that scored lower and no record that produced no measurement. Any next submission must clear 0.6694 to count as progress.

An important caveat for whoever writes the next attempt: the terms carried forward describe only the *measurements* of attempt 1, not its source. The implementation that produced reward 0.6694 is not reconstructible from what I was given — no architecture, optimizer, schedule, batch size, step count or data-handling choice was recorded. So the next attempt cannot literally resume attempt 1's code; it must produce a fresh implementation that at minimum reproduces attempt 1's perfect correctness profile, and should be written from the start with the cost profile below in mind.

## 2. Approach classes tried

Exactly one approach class has been graded, and it is defined by its outcome rather than by any recorded internals:

**Class A — a correct-and-conformant but cost-heavy trainer.** The single graded submission satisfied the harness completely on the correctness axis. It passed the task (`task_pass` 1.0000), was judged valid (`validity` 1.0000), reached the primary target (`primary_target_reached` 1.0000), broke no red line (`red_line_crossed` 0.0000), and conformed to the ruleset in full (`rule_conformance` 1.0000, `conformance_fraction` 1.0000). It also held every declared perturbation. Its only shortfall is expense: it burned 17.4264 seconds of wall clock — a figure identical to its `qualifying_budget`, i.e. it consumed the whole of the budget it qualified under — and its per-step work came in at 1.5134× the reference per-step cost, yielding a `compute_efficiency` of only 0.5488.

Because reward 0.6694 sits well above the correctness floor and well below 1, and because every correctness term is already saturated at 1.0 while the two efficiency terms sit near half-scale, the strong reading is that **the remaining headroom in the reward is on the compute/cost axis, not the correctness axis.** No approach class has yet been tried that trades differently on that axis.

No second class has been attempted: there is no record of a faster-but-riskier variant, no record of a differently-structured trainer, and no record of a failed or unmeasured submission.

## 3. Checks that failed

**None.** The one graded record has an empty `failed_checks` list at the top level, and an empty `failed_checks` list on each of its perturbation units. `conformance_fraction` is 1.0000 and `zero_reason_code` is 0.

Consequently there is no repeated failing check, no named check to name, and no verifier reason text to reproduce. This is the cleanest possible starting position on conformance and the next attempt's chief risk is *losing* it rather than fixing it.

## 4. Ruled-out directions

Nothing has been ruled out by evidence. With a single measured record and zero failed checks, no direction has been shown to be unworkable, and no submission has been penalised for a specific choice. I will not manufacture ruled-out entries the record does not support.

Two things are, however, established as **not worth spending effort on**, on the grounds that they are already maximal and cannot be improved:

- **Chasing correctness, validity, target-reaching or rule conformance.** `task_pass`, `validity`, `primary_target_reached`, `rule_conformance` and `conformance_fraction` are all 1.0000 already. There is no reward to be recovered there; effort spent there is effort not spent on cost.
- **Chasing perturbation robustness as a scoring lever.** `perturbations_declared` is 2.0 and `all_perturbations_held` is true, with both units reaching their thresholds. Hardening further cannot raise the score; it can only be protected.

## 5. Open leads

- **Cut per-step cost.** `per_step_cost_ratio` 1.5134 says each step costs roughly half again what the reference step costs. This is the single most legible deficiency in the record. Candidate moves: eliminate redundant per-step host/device transfers and per-step Python-level work, fuse or vectorise inner loops, avoid recomputing anything invariant inside the step, use a larger batch to amortise per-step overhead if the ruleset permits, and drop any per-step logging, evaluation, or copying that is not required for the target.
- **Cut wall clock, and note it equals the qualifying budget.** `wall_clock_sec` and `qualifying_budget` are both 17.4264. The run finished exactly at the budget it qualified under. Reducing total time — fewer steps to the same target, earlier stopping once `primary_target_reached` would be satisfied, cheaper warm-up — is the direct route to a better `compute_efficiency` than 0.5488 and therefore to a reward above 0.6694.
- **Stop as soon as the target is reached rather than running a fixed schedule.** Since `primary_target_reached` is a 1.0 boolean-like term and correctness is already saturated, any steps taken past the point of reaching the target are pure cost with no reward return. A convergence check that halts the moment the target criterion holds is the highest-leverage change available.
- **Protect the perturbation units while doing the above.** Both held-out runs reached their thresholds: one of kind `held_out_variant` and one of kind `ruleset`. In aggregate, 2 of 2 declared perturbation units held, and by kind: `held_out_variant` reached, `ruleset` reached; no check stopped either. Aggressive speed cuts — shortened schedules, reduced precision, tighter early stopping — are exactly the changes most likely to make a held-out variant miss its threshold or to trip the ruleset unit. Any speedup should be validated against both kinds before being kept, and if a speedup causes either kind to stop reaching, back it out rather than trying to compensate elsewhere.
- **Re-establish the correctness baseline first.** Because attempt 1's source does not carry forward, the next attempt should first write a straightforward implementation that reproduces `task_pass` 1.0, `validity` 1.0, `primary_target_reached` 1.0 and full conformance, confirm that shape, and only then apply the cost reductions above. Submitting a fast-but-unverified trainer risks trading a known 0.6694 for a failed check the record currently has no experience of.

**Call: exploit.** The approach that scored is correct and conformant on every axis the harness checks, and its only measured weakness — `compute_efficiency` 0.5488 driven by `per_step_cost_ratio` 1.5134 and a wall clock of 17.4264 that exactly consumes its qualifying budget — is precisely the one thing that stopped it going higher. That is the definition of a fixable single cause, and it has not yet been attempted even once. Exploring a structurally different design is unwarranted while the scoring approach has never been iterated on and its headroom is this clearly located.
