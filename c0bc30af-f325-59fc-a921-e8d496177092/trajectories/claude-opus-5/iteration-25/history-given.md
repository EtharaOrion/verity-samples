# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.9128, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All 19 attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.7684   0.857             2 of 2         yes             25                
  2        0.8385   1.000             2 of 2         yes             74                
  3        0.0000   1.000             0 of 2         no              --                
  4        0.8719   1.000             2 of 2         yes             50                
  5 *      0.9128   1.000             2 of 2         yes             25                
  6        0.5615   0.857             2 of 2         yes             204               
  7        0.0000   1.000             0 of 2         no              --                
  8        0.7551   1.000             2 of 2         yes             78                
  9        0.0000   1.000             0 of 2         no              --                
  10       0.0000   1.000             0 of 2         no              --                
  11       0.8980   1.000             2 of 2         yes             25                
  12       0.0000   1.000             0 of 2         no              --                
  13       0.8451   1.000             2 of 2         yes             71                
  14       0.6955   1.000             2 of 2         yes             100               
  15       0.0000   1.000             0 of 2         no              --                
  16       0.0000   1.000             0 of 2         no              --                
  17       0.7919   1.000             2 of 2         yes             74                
  18       0.8794   1.000             2 of 2         yes             49                
  19       0.9121   1.000             2 of 2         yes             46                
  20       0.8661   1.000             2 of 2         yes             62                
  21       0.0000   1.000             0 of 2         no              --                
  22       0.0000   1.000             0 of 2         no              --                
  23       0.8768   1.000             2 of 2         yes             50                
  24       0.8979   1.000             2 of 2         yes             25                

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
  18 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.9121, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 46
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 22 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 2 of your last 4 attempts
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same seed run has now failed on 2 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 23 -- reward 0.8768, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 24 -- reward 0.8979, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 9 attempts (3, 7, 9, 10, 12, 15, 16, 21, 22). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

All 24 records carry `measurement_status: "measured"`, so every one has a reward; none is a "no measurement" case. Ordered worst to best by reward:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 3, 7, 9, 10, 12, 15, 16, 21, 22 | **0.0000** each | Nine attempts, all `zero_reason_code: 4`, all with `wall_clock_sec` ≈ 1690–1693 s, all `task_pass: 0.0`, `primary_target_reached: 0.0`, `conformance_fraction: 0.0` |
| 2 | 6 | **0.5615** | `wall_clock_sec` 204.09, `rule_conformance` 0.8571, `task_pass` 0.0, C-API-SURFACE failed |
| 3 | 14 | **0.6955** | qualifying budget 99.74 s |
| 4 | 8 | **0.7551** | qualifying budget 78.14 s but `wall_clock_sec` 151.50 |
| 5 | 1 | **0.7684** | qualifying budget 25.46 s, but `rule_conformance` 0.8571, `task_pass` 0.0, C-API-SURFACE failed |
| 6 | 17 | **0.7919** | 73.80 s |
| 7 | 2 | **0.8385** | 73.62 s |
| 8 | 13 | **0.8451** | 71.31 s |
| 9 | 20 | **0.8661** | 62.46 s, `compute_efficiency` 1.0 |
| 10 | 4 | **0.8719** | 50.03 s, `compute_efficiency` 1.0 |
| 11 | 23 | **0.8768** | 49.67 s |
| 12 | 18 | **0.8794** | 49.33 s |
| 13 | 24 | **0.8979** | 25.37 s |
| 14 | 11 | **0.8980** | 25.35 s |
| 15 | 19 | **0.9121** | 45.81 s, `compute_efficiency` 0.9345 |
| 16 (best) | **5** | **0.9128** | 25.34 s, `compute_efficiency` 0.7728, `per_step_cost_ratio` 0.9887, no failed checks, both perturbations held |

**Attempt 5 holds the highest reward at 0.9128. That is the attempt to beat.**

Direction of travel must be stated plainly rather than softened. Attempt 5 was the last attempt marked `better_than_every_earlier_attempt`. Every single attempt after it — 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 — carries `standing_against_best_so_far: "worse_than_an_earlier_attempt"`. Nineteen consecutive attempts have failed to beat attempt 5, and several of them (6 at 0.5615, 14 at 0.6955, 8 at 0.7551, and the nine 0.0000 records) were substantially worse, not marginally so. The only attempts ever recorded as improvements were 2 (0.8385), 4 (0.8719) and 5 (0.9128), i.e. improvement stopped early and the later two-thirds of the record is regression and re-treading.

