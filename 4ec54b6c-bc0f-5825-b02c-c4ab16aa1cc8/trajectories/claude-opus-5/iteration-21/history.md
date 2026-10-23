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

    All five attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

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
  17       0.7716   1.000             2 of 2         yes             15                
  18       0.7140   1.000             2 of 2         yes             18                
  19       0.7950   1.000             2 of 2         yes             15                
  20       0.8298   1.000             2 of 2         yes             6                 
  21       0.4094   1.000             1 of 2         yes             24                

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
  16 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 14 -- reward 0.8820, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 7
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.7950, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 15
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 20 -- reward 0.8298, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 6
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

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (1, 13). Whatever has been
      changing between them is not what is causing it.
    C-NO-SHAPE-FINGERPRINT failed on attempt 15.
    C-PER-STEP-COST-CEILING failed on attempt 13.
    C-PERTURBATION-REACHED has failed on 2 attempts (1, 21). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty-one graded records, every one of which carries a `measurement_status` of `measured` or `measured_phase_cut` and therefore a reward. No record is missing a measurement; nothing below is a stand-in for an unmeasured run. Listed worst to best by reward:

| Rank | Attempt | reward | Notes from the measured terms |
|---|---|---|---|
| 1 | 13 | 0.0000 | `red_line_crossed` = 1, `validity` = 0, `task_pass` = 0, zero_reason_code 1. 37.20 s wall clock, per-step cost ratio 7.185. |
| 2 | 1 | 0.0000 | `primary_target_reached` = 0, `task_pass` = 0, zero_reason_code 4. 89.98 s wall clock, per-step cost ratio 1.019, `qualifying_budget` "not-measured". |
| 3 | 21 | 0.4094 | `primary_target_reached` = 1 but `conformance_fraction` = 0.5, `task_pass` = 0. 24.25 s. |
| 4 | 18 | 0.7140 | 18.25 s, ratio 1.835, efficiency 0.687. `measured_phase_cut`. |
| 5 | 15 | 0.7288 | 4.68 s (fast) but `rule_conformance` 0.857, `task_pass` = 0. |
| 6 | 10 | 0.7393 | 16.90 s, ratio 1.070, efficiency 0.836. |
| 7 | 12 | 0.7443 | 16.94 s, ratio 1.493. |
| 8 | 17 | 0.7716 | 14.84 s, ratio 1.852. |
| 9 | 8 | 0.7843 | 16.51 s, ratio 1.496. |
| 10 | 9 | 0.7891 | 14.16 s, ratio 1.192, `compute_efficiency` = 1.000. |
| 11 | 19 | 0.7950 | 14.69 s, ratio 1.747. |
| 12 | 7 | 0.7994 | 14.10 s, ratio 1.596. |
| 13 | 11 | 0.7997 | 17.00 s, ratio 1.479. |
| 14 | 2 | 0.8037 | 13.49 s, ratio 1.497. First clean pass. |
| 15 | 4 | 0.8042 | 13.66 s, ratio 1.497. (0.8041887) |
| 16 | 3 | 0.8042 | 13.66 s, ratio 1.532. (0.8042363) |
| 17 | 6 | 0.8059 | 13.43 s, ratio 0.971 — the only sub-1.0 per-step cost ratio recorded. |
| 18 | 5 | 0.8255 | 13.74 s, ratio 1.260. |
| 19 | 20 | 0.8298 | 6.31 s, ratio 1.511, efficiency 0.957. |
| 20 | 14 | 0.8820 | 6.63 s, ratio 1.869, efficiency 0.503. |
| 21 | 16 | **0.8841** | 3.34 s, ratio 1.706, efficiency 0.846. All checks held. |

**Attempt 16 holds the highest reward at 0.8841 and is the one to beat.** Attempt 14 (0.8820) is the closest runner-up.

Direction of movement must be stated plainly, because `standing_against_best_so_far` states it: attempts 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20 and 21 are each recorded as `worse_than_an_earlier_attempt`. That is fifteen of twenty-one records that regressed rather than improved. Only attempts 2, 3, 5, 14 and 16 are recorded as `better_than_every_earlier_attempt`. The last three graded records (19: 0.7950, 20: 0.8298, 21: 0.4094) are all regressions against 16's 0.8841, and attempt 21 in particular is a large regression, not partial progress.

