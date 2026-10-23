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

    All two attempts since have scored lower than it.
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
  13 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 17 -- reward 0.7716, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 15
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 18 -- reward 0.7140, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      NOTE: this attempt's phase was cut before it finished. What follows was graded
            on whatever was on disk at that moment, not on what it intended to submit,
            so a term below may report unfinished work rather than a failed idea.
      measured: rule conformance 1.000, target reached yes, qualifying budget 18
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (1, 13). Whatever has been
      changing between them is not what is causing it.
    C-NO-SHAPE-FINGERPRINT failed on attempt 15.
    C-PER-STEP-COST-CEILING failed on attempt 13.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Every one of the eighteen records carries a `measurement_status` of either `measured` or `measured_phase_cut`, and every one carries a reward. There is no record here that produced no measurement, so nothing below is an absent-measurement case.

Ordered worst to best by reward:

| Rank | Attempt | Reward | Note |
|---|---|---|---|
| 1 | 1 | 0.0000 | zero_reason_code 4; primary target never reached; conformance_fraction 0.0 |
| 1= | 13 | 0.0000 | zero_reason_code 1; red_line_crossed 1.0; validity 0.0 |
| 3 | 18 | 0.7140 | worse than an earlier attempt |
| 4 | 15 | 0.7288 | worse than an earlier attempt; task_pass 0.0 despite reward > 0 |
| 5 | 10 | 0.7393 | worse than an earlier attempt |
| 6 | 12 | 0.7443 | worse than an earlier attempt |
| 7 | 17 | 0.7716 | worse than an earlier attempt |
| 8 | 8 | 0.7843 | worse than an earlier attempt |
| 9 | 9 | 0.7891 | worse than an earlier attempt |
| 10 | 7 | 0.7994 | worse than an earlier attempt |
| 11 | 11 | 0.7997 | worse than an earlier attempt |
| 12 | 2 | 0.8037 | first attempt to score; best at the time |
| 13 | 4 | 0.8042 | worse than an earlier attempt (below attempt 3, which it trails by ~0.00005) |
| 14 | 3 | 0.8042 | best at the time |
| 15 | 6 | 0.8059 | worse than an earlier attempt (below attempt 5) |
| 16 | 5 | 0.8255 | best at the time |
| 17 | 14 | 0.8820 | best at the time |
| 18 | 16 | **0.8841** | **highest reward recorded; this is the one to beat** |

**Attempt 16 holds the highest reward, 0.8841, and is the target to beat.**

The single strongest signal across the scored records is wall clock. `wall_clock_sec` equals `qualifying_budget` in every scored record, and reward tracks it inversely and almost monotonically:

- 3.34 s → 0.8841 (attempt 16, best)
- 6.63 s → 0.8820 (attempt 14)
- 4.68 s → 0.7288 (attempt 15 — the exception, and the reason is a failed check, not the clock)
- 13.43–14.84 s → 0.7716 to 0.8255 (attempts 2, 3, 4, 5, 6, 7, 9, 17)
- 16.51–18.25 s → 0.7140 to 0.7996 (attempts 8, 10, 11, 12, 18)
- 37.20 s → 0.0000 (attempt 13, over the ceiling)

`compute_efficiency` and `per_step_cost_ratio` do **not** track reward. Attempt 9 reached `compute_efficiency` 1.0 and scored 0.7891; attempt 6 achieved `per_step_cost_ratio` 0.9711 (below the seed anchor) and scored only 0.8059; the two best attempts, 14 and 16, ran at `per_step_cost_ratio` 1.8690 and 1.7057 and `compute_efficiency` 0.5031 and 0.8460 respectively. Spending more per step to finish in fewer seconds has paid, and optimising per-step cost at the expense of total time has not.

# 2. Approach classes tried

The next attempt starts from a pristine stub and cannot see any earlier code, so these classes are grouped by their measured signature rather than by source. Records that failed the same way are collapsed into one entry.

**Class A — non-converging configuration (attempt 1, reward 0.0000).**
The run produced no evaluation row that crossed the threshold in the declared direction. `conformance_fraction` 0.0, `primary_target_reached` 0.0, `task_pass` 0.0, `zero_reason_code` 4. Both declared perturbations also failed. `per_step_cost_ratio` was 1.0194 and `compute_efficiency` 1.0, i.e. the run was cheap per step and simply never learned to threshold. `wall_clock_sec` 89.98 with no qualifying row at all. This class is a total loss and was abandoned after one record.

**Class B — converging baseline in the 13–18 s band (attempts 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18; rewards 0.7140 to 0.8255).**
All hold every check, all reach the primary target, all hold both perturbations, `rule_conformance` 1.0, `red_line_crossed` 0.0, `validity` 1.0. This is thirteen records clustered inside a ~0.11-wide reward band, distinguished almost entirely by wall clock (13.43 s to 18.25 s). Within the class, variations in `per_step_cost_ratio` across 0.9711 to 1.8690 and `compute_efficiency` across 0.5031 to 1.0 moved reward around unpredictably and never above 0.8255. This class was iterated on many times with diminishing and largely noise-level returns; attempts 6, 7, 8, 9, 10, 11, 12, 17 and 18 all came in **below** an earlier attempt in the same class.

