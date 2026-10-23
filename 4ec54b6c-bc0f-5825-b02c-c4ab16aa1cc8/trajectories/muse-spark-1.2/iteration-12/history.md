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

    All ten attempts since have scored lower than it.
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
  14       0.6426   1.000             2 of 2         yes             18                

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

    attempt 14 -- reward 0.6426, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 18
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 9.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

1. Results so far

Fourteen submissions were graded. Twelve carry a reward; two produced no measurement at all.

Worst to best by reward:

- Attempt 12 — reward 0.4962. task_pass 0.0. Failed C-PERTURBATION-REACHED; conformance_fraction 0.5; all_perturbations_held false. Lower than every earlier measured attempt at the time (standing: worse_than_an_earlier_attempt). wall_clock 16.78 s, compute_efficiency 0.6278, per_step_cost_ratio 1.4886.
- Attempt 9 — reward 0.5164. task_pass 0.0. Failed C-API-SURFACE; rule_conformance 0.8571. Lower than earlier attempts. wall_clock 17.12 s, compute_efficiency 0.6647, per_step_cost_ratio 1.4988.
- Attempt 8 — reward 0.5444. Clean: no failed checks, task_pass 1.0, all perturbations held. Lower than earlier attempts. wall_clock 26.10 s (the longest run recorded), compute_efficiency 0.9679, per_step_cost_ratio 0.9674.
- Attempt 13 — reward 0.5590. Clean, task_pass 1.0. Lower than earlier attempts. wall_clock 20.60 s, compute_efficiency 0.7642, per_step_cost_ratio 1.2404.
- Attempt 4 — reward 0.5792. Clean, task_pass 1.0. Lower than earlier attempts. wall_clock 17.51 s, compute_efficiency 0.8832, per_step_cost_ratio 1.1656.
- Attempt 10 — reward 0.5983. Clean, task_pass 1.0. Lower than earlier attempts. wall_clock 20.15 s, compute_efficiency 0.5686, per_step_cost_ratio 1.5152.
- Attempt 3 — reward 0.6279. Clean, task_pass 1.0. Lower than attempt 2. wall_clock 20.30 s, compute_efficiency 0.6033, per_step_cost_ratio 1.5225.
- Attempt 14 — reward 0.6426. Clean, task_pass 1.0. Lower than earlier attempts. wall_clock 17.78 s, compute_efficiency 0.6320, per_step_cost_ratio 1.6303.
- Attempt 5 — reward 0.6587. Clean, task_pass 1.0. Lower than attempt 2. wall_clock 20.53 s, compute_efficiency 0.6098, per_step_cost_ratio 1.6262.
- Attempt 11 — reward 0.6639. Clean, task_pass 1.0. Lower than attempt 2. wall_clock 20.06 s, compute_efficiency 0.8424, per_step_cost_ratio 1.0166.
- Attempt 1 — reward 0.6694. Clean, task_pass 1.0, first measured attempt. wall_clock 17.43 s, compute_efficiency 0.5488, per_step_cost_ratio 1.5134.
- Attempt 2 — reward 0.7155. Clean, task_pass 1.0, all perturbations held, rule_conformance 1.0. wall_clock 17.45 s, compute_efficiency 0.6205, per_step_cost_ratio 1.5175. Standing: better_than_every_earlier_attempt.

Attempt 2 holds the highest reward, 0.7155, and it is the one to beat. Nothing after it has matched it: attempts 3, 4, 5, 8, 9, 10, 11, 12, 13 and 14 are each recorded as worse_than_an_earlier_attempt, so the eleven graded submissions following attempt 2 constitute a run of regressions, not progress.

Attempts 6 and 7 have measurement_status "harbor_exception". They produced no measurement: no reward, no compute_efficiency, no conformance figures, no perturbation units. They must not be read as scoring zero — they were never scored.

Red lines: red_line_crossed is 0.0 and zero_reason_code is 0 on every measured record. validity is 1.0 on every measured record. No submission was invalidated or zeroed.

2. Approach classes tried

The records supply measured terms only, not source. The approaches are therefore grouped by the operating point they produced — wall clock, per_step_cost_ratio and compute_efficiency together identify the class of configuration each submission ran at.