A caution about reading the leaderboard: reward correlates strongly but not perfectly with wall clock / `qualifying_budget`. Attempt 20 ran *faster* than attempt 14 (6.31 s vs 6.63 s) and was far more compute-efficient (0.957 vs 0.503), yet scored lower (0.8298 vs 0.8820). Likewise attempt 9 achieved `compute_efficiency` = 1.000 and only scored 0.7891, and attempt 6 achieved the lowest per-step cost ratio on record (0.971) and only scored 0.8059. Shrinking the budget is the strongest single lever the data shows, but it is not the whole objective — something about solution quality at the qualifying row also moves the number, and the terms supplied do not name it.

# 2. Approach classes tried

The submissions' source is not carried forward, so these classes are grouped by their measured signatures (`wall_clock_sec` / `qualifying_budget`, `per_step_cost_ratio`, `compute_efficiency`, and which checks fired). Records that failed the same way are collapsed into one entry.

**Class A — near-seed-cost, non-converging baseline (attempt 1, 0.0000).** Per-step cost ratio 1.019, essentially the seed anchor's cost, `compute_efficiency` 1.000, but it ran 89.98 s and no evaluation row ever crossed the threshold in the declared direction. `qualifying_budget` came back "not-measured" because no row qualified. Both perturbation runs also failed. This class produced no usable signal beyond "cheap per step is not sufficient."

**Class B — mid-budget plateau, ~13–18 s (attempts 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 19; rewards 0.7140 to 0.8255).** Per-step cost ratios spread across 0.971 to 1.852, compute efficiency 0.503 to 1.000, and every one of these passed every check with `conformance_fraction` 1.0 and both perturbations reaching. This is the largest class and it is a plateau: fourteen records clustered between 0.71 and 0.83, with no monotone relationship to per-step cost or efficiency inside the band. Attempt 5 (0.8255, ratio 1.260) is the top of this class; attempt 6 (0.8059) drove per-step cost *below* the seed anchor at 0.971 and did not beat it; attempt 9 (0.7891) hit perfect `compute_efficiency` 1.000 and did not beat it either. Varying cost-per-step and efficiency within a fixed ~13–18 s budget did not break the plateau.

**Class C — short-budget family, 3.3–6.6 s (attempts 14, 16, 20; rewards 0.8820, 0.8841, 0.8298).** These are the only records under 7 s and they hold the top three rewards excluding nothing. All clean: `conformance_fraction` 1.0, both perturbations reached, `red_line_crossed` 0, `task_pass` 1. Per-step cost ratios 1.511 to 1.869 — i.e. this class *spends more per step* than Class B typically did while finishing far sooner, and `compute_efficiency` for the best member (16) is 0.846, not maximal. The best record overall, attempt 16, sits here at 3.34 s.

**Class D — heavy per-step / long-run variant (attempt 13, 0.0000).** Per-step cost ratio 7.185, wall clock 37.20 s. This crossed the red line: `validity` 0, `task_pass` 0. Both perturbation runs actually reached their thresholds, so the failure was purely on the primary run's budget and cost ceiling.

**Class E — short-budget with model-shape branching (attempt 15, 0.7288).** Fast (4.68 s) and both perturbations reached, but it fingerprinted the model by shape, which cost it `rule_conformance` (0.857) and `task_pass` (0) despite `conformance_fraction` staying at 1.0. This is Class C's speed with a conformance defect bolted on.

**Class F — extended primary run that starved a perturbation (attempt 21, 0.4094).** The primary run reached its target at 24.25 s and stayed inside the red line, but only 1 of 2 declared perturbations reached inside its own budget, giving `conformance_fraction` 0.5 and `task_pass` 0. Roughly half the reward of the Class B plateau and less than half of the best.

# 3. Checks that failed

Named checks, with the verifier's own reasons and how often each has now fired.

