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

    All six attempts since have scored lower than it.
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
  4 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 5 -- reward 0.6587, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 8 -- reward 0.5444, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 26
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.5164, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 10 -- reward 0.5983, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 9.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Ten records were graded. Eight carry a reward; two produced no measurement at all.

Worst to best by reward:

| Attempt | Reward | Notes |
|---|---|---|
| 9 | 0.5164 | worse than an earlier attempt; failed `C-API-SURFACE`; task_pass 0.0; rule_conformance 0.8571 |
| 8 | 0.5444 | worse than an earlier attempt; highest compute_efficiency observed (0.9679), longest wall clock (26.098 s) |
| 4 | 0.5792 | worse than an earlier attempt; compute_efficiency 0.8832, per_step_cost_ratio 1.1656, wall clock 17.512 s |
| 10 | 0.5983 | worse than an earlier attempt; compute_efficiency 0.5686, wall clock 20.150 s |
| 3 | 0.6279 | worse than an earlier attempt; compute_efficiency 0.6033, wall clock 20.300 s |
| 5 | 0.6587 | worse than an earlier attempt; compute_efficiency 0.6098, per_step_cost_ratio 1.6262, wall clock 20.529 s |
| 1 | 0.6694 | first measured attempt; compute_efficiency 0.5488, per_step_cost_ratio 1.5134, wall clock 17.426 s |
| 2 | **0.7155** | better than every earlier attempt; compute_efficiency 0.6205, per_step_cost_ratio 1.5175, wall clock 17.453 s |

**Attempt 2 holds the highest reward, 0.7155. That is the number to beat.**

Attempts 6 and 7 have `measurement_status: harbor_exception`. They produced **no measurement**: no reward, no compute_efficiency, no conformance figures, no perturbation units. They did not score zero and must not be treated as evidence about the code they contained — nothing about their merit is known either way.

Every attempt after attempt 2 that was measured came in **below** attempt 2. Attempts 3, 4, 5, 8, 9 and 10 are all recorded as `worse_than_an_earlier_attempt`. There has been no progress past attempt 2; the run since then has moved downward, with the two lowest scores (9 and 8) being among the most recent measured work.

Constant across all eight measured records: `validity` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, `primary_target_reached` 1.0, `conformance_fraction` 1.0, `all_perturbations_held` true, `perturbations_declared` 2.0. `task_pass` was 1.0 everywhere except attempt 9, where it was 0.0.

# 2. Approach classes tried

The forwarded terms contain measurements, not source. What distinguishes the attempts is therefore described by the operating point each one landed on — wall clock, compute_efficiency, and per_step_cost_ratio — which is what the next attempt can actually steer toward. Records with the same signature are one entry.

**Class A — baseline cost profile at ~17.4 s wall clock, per_step_cost_ratio ≈ 1.51, compute_efficiency 0.55–0.62.** Attempts 1 (0.6694) and 2 (0.7155). These two share a wall clock to within 30 ms and a per-step cost ratio to within 0.005; they differ mainly in compute_efficiency, 0.5488 versus 0.6205, and the higher-efficiency one scored higher. This class contains both of the two best results and is the region the whole run should be read against.

**Class B — same cost profile stretched to ~20.2–20.5 s wall clock, per_step_cost_ratio 1.52–1.63, compute_efficiency 0.57–0.61.** Attempts 3 (0.6279), 5 (0.6587) and 10 (0.5983). Three samples, all below both Class A results. Spending roughly three extra seconds of wall clock at an unchanged per-step cost did not buy back the reward it cost.

**Class C — aggressive per-step cost reduction / high compute efficiency.** Attempt 4 (compute_efficiency 0.8832, per_step_cost_ratio 1.1656, wall clock 17.512 s, reward 0.5792) and attempt 8 (compute_efficiency 0.9679, per_step_cost_ratio 0.9674, wall clock 26.098 s, reward 0.5444). This is the clearest signal in the data: as compute_efficiency rose from ~0.62 to 0.88 to 0.97 and per_step_cost_ratio fell from ~1.52 to 1.17 to 0.97, reward fell monotonically, 0.7155 → 0.5792 → 0.5444. Whatever these attempts traded away to make steps cheaper was worth more to the reward than the efficiency gained. Note that attempt 8, the cheapest per step, was also the slowest overall in wall clock, so cheap steps did not even translate into a shorter run.

**Class D — a variant at compute_efficiency 0.6647, per_step_cost_ratio 1.4988, wall clock 17.122 s, that broke the API surface rule.** Attempt 9, reward 0.5164. Its cost profile sits just above the best-scoring Class A point and it had the shortest wall clock of any record, but it failed `C-API-SURFACE`, which drove task_pass to 0.0 and rule_conformance to 0.8571 and left it the lowest measured reward. Its reward is therefore not a reading on the underlying method — it is a reading on the method plus a conformance failure.

**Class E — attempts 6 and 7.** Two consecutive submissions that ended in `harbor_exception`. No terms were produced, so no class of algorithmic behaviour can be attributed to them. They are unknowns, not failures of method.

# 3. Checks that failed

One named check failed, in one record:

