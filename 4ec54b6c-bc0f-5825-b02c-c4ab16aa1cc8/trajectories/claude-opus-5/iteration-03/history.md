# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 3 -- reward 0.5020, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 1 of 2 reached
        one ruleset run did not reach its threshold -- C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER
        the same ruleset run has now failed on 3 of your last 3 attempts
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.0000   1.000             0 of 2         no              --                
  2        0.5019   1.000             1 of 2         yes             14                
  3 *      0.5020   1.000             1 of 2         yes             14                

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

    attempt 1 -- reward 0.0000, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      NOTE: this attempt's phase was cut before it finished. What follows was graded
            on whatever was on disk at that moment, not on what it intended to submit,
            so a term below may report unfinished work rather than a failed idea.
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one ruleset run did not reach its threshold -- C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 2 -- reward 0.5019, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      NOTE: this attempt's phase was cut before it finished. What follows was graded
            on whatever was on disk at that moment, not on what it intended to submit,
            so a term below may report unfinished work rather than a failed idea.
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 1 of 2 reached
        one ruleset run did not reach its threshold -- C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER
        the same ruleset run has now failed on 2 of your last 2 attempts
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED has failed on 3 attempts (1, 2, 3). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Three graded attempts, all three of which produced a measurement. Listed worst to best by reward:

- **Attempt 1 — reward 0.0000.** measurement_status `measured_phase_cut`, zero_reason_code 4. `primary_target_reached` 0.0, `conformance_fraction` 0.0, `qualifying_budget` "not-measured", wall_clock 89.98 s, `per_step_cost_ratio` 1.0194, `compute_efficiency` 1.0. Nothing crossed a threshold, so no budget position existed. `validity` 1.0, `rule_conformance` 1.0, `red_line_crossed` 0.0 — the run was well-formed and broke no rule; it simply never reached the target.
- **Attempt 2 — reward 0.5019** (0.5018889886411652). measurement_status `measured_phase_cut`, zero_reason_code 0. `primary_target_reached` 1.0, `conformance_fraction` 0.5, `qualifying_budget` 14.1634, wall_clock 14.16 s, `per_step_cost_ratio` 1.5029, `compute_efficiency` 0.6529. `standing_against_best_so_far`: better than every earlier attempt.
- **Attempt 3 — reward 0.5020** (0.5020024293853175). measurement_status `measured`, zero_reason_code 0. `primary_target_reached` 1.0, `conformance_fraction` 0.5, `qualifying_budget` 13.8183, wall_clock 13.82 s, `per_step_cost_ratio` 1.5364, `compute_efficiency` 0.6176. `standing_against_best_so_far`: better than every earlier attempt.

**Attempt 3 holds the highest reward, 0.5020, and it is the one to beat.**

Note the size of that lead: attempt 3 beat attempt 2 by 0.0001. That is a flat result, not a real gain. Within that same configuration two secondary terms actually moved the wrong way — `per_step_cost_ratio` rose from 1.5029 to 1.5364 and `compute_efficiency` fell from 0.6529 to 0.6176 — and the only term that improved was wall clock (14.16 s → 13.82 s). `conformance_fraction` stayed pinned at 0.5 across both. Tuning inside this configuration has stopped paying.

# 2. Approach classes tried

Only the measured terms are available, not the source of the earlier attempts, so these classes are grouped by the behaviour the terms describe. Two distinct classes appear across the three records.

