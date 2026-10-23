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

    All six attempts since have scored lower than it.
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
  22       0.0000   1.000             2 of 2         yes             6                 

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
  17 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 14 -- reward 0.8820, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 7
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

All twenty-two graded records carry `measurement_status` of `measured` or `measured_phase_cut`, so every one of them produced a reward. None is missing a measurement. Ordered worst to best:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 | 1 | 0.0000 | zero_reason_code 4; primary target never reached; validity 1.0 but task_pass 0 |
| 1 | 13 | 0.0000 | zero_reason_code 1; red_line_crossed 1.0; validity 0.0 |
| 1 | 22 | 0.0000 | zero_reason_code 1; red_line_crossed 1.0; validity 0.0 |
| 4 | 21 | 0.4094 | conformance_fraction 0.5; one held-out run missed its budget |
| 5 | 18 | 0.7140 | 18.25 s wall clock |
| 6 | 15 | 0.7288 | rule_conformance 0.857; task_pass 0 |
| 7 | 10 | 0.7393 | 16.90 s |
| 8 | 12 | 0.7443 | 16.94 s |
| 9 | 17 | 0.7716 | 14.84 s |
| 10 | 8 | 0.7843 | 16.51 s |
| 11 | 9 | 0.7891 | 14.16 s, compute_efficiency 1.0 |
| 12 | 19 | 0.7950 | 14.69 s |
| 13 | 7 | 0.7994 | 14.10 s |
| 14 | 11 | 0.7997 | 17.00 s |
| 15 | 2 | 0.8037 | 13.49 s |
| 16 | 4 | 0.8042 | 13.658 s (0.8041887; fractionally below attempt 3) |
| 17 | 3 | 0.8042 | 13.662 s (0.8042363) |
| 18 | 6 | 0.8059 | 13.43 s, per_step_cost_ratio 0.971 |
| 19 | 5 | 0.8255 | 13.74 s |
| 20 | 20 | 0.8298 | 6.31 s, compute_efficiency 0.9565 |
| 21 | 14 | 0.8820 | 6.63 s, compute_efficiency 0.5031 |
| 22 | **16** | **0.8841** | **3.34 s, per_step_cost_ratio 1.706 — highest reward recorded** |

**Attempt 16 holds the highest reward at 0.8841 and is the one to beat.** Attempt 14 (0.8820) is the only other result within 0.01 of it.

Several later attempts are plainly worse than earlier ones, and `standing_against_best_so_far` says so directly rather than describing progress. Attempts 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21 and 22 are each recorded as `worse_than_an_earlier_attempt`. In particular: attempt 22 (0.0000) is a regression to zero from attempt 20 (0.8298) and from the best (0.8841); attempt 21 (0.4094) is the worst non-zero result on record and a large drop; attempt 13 (0.0000) is a regression from attempt 12 (0.7443). Only attempts 2, 3, 5, 14 and 16 ever set a new best.

# 2. Approach classes tried

The submission source is not carried forward, so these classes are inferred from the measured signatures (wall clock, per-step cost ratio, compute efficiency, failed checks). Twenty-two records collapse into six distinct approaches.

**A. Non-converging cheap-step baseline (attempt 1).** per_step_cost_ratio 1.019 — essentially the seed anchor's per-step cost — and compute_efficiency 1.0, meaning budget went unused, yet no evaluation row ever crossed the primary threshold in the declared direction. Both held-out runs also failed, and the ruleset run additionally failed log well-formedness and latch carryover. Reward 0.0000. This class produces no qualifying row at all, so no budget position and no partial credit.

**B. Slow conforming trainers, ~13.4–18.3 s wall clock (attempts 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 19).** Fully conforming: conformance_fraction 1.0, rule_conformance 1.0, no failed checks, both perturbation runs reaching threshold, task_pass 1.0. per_step_cost_ratio ranged 0.971–1.596, compute_efficiency 0.503–1.0. Rewards span 0.7140–0.8255. Within this family reward tracks wall clock closely: the 13.4–13.8 s cluster returns 0.8037–0.8255, the 14.1–14.8 s cluster 0.7716–0.7994, the 16.5–17.0 s cluster 0.7393–0.7997, and 18.25 s returns 0.7140. This is the plateau family; its ceiling is 0.8255 and it never approached the best.

**C. Fast conforming trainers, ~3.3–6.6 s (attempts 14, 16, 20).** Same clean conformance profile as class B — no failed checks, both perturbation runs reached, task_pass 1.0 — but with wall clock cut by half to a quarter. per_step_cost_ratio 1.511–1.869, i.e. per-step cost was allowed to rise well above the anchor in exchange for far fewer total seconds. Rewards 0.8298 (6.31 s), 0.8820 (6.63 s) and 0.8841 (3.34 s). This class contains every result above 0.826 and is where the best sits.

**D. High per-step-cost variants (attempts 13, 22).** per_step_cost_ratio 7.185 and 7.259 against a declared ceiling of 3.0. Both crossed the red line, both scored validity 0.0, task_pass 0.0, reward 0.0000. Notably the two differ enormously in wall clock — 37.20 s versus 6.39 s — and in compute_efficiency (0.580 versus 0.153), yet their per-step ratios are nearly identical at ~7.2×. Attempt 13 additionally overran the wall-clock ceiling; attempt 22 stayed inside it and still zeroed on cost alone.