- **C-BUDGET-RESPECTED — failed in three records (attempts 1, 13, 21), five occurrences once perturbation runs are counted.** Attempt 1, primary: "no qualifying row, so no budget position exists." Attempt 13, primary: "the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1" — this is the one place the numeric ceiling is stated, **31.1 on the wall_clock_sec axis**. It also fired on both of attempt 1's perturbation runs and on attempt 21's held-out-variant run. This is the most-repeated named failure. Whatever was changed between attempts 1, 13 and 21 is not what causes it; in each case the run simply sat above a budget ceiling (or never produced a qualifying row at all), and the fix is to keep the qualifying row's wall clock well under the ceiling on the primary run *and* on each perturbation run separately.
- **C-PERTURBATION-REACHED — failed in two records (attempts 1, 21).** Attempt 1: "0 of 2 declared perturbations reached their own threshold inside their own budget." Attempt 21: "1 of 2 declared perturbations reached their own threshold inside their own budget." Twice failed, and the two attempts differ substantially in every other measured term (attempt 1 never reached its primary target; attempt 21 did), so whatever was changed between them is not the cause. The cause in both is a perturbation run failing its own budget/threshold, and only per-perturbation headroom addresses it.
- **C-TARGET-REACHED — failed in one record (attempt 1) on the primary and on both of that record's perturbation runs.** Reason: "no evaluation row crosses the threshold in the declared direction." Note the phrase *in the declared direction* — the declared direction must match the metric being logged.
- **C-PER-STEP-COST-CEILING — failed once (attempt 13).** Reason: "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0". The ceiling is **3.0× the seed anchor**. Every other record's `per_step_cost_ratio` sits between 0.971 and 1.869, comfortably under it, so this ceiling is not currently binding except for that one heavy variant.
- **C-NO-SHAPE-FINGERPRINT — failed once (attempt 15).** Reason: "the submission fingerprints the model by shape". This dropped `rule_conformance` to 0.857 and `task_pass` to 0 while leaving speed and perturbation results intact; it cost roughly 0.15 of reward against sibling Class C records.
- **C-LOG-WELL-FORMED — failed once**, on attempt 1's ruleset perturbation run only. No separate reason string was supplied beyond the check name.
- **C-NO-LATCH-CARRYOVER — failed once**, on attempt 1's ruleset perturbation run only. No separate reason string was supplied.

Everything else passed everywhere: `rule_conformance` is 1.0 in every record except attempt 15, and `red_line_crossed` is 0 in every record except attempt 13.

# 4. Ruled-out directions

- **Minimising per-step cost as the primary lever.** Attempt 6 pushed `per_step_cost_ratio` to 0.971, below the seed anchor, and scored 0.8059 — below attempts 5, 20, 14 and 16, all of which spent *more* per step (1.260 to 1.869). Attempt 1's ratio of 1.019 scored 0.0000. Cheap steps do not buy reward.
- **Maximising `compute_efficiency`.** Attempt 9 reached `compute_efficiency` = 1.000 and scored 0.7891; attempt 1 also reported 1.000 and scored 0.0000. The best record (16) has efficiency 0.846 and the runner-up (14) has 0.503. This term does not rank submissions.
- **The ~13–18 s mid-budget operating point (Class B).** Fourteen records, all fully conformant, all landing between 0.7140 and 0.8255, none reaching the 0.8841 mark. Repeated re-parameterisation inside this band has stopped producing improvement; it is a plateau, not a ladder.
- **High per-step-cost / long-wall-clock configurations (Class D, attempt 13).** Ruled out by two hard ceilings simultaneously: 37.20 s against a 31.1 wall_clock_sec ceiling and a 7.185× per-step ratio against a 3.0× ceiling. It scored 0.0000 with `validity` 0 even though both its perturbation runs reached their thresholds. Do not exceed 31.1 s or 3.0× seed-anchor per-step cost under any circumstance.
- **Fingerprinting or branching on model shape (Class E, attempt 15).** Ruled out by C-NO-SHAPE-FINGERPRINT firing directly on it, which zeroed `task_pass` and dropped reward to 0.7288 despite a 4.68 s run. The algorithm must be shape-agnostic: no dispatch, no hyperparameter selection, and no special-casing keyed on parameter or tensor shapes.
- **Buying primary-run headroom at the perturbation runs' expense (Class F, attempt 21).** Extending the primary to 24.25 s left a held-out-variant perturbation unable to finish inside its own budget; `conformance_fraction` halved to 0.5 and reward fell to 0.4094. The perturbation runs get their own budgets, and the primary being comfortably inside its ceiling is no protection.
- **Configurations that never cross the threshold in the declared direction (attempt 1).** 89.98 s of wall clock with no qualifying row produces a cascade — C-TARGET-REACHED, then C-BUDGET-RESPECTED for want of a qualifying row, then C-PERTURBATION-REACHED — and a reward of 0.0000. Verify the declared direction matches the logged metric's sense.