**Class A — cheap-per-step, non-converging configuration (attempt 1).** Characterised by `per_step_cost_ratio` 1.0194 (essentially the harness's own reference cost per step) and `compute_efficiency` 1.0, but a wall clock of 89.98 s during which no evaluation row ever crossed the threshold in the declared direction. This is the profile of a training rule that costs almost nothing per step and correspondingly moves too slowly — it burned the full phase and was cut, producing zero. `validity` and `rule_conformance` were both 1.0, so the failure was purely one of not reaching the target, not of malformed output or rule-breaking. Both declared perturbations also failed to reach, including the held-out variant, which fits a configuration that is under-powered everywhere rather than one that is fragile in a specific way.

**Class B — costlier-per-step, fast-converging configuration (attempts 2 and 3).** Characterised by `per_step_cost_ratio` around 1.50–1.54 (roughly 50% more expensive per step than the reference) and `compute_efficiency` 0.62–0.65, but reaching the primary target in 13.8–14.2 s of wall clock, roughly a sixth of attempt 1's time. This class reliably satisfies `primary_target_reached` = 1.0 and it reliably carries the **held_out_variant** perturbation across its own threshold inside its own budget. It reliably fails the **ruleset** perturbation. Attempt 3 is best read as a re-tuning of attempt 2 within the same class: the failure signature is byte-identical between them and the reward moved by 0.0001.

The step from Class A to Class B is where all the reward came from: paying ~50% more per step to converge ~6x faster was worth 0.50 of reward. Every subsequent move inside Class B has been worth ~0.0001.

# 3. Checks that failed

**C-PERTURBATION-REACHED — failed in all three attempts (3 of 3).** In attempt 1 the reason was "0 of 2 declared perturbations reached their own threshold inside their own budget"; in attempts 2 and 3 it was "1 of 2 declared perturbations reached their own threshold inside their own budget". This is the only failed check remaining on the two scoring attempts, and it is what holds `conformance_fraction` at exactly 0.5 and `all_perturbations_held` at false. Whatever was changed between attempt 2 and attempt 3 is not what is causing this check to fail — the check failed identically before and after that change, with the same 1-of-2 reason string.

**C-TARGET-REACHED — failed at the primary level in attempt 1 only**, reason "no evaluation row crosses the threshold in the declared direction". It has not failed at the primary level since; the Class B configuration fixed it.

**C-BUDGET-RESPECTED — failed at the primary level in attempt 1 only**, reason "no qualifying row, so no budget position exists". This is a consequence of the C-TARGET-REACHED failure, not an independent budget overrun: with no row crossing the threshold there was nothing to position against the budget. It has not failed at the primary level since.

Within the perturbation runs, four checks recur (details in the next paragraph): C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER.

**Perturbation-unit outcomes.** Two perturbations were declared in every record. By kind:

- **ruleset** — reached in 0 of 3 attempts. It failed on the identical set of four checks every single time: **C-LOG-WELL-FORMED**, **C-TARGET-REACHED**, **C-BUDGET-RESPECTED**, **C-NO-LATCH-CARRYOVER**. This set did not change at all between attempt 1 (which scored zero) and attempts 2 and 3 (which scored 0.50). Three failures, unchanged signature: whatever was changed between those attempts is not what is causing the ruleset perturbation to fail. Note especially that C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER appear *only* here — they never fail on the primary run and never fail on the held-out variant. These two are not shared with the primary path at all.
- **held_out_variant** — reached in 2 of 3 attempts. It failed only in attempt 1, on **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**, the same pair that the primary run failed in that attempt; it held clean, with an empty failed_checks list, in attempts 2 and 3.

In aggregate across the three records: 6 perturbation runs, 2 reached, 4 not reached. All three non-reaching ruleset runs failed the same four checks; the single non-reaching held_out_variant run failed the two target/budget checks that its own primary run also failed in that attempt.

The perturbation runs are not identified by name, number or position, and nothing in the records ties any particular run in one attempt to a particular run in another. Only the *kind* is known, and the statements above are made by kind.

# 4. Ruled-out directions

- **Cheap-per-step / slow-convergence training (Class A).** Ruled out: it produced reward 0.0000 with zero_reason_code 4 and `conformance_fraction` 0.0, having spent 89.98 s without any evaluation row crossing the threshold in the declared direction. Its `compute_efficiency` of 1.0 is worthless because no qualifying row ever existed to bank it against. Do not restart from a configuration whose per-step cost ratio sits near 1.0 if that is bought by slower progress.
- **Further micro-tuning inside Class B aimed at the primary run's speed or cost.** Ruled out as a path to a materially higher reward: attempt 3 versus attempt 2 is the controlled experiment, and it moved reward by 0.0001 while `conformance_fraction` stayed at 0.5, `per_step_cost_ratio` got worse (1.5029 → 1.5364) and `compute_efficiency` got worse (0.6529 → 0.6176). The primary run is already passing every check it is graded on; there is very little headroom left there.
- **Any change that leaves the ruleset perturbation's handling untouched.** Ruled out because C-PERTURBATION-REACHED has now failed three times in a row and the ruleset unit's four-check failure signature has not shifted once across two structurally different training configurations. Changing the optimiser/schedule side of the work does not touch it.
- **Treating validity, rule_conformance or red_line as problems.** Ruled out: `validity` = 1.0, `rule_conformance` = 1.0 and `red_line_crossed` = 0.0 in every record including the zero. No effort should go to these.

# 5. Open leads

- **The single highest-value lead is making the ruleset perturbation hold.** `conformance_fraction` is 0.5 with 1 of 2 perturbations reaching, and reward is 0.5020. Taking the ruleset unit from not-reached to reached is the only structural move on the table that plausibly moves reward toward the upper half of the range, and it is the only failed check left on the best attempt.
- **C-LOG-WELL-FORMED on the ruleset unit is the most diagnostic thread.** This check never fails on the primary run and never fails on the held_out_variant, only on the ruleset perturbation, and it has done so all three times. That asymmetry says the submission emits a log the harness can parse under normal rules but cannot parse under the perturbed ruleset. Likely causes worth checking in the fresh stub: log fields or row schema that are hard-coded to the unperturbed ruleset; a header, column set or declared-direction field written once and not re-derived per ruleset; rows emitted in a format that assumes a fixed set of rules. Because C-TARGET-REACHED and C-BUDGET-RESPECTED are also failing on this unit, and those two are exactly what fails downstream when no parseable qualifying row exists (see attempt 1's primary reason strings: "no qualifying row, so no budget position exists"), it is plausible that C-LOG-WELL-FORMED is the root and the other two are consequences. **Fix the log well-formedness under the perturbed ruleset first and re-measure before touching anything else.**
- **C-NO-LATCH-CARRYOVER on the ruleset unit is the second thread and may be independent.** It also fails only on this unit, all three times. Its name points at state latched during one run and carried into the next — cached values, a module-level or global optimiser/scaler/schedule object, a memoised statistic, an RNG or best-so-far tracker that is not reset between rulesets. In a fresh stub, make every piece of run state constructed per-run and explicitly reset at run entry, with nothing surviving at module scope. This is worth doing even if the log fix alone lands the unit, because C-PERTURBATION-REACHED requires the unit to clear all of its checks.
- **Rebuild on the Class B profile, not Class A.** The next attempt starts from a pristine stub, so the fast-converging configuration must be re-established: something that pays roughly 1.5x the reference per-step cost and reaches the primary threshold in the 13–15 s range. That profile has now reached the primary target and carried the held_out_variant twice in a row, so it is the reliable base to build the ruleset fix on top of.
- **Secondary, only if the ruleset unit is already held:** `compute_efficiency` at 0.6176 and `per_step_cost_ratio` at 1.5364 are the terms with visible slack once conformance is full. Attempt 2's 0.6529 / 1.5029 shows the same class can run leaner. But this is worth at most a fraction of what the ruleset unit is worth, and chasing it first is what the last attempt effectively did.

**Call: exploit.** The Class B configuration already scores 0.5020 and passes every primary-level check; the one thing stopping it is C-PERTURBATION-REACHED, which resolves entirely to the ruleset unit's four checks. Attack that unit — C-LOG-WELL-FORMED first, then C-NO-LATCH-CARRYOVER — while re-establishing the Class B training profile from the stub. Do not re-submit a Class B variant with the ruleset handling unchanged: attempt 3 already did that against attempt 2 and the ruleset failure signature did not move by a single check.
