# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 14 -- reward 0.8820, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 7
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.0000   1.000             0 of 2         no              --                
  2        0.8037   1.000             2 of 2         yes             13                
  3        0.8042   1.000             2 of 2         yes             14                
  4        0.8042   1.000             2 of 2         yes             14                
  5        0.8255   1.000             2 of 2         yes             14                
  6        0.8059   1.000             2 of 2         yes             13                
  7        0.7994   1.000             2 of 2         yes             14                
  8        0.7843   1.000             2 of 2         yes             17                
  9        0.7891   1.000             2 of 2         yes             14                
  10       0.7393   1.000             2 of 2         yes             17                
  11       0.7997   1.000             2 of 2         yes             17                
  12       0.7443   1.000             2 of 2         yes             17                
  13       0.0000   1.000             2 of 2         yes             37                
  14 *     0.8820   1.000             2 of 2         yes             7                 
  15       0.7288   0.857             2 of 2         yes             5                 

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
  10 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 5 -- reward 0.8255, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 6 -- reward 0.8059, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 13
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 13 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 37
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-BUDGET-RESPECTED -- the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1
        C-PER-STEP-COST-CEILING -- per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0

    attempt 15 -- reward 0.7288, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 5
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-NO-SHAPE-FINGERPRINT -- the submission fingerprints the model by shape

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (1, 13). Whatever has been
      changing between them is not what is causing it.
    C-NO-SHAPE-FINGERPRINT failed on attempt 15.
    C-PER-STEP-COST-CEILING failed on attempt 13.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Fifteen graded records, all carrying a reward. Ordered worst to best:

| Rank | Attempt | reward | Notes from the measured terms |
|---|---|---|---|
| 1 (worst) | 13 | 0.0000 | `red_line_crossed` 1.0, `validity` 0.0, `task_pass` 0.0, `zero_reason_code` 1; wall clock 37.2022 s; per-step cost ratio 7.1852 |
| 1 (worst, tied) | 1 | 0.0000 | `task_pass` 0.0, `primary_target_reached` 0.0, `conformance_fraction` 0.0, `zero_reason_code` 4; wall clock 89.9778 s |
| 3 | 15 | 0.7288 | fastest run of all (4.6808 s) but `rule_conformance` 0.8571, `task_pass` 0.0 |
| 4 | 10 | 0.7393 | wall clock 16.8995 s |
| 5 | 12 | 0.7443 | wall clock 16.9433 s |
| 6 | 8 | 0.7843 | wall clock 16.5068 s |
| 7 | 9 | 0.7891 | wall clock 14.1599 s, `compute_efficiency` 1.0 |
| 8 | 7 | 0.7994 | wall clock 14.1032 s |
| 9 | 11 | 0.7997 | wall clock 17.0029 s |
| 10 | 2 | 0.8037 | wall clock 13.4877 s |
| 11 | 4 | 0.8042 (0.8041887) | wall clock 13.6584 s |
| 12 | 3 | 0.8042 (0.8042363) | wall clock 13.6621 s |
| 13 | 6 | 0.8059 | wall clock 13.4266 s, `compute_efficiency` 0.9465, per-step ratio 0.9711 |
| 14 | 5 | 0.8255 | wall clock 13.7398 s |
| 15 (best) | 14 | **0.8820** | wall clock 6.6280 s, per-step ratio 1.8690, all checks held |

**Attempt 14 holds the highest reward, 0.8820. That is the score to beat.**

Directional facts that must not be softened: attempts 4, 6, 7, 8, 9, 10, 11, 12, 13 and 15 each carry `standing_against_best_so_far` = `worse_than_an_earlier_attempt`. In particular, everything graded after attempt 14 went **down**: attempt 15 scored 0.7288, which is 0.1532 below the best. Attempt 13 scored 0.0000, a regression to nothing from the ~0.80 band that preceded it. Only attempts 2, 3, 5 and 14 ever improved on everything before them.

A measurement-status caveat: attempts 1 and 2 carry `measurement_status` = `measured_phase_cut` rather than plain `measured`; every other record is `measured`. Both phase-cut records do carry reward numbers (0.0000 and 0.8037) and are reported above as such, but their status is not identical to the rest and their numbers should be treated as slightly less authoritative than the twelve fully `measured` ones. No record in this set is missing a measurement.

