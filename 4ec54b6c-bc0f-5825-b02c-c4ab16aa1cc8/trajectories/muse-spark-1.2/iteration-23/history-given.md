# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 21 -- reward 0.7322, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All three attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2        0.7155   1.000             2 of 2         yes             17                
  3        0.6279   1.000             2 of 2         yes             20                
  4        0.5792   1.000             2 of 2         yes             18                
  5        0.6587   1.000             2 of 2         yes             21                
  6        --       --                --             --              --                
  7        --       --                --             --              --                
  8        0.5444   1.000             2 of 2         yes             26                
  9        0.5164   0.857             2 of 2         yes             17                
  10       0.5983   1.000             2 of 2         yes             20                
  11       0.6639   1.000             2 of 2         yes             20                
  12       0.4962   1.000             1 of 2         yes             17                
  13       0.5590   1.000             2 of 2         yes             21                
  14       0.6426   1.000             2 of 2         yes             18                
  15       0.5830   1.000             2 of 2         yes             24                
  16       0.5701   1.000             2 of 2         yes             21                
  17       0.5274   0.857             2 of 2         yes             24                
  18       0.5755   1.000             2 of 2         yes             21                
  19       0.7134   1.000             2 of 2         yes             17                
  20       0.5107   0.857             2 of 2         yes             17                
  21 *     0.7322   1.000             2 of 2         yes             14                
  22       0.6376   1.000             2 of 2         yes             17                
  23       0.6877   1.000             2 of 2         yes             20                
  24       0.6833   1.000             2 of 2         yes             20                

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
  18 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 2 -- reward 0.7155, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.7134, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 22 -- reward 0.6376, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 23 -- reward 0.6877, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 24 -- reward 0.6833, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (9, 17, 20). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-four attempts were submitted. Twenty-two carry a measurement. Attempts 6 and 7 have `measurement_status: harbor_exception`, no `failed_checks` entries and every term marked `not-measured`: they produced **no measurement at all** and must not be read as scores of zero — nothing can be inferred from them about the code they contained.

The twenty-two measured attempts, worst reward to best:

| Rank | Attempt | reward | wall_clock_sec | per_step_cost_ratio | compute_efficiency | task_pass | failed checks |
|---|---|---|---|---|---|---|---|
| 1 | 12 | 0.4962 | 16.78 | 1.4886 | 0.6278 | 0.0 | C-PERTURBATION-REACHED |
| 2 | 20 | 0.5107 | 17.39 | 1.5804 | 0.6658 | 0.0 | C-API-SURFACE |
| 3 | 9 | 0.5164 | 17.12 | 1.4988 | 0.6647 | 0.0 | C-API-SURFACE |
| 4 | 17 | 0.5274 | 23.58 | 1.2123 | 0.8228 | 0.0 | C-API-SURFACE |
| 5 | 8 | 0.5444 | 26.10 | 0.9674 | 0.9679 | 1.0 | none |
| 6 | 13 | 0.5590 | 20.60 | 1.2404 | 0.7642 | 1.0 | none |
| 7 | 16 | 0.5701 | 20.98 | 1.1256 | 0.8684 | 1.0 | none |
| 8 | 18 | 0.5755 | 20.63 | 1.5846 | 0.6466 | 1.0 | none |
| 9 | 4 | 0.5792 | 17.51 | 1.1656 | 0.8832 | 1.0 | none |
| 10 | 15 | 0.5830 | 23.70 | 1.6313 | 0.6165 | 1.0 | none |
| 11 | 10 | 0.5983 | 20.15 | 1.5152 | 0.5686 | 1.0 | none |
| 12 | 3 | 0.6279 | 20.30 | 1.5225 | 0.6033 | 1.0 | none |
| 13 | 22 | 0.6376 | 17.37 | 1.5983 | 0.6629 | 1.0 | none |
| 14 | 14 | 0.6426 | 17.78 | 1.6303 | 0.6320 | 1.0 | none |
| 15 | 5 | 0.6587 | 20.53 | 1.6262 | 0.6098 | 1.0 | none |
| 16 | 11 | 0.6639 | 20.06 | 1.0166 | 0.8424 | 1.0 | none |
| 17 | 1 | 0.6694 | 17.43 | 1.5134 | 0.5488 | 1.0 | none |
| 18 | 24 | 0.6833 | 19.98 | 1.5539 | 0.5850 | 1.0 | none |
| 19 | 23 | 0.6877 | 20.11 | 1.5949 | 0.6081 | 1.0 | none |
| 20 | 19 | 0.7134 | 17.49 | 1.5834 | 0.6001 | 1.0 | none |
| 21 | 2 | 0.7155 | 17.45 | 1.5175 | 0.6205 | 1.0 | none |
| 22 | **21** | **0.7322** | **14.39** | 1.5700 | 0.6162 | 1.0 | none |

