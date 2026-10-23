# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 16 -- reward 0.8841, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 3
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
  14       0.8820   1.000             2 of 2         yes             7                 
  15       0.7288   0.857             2 of 2         yes             5                 
  16 *     0.8841   1.000             2 of 2         yes             3                 
  17       0.7716   1.000             2 of 2         yes             15                

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
  12 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 5 -- reward 0.8255, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 14 -- reward 0.8820, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 7
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 15 -- reward 0.7288, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 5
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-NO-SHAPE-FINGERPRINT -- the submission fingerprints the model by shape

    attempt 17 -- reward 0.7716, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 15
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED has failed on 2 attempts (1, 13). Whatever has been
      changing between them is not what is causing it.
    C-NO-SHAPE-FINGERPRINT failed on attempt 15.
    C-PER-STEP-COST-CEILING failed on attempt 13.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Seventeen graded records, all of which carry a `reward` value. Two of them (attempts 1 and 2) have `measurement_status` of `measured_phase_cut` rather than plain `measured`; the remaining fifteen are `measured`. I report the numbers each record carries and flag the phase-cut status where it applies, rather than treating the phase cut as an absent measurement, because those two records do carry reward values.

Worst to best by reward:

| Rank | Attempt | reward | Note |
|---|---|---|---|
| 1 | 1 | 0.0000 | phase-cut measurement; `zero_reason_code` 4; nothing reached the threshold; `task_pass` 0, `conformance_fraction` 0.0 |
| 2 | 13 | 0.0000 | `zero_reason_code` 1; `red_line_crossed` 1.0, `validity` 0.0, `task_pass` 0 |
| 3 | 15 | 0.7288 | conformant perturbations but `task_pass` 0, `rule_conformance` 0.8571 |
| 4 | 10 | 0.7393 | wall clock 16.899 s |
| 5 | 12 | 0.7443 | wall clock 16.943 s |
| 6 | 17 | 0.7716 | wall clock 14.844 s |
| 7 | 8 | 0.7843 | wall clock 16.507 s |
| 8 | 9 | 0.7891 | `compute_efficiency` 1.0, wall clock 14.160 s |
| 9 | 7 | 0.7994 | wall clock 14.103 s |
| 10 | 11 | 0.7997 | wall clock 17.003 s |
| 11 | 2 | 0.8037 | phase-cut measurement; wall clock 13.488 s |
| 12 | 4 | 0.8042 | 0.8041887 exactly; wall clock 13.658 s |
| 13 | 3 | 0.8042 | 0.8042363 exactly, marginally above attempt 4; wall clock 13.662 s |
| 14 | 6 | 0.8059 | `compute_efficiency` 0.9465, `per_step_cost_ratio` 0.9711 |
| 15 | 5 | 0.8255 | wall clock 13.740 s |
| 16 | 14 | 0.8820 | wall clock 6.628 s |
| 17 | 16 | **0.8841** | wall clock 3.337 s — **highest reward; this is the one to beat** |

Attempt 16 holds the highest reward at 0.8841 and is the attempt to beat. Attempt 14 at 0.8820 is second and is the same family of result.

Several attempts scored below an earlier best and must be read as regressions, not progress; `standing_against_best_so_far` says so directly for each of them. Attempt 4 (0.8042) was worse than attempt 3. Attempts 6 (0.8059), 7 (0.7994), 8 (0.7843), 9 (0.7891), 10 (0.7393), 11 (0.7997) and 12 (0.7443) were each worse than an earlier attempt, i.e. all of them fell back from attempt 5's 0.8255. Attempt 13 (0.0000) was worse than an earlier attempt and is one of the two zero-scoring records. Attempt 15 (0.7288) was worse than an earlier attempt and is the lowest non-zero result of the whole series. Attempt 17 (0.7716) was worse than an earlier attempt, falling well back from attempt 16's 0.8841 immediately after that best result was obtained.

