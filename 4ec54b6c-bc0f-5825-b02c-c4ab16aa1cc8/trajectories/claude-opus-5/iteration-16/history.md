# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 16 -- reward 0.8841, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 3
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.0000   1.000             0 of 2         no              --                
  2        0.8037   1.000             2 of 2         yes             13                
  3        0.8042   1.000             2 of 2         yes             14                
  4        0.8042   1.000             2 of 2         yes             14                
  5        0.8255   1.000             2 of 2         yes             14                
  6        0.8059   1.000             2 of 2         yes             13                
  7        0.7994   1.000             2 of 2         yes             14                
  8        0.7843   1.000             2 of 2         yes             17                
  9        0.7891   1.000             2 of 2         yes             14                
  10       0.7393   1.000             2 of 2         yes             17                
  11       0.7997   1.000             2 of 2         yes             17                
  12       0.7443   1.000             2 of 2         yes             17                
  13       0.0000   1.000             2 of 2         yes             37                
  14       0.8820   1.000             2 of 2         yes             7                 
  15       0.7288   0.857             2 of 2         yes             5                 
  16 *     0.8841   1.000             2 of 2         yes             3                 

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
  12 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 5 -- reward 0.8255, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 14 -- reward 0.8820, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 7
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 15 -- reward 0.7288, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 5
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-NO-SHAPE-FINGERPRINT -- the submission fingerprints the model by shape

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (1, 13). Whatever has been
      changing between them is not what is causing it.
    C-NO-SHAPE-FINGERPRINT failed on attempt 15.
    C-PER-STEP-COST-CEILING failed on attempt 13.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Sixteen graded records, every one of them carrying `measurement_status` of `measured` or `measured_phase_cut`, so every one carries a reward. Listed worst to best:

| Rank | Attempt | Reward | Notes from the measured terms |
|---|---|---|---|
| 1 (worst) | 1 | 0.0000 | `zero_reason_code` 4; `task_pass` 0, `primary_target_reached` 0, `conformance_fraction` 0.0; `measured_phase_cut`; wall clock 89.978 s; `qualifying_budget` "not-measured" |
| 2 | 13 | 0.0000 | `zero_reason_code` 1; `red_line_crossed` 1, `validity` 0, `task_pass` 0; wall clock 37.202 s; `per_step_cost_ratio` 7.185 |
| 3 | 15 | 0.7288 | `task_pass` 0 and `rule_conformance` 0.857 despite target reached and wall clock 4.681 s |
| 4 | 10 | 0.7393 | wall clock 16.899 s |
| 5 | 12 | 0.7443 | wall clock 16.943 s |
| 6 | 8 | 0.7843 | wall clock 16.507 s |
| 7 | 9 | 0.7891 | wall clock 14.160 s; `compute_efficiency` 1.000 |
| 8 | 7 | 0.7994 | wall clock 14.103 s |
| 9 | 11 | 0.7997 | wall clock 17.003 s |
| 10 | 2 | 0.8037 | wall clock 13.488 s; first clean run |
| 11 | 4 | 0.8042 | raw 0.8041887; wall clock 13.658 s |
| 12 | 3 | 0.8042 | raw 0.8042363; wall clock 13.662 s |
| 13 | 6 | 0.8059 | wall clock 13.427 s; `per_step_cost_ratio` 0.971, `compute_efficiency` 0.946 |
| 14 | 5 | 0.8255 | wall clock 13.740 s |
| 15 | 14 | 0.8820 | wall clock 6.628 s; `compute_efficiency` 0.503 |
| 16 (best) | 16 | 0.8841 | wall clock 3.337 s; `per_step_cost_ratio` 1.706, `compute_efficiency` 0.846 |

**Attempt 16 holds the highest reward, 0.8841, and it is the one to beat.** Attempt 14 (0.8820) is the only other record within 0.01 of it.

Direction of movement, stated plainly rather than softened: attempts 4, 6, 7, 8, 9, 10, 11, 12, 13 and 15 each carry `standing_against_best_so_far` of `worse_than_an_earlier_attempt` — ten regressions. Attempt 13 regressed all the way to 0.0000 from a standing best of 0.8255, and attempt 15 regressed to 0.7288 from a standing best of 0.8820. Only attempts 2, 3, 5, 14 and 16 improved on everything before them.

The single strongest signal across the clean records is that reward tracks `qualifying_budget` / `wall_clock_sec` downward: the two fastest valid runs (3.337 s and 6.628 s) are the two highest rewards, and every run in the 13.4–17.0 s band scored between 0.7393 and 0.8255. But the relationship is not tight, and this matters for interpreting small deltas: attempt 6 at 13.427 s scored 0.8059 while attempt 5 at 13.740 s scored 0.8255, and attempt 10 at 16.899 s scored 0.7393 while attempt 11 at 17.003 s scored 0.7997. So roughly ±0.06 of reward exists at fixed wall clock. Attempts 3 and 4 differ by 0.00005. Treat any single comparison under ~0.02 as not decisive; only large moves in wall clock have reliably moved the reward.

