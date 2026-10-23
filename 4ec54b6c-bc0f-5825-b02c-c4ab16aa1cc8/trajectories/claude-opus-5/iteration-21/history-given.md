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

    All four attempts since have scored lower than it.
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
  15 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 14 -- reward 0.8820, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 7
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

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (1, 13). Whatever has been
      changing between them is not what is causing it.
    C-NO-SHAPE-FINGERPRINT failed on attempt 15.
    C-PER-STEP-COST-CEILING failed on attempt 13.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty graded records were supplied. Every one carries a `measurement_status` of `measured` or `measured_phase_cut`, and every one carries a reward, so no record is unmeasured; the two zeros below are genuine measured zeros, not absent measurements.

Ranked worst to best by reward:

| Rank | Attempt | reward | wall_clock_sec / qualifying_budget | notes |
|---|---|---|---|---|
| 1 | 1 | 0.0000 | 89.9778 / not-measured | zero_reason_code 4; target never reached; conformance_fraction 0.0 |
| 2 | 13 | 0.0000 | 37.2022 / 37.2022 | zero_reason_code 1; red_line_crossed 1.0; validity 0.0 |
| 3 | 18 | 0.7140 | 18.2474 | measured_phase_cut, no failed checks |
| 4 | 15 | 0.7288 | 4.6808 | task_pass 0.0 despite target reached; rule_conformance 0.8571 |
| 5 | 10 | 0.7393 | 16.8995 | |
| 6 | 12 | 0.7443 | 16.9433 | |
| 7 | 17 | 0.7716 | 14.8440 | |
| 8 | 8 | 0.7843 | 16.5068 | |
| 9 | 9 | 0.7891 | 14.1599 | compute_efficiency 1.0000 |
| 10 | 19 | 0.7950 | 14.6918 | |
| 11 | 7 | 0.7994 | 14.1032 | |
| 12 | 11 | 0.7997 | 17.0029 | |
| 13 | 2 | 0.8037 | 13.4877 | first clean pass |
| 14 | 4 | 0.8042 | 13.6584 | 0.8041887, marked worse than an earlier attempt |
| 15 | 3 | 0.8042 | 13.6621 | 0.8042363 |
| 16 | 6 | 0.8059 | 13.4266 | per_step_cost_ratio 0.9711, the only sub-1.0 value |
| 17 | 5 | 0.8255 | 13.7398 | |
| 18 | 20 | 0.8298 | 6.3142 | |
| 19 | 14 | 0.8820 | 6.6280 | |
| 20 | 16 | **0.8841** | 3.3367 | best |

**Attempt 16 holds the highest reward, 0.8841, and it is the one to beat.** Attempt 14 (0.8820) is the closest runner-up.

Direction of movement, stated plainly and not softened: attempts 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19 and 20 are all marked `worse_than_an_earlier_attempt`. In particular attempt 20 (0.8298) is **lower** than attempt 14 (0.8820) that preceded it, attempt 13 scored 0.0000 and is **lower** than every scoring attempt before it, and attempt 15 (0.7288) is **lower** than attempt 14 immediately before it. Only attempts 2, 3, 5, 14 and 16 ever set a new best.

The dominant regularity in the measured terms is that reward tracks `wall_clock_sec` (which equals `qualifying_budget` in every qualifying record) far more strongly than any other supplied quantity. The 13–14 s cluster sits at 0.79–0.83; the 16–18 s cluster sits at 0.71–0.80; the 3–7 s cluster sits at 0.83–0.88. It is not a pure function of wall clock: attempts 14 (6.6280 s) and 20 (6.3142 s) have near-identical budgets but rewards of 0.8820 and 0.8298, a gap of 0.05 that none of the supplied terms explains. `compute_efficiency` and `per_step_cost_ratio` do not predict reward at all — attempt 9 had `compute_efficiency` 1.0000 and scored 0.7891, while attempt 16 had 0.8460 and scored 0.8841; attempt 6 had the cheapest per-step cost ever recorded (0.9711× the seed anchor) and scored only 0.8059.

# 2. Approach classes tried

I was given measured terms only, not source, so these classes are grouped by their metric signature. Two records with the same signature are one entry.

**A. Non-converging baseline (attempt 1).** Ran 89.9778 s, produced no evaluation row crossing the threshold in the declared direction, `conformance_fraction` 0.0, both perturbation units failed. Reward 0.0000, zero_reason_code 4. This is the only attempt that never reached the primary target.