What the exposed terms show about reward structure. Among the fifteen records with `task_pass` 1 and `rule_conformance` 1.0, reward tracks `wall_clock_sec` / `qualifying_budget` negatively and strongly across coarse bands: ~16.5–17.0 s yields 0.7393–0.7997; ~13.4–14.8 s yields 0.7716–0.8255; 6.63 s yields 0.8820; 3.34 s yields 0.8841. But wall clock does not fully determine reward, and this is important. Attempt 6 ran in 13.427 s with `compute_efficiency` 0.9465 and `per_step_cost_ratio` 0.9711 and scored 0.8059, below attempt 5 which ran *longer* (13.740 s) at `compute_efficiency` 0.7476 and scored 0.8255. Attempt 9 reached `compute_efficiency` 1.0 and still scored only 0.7891. Attempt 11 at 17.003 s (0.7997) outscored attempt 17 at 14.844 s (0.7716). So there is a residual reward component that the supplied terms do not name, and neither `compute_efficiency` nor `per_step_cost_ratio` is a proxy for it. Also note the returns to speed have flattened at the top: cutting 6.628 s to 3.337 s bought only 0.0021 of reward.

## 2. Approach classes tried

No source-level description of any attempt carried into this summary, so these classes are grouped by what the measured terms distinguish. Records that failed identically are collapsed into one entry.

**Class A — the non-reaching configuration (attempt 1).** `conformance_fraction` 0.0, `primary_target_reached` 0.0, `task_pass` 0, both declared perturbations failing to reach. `per_step_cost_ratio` 1.019 and `compute_efficiency` 1.0, so it was cheap per step; it simply never crossed the threshold in the declared direction, and it ran 89.978 s of wall clock. Reward 0.0000.

**Class B — the mid-budget conforming baseline (attempts 2, 3, 4, 5, 6, 7, 9, 17).** Full conformance, `task_pass` 1, both perturbation kinds reaching, wall clock in the 13.4–14.8 s band, `per_step_cost_ratio` between 0.971 and 1.852, `compute_efficiency` between 0.5487 and 1.0. Rewards 0.7716–0.8255. This class was worked over repeatedly with the per-step cost ratio pushed both up (attempt 7 at 1.596, attempt 17 at 1.852) and down (attempt 6 at 0.971, attempt 9 at ratio 1.192 with efficiency 1.0), and the reward stayed inside a 0.054-wide band throughout. Best member: attempt 5 at 0.8255.

**Class C — the long-budget variants (attempts 8, 10, 11, 12).** Same full conformance and both perturbations reaching, but wall clock stretched to 16.5–17.0 s. Rewards 0.7393–0.7997, uniformly at or below the Class B band. Longer runtime bought nothing.

**Class D — the heavy per-step configuration (attempt 13).** `per_step_cost_ratio` 7.185 against a stated ceiling of 3.0, wall clock 37.202 s against a stated ceiling of 31.1. Both perturbation units still reached their own thresholds and `rule_conformance` stayed 1.0, and `primary_target_reached` was 1.0 — but `red_line_crossed` went to 1.0, `validity` to 0.0, `task_pass` to 0, and reward to 0.0000 with `zero_reason_code` 1.

**Class E — the fast conforming configuration (attempts 14, 16).** Wall clock 6.628 s and 3.337 s, `per_step_cost_ratio` 1.869 and 1.706, `compute_efficiency` 0.5031 and 0.8460, full conformance, `task_pass` 1, both perturbations reaching. Rewards 0.8820 and 0.8841. This class produced the two best results in the series and is where the frontier now sits.

**Class F — the fast configuration with shape fingerprinting (attempt 15).** Wall clock 4.681 s, `per_step_cost_ratio` 1.873 — squarely in Class E's cost profile and faster than attempt 14 — but it tripped `C-NO-SHAPE-FINGERPRINT`, which dropped `rule_conformance` to 0.8571 and `task_pass` to 0 and held reward to 0.7288, the lowest non-zero score recorded. Both perturbation units still reached. This is the single clearest cost measurement available: at roughly Class E speed, that one check cost on the order of 0.15 of reward.

## 3. Checks that failed

