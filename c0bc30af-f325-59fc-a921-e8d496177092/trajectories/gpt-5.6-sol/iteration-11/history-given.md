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

    All five attempts since have scored lower than it.
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
  8        0.7805   1.000             2 of 2         yes             99                
  9        0.8332   1.000             2 of 2         yes             50                
  10       0.8503   1.000             2 of 2         yes             75                

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
  4 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 8 -- reward 0.7805, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 99
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.8332, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 10 -- reward 0.8503, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 75
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED failed on attempt 7.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Ten graded submissions, all with `measurement_status: "measured"`. Every one carries a reward; none is missing a measurement. Ranked worst to best:

| Rank | Attempt | reward | Standing as reported |
|---|---|---|---|
| 1 (worst) | 7 | 0.4911 | worse than an earlier attempt |
| 2 | 6 | 0.7580 | worse than an earlier attempt |
| 3 | 4 | 0.7740 | worse than an earlier attempt |
| 4 | 8 | 0.7805 | worse than an earlier attempt |
| 5 | 2 | 0.8079 | worse than an earlier attempt |
| 6 | 9 | 0.8332 | worse than an earlier attempt |
| 7 | 10 | 0.8503 | worse than an earlier attempt |
| 8 | 1 | 0.8630 | first measured attempt |
| 9 | 3 | 0.8657 | better than every earlier attempt |
| 10 (best) | 5 | 0.8658 | better than every earlier attempt |

**Attempt 5 holds the highest reward, 0.8658, and is the mark to beat.** Attempt 3 (0.8657) is effectively tied with it, and attempt 1 (0.8630) is just behind; those three form the top band.

Every attempt after the best one regressed, and this must be stated plainly rather than read as progress: attempt 6 (0.7580), attempt 7 (0.4911), attempt 8 (0.7805), attempt 9 (0.8332) and attempt 10 (0.8503) are each explicitly recorded as *worse than an earlier attempt*. The last five graded attempts have produced no improvement at all. Attempt 2 (0.8079) was also a regression against attempt 1, and attempt 4 (0.7740) a regression against attempt 3.

Supporting terms worth carrying forward, because reward tracks them:

- `validity` = 1.0 and `red_line_crossed` = 0.0 on all ten; `zero_reason_code` = 0 on all ten. Nothing has ever been invalidated or tripped a red line, and nothing scored zero.
- `primary_target_reached` = 1.0 on all ten. The primary run has always hit its target; the reward differences come from cost/conformance terms, not from failing the main task.
- `task_pass` = 1.0 on eight attempts, but 0.0 on attempts 6 and 7 — the two attempts that carry failed checks. Those two are also the two lowest rewards.
- Operating point of the top band (attempts 5, 3, 1): `wall_clock_sec` ≈ 74.4 / 74.4 / 76.3, `qualifying_budget` ≈ 74.4 / 74.4 / 76.3, `compute_efficiency` ≈ 0.693 / 0.692 / 0.678, `per_step_cost_ratio` ≈ 0.958 / 0.984 / 1.072.

# 2. Approach classes tried

I was given only the measured terms — no source, no configuration text. The classes below are therefore grouped by the measured operating point each attempt produced, which is what the next attempt can actually aim at and re-derive. Records with the same measured signature are collapsed into one entry.

**Class A — baseline-cost, full-budget configuration (attempts 1, 3, 5, 10; also 2).** Per-step cost near parity with the reference (`per_step_cost_ratio` 0.94–1.07), compute efficiency in the 0.68–0.75 band, wall clock and qualifying budget both ≈ 74–76 s, all conformance checks clean, both perturbation units reaching threshold. This class produced every reward above 0.80 and all three of the top-band results (0.8658, 0.8657, 0.8630) plus 0.8503 and 0.8079. It is the only class that has ever set a best-so-far. Within the class, the highest rewards sit at `per_step_cost_ratio` between 0.95 and 0.99 with compute efficiency ≈ 0.69.

**Class B — aggressive per-step cost reduction (attempt 4).** `per_step_cost_ratio` driven down to 0.6934, the lowest of any attempt, and `compute_efficiency` pushed to 0.9681, by far the highest recorded. Conformance stayed perfect, both perturbations held, the primary target was still reached, yet reward *fell* to 0.7740 — below every Class A result except attempt 2. Cheapening each step this hard costs more in whatever the reward weights than the efficiency term returns.