- **`C-API-SURFACE`**, attempt 9 — verifier reason: *"module-level statements outside imports, constants, and permitted definitions"*. This is the only failed check in the entire set. It has failed **once**. Its consequences in that record were severe out of proportion to its apparent triviality: rule_conformance dropped from 1.0 to 0.8571, task_pass dropped from 1.0 to 0.0, and the reward was the lowest of any measured attempt at 0.5164 — even though `conformance_fraction` stayed at 1.0, `validity` stayed at 1.0, `primary_target_reached` was still 1.0, and both perturbation units still held.

The concrete requirement: the submission module must contain, at top level, only imports, constant assignments, and permitted definitions (functions/classes). Any other module-level statement — executing code, a print, a call, a conditional, a loop, an inline test, a mutation of a constant after definition — trips this. Work of that sort belongs inside a function body.

No other check failed in any record. Attempts 6 and 7 record an empty `failed_checks` list, but that is because they produced no measurement, not because they passed anything.

# 4. Ruled-out directions

**Raising compute_efficiency toward 0.88–0.97 / driving per_step_cost_ratio to ≤1.17.** Ruled out on two independent samples. Attempt 4 (efficiency 0.8832, cost ratio 1.1656) scored 0.5792 and attempt 8 (efficiency 0.9679, cost ratio 0.9674) scored 0.5444, against 0.7155 for attempt 2 at efficiency 0.6205 and cost ratio 1.5175. Both are worse than every attempt in the ~1.5 cost-ratio band. Reward and compute_efficiency move in opposite directions across this range; further cheapening of the per-step cost is not a route to a higher score.

**Lengthening the run to ~20 s or beyond at an unchanged per-step cost profile.** Ruled out on three samples. Attempts 3, 5 and 10 all sat at 20.15–20.53 s wall clock and returned 0.6279, 0.6587 and 0.5983 — every one below both Class A results at ~17.44 s. Attempt 8 at 26.098 s returned 0.5444, the second-lowest. Longer wall clock has never once produced a better reward than the ~17.4 s band.

**Any module-level executable statement in the submission.** Ruled out by attempt 9's `C-API-SURFACE` failure: it costs task_pass entirely (1.0 → 0.0) and roughly a seventh of rule_conformance. Whatever algorithmic merit attempt 9's configuration had was masked by this, so the direction "keep the attempt-9 cost profile but leave setup code at module scope" is dead on arrival.

**Treating attempts 6 and 7 as evidence.** Not a direction to pursue or avoid — there is nothing to learn from them. Do not reason from their outcome; they have none.

# 5. Open leads

**Reconstruct attempt 2's operating point first, then perturb within it.** The target signature is wall clock ≈ 17.45 s, per_step_cost_ratio ≈ 1.52, compute_efficiency ≈ 0.62, with all of task_pass, validity, primary_target_reached, conformance_fraction and rule_conformance at 1.0 and both perturbation units held. Nothing since has come near 0.7155, so the first job is to get back there rather than to invent something new.

**Probe the interior of the efficiency axis between 0.62 and 0.88 at fixed ~17.4 s wall clock.** The evidence points to an optimum inside that gap and not at either end. Attempt 1 (efficiency 0.5488) scored 0.6694; attempt 2 (0.6205) scored 0.7155 — moving up helped. Attempt 4 (0.8832) scored 0.5792 — moving further up hurt badly. The unexplored band is roughly 0.63–0.80 at unchanged wall clock and per-step cost ratio near 1.5. This is the single most promising untested region and it is directly reachable by small changes to whatever controls step count versus per-step work.

**Rerun attempt 9's configuration with a clean module surface.** Attempt 9 sat at compute_efficiency 0.6647 and per_step_cost_ratio 1.4988 — inside the promising band above and just past attempt 2 — with the shortest wall clock in the whole set, 17.122 s. Its reward is uninformative because `C-API-SURFACE` zeroed task_pass. Move every module-level statement into a function, leave only imports, constants and definitions at top level, and remeasure. This is a genuine unknown that costs one attempt to resolve, and it is the only case where a failed check is plausibly hiding a good result.

**Keep the perturbation posture unchanged.** Across all eight measured records there are sixteen perturbation units — eight of kind `held_out_variant` and eight of kind `ruleset`. Every single one reached its threshold with an empty `failed_checks` list, in aggregate and in both kinds, including in attempt 9 where the primary submission itself failed `C-API-SURFACE`. No held-out run of either kind has ever been stopped by a check. Generalisation across variants and rulesets is not a live problem and should not absorb effort; changes should be made in ways that do not disturb it.

**Guard the conformance surface mechanically before submitting.** Given how cheap `C-API-SURFACE` is to trip and how expensive it is when tripped, the next attempt should end with an explicit read-through of the module's top level, confirming it holds nothing but imports, constant assignments, and function/class definitions.

**Verdict: exploit.** The highest reward, 0.7155 at attempt 2, came from a well-characterised operating point, and every attempt since has moved away from it and scored lower — the efficiency-maximising direction is exhausted and demonstrably wrong-signed, and the longer-wall-clock direction has three failures against it. The right move is to rebuild attempt 2's profile and make a small, deliberate step into the untested compute_efficiency band of 0.63–0.80 at ~17.4 s, with the module surface kept clean so the measurement is not lost to `C-API-SURFACE`. One caution about the run's history: attempts 3, 5 and 10 re-sampled the same ~20 s band three times and it scored below the best each time — resampling a region already shown to underperform, without changing what makes it underperform, is neither exploiting nor exploring, and should not be repeated.