**`C-BUDGET-RESPECTED` — failed in two graded records, and it is the finding that matters most.** In attempt 1 the verifier's reason was "no qualifying row, so no budget position exists". In attempt 13 the reason was "the qualifying row sits at 37.20223784446716 on the wall_clock_sec axis, above the declared ceiling of 31.1". It also appears among the failed checks of both of attempt 1's perturbation units, so it has been recorded failing four times in total across the primary and held-out runs. Whatever was changed between attempt 1 and attempt 13 is not what causes this check to fail: the check survived twelve intervening attempts and reappeared. The two reasons are different in kind — one is a downstream consequence of no row qualifying at all, the other is a genuine runtime overrun against a ceiling of 31.1 s on the `wall_clock_sec` axis — and the ceiling number is the concrete, reusable fact: 31.1 s.

**`C-TARGET-REACHED` — failed in attempt 1 only,** reason "no evaluation row crosses the threshold in the declared direction". It also appears in both of attempt 1's perturbation units, so three recorded failures, all inside that one record. No later attempt has failed it.

**`C-PERTURBATION-REACHED` — failed in attempt 1 only,** reason "0 of 2 declared perturbations reached their own threshold inside their own budget".

**`C-LOG-WELL-FORMED` — failed once,** in attempt 1, on the ruleset-kind perturbation run only. No reason string was supplied for the perturbation-level checks.

**`C-NO-LATCH-CARRYOVER` — failed once,** in attempt 1, on the ruleset-kind perturbation run only.

**`C-PER-STEP-COST-CEILING` — failed once,** in attempt 13, reason "per-step cost is 7.185 times the seed anchor, above the ceiling of 3.0". This names the hard ceiling explicitly: per-step cost must stay at or under 3.0× the seed anchor. Every scoring attempt has kept `per_step_cost_ratio` between 0.971 and 1.869, so there is real headroom under that ceiling.

**`C-NO-SHAPE-FINGERPRINT` — failed once,** in attempt 15, reason "the submission fingerprints the model by shape". This is the only check ever to fail in a record that still scored: it drove `rule_conformance` to 0.8571 (six of seven) and `task_pass` to 0 while reward remained 0.7288.

## 4. Ruled-out directions

**The attempt 1 configuration.** Reward 0.0000. Nothing crossed the threshold in the declared direction, so `C-TARGET-REACHED`, `C-BUDGET-RESPECTED` and `C-PERTURBATION-REACHED` all failed and `conformance_fraction` was 0.0. It also spent 89.978 s of wall clock, more than any other record. Ruled out on its own terms and never revisited after attempt 1.

**High per-step cost (attempt 13 profile).** Ruled out by two named ceilings simultaneously: `C-PER-STEP-COST-CEILING` at 7.185× against a ceiling of 3.0, and `C-BUDGET-RESPECTED` at 37.202 s against a ceiling of 31.1 s. `red_line_crossed` 1.0 and `validity` 0.0 zeroed the reward outright even though the primary target was reached and both perturbations held. Any direction that multiplies per-step work is bounded by 3.0× seed anchor and by 31.1 s of wall clock.

**Shape-based model fingerprinting.** Ruled out by `C-NO-SHAPE-FINGERPRINT` in attempt 15, reason "the submission fingerprints the model by shape". It zeroes `task_pass` and cuts `rule_conformance` to 0.8571 regardless of how fast the run is; attempt 15 was faster than attempt 14 and scored 0.1532 lower.

**Optimising `compute_efficiency` / `per_step_cost_ratio` as a reward lever within the mid-budget class.** Ruled out empirically. Attempt 9 reached `compute_efficiency` 1.0 and scored 0.7891; attempt 6 reached 0.9465 with `per_step_cost_ratio` 0.9711 and scored 0.8059; both are below attempt 5 which scored 0.8255 at `compute_efficiency` 0.7476 and `per_step_cost_ratio` 1.2599. Driving these two terms toward their nominal optimum did not increase reward and in two separate records decreased it.

**Stretching wall clock into the 16.5–17.0 s band (Class C).** Ruled out: attempts 8, 10, 11 and 12 all held full conformance and both perturbations, and all landed at 0.7393–0.7997, at or below the shorter-running Class B band. Extra runtime was not converted into reward.

