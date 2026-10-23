# What earlier attempts measured

  Every number in this table is measured. The prose below it is a summary of the work and
  is not measured: an attempt that failed can describe a change that never took effect, so
  treat any claim there that this table does not support as unverified.

  BEST ATTEMPT SO FAR -- this is the standing to beat

    attempt 5 -- reward 0.8255, better than every earlier attempt   (best so far)
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    It is also the most recent attempt, so this is where the work stands.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.0000   1.000             0 of 2         no              --                
  2        0.8037   1.000             2 of 2         yes             13                
  3        0.8042   1.000             2 of 2         yes             14                
  4        0.8042   1.000             2 of 2         yes             14                
  5 *      0.8255   1.000             2 of 2         yes             14                

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

    attempt 3 -- reward 0.8042, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.8042, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 14
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

  Checks that did not hold, and the attempts they did not hold on:
    C-BUDGET-RESPECTED failed on attempt 1.
    C-PERTURBATION-REACHED failed on attempt 1.
    C-TARGET-REACHED failed on attempt 1.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Five graded records, all of which carry a reward. Listed worst to best:

- **Attempt 1 — reward 0.0000.** `measurement_status: measured_phase_cut`, `zero_reason_code: 4`, `task_pass: 0.0`, `primary_target_reached: 0.0`, `conformance_fraction: 0.0`, `qualifying_budget: "not-measured"`. Three primary checks failed and both declared perturbations failed. `validity: 1.0` and `rule_conformance: 1.0` were still clean, and `per_step_cost_ratio` was 1.0194 — the cheapest per-step cost of any attempt — but nothing reached its threshold, so none of that counted. `red_line_crossed: 0.0`.
- **Attempt 2 — reward 0.8036778762879345 (0.8037).** `measured_phase_cut`, but fully passing: `task_pass: 1.0`, `primary_target_reached: 1.0`, `conformance_fraction: 1.0`, no failed checks, both perturbations held. `compute_efficiency: 0.6203`, `per_step_cost_ratio: 1.4966`, `wall_clock_sec: 13.4877`, `qualifying_budget: 13.4877`. Standing: better than every earlier attempt.
- **Attempt 4 — reward 0.8041887297475568 (0.8042).** `measured`, all checks clean, both perturbations held. `compute_efficiency: 0.5835` (the lowest efficiency of any passing attempt), `per_step_cost_ratio: 1.4974`, `wall_clock_sec` and `qualifying_budget: 13.6584`. **Standing: `worse_than_an_earlier_attempt` — this was a regression, not progress.** It is placed above attempt 2 here only because its raw reward is marginally higher; against the then-best (attempt 3) it went down.
- **Attempt 3 — reward 0.8042363383093786 (0.8042).** `measured`, all checks clean, both perturbations held. `compute_efficiency: 0.6051`, `per_step_cost_ratio: 1.5320`, `wall_clock_sec` and `qualifying_budget: 13.6621`. Standing: better than every earlier attempt at the time. Note attempts 3 and 4 both round to 0.8042; at full precision attempt 3 is the higher of the two.
- **Attempt 5 — reward 0.8254758711461578 (0.8255).** `measured`, all checks clean, both perturbations held. `compute_efficiency: 0.7476`, `per_step_cost_ratio: 1.2599`, `wall_clock_sec` and `qualifying_budget: 13.7398`. Standing: better than every earlier attempt.

**Attempt 5, at reward 0.8255, holds the highest reward and is the one to beat.** No record is missing a measurement; every one of the five was measured and produced a number, including attempt 1, whose 0.0000 is a genuine measured zero rather than an absent result.

# 2. Approach classes tried

The measured terms describe outcomes, not source, so these classes are inferred from the metric signature each record left behind. Three distinct classes are visible.

**Class A — non-converging / non-conforming run (attempt 1).** The run never crossed the primary threshold in the declared direction, so no qualifying row existed and no budget position could be computed. Its distinguishing fingerprint is `per_step_cost_ratio: 1.0194` — essentially baseline per-step cost, the cheapest ever recorded — combined with `wall_clock_sec: 89.9778`, roughly 6.6× the wall clock of every later attempt. In other words, this class spent very little per step but ran far longer and still never reached the target. It also produced a malformed log and a latch-carryover violation on the ruleset perturbation, so it was failing on more than convergence alone. This class was abandoned after one record and never revisited.

