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

    All eight attempts since have scored lower than it.
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
  7 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 10 -- reward 0.5983, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.6639, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 12 -- reward 0.4962, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 9.
    C-PERTURBATION-REACHED failed on attempt 12.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Twelve graded records exist. Ten carry a reward; two produced no measurement at all.

Ranked worst to best by reward:

| Rank | Attempt | reward | standing |
|---|---|---|---|
| 1 (worst) | 12 | 0.4962 | worse than an earlier attempt |
| 2 | 9 | 0.5164 | worse than an earlier attempt |
| 3 | 8 | 0.5444 | worse than an earlier attempt |
| 4 | 4 | 0.5792 | worse than an earlier attempt |
| 5 | 10 | 0.5983 | worse than an earlier attempt |
| 6 | 3 | 0.6279 | worse than an earlier attempt |
| 7 | 5 | 0.6587 | worse than an earlier attempt |
| 8 | 11 | 0.6639 | worse than an earlier attempt |
| 9 | 1 | 0.6694 | first measured attempt |
| 10 (best) | 2 | 0.7155 | better than every earlier attempt |

**Attempt 2 holds the highest reward at 0.7155, and it is the one to beat.** Nothing since attempt 2 has matched it: attempts 3, 4, 5, 8, 9, 10, 11 and 12 each came in *lower* than an earlier attempt, and the verifier's own `standing_against_best_so_far` records that regression for every one of them. The trajectory after attempt 2 is downward, not upward, and should not be read as incremental progress.

Attempts 6 and 7 have `measurement_status: harbor_exception`. They produced **no measurement**: no reward, no conformance fraction, no perturbation units, no wall clock. They did not score zero — they were never scored, and no conclusion about their code quality can be drawn from them. Their `failed_checks` list is empty because nothing was checked, not because everything passed.

Supporting terms for the measured runs (these are the only levers the record exposes):

| Attempt | reward | compute_efficiency | per_step_cost_ratio | wall_clock_sec | task_pass | rule_conformance | conformance_fraction |
|---|---|---|---|---|---|---|---|
| 1 | 0.6694 | 0.5488 | 1.5134 | 17.43 | 1.0 | 1.0 | 1.0 |
| 2 | 0.7155 | 0.6205 | 1.5175 | 17.45 | 1.0 | 1.0 | 1.0 |
| 3 | 0.6279 | 0.6033 | 1.5225 | 20.30 | 1.0 | 1.0 | 1.0 |
| 4 | 0.5792 | 0.8832 | 1.1656 | 17.51 | 1.0 | 1.0 | 1.0 |
| 5 | 0.6587 | 0.6098 | 1.6262 | 20.53 | 1.0 | 1.0 | 1.0 |
| 8 | 0.5444 | 0.9679 | 0.9674 | 26.10 | 1.0 | 1.0 | 1.0 |
| 9 | 0.5164 | 0.6647 | 1.4988 | 17.12 | **0.0** | 0.8571 | 1.0 |
| 10 | 0.5983 | 0.5686 | 1.5152 | 20.15 | 1.0 | 1.0 | 1.0 |
| 11 | 0.6639 | 0.8424 | 1.0166 | 20.06 | 1.0 | 1.0 | 1.0 |
| 12 | 0.4962 | 0.6278 | 1.4886 | 16.78 | **0.0** | 1.0 | **0.5** |

`red_line_crossed` is 0.0 and `validity` is 1.0 on every measured attempt; `zero_reason_code` is 0 throughout. No attempt has ever been zeroed. `primary_target_reached` is 1.0 on all ten measured attempts, including attempts 9 and 12 whose `task_pass` was 0 — in both of those the primary run hit its target and the failure came from elsewhere (a conformance check in 9, a held-out run in 12).

The single most important structural fact: **reward is not a monotone function of compute_efficiency or per_step_cost_ratio.** Attempt 8 has the best compute_efficiency seen (0.9679) and the only sub-parity per-step cost ratio (0.9674), and it scored 0.5444 — third from the bottom. Attempt 4 has compute_efficiency 0.8832 and per-step cost 1.1656, both far better than attempt 2's 0.6205 and 1.5175, and it scored 0.5792 against attempt 2's 0.7155. Efficiency was bought and reward was lost. Whatever reward is weighting most heavily, it is a term this record does not name directly — most plausibly the quality of the trained result — and cheapening the per-step cost has consistently damaged it.

The one clean, controlled improvement in the whole record is attempt 1 → attempt 2: wall clock essentially identical (17.43 s vs 17.45 s), per-step cost essentially identical (1.5134 vs 1.5175), compute_efficiency up from 0.5488 to 0.6205, reward up from 0.6694 to 0.7155. Efficiency gained *without* changing the cost profile paid off. Efficiency gained *by* cutting the cost profile (attempts 4, 8, 11) did not.

