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

    All three attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2 *      0.7155   1.000             2 of 2         yes             17                
  3        0.6279   1.000             2 of 2         yes             20                
  4        0.5792   1.000             2 of 2         yes             18                
  5        0.6587   1.000             2 of 2         yes             21                

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

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 3 -- reward 0.6279, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.5792, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 18
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 5 -- reward 0.6587, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Five graded submissions, all with `measurement_status: "measured"`. Ranked worst to best by `reward`:

| Rank | Attempt | reward | compute_efficiency | per_step_cost_ratio | wall_clock_sec | standing |
|---|---|---|---|---|---|---|
| 5 (worst) | 4 | 0.5792 | 0.8832 | 1.1656 | 17.5121 | worse than an earlier attempt |
| 4 | 3 | 0.6279 | 0.6033 | 1.5225 | 20.3003 | worse than an earlier attempt |
| 3 | 5 | 0.6587 | 0.6098 | 1.6262 | 20.5293 | worse than an earlier attempt |
| 2 | 1 | 0.6694 | 0.5488 | 1.5134 | 17.4264 | first measured attempt |
| 1 (best) | 2 | 0.7155 | 0.6205 | 1.5175 | 17.4531 | better than every earlier attempt |

**Attempt 2 holds the highest reward, 0.7155. That is the attempt to beat.**

Every record is fully measured; none is missing a measurement, and none scored zero. `zero_reason_code` is 0 and `red_line_crossed` is 0 throughout.

Stated plainly, and not softened: after attempt 2 the reward went **down** three times in a row. Attempt 3 (0.6279) is lower than attempt 2 (0.7155). Attempt 4 (0.5792) is lower still and is the worst result recorded. Attempt 5 (0.6587) recovered somewhat but is still **below** both attempt 2 and attempt 1. No attempt after the second has improved on it.

Constant across all five records: `task_pass` 1.0, `validity` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `primary_target_reached` 1.0, `all_perturbations_held` true, `perturbations_declared` 2.0. In every record `qualifying_budget` is numerically identical to `wall_clock_sec`, so the budget figure carries no information beyond the observed wall clock.

## 2. Approach classes tried

I was given measured terms only — no source. The approaches below are therefore grouped by the distinct metric signatures they produced, which is what the next attempt can actually steer by. Two records with the same signature would be one entry; here the five records fall into four distinct classes.

**Class A — baseline correctness-first configuration (attempt 1).** Fast wall clock (17.4264 s) at low compute efficiency (0.5488) and per-step cost ratio 1.5134. Everything conformant, primary target reached, reward 0.6694. This is the reference point: it establishes that a ~17.4 s run with roughly 1.51 per-step cost already clears every check and lands near 0.67.

**Class B — same time envelope, better efficiency (attempt 2, the best result).** Wall clock essentially unchanged from Class A (17.4531 s vs 17.4264 s, a 27 ms difference) and per-step cost ratio essentially unchanged (1.5175 vs 1.5134), but compute efficiency rose from 0.5488 to 0.6205 and reward rose from 0.6694 to 0.7155. The whole of the improvement was obtained *without* spending more wall clock and *without* changing the per-step cost profile. This is the only change in the record that produced a gain, and it is worth re-deriving precisely: hold the step budget and the per-step cost where Class A had them, and raise efficiency by roughly 0.07.

**Class C — longer-running configurations (attempts 3 and 5).** Both push wall clock into the 20.3–20.5 s range (20.3003 and 20.5293) while sitting at compute efficiency 0.6033 and 0.6098 — i.e. at or slightly below Class B's 0.6205. Per-step cost ratios 1.5225 and 1.6262. Rewards 0.6279 and 0.6587, both below Class B and below Class A. Spending roughly 3 more seconds of wall clock bought nothing in efficiency and cost reward in both instances. Attempt 5's higher per-step cost ratio (1.6262, the highest recorded) came with a slightly better reward than attempt 3's, so within this class the cost ratio is not the discriminator either.

