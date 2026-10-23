# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.8255, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
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
  5 *      0.8255   1.000             2 of 2         yes             14                
  6        0.8059   1.000             2 of 2         yes             13                
  7        0.7994   1.000             2 of 2         yes             14                
  8        0.7843   1.000             2 of 2         yes             17                
  9        0.7891   1.000             2 of 2         yes             14                
  10       0.7393   1.000             2 of 2         yes             17                
  11       0.7997   1.000             2 of 2         yes             17                

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
  5 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 3 -- reward 0.8042, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 6 -- reward 0.8059, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 13
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.7891, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 10 -- reward 0.7393, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.7997, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Eleven graded submissions, all of which carry a `reward`. Listed worst to best:

| Rank | Attempt | reward | measurement_status | Notes |
|---|---|---|---|---|
| 1 (worst) | Attempt 1 | 0.0000 | measured_phase_cut | `zero_reason_code` 4; `task_pass` 0, `conformance_fraction` 0, three failed checks, neither perturbation run reached |
| 2 | Attempt 10 | 0.7393 | measured | worse than an earlier attempt |
| 3 | Attempt 8 | 0.7843 | measured | worse than an earlier attempt |
| 4 | Attempt 9 | 0.7891 | measured | worse than an earlier attempt |
| 5 | Attempt 7 | 0.7994 | measured | worse than an earlier attempt |
| 6 | Attempt 11 | 0.7997 | measured | worse than an earlier attempt (the most recent attempt, and it is below the best) |
| 7 | Attempt 2 | 0.8037 | measured_phase_cut | first passing attempt; best at the time |
| 8 | Attempt 4 | 0.8042 (0.8041887) | measured | worse than an earlier attempt |
| 9 | Attempt 3 | 0.8042 (0.8042363) | measured | best at the time |
| 10 | Attempt 6 | 0.8059 | measured | worse than an earlier attempt |
| 11 (best) | **Attempt 5** | **0.8255** | measured | best of every attempt |

**Attempt 5, reward 0.8255, is the highest score recorded and is the one to beat.**

Every record produced a measurement; none is missing. Attempts 1 and 2 are flagged `measured_phase_cut` rather than plain `measured`, but both still carry a reward and are reported at their numbers. Attempt 1's 0.0000 is a genuine measured zero (zero_reason_code 4, task_pass 0), not an absent measurement.

Supporting terms worth carrying forward, because they are the only visible axes on which the passing attempts differ:

| Attempt | reward | wall_clock_sec / qualifying_budget | per_step_cost_ratio | compute_efficiency |
|---|---|---|---|---|
| 1 | 0.0000 | 89.978 / not-measured | 1.0194 | 1.000 |
| 10 | 0.7393 | 16.899 | 1.0702 | 0.836 |
| 8 | 0.7843 | 16.507 | 1.4960 | 0.624 |
| 9 | 0.7891 | 14.160 | 1.1920 | 1.000 |
| 7 | 0.7994 | 14.103 | 1.5958 | 0.558 |
| 11 | 0.7997 | 17.003 | 1.4791 | 0.627 |
| 2 | 0.8037 | 13.488 | 1.4966 | 0.620 |
| 4 | 0.8042 | 13.658 | 1.4974 | 0.584 |
| 3 | 0.8042 | 13.662 | 1.5320 | 0.605 |
| 6 | 0.8059 | 13.427 | 0.9711 | 0.946 |
| 5 | **0.8255** | 13.740 | 1.2599 | 0.748 |

For attempts 2–11 every gate term is saturated: `task_pass` 1.0, `validity` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `red_line_crossed` 0.0, `primary_target_reached` 1.0, `all_perturbations_held` true, `failed_checks` empty. The entire 0.7393–0.8255 spread therefore comes from graded quantities that are *not* the pass/fail gates — and, importantly, it is not explained by wall clock or `compute_efficiency` alone (attempt 11 at 17.003 s scored 0.7997 while attempt 10 at 16.899 s scored 0.7393; attempt 9 at `compute_efficiency` 1.000 scored 0.7891, well below attempt 5 at 0.748). Treat differences below roughly 0.005 as indistinguishable — attempts 3 and 4 differ by 0.00005 — and treat attempt 5's ~0.02 lead over the 0.80 cluster as the only genuinely separated result.

# 2. Approach classes tried

Only measured terms were supplied, not source, so these classes are grouped by their metric fingerprints. Each is described so the operating point can be re-derived and re-aimed at.

**Class A — non-conforming baseline (attempt 1).** Ran ~90 s wall clock, never produced an evaluation row crossing the threshold, and emitted a malformed log on the ruleset perturbation run with latch state carried across runs. `per_step_cost_ratio` 1.0194 and `compute_efficiency` 1.0, i.e. it was cheap per step but simply never converged and never wrote a qualifying row. Scored 0.0000. This class is dead and must not be repeated unchanged.

