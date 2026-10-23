# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 2 -- reward 0.8385, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2 *      0.8385   1.000             2 of 2         yes             74                

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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Two attempts were graded; both carry `measurement_status: "measured"`, so both have a reward. Listed worst to best:

- **Attempt 1 — reward 0.7684** (0.7684495494479875). Valid (`validity` 1.0), no red line crossed (`red_line_crossed` 0.0), `zero_reason_code` 0. It reached the primary target (`primary_target_reached` 1.0) and held every declared perturbation (`all_perturbations_held` true, 2 declared), but it did **not** pass the task (`task_pass` 0.0) and its `rule_conformance` was 0.8571428571428571 against a `conformance_fraction` of 1.0, because of one failed check (see Section 3). Cost profile: `wall_clock_sec` 25.4619, `qualifying_budget` 25.4619, `compute_efficiency` 0.8160, `per_step_cost_ratio` 1.0639 (i.e. slightly more expensive per step than the reference).
- **Attempt 2 — reward 0.8385** (0.8385437894774304). `standing_against_best_so_far` is `better_than_every_earlier_attempt`. Clean: `failed_checks` empty, `rule_conformance` 1.0, `task_pass` 1.0, `primary_target_reached` 1.0, `validity` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, all 2 declared perturbations held. Cost profile: `wall_clock_sec` 73.6235, `qualifying_budget` 73.6235, `compute_efficiency` 0.9164, `per_step_cost_ratio` 0.9162 (cheaper per step than the reference).

**Attempt 2, at reward 0.8385, is the best result so far and is the score to beat.** No attempt produced a zero, and no attempt is missing a measurement.

The measured terms record outcomes, not source code, so nothing below claims knowledge of the actual implementations beyond what these fields support.

# 2. Approach classes tried

Only two distinct approach classes are distinguishable from the measured terms, and they differ on exactly two axes: module-level structure and compute profile.

**Class A — "fast but structurally non-conforming" (attempt 1).** A short-running submission: 25.46 s of wall clock, all of which counted as qualifying budget. It solved the held-out and seed perturbations and hit the primary target, so the learning content was adequate on the generalisation axis. Its two weaknesses were both scored: `task_pass` 0.0 (the task itself was not passed) and one conformance failure on the module surface. Its `per_step_cost_ratio` of 1.0639 says each step cost about 6% more than the reference step, and `compute_efficiency` 0.8160 is the lower of the two attempts despite the much shorter wall clock — so the short runtime came from doing fewer or shorter steps, not from cheaper ones.

**Class B — "conforming, longer-running, cheaper per step" (attempt 2).** Roughly 2.9× the wall clock of Class A (73.62 s, again fully counted as qualifying budget), yet with *better* `compute_efficiency` (0.9164 vs 0.8160) and a `per_step_cost_ratio` that dropped below 1.0 (0.9162 vs 1.0639). The combination — more total time, less cost per step — is consistent with the submission running more (or longer-horizon) training steps that are individually cheaper than the reference step. This class passed the task (`task_pass` 1.0), reached full `rule_conformance` 1.0 with no failed checks, and held all perturbations. It is the only class that has cleared every graded gate simultaneously, and it produced the top reward.

The transition from Class A to Class B moved three things at once: it fixed the module-surface conformance failure, it turned `task_pass` from 0.0 to 1.0, and it changed the compute profile. Because they moved together, the terms do not attribute the +0.0701 reward gain to any one of them individually.

# 3. Checks that failed

One named check has failed, once, in attempt 1 only:

- **`C-API-SURFACE`** — verifier's reason: *"module-level statements outside imports, constants, and permitted definitions."* This is a structural constraint on the submission file: at module scope, only imports, constant assignments, and the permitted definitions (functions/classes) are allowed. Anything else executed at import time — a print, a call, a setup block, an `if __name__` guard body doing work, a mutable global built by running code, a decorator side effect, a top-level seed or device initialisation — trips it. It drove `rule_conformance` down to 0.8571428571428571 (6 of 7 conformance items held) while `conformance_fraction` remained 1.0.

This check **did not recur**: attempt 2 has an empty `failed_checks` list and `rule_conformance` 1.0, so whatever attempt 2 did with module-level structure satisfies `C-API-SURFACE` and should be preserved verbatim in shape. Since the next attempt restarts from a pristine stub, the constraint must be re-satisfied from scratch: keep all executable work inside function or method bodies, and let the module body contain only imports, literal constants, and definitions.