The strongest signal in the table is that **reward tracks wall clock / `qualifying_budget` inversely, and does not track `compute_efficiency`**. Attempt 9 had `compute_efficiency` 1.0000 and scored 0.7891; attempt 14 had `compute_efficiency` 0.5031 — the second-lowest of any scoring run — and scored 0.8820 because it finished in 6.63 s. Attempt 6 had a per-step cost ratio below 1.0 (0.9711) and still only reached 0.8059 at 13.43 s. Every run in the 13.4–17.0 s band landed between 0.7393 and 0.8059 regardless of its efficiency numbers. Time-to-qualify is the lever; per-step efficiency is not.

## 2. Approach classes tried

I was given measured terms only, not source, so these classes are grouped by their measured signature. Five distinct classes appear.

**Class A — did not reach the target at all (attempt 1).** `primary_target_reached` 0.0, `conformance_fraction` 0.0, `zero_reason_code` 4, and a wall clock of 89.98 s, roughly six times any later run. Both declared perturbation runs also failed to reach. This is the only class that never produced a qualifying evaluation row. `rule_conformance` was 1.0 and `per_step_cost_ratio` was 1.0194, so the failure was not a rule violation or a cost blow-up — the run simply never crossed the threshold in the declared direction within its budget. Whatever it did, it was too slow to converge and never emitted a qualifying row.

**Class B — the conformant mid-band plateau (attempts 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12).** Eleven records, all with `task_pass` 1.0, `validity` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `red_line_crossed` 0.0, zero failed checks, and both perturbation runs reaching. Wall clocks cluster in 13.43–17.00 s and rewards in 0.7393–0.8059. Within this band the variation is essentially wall-clock variation: the four fastest (6, 2, 4, 3 at 13.43–13.66 s) sit at 0.8037–0.8059, and the three slowest (8, 12, 10 at 16.51–16.90 s) sit at 0.7393–0.7843. Attempt 5 is the one outlier upward inside the band (13.74 s, `compute_efficiency` 0.7476, per-step ratio 1.2599, reward 0.8255) — it is faster-scoring than its wall clock alone predicts and is worth re-reading as the best of the mid-band. Per-step cost ratios across this class span 0.9711 to 1.5958 with no visible reward correlation. **This class has stopped improving:** eleven records, ~0.06 of total spread, and repeated `worse_than_an_earlier_attempt` standings.

**Class C — the expensive/heavyweight variant (attempt 13).** Reached the primary target and both perturbations held, but took 37.20 s against a declared ceiling of 31.1 s and ran at 7.1852× the seed anchor's per-step cost against a ceiling of 3.0. `red_line_crossed` 1.0, `validity` 0.0, `task_pass` 0.0, reward 0.0000, `zero_reason_code` 1. Getting to the target is not sufficient; this class bought accuracy with per-step compute and was disqualified for it.

**Class D — the fast conformant run (attempt 14).** The current best at 0.8820. Wall clock 6.6280 s — less than half the mid-band — with per-step ratio 1.8690 (well under the 3.0 ceiling), `compute_efficiency` 0.5031, everything conformant, both perturbations reached, no failed checks. This is the proof that the reward is dominated by qualifying budget and that spending up to ~1.9× per step is affordable if it cuts the number of steps enough.

**Class E — fast but model-fingerprinting (attempt 15).** The fastest qualifying run in the whole set at 4.6808 s, with per-step ratio 1.8731 — almost identical per-step cost to attempt 14, i.e. the same cost regime, applied harder. It reached the primary target and both perturbations held, but it failed `C-NO-SHAPE-FINGERPRINT`, which dropped `rule_conformance` to 0.8571, set `task_pass` to 0.0, and left the reward at 0.7288. The reward was not zeroed, but the conformance penalty cost more than the extra ~1.9 s of speed was worth. This class contains the single most valuable unexploited fact in the whole set: **a 4.68 s qualifying run is achievable.**

## 3. Checks that failed

Named checks, with the verifier's own reasons.

