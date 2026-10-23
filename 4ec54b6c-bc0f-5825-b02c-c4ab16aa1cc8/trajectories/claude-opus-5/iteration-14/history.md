# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 14 -- reward 0.8820, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 7
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
  14 *     0.8820   1.000             2 of 2         yes             7                 

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
  9 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 5 -- reward 0.8255, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 6 -- reward 0.8059, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 13
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

Fourteen attempts were graded. Ranked worst to best by reward:

- Attempt 1 — reward 0.0000. measurement_status `measured_phase_cut`, zero_reason_code 4. It reached no target: primary_target_reached 0, task_pass 0, conformance_fraction 0. Both declared perturbations failed to reach threshold. This is a genuine measured zero, not an unmeasured record.
- Attempt 13 — reward 0.0000. measurement_status `measured`, zero_reason_code 1, red_line_crossed 1, validity 0. It did reach the primary target and both perturbations held, but it crossed two ceilings (see Section 3). A measured zero caused by a red-line crossing, distinct in cause from attempt 1.
- Attempt 10 — reward 0.7392551398592418.
- Attempt 12 — reward 0.7443384589070151.
- Attempt 8 — reward 0.7842706320335443.
- Attempt 9 — reward 0.7890867792063512.
- Attempt 7 — reward 0.7993993398303895.
- Attempt 11 — reward 0.7996679260744287.
- Attempt 2 — reward 0.8036778762879345. (measurement_status `measured_phase_cut`, still measured and rewarded.)
- Attempt 4 — reward 0.8041887297475568. Explicitly worse than an earlier attempt.
- Attempt 3 — reward 0.8042363383093786.
- Attempt 6 — reward 0.8059215510545337.
- Attempt 5 — reward 0.8254758711461578.
- Attempt 14 — reward 0.8820109442351848. This is the highest reward and the one to beat.

The signal in the rewarded band is strong and consistent: reward rises as the qualifying_budget (wall_clock to reach the target) falls. Attempt 14 reached the target in 6.628 sec, roughly half the ~13–17 sec of every other passing attempt, and took the top reward. Attempts 10 and 12, the weakest non-zero results, are the slowest passing runs at ~16.9 sec. Speed to target, not conformance, is what separates the rewarded attempts — every passing attempt already held all checks and all perturbations.

2. Approach classes tried

- Non-converging attempt (attempt 1). The trainer never crossed the target threshold in the declared direction; no qualifying row existed, so budget and perturbation checks had nothing to evaluate against. Distinct failure mode from everything after it.
- Baseline converging cluster (attempts 2, 3, 4, 6, 7, 8, 9, 11, 12, and the slower 10). These all pass every check, hold both perturbations, and land in the ~0.74–0.81 reward band with per_step_cost_ratio near 1.0–1.6 and qualifying_budget ~13–17 sec. They differ from each other only marginally; the reward spread inside this cluster tracks wall-clock time, with the slower runs (16–17 sec) at the bottom.
- Faster-convergence variant (attempt 5, then attempt 14). Attempt 5 (0.8255, budget 13.74, higher compute_efficiency 0.748) and especially attempt 14 (0.8820, budget 6.628) reach the target markedly faster. Attempt 14 accepts a higher per_step_cost_ratio (1.869) but wins overall by cutting total time roughly in half. This is the productive direction.
- Aggressive per-step compute (attempt 13). Pushed per-step work so hard that per_step_cost_ratio hit 7.185 and wall clock hit 37.2 sec; this crossed the red line and scored zero despite reaching the target and holding both perturbations.

3. Checks that failed

- C-TARGET-REACHED — failed once, in attempt 1: "no evaluation row crosses the threshold in the declared direction." Also failed inside both perturbation units of attempt 1.
- C-BUDGET-RESPECTED — failed twice, in attempts 1 and 13, but for opposite reasons. In attempt 1 there was no qualifying row, so no budget position existed. In attempt 13 the qualifying row sat at 37.20 sec on the wall_clock_sec axis, above the declared ceiling of 31.1. Because the two failures have unrelated causes (never-reached vs. too-slow), whatever was changed between those attempts is not the lever that controls this check; the fix is different in each case — reach the target at all in the first, stay under the wall-clock ceiling in the second.
- C-PERTURBATION-REACHED — failed once, in attempt 1: "0 of 2 declared perturbations reached their own threshold inside their own budget."
- C-PER-STEP-COST-CEILING — failed once, in attempt 13: per-step cost 7.185 times the seed anchor, above the ceiling of 3.0.
- Inside attempt 1's perturbation units: C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED, C-NO-LATCH-CARRYOVER (ruleset unit) and C-TARGET-REACHED, C-BUDGET-RESPECTED (held_out_variant unit).

perturbation_units by kind: two kinds run beside the primary, `ruleset` and `held_out_variant`. In attempt 1 both kinds failed to reach threshold — the ruleset kind failing on C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER, and the held_out_variant kind on C-TARGET-REACHED and C-BUDGET-RESPECTED. In every other attempt (2 through 14, including the two that scored zero on the primary red line), both the ruleset and the held_out_variant kind reached their thresholds with no failed checks. In aggregate the perturbation units are not a live problem for any converging solution; they only fell over in the one attempt that never converged.

4. Ruled-out directions

- Aggressive per-step compute to force faster convergence (attempt 13). Ruled out: driving per_step_cost_ratio to 7.185 crossed C-PER-STEP-COST-CEILING (ceiling 3.0) and the wall clock to 37.2 sec crossed C-BUDGET-RESPECTED (ceiling 31.1), yielding reward 0. The per-step cost ceiling is a hard 3.0× the seed anchor and the wall-clock ceiling is ~31.1 sec — both must be respected.
- Whatever configuration failed to converge in attempt 1. Ruled out on its own terms: no target crossing means no reward and takes the perturbations down with it. Any next attempt must first guarantee the primary target is reached.
- Re-running the mid-pack baseline converging cluster without change. The band of attempts scoring 0.74–0.81 has been sampled many times and has stopped improving; simply reproducing a ~13–17 sec converging run yields nothing new.

5. Open leads

- Exploit the speed-to-target lever. Reward tracks qualifying_budget inversely across the whole rewarded set, and attempt 14 set the best mark (0.8820) by reaching the target in 6.628 sec. Push convergence faster still while keeping per_step_cost_ratio under the 3.0 ceiling and wall clock under 31.1 sec. Attempt 14 sat at per_step_cost_ratio 1.869 with room to spare below 3.0, so modestly more per-step work traded for fewer total steps is the most promising trade — but stop well short of the attempt-13 regime that blew both ceilings.
- Keep compute_efficiency high alongside low budget. Attempt 14 combined low budget (6.628) with compute_efficiency 0.503; attempt 5 reached 0.8255 with efficiency 0.748 at a higher budget. Explore whether a run can hold attempt-14's low wall clock while raising efficiency, to see if reward climbs further.
- Conformance is solved for converging runs and is not where the gains are; do not spend effort there. All perturbations and all rule checks already pass for any run that reaches the target quickly.

Call: exploit. The best approach (fast convergence, attempt 14) just set a new high and the reward gradient — lower qualifying_budget, higher reward — is unmistakable and not yet exhausted. Continue driving time-to-target down within the per-step-cost (3.0×) and wall-clock (31.1 sec) ceilings rather than opening a structurally new approach.