`compute_efficiency` and `per_step_cost_ratio` do **not** drive the reward. Attempt 9 posted `compute_efficiency` 1.000 and scored 0.7891; attempt 14 posted 0.503 and scored 0.8820. Attempt 6 posted the only sub-1.0 `per_step_cost_ratio` (0.971) and scored 0.8059, below attempt 16's 1.706 at 0.8841. `per_step_cost_ratio` appears to matter only as a hard ceiling (see section 3), not as a graded quantity.

# 2. Approach classes tried

I have measured terms only, not the source of any attempt, so these classes are grouped by their measured signature. Records with the same signature are one entry.

**Class A — non-converging first cut (attempt 1).** The run never produced a qualifying evaluation row: `primary_target_reached` 0, `conformance_fraction` 0.0, wall clock 89.978 s, `qualifying_budget` "not-measured", `measured_phase_cut`. Both held-out runs also failed to reach. `per_step_cost_ratio` was 1.019 and `compute_efficiency` 1.000, so the per-step work was cheap — the failure was that the training loop did not reach the target at all in the declared direction, not that each step was expensive. Reward 0.0000.

**Class B — converged, mid-band plateau (attempts 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12).** Eleven records, all fully clean: no `failed_checks`, `conformance_fraction` 1.0, `rule_conformance` 1.0, `validity` 1.0, `task_pass` 1.0, `red_line_crossed` 0, both perturbation runs reached. Qualifying budgets 13.427–17.003 s, `per_step_cost_ratio` 0.971–1.596, `compute_efficiency` 0.558–1.000. Rewards 0.7393–0.8255. This class was worked over eleven times and its ceiling was 0.8255 (attempt 5). Within the class, the variations tried spanned the per-step cost ratio from 0.971 to 1.596 and compute efficiency from 0.558 to 1.000 without ever breaking 0.83 — the class is saturated.

**Class C — expensive-per-step variant (attempt 13).** `per_step_cost_ratio` 7.185, wall clock 37.202 s. It still reached the primary target and both perturbation runs still held, but it crossed the red line: `validity` 0, `task_pass` 0, `zero_reason_code` 1, reward 0.0000. Whatever this attempt did per step (heavier optimizer state, larger batch or model, or extra passes) bought target attainment at 7.19× the seed anchor's per-step cost and 2.7× the previous class's wall clock, and both were fatal.

**Class D — fast-converging (attempts 14 and 16).** Qualifying budgets 6.628 s and 3.337 s, `per_step_cost_ratio` 1.869 and 1.706, `compute_efficiency` 0.503 and 0.846. Fully clean on every check, both perturbation runs reached in both. Rewards 0.8820 and 0.8841. This is the winning class: it accepts a per-step cost roughly 1.7–1.9× the seed anchor — comfortably inside the 3.0 ceiling — in exchange for far fewer wall-clock seconds to the qualifying row. Attempt 16 nearly halved attempt 14's time and gained only 0.0021 of reward, which suggests the time term is flattening near 3 s or that the residual scatter noted in section 1 is absorbing the gain.

**Class E — fast but shape-fingerprinting (attempt 15).** Wall clock 4.681 s, `per_step_cost_ratio` 1.873, `compute_efficiency` 0.871 — i.e. squarely in the class D speed regime, between attempts 16 and 14 on time — but it failed `C-NO-SHAPE-FINGERPRINT`. `rule_conformance` dropped to 0.857 and `task_pass` to 0, and the reward fell to 0.7288: worse than every class B record except attempts 10 and 12. Note carefully that `conformance_fraction` stayed 1.0, `validity` stayed 1.0, `red_line_crossed` stayed 0 and `zero_reason_code` stayed 0 — a conformance failure of this kind is a large graded penalty, not a zeroing event. The lesson is that speed obtained by branching on model shape is worth roughly −0.155 of reward against the same speed obtained legitimately.

# 3. Checks that failed

Four distinct check identifiers have failed across the sixteen records, plus two more that appear only inside held-out runs.

