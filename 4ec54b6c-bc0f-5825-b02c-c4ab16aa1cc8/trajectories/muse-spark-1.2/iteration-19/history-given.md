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

    All 16 attempts since have scored lower than it.
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
  15       0.5830   1.000             2 of 2         yes             24                
  16       0.5701   1.000             2 of 2         yes             21                
  17       0.5274   0.857             2 of 2         yes             24                
  18       0.5755   1.000             2 of 2         yes             21                
  19       0.7134   1.000             2 of 2         yes             17                
  20       0.5107   0.857             2 of 2         yes             17                

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
  15 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 18 -- reward 0.5755, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 21
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 19 -- reward 0.7134, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 20 -- reward 0.5107, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 3 attempts (9, 17, 20). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Twenty attempts were graded. Eighteen carry a measurement; two do not.

Ordered worst to best by `reward`:

| Rank | Attempt | reward | standing |
|---|---|---|---|
| 1 (worst) | 12 | 0.4962 | worse than an earlier attempt |
| 2 | 20 | 0.5107 | worse than an earlier attempt |
| 3 | 9 | 0.5164 | worse than an earlier attempt |
| 4 | 17 | 0.5274 | worse than an earlier attempt |
| 5 | 8 | 0.5444 | worse than an earlier attempt |
| 6 | 13 | 0.5590 | worse than an earlier attempt |
| 7 | 16 | 0.5701 | worse than an earlier attempt |
| 8 | 18 | 0.5755 | worse than an earlier attempt |
| 9 | 4 | 0.5792 | worse than an earlier attempt |
| 10 | 15 | 0.5830 | worse than an earlier attempt |
| 11 | 10 | 0.5983 | worse than an earlier attempt |
| 12 | 3 | 0.6279 | worse than an earlier attempt |
| 13 | 14 | 0.6426 | worse than an earlier attempt |
| 14 | 5 | 0.6587 | worse than an earlier attempt |
| 15 | 11 | 0.6639 | worse than an earlier attempt |
| 16 | 1 | 0.6694 | first measured attempt |
| 17 | 19 | 0.7134 | worse than an earlier attempt |
| 18 (best) | 2 | **0.7155** | better than every earlier attempt |

**Attempt 2 holds the highest reward, 0.7155. That is the score to beat.**

Attempts 6 and 7 have `measurement_status: harbor_exception`. They produced **no measurement at all** — no reward, no conformance figures, no perturbation units. They are not zeros and must not be treated as evidence about the approach they carried; nothing can be concluded from them either way.

The blunt shape of the record: attempt 2 set the high-water mark early and **nothing in the sixteen measured attempts that followed beat it**. Every single measured attempt from 3 onward is marked `worse_than_an_earlier_attempt`. Attempt 19 came closest at 0.7134, which is still *below* 0.7155 — that is a regression, not a tie and not progress. The long run from attempt 3 through attempt 20 is a net decline, not a climb.

Supporting terms, for the measured attempts:

- `validity` = 1.0 and `red_line_crossed` = 0.0 in every measured attempt. No attempt was ever invalidated and no red line was ever crossed.
- `primary_target_reached` = 1.0 in every measured attempt, including the four that failed a check. The primary task target has never been the obstacle.
- `task_pass` = 1.0 everywhere except attempts 9, 12, 17 and 20, where it is 0.0. In each of those four, a named check failed (see section 3), yet reward remained in the 0.4962–0.5274 band — a failed check depresses reward heavily but does not zero it.
- `zero_reason_code` = 0 in every measured attempt. Nothing has ever been zeroed out.

Cost/efficiency terms worth carrying forward, since they are the only levers the data actually distinguishes:

| Attempt | reward | wall_clock_sec | per_step_cost_ratio | compute_efficiency |
|---|---|---|---|---|
| 2 | 0.7155 | 17.45 | 1.5175 | 0.6205 |
| 19 | 0.7134 | 17.49 | 1.5834 | 0.6001 |
| 1 | 0.6694 | 17.43 | 1.5134 | 0.5488 |
| 11 | 0.6639 | 20.06 | 1.0166 | 0.8424 |
| 5 | 0.6587 | 20.53 | 1.6262 | 0.6098 |
| 14 | 0.6426 | 17.78 | 1.6303 | 0.6320 |
| 3 | 0.6279 | 20.30 | 1.5225 | 0.6033 |
| 10 | 0.5983 | 20.15 | 1.5152 | 0.5686 |
| 15 | 0.5830 | 23.70 | 1.6313 | 0.6165 |
| 4 | 0.5792 | 17.51 | 1.1656 | 0.8832 |
| 18 | 0.5755 | 20.63 | 1.5846 | 0.6466 |
| 16 | 0.5701 | 20.98 | 1.1256 | 0.8684 |
| 13 | 0.5590 | 20.60 | 1.2404 | 0.7642 |
| 8 | 0.5444 | 26.10 | 0.9674 | 0.9679 |
| 17 | 0.5274 | 23.58 | 1.2123 | 0.8228 |
| 9 | 0.5164 | 17.12 | 1.4988 | 0.6647 |
| 20 | 0.5107 | 17.39 | 1.5804 | 0.6658 |
| 12 | 0.4962 | 16.78 | 1.4886 | 0.6278 |

