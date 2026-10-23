# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 1 -- reward 0.7684, first measured attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1 *      0.7684   0.857             2 of 2         yes             25                

  reward  = what the attempt scored, in the closed interval 0 to 1. No value of it is a pass:
            task pass is a separate conjunction and is reported beside the reward, not inferred
            from it. A high reward with a failed pass, or the reverse, is a real outcome.
  rule conformance = the fraction of the static conformance rules the submitted bytes held.
  perturbation runs = the held-out runs beside the primary one. They are described by kind
            and are deliberately not individually named, so no run has a label you can
            iterate against; what each one measured is not published either.
  --      = the run did not produce this measurement. It is not a zero.
  *       = the best reward so far, and the one to beat.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

One graded submission exists.

- **Attempt 1 — reward 0.7684** (`reward` = 0.7684495494479875, `measurement_status` = "measured"). `standing_against_best_so_far` = "first_measured_attempt", so there is no earlier result it stands against and no regression to report.

Attempt 1 holds the highest reward and **is the attempt to beat: 0.7684**.

Everything else recorded for attempt 1, so the next attempt can aim above it rather than merely reproduce it:

- `primary_target_reached` = 1.0 — the primary run reached its target.
- `validity` = 1.0, `red_line_crossed` = 0.0, `zero_reason_code` = 0 — the submission was valid, no red line was crossed, and nothing forced a zero.
- `all_perturbations_held` = true, `perturbations_declared` = 2.0 — both held-out runs held.
- `conformance_fraction` = 1.0 but `rule_conformance` = 0.8571428571428571 — i.e. six of seven rule checks held; exactly one did not.
- `task_pass` = 0.0 — the task-pass term did not register despite the primary target being reached. This is a distinct term from `primary_target_reached` and is the one place where a strong run scored nothing; it is not explained by anything else in the record and should be treated as an open question, not as a known failure cause.
- `compute_efficiency` = 0.8160403297407965, `per_step_cost_ratio` = 1.0638707778973995, `wall_clock_sec` = 25.461896419525146, `qualifying_budget` = 25.461896419525146. Wall clock exactly equals the qualifying budget, and the per-step cost ratio is slightly above 1.0 (≈6.4% above the reference per-step cost), leaving compute efficiency at 0.816 rather than 1.0.

# 2. Approach classes tried

Only **one** approach class has been graded, so this section is short by necessity — one record, one entry.

**Class A — a working training algorithm that trains and reaches target, written with executable logic at module scope.** The measured terms characterise it fully from the outside: it is functionally correct (primary target reached, both perturbation runs reached, validity 1.0, no red line, no zero-reason code), it is close to but not at the compute reference (per-step cost ratio 1.064, efficiency 0.816, wall clock 25.46 s consuming the whole qualifying budget), and it violates exactly one structural rule about what may appear at module level. The reward of 0.7684 is therefore an already-strong baseline whose shortfall is attributable to identifiable, separable terms — the single failed rule check, the sub-unity compute efficiency, and the zero `task_pass` — rather than to any training failure.

No second approach class exists yet. Nothing has been tried and abandoned; nothing has scored zero.

# 3. Checks that failed

One named check failed, in one record:

- **`C-API-SURFACE`** — verifier's reason: *"module-level statements outside imports, constants, and permitted definitions."* This has failed **once**, on attempt 1. Because there is only one graded record, nothing can yet be said about it recurring across changes; it is simply the one structural check standing between attempt 1 and full rule conformance (6/7 → 7/7).

Read literally, the reason says the submission file executes or declares something at module scope that is not an import, not a constant, and not one of the permitted definition forms (function/class definitions and the like). The fix is a file-layout fix, not an algorithmic one: everything that runs must be moved inside the permitted definitions the harness calls, leaving only imports, constant assignments, and definitions at top level. Do not paraphrase this as a general conformance problem — the identifier is `C-API-SURFACE` and the trigger is module-level statements.

