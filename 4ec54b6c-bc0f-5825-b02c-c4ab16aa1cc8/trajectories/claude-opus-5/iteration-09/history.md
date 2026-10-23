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

    All four attempts since have scored lower than it.
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
  3 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 7 -- reward 0.7994, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 8 -- reward 0.7843, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.7891, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Nine graded records, every one of them carrying a `measurement_status` of `measured` or `measured_phase_cut`, and therefore every one carrying a reward. No record is missing a measurement, and none should be described as absent.

Ordered worst to best by reward:

| Rank | Attempt | reward | measurement_status | standing |
|---|---|---|---|---|
| 1 (worst) | 1 | 0.0000 | measured_phase_cut | first_measured_attempt |
| 2 | 8 | 0.7843 | measured | worse than an earlier attempt |
| 3 | 9 | 0.7891 | measured | worse than an earlier attempt |
| 4 | 7 | 0.7994 | measured | worse than an earlier attempt |
| 5 | 2 | 0.8037 | measured_phase_cut | better than every earlier attempt (at the time) |
| 6 | 4 | 0.8042 | measured | worse than an earlier attempt |
| 7 | 3 | 0.8042 | measured | better than every earlier attempt (at the time) |
| 8 | 6 | 0.8059 | measured | worse than an earlier attempt |
| 9 (best) | 5 | 0.8255 | measured | better than every earlier attempt |

**Attempt 5 holds the highest reward, 0.8255. That is the one to beat.**

Plainly stated regressions, since `standing_against_best_so_far` says so directly and must not be softened: attempt 4 (0.8042) scored lower than an earlier attempt; attempt 6 (0.8059) scored lower than attempt 5; attempt 7 (0.7994) scored lower still; attempt 8 (0.7843) is the worst of all the non-zero results; attempt 9 (0.7891) also scored lower than an earlier attempt. Everything after attempt 5 has moved *down*, not up. Four consecutive attempts (6, 7, 8, 9) each came in below the standing best.

Attempt 1 scored 0.0000 with `zero_reason_code` 4, `task_pass` 0.0, `primary_target_reached` 0.0, `conformance_fraction` 0.0, and `qualifying_budget` reported as "not-measured". Note that its `validity` and `rule_conformance` were both 1.0 — the code itself was accepted; it simply never crossed the target threshold.

Secondary terms worth carrying forward, because they are the only axes on which attempts 2–9 differ at all (`task_pass`, `validity`, `rule_conformance`, `conformance_fraction`, `primary_target_reached`, `all_perturbations_held`, `red_line_crossed` are identical and saturated across all of 2–9):

| Attempt | reward | compute_efficiency | per_step_cost_ratio | wall_clock_sec |
|---|---|---|---|---|
| 5 | 0.8255 | 0.7476 | 1.2599 | 13.740 |
| 6 | 0.8059 | 0.9465 | 0.9711 | 13.427 |
| 3 | 0.8042 | 0.6051 | 1.5320 | 13.662 |
| 4 | 0.8042 | 0.5835 | 1.4974 | 13.658 |
| 2 | 0.8037 | 0.6203 | 1.4966 | 13.488 |
| 7 | 0.7994 | 0.5579 | 1.5958 | 14.103 |
| 9 | 0.7891 | 1.0000 | 1.1920 | 14.160 |
| 8 | 0.7843 | 0.6242 | 1.4960 | 16.507 |

The single most important structural fact in this table: **`compute_efficiency` does not order the rewards.** Attempt 9 achieved the maximum possible `compute_efficiency` of 1.0000 and scored 0.7891, well below attempt 5's 0.8255 at `compute_efficiency` 0.7476. Attempt 6 drove `per_step_cost_ratio` below the baseline (0.9711) and still landed at 0.8059. Whatever separates 0.8255 from 0.8059 is not raw cheapness. Attempts 3 and 4 differ by 0.00005 in reward while differing materially in `compute_efficiency` (0.6051 vs 0.5835), which sets a practical noise floor: reward differences below roughly 0.002 should not be treated as real signal.

