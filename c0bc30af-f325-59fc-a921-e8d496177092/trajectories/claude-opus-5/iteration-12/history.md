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

    All seven attempts since have scored lower than it.
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

    attempt 4 -- reward 0.8719, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 10 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 3 of your last 4 attempts
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same seed run has now failed on 3 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 11 -- reward 0.8980, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 25
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 12 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same held_out_variant run has now failed on 3 of your last 4 attempts
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        the same seed run has now failed on 3 of your last 4 attempts
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 5 attempts (3, 7, 9, 10, 12). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 5 attempts (3, 7, 9, 10, 12). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 5 attempts (3, 7, 9, 10, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# Between-attempt summary

*(Note: the prompt in the transcript asked for "four sections"; the governing spec requires five, so five are given, with the headings verbatim.)*

---

## 1. Results so far

Twelve graded submissions, all with `measurement_status: measured`, so every one carries a reward. Listed worst to best:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| = last | 3 | 0.0000 | zero_reason_code 4; target never crossed; wall_clock 1692.52 s |
| = last | 7 | 0.0000 | zero_reason_code 4; wall_clock 1692.21 s |
| = last | 9 | 0.0000 | zero_reason_code 4; wall_clock 1692.97 s |
| = last | 10 | 0.0000 | zero_reason_code 4; wall_clock 1690.96 s |
| = last | 12 | 0.0000 | zero_reason_code 4; wall_clock 1690.45 s |
| 7 | 6 | 0.5615 | target reached, but C-API-SURFACE failed; qualifying_budget 204.09 s |
| 6 | 8 | 0.7551 | clean checks; qualifying_budget 78.14 s, wall_clock 151.50 s |
| 5 | 1 | 0.7684 | target reached, C-API-SURFACE failed; qualifying_budget 25.46 s |
| 4 | 2 | 0.8385 | clean checks; qualifying_budget 73.62 s |
| 3 | 4 | 0.8719 | clean checks; qualifying_budget 50.03 s; compute_efficiency 1.0 |
| 2 | 11 | 0.8980 | clean checks; qualifying_budget 25.35 s |
| 1 | **5** | **0.9128** | clean checks; qualifying_budget 25.34 s; per_step_cost_ratio 0.9887 |

**Attempt 5, reward 0.9128, is the highest and is the one to beat.**

Direction of travel, stated plainly: after attempt 5 set the high mark, attempt 6 (0.5615), attempt 8 (0.7551) and attempt 11 (0.8980) were each *lower* than the best, and attempts 7, 9, 10 and 12 scored 0.0000. `standing_against_best_so_far` reads `worse_than_an_earlier_attempt` for attempts 3, 6, 7, 8, 9, 10, 11 and 12. Only attempts 2, 4 and 5 ever read `better_than_every_earlier_attempt`. Nothing has improved on attempt 5 since it was measured; the loop has spent seven subsequent submissions without beating it.

No record has `red_line_crossed` set (all 0.0), and `validity` is 1.0 in every record. Every failure so far is a threshold/budget or API-surface failure, not an invalidation.

## 2. Approach classes tried

The measured terms do not carry source code, so these classes are defined by their measurement signatures, which are sharply distinct.

**Class A — fast-converging, fully conformant runs (attempts 2, 4, 5, 8, 11).** `primary_target_reached` 1.0, `task_pass` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `failed_checks` empty, both perturbation units reached. These are the only submissions that ever scored above 0.84. Within this class reward is a steeply decreasing function of how much budget was consumed to reach the qualifying row:

- 25.34 s → 0.9128 (attempt 5)
- 25.35 s → 0.8980 (attempt 11)
- 50.03 s → 0.8719 (attempt 4)
- 73.62 s → 0.8385 (attempt 2)
- 78.14 s → 0.7551 (attempt 8)

The two ~25 s runs differ by 0.0148 in reward at essentially identical qualifying budget; the terms that separate them are `per_step_cost_ratio` (0.9887 for attempt 5 vs 1.0502 for attempt 11) and `compute_efficiency` (0.7728 vs 0.7043). That is the only evidence in hand about what moves reward once the budget is already at the ~25 s floor: at equal budget, the lower per-step cost ratio scored higher.

Attempt 8 is the one anomaly inside Class A: its `qualifying_budget` was 78.14 s but its `wall_clock_sec` was 151.50 s — the only record where the two diverge. It scored 0.7551, below attempt 2 which had a *similar* qualifying budget of 73.62 s and scored 0.8385. Two readings are consistent with the data and neither is settled: either total wall clock beyond the qualifying row is itself charged, or the gap is explained by `per_step_cost_ratio` (1.0291 for attempt 8 vs 0.9162 for attempt 2). Either way, running on past the qualifying row cost reward.

**Class B — reaches the target but leaves disallowed module-level code (attempts 1, 6).** `primary_target_reached` 1.0 and both perturbation units reached, but `rule_conformance` 0.8571 (6 of 7) and `task_pass` 0.0, driven entirely by C-API-SURFACE. Attempt 1 reached the qualifying row in 25.46 s — as fast as the best Class A runs — and still only scored 0.7684. Attempt 6 combined the same violation with a bloated 204.09 s budget and `per_step_cost_ratio` 1.3778, scoring 0.5615, the worst non-zero result on record.

**Class C — long-running runs that never cross the threshold (attempts 3, 7, 9, 10, 12).** Five submissions, all `reward` 0.0000, all `zero_reason_code` 4, all `conformance_fraction` 0.0, all `primary_target_reached` 0.0, all with `qualifying_budget` reported as `not-measured`. Their wall clocks are 1690.45, 1690.96, 1692.21, 1692.51 and 1692.97 s — a band under three seconds wide across five independent submissions, which is the signature of an externally imposed run ceiling rather than of five coincidentally similar training curves. Note their `compute_efficiency` values are high (1.0, 1.0, 0.9833, 0.9762, 0.9672) — that term is meaningless when nothing qualified and must not be read as a partial success.

## 3. Checks that failed

**C-API-SURFACE** — "module-level statements outside imports, constants, and permitted definitions." Failed **twice**, in attempts 1 and 6. These two attempts differ enormously in every other respect (25.46 s vs 204.09 s qualifying budget; per_step_cost_ratio 1.0639 vs 1.3778; reward 0.7684 vs 0.5615), yet both tripped the identical check with the identical reason. Whatever was changed between attempt 1 and attempt 6 is **not** what causes C-API-SURFACE. The cause is executable code sitting at module scope; the fix is to move every module-level statement that is not an import, a constant assignment, or a permitted definition inside a function or a `__main__` guard, and to leave nothing at import time that runs. Neither failure blocked the target — both attempts had `primary_target_reached` 1.0 — but both had `task_pass` forced to 0.0 and `rule_conformance` capped at 0.8571.

**C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction." Failed **five times**, in attempts 3, 7, 9, 10 and 12. This is the single most repeated finding in the record. Across those five attempts the loop varied something (per_step_cost_ratio spans 0.7758 to 0.8901), and the check failed identically every time: whatever was changed between them is not what is causing it. The invariant across all five is a wall clock pinned at ~1690–1693 s, i.e. these runs consumed the full available time without ever producing a qualifying evaluation row.

**C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists." Failed **five times**, in the same attempts 3, 7, 9, 10 and 12. Its reason text makes clear it is a *consequence* of C-TARGET-REACHED, not an independent budget overrun. Fixing target-crossing removes this check as well; there is no separate budget bug to hunt.

**C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget." Failed **five times**, in attempts 3, 7, 9, 10 and 12, always with the same "0 of 2" wording. Also a consequence of the same non-convergence.

## 4. Ruled-out directions

**Whatever produced the ~1690 s non-converging runs (Class C).** Five separate submissions, five rewards of 0.0000, five identical triples of failed checks, five wall clocks inside a 2.5 s band. This has been re-attempted four times after its first zero without changing what made it score zero, and it has never once produced a qualifying row. Do not submit anything whose expected time to first threshold crossing is anywhere near the full run ceiling. Note explicitly that these five records produced measurements — they are genuine measured zeros, not missing data — and equally that their high `compute_efficiency` figures are artefacts of `qualifying_budget` being `not-measured`.

**Leaving executable statements at module scope.** Two independent submissions were penalised for it, costing `task_pass` outright each time. Attempt 1 shows the cost is not recoverable by speed: it matched the best runs' ~25 s budget and still landed 0.7684, roughly 0.13 below the conformant attempt 11 at the same budget. There is no configuration in which this is worth keeping.

**Spending more budget to reach the target.** Within the conformant Class A the ordering is monotone against qualifying budget: 25 s outscores 50 s outscores 74 s outscores 78 s. Attempt 6 at 204.09 s and attempt 8 at 151.50 s wall clock are the two most expensive scoring runs and sit 6th and 7th of the eight non-zero results. Longer training is not buying reward.

**Continuing to run after the qualifying row.** Attempt 8 is the only record where `wall_clock_sec` (151.50) exceeds `qualifying_budget` (78.14), and it underperformed attempt 2 at a comparable qualifying budget by 0.0834. Stop as soon as the threshold is crossed in the declared direction.

## 5. Open leads

**Reproduce attempt 5's configuration exactly and treat 0.9128 as the floor.** Its profile is the target to rebuild: qualifying_budget 25.34 s, per_step_cost_ratio 0.9887, compute_efficiency 0.7728, rule_conformance 1.0, both perturbation units reached, no failed checks. Attempt 11 shows the ~25 s regime is reachable repeatedly (25.35 s), so this is not a lucky one-off.

**Drive `per_step_cost_ratio` below 1.0 while holding the ~25 s qualifying budget.** This is the only lever the data isolates at fixed budget. Attempt 5 (0.9887) beat attempt 11 (1.0502) by 0.0148 at the same budget. Attempt 4 achieved 0.7115 — the lowest ratio among all scoring runs — and `compute_efficiency` 1.0, but paid 50.03 s for it and landed at 0.8719. The untested combination is attempt 4's cheap per-step work at attempt 5's early stopping point; if both terms can be held simultaneously, it should clear 0.9128.

**Cut the qualifying budget below 25.3 s.** Three separate runs cluster at 25.34–25.46 s, which may be a natural convergence floor for this class or may simply be where the loop has stopped looking. Reaching the threshold sooner — a faster-converging schedule, a cheaper warm-up, earlier evaluation cadence so the crossing row is *detected* sooner — is the highest-value untested axis, given how steeply reward falls with budget across 25/50/74/78 s.

**Evaluate more frequently near the start.** C-TARGET-REACHED depends on an evaluation *row* crossing the threshold, not on the model state per se. Cheap, early, frequent evaluation both lowers the recorded qualifying budget for runs that would converge anyway and reduces the risk of a Class C-style run where the threshold is never recorded as crossed.

**Verify the module-level surface before submitting.** A mechanical pre-submission pass — every top-level node must be an import, a constant assignment, or a permitted definition — removes the only check that has ever cost a run its `task_pass` while the target was actually reached.

**On the perturbation runs.** Each record declares 2 perturbation units, of kinds `held_out_variant` and `seed`. In aggregate across the twelve records, 24 perturbation runs were exercised: 14 reached their threshold and 10 did not. By kind, the split is identical — of the 12 `held_out_variant` runs, 7 reached and 5 did not; of the 12 `seed` runs, 7 reached and 5 did not. Every one of the 10 failures occurred inside attempts 3, 7, 9, 10 and 12, and every failure names the same pair, C-TARGET-REACHED and C-BUDGET-RESPECTED. Neither kind is selectively fragile: no perturbation run has ever failed while its primary run succeeded, and `all_perturbations_held` is true in exactly the seven attempts whose primary target was reached. The perturbations are therefore not currently an independent risk — they fail if and only if the primary approach fails to converge — and no separate robustness work is indicated ahead of restoring the ~25 s converging configuration.

---

**Call: exploit.** The scoring family (Class A) has not stopped improving — 0.8385 → 0.8719 → 0.9128 came from tightening budget and per-step cost within it, and the attempt-4 vs attempt-5 comparison points at an untested combination that should go higher. The correct move is to rebuild the attempt-5 configuration, keep the qualifying budget at or below ~25 s, stop immediately on the first threshold crossing, push `per_step_cost_ratio` toward attempt 4's 0.71, and keep the module scope clean. Explicitly do not re-run anything resembling the ~1690 s non-converging class: that has been submitted five times without changing what made it score zero, and repeating it is neither exploring nor exploiting.
