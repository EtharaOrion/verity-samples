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

    All five attempts since have scored lower than it.
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

    attempt 10 -- reward 0.7393, worse than an earlier attempt
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

Ten graded records, all carrying a measurement status that yields a reward. Listed worst to best by reward:

| Rank (worst→best) | Attempt | reward | measurement_status |
|---|---|---|---|
| 1 | 1 | 0.0000 | measured_phase_cut (zero_reason_code 4) |
| 2 | 10 | 0.7393 | measured |
| 3 | 8 | 0.7843 | measured |
| 4 | 9 | 0.7891 | measured |
| 5 | 7 | 0.7994 | measured |
| 6 | 2 | 0.8037 | measured_phase_cut |
| 7 | 4 | 0.8042 (0.80418873) | measured |
| 8 | 3 | 0.8042 (0.80423634) | measured |
| 9 | 6 | 0.8059 | measured |
| 10 | 5 | **0.8255** | measured |

**Attempt 5 holds the highest reward, 0.8255. That is the score to beat.**

Every one of these ten records was measured, so every one carries a reward; none must be read as "no measurement". Attempt 1 genuinely scored 0.0000 — that is a measured zero with zero_reason_code 4, not a missing measurement.

Direction of movement, stated plainly rather than softened: after attempt 5 set the high-water mark at 0.8255, **every subsequent attempt was worse than an earlier attempt** — attempt 6 (0.8059), attempt 7 (0.7994), attempt 8 (0.7843), attempt 9 (0.7891), attempt 10 (0.7392551…, i.e. 0.7393). Attempt 10 is the worst non-zero result recorded and the run of five consecutive regressions after attempt 5 is a decline, not progress. Attempt 4 (0.8042, precisely 0.80418873) was also marked worse than an earlier attempt: it fell fractionally below attempt 3 (0.80423634) despite rounding to the same four decimals.

Supporting terms for the leaders and laggards:

- Attempt 5 (best, 0.8255): compute_efficiency 0.7476, per_step_cost_ratio 1.2599, wall_clock 13.7398 s, qualifying_budget 13.7398.
- Attempt 6 (0.8059): compute_efficiency 0.9465, per_step_cost_ratio 0.9711 (lowest recorded), wall_clock 13.4266 s (lowest recorded).
- Attempt 9 (0.7891): compute_efficiency 1.0000 (maximum), per_step_cost_ratio 1.1920, wall_clock 14.1599 s.
- Attempt 8 (0.7843): wall_clock 16.5068 s, per_step_cost_ratio 1.4960.
- Attempt 10 (0.7393): wall_clock 16.8995 s, compute_efficiency 0.8355, per_step_cost_ratio 1.0702.
- Attempts 2, 3, 4 (0.8037 / 0.8042 / 0.8042): per_step_cost_ratio clustered at 1.4966 / 1.5320 / 1.4974, wall_clock 13.49 / 13.66 / 13.66 s.

Across attempts 2–10: task_pass 1.0, validity 1.0, rule_conformance 1.0, conformance_fraction 1.0, red_line_crossed 0.0, primary_target_reached 1.0, all_perturbations_held true, zero_reason_code 0, and no failed checks whatsoever. The correctness/conformance layer is solved and has stayed solved for nine consecutive records. The reward differences among attempts 2–10 are entirely differences in the cost/budget terms, not in passing or conforming.

# 2. Approach classes tried

The records carry no textual description of the submitted code, only measured terms. Approaches below are therefore grouped by their measured signature, which is what a future attempt can actually steer toward.

**Class A — non-conforming / over-long run (attempt 1, reward 0.0000).** wall_clock 89.98 s (roughly six times any other record), per_step_cost_ratio 1.0194, compute_efficiency 1.0, conformance_fraction 0.0, primary_target_reached 0.0, task_pass 0.0, qualifying_budget "not-measured". Nothing crossed a threshold; the phase was cut. This is the only record with any failed check.

**Class B — conforming baseline at high per-step cost, ~1.50× (attempts 2, 3, 4, and 8).** per_step_cost_ratio 1.4966 / 1.5320 / 1.4974 / 1.4960, compute_efficiency 0.583–0.624. When wall_clock stayed near 13.5–13.7 s these produced 0.8037, 0.8042, 0.8042 — a spread of only ~0.0006 across three near-identical configurations, which is a useful noise estimate. Attempt 8 shares the ~1.496 cost ratio but ran 16.51 s and dropped to 0.7843.