## 2. Approach classes tried

I have measured terms only, not the source of any attempt, so these classes are grouped by their measured cost signature. Two records with the same signature and the same outcome are one entry.

**Class A — baseline cost profile, short budget (~17.1–17.5 s wall clock, per-step cost ratio ≈1.50–1.52, compute_efficiency 0.55–0.66).** Attempts 1, 2 and 9. This class contains both the first measured result (0.6694) and the best result to date (0.7155). Within the class, raising compute_efficiency from 0.5488 to 0.6205 at constant wall clock and constant per-step cost raised reward by 0.0461. Attempt 9 sits in this class on its cost terms (17.12 s, 1.4988) but was disqualified on a conformance check and scored 0.5164 despite `primary_target_reached` 1.0 and all perturbations held.

**Class B — baseline cost profile, extended budget (~20.1–20.5 s wall clock, per-step cost ratio ≈1.49–1.63).** Attempts 3, 5 and 10, scoring 0.6279, 0.6587 and 0.5983. All three are below attempt 2 and below attempt 1. Spending roughly 2.7–3.1 s more wall clock at an unchanged per-step cost bought nothing: compute_efficiency in this class (0.5686–0.6098) is no better than attempt 2's 0.6205, and reward is uniformly worse.

**Class C — reduced per-step cost at short budget.** Attempt 4 alone: per-step cost ratio driven down to 1.1656 while holding wall clock at 17.51 s, lifting compute_efficiency to 0.8832. Reward fell to 0.5792, a drop of 0.1363 from attempt 2. This is the clearest single demonstration that per-step cost reduction is not the reward's currency.

**Class D — per-step cost at or below parity.** Attempts 8 and 11, with per-step cost ratios 0.9674 and 1.0166 and compute_efficiency 0.9679 and 0.8424. Attempt 11 held wall clock at 20.06 s and scored 0.6639; attempt 8 let wall clock run to 26.10 s, the longest of any attempt, and scored 0.5444, the third worst. Within the class, the cheaper per step it got, the longer it ran and the worse it did. Attempt 11 is the best-performing member of the efficiency-first family at 0.6639, still 0.0516 below attempt 2.

**Class E — compressed budget.** Attempt 12, wall clock 16.78 s, the shortest of any measured attempt, at an otherwise baseline per-step cost of 1.4886. The primary run still reached its target, but one held-out run did not, `conformance_fraction` fell to 0.5, `task_pass` went to 0, and reward was 0.4962 — the worst measured result. Cutting the budget below the ~17.1 s floor that Class A used broke a held-out run.

**Class F — attempts producing no measurement.** Attempts 6 and 7, both `harbor_exception`. Whatever they contained was never graded. They carry no information about the code and must not be treated as failures of any approach.

## 3. Checks that failed

Two named checks have failed, each in exactly one record. Neither is a repeat, so there is no recurring check to attribute to an unchanged root cause — but both are specific and both are fixable.

**C-API-SURFACE**, attempt 9. Verifier's reason, verbatim: *"module-level statements outside imports, constants, and permitted definitions."* This drove `rule_conformance` down to 0.8571 and `task_pass` to 0.0 even though `primary_target_reached` was 1.0, `conformance_fraction` was 1.0, both perturbation runs reached their thresholds cleanly, and `validity` was 1.0. The submission worked and was thrown out on file shape. The remedy is exact: the module must contain nothing at top level except imports, constant assignments and permitted definitions (functions/classes). No top-level calls, no top-level prints, no `if __name__ == "__main__"` execution body, no configuration built by running code at import time, no side-effecting expressions at module scope. Everything executable belongs inside the permitted definitions.

**C-PERTURBATION-REACHED**, attempt 12. Verifier's reason, verbatim: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* This is the aggregate check; underneath it, the unit that failed was of kind **held_out_variant**, and it failed two unit-level checks: **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**. That run neither hit its target nor stayed inside its budget. `conformance_fraction` fell to 0.5 and `task_pass` to 0.0. The primary run was unaffected — `primary_target_reached` remained 1.0 — so this is a margin failure on a held-out run, not a broken algorithm.

All other eight measured attempts have empty `failed_checks`, `conformance_fraction` 1.0, `rule_conformance` 1.0 and `task_pass` 1.0.

## 4. Ruled-out directions

**Lowering per_step_cost_ratio as the route to reward — ruled out.** Attempt 4 cut it to 1.1656 (reward 0.5792) and attempt 8 cut it to 0.9674 (reward 0.5444), against attempt 2's 1.5175 at reward 0.7155. Three separate cost levels, and reward moves opposite to cost reduction across all of them. Cheapening the step is buying efficiency the reward does not pay for and losing something it does.