**Class B — converging run at roughly 1.50× per-step cost (attempts 2, 3, 4).** All three clear every check, hit the primary target, hold both perturbations, and land in a tight band: `per_step_cost_ratio` 1.4966 / 1.5320 / 1.4974, `compute_efficiency` 0.6203 / 0.6051 / 0.5835, `wall_clock_sec` 13.4877 / 13.6621 / 13.6584, rewards 0.8037 / 0.8042 / 0.8042. The total spread in reward across these three is 0.0006. Whatever was varied between attempts 2, 3 and 4 moved the reward by less than a thousandth and moved `compute_efficiency` in the wrong direction (0.6203 → 0.6051 → 0.5835, monotonically down). Treat these three as one approach that was tuned twice without effect; attempt 4 in particular is recorded as worse than an earlier attempt.

**Class C — converging run at reduced per-step cost (attempt 5).** Same clean-check, target-reached, both-perturbations-held profile as class B, but `per_step_cost_ratio` drops from ~1.50 to 1.2599 and `compute_efficiency` rises from ~0.60 to 0.7476. Reward rises by ~0.0213 to 0.8255. Notably its `wall_clock_sec` (13.7398) is the *highest* of the four passing attempts, and its `qualifying_budget` (13.7398) is likewise the largest — so the gain did not come from finishing sooner. The gain tracks per-step cost, not elapsed time. This is the single most informative signal in the whole record set.

# 3. Checks that failed

All failures are confined to attempt 1. Attempts 2 through 5 have empty `failed_checks` at the primary level and empty `failed_checks` on every perturbation unit.

Primary-level failures in attempt 1:

- **C-TARGET-REACHED** — "no evaluation row crosses the threshold in the declared direction".
- **C-BUDGET-RESPECTED** — "no qualifying row, so no budget position exists". This is a downstream consequence of C-TARGET-REACHED: with nothing qualifying, budget cannot be located at all.
- **C-PERTURBATION-REACHED** — "0 of 2 declared perturbations reached their own threshold inside their own budget".

Perturbation-level failures in attempt 1 are recorded in section 5's aggregate below and named here: on the ruleset-kind run, **C-LOG-WELL-FORMED**, **C-TARGET-REACHED**, **C-BUDGET-RESPECTED**, **C-NO-LATCH-CARRYOVER**; on the held-out-variant-kind run, **C-TARGET-REACHED** and **C-BUDGET-RESPECTED**.

Counting across the whole record set: **C-TARGET-REACHED failed three times** (once at primary, once on the ruleset run, once on the held-out-variant run) and **C-BUDGET-RESPECTED failed three times** in exactly the same three places — but all six of those failures sit inside the single attempt 1, and neither check has failed since. **C-LOG-WELL-FORMED** and **C-NO-LATCH-CARRYOVER** failed once each, both on the ruleset-kind run only, and never on the held-out-variant kind. Whatever changed between attempt 1 and attempt 2 did fix all of these; they are solved and are not the current obstacle. There is no check that recurs across two or more separate records.

# 4. Ruled-out directions

