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

    All four attempts since have scored lower than it.
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
  2 earlier attempt(s) are not detailed here; their measured row is above.

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

    attempt 6 -- reward --
      approach: not measured -- the unverified prose below is the only account of it
      measured: nothing. This attempt produced no measurement.
      narrative: no run was graded, so the verifier recorded no check.

    attempt 7 -- reward --
      approach: not measured -- the unverified prose below is the only account of it
      measured: nothing. This attempt produced no measurement.
      narrative: no run was graded, so the verifier recorded no check.

    attempt 8 -- reward 0.5444, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 26
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Eight graded records. Six carry a reward; two produced no measurement at all.

Ranked worst to best by reward:

| Rank | Attempt | reward | standing |
|---|---|---|---|
| worst | 8 | 0.5444 | worse than an earlier attempt |
| | 4 | 0.5792 | worse than an earlier attempt |
| | 3 | 0.6279 | worse than an earlier attempt |
| | 5 | 0.6587 | worse than an earlier attempt |
| | 1 | 0.6694 | first measured attempt |
| best | 2 | **0.7155** | better than every earlier attempt |

**Attempt 2 holds the highest reward, 0.7155. That is the number to beat.**

Attempts 6 and 7 have `measurement_status: harbor_exception`. They produced **no measurement** — no reward, no conformance fraction, no perturbation units, no wall clock. They are not zero-scoring attempts and must not be treated as evidence against whatever they contained; the harness never returned a graded result for them. Two such exceptions occurred back to back, so the infrastructure path is a live risk, not a one-off.

Plainly stated regressions: attempts 3, 4, 5 and 8 each scored **lower** than an earlier attempt. Attempt 8 (0.5444) is the lowest measured reward of the run and is 0.1711 below the best (attempt 2, 0.7155). Attempt 4 (0.5792) is the second lowest. There has been no improvement over attempt 2 in any subsequent measured attempt.

Supporting terms for every measured record (all six): `task_pass` 1.0, `validity` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `primary_target_reached` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, `all_perturbations_held` true, `perturbations_declared` 2.0. Nothing has ever failed correctness or conformance. The entire spread in reward — 0.5444 to 0.7155 — comes from the cost/efficiency side of the score, not from correctness.

Cost profile per measured attempt (`compute_efficiency` / `per_step_cost_ratio` / `wall_clock_sec` = `qualifying_budget`):

- Attempt 1: 0.5488 / 1.5134 / 17.4264 → reward 0.6694
- Attempt 2: 0.6205 / 1.5175 / 17.4531 → reward 0.7155
- Attempt 3: 0.6033 / 1.5225 / 20.3003 → reward 0.6279
- Attempt 4: 0.8832 / 1.1656 / 17.5121 → reward 0.5792
- Attempt 5: 0.6098 / 1.6262 / 20.5293 → reward 0.6587
- Attempt 8: 0.9679 / 0.9674 / 26.0978 → reward 0.5444

# 2. Approach classes tried

The records supply measured cost/efficiency terms but no source, so the approaches are distinguishable only by the compute signature they produced. Three distinct classes are visible, plus one non-class:

**Class A — high per-step compute, short wall clock (attempts 1 and 2).** `per_step_cost_ratio` ≈ 1.51, wall clock ≈ 17.43–17.45 s, `compute_efficiency` 0.5488 then 0.6205. This class produced both of the two best rewards, 0.6694 and 0.7155. Between attempt 1 and attempt 2 the wall clock was essentially unchanged (+0.027 s) and the per-step ratio essentially unchanged (+0.004), but `compute_efficiency` rose 0.5488 → 0.6205 and reward rose 0.6694 → 0.7155. Whatever changed between 1 and 2 bought efficiency without lengthening the run or cheapening the step, and that is the only change in the record set that improved reward.

**Class B — same per-step compute, longer wall clock (attempts 3 and 5).** `per_step_cost_ratio` 1.5225 and 1.6262, wall clock 20.3003 s and 20.5293 s, `compute_efficiency` 0.6033 and 0.6098 — i.e. efficiency comparable to attempt 2 but roughly 2.9 s more wall clock. Rewards 0.6279 and 0.6587, both below attempt 2. This class holds the per-step cost of Class A while spending ~17 % more wall clock, and loses 0.06–0.09 reward for it.