Separately, and not a named check: **`task_pass` = 0.0**. This is not attributed to any check in the record and is not accompanied by a failure reason, so its cause is unknown from the measured terms. It should not be conflated with `C-API-SURFACE` unless a later measurement shows them moving together.

# 4. Ruled-out directions

Nothing has been ruled out by measurement. There is one graded attempt, it scored, and no approach has yet been shown not to work. Three things are worth recording as *not needing further work* rather than as ruled out:

- **Rewriting the training algorithm for correctness.** Ruled out as a priority because `primary_target_reached` = 1.0, `validity` = 1.0, `all_perturbations_held` = true and `zero_reason_code` = 0. The algorithm works; changing it risks the 0.7684 already banked.
- **Chasing perturbation robustness.** Ruled out as a priority because both declared held-out runs reached their thresholds with empty `failed_checks`. There is nothing to repair there (see the perturbation report below).
- **Treating attempt 1 as a failure to be replaced.** Ruled out because it is measured and positive; it is the baseline, not a discard.

# 5. Open leads

**Perturbation report (by kind and in aggregate).** Two held-out runs were declared beside the primary one. By kind: one run of kind **`held_out_variant`** reached its threshold with no failed checks; one run of kind **`seed`** reached its threshold with no failed checks. In aggregate: 2 of 2 reached, 0 stopped by any check, `all_perturbations_held` = true. No check is failing on any held-out run of either kind. These runs carry no names, numbers or positions and none should be assumed to persist across future records.

Leads, in order of expected value:

1. **Clear `C-API-SURFACE` by restructuring file layout only.** Move every executable module-level statement into the permitted definitions. Keep at top level only: imports, constant assignments, and function/class definitions. In particular, look for anything the pristine stub does not itself contain at module scope — instantiation, calls, loops, conditionals, prints, seeding, device selection, config construction, `if`-guards, and any assignment whose right-hand side is a call rather than a literal. Convert config values to plain literal constants or push them inside a function. This should take `rule_conformance` from 0.8571 to 1.0 while leaving the training logic byte-for-byte equivalent, and it is the single highest-confidence gain available.
2. **Recover `task_pass`.** It is 0.0 while the primary target was reached, so the two terms are measuring different things. Since `C-API-SURFACE` is the only recorded violation, the first experiment is cheap: fix the layout (lead 1) and observe whether `task_pass` moves. If it does, the two were coupled through the API surface — plausibly the harness could not reach the expected entry point because logic lived at module scope. If it does not, `task_pass` needs a separate hypothesis, and the next thing to check is that the submission exposes exactly the entry points and return shapes the stub declares, with the expected names and signatures.
3. **Close the compute gap.** `per_step_cost_ratio` = 1.0639 and `compute_efficiency` = 0.816, with wall clock (25.46 s) exactly equal to the qualifying budget. Roughly 6% per-step overhead is being paid. Target per-step work specifically rather than total steps, since the primary target is already reached and cutting steps risks it: avoid per-step allocations and host/device syncs, hoist invariant work out of the step, avoid recomputing anything constant, and prefer in-place or fused operations. Because wall clock sits exactly at budget, any per-step saving should show up directly in both `compute_efficiency` and headroom.
4. **Change one thing at a time.** Attempt 1's reward is the bar. The layout fix (lead 1) is provably behaviour-neutral if done as a pure move; the efficiency work (lead 3) is not. Landing lead 1 alone first gives a clean reading on whether `task_pass` is coupled to it, and preserves an attributable baseline if a later efficiency change costs the primary target.

**Call: exploit.** Attempt 1 already scores 0.7684 with the algorithm working, both perturbation kinds holding, no red line and no zero-reason code. Its shortfall is concentrated in one named, precisely-described rule check (`C-API-SURFACE`), one unexplained zero term (`task_pass`), and a ~6% per-step cost overhead. Keep the training algorithm; fix the module-level statements; then look at `task_pass` and per-step cost. Exploring a structurally different training approach is not warranted while the scoring approach has an unaddressed, explicitly-named defect.