**Class B — the conforming ~13.5 s / high-per-step-cost cluster (attempts 2, 3, 4).** Wall clock 13.49–13.66 s, `per_step_cost_ratio` ≈1.50–1.53, `compute_efficiency` 0.58–0.62. Rewards 0.8037, 0.8042, 0.8042 — mutually indistinguishable. This is the reproducible, safe baseline: it passes every check and lands just above 0.80.

**Class C — moderate per-step cost, moderate efficiency (attempt 5).** Wall clock 13.740 s, `per_step_cost_ratio` 1.2599, `compute_efficiency` 0.748. Reward 0.8255, the best result. Relative to Class B it cut per-step cost by roughly a sixth and lifted efficiency by roughly a fifth while keeping wall clock essentially unchanged, and gained ~0.021 reward. This is the single most valuable configuration recorded.

**Class D — per-step cost pushed to or below parity (attempts 6 and 10).** Attempt 6: `per_step_cost_ratio` 0.9711, `compute_efficiency` 0.946, wall clock 13.427 s (the fastest passing run), reward 0.8059 — better than Class B but *below* attempt 5 despite dominating it on both cost ratio and efficiency. Attempt 10: `per_step_cost_ratio` 1.0702, `compute_efficiency` 0.836, but wall clock 16.899 s, reward 0.7393 — the worst passing result of all. This class demonstrates that driving per-step cost toward or under 1.0 does not by itself buy reward, and when it comes with a wall-clock blowout it costs a lot.

**Class E — efficiency maximised (attempt 9).** `compute_efficiency` 1.000, `per_step_cost_ratio` 1.1920, wall clock 14.160 s, reward 0.7891. Saturating `compute_efficiency` produced a *worse* score than attempt 5's 0.748. Efficiency is clearly not the reward.

**Class F — longer / more expensive runs (attempts 7, 8, 11).** `per_step_cost_ratio` 1.48–1.60 with wall clocks 14.10, 16.51 and 17.00 s; rewards 0.7994, 0.7843, 0.7997. All below the Class B baseline and well below attempt 5. Extending the run at Class B's cost profile does not help.

Cross-class reading: the two configurations that beat 0.805 (attempts 5 and 6) both kept wall clock under ~13.75 s *and* pulled `per_step_cost_ratio` below the ~1.50 of the baseline cluster. Every attempt whose wall clock exceeded ~14.2 s scored at or below 0.7997, regardless of its cost ratio. Neither wall clock nor cost ratio nor efficiency predicts reward on its own; the surviving hypothesis consistent with all eleven records is that reward mixes a solution-quality term with a cost term, and that attempt 5 found a better quality/cost balance than either the cheap-and-efficient extreme (attempts 6, 9, 10) or the expensive extreme (attempts 7, 8, 11).

# 3. Checks that failed

All failures are confined to attempt 1. Attempts 2 through 11 have empty `failed_checks` on the primary run and on both perturbation runs.

Attempt 1, primary run:
- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction".
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". This is a downstream consequence of the above: with no qualifying row, `qualifying_budget` was reported as "not-measured".
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget".

Attempt 1, perturbation runs:
- The **ruleset** run failed **C-LOG-WELL-FORMED**, **C-TARGET-REACHED**, **C-BUDGET-RESPECTED** and **C-NO-LATCH-CARRYOVER**.
- The **held_out_variant** run failed **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**.

Repetition within that record matters: **C-TARGET-REACHED failed three times in attempt 1** — on the primary run and on both perturbation runs — and **C-BUDGET-RESPECTED likewise failed three times**, in each case for the same reason (no qualifying row exists). That pattern says the failure was global to the training procedure, not specific to any perturbation. **C-LOG-WELL-FORMED** and **C-NO-LATCH-CARRYOVER** failed once each, and only on a ruleset-kind run; those two are the perturbation-specific defects — a log the harness could not parse, and state latched from a prior run leaking into it.

No check has failed in any attempt after the first, so whatever was changed between attempt 1 and attempt 2 is what fixed all five named checks; nothing since has re-broken them. There is no check that recurs across records, and therefore no standing conformance bug to chase — the remaining problem is score magnitude, not conformance.

# 4. Ruled-out directions