**B. Mid-budget conforming solver, ~13.4–14.9 s (attempts 2, 3, 4, 5, 6, 7, 9, 17, 19).** All clean: no failed checks, `rule_conformance` 1.0, both perturbations held, `red_line_crossed` 0. Rewards 0.7716–0.8255. This class was worked repeatedly with small variations in cost profile — `per_step_cost_ratio` was pushed across the range 0.9711 (attempt 6) to 1.5958 (attempt 7) and `compute_efficiency` across 0.5487 (attempt 17) to 1.0000 (attempt 9) — and the reward band barely moved, staying inside roughly 0.05. Attempt 5 (0.8255, efficiency 0.7476, per-step 1.2599) is the best member.

**C. Longer-budget conforming solver, ~16.5–18.2 s (attempts 8, 10, 11, 12, 18).** Same clean check profile, rewards 0.7140–0.7997. Strictly worse than class B on average. Attempt 18 (18.2474 s, 0.7140) is the worst scoring record that passed all checks.

**D. Heavy per-step variant (attempt 13).** Reached the primary target and both perturbations held, but spent 37.2022 s against a declared wall-clock ceiling of 31.1 and ran at 7.185× the seed per-step anchor against a ceiling of 3.0. `red_line_crossed` 1.0, `validity` 0.0, `task_pass` 0.0, reward 0.0000, zero_reason_code 1. This is the only record that shows what the ceilings actually are.

**E. Fast conforming solver, 3.3–6.6 s (attempts 14, 16, 20).** `per_step_cost_ratio` 1.5111–1.8731, `compute_efficiency` 0.5031–0.9565, all checks clean, both perturbations held. Rewards 0.8298 (attempt 20), 0.8820 (attempt 14), 0.8841 (attempt 16). This class contains the two best results and is the productive one.

**F. Shape-fingerprinting shortcut (attempt 15).** Fastest of all at 4.6808 s and both perturbations held, but the verifier found that the submission fingerprints the model by shape. `rule_conformance` dropped to 0.8571 (6 of 7 conformance rules), `task_pass` fell to 0.0, and the reward came in at 0.7288 — below every clean member of class E despite being faster than two of them. Speed bought by shape-conditioning is paid back with interest.

# 3. Checks that failed

**C-TARGET-REACHED** — attempt 1, primary evaluation: "no evaluation row crosses the threshold in the declared direction". It also failed inside both of attempt 1's perturbation units. Counting the primary and the two held-out runs, this identifier failed three times, all within attempt 1, and has not failed since.

**C-BUDGET-RESPECTED** — failed in two separate attempts, for two different reasons. In attempt 1: "no qualifying row, so no budget position exists" — a consequence of there being no target-reaching row at all. In attempt 13: "the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1". It also failed in both of attempt 1's perturbation units. This is the check that has now failed in more than one record — twice at the primary level, plus twice more inside attempt 1's held-out runs, four failures in total. Whatever was changed between attempt 1 and attempt 13 is not what causes C-BUDGET-RESPECTED: the two failures have unrelated causes, one from having no qualifying row and one from a real 37.2022 s overrun of the 31.1 ceiling, so there is no single edit connecting them.

**C-PERTURBATION-REACHED** — attempt 1: "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed once.

**C-PER-STEP-COST-CEILING** — attempt 13: "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0". Failed once. This fixes the ceiling at 3.0× the seed anchor; every other attempt sat between 0.9711 and 1.8731, comfortably inside it.

**C-LOG-WELL-FORMED** — failed once, inside a perturbation run of attempt 1 (ruleset kind). No reason string was supplied for perturbation-level checks.

**C-NO-LATCH-CARRYOVER** — failed once, inside the same ruleset perturbation run of attempt 1.

**C-NO-SHAPE-FINGERPRINT** — attempt 15: "the submission fingerprints the model by shape". Failed once. It cost `rule_conformance` (0.8571, i.e. 6 of 7) and `task_pass` (0.0) while leaving the reward nonzero at 0.7288.

**Perturbation-unit outcomes.** Each attempt declared 2 perturbations, one of kind `ruleset` and one of kind `held_out_variant`, giving 40 held-out runs across the 20 records. 38 reached their threshold. The 2 failures both occurred in attempt 1. By kind: the `ruleset` kind failed once, stopped by C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER; the `held_out_variant` kind failed once, stopped by C-TARGET-REACHED and C-BUDGET-RESPECTED. Since attempt 2, `all_perturbations_held` has been true in every record, including attempts 13 and 15 whose primary runs failed checks — the perturbation runs are not currently the binding constraint, and the runs are not identified across records, so nothing here should be read as the same run recurring.

# 4. Ruled-out directions

**Spending more wall clock (class C, 16.5–18.2 s).** Five records in this band scored 0.7140–0.7997, all below the class B mid-band and far below the 3–7 s band. Every one is marked `worse_than_an_earlier_attempt`. More budget does not buy reward.