**Maximising compute_efficiency in isolation — ruled out.** Attempt 8 posted the highest compute_efficiency in the record, 0.9679, and landed third from the bottom at 0.5444. Attempt 4's 0.8832 landed at 0.5792. Attempt 2's winning 0.7155 came with a middling 0.6205. Compute_efficiency is worth raising only when the cost profile and wall clock are held fixed, as in the attempt 1 → 2 step.

**Extending wall clock into the 20 s band at baseline cost — ruled out.** Attempts 3, 5 and 10 all ran 20.15–20.53 s at per-step cost 1.49–1.63 and scored 0.6279, 0.6587 and 0.5983, every one of them below both attempt 1 (0.6694) and attempt 2 (0.7155). The extra ~3 s of budget produced no reward and no compute_efficiency gain.

**Running long, 26 s wall clock — ruled out.** Attempt 8 is the longest run measured and scored 0.5444. Length by itself is penalised even when every conformance check passes and every perturbation holds.

**Compressing wall clock below ~17.1 s — ruled out.** Attempt 12 at 16.78 s is the only attempt whose held-out variant missed both C-TARGET-REACHED and C-BUDGET-RESPECTED, and it produced the worst reward in the record, 0.4962. Attempt 9 at 17.12 s is the shortest run that still held every perturbation. Treat ~17.1 s as a floor with no margin below it.

**Any module-level executable code — ruled out.** C-API-SURFACE zeroed attempt 9's `task_pass` on a submission whose primary target and both perturbation runs were fine. There is no upside to top-level statements and the downside is total.

## 5. Open leads

**Rebuild attempt 2's operating point exactly, then improve inside it.** The target profile is wall clock ≈17.45 s, per_step_cost_ratio ≈1.52, compute_efficiency ≈0.62, `task_pass` 1.0, both perturbations held. The next attempt starts from a pristine stub and cannot see attempt 2's code, so re-establishing this profile is the first job; treat any run that lands materially outside it as off-course.

**Repeat the attempt 1 → attempt 2 move: raise compute_efficiency while holding wall clock and per-step cost constant.** That is the only change in the entire record that raised reward (+0.0461). Attempt 2 sits at 0.6205 and attempts 4, 8 and 11 prove that 0.84–0.97 is reachable — but they reached it by cutting per-step cost, which cost reward. The open question is whether compute_efficiency can be pushed toward 0.70–0.75 with per_step_cost_ratio pinned near 1.52 and wall clock pinned near 17.45 s. That combination has never been measured.

**Treat solution quality, not cost, as the dominant reward term.** With compute_efficiency, per_step_cost_ratio and wall clock all failing to predict the ranking, the residual is almost certainly how good the trained result is. Effort is better spent on what the algorithm learns per step than on making steps cheaper. Attempt 2's relatively expensive step (1.5175) with a good outcome beat attempt 8's parity step (0.9674) by 0.1711.

**Keep an explicit safety margin for the held_out_variant runs.** Across ten measured attempts there were twenty perturbation units, two per attempt. All ten **ruleset**-kind units reached their thresholds with no failed checks — that kind has never failed. Of the ten **held_out_variant**-kind units, nine reached and one did not, failing C-TARGET-REACHED and C-BUDGET-RESPECTED together, in the attempt with the shortest wall clock. Aggregate: 19 of 20 units reached; the sole failure was of the held_out_variant kind. These runs are not identified or ordered in the record and cannot be matched across attempts, so the actionable form of this is: whatever budget the primary run needs, the held-out variant needs comparable headroom, and shaving the budget takes it from the held-out variant first. Do not tune wall clock down to the primary run's minimum.

**Audit the module surface before submitting.** Concretely, scan the final file: top level must hold imports, constant assignments, and function/class definitions only. This is a one-time mechanical check that reclaims the ~0.15 of reward attempt 9 lost on an otherwise sound run.

**Ignore the harbor_exception records as evidence.** Attempts 6 and 7 tell us nothing about any approach. Do not avoid a direction because it coincided with them, and do not count them against any hypothesis.

**Call: exploit.** Class A at attempt 2's operating point is the only approach that has ever set a best score, and its improvement path — compute_efficiency up at fixed cost profile — was demonstrated once and then abandoned in favour of cost-cutting variants that all scored lower. The efficiency-first family (Classes C and D) has been sampled at three distinct cost levels and produced 0.5444, 0.5792 and 0.6639, none of them competitive; the extended-budget family (Class B) has been sampled three times and produced 0.5983, 0.6279 and 0.6587, none of them competitive. Those are exhausted, not under-explored. Earlier work did repeatedly re-enter the same cost-cutting and budget-stretching classes without changing the thing that made them lose — the sacrifice of result quality for step cost — and that pattern should stop. Reconstruct attempt 2's profile, verify the module surface, keep the held-out margin, and push compute_efficiency only at fixed wall clock and fixed per-step cost.