- **The class A configuration behind attempt 1 (cheap per step, very long wall clock, never converges).** Ruled out because it scored 0.0000 with `zero_reason_code: 4` and `task_pass: 0.0`: no evaluation row ever crossed the threshold in the declared direction, so C-TARGET-REACHED failed, C-BUDGET-RESPECTED could not even be evaluated, and 0 of 2 perturbations reached their own threshold. Its attractive `per_step_cost_ratio` of 1.0194 is worthless without convergence. Do not reintroduce whatever made this run take 89.98s without reaching target.
- **Emitting logs that trip C-LOG-WELL-FORMED and carrying latch state across into the ruleset perturbation (C-NO-LATCH-CARRYOVER).** Ruled out because both fired on the ruleset run in attempt 1 and are the only kind-specific failures ever observed. Whatever hygiene the later attempts adopted must be preserved verbatim — per-perturbation state must be reset, and log rows must remain well-formed.
- **Further micro-tuning inside the class B band (per-step cost ~1.50, efficiency ~0.58–0.62).** Ruled out because three records in that band produced rewards spanning only 0.0006 (0.8037, 0.8042, 0.8042) while efficiency fell monotonically, and one of those three is explicitly recorded as `worse_than_an_earlier_attempt`. This region is flat-to-declining; more of the same will not beat 0.8255.
- **Chasing wall clock as the lever.** Ruled out by the data: the best reward (attempt 5) has the *longest* wall clock among passing attempts (13.7398s vs 13.4877s for the worst-scoring passing attempt), and `qualifying_budget` equals `wall_clock_sec` in every passing record. Elapsed time varies by under 2% across attempts 2–5 while reward moved 0.0218. Reward is not being bought with seconds.
- **Trading conformance for speed.** Ruled out preemptively by attempt 1's structure: `validity` and `rule_conformance` were both 1.0 there and it still scored zero, while `conformance_fraction` was 0.0. Passing checks is a gate, not a slider — there is no partial credit visible for a run that misses the target.

# 5. Open leads

**Aggregate perturbation outcomes.** Ten perturbation runs across five records, two per record, one of each kind every time. By kind: the **ruleset** kind reached its threshold in 4 of 5 records, failing only in attempt 1, where it was stopped by C-LOG-WELL-FORMED, C-TARGET-REACHED, C-BUDGET-RESPECTED and C-NO-LATCH-CARRYOVER. The **held-out-variant** kind also reached in 4 of 5 records, failing only in attempt 1, stopped by C-TARGET-REACHED and C-BUDGET-RESPECTED. In aggregate, 8 of 10 perturbation runs held, and `all_perturbations_held` is true for attempts 2 through 5. No perturbation kind is currently failing. The runs are not individually identified across records, so nothing here should be read as tracking one particular run over time.

Leads worth pursuing, in priority order:

1. **Push `per_step_cost_ratio` further toward 1.0 while keeping convergence.** This is the one lever with demonstrated effect. Moving from ~1.50 to 1.2599 raised `compute_efficiency` from ~0.60 to 0.7476 and reward from ~0.8042 to 0.8255 — about +0.021 of reward for −0.24 of cost ratio. Attempt 1 proves a ratio near 1.02 is physically attainable in this harness; the open question is whether it is attainable *together with* crossing the target, which attempt 1 never did. If the relationship stays roughly linear, closing the remaining 0.26 gap to baseline is worth on the order of another two hundredths of reward. Reproduce whatever attempt 5 did to cut per-step overhead and extend it.
2. **Identify precisely what attempt 5 changed relative to attempts 2–4 and amplify only that.** The delta is visible entirely in per-step cost, not in wall clock, not in budget, not in conformance. Any change that does not move `per_step_cost_ratio` down should be expected to produce a null result, as attempts 3 and 4 did.
3. **Accept a slightly larger wall clock and budget if it buys per-step cost.** Attempt 5 already did this (largest `qualifying_budget` of any passing run, 13.7398) and was rewarded for it. `C-BUDGET-RESPECTED` has held comfortably in every converging run, so there appears to be headroom, though the exact ceiling is not stated in these terms — do not push so far that budget position becomes a risk.
4. **Preserve the passing skeleton unchanged.** `validity`, `rule_conformance` and `conformance_fraction` are all 1.0 and `red_line_crossed` is 0.0 in all four passing attempts; the per-perturbation reset and log formatting that fixed C-LOG-WELL-FORMED and C-NO-LATCH-CARRYOVER must be carried over intact. The next attempt starts from a pristine stub, so these must be re-established, not assumed.

**Call: exploit.** The scoring approach — the class C converging run — has just improved by 0.0213 on its most recent measurement, so it has not stopped improving, and its improvement is attributable to one identified quantity (`per_step_cost_ratio`) that still has a large unexploited gap to the 1.0194 baseline attempt 1 demonstrated. Take attempt 5's configuration and drive per-step cost down further while keeping the target and both perturbation thresholds reached. Do not re-run the class B band unchanged: attempts 3 and 4 already did that twice and produced a 0.0006 spread and one recorded regression, and repeating it again would be neither exploration nor exploitation.