**Very heavy per-step computation (class D, attempt 13).** 7.185× the seed anchor against a hard ceiling of 3.0, and 37.2022 s against a hard ceiling of 31.1. Result: `red_line_crossed` 1.0, `validity` 0.0, reward 0.0000. Any design whose per-step cost exceeds 3.0× the anchor or whose qualifying row exceeds 31.1 s is dead on arrival regardless of how good the model is.

**Shape fingerprinting the model (attempt 15).** Explicitly caught by C-NO-SHAPE-FINGERPRINT, dropped `rule_conformance` to 0.8571 and `task_pass` to 0.0, and produced 0.7288 — worse than every clean fast run despite being the second-fastest record. Do not branch on, hash, or dispatch by parameter/tensor shape anywhere in the submission.

**Minimising `per_step_cost_ratio` as a proxy objective.** Attempt 6 achieved 0.9711, the only value below the seed anchor, and scored 0.8059 — below attempts 14, 16 and 20, which all ran at 1.51–1.87. The reward does not reward cheap steps; it rewards finishing early. Likewise **maximising `compute_efficiency`**: attempt 9 hit 1.0000 and scored 0.7891, while the best result (attempt 16) sat at 0.8460 and attempt 14 at 0.5031. Neither term is the objective.

**Further small perturbations of the 13–14 s class B configuration.** Nine records explored this band across a wide spread of efficiency and per-step cost and produced a reward range of only 0.7716–0.8255, topping out 0.06 below the current best. The class has stopped improving.

**Treating the perturbation runs as the problem.** They have held in 19 of 20 records and in 38 of 40 individual runs; the two failures were both collateral from the attempt-1 baseline that never reached its target at all. Effort spent hardening against the `ruleset` or `held_out_variant` runs is not where the reward is.

# 5. Open leads

**Drive the qualifying budget below 3.3367 s while keeping all seven conformance rules clean.** This is the single strongest signal in the data: reward improves monotonically across the budget bands 16–18 s → 13–15 s → 6.3–6.6 s → 3.3 s, and the best record is also the fastest clean one. The ceilings give plenty of headroom for aggressive early stopping: the wall-clock ceiling is 31.1 s and the per-step ceiling is 3.0× the seed anchor, while attempt 16 used 3.3367 s at 1.7057×. Buying speed by raising per-step cost up to roughly 2.5× the anchor is legal and untested — the highest ratio ever measured in a clean run is 1.8731.

**Find the residual quality term.** Attempts 14 and 20 have nearly identical budgets (6.6280 s vs 6.3142 s) and rewards 0.8820 vs 0.8298. That 0.05 gap is not explained by `compute_efficiency` (0.5031 vs 0.9565), `per_step_cost_ratio` (1.8690 vs 1.5111), conformance, validity or perturbations, all of which are equal or favour the lower-scoring run. Something in the model's own performance margin above the threshold is being scored. Reaching the target with more headroom, rather than just reaching it, is likely worth more than shaving another second, and is worth an explicit experiment: hold the attempt-16 budget and push accuracy/margin.

**Stop as soon as the threshold is crossed with margin, rather than running a fixed schedule.** The `qualifying_budget` equals `wall_clock_sec` in every record, meaning the whole run is being charged. An explicit convergence check that terminates the moment the declared-direction threshold is met — with a small safety margin to keep both the `ruleset` and `held_out_variant` runs reaching, since those must still hold — would convert the class B and C configurations into class E ones without changing the learner.

**Guard the two hard ceilings defensively.** A cheap wall-clock watchdog well under 31.1 s and a per-step cost cap well under 3.0× the anchor would make an attempt-13-style zero structurally impossible while costing nothing when the run is already fast.

**Re-verify the shape-fingerprint rule is not reintroduced.** `rule_conformance` 0.8571 corresponds to 6 of 7 rules; only C-NO-SHAPE-FINGERPRINT has ever been named among them, so six conformance rules remain unnamed and unbroken. Speed optimisations that specialise on tensor dimensions are exactly the kind of change likely to trip it again.

**Call: exploit.** Take attempt 16 — the 0.8841 record, 3.3367 s, `per_step_cost_ratio` 1.7057, `compute_efficiency` 0.8460, all checks clean, both perturbations held — and push it on the two levers the data supports: a shorter qualifying budget, and a larger margin over the threshold at that budget. Class E has not stopped improving (it produced the two highest rewards on record), so a structural change is not yet warranted. What must not be repeated is attempt 13's ceiling breach or attempt 15's shape fingerprint: those are the two ways this work has scored zero or gone backwards, and rerunning either without removing its cause would be neither exploring nor exploiting. Earlier work did repeatedly rework the 13–14 s configuration for nine records without moving the band, and that pattern should not continue.