# 5. Open leads

- **Push the short-budget family (Class C) further down.** The measured trend inside that class is 6.63 s → 0.8820, 3.34 s → 0.8841. Attempt 16's configuration at 3.34 s with `per_step_cost_ratio` 1.706 is the profile to reproduce and then shave. There is a large amount of unused headroom against the 31.1 s ceiling, so the risk here is not the budget check but under-converging into C-TARGET-REACHED, as attempt 1 did.
- **Resolve the 14-vs-20 anomaly.** Attempt 20 was faster and more compute-efficient than attempt 14 and still scored 0.0522 lower. Whatever distinguishes them is worth isolating, because it is a lever independent of budget and efficiency. The supplied terms do not name it; the only measured differences are `per_step_cost_ratio` (1.511 vs 1.869) and `compute_efficiency` (0.957 vs 0.503), both of which point the "wrong" way for 20. A deliberate A/B at fixed budget varying only per-step spend would settle whether higher per-step spend at short budget is what buys the extra reward.
- **Combine attempt 16's timing profile with a shape-agnostic reimplementation of whatever attempt 15 was doing.** Attempt 15 was the second-fastest record on file (4.68 s) and lost roughly 0.15 of reward solely to C-NO-SHAPE-FINGERPRINT. If the speed came from something that can be obtained without keying on shape — e.g. deriving the same quantity from parameter counts computed generically, or from a runtime probe rather than a shape lookup — that speed is recoverable at full conformance.
- **Guard the perturbation runs explicitly.** Held-out-variant runs have now failed twice (attempt 1 and attempt 21) and ruleset runs once (attempt 1); see the aggregate below. Any budget the algorithm chooses should be self-limiting relative to whatever budget it is handed, rather than an absolute step count or time, so that a perturbation run with a tighter budget still terminates inside it.
- **Keep per-step cost between roughly 1.5× and 1.9× the seed anchor.** Every top-three record sits in that band, and the 3.0× ceiling leaves room, so the band can be explored upward with a safety margin rather than treated as fixed.

**Perturbation-unit outcomes.** Each record declares 2 perturbations, one of kind `ruleset` and one of kind `held_out_variant` — 42 held-out runs in total across the 21 records. The runs are not identified beyond their kind, so no run can be traced from one record to another. By kind: **ruleset** reached its threshold in 20 of 21 records; the single failure was in attempt 1, where it failed four checks at once — C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER. **held_out_variant** reached its threshold in 19 of 21 records; it failed in attempt 1 on C-TARGET-REACHED and C-BUDGET-RESPECTED, and in attempt 21 on C-BUDGET-RESPECTED alone. In aggregate, 39 of 42 held-out runs reached their thresholds, and the kind that has failed most often is `held_out_variant`, failing on **C-BUDGET-RESPECTED** both times. That single check is the one recurring obstacle in the held-out runs and the thing to engineer against.

**Recommendation: exploit.** The short-budget family (Class C) is the only class still improving — it produced the two best rewards on record, 0.8841 and 0.8820, and its trend inside the class points toward shorter budgets. The right move is to rebuild attempt 16's profile (≈3.3 s qualifying budget, per-step cost ratio ≈1.7, shape-agnostic throughout, both perturbations comfortably inside their own budgets) and tighten it, rather than open a new structural direction. Note for the record that the mid-budget plateau (Class B) absorbed fourteen records that kept re-landing in the same 0.71–0.83 band; re-entering that band without changing the operating point is neither exploration nor exploitation and should not be repeated. Likewise, the two 0.0000 records failed for two distinct and now-known reasons — never crossing the threshold, and crossing the 31.1 s / 3.0× red lines — and either would score 0.0000 again unchanged.
