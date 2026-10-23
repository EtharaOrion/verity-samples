# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 4 -- reward 0.5043, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 1 of 2 reached
        one ruleset run did not reach its threshold -- C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER
        the same ruleset run has now failed on 4 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.0000   1.000             0 of 2         no              --                
  2        0.5019   1.000             1 of 2         yes             14                
  3        0.5020   1.000             1 of 2         yes             14                
  4 *      0.5043   1.000             1 of 2         yes             14                

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

    attempt 3 -- reward 0.5020, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 1 of 2 reached
        one ruleset run did not reach its threshold -- C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER
        the same ruleset run has now failed on 3 of your last 3 attempts
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED has failed on 4 attempts (1, 2, 3, 4). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Four graded submissions, every one of them carrying `measurement_status` of `measured` or `measured_phase_cut` and therefore a real reward. Listed worst to best:

- **Attempt 1 — reward 0.0000.** `measured_phase_cut`, `zero_reason_code` 4. `primary_target_reached` 0.0, `conformance_fraction` 0.0, `qualifying_budget` "not-measured". Nothing crossed a threshold, so no budget position existed at all. `wall_clock_sec` 89.98 — by far the longest run of the four.
- **Attempt 2 — reward 0.5018889886411652 → 0.5019.** `measured_phase_cut`, `zero_reason_code` 0. `primary_target_reached` 1.0, `conformance_fraction` 0.5, `qualifying_budget` 14.1634, `compute_efficiency` 0.6529, `per_step_cost_ratio` 1.5029, `wall_clock_sec` 14.16. Standing: better than every earlier attempt.
- **Attempt 3 — reward 0.5020024293853175 → 0.5020.** Fully `measured`. Same shape as attempt 2: `primary_target_reached` 1.0, `conformance_fraction` 0.5, `qualifying_budget` 13.8183, `compute_efficiency` 0.6176, `per_step_cost_ratio` 1.5364. Standing: better than every earlier attempt, but the gain over attempt 2 is +0.0001 — within noise of the same configuration.
- **Attempt 4 — reward 0.5043341291715087 → 0.5043.** Fully `measured`. `primary_target_reached` 1.0, `conformance_fraction` 0.5, `qualifying_budget` 13.7925, `compute_efficiency` 0.5856, `per_step_cost_ratio` 1.4727, `wall_clock_sec` 13.79. Standing: better than every earlier attempt.

**Attempt 4 holds the highest reward, 0.5043. That is the one to beat.**

Constant across all four records: `validity` 1.0, `rule_conformance` 1.0, `red_line_crossed` 0.0, `perturbations_declared` 2.0, `all_perturbations_held` false, and — worth noting — **`task_pass` 0.0 in every record, including the three where `primary_target_reached` is 1.0**. Reaching the primary target has not been sufficient to set `task_pass`.

One counter-trend to be honest about: reward rose across attempts 2→3→4 while `compute_efficiency` fell monotonically (0.6529 → 0.6176 → 0.5856). The reward movement in that band is not coming from getting cheaper; it is small and the efficiency term is moving the wrong way underneath it. Total reward has been pinned near 0.50 for three consecutive attempts, which is what `conformance_fraction` 0.5 predicts.

## 2. Approach classes tried

The supplied terms record measurements only, not source code, so these classes are grouped by their measured signature rather than by any description of the implementation. Two distinct classes appear:

**Class A — the non-reaching configuration (attempt 1).** Produced no evaluation row crossing the threshold in the declared direction, hence no qualifying budget row at all, hence `conformance_fraction` 0.0 and `zero_reason_code` 4. Its distinguishing measured feature is `wall_clock_sec` 89.98 against a `per_step_cost_ratio` of only 1.0194 — a cheap per-step configuration that ran long and still never reached the target. That combination points to a run that was under-trained or converging too slowly per step rather than one that was too expensive per step. Its `compute_efficiency` of 1.0 is not an achievement; with no qualifying row there was nothing to charge against.

**Class B — the reaching configuration and two refinements of it (attempts 2, 3, 4).** Primary target reached, `conformance_fraction` 0.5, one of two declared perturbations reached, reward parked at 0.50–0.51. The three records differ from attempt 1 by roughly a 6.5× reduction in wall clock (89.98 → ~14) bought at a ~50% higher `per_step_cost_ratio` (1.02 → ~1.5). That is the trade that unlocked the primary target: more work per step, far fewer steps. Within Class B the three attempts are barely distinguishable in outcome — rewards 0.5019, 0.5020, 0.5043, identical failed-check set, identical perturbation outcomes by kind. Whatever was varied between them moved reward by less than 0.003 in total and did not change any check's verdict.

## 3. Checks that failed

