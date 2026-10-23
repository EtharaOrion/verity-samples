# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 2 -- reward 0.7155, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All nine attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2 *      0.7155   1.000             2 of 2         yes             17                
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
  8 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.6639, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 12 -- reward 0.4962, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 13 -- reward 0.5590, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 9.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Thirteen submissions were graded. Eleven produced a measurement; two did not.

Ordered worst to best by `reward`:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 12 | 0.4962 | failed `C-PERTURBATION-REACHED`; `task_pass` 0.0 |
| 2 | 9 | 0.5164 | failed `C-API-SURFACE`; `task_pass` 0.0; `rule_conformance` 0.8571 |
| 3 | 8 | 0.5444 | clean; highest `compute_efficiency` recorded (0.9679), longest wall clock (26.10 s) |
| 4 | 13 | 0.5590 | clean |
| 5 | 4 | 0.5792 | clean |
| 6 | 10 | 0.5983 | clean |
| 7 | 3 | 0.6279 | clean |
| 8 | 5 | 0.6587 | clean |
| 9 | 11 | 0.6639 | clean |
| 10 | 1 | 0.6694 | clean; first measured attempt |
| 11 (best) | **2** | **0.7155** | clean; `standing_against_best_so_far` = better_than_every_earlier_attempt |

**Attempt 2, at reward 0.7155, holds the highest reward and is the one to beat.** It is also the only attempt whose standing was recorded as better than every earlier attempt; every measured attempt after it — 3, 4, 5, 8, 9, 10, 11, 12, 13 — carries `standing_against_best_so_far` = *worse_than_an_earlier_attempt*. That is a regression, not progress, and eleven graded submissions have produced exactly one improvement, which came at attempt 2.

**Attempts 6 and 7 produced no measurement at all.** Both carry `measurement_status` = `harbor_exception`, with every term reported as "not-measured" and no perturbation units recorded. They did not score zero; they were never scored. Nothing about the merit of the code in those attempts can be read out of their absent terms — including whether their `failed_checks` list is genuinely empty or simply never populated.

Supporting terms across the eleven measured attempts, for calibration:
- `validity` = 1.0 and `red_line_crossed` = 0.0 in all eleven. No submission has ever tripped a red line or been ruled invalid.
- `primary_target_reached` = 1.0 in all eleven, including attempts 9 and 12 whose `task_pass` was 0.0. The primary run always hits its target; failures come from conformance and from the held-out runs, never from the primary objective.
- `task_pass` = 1.0 in nine of eleven; 0.0 only in 9 and 12, the two attempts carrying failed checks.
- `wall_clock_sec` equals `qualifying_budget` in every measured record (range 16.78 s to 26.10 s).
- `compute_efficiency` ranges 0.5488 to 0.9679; `per_step_cost_ratio` ranges 0.9674 to 1.6262.

A relationship worth stating because it is measured and counter-intuitive: **higher `compute_efficiency` has gone with lower reward, not higher.** The best attempt (2) had efficiency 0.6205 and cost ratio 1.5175. The three attempts with the highest efficiency — 8 (0.9679), 4 (0.8832), 11 (0.8424) — scored 0.5444, 0.5792 and 0.6639, all below attempt 2. The worst clean attempt on reward, 8, is the one with the best efficiency and the lowest per-step cost ratio (0.9674). Attempt 11 is the partial exception: efficiency 0.8424 with reward 0.6639, close to the top. The terms do not disclose why, so this is reported as an observed correlation, not a mechanism.

The two shortest wall clocks (12 at 16.78 s, 9 at 17.12 s) are the two failed attempts, and the longest (8 at 26.10 s) is the worst clean one. The top four rewards (2, 1, 11, 5) sit at 17.45, 17.43, 20.06 and 20.53 seconds — the middle of the observed range.

## 2. Approach classes tried

The measured terms carry no description of the source code, so the approach classes below are grouped by their metric signatures, which is what the record actually supports. The next attempt should treat these as families to re-enter or avoid, not as verbatim recipes.

**Class A — moderate-cost, ~17.4 s, cost ratio ~1.51–1.52, efficiency ~0.55–0.62.** Attempts 1 (0.6694) and 2 (0.7155). This family contains both the best result and the second-best-but-one, and is the highest-scoring class on the record. Between 1 and 2 the metric signature barely moved (efficiency 0.5488→0.6205, ratio 1.5134→1.5175, wall 17.426→17.453 s) yet reward rose by 0.046. Whatever changed between those two was small in cost terms and materially positive in reward terms.

