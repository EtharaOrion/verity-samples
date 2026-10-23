# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.8658, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3        0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                
  5 *      0.8658   1.000             2 of 2         yes             74                

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
  1 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.8630, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.7740, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Five graded submissions, all with `measurement_status: measured`. Every one carries a reward. Listed worst to best:

| Rank | Attempt | reward | compute_efficiency | per_step_cost_ratio | wall_clock_sec | standing |
|---|---|---|---|---|---|---|
| 5th | Attempt 4 | 0.7740 | 0.9681 | 0.6934 | 73.744 | worse than an earlier attempt |
| 4th | Attempt 2 | 0.8079 | 0.7226 | 0.9441 | 74.257 | worse than an earlier attempt |
| 3rd | Attempt 1 | 0.8630 | 0.6784 | 1.0723 | 76.337 | first measured attempt |
| 2nd | Attempt 3 | 0.8657 | 0.6922 | 0.9835 | 74.368 | better than every earlier attempt |
| 1st | Attempt 5 | 0.8658 | 0.6926 | 0.9581 | 74.378 | better than every earlier attempt |

**Attempt 5 holds the highest reward, 0.8658. That is the score to beat.**

Two attempts were regressions, and this must not be read as progress: Attempt 2 scored 0.8079, lower than Attempt 1's 0.8630, and its record says so directly (`worse_than_an_earlier_attempt`). Attempt 4 scored 0.7740, the lowest of all five and lower than the 0.8657 standing at the time, and its record likewise says `worse_than_an_earlier_attempt`. The improvement from Attempt 3 (0.8657) to Attempt 5 (0.8658) is +0.0001 — real by the recorded ordering, but small enough that the top of the range should be treated as flat, not as a trend.

Uniform across all five records: `task_pass` 1.0, `validity` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `primary_target_reached` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, `all_perturbations_held` true, `perturbations_declared` 2.0. `qualifying_budget` equals `wall_clock_sec` exactly in every record (73.744–76.337 s), so the whole run counts against budget; no run was truncated or disqualified.

## 2. Approach classes tried

The code from earlier attempts is not carried forward and was not supplied to me, so I can only group the attempts by the measured fingerprint they left behind. The fingerprint that separates them is the pair (`per_step_cost_ratio`, `compute_efficiency`), which moved a great deal while every correctness and conformance term stayed pinned at its maximum. Four classes:

**Class A — baseline, per-step cost above parity (Attempt 1).** `per_step_cost_ratio` 1.0723, `compute_efficiency` 0.6784, the slowest wall clock at 76.337 s. Reward 0.8630. This is the reference point: it already reached the primary target, held both perturbation runs, and passed every check, so the task itself was solved on the first measured submission. All later work was margin-chasing, not repair.

**Class B — near-parity cost, the scoring region (Attempts 3 and 5).** `per_step_cost_ratio` 0.9835 and 0.9581, `compute_efficiency` 0.6922 and 0.6926, wall clock 74.368 s and 74.378 s. Rewards 0.8657 and 0.8658 — the two best results, and nearly identical to each other. Trimming per-step cost from ~1.07 to ~0.96–0.98 while leaving the compute-efficiency figure essentially unchanged (0.678 → 0.692) bought about +0.003 over the baseline and then stopped buying anything: the second member of this class gained 0.0001 over the first.

**Class C — moderate cost reduction that lost reward (Attempt 2).** `per_step_cost_ratio` 0.9441, `compute_efficiency` 0.7226, wall clock 74.257 s. Reward 0.8079. This sits *between* Class B members on cost ratio yet scored 0.058 below both, which is the single most informative anomaly in the data (see Section 3).

**Class D — aggressive cost reduction (Attempt 4).** `per_step_cost_ratio` 0.6934 — by far the cheapest per step — and `compute_efficiency` 0.9681, by far the highest, with the fastest wall clock at 73.744 s. Reward 0.7740, the worst of the five. Maximising the efficiency term cost roughly 0.092 of reward relative to Class B. Whatever was cut to reach a 0.69 cost ratio cut something the reward pays for.

Note the shape across all four classes: reward is **not** monotone in `compute_efficiency`. The highest-efficiency submission is the lowest-scoring one, and the two best rewards come from the middle of the efficiency range (0.692). Efficiency is at best a weak, non-monotone contributor here, and past about 0.72 it is actively negative.

## 3. Checks that failed

**None. Across all five records, `failed_checks` is empty.** There is no repeated failing check to report, no check that stopped any submission, and no conformance identifier to fix. `rule_conformance` and `conformance_fraction` are 1.0 in every record and `red_line_crossed` is 0.0 in every record. The next attempt is not fighting a validity, conformance or red-line problem, and time spent hardening against one is time wasted.

**Perturbation units.** Every record declared 2.0 perturbations and reported exactly two held-out runs beside the primary one: one of kind `held_out_variant` and one of kind `seed`. In all five records both runs reached their threshold with empty `failed_checks`, and `all_perturbations_held` is true. By kind: `held_out_variant` — five runs recorded, all reached, none stopped by any check; `seed` — five runs recorded, all reached, none stopped by any check. In aggregate, ten held-out runs, ten reached, zero stopped. No run is identified by name, number or position, and no run in one record can be matched to a run in another; these are per-record kind totals only. **Neither kind of held-out run is failing, and generalisation and seed-robustness are not currently the constraint.**