- **Whatever attempt 1 did (Class A).** Ruled out: measured reward 0.0000 with five distinct checks failing, including a training run that never crossed the target threshold in ~90 s of wall clock, a malformed log on a ruleset run, and latched state carried across runs. Do not re-run this shape.
- **Maximising `compute_efficiency` as the objective.** Ruled out by attempt 9: `compute_efficiency` = 1.000, the theoretical maximum, produced reward 0.7891 — **lower** than attempt 5's 0.8255 at efficiency 0.748 and lower even than the 0.8037–0.8042 baseline cluster. Efficiency is not the graded quantity.
- **Minimising `per_step_cost_ratio` as the objective.** Ruled out by attempts 6 and 10: cost ratios 0.9711 and 1.0702, both far below attempt 5's 1.2599, yielded 0.8059 and 0.7393 respectively. Attempt 6 in particular beat attempt 5 on wall clock, on cost ratio and on efficiency simultaneously, and still scored 0.0196 lower. Cheapening the step is not sufficient.
- **Spending more wall clock at the Class B cost profile (Class F).** Ruled out: attempts 8 and 11 ran 16.51 s and 17.00 s at cost ratios ~1.48–1.50 and returned 0.7843 and 0.7997, both below the 13.5 s versions of the same profile (0.8037/0.8042). Attempt 7 at 14.10 s and cost ratio 1.5958 gave 0.7994, also below. Longer runs at this profile lose reward.
- **Re-running the Class B baseline expecting improvement.** Ruled out as a *goal*: three records (attempts 2, 3, 4) landed at 0.8037, 0.8042, 0.8042 — a spread of 0.0005, i.e. noise. It is a reliable floor above 0.80 but it has stopped improving and cannot reach 0.8255 by repetition.
- **Reading tiny reward deltas as signal.** Ruled out: attempts 3 and 4 differ by 0.00005 with materially different `compute_efficiency` (0.605 vs 0.584). Any change judged by a sub-0.005 delta is unverifiable.

# 5. Open leads

1. **Reconstruct attempt 5's operating point and hold it.** It is the only configuration to clear 0.81. Its signature is: wall clock ≈13.74 s, `qualifying_budget` ≈13.74, `per_step_cost_ratio` ≈1.26, `compute_efficiency` ≈0.75, all checks clean, both perturbation runs reaching. Since the next attempt starts from a pristine stub with no sight of prior code, aim explicitly at that fingerprint rather than at any remembered code detail, and verify the four numbers before considering anything else. Reproducing 0.8255 is the first order of business; beating it is the second.
2. **Search the narrow band between attempt 5 and attempt 6, not outside it.** The two best results bracket `per_step_cost_ratio` in [0.97, 1.26] and `compute_efficiency` in [0.75, 0.95], with wall clock in [13.43, 13.74]. Reward is non-monotone across that bracket (0.8059 at the cheap end, 0.8255 in the middle), which means there is an interior optimum that has not been mapped. Try cost ratios around 1.10–1.20 with wall clock held near 13.5–13.7 s.
3. **Keep wall clock under ~13.8 s as a hard self-imposed constraint.** Every record above 14.1 s scored ≤0.7997; every record above 0.805 was under 13.75 s. This is the strongest single regularity in the data and is cheap to enforce.
4. **Identify the unexposed quality term.** No exposed metric explains why attempt 5 (0.8255) beats attempt 6 (0.8059) when attempt 6 dominates it on every visible cost axis. The residual must be solution quality — how far past the threshold the evaluation rows go, or the margin at which the perturbation runs clear their own thresholds. Log and inspect the achieved metric relative to the declared threshold, and try trading a little cost back for a larger margin, which is precisely the direction attempt 5 sits in relative to attempt 6.
5. **Do not economise on the conformance machinery.** The ruleset-kind perturbation run is the one that historically broke C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER. Whatever the stub needs for a well-formed log and for resetting all latched state between runs must be reinstated from scratch, since the stub is pristine; twenty of twenty perturbation runs have held since attempt 2, and losing that would cost the whole score, not a fraction of it.
6. **Perturbation status, for reference.** Two perturbation runs per record, one of `ruleset` kind and one of `held_out_variant` kind. In attempt 1 neither reached threshold: the ruleset-kind run was stopped by C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER; the held_out_variant-kind run was stopped by C-TARGET-REACHED and C-BUDGET-RESPECTED. In attempts 2–11 both kinds reached their thresholds with no failed checks — 10 of 10 for each kind, 20 of 20 in aggregate, and `all_perturbations_held` true throughout. No perturbation run can be traced across records and none should be assumed to be the same run twice.

**Call: exploit.** The passing family has not plateaued in a way that justifies a structural rewrite — attempt 5 sits ~0.02 above a tight cluster and the region between it and attempt 6 is unmapped. The right move is to rebuild the attempt-5 operating point (≈13.74 s wall clock, `per_step_cost_ratio` ≈1.26, `compute_efficiency` ≈0.75, all checks clean) and then perturb it inward along lead 2, judging changes only by deltas larger than ~0.005. Note for the record that attempts 7 through 11 all scored below attempt 5 — five consecutive attempts that moved the cost/efficiency knobs to their extremes without recovering the best configuration; re-sweeping those extremes again would repeat what has already been measured and rejected.