**Primary-run checks:**

- `C-TARGET-REACHED` — "no evaluation row crosses the threshold in the declared direction". Failed once, on attempt 1's primary run, and again on both of attempt 1's perturbation runs. Three failures in total, all inside attempt 1; never seen again.
- `C-BUDGET-RESPECTED` — failed on **two separate primary runs, attempts 1 and 13**, for two different reasons. On attempt 1: "no qualifying row, so no budget position exists" — a downstream consequence of `C-TARGET-REACHED` failing. On attempt 13: "the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1". It also failed on both of attempt 1's perturbation runs, making four appearances overall. Because its two primary failures have distinct reasons and are separated by eleven clean attempts, this is not one persistent defect: it is the generic symptom of either never qualifying or qualifying too late. **The declared wall-clock ceiling is 31.1 s** — that number comes straight from the attempt 13 reason string and is the hard boundary.
- `C-PERTURBATION-REACHED` — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed once, attempt 1.
- `C-PER-STEP-COST-CEILING` — "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0". Failed once, attempt 13. **The per-step cost ceiling is 3.0× the seed anchor.** Every other record sits between 0.9711 and 1.8731, comfortably inside it.
- `C-NO-SHAPE-FINGERPRINT` — "the submission fingerprints the model by shape". Failed once, attempt 15. This is a rule-conformance check, not a budget one: it did not zero the reward, but it pulled `rule_conformance` from 1.0 to 0.8571 and `task_pass` from 1.0 to 0.0, and the record scored 0.7288 rather than the ~0.88+ its 4.68 s wall clock would otherwise have supported. Reading shape to decide behaviour is prohibited; branch on nothing about the model's dimensions.

**Perturbation-run-only checks (attempt 1 alone):**

- `C-LOG-WELL-FORMED` — failed on the `ruleset` perturbation run of attempt 1. Once, never since.
- `C-NO-LATCH-CARRYOVER` — failed on the `ruleset` perturbation run of attempt 1. Once, never since. State must not persist across runs; nothing may be latched from one invocation into the next.

No check failed in more than one attempt with the same reason. The nearest thing to a recurring finding is `C-BUDGET-RESPECTED` at two primary failures, and, as noted, its two reasons are different mechanisms — so nothing that was changed between attempts 1 and 13 is implicated as a common cause. Twelve of the fifteen records had an empty `failed_checks` list entirely.

## 4. Ruled-out directions

**Optimising `compute_efficiency` or per-step cost as the objective.** Ruled out by direct counterexample. Attempt 9 hit `compute_efficiency` 1.0000 and scored 0.7891. Attempt 6 got its per-step ratio down to 0.9710 — cheaper per step than the seed anchor — and scored 0.8059. Attempt 14, the best record at 0.8820, has `compute_efficiency` 0.5031 and a per-step ratio of 1.8690. Cheap steps that take a long wall clock lose to expensive steps that finish early.

**Buying the target with heavy per-step compute (Class C, attempt 13).** Ruled out: it hit both ceilings at once, `C-BUDGET-RESPECTED` at 37.20 s against 31.1 s and `C-PER-STEP-COST-CEILING` at 7.185× against 3.0×, and scored 0.0000 with `red_line_crossed` 1.0 and `validity` 0.0. Reaching the target and holding both perturbations bought nothing. Any per-step ratio approaching 3.0× is not worth exploring; 1.87× has already been shown sufficient.

**Further tuning inside the 13–17 s mid-band (Class B).** Ruled out as a source of gains: eleven records, best 0.8059, and the class has been repeatedly re-entered with `worse_than_an_earlier_attempt` standings (attempts 7, 8, 9, 10, 11, 12 all fell below attempt 6's 0.8059, and all fell below attempt 5's 0.8255). Attempt 14 beat the entire class by 0.0761 by leaving it. Returning to a ~14 s qualifying time caps the reward around 0.80 no matter how clean the run is.

**Shape-based dispatch or any model fingerprinting by shape (Class E).** Ruled out by `C-NO-SHAPE-FINGERPRINT`. It is the only mechanism that has cost a reward without zeroing it, and it cost roughly 0.15. Whatever speed attempt 15 gained, the check took more back.