**`C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction."** Failed in attempt 1's primary run, and separately in both of attempt 1's held-out runs. Three occurrences, all confined to attempt 1. No record since has failed it; `primary_target_reached` has been 1.0 in every record from attempt 2 onward, including the two that scored 0.0000 for other reasons.

**`C-BUDGET-RESPECTED` — failed twice at the primary level, in attempts 1 and 13, and once in each of attempt 1's two held-out runs.** The verifier's reasons differ between the two primary occurrences and both must be carried forward. In attempt 1: "no qualifying row, so no budget position exists" — i.e. it is a downstream consequence of `C-TARGET-REACHED`, not an independent overrun. In attempt 13: "the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1." **This gives the hard number the next attempt needs: the budget axis is `wall_clock_sec` and the declared ceiling is 31.1 s.** Every clean record sits between 3.337 s and 17.003 s, comfortably under it. This check has now failed in two separate attempts twelve ordinals apart, so the changes made across the intervening attempts 2–12 are not what governs it; what governs it is whether a qualifying row exists at all and, if it does, whether it lands under 31.1 s on the wall-clock axis.

**`C-PER-STEP-COST-CEILING` — "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0."** One occurrence, attempt 13. **The ceiling is 3.0× the seed anchor's per-step cost.** Every other record ran between 0.971× and 1.873×, so there is real headroom here that has never been spent: a step up to roughly 2.5× is permitted and has never been tried in combination with the class D short-schedule structure.

**`C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget."** One occurrence, attempt 1. `perturbations_declared` has been 2.0 in every record.

**`C-NO-SHAPE-FINGERPRINT` — "the submission fingerprints the model by shape."** One occurrence, attempt 15. It cost `task_pass` (1 → 0) and `rule_conformance` (1.0 → 0.857) and dropped the reward to 0.7288 from a standing best of 0.8820. This is the only check ever failed by an otherwise-converging, in-budget, fast submission, and it is the cheapest failure to avoid: do not branch on, dispatch on, hash, or key any behaviour off the parameter shapes, layer dimensions, or tensor sizes of the model.

**`C-LOG-WELL-FORMED` and `C-NO-LATCH-CARRYOVER`** appear only inside attempt 1's held-out runs, never at the primary level, and only there. See section 4's perturbation aggregate below.

**Perturbation-unit outcomes.** Every record declared two held-out runs beside the primary one, one of kind `ruleset` and one of kind `held_out_variant`. Across the sixteen records that is 32 held-out runs; 30 reached their threshold and 2 did not, and both failures are in attempt 1 — one of each kind.

- By kind, `ruleset`: 16 runs, 15 reached, 1 failed. The failing `ruleset` run was stopped by four checks: `C-LOG-WELL-FORMED`, `C-TARGET-REACHED`, `C-BUDGET-RESPECTED`, and `C-NO-LATCH-CARRYOVER`. The latter two identifiers are unique to a `ruleset` run and have never appeared anywhere else in the record set, so a `ruleset` run exercises log formatting and latched-state clearing that the primary run does not. If a future attempt keeps mutable state across runs or emits logs the ruleset harness cannot parse, this is where it will show.
- By kind, `held_out_variant`: 16 runs, 15 reached, 1 failed, stopped by `C-TARGET-REACHED` and `C-BUDGET-RESPECTED` — the same generalisation failure the primary run had in that record, with no additional failure mode of its own.
- In aggregate: `all_perturbations_held` is true in fifteen of sixteen records, including both zero-reward records (13 crossed the red line with both perturbations holding). Generalisation to held-out runs has been solved since attempt 2 and has not been the binding constraint at any point after that.

I was given no name, number or position for any individual held-out run and cannot say that any particular run in one record is the same run as in another.

# 4. Ruled-out directions

**Direction: the class B mid-band configuration (attempts 2–12).** Ruled out as a route to a new best. Eleven measured records in a 13.4–17.0 s qualifying band produced a ceiling of 0.8255 and a mean well below it, while two records in the 3–7 s band produced 0.8820 and 0.8841. Continued tuning inside the mid-band is spending measurements on a saturated class.

**Direction: minimising `per_step_cost_ratio` or maximising `compute_efficiency` as the objective.** Ruled out by direct counter-evidence. Attempt 6 achieved `per_step_cost_ratio` 0.971 — the only value below 1.0 recorded — and scored 0.8059. Attempt 9 achieved `compute_efficiency` 1.000 and scored 0.7891. Both are beaten by attempt 14 at `compute_efficiency` 0.503 and by attempt 16 at `per_step_cost_ratio` 1.706. These two quantities function as constraints, not as reward terms; optimising them directly trades away the thing that does pay, which is time to the qualifying row.

**Direction: heavy per-step compute to reach the target (class C, attempt 13).** Ruled out by the two named ceilings it broke: `per_step_cost_ratio` 7.185 against a 3.0 ceiling, and 37.202 s against a 31.1 s wall-clock ceiling. It crossed the red line and scored 0.0000 despite reaching the target and holding both perturbations. Anything that pushes per-step cost past 3.0× the seed anchor is a guaranteed zero regardless of how well it trains.

