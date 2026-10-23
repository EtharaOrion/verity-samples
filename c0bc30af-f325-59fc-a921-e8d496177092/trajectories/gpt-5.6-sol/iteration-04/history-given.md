# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 3 -- reward 0.8657, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.8630   1.000             2 of 2         yes             76                
  2        0.8079   1.000             2 of 2         yes             74                
  3 *      0.8657   1.000             2 of 2         yes             74                

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

    attempt 1 -- reward 0.8630, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 76
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 2 -- reward 0.8079, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Three graded submissions, all of them measured. Ordered worst to best by reward:

- **Attempt 2 — reward 0.8079.** `standing_against_best_so_far` reads `worse_than_an_earlier_attempt`. This is plainly a regression against attempt 1, not progress: it is the lowest reward on record despite having the best compute numbers of the three (`compute_efficiency` 0.7226, `per_step_cost_ratio` 0.9441, `wall_clock_sec` 74.2572).
- **Attempt 1 — reward 0.8630.** `standing_against_best_so_far` reads `first_measured_attempt`. `compute_efficiency` 0.6784, `per_step_cost_ratio` 1.0723, `wall_clock_sec` 76.3367 (the slowest of the three).
- **Attempt 3 — reward 0.8657.** `standing_against_best_so_far` reads `better_than_every_earlier_attempt`. `compute_efficiency` 0.6922, `per_step_cost_ratio` 0.9835, `wall_clock_sec` 74.3681.

**Attempt 3 holds the highest reward, 0.8657, and it is the one to beat.**

Every record shares the same clean secondary profile: `task_pass` 1.0, `validity` 1.0, `rule_conformance` 1.0, `conformance_fraction` 1.0, `primary_target_reached` 1.0, `red_line_crossed` 0.0, `zero_reason_code` 0, `all_perturbations_held` true. In all three, `qualifying_budget` is numerically identical to `wall_clock_sec`, so the budget being scored is the measured wall clock itself and nothing is being clipped or discounted before it lands.

The spread across all three attempts is only 0.0578, and the gap between the best (0.8657) and the previous best (0.8630) is 0.0027. That margin is small enough that it should not be treated as a demonstrated improvement of mechanism until it is reproduced.

## 2. Approach classes tried

The records carry no source, so the approaches are distinguishable only by their measured compute signature. Three distinct operating points were reached, and no two records duplicate one:

- **Class A — expensive-per-step baseline (attempt 1).** `per_step_cost_ratio` 1.0723, i.e. each step costs about 7% more than the harness reference step; longest wall clock at 76.3367 s; lowest `compute_efficiency` at 0.6784. Scored 0.8630.
- **Class B — aggressive per-step cost reduction (attempt 2).** `per_step_cost_ratio` driven down to 0.9441, the cheapest step of the three, lifting `compute_efficiency` to its maximum observed value of 0.7226 and trimming wall clock to 74.2572 s. Scored 0.8079 — the worst reward measured.
- **Class C — near-parity step cost (attempt 3).** `per_step_cost_ratio` 0.9835, essentially parity with the reference step; `compute_efficiency` 0.6922; wall clock 74.3681 s, statistically indistinguishable from class B's. Scored 0.8657 — the best reward measured.

The important structural fact across these three classes is that reward is **not** monotone in `compute_efficiency`. The run with the highest efficiency (B, 0.7226) produced the lowest reward, and the two runs with efficiency near 0.68–0.69 produced the two highest rewards. Whatever the reward is weighting most heavily, cheapening the individual step is not it, and past a point it actively costs reward. Class C recovered nearly all of B's wall-clock saving (74.37 s vs 74.26 s, a difference of 0.11 s) while giving back the per-step cost cut, and gained 0.0578 of reward over B in doing so. That pairing is the single most informative contrast in the record.

## 3. Checks that failed

None. `failed_checks` is empty in all three records, at the top level and inside every perturbation unit. `conformance_fraction` is 1.0 and `rule_conformance` is 1.0 throughout; `red_line_crossed` is 0.0 and `zero_reason_code` is 0 in every case. There is no repeated failing check to report, because there is no failing check at all.