Class A — baseline-cost regime, per_step_cost_ratio ≈ 1.49–1.52 with wall clock ≈ 17.1–17.5 s. Attempts 1 (0.6694), 2 (0.7155) and 9 (0.5164, but conformance-broken). This class contains both the best result and the second best. Within it, attempt 2 differs from attempt 1 almost only in compute_efficiency (0.6205 vs 0.5488) at essentially identical per-step cost and wall clock, and gained +0.0461 reward.

Class B — same baseline cost ratio but stretched wall clock, ≈ 20.1–20.3 s. Attempts 3 (0.6279) and 10 (0.5983). Same per_step_cost_ratio band as class A (1.5225, 1.5152) but roughly 2.7–3.0 s more wall clock, and both landed 0.09–0.12 below attempt 2.

Class C — cost-reduction regime, per_step_cost_ratio driven down to 0.97–1.24 with compute_efficiency pushed up to 0.76–0.97. Attempts 4 (0.5792), 8 (0.5444), 11 (0.6639), 13 (0.5590). The extreme of this class, attempt 8 at per_step_cost_ratio 0.9674 and compute_efficiency 0.9679, is the lowest-scoring clean submission of all. Every member of this class scored below attempt 2.

Class D — raised per-step cost, per_step_cost_ratio ≈ 1.63. Attempts 5 (0.6587, wall 20.53 s) and 14 (0.6426, wall 17.78 s). Both below attempt 2, and the shorter of the two did not recover the gap.

Class E — submissions that broke a harness check. Attempt 9 (C-API-SURFACE) and attempt 12 (C-PERTURBATION-REACHED). Both took task_pass to 0.0 and are the two lowest rewards on record.

Class F — submissions that the harbor could not run. Attempts 6 and 7, harbor_exception, no measurement produced.

3. Checks that failed

Two named checks failed, in two different records, plus two unit-level checks inside one perturbation run.

- C-API-SURFACE — failed once, in attempt 9. Verifier reason: "module-level statements outside imports, constants, and permitted definitions". This dropped rule_conformance to 0.8571 and task_pass to 0.0, while conformance_fraction stayed 1.0 and all perturbations still held. The submission must place all executable logic inside the permitted function/class definitions; only imports, constants and permitted definitions may sit at module level.
- C-PERTURBATION-REACHED — failed once, in attempt 12. Verifier reason: "1 of 2 declared perturbations reached their own threshold inside their own budget". conformance_fraction 0.5, all_perturbations_held false, task_pass 0.0. Note that rule_conformance stayed 1.0 and primary_target_reached stayed 1.0 here — the primary run was fine; only a held-out run failed.
- Inside attempt 12's perturbation units, the run that failed reported C-TARGET-REACHED and C-BUDGET-RESPECTED as its own failed checks. Both fired together: the run did not hit its threshold and also did not stay inside its budget.

No named check has failed in more than one record, so there is no single recurring conformance defect. The recurring non-check failure is the harbor_exception, which occurred twice (attempts 6 and 7) and produced no measurement either time.

Perturbation-unit outcomes. Every measured record declared 2 perturbations and reported 2 units, one of kind "ruleset" and one of kind "held_out_variant" — 24 units across the twelve measured records.

- By kind, ruleset: 12 of 12 reached their threshold, with no failed checks in any record.
- By kind, held_out_variant: 11 of 12 reached. The single failure occurred in attempt 12 and was stopped by C-TARGET-REACHED and C-BUDGET-RESPECTED.
- In aggregate: 23 of 24 units reached; 1 of 24 did not.

Attempts 6 and 7 reported no perturbation units at all, consistent with their harbor_exception status; that is an absence of measurement, not a failure of any unit.

The held-out-variant kind is the one that has broken, and it broke on the pair C-TARGET-REACHED / C-BUDGET-RESPECTED. The ruleset kind has never broken.

4. Ruled-out directions