No other check has failed in any record, and no check has failed more than once.

# 4. Ruled-out directions

- **Leaving initialisation or any executable statement at module scope.** Ruled out by the `C-API-SURFACE` failure in attempt 1 with the stated reason; it cost roughly 14 percentage points of `rule_conformance` and the attempt still only reached 0.7684.
- **Treating reward as dominated by wall clock, i.e. optimising for the shortest run.** Ruled out by direct comparison: attempt 1 ran in 25.46 s and scored 0.7684; attempt 2 ran in 73.62 s — 2.9× longer — and scored 0.8385, higher. Short total runtime by itself did not buy reward, and the shorter run had the *worse* `compute_efficiency` (0.8160 vs 0.9164). Budget was not the binding constraint in either attempt (`red_line_crossed` 0.0 both times).
- **Spending effort on perturbation robustness.** Ruled out as a lever because it is already saturated: in both attempts `all_perturbations_held` is true, `perturbations_declared` is 2, and every unit reached its threshold with no failing check. There is no headroom here to recover.
- **Chasing `primary_target_reached`.** Ruled out for the same reason: it is 1.0 in both attempts, including the attempt that failed the task and a conformance check. It is not what separates the two rewards.
- **Any change that risks `validity` or trips the red line.** Both attempts have `validity` 1.0, `red_line_crossed` 0.0 and `zero_reason_code` 0; there is nothing to gain here and a zero to lose.

# 5. Open leads

- **Rebuild the Class B (attempt 2) shape first and re-establish the clean baseline.** It is the only configuration that has produced `task_pass` 1.0, `rule_conformance` 1.0 and reward 0.8385. From the pristine stub, reconstruct: all logic inside permitted definitions, module body limited to imports/constants/definitions (satisfies `C-API-SURFACE`), and a training loop whose per-step cost is below the reference (attempt 2 achieved `per_step_cost_ratio` 0.9162).
- **Attack `compute_efficiency`, which is the clearest remaining headroom.** It stands at 0.9164 with the other graded gates already at their ceilings (`task_pass` 1.0, `rule_conformance` 1.0, `validity` 1.0, `primary_target_reached` 1.0, all perturbations held). The two attempts differ 0.8160 → 0.9164 on this term while reward moved 0.7684 → 0.8385, which is consistent with efficiency and conformance/task-pass jointly carrying the reward.
- **Cut total wall clock while holding `task_pass` at 1.0.** Attempt 2 spent 73.62 s of qualifying budget with a per-step ratio of 0.9162; attempt 1 showed the task is reachable in a 25 s neighbourhood, though it failed the task there. The specific experiment: keep attempt 2's cheap per-step formulation and reduce the number of steps / epochs / evaluation passes toward the middle of that 25–74 s range, checking after each cut that `task_pass` stays 1.0 and all perturbations still hold. If task pass degrades, back off — a `task_pass` 0.0 attempt scored 0.7684, well below the 0.8385 to beat.
- **Push `per_step_cost_ratio` further below 0.9162** without shortening the schedule: cheaper per-step arithmetic (larger batches with fewer steps, avoiding redundant forward passes, no per-step full-dataset evaluation, minimal host/device transfer, no per-step logging or copies). This raises `compute_efficiency` without touching the task-pass margin.
- **Hold the perturbation surface intact while doing the above.** Across both records there are four held-out runs in aggregate — two of kind `held_out_variant` and two of kind `seed` — and every one reached its threshold with an empty `failed_checks` list; no run of either kind has ever been stopped by a check. That means the current formulation generalises across both variant and seed changes, so any efficiency cut must avoid seed-specific or variant-specific shortcuts (no hardcoded seed, no fixed data assumptions) that would convert these into failures.

**Call: exploit.** Attempt 2's approach class is clean on every gate and holds the best reward at 0.8385; the remaining measured slack is in `compute_efficiency` (0.9164) and `per_step_cost_ratio` (0.9162), both of which are refinements of that same approach rather than reasons to restructure it. Note also that attempt 1's `C-API-SURFACE` failure was a one-off that attempt 2 already fixed — re-introducing module-level executable code would be repeating a known-losing move, and the next attempt must re-apply the fix from the stub rather than assume it.