**Class C — moderate per-step cost reduction, ~1.26× (attempt 5, reward 0.8255).** compute_efficiency 0.7476 at wall_clock 13.7398 s. This is the single best result and sits ~0.021 above the Class B plateau — roughly thirty times the observed Class B noise, so the gain is real and not run-to-run variance.

**Class D — aggressive cost/efficiency maximisation, per_step_cost_ratio ≤ ~1.19 (attempts 6, 9, 10).** These pushed the efficiency terms to their best recorded values: attempt 6 hit per_step_cost_ratio 0.9711 and compute_efficiency 0.9465; attempt 9 hit compute_efficiency 1.0000; attempt 10 hit per_step_cost_ratio 1.0702. All three scored *below* attempt 5: 0.8059, 0.7891, 0.7393. Maximising the efficiency terms did not maximise reward.

**Class E — increased per-step cost, ~1.60× (attempt 7, reward 0.7994).** compute_efficiency 0.5579, the lowest recorded, wall_clock 14.10 s. Worse than the Class B plateau and well below attempt 5.

**Cross-cutting observation on budget.** The two lowest non-zero rewards (attempt 10 at 0.7393, attempt 8 at 0.7843) are exactly the two records with qualifying_budget / wall_clock ≥ 16.5 s (16.8995 and 16.5068). Every record with wall_clock ≤ 14.2 s scored ≥ 0.7891. Letting the qualifying budget grow past roughly 14 s costs reward regardless of what the per-step cost ratio does — attempt 10 had a good cost ratio (1.0702) and still scored worst of the non-zero set.

# 3. Checks that failed

Only attempt 1 has any failed checks. Attempts 2 through 10 each recorded an empty failed_checks list.

Primary-level failures, attempt 1:

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction".
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". This is a consequence of the previous one: with nothing crossing the threshold there is no row against which a budget position can be computed.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget".

Held-out run failures, attempt 1 (see section on perturbation outcomes below): a **ruleset** run failed **C-LOG-WELL-FORMED**, **C-TARGET-REACHED**, **C-BUDGET-RESPECTED**, and **C-NO-LATCH-CARRYOVER**; a **held_out_variant** run failed **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**.

Repeat counts. Within attempt 1, C-TARGET-REACHED failed three times (primary, ruleset run, held_out_variant run) and C-BUDGET-RESPECTED failed three times (same three places). C-PERTURBATION-REACHED, C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER failed once each. **No check has failed in more than one record.** Every one of these six named checks has held in all nine records since, so whatever attempt 1 did differently from attempt 2 is what fixed them, and none of these is an open problem — the conformance layer has been stable across nine consecutive graded records and is not what is separating the recent attempts from the best one.

Perturbation outcomes. Every record declared 2 perturbations, one of kind **ruleset** and one of kind **held_out_variant** (the runs are not identified beyond their kind, and no run can be assumed to be the same run across two records). Aggregate: 20 held-out runs across the ten records, **18 reached their threshold, 2 did not** — both failures in attempt 1. By kind: ruleset 9 of 10 reached; held_out_variant 9 of 10 reached. The ruleset kind is the one that additionally tripped C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER, which the held_out_variant kind did not; both kinds tripped C-TARGET-REACHED and C-BUDGET-RESPECTED. Since attempt 2, all_perturbations_held has been true in every record and no held-out run of either kind has failed any check.

# 4. Ruled-out directions

- **Whatever attempt 1 submitted (Class A).** Ruled out: it is the only zero, with conformance_fraction 0.0, task_pass 0.0, no qualifying budget, and a wall_clock of 89.98 s against ~13–17 s for everything else. It failed C-TARGET-REACHED, C-BUDGET-RESPECTED and C-PERTURBATION-REACHED at the primary level and additionally C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER on the ruleset held-out run. There is no reason to revisit anything resembling it, and no reward-bearing lesson in it beyond "conform and finish inside the budget", which attempts 2–10 already do.

- **Maximising compute_efficiency / driving per_step_cost_ratio to ~1.0 or below (Class D).** Ruled out as a reward-maximising objective. Attempt 6 achieved the lowest per_step_cost_ratio (0.9711), the lowest wall_clock (13.4266 s) and a compute_efficiency of 0.9465, and still scored 0.8059 — below attempt 5's 0.8255. Attempt 9 achieved compute_efficiency 1.0000, the maximum, and scored 0.7891. Attempt 10 achieved per_step_cost_ratio 1.0702 and scored 0.7393, the worst non-zero result. Three independent records show the efficiency terms improving while reward falls. Reward is not monotone in these terms and they must not be treated as proxies for it.

