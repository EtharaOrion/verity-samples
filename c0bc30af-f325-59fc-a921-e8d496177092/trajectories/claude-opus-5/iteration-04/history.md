# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 4 -- reward 0.8719, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4 *      0.8719   1.000             2 of 2         yes             50                

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

    attempt 1 -- reward 0.7684, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 2 -- reward 0.8385, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 3 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 1.
    C-BUDGET-RESPECTED failed on attempt 3.
    C-PERTURBATION-REACHED failed on attempt 3.
    C-TARGET-REACHED failed on attempt 3.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Four graded submissions, all with `measurement_status: measured`, so all four carry a reward. Listed worst to best:

- **Attempt 3 — reward 0.0000.** Zeroed out (`zero_reason_code: 4`, `primary_target_reached: 0.0`, `task_pass: 0.0`, `conformance_fraction: 0.0`). This is **lower than both attempts that preceded it**; `standing_against_best_so_far` reads `worse_than_an_earlier_attempt`, and that is a regression, not partial progress. Wall clock 1692.5153 s — roughly 23× the previous attempt and 34× attempt 4. Notably `rule_conformance` was 1.0 and `validity` 1.0 and `per_step_cost_ratio` 0.8484: the code was well-formed and cheap per step; it simply never crossed the threshold, and `qualifying_budget` is reported as `not-measured` because no qualifying row existed.
- **Attempt 1 — reward 0.7684.** `standing_against_best_so_far: first_measured_attempt`. Primary target reached (1.0) and both held-out runs held, but `task_pass: 0.0` and `rule_conformance: 0.8571` (i.e. six of seven rules) because of one failed check. Wall clock 25.4619 s — the fastest of all four — yet `compute_efficiency` only 0.8160 and `per_step_cost_ratio` 1.0639, the only attempt whose per-step cost exceeded the reference.
- **Attempt 2 — reward 0.8385.** `better_than_every_earlier_attempt` at the time. Clean: no failed checks, `rule_conformance` 1.0, `task_pass` 1.0, `conformance_fraction` 1.0, both perturbations held. Wall clock 73.6235 s, `compute_efficiency` 0.9164, `per_step_cost_ratio` 0.9162.
- **Attempt 4 — reward 0.8719. This is the highest reward recorded and the one to beat.** `better_than_every_earlier_attempt`. No failed checks, `rule_conformance` 1.0, `validity` 1.0, `task_pass` 1.0, `conformance_fraction` 1.0, both perturbations held, `compute_efficiency` 1.0 (saturated), `per_step_cost_ratio` 0.7115 (the cheapest per step of any attempt), wall clock 50.0341 s with `qualifying_budget` 50.0341 s.

The trend across the three non-zero attempts is monotone upward: 0.7684 → 0.8385 → 0.8719. Attempt 3 is the sole break in that trend and it produced a hard zero.

Worth stating precisely, because it bounds what is left to win: in attempt 4 every reported sub-quantity that has a visible ceiling is already at it — `compute_efficiency` 1.0, `rule_conformance` 1.0, `validity` 1.0, `task_pass` 1.0, `conformance_fraction` 1.0, `primary_target_reached` 1.0, `red_line_crossed` 0.0 — and yet reward is 0.8719, not 1.0. The residual ~0.128 is therefore driven by something the supplied terms do not name. I will not guess what it is; the next attempt should treat it as an unknown margin term rather than assume more speed will recover it, since speed is already maxed.

## 2. Approach classes tried

Only the measured terms were carried forward, not the source, so these classes are characterised by their measured signatures. Three distinct classes plus one regression appear.