## 2. Approach classes tried

Grouping the nine records by their measured operating signature rather than by count — records that behaved the same way are one entry.

**Class A — the non-converging first cut (attempt 1).** A configuration that produced valid, rule-conformant output but in which no evaluation row ever crossed the threshold in the declared direction. `per_step_cost_ratio` 1.0194 and `compute_efficiency` 1.0, i.e. it was cheap per step, and it ran 89.98 s of wall clock — by far the longest of any record, six times the wall clock of the converged attempts — without producing a qualifying row. Its ruleset held-out run additionally emitted a malformed log and carried latch state across. This class is dead and is treated below as ruled out.

**Class B — the heavy-per-step converged family (attempts 2, 3, 4, 8).** All four sit at `per_step_cost_ratio` 1.496–1.532 with `compute_efficiency` 0.583–0.624 and cluster tightly at rewards 0.7843, 0.8037, 0.8042, 0.8042. This is the family that first got the primary target and both perturbations to hold: full conformance, `task_pass` 1.0, `red_line_crossed` 0.0, no failed checks. It is a stable, reliable, mid-0.80 plateau. Attempt 8 is the same class with wall clock blown out to 16.51 s (against ~13.5 s for the rest) and it paid for that with the worst non-zero reward in the set, 0.7843.

**Class C — the push-cost-higher variant (attempt 7).** Class B taken further in the expensive direction: `per_step_cost_ratio` 1.5958, the highest recorded, `compute_efficiency` 0.5579, the lowest recorded, wall clock 14.10 s. Reward 0.7994 — below the Class B plateau. Making the per-step work heavier than Class B costs reward.

**Class D — the moderate-cost operating point (attempt 5).** `per_step_cost_ratio` 1.2599, `compute_efficiency` 0.7476, wall clock 13.74 s, reward 0.8255. This is the sole best result and it sits between Class B (≈1.50) and Class E (≈0.97) on the cost axis. It is not the cheapest, not the most efficient, and not the fastest record in the set, yet it is the highest scoring by a clear 0.0196 over the runner-up — a margin an order of magnitude above the ~0.002 noise floor.

**Class E — the aggressive-efficiency variants (attempts 6 and 9).** Two different ways of chasing cheapness. Attempt 6 pushed `per_step_cost_ratio` to 0.9711, below baseline, with `compute_efficiency` 0.9465 and the fastest wall clock in the set, 13.43 s; reward 0.8059. Attempt 9 saturated `compute_efficiency` at exactly 1.0000 with `per_step_cost_ratio` 1.1920 and wall clock 14.16 s; reward 0.7891. Both are fully conformant and both scored below attempt 5. Squeezing efficiency past the attempt-5 point loses reward.

Note on scope: these classes are reconstructed from the measured terms alone. The source of each attempt is not available to this summary, so what carries forward is the *operating signature* — the cost ratio, efficiency, and wall-clock triple — not the code. The next attempt should treat the attempt-5 signature (`per_step_cost_ratio` ≈ 1.26, `compute_efficiency` ≈ 0.75, wall clock ≈ 13.7 s, with both perturbations holding) as the target to reproduce and then improve, and should read its own measured triple as evidence of which class it has landed in.

## 3. Checks that failed

Only one record has any failed checks at all: attempt 1. Attempts 2 through 9 each report `failed_checks: []` on the primary run and `failed_checks: []` on both held-out runs, with `conformance_fraction` 1.0 and `all_perturbations_held` true.

Attempt 1, primary run, three failures with the verifier's own reasons:

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction".
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". This is a downstream consequence of the first: with nothing qualifying, there is no budget position to evaluate, which is also why `qualifying_budget` is reported as "not-measured" for that record.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget".

Attempt 1, held-out runs (both of the two declared perturbations failed):