**Re-tuning within the 13.4–14.8 s mid-budget band (Class B).** Ruled out as a path to the top: eight attempts occupy this band, spanning a wide range of per-step cost and efficiency settings, and every one of them scored between 0.7716 and 0.8255 — the entire band sits below both Class E results. Attempt 17 returned to this band immediately after attempt 16's 0.8841 and scored 0.7716, a clear regression.

## 5. Open leads

**Start from the attempt 16 profile.** Full conformance, `task_pass` 1, `red_line_crossed` 0, `validity` 1, `wall_clock_sec` 3.337, `qualifying_budget` 3.337, `per_step_cost_ratio` 1.706, `compute_efficiency` 0.8460, both perturbation kinds reaching, reward 0.8841. Attempt 14 corroborates the family at 6.628 s / ratio 1.869 / 0.8820. Whatever these two shared is the only thing that has broken 0.88, and rebuilding it is the first job.

**Attack the unexplained residual, not the clock.** Speed has nearly saturated: 6.628 s → 3.337 s bought 0.0021. But reward varies by up to 0.054 among runs at nearly identical wall clock (attempt 5 at 0.8255 versus attempts 2/3/4 at ~0.804, all near 13.5 s; attempt 11 at 17.0 s outscoring attempt 17 at 14.8 s). Some term the supplied metrics do not name — most plausibly the margin or quality of the qualifying evaluation row beyond merely crossing the threshold — is moving reward independently of time and efficiency. Holding wall clock near 3.3 s and pushing the final metric further past the threshold in the declared direction is the highest-value untested variation.

**Spend the per-step headroom to buy fewer steps.** The ceiling is 3.0× the seed anchor; attempt 16 sat at 1.706 and attempt 14 at 1.869. Roughly 1.6× of per-step cost is unused. A heavier but shorter schedule stays legal provided the ratio stays under 3.0 and wall clock stays under 31.1 s — attempt 13 shows what happens past both, so keep a wide margin on each.

**Keep the shape-agnostic path that attempt 16 used.** Attempt 15 was the fast profile plus shape fingerprinting and lost 0.1532 to it. Whatever model-dispatch mechanism attempt 16 used instead of shape inspection must be reproduced deliberately, not rediscovered by accident, since the stub is pristine and this is the one check that penalises a run without zeroing it — it is easy to reintroduce and easy to miss.

**Do not lose the ruleset-perturbation guarantees.** Across all seventeen records there were 34 held-out perturbation runs, two per record, one of kind `ruleset` and one of kind `held_out_variant`. Thirty-two of them reached their threshold — every one in attempts 2 through 17, both kinds, with no failed checks. The two failures both sit in attempt 1: the `held_out_variant`-kind run failed `C-TARGET-REACHED` and `C-BUDGET-RESPECTED`, and the `ruleset`-kind run failed those two plus `C-LOG-WELL-FORMED` and `C-NO-LATCH-CARRYOVER`. By kind, the `ruleset` run is the more fragile: it is the only kind ever to have failed `C-LOG-WELL-FORMED` or `C-NO-LATCH-CARRYOVER`. So log formatting and freedom from latched state carried between runs are requirements the ruleset run specifically enforces, and they have held unbroken since attempt 1 — a fast rewrite must not silently drop whichever practice keeps them holding.

**Call: exploit.** Take attempt 16 (0.8841, the mark to beat) and improve it, rather than restructure. The scoring approaches have not stopped improving — the jump from 0.8255 to 0.8820 to 0.8841 came from the fast conforming class and is recent — and the fastest legal run already leaves large margins under both named ceilings (1.706 against 3.0 per-step, 3.337 s against 31.1 s). Exploit means: reconstruct the fast full-conformance profile, keep the shape-agnostic dispatch, and spend the per-step headroom on pushing the qualifying row further past its threshold to move the residual reward term, since wall clock alone has flattened out. One caution drawn from the history: attempts 2 through 12 kept re-entering the 13–17 s mid-budget band with different efficiency settings and produced eight regressions in a row against attempt 5 without changing what bounded them — do not repeat that pattern in the fast band.