**Class A — fast configuration with non-conforming module structure (attempt 1).** Shortest runtime of any attempt (25.4619 s) and the target was reached on the primary run and on both held-out runs. Its distinguishing signature is `per_step_cost_ratio` 1.0639, the only value above 1.0 recorded: each step cost more than the reference step, and the short wall clock came from doing fewer steps rather than cheaper ones. It also carried module-level executable statements outside imports, constants and permitted definitions, which cost it the `C-API-SURFACE` check and dropped `rule_conformance` to 0.8571 and `task_pass` to 0.0. Reward 0.7684. Takeaway: reaching the target fast is not sufficient; the API-surface discipline is separately priced, and losing one of seven rules cost roughly 0.07 of reward relative to the next attempt.

**Class B — conformant baseline, generous step budget (attempt 2).** The structural defect of Class A was removed: all module-level work moved inside permitted definitions so nothing executes at import time. Every check held. Runtime rose to 73.6235 s and `per_step_cost_ratio` fell to 0.9162, i.e. cheaper steps but more of them, or a longer schedule. Reward 0.8385, the first clean measurement. This established that full conformance plus target-reached is worth about +0.070 over the same result with `C-API-SURFACE` broken.

**Class C — conformant, tightened schedule and cheaper steps (attempt 4).** Same conformance posture as Class B, but the run was compressed to 50.0341 s while `per_step_cost_ratio` improved further to 0.7115 and `compute_efficiency` reached its ceiling of 1.0. Target still reached on the primary run and on both held-out runs. Reward 0.8719 — the best. Takeaway: shortening the schedule while keeping every check green converts directly into reward, and this lever is now exhausted because `compute_efficiency` cannot exceed 1.0.

**Class D — long-horizon variant that never converged (attempt 3).** Structurally conformant (`rule_conformance` 1.0, `validity` 1.0, no `C-API-SURFACE` failure) and cheap per step (`per_step_cost_ratio` 0.8484, better than Class B), but it ran 1692.5153 s and no evaluation row ever crossed the threshold in the declared direction. Because no row qualified, no budget position existed either, so the budget check failed as a consequence rather than as an independent fault. This class scored a hard zero. Whatever was changed here — the very long horizon combined with the cheap-step configuration — moved the run away from convergence, not toward it.

## 3. Checks that failed

Four distinct check identifiers appear across the records.

- **`C-API-SURFACE`** — reason: *"module-level statements outside imports, constants, and permitted definitions."* Failed **once**, in attempt 1 only. It has held in every attempt since.
- **`C-TARGET-REACHED`** — reason: *"no evaluation row crosses the threshold in the declared direction."* Failed in attempt 3 only, but within that single record it failed **three times over**: once at the primary level and once in each of the two held-out runs. This is the check that produced the zero.
- **`C-BUDGET-RESPECTED`** — reason: *"no qualifying row, so no budget position exists."* Failed in attempt 3 only, again at the primary level and in both held-out runs. Its stated reason makes it strictly downstream of `C-TARGET-REACHED`: it did not fail on its own terms, it failed because nothing qualified. Fixing convergence fixes this check for free; tuning the budget without fixing convergence will not.
- **`C-PERTURBATION-REACHED`** — reason: *"0 of 2 declared perturbations reached their own threshold inside their own budget."* Failed in attempt 3 only, at the primary level, and is the roll-up of the two held-out failures above.

**No check identifier has failed in more than one attempt.** Each failure was fixed and stayed fixed: `C-API-SURFACE` broke once and never recurred; the three attempt-3 checks broke once, in the record that also has the anomalous 1692 s runtime, and all held again in attempt 4. There is therefore no persistent check that the edits so far have failed to address — the failure pattern is one-off per class, not chronic.

## 4. Ruled-out directions