The clearest signal in the table: among attempts that passed every check, **short wall clock tracks high reward**. All four of the best clean scores (2, 19, 1, 14) finished in 17.4–17.8 s. Every clean attempt at 20.0 s or above scored 0.6639 or lower, and the slowest clean attempt (8, at 26.10 s) scored 0.5444, the worst clean score on record. `qualifying_budget` equals `wall_clock_sec` exactly in every measured record, so the two are the same quantity under two names.

The second clear signal is that **`compute_efficiency` near 1.0 and `per_step_cost_ratio` near 1.0 did not pay**. Attempt 8 has the best efficiency figures on record (0.9679 efficiency, 0.9674 per-step ratio) and one of the worst rewards. Attempts 4 (0.8832 / 1.1656) and 16 (0.8684 / 1.1256) are the same story. The best-scoring attempts sit at mediocre efficiency (0.60–0.63) and per-step ratios around 1.5–1.6. Whatever `compute_efficiency` is measuring, driving it upward has consistently coincided with slower wall clock and lower reward — attempt 11 (0.8424 efficiency, 0.6639) is the only high-efficiency attempt that scored respectably, and it still lost to attempt 2.

I hold only these measured terms, not the source of any attempt, so the groupings in section 2 are by metric signature and by the checks each attempt tripped.

# 2. Approach classes tried

**Class A — the fast, ordinary-cost configuration (attempts 1, 2, 19, and 14 at its edge).** Wall clock 17.4–17.8 s, `per_step_cost_ratio` 1.51–1.63, `compute_efficiency` 0.55–0.63, all checks held, all perturbations reached. This class produced the top four clean scores: 0.7155, 0.7134, 0.6694, 0.6426. It is the only class that has ever exceeded 0.67. Attempt 2 is its best instance. The spread *within* the class (0.6426 to 0.7155) is wide despite near-identical cost signatures, which means something other than wall clock and per-step cost is moving reward inside this band — most likely the quality of the trained result itself, which none of the supplied terms expose directly.

**Class B — the same fast configuration slowed to ~20 s (attempts 3, 10, 18, and 5 at 20.5 s).** Cost signature nearly identical to class A (`per_step_cost_ratio` 1.51–1.63, efficiency 0.57–0.65) but 2.5–3 s more wall clock. Rewards 0.5755, 0.5983, 0.6279, 0.6587 — the whole band sits below class A's band. Nothing else in the terms distinguishes B from A, so the extra ~3 s of wall clock is the visible difference and it costs roughly 0.05–0.10 of reward.

**Class C — efficiency-optimised / low per-step-cost configurations (attempts 4, 8, 11, 13, 16, and 17 which additionally failed a check).** `per_step_cost_ratio` pushed down to 0.97–1.24 and `compute_efficiency` pushed up to 0.76–0.97. Every one of these was slower in wall clock than class A except attempt 4 (17.51 s), and every one scored below attempt 2. Best of the class is attempt 11 at 0.6639 (20.06 s, ratio 1.0166); worst clean is attempt 8 at 0.5444 (26.10 s, ratio 0.9674). Attempt 4 is the instructive one: it achieved class-A wall clock (17.51 s) *and* strong efficiency (0.8832) and still scored only 0.5792, well below attempt 2's 0.7155 at the same wall clock. So the efficiency reshaping did not merely trade time for reward — it appears to have cost reward at fixed time as well.

**Class D — slow, high-cost configurations (attempt 15 at 23.70 s / ratio 1.6313, and attempt 17 at 23.58 s).** These combine the long wall clock of class B or worse with no efficiency benefit. Attempt 15 scored 0.5830. This is the weakest region of the clean space.