**Class C — heavy per-step compute (attempt 13, reward 0.0000).**
`per_step_cost_ratio` 7.1852 and `wall_clock_sec` 37.20. This reached the primary target and held both perturbations, but crossed the red line: `red_line_crossed` 1.0, `validity` 0.0, `task_pass` 0.0, `zero_reason_code` 1. Two checks failed, both quantified in the verifier's own reasons (see section 3). This class buys nothing because the reward is zeroed regardless of target attainment.

**Class D — fast convergence (attempts 14 and 16; rewards 0.8820 and 0.8841).**
Wall clock 6.63 s and 3.34 s, roughly a half and a quarter of the class-B band. Both hold every check, both hold both perturbations, `rule_conformance` 1.0. Both run at elevated per-step cost (1.8690 and 1.7057) with mid-range `compute_efficiency` (0.5031 and 0.8460). **This is the only class that has beaten 0.83, and attempt 16 in this class is the best result recorded.**

**Class E — shape-fingerprinting shortcut (attempt 15, reward 0.7288).**
Wall clock 4.68 s, i.e. inside class D's fast band and faster than attempt 14, with a comparable `per_step_cost_ratio` of 1.8731. It nevertheless scored 0.7288, below attempt 14's 0.8820, because it failed `C-NO-SHAPE-FINGERPRINT`. `rule_conformance` fell to 0.8571 and `task_pass` to 0.0 while `conformance_fraction` stayed 1.0 and `validity` stayed 1.0. This is the cleanest controlled comparison in the whole set: fast timing was preserved, one named check was broken, and roughly 0.15 of reward was lost.

# 3. Checks that failed

**C-TARGET-REACHED** — failed once at the primary level, in attempt 1, reason: "no evaluation row crosses the threshold in the declared direction". It also failed in both of attempt 1's held-out runs. Across the whole set that is three failures, all inside the single record attempt 1.

**C-BUDGET-RESPECTED** — failed at the primary level in **two** records, attempts 1 and 13, with two different reasons. In attempt 1: "no qualifying row, so no budget position exists", i.e. it failed as a consequence of C-TARGET-REACHED failing, not as an independent budget overrun. In attempt 13: "the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1". It additionally failed in both of attempt 1's held-out runs, for four failures in total. **The two primary failures have distinct causes and the changes made between attempts 1 and 13 are not what links them** — one is a no-qualifying-row artefact, the other a genuine overrun of the 31.1 s ceiling. The single actionable fact is the number: the wall-clock ceiling is 31.1 and every scored attempt has come in well under it.

**C-PERTURBATION-REACHED** — failed once, in attempt 1, reason: "0 of 2 declared perturbations reached their own threshold inside their own budget". It has held in all seventeen subsequent records.

**C-PER-STEP-COST-CEILING** — failed once, in attempt 13, reason: "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0". This gives the hard number the next attempt must respect: **per-step cost must stay at or below 3.0× the seed anchor**. Every scored record has sat between 0.9711 and 1.8731, comfortably inside it, including the two best.

**C-NO-SHAPE-FINGERPRINT** — failed once, in attempt 15, reason: "the submission fingerprints the model by shape". This is the only conformance-behaviour check ever to fail, and it cost that attempt `task_pass` and dropped `rule_conformance` to 0.8571 while every other measured quantity stayed healthy.

**C-LOG-WELL-FORMED** and **C-NO-LATCH-CARRYOVER** — each failed once, and only inside a held-out run of attempt 1 (see section on perturbation outcomes below). Neither has appeared at the primary level in any record.

**Perturbation outcomes.** Each record declared two held-out runs, one of kind `ruleset` and one of kind `held_out_variant`, for 36 units in total across the eighteen records. 34 of 36 reached their threshold. The only failures are the two units in attempt 1, one of each kind:

- **`ruleset` kind:** 18 declared, 17 reached, 1 not reached. The failing unit was stopped by `C-LOG-WELL-FORMED`, `C-TARGET-REACHED`, `C-BUDGET-RESPECTED` and `C-NO-LATCH-CARRYOVER`.
- **`held_out_variant` kind:** 18 declared, 17 reached, 1 not reached. The failing unit was stopped by `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`.

Since attempt 1, `all_perturbations_held` has been true in every record, including attempts 13 and 15 which failed primary-level checks. Held-out generalisation is not the bottleneck and has not been for a long time; the `C-LOG-WELL-FORMED` and `C-NO-LATCH-CARRYOVER` failures on the `ruleset` kind are a solved historical problem, not a live one.

# 4. Ruled-out directions

**Any configuration that does not drive the primary metric across its threshold (class A).** Attempt 1 scored 0.0000 with `zero_reason_code` 4 and `conformance_fraction` 0.0. Crossing the threshold in the declared direction is a precondition; without a qualifying row, the budget check cannot even be evaluated. Ruled out.