**Attempt 21 holds the highest reward, 0.7322. That is the number to beat.** Only two attempts ever carried `standing_against_best_so_far: better_than_every_earlier_attempt` — attempt 2 (0.7155) and attempt 21 (0.7322). Every other measured attempt is marked `worse_than_an_earlier_attempt`, including all three attempts after the best one: attempt 22 scored 0.6376, attempt 23 scored 0.6877 and attempt 24 scored 0.6833, all plainly **below** 0.7322 and below attempt 2's 0.7155. The last three attempts were regressions, not progress.

`validity` is 1.0 and `red_line_crossed` is 0.0 in every measured record; `zero_reason_code` is 0 throughout. No attempt was ever invalidated or zeroed — the entire spread from 0.4962 to 0.7322 is graded variation, not collapse.

One caution the numbers themselves force: attempts 1 and 2 have near-identical fingerprints (17.43s vs 17.45s wall clock, per-step cost ratio 1.5134 vs 1.5175) yet rewards 0.6694 and 0.7155, a gap of 0.046. A difference smaller than roughly 0.05 between two attempts cannot be safely attributed to the change made between them.

# 2. Approach classes tried

The submissions' source is not available to me; the groupings below are drawn from the measured terms, which separate cleanly into four fingerprints.

**Class A — high per-step compute, moderate wall clock (per_step_cost_ratio ≈ 1.50–1.63, wall_clock ≈ 14–21 s).** Attempts 1, 2, 3, 5, 10, 14, 18, 19, 21, 22, 23, 24. This class contains every one of the top results and the best result overall. Within it reward tracks total wall clock closely: 14.39 s → 0.7322 (attempt 21), 17.4–17.5 s → 0.7155, 0.7134, 0.6694, 0.6376, ~20 s → 0.6877, 0.6833, 0.6587, 0.6279, 0.5983, 0.5755, 23.70 s → 0.5830. Compute efficiency in this class sits low (0.55–0.66) and that did not prevent it from scoring highest.

**Class B — cheapened per-step work, high compute efficiency (per_step_cost_ratio ≈ 0.97–1.24, compute_efficiency ≈ 0.76–0.97).** Attempts 4, 8, 11, 13, 16, and (with a conformance failure) 17. This class drove the per-step cost ratio down toward and below 1.0 and pushed compute_efficiency as high as 0.9679. It did not pay: attempt 8 achieved the best efficiency ever measured (0.9679, ratio 0.9674) and returned 0.5444, among the lowest clean rewards, on the longest wall clock recorded (26.10 s). Attempt 4 achieved efficiency 0.8832 at 17.51 s — essentially the same wall clock as attempt 2's 17.45 s — and returned 0.5792 against attempt 2's 0.7155. The single exception is attempt 11 (ratio 1.0166, efficiency 0.8424, 20.06 s, reward 0.6639), which is respectable but still below the Class A leaders; it is the one datum that keeps this class from being fully dismissed.

**Class C — variants that broke the module API surface.** Attempts 9, 17 and 20 all tripped C-API-SURFACE. They span both other classes by fingerprint (9 and 20 are Class A-shaped, ratio 1.4988 and 1.5804; 17 is Class B-shaped, ratio 1.2123), which tells us the surface violation is orthogonal to the algorithmic idea being tested.

**Class D — the variant that lost a held-out perturbation.** Attempt 12 alone, Class A-shaped by fingerprint (ratio 1.4886, 16.78 s), but the held-out-variant perturbation neither reached its target nor respected its budget.

# 3. Checks that failed

