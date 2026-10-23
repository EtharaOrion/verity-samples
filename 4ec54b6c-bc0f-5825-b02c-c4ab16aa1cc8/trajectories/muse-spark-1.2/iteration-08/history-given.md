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

    All five attempts since have scored lower than it.
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

    attempt 7 -- reward --
      approach: not measured -- the unverified prose below is the only account of it
      measured: nothing. This attempt produced no measurement.
      narrative: no run was graded, so the verifier recorded no check.

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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 9.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Nine graded submissions. Seven carry a reward; two do not.

Ordered worst to best by reward:

| Rank | Attempt | reward |
|---|---|---|
| 1 (worst) | 9 | 0.5164 |
| 2 | 8 | 0.5444 |
| 3 | 4 | 0.5792 |
| 4 | 3 | 0.6279 |
| 5 | 5 | 0.6587 |
| 6 | 1 | 0.6694 |
| 7 (best) | 2 | 0.7155 |

**Attempt 2 holds the highest reward at 0.7155, and it is the one to beat.**

Attempts 6 and 7 have `measurement_status: harbor_exception`. They produced **no measurement at all** — no reward, no conformance fraction, no perturbation units, no wall clock. They are not zeros and must not be counted as failures of the algorithm; they are records with nothing measured in them.

Direction of travel, stated plainly: after attempt 2 set the high mark, **every subsequent measured attempt scored lower than an earlier attempt.** Attempt 3 (0.6279) is below attempt 2 and below attempt 1. Attempt 4 (0.5792) is below both. Attempt 5 (0.6587) is below attempts 1 and 2. Attempt 8 (0.5444) is below every clean earlier attempt. Attempt 9 (0.5164) is the lowest of all. The verifier's own `standing_against_best_so_far` reads `worse_than_an_earlier_attempt` for attempts 3, 4, 5, 8 and 9. There has been no improvement over attempt 2 since attempt 2.

Supporting terms for the measured attempts:

| Attempt | reward | compute_efficiency | per_step_cost_ratio | wall_clock_sec | task_pass | rule_conformance |
|---|---|---|---|---|---|---|
| 1 | 0.6694 | 0.5488 | 1.5134 | 17.426 | 1.0 | 1.0 |
| 2 | 0.7155 | 0.6205 | 1.5175 | 17.453 | 1.0 | 1.0 |
| 3 | 0.6279 | 0.6033 | 1.5225 | 20.300 | 1.0 | 1.0 |
| 4 | 0.5792 | 0.8832 | 1.1656 | 17.512 | 1.0 | 1.0 |
| 5 | 0.6587 | 0.6098 | 1.6262 | 20.529 | 1.0 | 1.0 |
| 8 | 0.5444 | 0.9679 | 0.9674 | 26.098 | 1.0 | 1.0 |
| 9 | 0.5164 | 0.6647 | 1.4988 | 17.122 | **0.0** | **0.8571** |

`validity` is 1.0 and `red_line_crossed` is 0.0 on every measured attempt; `zero_reason_code` is 0 throughout. No attempt has ever been invalidated or zeroed.

# 2. Approach classes tried

The records carry measured terms only, so the approach classes are distinguishable by their cost/latency signatures rather than by source text. Grouping records that behave the same way as one entry:

**Class A — the baseline operating point (~17.4 s wall clock, per-step cost ratio ≈ 1.51, compute efficiency 0.55–0.62).** Attempts 1 and 2. Both fully conformant, both reached the primary target, both held all perturbations. This class produced the two best rewards on record (0.6694 and 0.7155). Attempt 2 is a small refinement of attempt 1 within this class: cost ratio essentially unchanged (1.5134 → 1.5175), wall clock essentially unchanged (17.426 → 17.453), compute efficiency up (0.5488 → 0.6205), reward up by 0.0461. This is the only measured step in the whole record that improved on the incumbent.

**Class B — longer-running variants (~20.3–20.5 s wall clock, cost ratio 1.52–1.63).** Attempts 3 and 5. Same conformance and perturbation profile as Class A, but roughly 3 s more wall clock and rewards of 0.6279 and 0.6587 — both below attempt 2 and below attempt 1. Two independent samples of "spend more wall clock per run," two results worse than the baseline.

**Class C — cost-reduction / efficiency-maximising variants.** Attempts 4 and 8. These drove `per_step_cost_ratio` down hard (1.1656 and 0.9674 against the ~1.51 baseline) and pushed `compute_efficiency` to the highest values on record (0.8832 and 0.9679). Rewards were 0.5792 and 0.5444 — the second-worst and third-worst overall, and the worst two among fully conformant attempts. Attempt 8 additionally ran the longest wall clock on record, 26.098 s, despite the sub-1.0 cost ratio.

**Class D — a variant with module-level executable code.** Attempt 9. Cost signature back near baseline (cost ratio 1.4988, wall clock 17.122 s, the fastest on record), but it broke the API-surface check, lost `task_pass` (0.0) and dropped `rule_conformance` to 0.8571. Reward 0.5164, the lowest recorded.

**Class E — two submissions that never reached measurement.** Attempts 6 and 7, both `harbor_exception`. Whatever they contained, the harness raised before any term was produced. Two consecutive records with no data. There is no failed check attached to either, so nothing in the record identifies the cause beyond "the run did not complete under the harness."

# 3. Checks that failed

One named check has ever failed, and it failed exactly once:

- **`C-API-SURFACE`** — verifier's reason: *"module-level statements outside imports, constants, and permitted definitions."* Failed on attempt 9 only. Its consequences in that record were `rule_conformance` 0.8571 (six of seven rules held, `conformance_fraction` still reported 1.0 for the perturbation set) and `task_pass` 0.0.

Because it appears in one record and one only, it is not the recurring finding of this loop — it is a single self-inflicted regression from putting executable statements at module scope in the submission file. Attempts 1–5 and 8 held every check with `failed_checks: []`, so the conformant shape is demonstrably reachable and was reached six times.

No check failed on attempts 6 and 7: their `failed_checks` list is empty because nothing was checked. Do not read that emptiness as a pass.

# 4. Ruled-out directions

**Maximising compute efficiency / minimising per-step cost.** Ruled out. The two attempts that pushed hardest on this (attempt 4 at compute_efficiency 0.8832 / cost ratio 1.1656, attempt 8 at 0.9679 / 0.9674) returned 0.5792 and 0.5444 — the two lowest rewards among conformant attempts, against 0.7155 for the baseline at compute_efficiency 0.6205 and cost ratio 1.5175. Across the seven measured records the relationship runs the wrong way: higher compute efficiency has accompanied lower reward, without exception. Cheapening the per-step work is not what the reward pays for, and the harness never penalised the more expensive baseline for cost — it reached its target and held every perturbation at cost ratio ≈ 1.52.

**Extending wall clock into the ~20 s band.** Ruled out on two independent samples. Attempts 3 (20.300 s, 0.6279) and 5 (20.529 s, 0.6587) both fall short of attempt 2 (17.453 s, 0.7155) and attempt 1 (17.426 s, 0.6694). Attempt 8 at 26.098 s is worse still at 0.5444. Nothing in the record rewards longer runs; the best three rewards all sit in the 17.4–17.5 s band.

**Any module-level executable statement in the submission file.** Ruled out by `C-API-SURFACE`. The permitted module scope is imports, constants and permitted definitions. Anything else there costs `task_pass` outright, as it did on attempt 9 (0.5164, the worst result on record) — note that attempt 9 was otherwise the fastest run measured, so speed does not compensate for this.

**Re-submitting whatever produced the harbor exceptions.** Attempts 6 and 7 both returned `harbor_exception` back to back and yielded no measurement whatsoever. Repeating a construct that prevents measurement is neither exploration nor exploitation — it buys no information and no reward. The record does not say what triggered it, so the mitigation is to keep the submission structurally plain and inside the stub's declared contract rather than to guess at the trigger.

# 5. Open leads

**Return to the attempt-2 operating point and refine within it.** That is the only class that has ever improved on its predecessor. Its signature: wall clock ≈ 17.45 s, per_step_cost_ratio ≈ 1.52, compute_efficiency ≈ 0.62, full conformance, primary target reached, both perturbations held. Reconstruct that operating point first and confirm the reward lands near 0.7155 before changing anything else.

**Attack reward through solution quality at fixed cost, not through cost.** Attempts 1 → 2 held cost ratio and wall clock nearly constant (1.5134 → 1.5175; 17.426 → 17.453 s) and still gained 0.0461 reward. That is the shape of the one successful step in this record: same budget, better result. Candidate levers that fit inside a fixed step budget — better initialisation, a better-conditioned optimiser or learning-rate schedule, better regularisation, more effective use of each step — are untested at the attempt-2 budget and are the natural next probes.

**Consider a small increase in cost ratio above 1.52 while holding wall clock at ~17.4 s.** The record has never separated these two variables: every attempt that raised cost ratio also raised wall clock (attempt 5: 1.6262 / 20.529 s), and every attempt that held wall clock at ~17.5 s also lowered the cost ratio (attempt 4: 1.1656). A run at ~1.6 cost ratio and ~17.5 s wall clock would tell us which of the two is actually depressing reward in Class B and Class C. This is a genuinely open cell in the table.

**Guard the API surface mechanically.** Before submitting, verify that module scope contains nothing but imports, constants and permitted definitions — all state construction and all execution inside the permitted functions. This is cheap insurance against a repeat of the single `C-API-SURFACE` failure, which cost the worst reward on record.

**Perturbation robustness needs no work.** Across the seven measured attempts there are fourteen held-out runs beside the primary one: seven of kind `held_out_variant` and seven of kind `ruleset`. Every one of them reached its threshold and every one recorded an empty `failed_checks` list. By kind: `held_out_variant`, 7 of 7 reached, no check stopped any of them; `ruleset`, 7 of 7 reached, no check stopped any of them. In aggregate, 14 of 14 reached, zero failures, and `all_perturbations_held` is true on every measured record — including attempt 9, whose `C-API-SURFACE` failure was on the primary submission and did not stop either held-out run. Attempts 6 and 7 have empty `perturbation_units`, because nothing was run. No individual run is identified in these records and none can be tracked across records; there is no named, numbered or positioned run to point at, and none should be assumed. The conclusion is simply that neither kind is currently a constraint — generalisation is not where reward is being lost, so effort should go to the primary objective.

**Call: exploit.** Take Class A — the attempt-2 configuration — as the base and improve solution quality within it at unchanged cost and wall clock, exactly the move that took attempt 1 to attempt 2. Explore is not warranted yet: the scoring class has not stopped improving so much as been abandoned, since the five measured attempts after it all changed the cost/latency regime instead of refining the winner, and all five came back worse. One caution about the loop's own pattern: attempts 6 and 7 repeated something that produced no measurement without changing whatever made it unmeasurable, which is neither explore nor exploit and yielded nothing to learn from. Do not repeat that.