**Class C — cheapen the step, maximise compute_efficiency (attempts 4 and 8).** Attempt 4 drove `per_step_cost_ratio` down to 1.1656 and `compute_efficiency` up to 0.8832 at an unchanged wall clock of 17.5121 s; reward fell to 0.5792. Attempt 8 pushed further — `per_step_cost_ratio` 0.9674 (the only sub-1.0 value recorded) and `compute_efficiency` 0.9679 (the highest recorded) — but wall clock ballooned to 26.0978 s, the longest of any attempt, and reward fell to 0.5444, the worst measured. This class is the clearest measured finding of the run: **`compute_efficiency` is not the reward.** Pushing it from 0.6205 to 0.9679 cost 0.1711 of reward.

**Non-class — attempts 6 and 7.** Both terminated as `harbor_exception` with no measurement. Nothing can be inferred about their approach from the terms; they are not evidence for or against any hypothesis.

# 3. Checks that failed

No named check failed in any record. `failed_checks` is empty in all eight, including both harbor-exception records. `rule_conformance` is 1.0 and `conformance_fraction` is 1.0 in all six measured records, `validity` is 1.0, `red_line_crossed` is 0.0, and `zero_reason_code` is 0 throughout. There is therefore no repeated named check to point at, and no conformance defect to fix — the submissions are all valid and rule-conforming, and the reward gap is entirely a cost/efficiency matter.

The only non-completion in the set is the pair of `harbor_exception` results at attempts 6 and 7. These are a harness-level exception, not a verifier check: the verifier named no reason and returned no metrics. Two consecutive occurrences say the exception is reproducible enough to guard against — keep the submission's imports, runtime and I/O footprint conservative and close to the shapes that measured cleanly (attempts 1–5, 8) — but the records give no reason string, so its cause cannot be attributed from these terms.

Perturbation outcomes, by kind and in aggregate: every measured record declared 2 perturbations and ran two held-out units, one of kind `held_out_variant` and one of kind `ruleset`. Across the six measured records that is six `held_out_variant` runs and six `ruleset` runs, **twelve units in total, all of which reached their threshold with empty `failed_checks`**, and `all_perturbations_held` true in every case. Neither kind has ever failed, and no check has ever stopped either kind. The two harbor-exception records carry an empty `perturbation_units` list — those runs never happened, rather than having failed. Robustness to held-out variation and to ruleset variation is not a constraint that has bound so far; it should be preserved but is not where reward is being lost.

# 4. Ruled-out directions

**Maximising `compute_efficiency` as if it were the objective — ruled out.** Attempt 4 raised it to 0.8832 and scored 0.5792; attempt 8 raised it to 0.9679 and scored 0.5444. Both are worse than attempt 2's 0.7155 at `compute_efficiency` 0.6205. Two independent data points, moving in the same direction, both regressing. Do not chase this term.

**Cheapening the per-step cost below roughly 1.5 — ruled out.** Every attempt with `per_step_cost_ratio` ≥ 1.51 (attempts 1, 2, 3, 5) scored between 0.6279 and 0.7155. Both attempts that cut it (4 at 1.1656, 8 at 0.9674) landed in the bottom two, 0.5792 and 0.5444. Cutting per-step work appears to trade away whatever quality term the reward actually rewards.

**Spending more wall clock at the Class-A per-step cost — ruled out.** Attempts 3 and 5 held the per-step ratio at 1.52–1.63 but ran 20.30 s and 20.53 s against attempt 2's 17.45 s, and scored 0.6279 and 0.6587 — both below 0.7155. `qualifying_budget` equals `wall_clock_sec` exactly in every record, so wall clock is directly the budget being charged. The ~17.4 s band is where the two best results sit.

**Any combination that lengthens wall clock past ~20 s — ruled out on present evidence.** The three longest runs (3 at 20.30 s, 5 at 20.53 s, 8 at 26.10 s) produced 0.6279, 0.6587 and 0.5444. None beat any of the three shortest runs' best result. The longest run produced the worst reward.