- **Raising per-step cost to ~1.6× (Class E, attempt 7).** Ruled out: 0.7994, below the ~0.804 Class B plateau and 0.026 below attempt 5, with the lowest compute_efficiency on record (0.5579).

- **Any change that lets wall_clock / qualifying_budget reach ~16.5 s or more.** Ruled out: the only two records in that range are attempts 8 (16.5068 s → 0.7843) and 10 (16.8995 s → 0.7393), and they are the two worst non-zero rewards. Attempt 8 in particular ran the same ~1.496 per-step cost ratio as the 0.804-scoring Class B attempts and lost ~0.020 reward on budget alone.

- **Re-running the Class B ~1.50× configuration unchanged.** Ruled out as a way to improve: three near-identical records (attempts 2, 3, 4) landed at 0.8037, 0.8042 and 0.8042, a spread of ~0.0006. That plateau is measured and stable, and it is ~0.021 below attempt 5. Repeating it will reproduce ~0.804, not beat 0.8255.

Note on what the later attempts did: attempts 6 through 10 each explored away from attempt 5's operating point (down in cost ratio, up in cost ratio, up in budget) and every one came back lower. That is exploration that has now been paid for; the answer it returned is that attempt 5's operating point was already better than its neighbours in every direction that has been probed.

# 5. Open leads

1. **Return to attempt 5's operating point and re-establish it as the base.** Target signature: per_step_cost_ratio ≈ 1.26, compute_efficiency ≈ 0.748, wall_clock and qualifying_budget ≈ 13.74 s, all conformance terms at 1.0, both held-out runs reaching. Anything that does not reproduce roughly this signature is off the best-known path. Because the Class B triple shows run-to-run noise of only ~0.0006 at a fixed configuration, a re-run landing near 0.8255 confirms the point rather than needing many repeats.

2. **Sweep the unexplored band between Class C and Class D: per_step_cost_ratio in roughly 1.10–1.35.** The measured points bracket this band — 1.1920 gave 0.7891 (but at 14.16 s), 1.2599 gave 0.8255 (at 13.74 s), 1.4960–1.5320 gave ~0.804. The interior of 1.20–1.30 at a ~13.7 s budget has not been sampled. Change one knob at a time so the cost ratio moves without the budget moving.

3. **Hold the budget floor while varying cost.** Every record with wall_clock ≤ 14.2 s scored ≥ 0.7891 and every record above 16.5 s scored ≤ 0.7843. Treat ~14 s as a hard ceiling on qualifying_budget and make cost-ratio changes that do not push through it. Attempt 5 achieved its best score at 13.74 s, not at the minimum 13.43 s, so shaving wall clock below ~13.5 s is not itself the lever (attempt 6 proves that).

4. **Look for the term that separates attempt 5 from attempt 6.** Attempt 6 was faster (13.43 s vs 13.74 s) and cheaper per step (0.9711 vs 1.2599) and yet scored 0.0196 lower. Since task_pass, validity, rule_conformance, conformance_fraction, red_line_crossed and both held-out outcomes are identical between them, the difference is carried by whatever quality-of-solution quantity the reward weighs against cost. The lead is to spend the per-step budget that attempt 5 spent — do not economise it — and to look for where extra per-step work buys solution quality rather than where it can be trimmed.

5. **Preserve, unchanged, everything that fixed attempt 1's checks.** Well-formed logging on the ruleset held-out run (C-LOG-WELL-FORMED), no state carried across between held-out runs (C-NO-LATCH-CARRYOVER), a declared threshold direction that an evaluation row actually crosses (C-TARGET-REACHED), and both declared perturbations reaching inside their own budgets (C-PERTURBATION-REACHED). These have held nine times running; any refactor that risks them risks a 0.0000, which is far larger than the ~0.02 at stake in the cost tuning.

**Call: exploit.** The best-scoring approach (attempt 5, 0.8255) has been probed in several directions and every probe came back lower, but it has not yet been re-run and refined at its own operating point — the five records after it all moved to structurally different cost regimes rather than tuning within Class C. Rebuild attempt 5's signature and tune inside the 1.20–1.35 per-step-cost band at a ≤14 s budget. Explore is not yet warranted: the scoring approaches have not stopped improving so much as been abandoned mid-tuning, and the one measured zero came from a non-conforming direction that has already been fixed and should not be re-entered.