**Class C — expensive-per-step / long-wall-clock configuration (attempt 8; and, in a degraded form, attempt 6).** Attempt 8 ran 98.6 s of wall clock with `qualifying_budget` 98.6 and `per_step_cost_ratio` 1.0848, compute efficiency 0.6575, clean conformance, both perturbations held — reward 0.7805, a clear regression. Attempt 6 pushed `per_step_cost_ratio` to 1.4094 (compute efficiency 0.4942) and additionally broke a conformance check — reward 0.7580.

**Class D — truncated / shortened run (attempts 7 and 9, in two different forms).** Attempt 7 finished in 50.0 s with `qualifying_budget` 50.0, and one held-out run then blew its own budget check; reward collapsed to 0.4911, the worst result recorded. Attempt 9 shows a related but milder signature: `wall_clock_sec` 74.4 but `qualifying_budget` only 49.9, conformance clean, both perturbations held, reward 0.8332 — below the top band. Shrinking the qualifying budget away from the ≈74 s that the top band uses has never helped.

**Class E — submission-file structure change that broke the module surface (attempt 6).** Distinct from its cost profile: whatever restructuring was done put executable statements at module level, which the harness rejects. Discussed under section 3.

# 3. Checks that failed

Eight of ten attempts have an empty `failed_checks` list, `conformance_fraction` 1.0 and `rule_conformance` 1.0. Two attempts failed checks, and each named check has failed exactly once so far. There is no repeat offender across records — no check has failed in more than one attempt — so no single conformance defect has survived a change and none of them can yet be said to be independent of what was edited between attempts.

- **`C-API-SURFACE`** — failed once, in attempt 6. Verifier's reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions."* This dropped `rule_conformance` to 0.8571 and `conformance_fraction` stayed 1.0, but `task_pass` went to 0.0. The submission module must contain nothing at top level except imports, constant assignments, and the permitted definitions (functions/classes); no top-level execution, no setup calls, no prints, no `if __name__` blocks doing work, no module-level instantiation or side effects. Move any such work inside the permitted entry-point definitions.

- **`C-PERTURBATION-REACHED`** — failed once, in attempt 7. Verifier's reason, verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This halved `conformance_fraction` to 0.5, set `all_perturbations_held` to false and `task_pass` to 0.0, and is the direct cause of the worst reward on record (0.4911).

- **`C-BUDGET-RESPECTED`** — failed once, at the perturbation-unit level in attempt 7, on a held-out-variant run. This is the underlying cause of the `C-PERTURBATION-REACHED` failure above: the variant run did not reach its threshold inside its own budget.

Perturbation outcomes, reported by kind and in aggregate. Each record declares two perturbation units (`perturbations_declared` = 2.0), one of kind `seed` and one of kind `held_out_variant`, giving 20 units across the ten records.

- **By kind — `seed`:** 10 of 10 reached their threshold, with no failed checks on any of them. Seed perturbation has never been a problem.
- **By kind — `held_out_variant`:** 9 of 10 reached their threshold. The single failure occurred in attempt 7 and was stopped by `C-BUDGET-RESPECTED`. The runs are not identified by name, number or position, so nothing here says that any particular held-out run recurs across records; what the data supports is only that the *held-out-variant kind* is the kind that failed, and it failed on the budget check.
- **Aggregate:** 19 of 20 perturbation units held. `all_perturbations_held` is true in nine records and false only in attempt 7.

# 4. Ruled-out directions

- **Maximising compute efficiency / minimising per-step cost.** Attempt 4 achieved `compute_efficiency` 0.9681 and `per_step_cost_ratio` 0.6934 — the best efficiency numbers on record, with perfect conformance and both perturbations held — and still scored 0.7740, roughly 0.092 below the best. Efficiency is not the binding term; buying it at the price of whatever the primary quality term measures loses reward. Do not repeat a cost-ratio near 0.69.

- **Raising per-step cost well above parity.** Attempt 8 at ratio 1.0848 with a 98.6 s wall clock scored 0.7805, and attempt 6 at ratio 1.4094 scored 0.7580. Note the nuance: attempt 1 ran at ratio 1.0723 and still scored 0.8630, so a ratio slightly above 1 is not fatal by itself — but pairing an above-parity ratio with a wall clock stretched to ~99 s, or pushing the ratio to ~1.4, both regressed hard.

