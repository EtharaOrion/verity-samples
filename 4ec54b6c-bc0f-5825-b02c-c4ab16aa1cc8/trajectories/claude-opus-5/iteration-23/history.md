# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 23 -- reward 0.9151, better than every earlier attempt   (best so far)
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
  16       0.8841   1.000             2 of 2         yes             3                 
  17       0.7716   1.000             2 of 2         yes             15                
  18       0.7140   1.000             2 of 2         yes             18                
  19       0.7950   1.000             2 of 2         yes             15                
  20       0.8298   1.000             2 of 2         yes             6                 
  21       0.4094   1.000             1 of 2         yes             24                
  22       0.0000   1.000             2 of 2         yes             6                 
  23 *     0.9151   1.000             2 of 2         yes             3                 

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

    attempt 14 -- reward 0.8820, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 7
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 16 -- reward 0.8841, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 3
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 21 -- reward 0.4094, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      NOTE: this attempt's phase was cut before it finished. What follows was graded
            on whatever was on disk at that moment, not on what it intended to submit,
            so a term below may report unfinished work rather than a failed idea.
      measured: rule conformance 1.000, target reached yes, qualifying budget 24
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 22 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 6
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-PER-STEP-COST-CEILING -- per-step cost is 7.259 times the seed anchor, above the ceiling of 3.0

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (1, 13). Whatever has been
      changing between them is not what is causing it.
    C-NO-SHAPE-FINGERPRINT failed on attempt 15.
    C-PER-STEP-COST-CEILING has failed on 2 attempts (13, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 2 attempts (1, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All 23 records carry `measurement_status` of either `measured` or `measured_phase_cut`, and every one of them carries a reward. No record is missing a measurement, so none of the zeros below is an "absent measurement" — the three zeros are genuine measured zeros with stated zero-reason codes.

Ordered worst to best by reward:

| Rank | Attempt | Reward | Wall clock (s) | Notes |
|---|---|---|---|---|
| 1 | 1 | 0.0000 | 89.9778 | zero_reason_code 4; target never reached |
| 2 | 13 | 0.0000 | 37.2022 | zero_reason_code 1; red line crossed; validity 0 |
| 3 | 22 | 0.0000 | 6.3893 | zero_reason_code 1; red line crossed; validity 0 |
| 4 | 21 | 0.4094 | 24.2457 | one of two perturbations missed; task_pass 0 |
| 5 | 18 | 0.7140 | 18.2474 | clean checks |
| 6 | 15 | 0.7288 | 4.6808 | C-NO-SHAPE-FINGERPRINT failed; task_pass 0 |
| 7 | 10 | 0.7393 | 16.8995 | clean checks |
| 8 | 12 | 0.7443 | 16.9433 | clean checks |
| 9 | 17 | 0.7716 | 14.8440 | clean checks |
| 10 | 8 | 0.7843 | 16.5068 | clean checks |
| 11 | 9 | 0.7891 | 14.1599 | compute_efficiency 1.0000 |
| 12 | 19 | 0.7950 | 14.6918 | clean checks |
| 13 | 7 | 0.7994 | 14.1032 | clean checks |
| 14 | 11 | 0.7997 | 17.0029 | clean checks |
| 15 | 2 | 0.8037 | 13.4877 | first attempt to pass everything |
| 16 | 4 | 0.8042 | 13.6584 | exact value 0.8041887 |
| 17 | 3 | 0.8042 | 13.6621 | exact value 0.8042363; edges out attempt 4 |
| 18 | 6 | 0.8059 | 13.4266 | per_step_cost_ratio 0.9711, the lowest seen |
| 19 | 5 | 0.8255 | 13.7398 | clean checks |
| 20 | 20 | 0.8298 | 6.3142 | clean checks |
| 21 | 14 | 0.8820 | 6.6280 | clean checks |
| 22 | 16 | 0.8841 | 3.3367 | clean checks |
| 23 | 23 | **0.9151** | 2.9523 | best; clean checks |

**Attempt 23 holds the highest reward at 0.9151 and is the attempt to beat.**

Direction of travel must not be softened: `standing_against_best_so_far` reads `worse_than_an_earlier_attempt` for attempts 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21 and 22. Fifteen of the twenty-three graded submissions were regressions against the then-current best, including everything in the 0.71–0.80 band and all three zeros after attempt 1. Only attempts 2, 3, 5, 14, 16 and 23 improved on every earlier attempt. The improvement track is short and the regression track is long.

The single strongest signal in the whole table is that reward tracks wall clock (equal to `qualifying_budget` in every record) almost monotonically, and does **not** track `compute_efficiency`. Attempt 9 achieved `compute_efficiency` 1.0000 and scored only 0.7891 at 14.16 s; attempt 23 achieved `compute_efficiency` 0.7216 and scored 0.9151 at 2.95 s. Attempt 6 achieved the lowest `per_step_cost_ratio` of the whole run (0.9711) and scored 0.8059 at 13.43 s. Total elapsed time, not per-step frugality and not the efficiency figure, is what moves the reward.

# 2. Approach classes tried

The records give metrics, not source, so the classes below are grouped by their measured fingerprint (`wall_clock_sec`, `per_step_cost_ratio`, `compute_efficiency`, `task_pass`, `failed_checks`). Treat the labels as descriptions of measured behaviour rather than as claims about specific code.

**Class A — non-converging baseline (attempt 1).** 89.98 s, `primary_target_reached` 0, `conformance_fraction` 0, `task_pass` 0, reward 0.0000. Ran long and never crossed the threshold in the declared direction. Both perturbation units also failed. Also the only record whose ruleset unit tripped log-format and latch-carryover checks. Nothing about this class scored.

**Class B — mid-cost converging solutions, ~13–19 s (attempts 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 19).** All pass every check, `validity` 1, `rule_conformance` 1, `task_pass` 1, both perturbations held. `per_step_cost_ratio` spread 0.9711–1.8520; `compute_efficiency` spread 0.5031–1.0000. Rewards cluster tightly in 0.7140–0.8059. Within this class the internal variation in per-step cost and efficiency buys almost nothing: the whole class is pinned by its runtime. This is the plateau that the loop kept revisiting.

**Class C — fast converging solutions, ~2.9–6.7 s (attempts 14, 16, 20, 23).** Same clean-check profile as class B — every check held, both perturbations reached, `validity` 1, `task_pass` 1 — but wall clock cut to 6.63, 3.34, 6.31 and 2.95 s respectively, with rewards 0.8820, 0.8841, 0.8298 and 0.9151. `per_step_cost_ratio` in this class sits higher than class B (1.5111–1.8690) and `compute_efficiency` is often lower, yet the rewards are uniformly better. This is the only class that has produced anything above 0.83, and it contains the current best.

**Class D — heavy per-step approaches (attempts 13 and 22).** `per_step_cost_ratio` of 7.1852 and 7.2593 against a declared ceiling of 3.0. Both crossed the red line, both had `validity` driven to 0 and `task_pass` to 0, both scored 0.0000 under zero_reason_code 1. Notably attempt 22 still reached the primary target, still held both perturbations, and still ran in 6.39 s — the cost ceiling alone destroyed it. Attempt 13 additionally blew the wall-clock ceiling at 37.20 s against a declared 31.1.

**Class E — shape-fingerprinting shortcut (attempt 15).** Fast (4.68 s), reached the primary target, held both perturbations, `validity` 1 — but `rule_conformance` fell to 0.8571 on C-NO-SHAPE-FINGERPRINT and `task_pass` went to 0. Reward 0.7288, well below what a clean run at that runtime would suggest given attempt 16 scored 0.8841 at 3.34 s. Identifying the model by its shape is measurably penalised.

**Class F — primary-passing but perturbation-failing (attempt 21).** Reached the primary target at 24.25 s with `per_step_cost_ratio` 1.2205 and clean rule conformance, but only 1 of 2 declared perturbations reached its threshold inside its own budget; `conformance_fraction` 0.5, `task_pass` 0, reward 0.4094. Passing the primary run is not sufficient — the held-out runs carry roughly half the outcome.

# 3. Checks that failed

**C-BUDGET-RESPECTED — failed in three records, and this is the most repeated finding.** In attempt 1 the reason was "no qualifying row, so no budget position exists." In attempt 13 the reason was "the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1." It also appears at the perturbation-unit level in attempt 1 (both units) and in attempt 21 (the held-out-variant unit). Across three widely separated attempts with different structural approaches this check kept failing, so **whatever was changed between those attempts is not what causes C-BUDGET-RESPECTED.** It fails for exactly one measured reason: the qualifying row's position on the wall_clock_sec axis relative to the declared ceiling, either because no row qualifies at all or because the row that does sits above the ceiling.

**C-PER-STEP-COST-CEILING — failed twice, attempts 13 and 22.** Reasons: "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0" and "per-step cost is 7.259 times the seed anchor, above the ceiling of 3.0." Two attempts, two nearly identical ratios (7.19 and 7.26), one of them at 37 s and one at 6.4 s. **The change made between attempt 13 and attempt 22 did not address this check** — the cost ratio barely moved. The ceiling is a hard 3.0 multiple of the seed anchor and both records had `validity` forced to 0 and reward to 0.0000 as a direct result.

**C-PERTURBATION-REACHED — failed twice, attempts 1 and 21.** Reasons: "0 of 2 declared perturbations reached their own threshold inside their own budget" and "1 of 2 declared perturbations reached their own threshold inside their own budget." This is an aggregate over the held-out runs and it failed with two very different underlying approaches, so the difference between those attempts is not what governs it.

**C-TARGET-REACHED — failed once at the primary level, attempt 1**, reason "no evaluation row crosses the threshold in the declared direction." It also failed at the perturbation-unit level in both of attempt 1's units.

**C-NO-SHAPE-FINGERPRINT — failed once, attempt 15**, reason "the submission fingerprints the model by shape." This drove `rule_conformance` to 0.8571 and `task_pass` to 0 on an otherwise fast, target-reaching, perturbation-holding run.

**C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER — failed once each**, both inside attempt 1's ruleset perturbation unit only. No verifier reason string was supplied for these two at unit level. They have not recurred in any later record.

**Perturbation-unit outcomes.** Two units are declared in every record, one of kind `ruleset` and one of kind `held_out_variant`. The units are not identified, so nothing below asserts that a given unit is the same one across records. Across the 23 records that is 46 unit outcomes, of which 43 reached their threshold and 3 did not. By kind: units of kind `ruleset` failed to reach in exactly one record (attempt 1), where they were stopped by C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER. Units of kind `held_out_variant` failed to reach in two records — attempt 1, stopped by C-TARGET-REACHED and C-BUDGET-RESPECTED, and attempt 21, stopped by C-BUDGET-RESPECTED alone. **The `held_out_variant` kind is the one that has failed more often, and the check that stops it in both cases is C-BUDGET-RESPECTED.** Every record from attempt 2 onward except attempt 21 had all perturbations hold.

# 4. Ruled-out directions

**Any approach whose per-step cost exceeds 3.0× the seed anchor.** Ruled out because attempts 13 and 22 both measured above 7× and both were zeroed under zero_reason_code 1 with `validity` 0, regardless of everything else being right — attempt 22 reached the primary target, held both perturbations, kept full rule conformance and ran in 6.39 s, and still scored 0.0000. There is no partial credit past this ceiling.

**Fingerprinting the model by shape.** Ruled out because attempt 15 did exactly this, was flagged by C-NO-SHAPE-FINGERPRINT, and had `task_pass` set to 0 and `rule_conformance` cut to 0.8571, yielding 0.7288 at 4.68 s — worse than attempt 16's 0.8841 at 3.34 s and worse than attempt 14's 0.8820 at 6.63 s. Whatever the shortcut bought in speed was more than erased by the conformance penalty.

**Running long, in any form.** Ruled out because the entire 13–19 s class B band (fourteen attempts) never exceeded 0.8059 despite all of them being fully clean, while every sub-7 s clean run scored 0.8298 or better. The 24.25 s attempt 21 scored 0.4094 and the 37.20 s attempt 13 was zeroed on the wall-clock ceiling of 31.1. Time is the reward.

**Optimising `compute_efficiency` or `per_step_cost_ratio` as the objective.** Ruled out on direct measurement: attempt 9 hit `compute_efficiency` 1.0000 and scored 0.7891; attempt 6 hit `per_step_cost_ratio` 0.9711, the best of any record, and scored 0.8059; the best-scoring attempt 23 had a middling 0.7216 efficiency and a 1.6248 cost ratio. These two quantities only matter as constraints (stay under the 3.0 ceiling); driving them further down has never bought reward.

**Micro-variation within the class B plateau.** Ruled out because attempts 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18 and 19 all cleared every check and all landed in a 0.09-wide band, with eleven of them recorded as regressions against the then-current best. Re-entering that band by tweaking parameters at ~14 s is not a path to beating 0.9151.

**Approaches that trade primary-run speed against the held-out budget.** Ruled out because attempt 21 obtained a decent `per_step_cost_ratio` of 1.2205 and reached the primary target, but let a `held_out_variant` unit exceed its own budget, halving `conformance_fraction` to 0.5 and collapsing the reward to 0.4094. The held-out runs have their own budgets and must be satisfied on their own terms.

# 5. Open leads

**Drive wall clock below 2.95 s while keeping every check clean.** This is the single lead the data supports most strongly. The reward-versus-runtime relation across the clean records is close to monotone: 2.95 s → 0.9151, 3.34 s → 0.8841, 6.31 s → 0.8298, 6.63 s → 0.8820, 13.4–19.0 s → 0.7140–0.8059. The current best sits at the fastest measured runtime, so the frontier has not been shown to flatten. Reproduce whatever class C does and cut further.

**Note the 3.34 s / 6.63 s inversion and exploit it.** Attempt 16 at 3.34 s scored 0.8841 and attempt 14 at 6.63 s scored 0.8820 — nearly identical rewards at twice the runtime, while attempt 20 at 6.31 s scored only 0.8298. Runtime therefore explains most but not all of the variation; there is a second-order term worth perhaps 0.05 that separates attempt 14 from attempt 20 at essentially the same runtime. Attempt 14 had `per_step_cost_ratio` 1.8690 and `compute_efficiency` 0.5031 against attempt 20's 1.5111 and 0.9565, which is the opposite of what a cost-driven story predicts, so the residual is not explained by the cost terms in the record. Isolating it is the one lead that could add reward without further speedup.

**Keep `per_step_cost_ratio` in the band that has actually scored: roughly 1.5–1.9.** Every class C record sits there (1.5111, 1.6248, 1.7057, 1.8690). The ceiling is 3.0, so there is headroom to spend more per step in exchange for fewer steps — the two zeroed records overshot to ~7.2, which is far past the ceiling, but nothing between 1.9 and 3.0 has ever been measured. Trading steps for per-step work up to a ratio of about 2.5 is unexplored territory that stays legal.

**Verify the held-out-variant budget explicitly before submitting.** C-BUDGET-RESPECTED at unit level has stopped a `held_out_variant` run twice, and that failure mode costs about half the reward (attempt 21, 0.4094) rather than zeroing it. As total runtime is pushed down, confirm the speedup applies inside the held-out runs' own budgets and not only to the primary row.

**Keep the primary wall clock far from the 31.1 declared ceiling.** Attempt 13 is the only record that ever touched it, at 37.20 s. At sub-3 s this is not currently a live risk, but it is the exact axis and number the verifier cited, so it is worth respecting as a hard bound in any change that could lengthen the run.

**Do not reintroduce shape-based model identification, log-format irregularities, or latch carryover.** C-NO-SHAPE-FINGERPRINT cost attempt 15 its `task_pass`; C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER appeared only in attempt 1's ruleset unit and have stayed clean since, which is a property worth preserving rather than a problem to solve.

---

**Call: exploit.** Class C — the fast, fully clean approach that produced 0.8820, 0.8841 and the leading 0.9151 — is still improving, and its improvements have come from one lever, runtime, whose relationship to reward has not yet flattened. The right move is to rebuild the class C shape, cut wall clock below 2.95 s while holding `per_step_cost_ratio` under 3.0, keep every check clean including the two held-out units and their own budgets, and beat 0.9151. Exploring structurally new ideas is not warranted: the plateau class B and the two red-line classes are well characterised and none of them approaches the current best. It should also be said plainly that earlier work repeatedly re-entered the class B 13–19 s plateau and repeatedly re-crossed the 3.0 per-step cost ceiling at ~7.2× without changing what caused those outcomes; that pattern is neither exploration nor exploitation and should not be repeated.