- Driving per_step_cost_ratio to or below 1.0 while maximising compute_efficiency. Attempt 8 reached compute_efficiency 0.9679 and per_step_cost_ratio 0.9674 and scored 0.5444, the worst clean result. It also had the longest wall clock, 26.10 s. Cheap-per-step but long-running configurations are not rewarded here.
- The broader cost-reduction class generally. All four members — attempts 4 (0.5792), 8 (0.5444), 11 (0.6639), 13 (0.5590) — scored below attempt 2's 0.7155 despite every one of them being clean with task_pass 1.0 and all perturbations held. Raising compute_efficiency into the 0.76–0.97 band has never produced a competitive reward.
- Raising per_step_cost_ratio to ≈1.63. Attempts 5 (0.6587) and 14 (0.6426) both fell short of attempt 2, and attempt 14 did so even at a near-matching wall clock of 17.78 s. Going more expensive per step than the ≈1.51–1.52 band did not help.
- Extending wall clock past ~20 s at the baseline cost ratio. Attempts 3 (20.30 s, 0.6279) and 10 (20.15 s, 0.5983) share attempt 2's per-step cost band but ran ~3 s longer and lost 0.09–0.12 of reward. Longer is not better in this harness.
- Any module-level executable statement. C-API-SURFACE in attempt 9 zeroed task_pass and produced 0.5164 despite a completely healthy 17.12 s run with both perturbations reached. This is a hard structural constraint, not a tuning knob.
- Whatever shortened attempt 12's held-out run. At 16.78 s wall clock, the shortest recorded, its held-out_variant unit failed both C-TARGET-REACHED and C-BUDGET-RESPECTED, giving the lowest reward on record. Trimming work until the held-out variant cannot reach its own threshold inside its own budget is ruled out.

5. Open leads

- Reconstruct attempt 2's operating point and treat it as the target: wall clock ≈ 17.45 s, per_step_cost_ratio ≈ 1.518, compute_efficiency ≈ 0.620, task_pass 1.0, rule_conformance 1.0, both perturbations reached. This is the only configuration that has ever been better_than_every_earlier_attempt and is the one to beat at 0.7155.
- Tune compute_efficiency upward only slightly, holding the other two terms fixed. The attempt 1 → attempt 2 pair is the single clean controlled comparison on record: identical per-step cost (1.5134 vs 1.5175) and identical wall clock (17.43 vs 17.45 s), with compute_efficiency moving 0.5488 → 0.6205 and reward moving 0.6694 → 0.7155. A cautious extension into roughly the 0.65–0.72 efficiency band, with per_step_cost_ratio pinned near 1.51–1.52 and wall clock near 17.4–17.5 s, is the highest-value untested point. It must not be pushed into the 0.76+ band, where class C consistently lost.
- Keep wall clock at or just under 17.5 s. Every attempt in the 17.1–17.8 s window that was clean scored 0.5792 or better and includes both top results; every 20 s+ clean attempt scored 0.6639 or worse. But do not compress below ~17 s: attempt 12 at 16.78 s is where the held-out variant broke its budget and threshold.
- Guard the held-out variant explicitly. It is the only perturbation kind that has ever failed (1 of 12), and it failed on C-TARGET-REACHED together with C-BUDGET-RESPECTED. Whatever schedule or step count the primary run uses, verify the held-out variant still converges within its own separate budget rather than assuming the primary run's margin transfers.
- Keep the module surface strictly clean: imports, constants and permitted definitions only, with every side effect inside a function body. This costs nothing and removes the C-API-SURFACE failure mode that cost attempt 9 its task_pass.
- Keep the submission structurally simple and free of anything exotic at import or setup time. Two submissions produced no measurement at all through harbor_exception; a run that cannot be measured cannot score, so favour constructs already proven to execute in the harness over novel ones.

Verdict: exploit. The best result, attempt 2 at 0.7155, was reached early and every subsequent approach class — cheaper per step, more expensive per step, longer wall clock, and the two conformance breaks — has scored below it. The approaches that scored have not stopped improving so much as never been revisited: the attempt 1 → attempt 2 axis (efficiency up at fixed cost ratio and fixed wall clock) was abandoned after one step and is still the only movement that ever raised the reward. The next attempt should rebuild that exact operating point and take one more careful step along that same axis, rather than opening a new structural direction.
