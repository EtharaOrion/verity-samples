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

    All eight attempts since have scored lower than it.
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
  12       0.7443   1.000             2 of 2         yes             17                
  13       0.0000   1.000             2 of 2         yes             37                

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
  7 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 11 -- reward 0.7997, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 12 -- reward 0.7443, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 13 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 37
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PER-STEP-COST-CEILING -- per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (1, 13). Whatever has been
      changing between them is not what is causing it.
    C-PER-STEP-COST-CEILING failed on attempt 13.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Thirteen graded attempts, reported worst to best by reward.

- Attempt 1 — reward 0.0000. measurement_status `measured_phase_cut`, zero_reason_code 4. It converged on nothing: primary target not reached, no qualifying row, and neither declared perturbation reached threshold.
- Attempt 13 — reward 0.0000. measurement_status `measured`, zero_reason_code 1, red_line_crossed 1, task_pass 0, validity 0. This is a scored run that hit a hard ceiling, not a phase cut; treat it as distinct from attempt 1's failure.
- Attempt 10 — reward 0.7392.
- Attempt 12 — reward 0.7443.
- Attempt 8 — reward 0.7843.
- Attempt 9 — reward 0.7891.
- Attempt 7 — reward 0.7994.
- Attempt 11 — reward 0.7997.
- Attempt 2 — reward 0.8037. First fully-passing attempt (`measured_phase_cut` but all checks held, all perturbations held).
- Attempt 4 — reward 0.8042 (0.8041887; slightly below attempt 3, `worse_than_an_earlier_attempt`).
- Attempt 3 — reward 0.8042 (0.8042363).
- Attempt 6 — reward 0.8059.
- Attempt 5 — reward 0.8255. **Highest reward measured; this is the one to beat.**

Two attempts produced no reward-positive result: attempt 1 produced its measurement but scored 0.0000 for non-convergence, and attempt 13 produced its measurement but scored 0.0000 for crossing the red line. Every other attempt is a passing, reward-bearing run clustered between 0.7392 and 0.8255. Note that reward does not track wall_clock or compute_efficiency monotonically: attempt 9 reached compute_efficiency 1.0 yet scored 0.7891, and attempt 6 reached compute_efficiency 0.9465 with per_step_cost_ratio 0.9711 yet scored only 0.8059 — below attempt 5's 0.8255, which ran at compute_efficiency 0.7476 and per_step_cost_ratio 1.2599. Whatever attempt 5 did well is not captured by raw efficiency alone.

2. Approach classes tried

Three behavioral regimes are distinguishable from the measured terms (the underlying code is not visible, so classes are grouped by measured behavior).

- Non-converging regime (attempt 1). Ran ~90 wall-clock seconds, never crossed the target threshold in the declared direction, produced no qualifying row, and left both perturbations short. Ended in phase cut. This regime does not solve the task.
- Converging in-budget regime (attempts 2–12). All pass conformance (conformance_fraction 1.0, rule_conformance 1.0, validity 1.0), reach the primary target, and hold both perturbation kinds. Qualifying budgets sit between ~13.4 and ~17.0 s; per_step_cost_ratio between ~0.97 and ~1.60; rewards 0.7392–0.8255. This is the productive family and contains the best result (attempt 5).
- Overshoot / ceiling-breaking regime (attempt 13). Converges and holds both perturbations, but drives per_step_cost_ratio to 7.185× the seed anchor and wall_clock to 37.2 s, crossing the red line and zeroing the reward.

3. Checks that failed

- C-TARGET-REACHED — attempt 1 only: "no evaluation row crosses the threshold in the declared direction."
- C-PERTURBATION-REACHED — attempt 1 only: "0 of 2 declared perturbations reached their own threshold inside their own budget."
- C-BUDGET-RESPECTED — failed in two records, attempt 1 and attempt 13, and this is the finding to weigh. In attempt 1 the reason was "no qualifying row, so no budget position exists" (a downstream effect of not converging at all); in attempt 13 the reason was "the qualifying row sits at 37.20 on the wall_clock_sec axis, above the declared ceiling of 31.1." These are two different root causes — non-convergence versus overshoot — so whatever changed between those two attempts is not the common cause; the name recurs for unrelated reasons and should not be read as one persistent defect.
- C-PER-STEP-COST-CEILING — attempt 13 only: "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0."
- Perturbation-level checks in attempt 1: the ruleset run additionally failed C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, and C-NO-LATCH-CARRYOVER; the held_out_variant run failed C-TARGET-REACHED and C-BUDGET-RESPECTED. From attempt 2 onward no check failed except the two ceiling breaches in attempt 13.

Perturbation_units by kind and in aggregate: two held-out runs accompany each primary, of kinds `ruleset` and `held_out_variant`. In attempt 1 both kinds failed to reach threshold — the ruleset run on C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER, and the held_out_variant run on C-TARGET-REACHED and C-BUDGET-RESPECTED. In every other graded attempt (2–13) both kinds reached their threshold with no failed checks. Aggregate: perturbations are a solved problem in the converging regime; the only kind-level failures on record are both in attempt 1, driven by that run reaching no target at all, and the log-well-formed and latch-carryover failures were seen only on the ruleset kind.

4. Ruled-out directions

- The non-converging configuration of attempt 1 — ruled out because it reaches no target, produces no qualifying row, and fails C-TARGET-REACHED and C-PERTURBATION-REACHED; it scores 0.0000 and gives the perturbation runs nothing to hold onto.
- Pushing per-step cost or wall-clock as hard as attempt 13 did — ruled out because per_step_cost_ratio 7.185 breaks C-PER-STEP-COST-CEILING (ceiling 3.0) and wall_clock 37.2 s breaks C-BUDGET-RESPECTED (ceiling 31.1), crossing the red line for a 0.0000. Any future configuration must keep per_step_cost_ratio under 3.0× the seed anchor and the qualifying row under 31.1 s.

5. Open leads

- Exploit attempt 5's regime. It is the high-water mark at 0.8255 and it did so at moderate efficiency (compute_efficiency 0.7476, per_step_cost_ratio 1.2599, qualifying_budget 13.74 s), not at the extremes. Reproducing that operating point is the safest starting line.
- Investigate why efficiency does not buy reward. Attempts 6 and 9 reached higher compute_efficiency (0.9465 and 1.0) and lower per-step cost than attempt 5 yet scored below it (0.8059, 0.7891). Reward is a composite; before optimizing cost further, identify the term attempt 5 maximized that the more efficient runs did not — likely a quality/convergence-margin component rather than raw speed.
- Keep both ceilings in view while tuning. The converging cluster lives comfortably at per_step_cost_ratio ~1.0–1.6 and wall_clock ~13–17 s, far from the 3.0× and 31.1 s red lines; there is room to trade a little more compute for margin without risk, as long as it does not drift toward attempt 13's regime.
- Avoid re-running attempt 1's non-converging setup unchanged; repeating a zero-scoring configuration without altering the cause of non-convergence would be neither explore nor exploit.

Call: **exploit.** The converging family scores reliably and attempt 5 stands clearly above the rest at 0.8255; the productive next move is to re-establish attempt 5's operating point and isolate which reward term it captured, rather than to try a structurally new approach while the scoring family still shows unexplained headroom.