**Direction: shape-based fingerprinting or dispatch (class E, attempt 15).** Ruled out by `C-NO-SHAPE-FINGERPRINT`. It reached the target in 4.681 s, faster than the 6.628 s of attempt 14, and still scored 0.7288 against attempt 14's 0.8820. Speed bought this way is a net loss of about 0.155 reward. Do not inspect or condition on parameter shapes.

**Direction: any configuration that does not produce a qualifying evaluation row (class A, attempt 1).** Ruled out: it cascades into `C-TARGET-REACHED`, `C-BUDGET-RESPECTED` and `C-PERTURBATION-REACHED` simultaneously and scores 0.0000 with `zero_reason_code` 4. Reaching the threshold in the declared direction is the precondition for everything else; note that attempt 1's `per_step_cost_ratio` of 1.019 shows the run was cheap per step and still failed, so cheapness is no defence.

**Direction: reading small reward differences as signal.** Ruled out as a basis for decisions. Attempts 3 and 4 differ by 0.00005 with opposite `standing_against_best_so_far` labels, and equal-wall-clock pairs differ by up to 0.06. Do not chase deltas below roughly 0.02.

# 5. Open leads

**Lead 1 — push the qualifying wall clock below attempt 16's 3.337 s.** This is the one lever with demonstrated, repeated effect: 17.0 s → 0.7997, 13.4 s → 0.8059, 6.63 s → 0.8820, 3.34 s → 0.8841. Caveat that must be carried: the 6.63 → 3.34 s halving bought only 0.0021, which is inside the observed scatter, so the time term may be flattening near 3 s. Worth one probe at a materially shorter time (say under 2 s) to find out whether the curve is flat or still climbing; if it is flat, further speed work is done and the residual 0.116 to a perfect score lies elsewhere.

**Lead 2 — spend the unused per-step cost headroom to shorten the schedule.** The ceiling is 3.0× the seed anchor and the best two records sit at 1.706× and 1.869×. Nothing has ever been measured between 1.9× and 7.2×. A configuration at roughly 2.2–2.6× per step — larger batch, stronger optimizer, higher learning rate with warmup, fused or higher-precision-throughput ops — that cuts the step count enough to land under 3 s of wall clock stays legal on `C-PER-STEP-COST-CEILING` and directly serves Lead 1. This is the most concrete untried point in the space.

**Lead 3 — recover class E's speed legitimately.** Attempt 15 reached the target in 4.681 s while fingerprinting by shape. Whatever adaptation it was making from shape almost certainly has a shape-independent equivalent: derive the same decision from runtime signals available without inspecting the model's dimensions — loss trajectory, gradient norm, step timing, elapsed wall clock, iteration count. If that adaptation is what made it fast, reimplementing it shape-blind should give class D speed with `rule_conformance` back at 1.0.

**Lead 4 — investigate the residual scatter at fixed time.** Roughly 0.06 of reward separates records at near-identical wall clock (attempt 5 at 13.740 s scored 0.8255; attempt 6 at 13.427 s scored 0.8059). That residual is either genuine run-to-run variance or a second graded term the class B sweep moved by accident. If it is a term, it is worth as much as a 3-second time cut. Cheap probe: hold the class D structure fixed and vary only the seed or only the final-model quality margin above threshold, and see whether the reward moves.

**Lead 5 — protect the invariants that are currently free.** Since attempt 2 the following have held in every record and must not be disturbed while chasing Leads 1–3: both perturbation runs reaching (`all_perturbations_held` true in fifteen of sixteen), `conformance_fraction` 1.0, `red_line_crossed` 0. In particular, the `ruleset` held-out run is the only place `C-LOG-WELL-FORMED` and `C-NO-LATCH-CARRYOVER` are ever exercised — so keep log output in the exact expected form, and ensure no module-level or global state (caches, RNG state, accumulated counters, memoised decisions) survives from one run into the next. An aggressive short-schedule rewrite is exactly the kind of change that reintroduces a latch.

**Call: exploit.** Attempt 16 at 0.8841 is the standing best and the target to beat, and its class (attempts 14 and 16, fast convergence, clean on every check) is still improving — it produced the two highest rewards on record and its cost-ceiling headroom is unspent. The next attempt should rebuild the fast short-schedule configuration and drive the qualifying wall clock below 3.337 s using the per-step budget up to but not past 3.0× the seed anchor, with no shape-based branching anywhere, no state carried between runs, and log output left well-formed. Note for the record that attempts 2–12 repeatedly re-worked the mid-band class after it had stopped improving; do not return to that band.