- **Leaving executable statements at module scope.** Ruled out by the `C-API-SURFACE` failure in attempt 1 with reason "module-level statements outside imports, constants, and permitted definitions." It cost `task_pass` outright (0.0) and one seventh of `rule_conformance` (0.8571). Everything that runs must live inside permitted definitions; the module body may contain only imports, constants and definitions.
- **Very long training horizons (order 1700 s) as a route to a better result.** Ruled out by attempt 3: 1692.5153 s produced no threshold crossing at all on the primary run or on either held-out run, and a reward of 0.0000. Cheap steps (`per_step_cost_ratio` 0.8484) did not compensate. Long horizons are not merely inefficient here, they are the configuration under which convergence was lost.
- **Buying reward with more wall clock generally.** Ruled out by the ordering of the clean attempts: 73.6235 s scored 0.8385 while 50.0341 s scored 0.8719. Shorter and cheaper was strictly better among conformant runs.
- **Further pursuit of raw speed / compute efficiency as the primary lever.** Ruled out by saturation, not by failure: attempt 4 already reports `compute_efficiency` 1.0. There is no headroom left in that term, so a fifth attempt that only shaves seconds cannot beat 0.8719 through that channel and risks re-crossing the threshold as in attempt 3.
- **Re-running the attempt-3 configuration unchanged.** It scored zero for a specific, named reason — the target was never crossed. Repeating a zero-scoring configuration without changing what caused the zero is neither exploration nor exploitation. Attempt 4 correctly abandoned it, and it should not be revisited.

## 5. Open leads

- **Start from the Class C / attempt-4 posture and treat it as the baseline.** Conformant module structure (no module-level execution), the tightened schedule around 50 s, and whatever produced `per_step_cost_ratio` 0.7115. That combination holds every check and reaches the target on the primary run and on both held-out runs. Do not regress any of it.
- **Attack the unexplained residual.** With `compute_efficiency`, `rule_conformance`, `validity`, `task_pass`, `conformance_fraction` and `primary_target_reached` all at their ceilings and `red_line_crossed` at 0.0, the remaining ~0.128 of reward must come from a quantity not itemised in the terms supplied — most plausibly the margin by which evaluation rows clear the threshold, or the quality of the qualifying row rather than the mere fact of qualifying. The productive experiment is to hold runtime near 50 s and push the result further past the threshold rather than merely across it.
- **Widen the safety margin on the held-out runs specifically.** Attempt 3 shows the target can be missed on the held-out runs as easily as on the primary one. Any change that improves the primary margin should be checked for whether it also improves the held-out margin, since a single non-reaching held-out run of either kind triggers `C-PERTURBATION-REACHED` and zeroes the attempt.
- **If runtime is reduced further, do it in small increments and verify convergence each time.** The 50 s point already saturates `compute_efficiency`, so the only reason to go shorter is to buy budget headroom elsewhere; going shorter carries the attempt-3 risk of losing the threshold crossing with no compensating gain.

**Perturbation-unit outcomes.** Every record declared exactly 2 perturbations, one of kind `held_out_variant` and one of kind `seed` — 8 held-out runs across the four graded records. Six reached their threshold: both runs in attempt 1, both in attempt 2, both in attempt 4, in each case with no failed checks. Two did not reach, both inside attempt 3 — the `held_out_variant` run and the `seed` run each failed on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. By kind, then, the `held_out_variant` runs reached 3 times out of 4 and the `seed` runs reached 3 times out of 4, and the single failure of each kind occurred in the same record and on the same two checks. Both kinds are equally exposed: neither kind is more fragile than the other on this evidence, and the failure mode for both is "no evaluation row crosses the threshold in the declared direction," with the budget check falling out as a consequence. The runs are not individually identified in the data, so nothing here should be read as tracking a particular run across records.

**Call: exploit.** The scoring line is still climbing — 0.7684 to 0.8385 to 0.8719 — and the best attempt has not plateaued; it has merely exhausted one of its levers (`compute_efficiency`, now 1.0). The next attempt should take attempt 4's structure intact and push on the unmeasured margin above the threshold while keeping runtime near 50 s and all four named checks green. Exploration into new structures is not yet warranted, and the one structural departure that was tried, the long-horizon Class D, is the only attempt that scored 0.0000.