**Class D — aggressive efficiency / low per-step cost (attempt 4).** The extreme of the recorded space: compute efficiency 0.8832 (by far the highest, +0.263 over Class B) and per-step cost ratio 1.1656 (by far the lowest, −0.352 below Class B), at a wall clock of 17.5121 s that is within 60 ms of Class B's. It produced the **worst** reward of the five, 0.5792. This is the single most informative negative result available: driving efficiency up and per-step cost down, at fixed wall clock, moved reward sharply the wrong way.

The cross-class conclusion: **reward is not monotone in `compute_efficiency` and not monotone in the inverse of `per_step_cost_ratio`.** Attempt 4 dominates attempt 2 on both of those metrics at nearly the same wall clock and still loses by 0.1363. Whatever residual quantity the reward depends on — something the supplied terms do not name, since task_pass, validity, conformance and all perturbation outcomes are pinned at their maxima in every record — is what separates 0.5792 from 0.7155. Optimising the visible efficiency metrics in isolation has already been shown to destroy it.

## 3. Checks that failed

**None.** `failed_checks` is an empty list in all five records, and it is also empty in every one of the ten perturbation units. There is no repeated failing check, no named check to fix, and no verifier reason text anywhere in the record set.

Supporting evidence that nothing conformance-related is limiting the score: `conformance_fraction` = 1.0 and `rule_conformance` = 1.0 in all five; `validity` = 1.0 in all five; `task_pass` = 1.0 in all five; `primary_target_reached` = 1.0 in all five; `red_line_crossed` = 0.0 and `zero_reason_code` = 0 in all five.

**Perturbation units, by kind and in aggregate.** Each record declares 2 perturbation units (`perturbations_declared` = 2.0) beside the primary run, one of kind `held_out_variant` and one of kind `ruleset`. Across the five records that is 5 `held_out_variant` runs and 5 `ruleset` runs, 10 in total. **Every one of them reached its threshold** (`reached: true`) and **none of them was stopped by any check** (`failed_checks` empty in all ten). `all_perturbations_held` is true in all five records. By kind: `held_out_variant` — 5 of 5 reached, 0 failures; `ruleset` — 5 of 5 reached, 0 failures. In aggregate: 10 of 10 reached, 0 failures.

The runs are not identified in the data, so nothing here should be read as tracking a particular run across records; the statement is only that both *kinds* held everywhere. Since no perturbation has ever failed, robustness is not the binding constraint and there is no evidence that any of the four approach classes is closer than another to breaking one. That said, all five submissions held them, so a new approach must be assumed to owe the same 10-for-10 record and should not be allowed to trade generalisation for score.

## 4. Ruled-out directions

**Chasing compute efficiency at the expense of the per-step cost profile (Class D, attempt 4).** Ruled out. It achieved compute_efficiency 0.8832 and per_step_cost_ratio 1.1656 — the best values recorded on both — at a wall clock (17.5121 s) indistinguishable from the best attempt's, and returned the lowest reward of all, 0.5792, versus 0.7155. The efficiency gain was real and the reward loss was large; this direction is not merely unproductive, it is actively harmful.

**Extending wall clock into the ~20.3–20.5 s range (Class C, attempts 3 and 5).** Ruled out on two independent measurements. Attempt 3 (20.3003 s) scored 0.6279 and attempt 5 (20.5293 s) scored 0.6587, both below attempt 1's 0.6694 at 17.4264 s and well below attempt 2's 0.7155 at 17.4531 s. Neither longer run bought any compute efficiency over attempt 2 (0.6033 and 0.6098 vs 0.6205). Spending more wall clock has been tried twice and lost both times.

**Raising per_step_cost_ratio above ~1.52 (attempt 5, 1.6262).** Ruled out as a lever on its own: it produced the highest cost ratio recorded and a reward 0.0568 below the best. Note the confound — attempt 5 also ran long — so this is ruled out only as tested, in combination with the long wall clock.