**Class B — same cost ratio (~1.5), stretched to ~20.2–20.5 s.** Attempts 3 (0.6279), 5 (0.6587), 10 (0.5983). Efficiency 0.60, 0.61, 0.57; ratios 1.523, 1.626, 1.515. Consistently below Class A despite near-identical per-step cost. Spending the extra ~3 seconds did not buy reward.

**Class C — efficiency-optimised, cost ratio driven toward or below 1.0.** Attempts 4 (0.5792, ratio 1.166, 17.51 s), 11 (0.6639, ratio 1.017, 20.06 s), 13 (0.5590, ratio 1.240, 20.60 s), 8 (0.5444, ratio 0.967, 26.10 s). This class produced the largest efficiency numbers on the record and, with the exception of 11, the poorest clean rewards. Attempt 8 pushed cost ratio below 1.0 and paid for it with the longest wall clock and the worst clean reward.

**Class D — an attempt that broke the module API surface.** Attempt 9 (0.5164). Efficiency 0.6647, ratio 1.4988, wall 17.12 s — a Class A cost signature — but it failed `C-API-SURFACE`, dropping `rule_conformance` to 0.8571 and `task_pass` to 0.0. The cost profile was competitive; the file layout was not.

**Class E — an attempt that lost a held-out run.** Attempt 12 (0.4962). Ratio 1.4886, wall 16.78 s, the shortest on record. Its held-out variant run failed both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, taking `conformance_fraction` to 0.5, `all_perturbations_held` to false and `task_pass` to 0.0, even though the primary run reached its target.

**Class F — two submissions that never reached measurement.** Attempts 6 and 7, both `harbor_exception`. No approach content can be recovered from their terms.

## 3. Checks that failed

Two named checks failed at the submission level, and two more at the level of an individual held-out run. Each has failed exactly once.

- **`C-API-SURFACE`** — attempt 9. Verifier's reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions."* This is the only failure of this check on the record. It set `rule_conformance` to 0.8571 and `task_pass` to 0.0 while the primary target was still reached and both perturbation units still held. The submission file must contain only imports, constants, and permitted definitions at module scope — no top-level executable statements, no module-level demo/driver/print/seed calls, no top-level `if` blocks doing work. Wrap anything executable inside a function or guard it out of module scope entirely.

- **`C-PERTURBATION-REACHED`** — attempt 12. Verifier's reason, verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* One of the two declared perturbations fell short. This drove `conformance_fraction` to 0.5, `all_perturbations_held` to false, `task_pass` to 0.0, and the record's lowest reward.

- **`C-TARGET-REACHED`** and **`C-BUDGET-RESPECTED`** — both recorded against the same held-out run inside attempt 12 (see section on perturbation runs below). No per-run reason string was supplied for either; only the check identifiers. Together they say the run neither hit its threshold nor stayed inside its own budget.

No check has failed more than once, so there is no repeated finding to isolate. Correspondingly, there is no evidence that any change made between attempts is or is not the cause of a recurring failure — the two failures are single, distinct events in attempts 9 and 12, and every other measured attempt held every check with `conformance_fraction` = 1.0.

### Perturbation runs

Each measured attempt declared 2 perturbation units, one of kind `held_out_variant` and one of kind `ruleset`. Across the eleven measured attempts that is 22 held-out runs. Attempts 6 and 7 recorded no perturbation units at all, consistent with never being measured.

By kind:
- **`ruleset`: 11 of 11 reached their threshold.** This kind has never failed a check on any attempt.
- **`held_out_variant`: 10 of 11 reached their threshold.** The single failure occurred in attempt 12, where a run of this kind did not reach, and was stopped by `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.

In aggregate, 21 of 22 perturbation runs reached, and the sole failure is of kind `held_out_variant`. The runs are not identified individually in the record, so nothing links a particular run in one attempt to a particular run in another; the only safe statement is by kind. **The kind that is fragile is `held_out_variant`, and the checks it fails on are `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.** The `ruleset` kind has shown no fragility whatsoever.

## 4. Ruled-out directions

- **Pushing `compute_efficiency` upward as the route to reward.** Ruled out by four measurements. Attempt 8 reached the highest efficiency on record (0.9679) and the lowest per-step cost ratio (0.9674) and scored 0.5444, the worst clean reward. Attempt 4 (0.8832) scored 0.5792. Attempt 13 (0.7642) scored 0.5590. All three sit below attempt 2's 0.7155, which was achieved at efficiency 0.6205. The reward is not monotone in efficiency and this direction has been walked three separate ways with three regressions.

- **Driving `per_step_cost_ratio` to or below 1.0.** Ruled out with the same evidence. The two attempts closest to or below 1.0 — 8 at 0.9674 and 11 at 1.0166 — scored 0.5444 and 0.6639, both worse than attempt 2 at ratio 1.5175. Attempt 8, the only submission ever to get the ratio under 1.0, is the worst clean result. Cheapening the per-step work has not paid.