**Whatever attempt 1 did (Class A).** Ruled out: `zero_reason_code` 4, no qualifying row at all, 89.98 s, and four distinct checks down across the primary and perturbation runs. It has been superseded by eleven conformant classmates and there is no diagnostic value left in it.

## 5. Open leads

**Lead 1 — reconstruct attempt 15's speed without the shape fingerprint.** This is the single highest-value lead. Attempt 15 qualified in 4.6808 s versus attempt 14's 6.6280 s at essentially identical per-step cost (1.8731 vs 1.8690). If the mechanism that produced that ~29% wall-clock reduction can be re-derived without reading model shapes to decide anything, the resulting run should land above 0.8820. The check is specific: do not branch on, hash, key off, or dispatch by tensor or layer dimensions. Derive any schedule from the seed anchor, from step count, or from observed loss/metric trajectory instead — nothing that inspects the model's dimensions.

**Lead 2 — treat qualifying wall clock as the objective directly.** Across all thirteen scoring records, reward is a near-monotone decreasing function of `qualifying_budget`: 4.68 s → (0.7288, penalised) / 6.63 s → 0.8820 / 13.4–13.7 s → 0.8037–0.8255 / 14.1–14.2 s → 0.7891–0.7994 / 16.5–17.0 s → 0.7393–0.7997. Every design decision should be evaluated by whether it reduces the time at which the first qualifying row appears, and by nothing else, subject only to the two hard ceilings.

**Lead 3 — spend the remaining per-step headroom.** The ceiling is 3.0× the seed anchor; the best run used 1.869×. There is roughly 1.6× of unused per-step budget. A more aggressive per-step method — larger effective step, stronger preconditioning, more work per iteration — that cuts total steps enough to land under ~5 s is squarely inside the rules, provided the ratio stays clear of 3.0 and total wall clock stays clear of 31.1 s. Attempt 13 shows what overshooting looks like; stay under about 2.5× to keep margin.

**Lead 4 — re-read attempt 5 as the mid-band anomaly.** At 13.7398 s attempt 5 was slightly *slower* than attempts 2, 3, 4 and 6, yet scored 0.8255 against their 0.8037–0.8059, with `compute_efficiency` 0.7476 and per-step ratio 1.2599. Something in that configuration earned about 0.02 that wall clock alone does not explain. If that mechanism is separable from timing it may compose with the attempt 14 / attempt 15 speed regime.

**Lead 5 — keep the perturbation surface intact.** Both declared perturbation kinds, `ruleset` and `held_out_variant`, have reached their thresholds in every record from attempt 2 onward: 28 of 30 perturbation runs across the set reached, with the only two failures both in attempt 1. By kind: the `ruleset` runs failed once, on `C-LOG-WELL-FORMED`, `C-TARGET-REACHED`, `C-BUDGET-RESPECTED` and `C-NO-LATCH-CARRYOVER`; the `held_out_variant` runs failed once, on `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`. Notably attempts 13 and 15 held both perturbations while failing primary-run checks, so perturbation robustness and primary conformance are independent. Preserve what makes them hold: emit well-formed logs, carry no latched state between runs, and keep the method generic rather than tuned to the primary configuration. Since the runs are unidentified, treat both kinds as equally at risk and do not assume any particular run recurs across attempts.

**Call: exploit.** Attempt 14 (0.8820) is the reference, and attempt 15 already demonstrated a faster qualifying time from the same per-step cost regime. The gain is available by fixing the one named thing that broke attempt 15 — `C-NO-SHAPE-FINGERPRINT` — rather than by a structurally new idea. Concretely: build from the attempt 14 / attempt 15 fast regime, drive qualifying wall clock below 6.63 s toward 4.7 s, keep the per-step ratio in the 1.8–2.5× range, stay far under the 31.1 s wall-clock ceiling and the 3.0× cost ceiling, and introduce nothing that inspects model shape. Do not re-enter the 13–17 s mid-band; eleven records there have exhausted it. Note for the record: the loop has already re-entered that plateau many times over without changing what caps it, which is neither exploiting nor exploring, and should not be repeated.