**C-API-SURFACE — failed three times**, in attempts 9, 17 and 20, with the identical verifier reason every time: *"module-level statements outside imports, constants, and permitted definitions."* In all three the primary target was still reached (`primary_target_reached: 1.0`) and both perturbation units held, yet `task_pass` was forced to 0.0 and `rule_conformance` fell from 1.0 to 0.8571428571428571, costing roughly 0.15–0.20 of reward relative to comparable clean attempts (0.5164, 0.5274, 0.5107 versus a Class A norm above 0.63). These three attempts differed from each other in algorithmic fingerprint — 9 and 20 ran high per-step cost, 17 ran cheapened steps — so **whatever was changed between them is not what causes this failure.** The cause is structural and fixed: the submitted module executes statements at import time that are neither imports, nor constant assignments, nor permitted `def`/`class` definitions. Nothing short of moving all such code inside a function or class body will clear it.

**C-PERTURBATION-REACHED — failed once**, in attempt 12: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This dropped `conformance_fraction` to 0.5, set `all_perturbations_held` to false, forced `task_pass` to 0.0, and produced the lowest reward on record, 0.4962. Note that `rule_conformance` stayed at 1.0 here — this is a distinct failure mode from C-API-SURFACE and the two have never co-occurred.

**C-TARGET-REACHED and C-BUDGET-RESPECTED** — failed once each, inside the failing perturbation unit of attempt 12 (see section on perturbation outcomes below).

No other check has ever failed. In every other measured record `failed_checks` is empty, `conformance_fraction` is 1.0 and `rule_conformance` is 1.0.

**Perturbation outcomes by kind.** Each measured attempt declared 2.0 perturbations and reported two held-out units: one of kind `held_out_variant` and one of kind `ruleset`. Across the 22 measured attempts that is 44 units, of which 43 reached their threshold. In aggregate, `all_perturbations_held` is true in 21 of 22 measured attempts.

- Kind `ruleset`: 22 of 22 reached. This kind has never failed a check.
- Kind `held_out_variant`: 21 of 22 reached. The single failure is in attempt 12, where the held-out-variant unit reported `reached: false` and failed **two** checks, **C-TARGET-REACHED** and **C-BUDGET-RESPECTED** — it neither hit its own threshold nor stayed inside its own budget. So the only fragility ever observed under perturbation is on held-out-variant runs, and it manifests as a simultaneous target-and-budget miss.

Attempts 6 and 7 report an empty `perturbation_units` list and `perturbations_declared: not-measured` — the harness never got as far as running perturbations, which is consistent with a harbor exception and carries no information about robustness.

# 4. Ruled-out directions

**Maximising compute efficiency / minimising per-step cost.** Ruled out as a route to higher reward. The evidence is direct and repeated: attempt 8 pushed `compute_efficiency` to 0.9679 and `per_step_cost_ratio` to 0.9674 — the best efficiency figures in the entire record — and scored 0.5444, roughly 0.19 below the best. Attempt 16 (efficiency 0.8684, ratio 1.1256) scored 0.5701. Attempt 13 (0.7642, 1.2404) scored 0.5590. Attempt 4 (0.8832, 1.1656) scored 0.5792. Meanwhile the best result, attempt 21, has efficiency of only 0.6162 and a per-step cost ratio of 1.5700. The reward is clearly not paying for cheap steps; cutting per-step work appears to cost whatever quality term drives the score. (Qualifier: attempt 11 at ratio 1.0166 reached 0.6639, so a low ratio is not automatically fatal — but no low-ratio attempt has come within 0.06 of the best.)

**Extending total run time.** Ruled out. Within the strong Class A fingerprint the ordering by wall clock is nearly monotone in reward: 14.39 s → 0.7322, ~17.4 s → 0.7155/0.7134/0.6694, ~20 s → 0.6877/0.6833/0.6587/0.6279/0.5983/0.5755, 23.70 s → 0.5830. Attempt 8's 26.10 s is the longest run and one of the weakest clean rewards. Longer budgets have never bought back reward.

