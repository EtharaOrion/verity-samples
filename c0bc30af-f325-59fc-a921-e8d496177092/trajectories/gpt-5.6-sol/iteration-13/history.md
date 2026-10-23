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

    All eight attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3        0.8657   1.000             2 of 2         yes             74                
  4        0.7740   1.000             2 of 2         yes             74                
  5 *      0.8658   1.000             2 of 2         yes             74                
  6        0.7580   0.857             2 of 2         yes             46                
  7        0.4911   1.000             1 of 2         yes             50                
  8        0.7805   1.000             2 of 2         yes             99                
  9        0.8332   1.000             2 of 2         yes             50                
  10       0.8503   1.000             2 of 2         yes             75                
  11       0.8067   1.000             2 of 2         yes             74                
  12       0.4275   1.000             1 of 2         yes             74                
  13       0.8657   1.000             2 of 2         yes             74                

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
  8 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 3 -- reward 0.8657, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 11 -- reward 0.8067, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 12 -- reward 0.4275, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 1 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-PERTURBATION-REACHED -- 1 of 2 declared perturbations reached their own threshold inside their own budget

    attempt 13 -- reward 0.8657, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 6.
    C-PERTURBATION-REACHED has failed on 2 attempts (7, 12). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

All thirteen graded attempts carry `measurement_status: "measured"`, so every one has a reward; none produced an absent measurement, and none scored zero (`zero_reason_code` is 0 and `red_line_crossed` is 0.0 throughout, `validity` is 1.0 throughout).

Worst to best by reward:

| Rank | Attempt | Reward | Notes from its own terms |
|---|---|---|---|
| 1 (worst) | 12 | 0.4275 | `all_perturbations_held: false`; `conformance_fraction` 0.5; `task_pass` 0.0; failed C-PERTURBATION-REACHED |
| 2 | 7 | 0.4911 | `all_perturbations_held: false`; `conformance_fraction` 0.5; `task_pass` 0.0; failed C-PERTURBATION-REACHED |
| 3 | 6 | 0.7580 | `rule_conformance` 0.8571; `task_pass` 0.0; failed C-API-SURFACE; `per_step_cost_ratio` 1.4094, `compute_efficiency` 0.4942 |
| 4 | 4 | 0.7740 | clean; `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934 |
| 5 | 8 | 0.7805 | clean; `wall_clock_sec` 98.60, `per_step_cost_ratio` 1.0848, `compute_efficiency` 0.6575 |
| 6 | 11 | 0.8067 | clean; `compute_efficiency` 1.0000 (the maximum observed), `per_step_cost_ratio` 0.6947 |
| 7 | 2 | 0.8079 | clean; `compute_efficiency` 0.7226, `per_step_cost_ratio` 0.9441 |
| 8 | 9 | 0.8332 | clean; `qualifying_budget` 49.89 against `wall_clock_sec` 74.39; `per_step_cost_ratio` 0.9516 |
| 9 | 10 | 0.8503 | clean; `compute_efficiency` 0.7433, `per_step_cost_ratio` 0.9615 |
| 10 | 1 | 0.8630 | clean; `per_step_cost_ratio` 1.0723, `wall_clock_sec` 76.34 |
| 11 | 13 | 0.8657 | clean; `compute_efficiency` 0.6829, `per_step_cost_ratio` 0.9710 |
| 12 | 3 | 0.8657 | clean; `compute_efficiency` 0.6922, `per_step_cost_ratio` 0.9835 |
| 13 (best) | 5 | 0.8658 | clean; `compute_efficiency` 0.6926, `per_step_cost_ratio` 0.9581 |

**Attempt 5, reward 0.8658, holds the highest reward. That is the score to beat.** Attempt 3 (0.8657110) and attempt 13 (0.8656561) sit within a thousandth of it; the three are effectively a plateau, and attempt 13 came after attempt 5 and is marked `worse_than_an_earlier_attempt` — it did not improve on the plateau, it re-landed on it slightly below.

Direction of travel, stated plainly: only attempts 1, 3 and 5 ever carried `better_than_every_earlier_attempt` (attempt 1 as `first_measured_attempt`). Every attempt from 6 onward — 6, 7, 8, 9, 10, 11, 12 and 13 — is marked `worse_than_an_earlier_attempt`. That is eight consecutive attempts that did not beat attempt 5. Attempt 2 was worse than attempt 1; attempt 4 was worse than attempt 3; attempts 7 and 12 were the two worst results recorded, each roughly 0.37–0.44 below the best. There has been no progress past 0.8658.

## 2. Approach classes tried

The measured terms expose each submission only through its cost and conformance fingerprint, so the classes below are grouped by that fingerprint. Do not read more mechanism into them than the numbers support.

**Class A — the plateau configuration: near-parity per-step cost, ~74 s wall clock.** Attempts 3 (0.8657), 5 (0.8658), 13 (0.8657), and closely related 10 (0.8503) and 2 (0.8079). Signature: `per_step_cost_ratio` between 0.944 and 0.984, `compute_efficiency` 0.69–0.74, `wall_clock_sec` 74.26–74.54, `qualifying_budget` equal to wall clock at ~74.3–74.5, all checks held, `task_pass` 1.0, both perturbations reached. This class produced every one of the top three rewards. Within the class, the three highest scores all sit at `compute_efficiency` 0.6829–0.6926 and `per_step_cost_ratio` 0.958–0.984; the two lower members (10 at 0.7433/0.9615, 2 at 0.7226/0.9441) are slightly cheaper per step and score 0.0155 and 0.0579 lower respectively. So inside this class, spending slightly *more* per step correlates with the better reward, up to a limit.

**Class B — aggressive cost reduction, per-step ratio pushed to ~0.69.** Attempts 4 (0.7740, `compute_efficiency` 0.9681, `per_step_cost_ratio` 0.6934) and 11 (0.8067, `compute_efficiency` 1.0000, `per_step_cost_ratio` 0.6947). Both are fully clean: all checks held, `task_pass` 1.0, both perturbations reached, wall clock 73.74 and 73.93 s — the fastest clean runs recorded. Attempt 11 achieved the maximum possible `compute_efficiency` of 1.0 and still scored 0.0591 *below* attempt 5. This is the single most informative negative result in the set: maximising compute efficiency does not maximise reward, and the efficiency term is not the binding constraint on the score.

**Class C — over-budget / slow, per-step ratio above 1.0.** Attempts 1 (0.8630, ratio 1.0723, 76.34 s) and 8 (0.7805, ratio 1.0848, 98.60 s). Attempt 1 was only mildly above parity and scored near the plateau; attempt 8 pushed wall clock to 98.60 s — by far the longest run — and lost 0.0853 against the best while remaining fully clean. Cost overruns past roughly 76 s are penalised heavily even when nothing fails.

**Class D — reduced qualifying budget.** Attempt 9 (0.8332) is the only clean run whose `qualifying_budget` (49.89) is well below its `wall_clock_sec` (74.39). Its per-step ratio (0.9516) and efficiency (0.7505) are otherwise Class-A-like, and it scored 0.0326 below attempt 5. Attempt 7 shares the low qualifying budget (50.05, equal to its wall clock) but failed conformance.

**Class E — module-level structure change that broke the API surface.** Attempt 6 alone (0.7580). It failed C-API-SURFACE, dropping `rule_conformance` to 0.8571 and `task_pass` to 0.0, while simultaneously being the most expensive per step of any run (`per_step_cost_ratio` 1.4094, `compute_efficiency` 0.4942) and the only clean-wall-clock/short-budget mismatch of its kind (`wall_clock_sec` 70.37 against `qualifying_budget` 45.82). Both perturbation runs still reached their thresholds.

**Class F — configurations that starve the held-out variant run.** Attempts 7 (0.4911) and 12 (0.4275). Both failed C-PERTURBATION-REACHED with `conformance_fraction` 0.5, `all_perturbations_held: false`, `task_pass` 0.0. In both, the primary run itself was fine (`primary_target_reached` 1.0) and the seed run reached; only the held-out variant run failed. These are the two worst rewards on record and they are worse by a wide margin — roughly half the plateau score.

## 3. Checks that failed

Ten of the thirteen attempts had an empty `failed_checks`. Three did not.

- **C-API-SURFACE** — reason given by the verifier: *"module-level statements outside imports, constants, and permitted definitions."* Failed once, at attempt 6. It drove `rule_conformance` to 0.8571 and `task_pass` to 0.0.
- **C-PERTURBATION-REACHED** — reason given: *"1 of 2 declared perturbations reached their own threshold inside their own budget."* **Failed twice, at attempt 7 and at attempt 12.** This is the repeat finding and the one that matters most. Whatever was changed between attempt 7 and attempt 12 is not what causes this failure: the failure survived that change intact, with the same identifier and the same verifier reason, and the two attempts differ markedly in their other terms (attempt 7: `compute_efficiency` 0.6954, `per_step_cost_ratio` 0.9657, `qualifying_budget` 50.05; attempt 12: `compute_efficiency` 0.8464, `per_step_cost_ratio` 0.8114, `qualifying_budget` 74.11). Cost profile and budget were both altered between them and the check failed both times. The cause lies elsewhere.
- **C-BUDGET-RESPECTED** — recorded inside `perturbation_units`, not at top level. Failed twice: once in attempt 7 and once in attempt 12, in both cases on the held-out-variant run. This is the check that actually stopped those runs and is the mechanism behind both C-PERTURBATION-REACHED failures.
- **C-TARGET-REACHED** — recorded inside `perturbation_units`. Failed once, in attempt 12, on the held-out-variant run, alongside C-BUDGET-RESPECTED there.

Note that a failed check does not zero the reward here: attempt 6 still scored 0.7580 and attempts 7 and 12 scored 0.4911 and 0.4275. But a C-PERTURBATION-REACHED failure costs roughly 0.37–0.44 of reward against the plateau, and a C-API-SURFACE failure roughly 0.11.

## 4. Ruled-out directions

- **Maximising `compute_efficiency` / driving `per_step_cost_ratio` down toward 0.69.** Ruled out. Attempt 11 reached `compute_efficiency` 1.0000 — the ceiling — with `per_step_cost_ratio` 0.6947, held every check, passed the task and both perturbations, and still scored 0.8067, which is 0.0591 below attempt 5. Attempt 4 did the same thing (0.9681 / 0.6934) and scored 0.7740, worse still. Two independent runs of this class confirm that cheapening the per-step cost to that level costs more reward than the efficiency term returns.
- **Long wall-clock runs above ~76 s.** Ruled out. Attempt 8 ran 98.60 s with `per_step_cost_ratio` 1.0848, held every check, and scored 0.7805 — 0.0853 below the best. Attempt 1 at 76.34 s and ratio 1.0723 scored 0.8630, near-plateau, so the penalty sets in somewhere above that; 98 s is clearly past it.
- **The module-level structural change made in attempt 6.** Ruled out as written. It is the only attempt to trip C-API-SURFACE, with the explicit reason "module-level statements outside imports, constants, and permitted definitions." The submission must confine module scope to imports, constants and permitted definitions; anything executable at module level must move inside a permitted definition. The same attempt also had the worst per-step cost ratio recorded (1.4094), so nothing about it is worth salvaging as-is.
- **Reducing the qualifying budget to ~50 s while leaving wall clock at ~74 s.** Ruled out on the evidence available. Attempt 9 did this cleanly and scored 0.8332, 0.0326 below the best; attempt 7, the other low-qualifying-budget run, failed C-PERTURBATION-REACHED outright at 0.4911. No run with a ~50 s qualifying budget has ever matched the plateau.
- **Re-landing on the Class A plateau unchanged.** Attempt 13 reproduced the Class A fingerprint (0.6829 / 0.9710 / 74.26 s, all checks held) and scored 0.8656561 — marginally below attempt 5's 0.8658084. Simply re-running the plateau configuration does not beat it; the differences among attempts 3, 5 and 13 are within noise at the fourth decimal.

## 5. Open leads

- **Fix the held-out-variant budget failure without disturbing the Class A cost profile.** Across all thirteen records, the `seed` perturbation run reached its threshold every single time — 13 of 13, with no failed checks ever recorded on a run of that kind. The `held_out_variant` kind reached 11 of 13 times and is the *only* kind that has ever failed, failing in attempts 7 and 12. In aggregate that is 24 of 26 perturbation runs reaching threshold, with both failures concentrated in one kind. In both failures the stopping check was C-BUDGET-RESPECTED (and in one of them C-TARGET-REACHED as well). The held-out-variant run therefore needs headroom within its *own* budget that the seed run does not: whatever adaptive or data-dependent behaviour makes the algorithm run long, it runs long only on the variant. Concretely, cap the work the algorithm will do as a function of its own elapsed budget rather than as a fixed step count, so that the variant run terminates inside its allowance even when it converges more slowly. Note that the two failures bracket very different cost settings (per-step ratio 0.9657 and 0.8114), so a global cost knob is not the fix — the guard must be internal to the run.
- **Explore the narrow band just above the plateau's per-step cost.** Within Class A, reward rises with per-step ratio across 0.944 → 0.958 → 0.971 → 0.984 (0.8079, 0.8658, 0.8657, 0.8657) and is still high at 1.0723 (attempt 1, 0.8630) before collapsing at 1.0848 with a 98.6 s wall clock (attempt 8, 0.7805). The unexplored region is per-step ratio roughly 0.99–1.06 held at a ~74 s wall clock — attempt 1 mixed a high ratio with a longer run, so the two effects were never separated. Try parity-ish cost with the wall clock kept at ~74 s.
- **Improve the quantity the reward is actually tracking, holding cost fixed.** The plateau at 0.8658 is reached with `task_pass` 1.0, `rule_conformance` 1.0, `validity` 1.0 and both perturbations held — every conformance term is already saturated. The remaining ~0.13 of headroom cannot come from conformance and demonstrably does not come from efficiency (attempt 11 proved that). It must come from the underlying training quality at fixed budget. Lock the Class A cost fingerprint exactly (`per_step_cost_ratio` ≈ 0.96, wall clock ≈ 74.4 s, `qualifying_budget` ≈ 74.4) and change only the learning behaviour — schedule, initialisation, optimiser parameters, regularisation — so that any reward movement is attributable to quality rather than cost.
- **Confirm the module-scope constraint proactively.** Since C-API-SURFACE has fired once with a precise reason, any new submission should be inspected before scoring for executable statements at module level; only imports, constants and permitted definitions belong there. This is cheap insurance worth 0.11 of reward.

**Call: exploit.** The Class A configuration has already produced the three best rewards and the top score of 0.8658 (attempt 5). The path forward is to reproduce that exact cost fingerprint and change one thing at a time — first ensuring the held-out-variant run cannot overrun its own budget, then probing the 0.99–1.06 per-step-cost band and the training-quality knobs at fixed cost. Two things earlier work kept doing that must not be repeated: re-running the plateau unchanged (attempt 13, which merely re-landed 0.0002 below the best), and re-testing the maximum-efficiency direction, which has now been measured twice (attempts 4 and 11) and lost both times.