- The **ruleset** run failed four checks: **C-LOG-WELL-FORMED**, **C-TARGET-REACHED**, **C-BUDGET-RESPECTED**, and **C-NO-LATCH-CARRYOVER**.
- The **held_out_variant** run failed two: **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**.

Repeat-failure accounting. No named check fails in more than one record — every failure in this set is confined to attempt 1, and nothing between attempts 2 and 9 has re-tripped any of them. Within attempt 1, however, **C-TARGET-REACHED failed three times** (primary run, ruleset run, held_out_variant run) and **C-BUDGET-RESPECTED failed three times** (same three sites). That within-record triple is the signature of a single root cause — non-convergence to the threshold — propagating identically to every evaluation site, and not of three independent defects. **C-LOG-WELL-FORMED** and **C-NO-LATCH-CARRYOVER** failed once each, and only in the ruleset run; they are ruleset-run-specific and did not appear on the primary run or on the held_out_variant run.

Because whatever changed between attempt 1 and attempt 2 cleared all six named checks at once and they have stayed cleared through seven subsequent records, the conformance scaffolding established at attempt 2 is load-bearing and must be preserved verbatim in structure. The remaining reward gap is not a conformance problem.

## 4. Ruled-out directions

**The attempt-1 configuration class, in full.** Ruled out because it produced reward 0.0000 with `zero_reason_code` 4 and no qualifying row at all: C-TARGET-REACHED failed on the primary run and on both held-out runs, C-BUDGET-RESPECTED consequently had no budget position to evaluate, and C-PERTURBATION-REACHED recorded 0 of 2. It also emitted a malformed log and carried latch state across on the ruleset run. Reproducing anything with this shape scores zero.

**Maximizing `compute_efficiency` toward 1.0.** Ruled out on direct evidence: attempt 9 hit `compute_efficiency` exactly 1.0000 — the ceiling — and returned 0.7891, which is 0.0364 *below* attempt 5's 0.8255 at `compute_efficiency` 0.7476. Efficiency is not the objective and pushing it to the ceiling costs reward.

**Driving `per_step_cost_ratio` below baseline.** Ruled out: attempt 6 reached 0.9711, cheaper per step than the reference, with the fastest wall clock in the whole set (13.43 s), and scored 0.8059 — 0.0196 below attempt 5. Being cheaper and faster than attempt 5 did not beat attempt 5.

**Pushing `per_step_cost_ratio` above ~1.5.** Ruled out: attempt 7 at 1.5958 (the most expensive per step, `compute_efficiency` 0.5579, the lowest) scored 0.7994, below the 0.8037–0.8042 Class B plateau it came from. The expensive direction is exhausted.

**The Class B plateau at `per_step_cost_ratio` ≈ 1.50 as a place to keep iterating.** Ruled out as a target: four records (2, 3, 4, 8) landed there and produced 0.8037, 0.8042, 0.8042, 0.7843. Attempts 3 and 4 differ by 0.00005 in reward despite differing `compute_efficiency` — that is noise, not movement. This region is flat and has been sampled enough.

**Letting wall clock drift upward.** Ruled out: attempt 8 ran 16.51 s against ~13.4–14.2 s for every other converged record and posted 0.7843, the worst non-zero reward, despite being otherwise indistinguishable from attempts 2/3/4 in cost ratio (1.4960) and efficiency (0.6242). Extra wall clock at a fixed cost profile is pure loss.

**Chasing sub-0.002 reward differences.** Ruled out as a strategy: the 3-vs-4 pair establishes that reward can move by 0.00005 across materially different efficiency figures. Any change that produces a swing smaller than about 0.002 cannot be distinguished from noise and should not be interpreted as an improvement.

## 5. Open leads