**Treating attempts 6 and 7 as failed approaches — ruled out as an inference.** They produced no measurement. Whatever they contained is untested, not disproven, and could legitimately be retried provided the runtime footprint is kept conservative.

# 5. Open leads

1. **Re-derive attempt 2's operating point first and confirm it reproduces at ≈0.7155.** Target signature: `per_step_cost_ratio` ≈ 1.51–1.52, `wall_clock_sec` ≈ 17.4–17.5 s, `compute_efficiency` ≈ 0.62. That means a training loop that does substantial work per step (roughly 1.5× the reference per-step cost) and finishes the whole run in about 17.5 seconds — i.e. relatively few, relatively heavy steps rather than many cheap ones. Establishing this baseline is the precondition for any further tuning, because five of the six measured attempts drifted away from it and all five scored lower.

2. **Exploit the one gradient that actually worked: attempt 1 → attempt 2.** Holding wall clock and per-step cost fixed, `compute_efficiency` moved 0.5488 → 0.6205 and reward moved 0.6694 → 0.7155 (+0.0461). This is the only measured improvement in the run. The lever is efficiency gained *without* touching either the step's cost or the total runtime — e.g. removing dead work, avoiding redundant passes over data, eliminating unnecessary host/device transfers or recomputation, tightening the data pipeline so the same optimisation work happens with less overhead. Push a small increment further along exactly this axis: aim for `compute_efficiency` around 0.65–0.72 while pinning `per_step_cost_ratio` at ~1.51 and wall clock at ~17.4 s. Do not let it drift toward the 0.88–0.97 region — attempts 4 and 8 show that region is reached by cheapening the step, which is what destroys the reward.

3. **Probe the wall-clock floor below 17.4 s, at unchanged per-step cost.** No attempt has ever run faster than 17.4264 s. Since `qualifying_budget` is identical to `wall_clock_sec`, shortening the run is a direct saving, and the evidence that longer runs hurt (leads 3–4 in section 4) implies the reward is sensitive to this term. The untested question is whether ~15–16 s is reachable while keeping `per_step_cost_ratio` ≈ 1.5 — that is, fewer heavy steps rather than lighter steps. This is a genuinely unexplored corner: every efficiency gain so far has been bought by cheapening the step, never by shortening the run at constant step cost. Guard it with the fact that `task_pass` and `primary_target_reached` must stay at 1.0 and both perturbation kinds must keep reaching threshold; a shortened run that drops `primary_target_reached` would be a far worse trade than the 0.0461 on offer.

4. **Bracket the per-step cost between 1.17 and 1.51.** Reward is 0.5792 at 1.1656 and 0.7155 at 1.5175, but nothing has been measured in between. If there is a plateau near 1.3–1.4 that keeps the quality term intact while trimming budget, it is unmeasured. Lower priority than leads 1–3 because the direction of the known evidence is unfavourable.

5. **Keep the submission's runtime footprint minimal to avoid another `harbor_exception`.** Two consecutive attempts returned no measurement, which is strictly worse than a mediocre score because it yields no information at all. Prefer standard, already-exercised library calls and avoid anything that lengthens import time, touches the filesystem or network, or spawns subprocesses. Attempts 1–5 and 8 all measured cleanly, so their structural shape is known-safe.

**Call: exploit.** The best-scoring approach class (Class A, attempts 1 and 2) has not been exhausted — it was abandoned after attempt 2 in favour of Class B and Class C, both of which regressed, and it has exactly one measured improvement direction (attempt 1 → attempt 2) that was never followed up. There is no conformance defect to repair and no perturbation kind failing, so the whole of the remaining headroom is in the cost/efficiency terms of an already-working, already-conforming solution. Reconstruct attempt 2's operating point, then advance along the efficiency-at-fixed-step-cost axis and, if safe, the wall-clock-floor axis. Explicitly do not repeat Class C: raising `compute_efficiency` by cheapening the step has now been measured twice and regressed both times, and repeating it without changing what caused the regression would be neither exploring nor exploiting.