**Chasing conformance, validity, rule adherence or perturbation robustness.** Ruled out as a source of headroom. All of these terms are already saturated at 1.0 (or, for perturbations, 10/10 held) in every record. There is no partial credit left to recover on them, and no failed check to repair. Effort spent hardening conformance cannot raise the reward; it can only risk the parts that are working.

**Reverting to the Class A baseline profile (attempt 1, compute_efficiency 0.5488).** Ruled out as a target: attempt 2 strictly beat it, at the same wall clock and the same per-step cost, by 0.0461. There is no reason to return to the lower-efficiency end of the 17.4 s band.

## 5. Open leads

**Lead 1 — reconstruct the Class B operating point exactly, and treat it as the floor.** The single highest-value action is to land back on attempt 2's signature: wall clock ≈ 17.45 s, compute_efficiency ≈ 0.62, per_step_cost_ratio ≈ 1.52, all checks held. That configuration is worth 0.7155 and nothing since has matched it. Any new idea should be layered on top of that point, and the resulting metric signature compared to (17.4531, 0.6205, 1.5175) before anything else is judged.

**Lead 2 — search the narrow efficiency band between 0.55 and 0.62 upward, not beyond ~0.65.** The evidence brackets the useful range tightly: 0.5488 → 0.6694, 0.6205 → 0.7155, 0.8832 → 0.5792. Reward rises with efficiency in the low band and collapses well before 0.88. A cautious step to compute_efficiency ≈ 0.65–0.70 at fixed ~17.45 s wall clock and ~1.52 per-step cost would locate the turning point. This is the only interpolation the data actually supports, and it should be taken in one small step, not a leap toward Class D.

**Lead 3 — hold wall clock at 17.4–17.5 s as a hard self-imposed constraint.** The three attempts in that band scored 0.6694, 0.7155, 0.5792; the two outside it scored 0.6279 and 0.6587. The best result and the second-best are both inside it. Treat ~17.5 s as a ceiling rather than a target to exploit, since going over has cost reward twice.

**Lead 4 — identify what attempt 4 sacrificed to buy its efficiency, and protect that quantity.** Attempt 4 differs from attempt 2 chiefly in per_step_cost_ratio (1.1656 vs 1.5175). The reward drop of 0.1363 came with cheaper steps at equal total time — consistent with each step doing materially less work. The lead is to keep per-step work at roughly the Class B level (cost ratio ~1.50–1.55) and find efficiency elsewhere, e.g. in setup, data handling, or overhead outside the step loop, rather than by making steps cheaper.

**Lead 5 — probe the unnamed residual quality term.** Because task_pass, validity, conformance and all ten perturbation outcomes are pinned at their maxima while reward varies from 0.5792 to 0.7155, the reward must depend on a continuous quantity not named in the supplied terms — most plausibly held-out solution quality or accuracy, blended with a cost term. Two small, single-variable perturbations around the Class B point, changing one thing each and reading the reward delta, would map this better than any further movement along the efficiency axis, which is already well characterised and already exhausted at both ends.

**Non-lead, stated for completeness:** there is no failing check to fix, so no lead exists in that direction, and no attempt has scored zero, so there is no zero-scoring pattern being blindly repeated.

## Call: exploit

**Exploit.** The reason is specific rather than default. Attempt 2 scored 0.7155 with every check and every perturbation held, and the three attempts that followed it all scored lower — 0.6279, 0.5792, 0.6587 — which means the exploration since then has been sampling a region that is measurably worse, not extending a frontier. The mechanism of the best result is also known and narrow: at fixed wall clock and fixed per-step cost, a compute-efficiency gain of about 0.07 was worth about 0.046 of reward. That is a lever with a measured sign and a measured magnitude, and its failure mode is equally well measured — pushing the same lever to 0.8832 cost 0.1363. The next attempt should re-establish the attempt-2 operating point, confirm it reproduces near 0.7155 with 10/10 perturbations held, and then take one small step up in compute efficiency while holding wall clock at ~17.45 s and per-step cost ratio at ~1.52. Structural exploration is not warranted while a scoring approach has an unexplored, bounded interval directly above it.