On the held-out runs: each record declares `perturbations_declared` 2.0 and carries exactly two `perturbation_units`, one of kind `held_out_variant` and one of kind `seed`. Every one of them has `reached` true and an empty `failed_checks`. By kind: the `held_out_variant` runs reached their threshold in all three records, and the `seed` runs reached their threshold in all three records. In aggregate that is six held-out units across the three graded submissions, all six held, none stopped by any check, and `all_perturbations_held` true in every record. Nothing is being identified about which specific run is which, and no run should be assumed to be the same one across two records.

The practical consequence: conformance and robustness are not the binding constraint here. Reward is being lost inside the scored quantity itself, not to a gate.

## 4. Ruled-out directions

- **Minimising per-step cost / maximising `compute_efficiency` as the primary objective.** Ruled out by attempt 2 directly. It achieved the best `per_step_cost_ratio` (0.9441) and the best `compute_efficiency` (0.7226) of any attempt and returned the worst reward, 0.8079, a fall of 0.0551 from attempt 1's 0.8630. Pushing the step cheaper is a measured loss, not a gain.
- **Work aimed at conformance, validity, rule adherence, or red-line avoidance.** Ruled out because those terms are already saturated in every record: `conformance_fraction` 1.0, `rule_conformance` 1.0, `validity` 1.0, `task_pass` 1.0, `red_line_crossed` 0.0. There is no headroom there and no failing check to repair, so effort spent on them cannot move the reward.
- **Hardening against the held-out perturbations.** Ruled out on the same grounds: both kinds, `held_out_variant` and `seed`, reached threshold in all three records with no failed checks. Robustness is not what is capping the score.
- **Returning to the class A operating point unchanged.** Its wall clock, 76.3367 s, is about 2 s longer than either later attempt and its `per_step_cost_ratio` of 1.0723 is the only above-parity value on record, yet it still scored below attempt 3. It is dominated: attempt 3 is faster, cheaper per step, and higher reward.

## 5. Open leads

- **Rebuild the class C operating point first and confirm it.** Attempt 3's configuration — `per_step_cost_ratio` near 1.0 (0.9835), wall clock about 74.4 s, `compute_efficiency` about 0.69 — is the best-scoring regime known and must be reconstructed from the stub before anything is varied, since the next attempt sees none of the earlier code. Getting back to 0.8657 is the floor for the attempt to be informative.
- **Buy wall clock with fewer steps rather than cheaper steps.** The wall clock and the qualifying budget are the same number, so total elapsed time is scored directly, while the per-step cost cut is what appears to have cost attempt 2 its reward. That separation suggests reducing the *count* of steps (earlier stopping once `primary_target_reached` is secure, a shorter schedule) while holding per-step fidelity at parity, rather than degrading each step. Attempts 2 and 3 differ by only 0.11 s of wall clock but 0.0578 of reward, which says the last fraction of a second of elapsed time is worth far less than whatever attempt 2 sacrificed to get it.
- **Probe for margin above the primary target.** `primary_target_reached` is a saturated 1.0 indicator and tells us nothing about how far above the target the run finished. Since reward moves substantially while every reported gate stays pinned at 1.0, the unreported quality margin is the most likely carrier of the 0.0578 swing. A run at the class C compute point but with deliberately more headroom on the target would test that directly.
- **Explore the space between class A and class C on per-step cost.** The three sampled ratios are 0.9441 (bad), 0.9835 (best), 1.0723 (middling). The peak is bracketed but coarsely; a point around 1.00–1.04 would show whether reward is still climbing just above parity or whether 0.9835 is already near the optimum.
- **Treat the 1-to-3 gain as unconfirmed.** 0.8630 to 0.8657 is 0.0027 and there is no repeated measurement of any single configuration, so seed-to-seed variation of the reward is unknown. If a rebuild of class C lands materially away from 0.8657, the ranking between classes A and C is not yet established and small-margin tuning against it is wasted.

**Call: exploit.** Take the class C configuration that scored 0.8657, reproduce it, and improve it along the one axis the evidence supports — fewer total steps and more target margin at unchanged per-step fidelity. The approaches that scored have not stopped improving, no gate is blocking, and one structurally different direction has already been tested and measured as worse; there is nothing here that justifies exploring away from the best point yet. Note for the record that attempt 2 pushed further along an axis (cheaper steps) that attempt 1's numbers already made questionable, and it lost 0.0551 of reward doing so — repeating that axis without changing what made it lose would be neither exploration nor exploitation.