- **Shortening the qualifying budget below the ~74 s the top band uses.** Attempt 7 cut it to 50.0 s and a held-out-variant run then failed `C-BUDGET-RESPECTED`, producing the worst reward on record (0.4911). Attempt 9 kept the 74.4 s wall clock but recorded a 49.9 s qualifying budget and scored 0.8332, still below the top band. Compressing the schedule has cost reward in both forms it was tried.

- **Any module-level executable code in the submission.** Ruled out by the `C-API-SURFACE` failure in attempt 6, which zeroed `task_pass` and cut `rule_conformance` to 0.8571. There is no upside to be recovered here; the constraint is explicit in the verifier's reason.

- **Repeating the attempt-2 point.** Attempt 2 sits inside Class A (`per_step_cost_ratio` 0.9441, compute efficiency 0.7226, clean conformance) yet scored 0.8079, well below its Class A siblings. Whatever distinguished it from attempts 3/5/10 within the same measured envelope was harmful; the envelope alone does not guarantee the score.

# 5. Open leads

1. **Reconstruct and re-hit the attempt-5 operating point exactly, then perturb one dimension.** The target signature is: `wall_clock_sec` ≈ 74.4 s, `qualifying_budget` ≈ 74.4 s (i.e. the qualifying budget should equal the wall clock, not be a truncated fraction of it), `per_step_cost_ratio` ≈ 0.958, `compute_efficiency` ≈ 0.693, empty `failed_checks`, both perturbation units reaching threshold. Attempts 3 (ratio 0.9835) and 5 (ratio 0.9581) bracket a narrow band and scored 0.8657 and 0.8658; attempt 10 at ratio 0.9615 scored 0.8503, so the band is not perfectly monotone and the residual differences are not explained by cost ratio alone. Land inside the band first, confirm the score reproduces near 0.866, and only then vary.

2. **Probe the interval between parity and the attempt-4 point, i.e. `per_step_cost_ratio` in roughly 0.85–0.95.** Ratio 0.96–0.98 gives the best rewards seen; ratio 0.69 gives 0.7740. The reward-versus-cost curve therefore turns somewhere in between and has never been sampled in 0.70–0.94. A single probe near 0.90 would locate the turn and tell you whether any efficiency at all can be bought without losing reward.

3. **Separate the two things attempt 9 changed.** It reported a 74.4 s wall clock but a 49.9 s qualifying budget and lost ~0.033 against the best. If the qualifying budget can be restored to the full wall clock while keeping whatever else attempt 9 did, that lost margin may come back. This is the cheapest identified regression to reverse.

4. **Give the held-out-variant run explicit budget headroom.** The only perturbation failure on record is a held-out-variant run stopped by `C-BUDGET-RESPECTED`, and it appeared as soon as the overall schedule was compressed to ~50 s. Any schedule, early-stopping rule or iteration count should be sized so the variant finishes inside *its own* budget rather than being tuned against the primary run's budget. Do not tie the variant's stopping condition to primary-run wall clock.

5. **Keep the module surface trivially clean by construction.** Imports, constants, and permitted definitions only; all initialisation, seeding, device selection, data setup and training loop bodies inside functions. This is a guardrail rather than a lead, but `C-API-SURFACE` cost an entire attempt and it is free to avoid.

6. **Attribute the top-band spread.** Attempts 1, 3 and 5 span 0.8630–0.8658 while sitting at similar conformance and perturbation outcomes but different cost ratios (1.072, 0.984, 0.958). The 0.0028 spread is small; treat differences under ~0.003 as inside the reproducibility of this harness and do not chase them as if they were signal.

**Call: exploit.** Class A is the only approach that has ever set a best-so-far, and its ceiling (0.8658) has not been beaten by the cost-cutting (Class B), cost-inflating (Class C) or truncated (Class D) variants that followed — all five attempts after the best regressed. The right move is to rebuild the Class A operating point described in lead 1, confirm it reproduces near 0.8658, and then make exactly one controlled change per attempt from leads 2–4, since the two things that have demonstrably cost whole tenths of reward (`C-API-SURFACE`, and the held-out-variant `C-BUDGET-RESPECTED` failure behind `C-PERTURBATION-REACHED`) are both avoidable by construction. A caution about the loop's earlier behaviour: attempts 6 through 10 each moved to a different measured operating point and each scored below attempt 5 without isolating why, which is neither exploiting nor exploring — do not continue changing several dimensions at once. If two or three disciplined single-variable probes around the Class A point all land inside 0.003 of 0.8658, then and only then is the class exhausted and a structurally different idea warranted.