**E. Shape-fingerprinting shortcut (attempt 15).** Fast (4.68 s), per_step_cost_ratio 1.873, both perturbation runs reached, compute_efficiency 0.871 — a profile close to class C — but the verifier found the submission fingerprints the model by shape. rule_conformance dropped to 0.857, task_pass fell to 0.0, and reward landed at 0.7288, below every clean class-C result and below most of the slow class-B results.

**F. Perturbation-fragile long run (attempt 21).** Primary target reached at 24.25 s, per_step_cost_ratio 1.220, primary checks otherwise fine, but only one of the two declared perturbations reached its own threshold inside its own budget. conformance_fraction 0.5, task_pass 0.0, reward 0.4094. Reaching the primary target is not sufficient; the held-out runs carry roughly half the credit.

# 3. Checks that failed

Named checks that did not hold, with the verifier's own reasons:

- **C-PER-STEP-COST-CEILING** — failed twice, on attempts 13 and 22. Reasons: "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0" and "per-step cost is 7.259 times the seed anchor, above the ceiling of 3.0". This is the most important repeated finding. Between those two attempts the wall clock changed from 37.20 s to 6.39 s and compute_efficiency from 0.580 to 0.153, yet the ratio barely moved (7.185 → 7.259). Whatever was changed between them is not what is causing this failure. The cost is per *step*, not per run: shortening the run does not touch it. Something structural in the step — extra passes, extra evaluations, or extra work folded into each optimizer step — is ~7.2× the seed anchor's step and must be removed, not merely run for less time. Both failures zeroed the reward via red_line_crossed and validity 0.0.
- **C-BUDGET-RESPECTED** — failed on the primary axis twice, on attempts 1 and 13. Attempt 1: "no qualifying row, so no budget position exists" (a consequence of never reaching the target). Attempt 13: "the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1". It also failed inside held-out runs, described below.
- **C-PERTURBATION-REACHED** — failed twice, on attempts 1 and 21. Reasons: "0 of 2 declared perturbations reached their own threshold inside their own budget" and "1 of 2 declared perturbations reached their own threshold inside their own budget". The change made between those attempts did fix the ruleset side but not the whole check.
- **C-TARGET-REACHED** — failed once on the primary axis, attempt 1: "no evaluation row crosses the threshold in the declared direction".
- **C-NO-SHAPE-FINGERPRINT** — failed once, attempt 15: "the submission fingerprints the model by shape". This alone dropped rule_conformance to 0.857 and task_pass to 0 despite an otherwise strong 4.68 s profile.
- **C-LOG-WELL-FORMED** — failed once, inside a ruleset perturbation run on attempt 1.
- **C-NO-LATCH-CARRYOVER** — failed once, inside a ruleset perturbation run on attempt 1.

Held-out run outcomes (`perturbation_units`). Every record declared two units, one of kind `ruleset` and one of kind `held_out_variant`; the runs are not identified beyond their kind, so no claim is made here about any one of them being the same run across records. In aggregate, 41 of 44 units reached their threshold.

- **ruleset runs:** 21 of 22 reached. The single failure was on attempt 1, where it failed C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER. Every subsequent record's ruleset run reached.
- **held_out_variant runs:** 20 of 22 reached. Two failures: on attempt 1, failing C-TARGET-REACHED and C-BUDGET-RESPECTED; and on attempt 21, failing C-BUDGET-RESPECTED alone. The held_out_variant kind is therefore the fragile one — it is the kind that failed most recently and the one whose failure mode is a budget overrun rather than a convergence failure. Attempt 21's primary run took 24.25 s, and at that scale the variant run could not finish inside its own budget.

# 4. Ruled-out directions