`red_line_crossed` is 0.0 and `validity` is 1.0 in every record, including the zeros. Nothing has ever tripped a red line or produced an invalid submission.

# 2. Approach classes tried

The measured terms describe outcomes, not source code, so the classes below are grouped by the measured signature they produced. Two records with the same signature are one entry.

**Class A — fast conformant trainer, qualifying budget ≈ 25.3 s.** Attempts 5 (0.9128), 11 (0.8980), 24 (0.8979), and the non-conformant variant 1 (0.7684, 25.46 s). This class produces the highest rewards on record. Within it, `compute_efficiency` varies (5: 0.7728, 24: 0.7330, 11: 0.7043) and `per_step_cost_ratio` varies (5: 0.9887, 24: 1.1078, 11: 1.0502), while `wall_clock_sec` is nearly identical (25.34 / 25.37 / 25.35). Reward tracks `compute_efficiency` within this class: the ordering 0.7728 > 0.7330 > 0.7043 matches the reward ordering 0.9128 > 0.8979 > 0.8980 almost exactly. This is the single most actionable regularity in the data.

**Class B — mid-budget conformant trainer, 45–78 s.** Attempts 19 (45.81 s, 0.9121), 18 (49.33 s, 0.8794), 23 (49.67 s, 0.8768), 4 (50.03 s, 0.8719), 20 (62.46 s, 0.8661), 13 (71.31 s, 0.8451), 2 (73.62 s, 0.8385), 17 (73.80 s, 0.7919), 8 (78.14 s qualifying / 151.50 s wall, 0.7551). All pass every check, `task_pass: 1.0`, both perturbations held. Reward falls roughly monotonically with elapsed time inside this class. Attempt 19 is the notable outlier: at 45.81 s it scored 0.9121, essentially matching the 25 s attempts, and it carries the highest `compute_efficiency` in the class (0.9345). Attempt 17 (73.80 s, `compute_efficiency` 0.9221, reward 0.7919) and attempt 2 (73.62 s, `compute_efficiency` 0.9164, reward 0.8385) sit at near-identical time and efficiency yet 0.047 apart in reward, so time and efficiency do not fully determine the score.

**Class C — heavy/long conformant trainer, ≥ 99 s.** Attempt 14 (99.74 s, 0.6955, all checks passed) and attempt 6 (204.09 s, 0.5615, C-API-SURFACE failed). Uniformly the worst non-zero rewards. Attempt 20 with `compute_efficiency: 1.0` at 62.46 s still only reached 0.8661, so maximising `compute_efficiency` while spending more wall clock is a losing trade.

**Class D — runaway configurations that never cross the threshold.** Nine attempts (3, 7, 9, 10, 12, 15, 16, 21, 22), each 0.0000, each `zero_reason_code: 4`, each burning ≈ 1690–1693 s. The wall-clock values cluster in a 2.5-second band across all nine (1690.32 to 1692.97), which is the signature of a hard ceiling being hit rather than nine independent slow runs. `compute_efficiency` in this class is high (0.9033 to 1.0) and `per_step_cost_ratio` low (0.6826 to 0.8901) — the per-step economics look fine; nothing ever reaches the target. These nine are spread throughout the record (3rd, 7th, 9th, 10th, 12th, 15th, 16th, 21st, 22nd), i.e. this failure was re-entered repeatedly long after it was first observed.

**Class E — module-level statements at import.** Attempts 1 and 6, the only two records with `rule_conformance: 0.8571` and `conformance_fraction: 1.0`. Both reached the primary target and both held all perturbations, yet both carry `task_pass: 0.0` because of the C-API-SURFACE failure. Attempt 1 shows the cost precisely: 25.46 s of qualifying budget, comparable to attempt 5's 25.34 s, but reward 0.7684 versus 0.9128 — roughly 0.14 of reward surrendered purely to the conformance violation.

# 3. Checks that failed

**C-API-SURFACE — "module-level statements outside imports, constants, and permitted definitions". Failed 2 times** (attempts 1 and 6), with the identical reason string both times. Between attempt 1 and attempt 6 the timing profile changed completely (25.46 s versus 204.09 s, `per_step_cost_ratio` 1.0639 versus 1.3778), so whatever was altered between those two attempts is not what causes C-API-SURFACE. The cause is structural: executable statements sitting at module scope in the submission file. Only imports, constant assignments and permitted definitions may appear there; anything else — a call, a print, a loop, an `if`, a device probe, a seeding call, a config-building expression, a `torch.set_num_threads(...)`, a bare assignment computed from a function call — must move inside a function body. Note that this check does not stop the run: both records reached the primary target and held both perturbations. It costs reward through `rule_conformance` (0.8571 instead of 1.0) and forces `task_pass` to 0.0.