**Class E — configurations that put executable statements at module level (attempts 9, 17, 20).** Metric signatures otherwise span classes A and C (attempt 9 at 17.12 s / ratio 1.4988; attempt 20 at 17.39 s / ratio 1.5804; attempt 17 at 23.58 s / ratio 1.2123). All three tripped `C-API-SURFACE`, all three had `task_pass` driven to 0.0 and `rule_conformance` cut to 0.8571, and all three scored in the 0.5107–0.5274 band. Attempts 9 and 20 are especially costly: they had class-A wall clocks (17.12 s and 17.39 s) — the profile that produced the best scores — and were dragged to near the bottom of the table purely by the check failure.

**Class F — a configuration that broke a held-out perturbation (attempt 12).** Fastest wall clock on record at 16.78 s, `per_step_cost_ratio` 1.4886, `compute_efficiency` 0.6278, primary target still reached. But `all_perturbations_held` = false, `conformance_fraction` = 0.5, `task_pass` = 0.0, and reward 0.4962 — the worst on record. Whatever made it the fastest also made it fail to generalise to the held-out run.

**Class G — attempts 6 and 7, which raised a harbor exception.** No measurement was produced for either. Their approach cannot be classed, evaluated, or ruled in or out from these terms.

# 3. Checks that failed

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions". This check has now failed three times: attempts 9, 17 and 20.** This is the single most important finding in the record. The three attempts have materially different cost profiles — 17.12 s at ratio 1.4988 and efficiency 0.6647; 23.58 s at ratio 1.2123 and efficiency 0.8228; 17.39 s at ratio 1.5804 and efficiency 0.6658 — spanning both the fast class-A profile and the slow efficiency-optimised class-C profile. **Whatever was changed between those three attempts is therefore not what is causing this failure.** It is not a consequence of the training algorithm, the cost tuning, the step schedule, or the runtime. It is caused by the submission file containing statements at module scope that are not imports, not constant assignments, and not permitted definitions — top-level calls, prints, seeding statements, `if`-blocks, loops, self-tests, timing harnesses, demo or `__main__`-style code executed on import, anything of that shape. Each occurrence set `rule_conformance` to 0.8571 and `task_pass` to 0.0 and cost roughly 0.19–0.20 of reward against attempts of comparable speed. Attempt 20 in particular ran at 17.39 s — a class-A speed that has otherwise produced 0.67–0.72 — and scored 0.5107 solely because of this. The fix is mechanical and entirely under the author's control: put every executable statement inside a function or method, leave the module body containing only imports, constant assignments, and function/class definitions.

**`C-PERTURBATION-REACHED` — "1 of 2 declared perturbations reached their own threshold inside their own budget". Failed once, in attempt 12.** This drove `conformance_fraction` to 0.5, `all_perturbations_held` to false, and `task_pass` to 0.0, producing the lowest reward on record, 0.4962.

**`C-TARGET-REACHED` and `C-BUDGET-RESPECTED` — failed once each, both inside attempt 12's held-out run.** These are the unit-level checks underlying the `C-PERTURBATION-REACHED` failure above: the held-out run neither reached its own threshold nor stayed inside its own budget.

No other check has ever failed. `validity`, `red_line_crossed` and `primary_target_reached` have never been an issue in any measured attempt.

# 4. Ruled-out directions

**Maximising `compute_efficiency` / driving `per_step_cost_ratio` toward or below 1.0.** Ruled out. Class C tried this repeatedly — attempts 8 (0.9679 efficiency, 0.9674 ratio, reward 0.5444), 4 (0.8832 / 1.1656, reward 0.5792), 16 (0.8684 / 1.1256, reward 0.5701), 13 (0.7642 / 1.2404, reward 0.5590) — and every instance scored below attempt 2's 0.7155, which sits at a mediocre 0.6205 efficiency and a ratio of 1.5175. Attempt 8 achieved the best efficiency figures on record and one of the worst rewards. Attempt 4 matched the winning wall clock while raising efficiency and still lost 0.14 of reward. Efficiency is not the graded quantity and pushing it has consistently coincided with lower reward.

**Letting wall clock drift to 20 s or beyond.** Ruled out for any clean configuration. Every clean attempt at ≥20.0 s scored ≤0.6639; every score above 0.67 came from an attempt finishing in 17.4–17.5 s. Attempts 3, 5, 10, 11, 13, 15, 16 and 18 all sit in the 20–24 s range and none beat attempt 2. The slowest, attempt 8 at 26.10 s, is the worst clean result.

**Leaving executable code at module scope.** Ruled out absolutely. Three separate attempts (9, 17, 20) died on `C-API-SURFACE` for exactly this, each losing `task_pass` outright. Attempt 20's 17.39 s runtime shows a class-A-speed submission being thrown away by a purely structural defect. There is no upside to this and it has cost three graded attempts.