**Re-establish the attempt-5 operating point first, and confirm it by signature.** The single highest-value action is reproducing the configuration whose measured triple was `per_step_cost_ratio` ≈ 1.2599, `compute_efficiency` ≈ 0.7476, wall clock ≈ 13.74 s, with `task_pass` 1.0, `conformance_fraction` 1.0, both perturbations holding, and `red_line_crossed` 0.0. Since the next attempt starts from a pristine stub and cannot see the earlier code, it should aim for that cost signature explicitly and treat landing at ≈1.50 (Class B) or ≈0.97 (Class E) as a sign it has drifted into a region already known to score ~0.80 or lower.

**Sweep the unexplored band between attempt 5 and attempt 6.** The cost axis has been sampled at 0.97 (0.8059), 1.19 (0.7891), 1.26 (0.8255), 1.50 (≈0.804), and 1.60 (0.7994). The 0.8255 peak sits at 1.26 with the neighbours on both sides lower, which is consistent with an interior optimum rather than a monotone trend. The band roughly 1.20–1.40 is the least-sampled region adjacent to the peak and is the most promising place to look for a better point. Note that 1.19 (attempt 9) scored poorly while 1.26 scored best, so this optimum, if real, is narrow — move in small steps and treat anything within 0.002 of 0.8255 as a tie, not a gain.

**Find the term the exposed metrics are not showing.** For attempts 2–9, `task_pass`, `validity`, `rule_conformance`, `conformance_fraction`, `primary_target_reached`, `all_perturbations_held` and `red_line_crossed` are all identical and saturated, yet reward spans 0.7843 to 0.8255. That spread is therefore driven by something beyond the binary pass terms, and it is not explained by `compute_efficiency` alone (attempt 9 disproves that) nor by `per_step_cost_ratio` alone (attempt 6 disproves that) nor by wall clock alone (attempt 6 is fastest and not best). The lead is to improve the *quality or margin* of the converged solution — how decisively the target is crossed, not merely that it is crossed — while holding the attempt-5 cost profile fixed. Vary one thing at a time and read the reward against the 0.002 noise floor.

**Hold wall clock at or below ~13.7 s.** Every record at or under 13.74 s scored 0.8037 or better; the two slowest converged records, 14.10 s (0.7994) and 14.16 s (0.7891), and the outlier at 16.51 s (0.7843), are the three lowest non-zero rewards. Keeping wall clock in the 13.4–13.7 s band is a cheap constraint that is consistent with every good result.

**Preserve the conformance scaffolding without modification.** Log well-formedness, absence of latch carryover between held-out runs, and budget-position emission on qualifying rows have held on all sixteen held-out runs across attempts 2–9 and on all eight primary runs. Do not restructure that machinery while tuning the cost profile; the six named checks from attempt 1 are the only checks that have ever failed and they were fixed exactly once.

**Perturbation-unit status, by kind and in aggregate.** Across the nine records there are eighteen held-out runs beside the primary, two per record, one of kind `ruleset` and one of kind `held_out_variant` in each. Aggregate: sixteen of eighteen reached their threshold. By kind: `ruleset` reached in eight of nine records and failed in one, on C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER; `held_out_variant` reached in eight of nine records and failed in one, on C-TARGET-REACHED and C-BUDGET-RESPECTED. Both failures occurred within attempt 1 and no held-out run has failed since. The runs are not identified by name, number or position in the records, so no claim is made here that any particular run recurs across records — only the kinds and their outcomes are reportable, and neither kind is currently failing.

**Call: exploit.** The approach that scored has *not* stopped improving in any sense that justifies a structural rewrite — rather, it was found once at attempt 5 and then abandoned, and the four attempts that followed all moved away from it and all scored lower. The correct move is to return to the attempt-5 operating point, confirm it reproduces at ≈0.8255, and then perturb narrowly around `per_step_cost_ratio` 1.20–1.40 while holding wall clock ≤ ~13.7 s and the conformance scaffolding untouched. One caution drawn from the record: attempts 2, 3, 4 and 8 kept re-sampling the same flat ≈1.50 plateau and produced four rewards within 0.02 of each other — repeatedly re-landing in a region already known to be flat is neither exploiting nor exploring, and it should not be repeated.