- **C-PERTURBATION-REACHED — failed in all 4 records.** Reason in attempt 1: "0 of 2 declared perturbations reached their own threshold inside their own budget". Reason in attempts 2, 3 and 4: "1 of 2 declared perturbations reached their own threshold inside their own budget". This check has now failed four consecutive times, and for the last three it has failed with exactly the same 1-of-2 count. Whatever was changed between attempts 2, 3 and 4 is not what is causing this failure.
- **C-TARGET-REACHED — failed on the primary in attempt 1**, reason "no evaluation row crosses the threshold in the declared direction". Held in attempts 2–4 on the primary.
- **C-BUDGET-RESPECTED — failed on the primary in attempt 1**, reason "no qualifying row, so no budget position exists". This is a consequence of the C-TARGET-REACHED failure, not an independent budget overrun. Held in attempts 2–4 on the primary.

Inside the held-out runs, the ruleset-kind run failed the same four checks in **all four records**: **C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER**. Four failures each, unchanged in composition from attempt 1 through attempt 4 — including across the attempt-1-to-attempt-2 transition that fixed the primary target and more than tripled the reward. Nothing done so far has touched any of these four.

## 4. Ruled-out directions

- **The Class A configuration (cheap per step, ~90 s wall clock, `per_step_cost_ratio` ≈ 1.02).** Ruled out: it produced reward 0.0000 with no evaluation row crossing the threshold in the declared direction and no qualifying budget row. Do not return to a low-per-step-cost, long-horizon setting.
- **Further small variation within Class B while leaving the ruleset perturbation untouched.** Ruled out as a way to gain meaningful reward: three attempts in that mode produced 0.5019, 0.5020, 0.5043 — a total movement of 0.0024 — with an identical `failed_checks` list and identical per-kind perturbation outcomes every time. The ceiling here is the `conformance_fraction` of 0.5.
- **Chasing `compute_efficiency` as the lever.** Ruled out on the evidence: efficiency fell from 0.6529 to 0.5856 across attempts 2→4 while reward rose. Efficiency is not what is gating the score, and optimising it will not move the half of the reward that `conformance_fraction` 0.5 is withholding.
- **Treating the primary target as the remaining problem.** Ruled out: `primary_target_reached` has been 1.0 for three consecutive attempts with C-TARGET-REACHED and C-BUDGET-RESPECTED holding on the primary. The loss is entirely on the held-out side.

## 5. Open leads

- **The ruleset-kind held-out run is the whole remaining gap, and C-LOG-WELL-FORMED plus C-NO-LATCH-CARRYOVER are the two checks nothing has yet addressed.** Across the four records there were eight held-out runs beside the primary. By kind: **ruleset — 0 of 4 reached, failing C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER every time; held_out_variant — 3 of 4 reached**, the single miss being in attempt 1 where it failed C-TARGET-REACHED and C-BUDGET-RESPECTED alongside the primary. In aggregate 3 of 8 reached. The held_out_variant kind now travels with the primary: fix the primary and it comes along. The ruleset kind does not, and it has never come along.
- **C-LOG-WELL-FORMED is the only check in the whole dataset that is exclusive to the ruleset kind, and it is a plausible root of the other three.** Note that the ruleset run's C-TARGET-REACHED and C-BUDGET-RESPECTED failures mirror the wording family of attempt 1's primary failure — "no qualifying row, so no budget position exists" — which is what a malformed or unparseable log would produce even if the underlying training reached its threshold. Emitting a correct, complete, schema-valid evaluation log under the ruleset perturbation is the highest-value single change available, and it may resolve three checks at once.
- **C-NO-LATCH-CARRYOVER points at state persisting where it should not.** It fires only on the ruleset kind and only there. Audit anything module-level, global, cached, or reused across phases — optimiser state, RNG state, a fitted preprocessor, a memoised threshold or best-so-far latch — and ensure the ruleset run starts from a clean slate and never reads a value latched during an earlier phase.
- **`task_pass` is 0.0 even when the primary target is reached.** No record has ever set it. It is worth establishing what `task_pass` requires beyond `primary_target_reached` — plausibly it needs `all_perturbations_held` true, i.e. it may unlock together with the ruleset fix — but this is untested and no supplied term states the dependency.
- **Preserve attempt 4's operating point.** `per_step_cost_ratio` ≈ 1.47, `qualifying_budget` 13.79, wall clock 13.79 s: that setting reaches the primary comfortably and leaves headroom. Change the ruleset-run logging and state handling on top of it rather than re-tuning the training loop.

**Call: exploit.** Take the attempt-4 configuration unchanged — it holds the best reward at 0.5043 and satisfies every primary-side check — and fix the one thing that has stopped it four times running: the ruleset-kind held-out run, starting with C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER. Attempts 2, 3 and 4 kept re-running the same Class B approach and re-earning the same C-PERTURBATION-REACHED failure without changing anything that could have caused it; that pattern must not be repeated. The remaining reward is on the other half of `conformance_fraction`, and it is reachable only through the ruleset perturbation.