- **Extending the wall clock past ~20.5 s.** Ruled out. `wall_clock_sec` equals `qualifying_budget` in every record, so extra time is charged directly. Attempt 8 at 26.10 s produced the worst clean reward. The 20.1–20.6 s band (attempts 3, 10, 11, 13) averages below the 17.4 s band (attempts 1, 2). No attempt above 20.6 s has ever scored well.

- **Anything placing executable code at module scope.** Ruled out by `C-API-SURFACE` in attempt 9: *"module-level statements outside imports, constants, and permitted definitions."* Attempt 9 had a competitive cost profile (ratio 1.4988, 17.12 s, both perturbations held) and still lost `task_pass` entirely to this one structural rule. There is no reward to be recovered from module-level work.

- **Trimming the budget below ~17 s.** Ruled out on the current evidence. The two shortest runs on record, attempt 12 at 16.78 s and attempt 9 at 17.12 s, are the two attempts with failed checks, and attempt 12's held-out variant specifically failed `C-BUDGET-RESPECTED` alongside `C-TARGET-REACHED`. Compression that leaves the held-out variant unable to reach its threshold inside its own budget costs far more than it saves.

- **Re-submitting anything with the shape of attempts 6 or 7.** Cannot be ruled in or out on merit — they produced no measurement — but they cannot be counted as evidence for anything either, and they should not be treated as failures of the algorithm. Two of thirteen graded submissions returned nothing measurable, so the possibility of a `harbor_exception` on any given submission is real; the code should be kept structurally simple and self-contained to reduce exposure to it.

## 5. Open leads

- **Rebuild the Class A signature and hold it.** Attempt 2's profile is: wall clock ≈ 17.45 s, `per_step_cost_ratio` ≈ 1.52, `compute_efficiency` ≈ 0.62, both perturbations held, `conformance_fraction` = 1.0. Attempt 1 sits within a hair of this on every cost term (17.43 s, 1.5134, 0.5488) and scored 0.6694. The gap of 0.046 between them was bought with almost no change in cost, which means there is a quality dimension the cost terms do not capture and which moved favourably between attempt 1 and attempt 2. Target that dimension — better per-step learning quality at unchanged cost — rather than the cost terms themselves.

- **Explore the region between Class A and attempt 11.** Attempt 11 (ratio 1.0166, efficiency 0.8424, 20.06 s, reward 0.6639) is the one efficiency-oriented result that stayed near the top. It is the only measured evidence that a low cost ratio need not collapse reward. A configuration at attempt 2's ~17.4 s wall clock with attempt 11's cheaper per-step work is a point on the grid that has never been measured, and both of its parents scored above 0.66.

- **Guard the `held_out_variant` run explicitly.** It is the only kind that has ever failed, and it failed on both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` simultaneously in attempt 12. Whatever schedule, step count or early-stopping rule the algorithm uses must be robust when the variant's data or task shifts, and must leave headroom inside the variant's own budget rather than the primary's. Do not tune the primary run so close to the wire that the variant run inherits an infeasible schedule; attempt 12 reached its primary target and still lost `task_pass` outright.

- **Audit module scope before submitting.** A single mechanical pass over the file — every top-level statement is an import, a constant assignment, a `def`, or a `class`, and nothing else — would have saved attempt 9's 0.5164 from being a `task_pass` = 0.0 result. This is a cheap, deterministic check with a known verifier reason string to check against.

- **Keep the submission structurally plain.** Two submissions returned `harbor_exception` and no measurement. An unmeasured attempt yields no information at all, so minimising anything exotic in imports or file structure has option value independent of reward.

- **Do not repeat the efficiency-maximising family.** Attempts 4, 8 and 13 are three separate walks down that road, each returning a regression against attempt 2 (0.5792, 0.5444, 0.5590). Re-entering it without changing the reason it scored low — a per-step cost ratio at or below ~1.2 coinciding with lower reward — would be repeating a known regression rather than exploring or exploiting.

**Call: exploit.** Attempt 2 at reward 0.7155 is the target, and the cheapest path to beating it is to reconstruct its cost signature (≈17.4 s wall clock, per-step cost ratio ≈1.5, efficiency ≈0.62, both perturbations held, no module-level statements) and then vary only the per-step learning quality, which is the axis on which attempt 1 → attempt 2 gained 0.046 at essentially unchanged cost. The scoring approaches have not stopped improving so much as never been pushed on the right axis: nine of the last nine measured attempts moved cost terms and every one of them regressed. Exploit the Class A configuration, fix the two known conformance hazards (module scope, held-out variant budget headroom), and leave the efficiency dial alone.