**C-TARGET-REACHED — "no evaluation row crosses the threshold in the declared direction". Failed 9 times as the primary check** (attempts 3, 7, 9, 10, 12, 15, 16, 21, 22) **and 18 further times across the held-out runs of those same nine records.** This is the dominant failure in the record. Across those nine attempts the `compute_efficiency` ranged from 0.9033 to 1.0 and `per_step_cost_ratio` from 0.6826 to 0.8901 — the parameters that were varied between them moved the cost profile around but never moved the outcome. Whatever was changed between those nine attempts is not what is causing C-TARGET-REACHED. Two possibilities remain consistent with the terms: either the evaluation metric is not being reported in a row the harness recognises, or it is reported but is on the wrong side of the threshold in the declared direction (a sign/direction inversion in the declaration would produce exactly this string on every row).

**C-BUDGET-RESPECTED — "no qualifying row, so no budget position exists". Failed 9 times as the primary check and 18 further times across held-out runs**, always in exactly the same nine records and always alongside C-TARGET-REACHED. In every one of those records `qualifying_budget` is the literal string `"not-measured"`. This is a downstream consequence of C-TARGET-REACHED, not an independent budget overrun: with no row crossing the threshold there is no qualifying row to position against a budget. Fixing C-TARGET-REACHED will clear this one automatically; attacking the budget directly will not.

**C-PERTURBATION-REACHED — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed 9 times**, in the same nine records. Also downstream: it is the primary-level restatement of the held-out runs' failures.

No other check identifier appears anywhere in the record. In the 15 attempts that scored above zero (1, 2, 4, 5, 6, 8, 11, 13, 14, 17, 18, 19, 20, 23, 24), the only check ever failed was C-API-SURFACE.

# 4. Ruled-out directions

**The ≈1690 s runaway configuration (Class D) — ruled out, 9 times over.** Nine separate attempts entered this state and every one returned 0.0000 with the same triple of failed checks. Nothing distinguishing them in the measured terms (`compute_efficiency` 0.9033–1.0, `per_step_cost_ratio` 0.6826–0.8901) correlates with any change in outcome. Re-entering this state without first changing what makes no evaluation row cross the threshold is not exploration and not exploitation — it is repetition of a known zero, and that is precisely what the record shows happening nine times.

**Module-level executable statements (Class E) — ruled out.** Two records, identical reason, ~0.14 of reward forfeited on attempt 1 relative to the comparable attempt 5. There is no upside to it: both records still reached target and held perturbations, so the statements bought nothing and cost `rule_conformance` and `task_pass`. Keep module scope to imports, constants and definitions only.

**Long-running conformant trainers (≥ 99 s, Class C) — ruled out.** Attempt 14 (99.74 s → 0.6955) and attempt 6 (204.09 s → 0.5615) are the worst non-zero results. Every attempt above 0.86 finished in under 63 s. Time spent is being charged against reward directly.

**Maximising `compute_efficiency` at the cost of wall clock — ruled out.** Attempt 20 achieved `compute_efficiency: 1.0` and `per_step_cost_ratio: 0.6145` (the lowest per-step cost on record) yet scored only 0.8661 at 62.46 s, below the 25 s attempts whose `compute_efficiency` was in the 0.70–0.77 range. Attempt 4 likewise hit `compute_efficiency: 1.0` at 50.03 s for 0.8719, below attempt 5's 0.9128. Perfect per-step economics do not compensate for elapsed time.

**Running past the qualifying point — ruled out.** Attempt 8 found its qualifying row at 78.14 s but ran to 151.50 s of wall clock, and scored 0.7551 — lower than attempt 2 (0.8385), which had a nearly identical qualifying budget of 73.62 s and stopped there. The extra ~73 seconds after qualifying bought a 0.083 reward loss. Stop as soon as the target is met; do not continue training or evaluating afterwards.

# 5. Open leads