**The unexplained ordering.** The graded terms supplied do not fully account for the reward ranking. `task_pass`, `validity`, `primary_target_reached`, `rule_conformance` and both perturbation outcomes are saturated and identical across all five attempts, so they cannot be separating 0.7740 from 0.8658. Cost/efficiency alone cannot separate them either: Attempt 2 at cost ratio 0.9441 scored 0.8079 while Attempt 5 at 0.9581 scored 0.8658, so a 0.014 difference in cost ratio sits alongside a 0.058 difference in reward with the ordering pointing the wrong way for a pure cost story. The conclusion the data supports is that reward carries a substantial component — a solution-quality or margin term above the pass threshold — that is not exposed in these fields, and that this hidden component, not efficiency and not conformance, is what ranks the attempts. Do not treat this as a named failing check; it is an inference about the reward's shape, and I state it as such.

## 4. Ruled-out directions

- **Aggressive per-step cost cutting / efficiency maximisation (the Class D setting).** Ruled out by Attempt 4: `per_step_cost_ratio` 0.6934 and `compute_efficiency` 0.9681 — both the most favourable of any attempt on their own terms — produced the worst reward of the five, 0.7740, against 0.8657 standing at the time. Pushing the cost ratio below ~0.9 is a measured loss of roughly 0.09 reward.
- **Treating `compute_efficiency` as a reward proxy.** Ruled out by the same evidence plus the ranking as a whole: the highest efficiency (0.9681) gives the lowest reward and the two best rewards come from efficiency 0.6922 and 0.6926. Optimising this number directly has been tried and inverts the outcome.
- **Buying reward with wall clock.** Ruled out: wall clock spans only 73.744–76.337 s across the five, and the slowest run (Attempt 1, 76.337 s) scored 0.8630 while a run 2.6 s faster (Attempt 5, 74.378 s) scored 0.8658. `qualifying_budget` equals wall clock everywhere and nothing was ever budget-limited. There is no evidence that spending more or less wall time inside this band moves reward, and no evidence that the budget is binding at all.
- **Conformance, validity and red-line hardening.** Ruled out as a source of gain: all four terms are already saturated in every record and `failed_checks` is empty in every record. There is nothing to recover here.
- **Robustness work aimed at the held-out runs.** Ruled out as a source of gain: ten held-out runs across the records, both kinds, all reached threshold with no failing check. `all_perturbations_held` is true in every record.
- **Re-submitting the Class B configuration unchanged.** Ruled out as a way to improve: Attempts 3 and 5 already occupy that region and differ by 0.0001. Another draw from the same region is a repeat, not a step.

## 5. Open leads

1. **Attack the hidden quality/margin term, holding cost fixed.** This is the one dimension never isolated. Every attempt so far varied cost/efficiency and left the reward ordering partly unexplained. Rebuild the Class B configuration — target `per_step_cost_ratio` in the 0.95–0.99 band and `compute_efficiency` near 0.69, which is where 0.8657 and 0.8658 were scored — and change only the training-quality side: more effective optimisation per step (schedule shape, warmup, final-phase learning-rate decay to a small floor, averaging or EMA of the final weights, a slightly larger effective batch, better initialisation) rather than fewer or cheaper steps. If reward rises with the cost fingerprint held near 0.96, the hidden term is confirmed as the lever and the next moves are obvious.
2. **Recover what Attempt 4 discarded, at Attempt-4 cost.** Attempt 4 proved a 0.6934 cost ratio is achievable inside the same budget without breaking any check. It lost 0.092 of reward doing so, which means it bought roughly 30% cheaper steps and spent the savings badly. Reinvest that headroom: keep the cheap step but spend the freed time on *more* steps or a longer decay tail, so the cost ratio lands back near 0.95 with strictly more optimisation done than Class B managed. This is the most concrete path to beating 0.8658 rather than tying it.
3. **Probe the interval between Attempts 2 and 5 to localise the cliff.** Cost ratio 0.9441 gave 0.8079 and 0.9581 gave 0.8658. Either something other than cost differed between those two submissions (most likely), or there is a sharp discontinuity in a narrow band. One submission placed deliberately at ~0.95 with the Class B quality settings otherwise intact would distinguish the two and tell the next attempt whether cost ratio near 0.94 is safe territory.
4. **Reduce run-to-run variance at the top.** Attempts 3 and 5 sit 0.0001 apart. Some of that gap may be noise, which means a genuine improvement of similar size would be indistinguishable from noise. Prefer changes with an expected effect well above 0.001 — the +0.003 Class A→B step is the smallest move so far that is clearly real — and prefer variance-reducing choices (weight averaging, a lower final learning rate) that raise the floor as well as the mean.

**Call: exploit.** The approach that scored best is intact, fully conformant, holds both kinds of held-out run, and has a known-good operating point (per-step cost ~0.96, compute efficiency ~0.69, wall clock ~74 s, reward 0.8658). Nothing is broken and no check needs repair, so a structural restart would throw away a solved task to chase an unmeasured alternative. The exploitation is not "resubmit Class B" — that has been done twice for +0.0001 and is a repeat, not a step. It is lead 1 combined with lead 2: hold the Class B cost fingerprint, and put the change entirely into how much useful optimisation happens per unit of that fixed cost, which is the one axis the five records show was never varied on its own. If a submission built that way still lands within 0.001 of 0.8658, the cost/quality trade in this family is exhausted and the next summary should call explore.