**Trading generalisation for raw speed.** Ruled out on attempt 12's evidence: at 16.78 s it is the fastest submission on record and it is also the only one whose held-out run failed both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, producing the worst reward of all, 0.4962. Speed below roughly 17 s bought by weakening the training so that a held-out variant no longer converges inside its own budget is strictly negative.

**Re-running the class-B configuration (class-A cost signature, ~20 s wall clock).** Ruled out as a way to beat 0.7155: four separate instances (3, 5, 10, 18) all landed between 0.5755 and 0.6587.

**Nothing about attempts 6 and 7 is ruled out.** They produced no measurement, so they carry no evidence in either direction. If either represented a genuinely distinct idea, that idea remains untested, not refuted.

# 5. Open leads

**Reconstruct the attempt-2 profile as the baseline, and treat it as the target to beat.** Its measured signature is: wall clock ≈17.45 s, `per_step_cost_ratio` ≈1.518, `compute_efficiency` ≈0.620, all checks held, both perturbations reached, `task_pass` 1.0. Attempts 1 (17.43 s, ratio 1.513, reward 0.6694) and 19 (17.49 s, ratio 1.583, reward 0.7134) sit in the same envelope and are the second and third best clean results, so this envelope is reproducible and is where all the reward lives. Any new submission should aim to land in it before attempting anything else.

**Enforce the module-scope discipline mechanically, before anything else.** Write the file so the module body contains only imports, constant assignments, and `def`/`class` definitions. No top-level calls, no seeding or configuration executed at import, no `if __name__ == "__main__"` block, no timing or self-test scaffolding, no top-level loops or conditionals. Read the finished file top to bottom and confirm every line at column zero is an import, a constant, a `def` or a `class`. Three attempts have been lost to `C-API-SURFACE`; this alone recovers ~0.19 of reward on a fast submission.

**Look for reward inside the 17.4–17.8 s band rather than by changing the band.** Attempts 1, 2, 19 and 14 all sit in that band with near-identical cost signatures yet span 0.6426 to 0.7155. That 0.073 spread is not explained by any supplied term — wall clock, per-step ratio and efficiency barely move across them. Something in the training itself (initialisation, learning-rate schedule, number or size of steps, regularisation, the final model's accuracy margin over the target) is doing the work. That is the most promising unexplored axis: hold the cost signature fixed at attempt 2's and vary the learning dynamics, rather than varying the cost.

**Keep a margin on the held-out variant.** Attempt 12 shows the failure mode of cutting too close: the held-out run must reach its own threshold inside its own budget, not just the primary target. Attempt 2 achieved this at 17.45 s, so the margin exists at that speed; do not shave below roughly 17.4 s in pursuit of it.

**Do not chase efficiency metrics.** `compute_efficiency` and `per_step_cost_ratio` are reported but the evidence says optimising them is counterproductive. Let them land wherever the attempt-2-style configuration puts them (≈0.62 and ≈1.52) and ignore them.

**Perturbation outcomes, by kind and in aggregate.** Every measured attempt declared exactly two perturbation units, one of kind `held_out_variant` and one of kind `ruleset`. Across the eighteen measured attempts that is thirty-six units, of which thirty-five reached their threshold. Units of kind `ruleset` reached in all eighteen measured attempts and have never failed any check. Units of kind `held_out_variant` reached in seventeen of eighteen; the single failure is in attempt 12, where a `held_out_variant` unit failed both `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. So the only perturbation kind that has ever failed is `held_out_variant`, and it failed on target-reaching and budget-respecting — generalisation and cost on unseen data, not rule compliance. Attempts 6 and 7 reported no perturbation units at all, consistent with their producing no measurement.

---

**Call: exploit.**

The reason is direct. The best score, attempt 2 at 0.7155, came from a specific and reproducible measured profile — a ~17.45 s run at a per-step cost ratio near 1.52 with all checks held — and attempts 1, 19 and 14 confirm that profile is not a fluke. Everything that followed either moved away from that profile (classes B, C, D, all worse) or destroyed an otherwise-good run with a structural defect (class E's three `C-API-SURFACE` failures, class F's held-out failure). The single largest recoverable loss on the record is `C-API-SURFACE`: three attempts, one of them at 17.39 s, thrown away for module-level statements. Fixing that one thing while sitting in attempt 2's cost envelope is the highest-value move available.

One caution about the pattern in the record itself: `C-API-SURFACE` failed at attempt 9, again at attempt 17, and again at attempt 20, across attempts whose cost profiles differ substantially. That is the same defect reintroduced three times while other things were being tuned. Reintroducing it again would not be exploiting and would not be exploring — it would be repeating a known failure without changing what causes it. The next attempt must not do that.