**Reproduce attempt 5's operating point first.** Its measured fingerprint: `wall_clock_sec` 25.34, `qualifying_budget` 25.34 (identical, i.e. it stopped at qualifying), `compute_efficiency` 0.7728, `per_step_cost_ratio` 0.9887, `rule_conformance` 1.0, `task_pass` 1.0, both perturbations reached, no failed checks, reward 0.9128. Anything the next attempt does should be measured against landing in that ≈25 s band with clean conformance. Three separate attempts (5, 11, 24) landed within 0.03 s of each other in that band, so the band is reproducible.

**Raise `compute_efficiency` while holding the ≈25 s wall clock.** Within the 25 s band, reward orders with `compute_efficiency`: 0.7728 → 0.9128, 0.7330 → 0.8979, 0.7043 → 0.8980. Attempt 19 shows `compute_efficiency` as high as 0.9345 is achievable, and attempts 4 and 20 reached 1.0 — but all three of those paid for it with 45–62 s of wall clock. The untried combination is high `compute_efficiency` **at** ≈25 s. If that combination is reachable it should beat 0.9128; it is the most direct exploit available.

**Examine what attempt 19 did differently.** At 45.81 s it scored 0.9121, essentially tying the best while taking 80% longer than attempt 5 — it is a clear outlier above the time/reward trend of its own class (18 at 49.33 s → 0.8794, 23 at 49.67 s → 0.8768, 4 at 50.03 s → 0.8719). Its distinguishing measured terms are `compute_efficiency` 0.9345 with `per_step_cost_ratio` 0.7669. Whatever produced that efficiency-at-moderate-cost, carried into the 25 s regime, is the most promising single lead.

**Reduce `per_step_cost_ratio` in the fast band.** The three 25 s attempts had per-step ratios of 0.9887, 1.0502 and 1.1078 — all at or above 1.0, the worst per-step economics of any conformant class. Elsewhere ratios of 0.61–0.77 were achieved (attempts 20, 4, 19, 17). Bringing the fast configuration's per-step ratio down toward 0.7 while keeping the same total elapsed time would raise `compute_efficiency` and, on the within-band regularity above, the reward with it.

**Note the residual unexplained variance and do not over-fit to time alone.** Attempts 2 and 17 finished 0.18 s apart (73.62 vs 73.80) with near-identical `compute_efficiency` (0.9164 vs 0.9221) and scored 0.8385 versus 0.7919. Something not captured by elapsed time or per-step cost moved the reward by 0.047 there. Expect roughly ±0.03–0.05 of noise or hidden quality signal at fixed time; do not read a single small regression as a refuted hypothesis.

**If any target-reaching change is attempted, verify the threshold direction before spending a run.** C-TARGET-REACHED's reason names "the declared direction" explicitly and has now failed 9 times with nothing that was varied between those runs affecting it. A declared-direction or metric-reporting inversion would explain all nine identically. This is only worth touching if a change to the training body is planned at all — the currently scoring configurations already satisfy this check and must not be disturbed.

**Perturbation-unit outcomes, by kind and in aggregate.** Two held-out runs accompany each attempt, one of kind `held_out_variant` and one of kind `seed`. Across all 24 records that is 48 held-out runs: 30 reached their threshold with no failed checks (the 15 records where `all_perturbations_held` is true), and 18 did not. By kind: the `held_out_variant` runs reached in 15 records and failed in 9; the `seed` runs reached in 15 records and failed in 9 — an identical pattern for both kinds. Every one of the 18 failures carries the same pair, C-TARGET-REACHED and C-BUDGET-RESPECTED, and every one occurs in a record whose primary run also failed those checks. There is no case anywhere in the record of a held-out run failing while the primary run succeeded, and no case of one kind failing while the other held. The held-out runs are therefore not currently an independent source of risk: they fail exactly when and only when the primary configuration fails to reach the target, and both kinds fail together on the same check. Nothing in the terms identifies any individual held-out run across records, so no claim is made that any particular run recurs.

**Call: exploit.** The best-scoring approach class (Class A, the ≈25 s conformant trainer, best reward 0.9128 at attempt 5) has a clear, measured, unexploited axis of improvement — `compute_efficiency` at fixed wall clock — and a concrete donor configuration to borrow from in attempt 19. Structural exploration is not warranted: every structurally different thing tried so far either scored zero nine times over (Class D) or scored below the fast band (Classes B, C, E). The next attempt should rebuild the fast ≈25 s path, keep module scope free of executable statements so C-API-SURFACE holds, stop the moment the target is met, and push `compute_efficiency` upward from 0.7728 without letting elapsed time grow.