**Heavy per-step compute to accelerate convergence (class C).** Attempt 13 scored 0.0000. It reached the primary target and held both perturbations, and it was still zeroed: `per_step_cost_ratio` 7.1852 broke the 3.0 ceiling and `wall_clock_sec` 37.20 broke the 31.1 ceiling, setting `red_line_crossed` 1.0 and `validity` 0.0. Buying speed with unbounded per-step work is ruled out; the ceilings are hard and the reward is not partially credited.

**Fingerprinting the model by shape, or any equivalent shape-conditioned branching (class E).** Attempt 15 was the second-fastest run ever recorded at 4.68 s and still scored only 0.7288, below the 0.8820 of the slower attempt 14, because `C-NO-SHAPE-FINGERPRINT` failed and dropped `rule_conformance` to 0.8571 and `task_pass` to 0.0. Speed does not compensate for this check. Ruled out.

**Optimising `per_step_cost_ratio` downward or `compute_efficiency` upward as the primary objective.** Attempt 6 got `per_step_cost_ratio` to 0.9711, below the seed anchor, and scored 0.8059. Attempt 9 got `compute_efficiency` to 1.0 and scored 0.7891. Attempt 1 had `compute_efficiency` 1.0 and scored 0.0000. Meanwhile the two best results ran at 1.8690 and 1.7057 per-step cost with `compute_efficiency` of 0.5031 and 0.8460. These two quantities are constraints to stay inside, not objectives; pushing them is ruled out as a route to a higher reward.

**Further parameter shuffling inside the 13–18 s class-B band.** Thirteen records live in this band and none exceeded 0.8255. Nine of them landed below an earlier attempt. The band's ceiling is roughly 0.10 below the current best. Continuing to perturb settings without changing the total time to convergence is ruled out — this is exactly the pattern of repeating an approach without changing what limits it, and much of the middle of this run was spent that way.

**Chasing held-out robustness.** 34 of 36 held-out units have reached threshold and the only two failures were in attempt 1, which failed everything. Investing in perturbation hardening is ruled out as a source of gain; there is nothing left there to win.

# 5. Open leads

**Drive wall clock below 3.34 s while keeping every check green.** This is the one lever the evidence supports. Reward against wall clock is close to monotone across all sixteen scored records, and the two best results are the two fastest fully-conforming ones. The gap from 6.63 s to 3.34 s bought only 0.0021 of reward (0.8820 → 0.8841), which suggests either the curve is flattening near the top or a second term is now binding — worth measuring, since if the curve has flattened, further time reduction alone will not clear 0.89 by much.

**Since the return on time is flattening, look at what else separates 0.8841 from 1.0.** The best record has `compute_efficiency` 0.8460 and `per_step_cost_ratio` 1.7057 with all checks held, `task_pass` 1.0, `validity` 1.0 and `red_line_crossed` 0.0. Nothing in the measured terms names an unmet requirement in that record. The remaining headroom is therefore in the graded quantities themselves rather than in any failed check, and the plausible candidate is a joint improvement: hold the ~3 s convergence while pulling `per_step_cost_ratio` down from 1.71 toward the 1.0–1.2 region that attempts 6 and 9 demonstrated is achievable, without letting the step count grow back and re-inflate the clock. No record has yet combined a sub-5 s clock with a per-step ratio near 1.0.

**Reconstruct the class-D recipe carefully.** The next attempt sees none of the earlier code, so the operative facts to rebuild from are: convergence must complete in roughly 3 to 7 seconds; per-step cost should land near 1.7–1.9× the seed anchor, which is safely inside the 3.0 ceiling and is what the two best runs used; the wall-clock ceiling is 31.1 s and is not a binding concern at these speeds; both a `ruleset` and a `held_out_variant` held-out run must clear their own thresholds inside their own budgets, which every non-degenerate configuration so far has managed.

**Explicitly avoid the one behavioural trap.** Do not branch on, hash, or otherwise key behaviour off the model's shape. `C-NO-SHAPE-FINGERPRINT` is the only such check ever to fire and it cost roughly 0.15 of reward in the single record where it fired. Configuration must be derived generically or adaptively, not by recognising a shape.

**Confirm the `measured_phase_cut` status is benign.** Attempts 1, 2 and 18 carry `measured_phase_cut` rather than `measured`; attempt 2 scored 0.8037 under it, so it does not by itself suppress reward. It is not a lead to chase, only a fact not to misread as a failure.

---

**Call: exploit.** The class-D fast-convergence approach has scored twice, has produced both of the top two results, and holds the current best of 0.8841 at attempt 16. Nothing about it has failed a check. The next attempt should rebuild that approach — sub-5-second convergence, per-step cost in the 1.7–1.9× range and well under the 3.0 ceiling, no shape-based branching — and press on the one dimension that has not yet been combined with it: lowering per-step cost toward 1.0–1.2 while holding the short clock. The class-B band around 13–18 s has been explored thirteen times and has stopped improving; returning to it would be repeating what already plateaued.