- **Raising per-step compute to roughly 7× the seed anchor.** Ruled out: C-PER-STEP-COST-CEILING fails at a hard ceiling of 3.0, red_line_crossed goes to 1.0, validity to 0.0 and reward to exactly 0.0000. Attempts 13 and 22 both died here. Anything that multiplies work inside a step (extra forward/backward passes, per-step full evaluations, per-step heavy bookkeeping) must be assumed to hit this.
- **Fixing a per-step-cost violation by shortening the run.** Ruled out by the 13→22 pair: wall clock fell from 37.20 s to 6.39 s and the ratio stayed at ~7.2. The ceiling is measured per step against a seed anchor and is invariant to run length.
- **Wall clock above ~16 s.** Ruled out on reward grounds: every record at or above 16.5 s scored 0.7140–0.7997, all below the 13-second cluster and far below the 3–7 second cluster. There is a clean monotone penalty for time-to-target.
- **Wall clock above ~24 s.** Ruled out on conformance grounds as well as reward: at 24.25 s (attempt 21) the held_out_variant run failed C-BUDGET-RESPECTED, conformance_fraction halved and reward collapsed to 0.4094 even though the primary target was reached.
- **Fingerprinting the model by shape.** Ruled out: C-NO-SHAPE-FINGERPRINT is checked directly, and attempt 15 forfeited task_pass and 14% of rule_conformance for it, scoring 0.7288 despite being the third-fastest run recorded. Any branching on parameter shapes, layer counts, or tensor dimensions to select hyperparameters is off the table.
- **Driving per-step cost below the anchor while leaving the run long.** Ruled out: attempt 6 achieved per_step_cost_ratio 0.971 — cheaper per step than the seed — with compute_efficiency 0.9465, and still only scored 0.8059 at 13.43 s. Cheap steps are not rewarded; short total time is. The best result (attempt 16) has a per-step ratio of 1.706, well above 1, and still wins.
- **Further micro-tweaking inside the 13.4–14.8 s family.** Ruled out as exhausted: fourteen records live in the 13–18 s band, its best is 0.8255 and its rewards are noisy at the fourth decimal (attempts 3 and 4 both round to 0.8042, differing by 0.00005 across near-identical 13.66 s runs). Differences of that size are run-to-run noise, not signal, and the whole family is capped ~0.06 below the best.
- **The attempt-1 configuration.** Ruled out: it never produced a qualifying row, so C-TARGET-REACHED, C-BUDGET-RESPECTED and C-PERTURBATION-REACHED all failed together and the reward was 0.0000. Cheap steps that never cross the threshold earn nothing; the target must be crossed before any budget or efficiency term matters.

# 5. Open leads

- **Rebuild attempt 16's profile and push the wall clock below 3.34 s.** Its measured signature is the template to aim at: wall_clock_sec 3.337, qualifying_budget 3.337, per_step_cost_ratio 1.706, compute_efficiency 0.846, conformance_fraction 1.0, both perturbation runs reached, no failed checks, reward 0.8841. Time-to-target is the dominant lever across the whole record set; the fast family (3.3–6.6 s) holds the top three rewards and the slow family holds none of them. Reaching the threshold sooner — fewer total steps, more aggressive learning rate schedule, earlier stopping the moment the threshold is crossed — is the highest-value change, provided per_step_cost_ratio stays comfortably under 3.0.
- **Explain and exploit the attempt-14 / attempt-20 residual.** Attempt 20 ran faster (6.314 s vs 6.628 s) and used far more of its per-step allowance efficiently (compute_efficiency 0.9565 vs 0.5031), yet scored *lower* (0.8298 vs 0.8820). Wall clock alone does not order these two, so there is a second term in play — plausibly how far past the threshold the qualifying row sits, or the number of steps taken. This is worth probing deliberately: run the same schedule at two step counts and see which direction the residual moves. Do not guess at the mechanism in code; measure it.
- **Trade per-step cost for step count, up to but not near the ceiling of 3.0.** The best results sit at ratios 1.51–1.87. There is headroom to roughly 3.0, and the record shows that spending more per step to take fewer steps has paid (class C beats class B). A ratio target of ~2.0–2.5 with a correspondingly shorter run is unexplored territory between the winning family and the 7.2× disasters. Keep a wide margin: the only two attempts that exceeded the ceiling did so by more than a factor of two, so the failure mode is a cliff, not a gradient.
- **Recover attempt 15's speed without the fingerprint.** Attempt 15 reached its target in 4.68 s with both perturbation runs holding, and its only defect was C-NO-SHAPE-FINGERPRINT. If its speed came from its schedule rather than from shape-conditional dispatch, that schedule is worth re-running with all decisions made from shape-agnostic signals — loss values, gradient norms, step index, elapsed time — and none from parameter dimensions.
- **Protect the held_out_variant run explicitly.** It is the kind that has failed most recently and it failed on C-BUDGET-RESPECTED, at a primary wall clock of 24.25 s. Every attempt whose primary run finished under about 18 s had both perturbation kinds reach. Staying in the 3–7 s band is itself the mitigation, but the algorithm should not assume the variant run enjoys the same convergence speed as the primary — leave slack rather than tuning the step count to the primary's exact threshold crossing.
- **Hold the two cheap invariants that failed only once.** C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER each failed only inside attempt 1's ruleset run and have held ever since, but they cost nothing to preserve: emit well-formed evaluation rows on every run, and reset all optimizer/scheduler/adaptive state between runs so nothing latches from one run into the next.

**Verdict: exploit.** The scoring family is identified and still improving — attempt 16 (0.8841) improved on attempt 14 (0.8820) which improved on everything before it, and the improvement came from cutting wall clock roughly in half within the same conforming design. The right move is to rebuild the fast conforming trainer of attempt 16 and shorten time-to-target further while holding per_step_cost_ratio under 3.0, avoiding any shape-conditional logic, and keeping both perturbation runs inside their own budgets. It is worth naming the pattern that has repeatedly wasted attempts: reaching for extra per-step compute produced a reward of exactly 0.0000 twice, on attempts 13 and 22, with essentially the same 7.2× ratio both times and nothing between them addressing the cost of the step itself. Do not make that move a third time without first cutting the per-step work.