**Leaving module-level executable code in the submission.** Ruled out by three separate C-API-SURFACE failures with an identical verifier reason. Each such attempt zeroed `task_pass` and forfeited about 0.15 of `rule_conformance`, capping the reward near 0.51–0.53 regardless of how good the underlying algorithm was. Any design that requires setup work to run at import time is not viable under this harness.

**Re-running Class A unchanged and hoping for a better draw.** Attempts 22, 23 and 24 all sit in the Class A fingerprint (ratios 1.5983, 1.5949, 1.5539; wall clocks 17.37, 20.11, 19.98 s) and all three landed below both attempt 2 and attempt 21. Simply reoccupying the class without shortening the run has now been shown three consecutive times not to recover the top score.

Nothing is ruled out on the basis of attempts 6 and 7, which produced no measurement.

# 5. Open leads

**Lead 1 — reproduce the attempt-21 operating point exactly, then shorten further.** Attempt 21 is the only run under 15 seconds, and it holds the record. Its fingerprint is: `per_step_cost_ratio` 1.5700 (rich per-step compute retained), `compute_efficiency` 0.6162, `wall_clock_sec` 14.39, `task_pass` 1.0, both perturbations held. The single strongest signal in the whole record is that, holding the per-step cost ratio in the 1.50–1.63 band, reward rises as total wall clock falls. The next attempt should keep the expensive per-step computation intact and cut the number of steps / total iterations until wall clock lands near or below 14.4 s, while confirming `primary_target_reached` stays at 1.0 and both perturbation units still report `reached: true`. Cutting steps is the lever; cutting per-step work is not (section 4).

**Lead 2 — probe below 14 s, but watch the held-out-variant unit.** Shortening the run is the only demonstrated path upward, but attempt 12 shows the failure mode that lies at the end of it: at 16.78 s the held-out-variant perturbation missed both C-TARGET-REACHED and C-BUDGET-RESPECTED, costing `task_pass` and dropping the reward to 0.4962, the worst on record. Note that attempt 21 ran *shorter* than attempt 12 and held both perturbations, so wall clock alone did not cause attempt 12's miss — but the held-out-variant unit is the one place robustness has ever broken, and any aggressive shortening should preserve whatever convergence guarantee lets that unit hit its target inside its own budget (e.g. keep an adaptive stopping rule keyed to the target rather than a hard step count).

**Lead 3 — audit the module top level before submitting, unconditionally.** C-API-SURFACE has now cost three attempts an automatic `task_pass: 0.0`. Because the next attempt starts from a pristine stub, the discipline must be re-imposed from scratch: at module scope permit only `import` statements, constant assignments, and `def`/`class` definitions. No calls, no loops, no conditionals, no `if __name__ == "__main__"` block, no logging or seeding or device-selection statements, no decorator that executes work at definition time — every such statement belongs inside the entry-point function. This is worth an estimated 0.15–0.20 of reward on any attempt that would otherwise trip it.

**Lead 4 — resolve the attempt-11 anomaly only if leads 1–3 stall.** Attempt 11 reached 0.6639 with a per-step cost ratio of 1.0166 and efficiency 0.8424, far off the Class B trend line that otherwise tops out around 0.58. If the short-run Class A path stops improving, it is worth identifying what attempt 11 did differently from attempts 4, 8, 13 and 16, since it is the one piece of evidence that cheap per-step work can be made to score. It is not the first thing to try: it is still 0.068 behind the best.

**Lead 5 — treat sub-0.05 reward differences as noise.** Attempts 1 and 2 differ by 0.046 on essentially identical measured fingerprints. Any experiment intended to decide between two configurations should aim for a change larger than that, or its result will not be interpretable.

**Call: exploit.** The best result, 0.7322 at attempt 21, is recent, and it sits at an operating point — high per-step cost ratio, shortest wall clock ever measured — that no other attempt has occupied. The improvement axis is identified and unexhausted: shorten total run time while holding per-step compute rich and keeping both perturbation units reaching their thresholds, with a mandatory module-top-level audit to avoid the C-API-SURFACE forfeit. Exploring a structurally new approach is not warranted while the leading class has an untested direction directly ahead of it. What must *not* be repeated is re-submitting a Class A variant at ~17–21 s with no change to the step budget: attempts 22, 23 and 24 each did essentially that and each landed below the record.
