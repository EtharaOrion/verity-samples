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

    All two attempts since have scored lower than it.
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

    attempt 2 -- reward 0.8385, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 74
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 4 -- reward 0.8719, better than every earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 50
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 6 -- reward 0.5615, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 204
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

    attempt 7 -- reward 0.0000, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached no, qualifying budget --
      perturbation runs: 0 of 2 reached
        one held_out_variant run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
        one seed run did not reach its threshold -- C-TARGET-REACHED, C-BUDGET-RESPECTED
      narrative: the verifier recorded these checks as not holding
        C-TARGET-REACHED -- no evaluation row crosses the threshold in the declared direction
        C-BUDGET-RESPECTED -- no qualifying row, so no budget position exists
        C-PERTURBATION-REACHED -- 0 of 2 declared perturbations reached their own threshold inside their own budget

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE has failed on 2 attempts (1, 6). Whatever has been
      changing between them is not what is causing it.
    C-BUDGET-RESPECTED has failed on 2 attempts (3, 7). Whatever has been
      changing between them is not what is causing it.
    C-PERTURBATION-REACHED has failed on 2 attempts (3, 7). Whatever has been
      changing between them is not what is causing it.
    C-TARGET-REACHED has failed on 2 attempts (3, 7). Whatever has been
      changing between them is not what is causing it.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Seven graded submissions, all with `measurement_status: measured`, so all seven carry a reward. Ranked worst to best:

| Rank | Attempt | reward | Notes |
|---|---|---|---|
| 1 (worst) | 3 | 0.0000 | zero_reason_code 4; primary target not reached; both perturbation runs failed; wall_clock 1692.52 s |
| 1 (worst, tied) | 7 | 0.0000 | zero_reason_code 4; identical check failures to attempt 3; wall_clock 1692.21 s |
| 3 | 6 | 0.5615 | conformant-run but C-API-SURFACE failed; rule_conformance 0.8571; task_pass 0; wall_clock 204.09 s |
| 4 | 1 | 0.7684 | C-API-SURFACE failed; rule_conformance 0.8571; task_pass 0; wall_clock 25.46 s |
| 5 | 2 | 0.8385 | fully clean; task_pass 1; wall_clock 73.62 s |
| 6 | 4 | 0.8719 | fully clean; task_pass 1; wall_clock 50.03 s; compute_efficiency 1.0 |
| 7 (best) | 5 | 0.9128 | fully clean; task_pass 1; wall_clock 25.34 s |

**Attempt 5 holds the highest reward, 0.9128. That is the score to beat.**

Direction of travel, stated plainly rather than smoothed:
- Attempt 3 (0.0000) was **worse than an earlier attempt** — it lost the whole reward that attempt 2 had already earned (0.8385).
- Attempt 6 (0.5615) was **worse than an earlier attempt** — a regression from attempt 5's 0.9128, giving up roughly 0.35 of reward.
- Attempt 7 (0.0000) was **worse than an earlier attempt** — the second total loss, again after a clean, high-scoring attempt had already been achieved.
- Only attempts 2, 4 and 5 were recorded as better than every earlier attempt.

Every record produced a measurement; none must be read as "no measurement". The two zeros are genuine measured zeros with zero_reason_code 4, not absent data.

Supporting terms for the scored attempts, since reward tracks them:

- `validity` is 1.0 in all seven records and `red_line_crossed` is 0.0 in all seven. Neither has ever been the problem.
- `rule_conformance` is 1.0 in five records and 0.8571428571 in attempts 1 and 6 — exactly the two records that failed C-API-SURFACE.
- `task_pass` is 1.0 only in attempts 2, 4 and 5. Attempts 1 and 6 reached the primary target (`primary_target_reached` 1.0) and held both perturbations, yet still scored `task_pass` 0.0. The only differentiating term is the C-API-SURFACE failure and the resulting rule_conformance of 0.8571. **Reaching the target is not sufficient; a conformance failure suppresses task_pass and costs a large slice of reward while still leaving a non-zero score.**
- Among the three fully clean attempts, reward rose monotonically as `wall_clock_sec` / `qualifying_budget` fell: 73.62 s → 0.8385, 50.03 s → 0.8719, 25.34 s → 0.9128. This is the strongest signal in the data for how to improve on 0.9128.
- `compute_efficiency` does *not* track reward monotonically: attempt 4 had compute_efficiency 1.0 and scored 0.8719, while attempt 5 had 0.7728 and scored higher at 0.9128. Do not optimise compute_efficiency as a proxy for reward. `per_step_cost_ratio` likewise does not rank the attempts (attempt 5's was 0.9887, attempt 4's 0.7115, and 5 outscored 4).

# 2. Approach classes tried

The measured terms do not carry source code, so the classes below are grouped by their measured signature. Records with the same signature are one entry.

**Class A — clean, fast-converging trainer (attempts 2, 4, 5).** Reaches the primary target inside budget, rule_conformance 1.0, no failed checks, both declared perturbations reached, task_pass 1.0. Three instances, differing essentially in run length: 73.62 s, 50.03 s, 25.34 s of qualifying budget, scoring 0.8385, 0.8719 and 0.9128 respectively. This is the only class that has ever produced task_pass 1.0, and it contains the best result. Within the class, the shortest qualifying budget scored best.

**Class B — same converging trainer but with disallowed module-level code (attempts 1, 6).** Also reaches the primary target and holds both perturbations, but trips C-API-SURFACE for "module-level statements outside imports, constants, and permitted definitions". rule_conformance drops to 0.8571428571, task_pass falls to 0.0, and reward lands at 0.7684 (25.46 s) and 0.5615 (204.09 s). Note that attempt 1 at 25.46 s scored 0.7684 while attempt 5 at 25.34 s — essentially the same budget — scored 0.9128. The gap of roughly 0.14 at matched runtime is the direct price of the C-API-SURFACE violation. Attempt 6 shows the two penalties compounding: a violation *and* a 204 s budget gave the worst non-zero score.

**Class C — long-running, non-converging configuration (attempts 3, 7).** Both ran to 1692.52 s and 1692.21 s wall clock — near-identical durations, consistent with hitting a hard cap rather than terminating on their own criterion — and in both cases no evaluation row crossed the threshold in the declared direction. rule_conformance was 1.0 in both, so these were *rule-clean but non-performing*: the code was well-formed and the training simply never reached the target. `qualifying_budget` is "not-measured" in both because no qualifying row exists. Both scored 0.0000. This class was tried twice and produced the identical failure signature both times.

# 3. Checks that failed

**C-API-SURFACE — "module-level statements outside imports, constants, and permitted definitions". Failed twice, in attempt 1 and attempt 6.** Between those two attempts the runtime changed enormously (25.46 s vs 204.09 s), per_step_cost_ratio changed (1.0639 vs 1.3778) and compute_efficiency changed (0.8160 vs 0.6091) — yet the identical check failed with the identical reason. Whatever was altered between attempts 1 and 6 is not what causes C-API-SURFACE. The cause is structural: executable statements sitting at module scope in the submission file that are not imports, not constant assignments, and not permitted definitions (functions/classes). Fixing it means moving all such top-level work — setup calls, prints, device selection, seeding, data loading, `if`/`for` blocks, anything that runs on import — inside the permitted function or class bodies, leaving the module body containing only imports, plain constant bindings, and definitions.

**C-TARGET-REACHED — "no evaluation row crosses the threshold in the declared direction". Failed twice, in attempt 3 and attempt 7.** Recorded both as a top-level failure and, separately, on every perturbation run in those two records.

**C-BUDGET-RESPECTED — "no qualifying row, so no budget position exists". Failed twice, in attempt 3 and attempt 7.** This is a downstream consequence of C-TARGET-REACHED, not an independent budget overrun: with no row crossing the threshold there is nothing to measure a budget position against. It is not evidence that the budget itself was too tight.

**C-PERTURBATION-REACHED — "0 of 2 declared perturbations reached their own threshold inside their own budget". Failed twice, in attempt 3 and attempt 7.**

The C-TARGET/C-BUDGET/C-PERTURBATION triple has now failed twice with byte-identical reasons and near-identical 1692 s runtimes. Whatever differed between attempts 3 and 7 did not touch the cause; both are the same failure re-run.

**Perturbation unit outcomes.** Every record declares 2 perturbations, one of kind `held_out_variant` and one of kind `seed`. Across the seven records that is 14 held-out runs in total: 10 reached their threshold and 4 did not. By kind: the `held_out_variant` kind reached in 5 of 7 records and failed in 2; the `seed` kind reached in 5 of 7 records and failed in 2. The four failures all occurred inside attempts 3 and 7, and in each of those records **both** kinds failed together, on the same pair of checks, C-TARGET-REACHED and C-BUDGET-RESPECTED. No perturbation kind has ever failed while the primary target was reached, and no kind has ever failed on its own. The runs are not identified across records, so nothing here says that any particular run recurred; what the data supports is only this: perturbation failure has been all-or-nothing and has co-occurred exactly with primary-target failure. In every record where the primary target was reached — including the two C-API-SURFACE records — `all_perturbations_held` was true. Generalisation to held-out variants and to reseeding has never been the limiting factor; convergence has.

# 4. Ruled-out directions

**Leaving any executable statement at module scope.** Ruled out because C-API-SURFACE failed on exactly this reason twice, and in both cases it forced task_pass to 0.0 and rule_conformance to 0.8571428571 even though the run reached its primary target and held both perturbations. At matched runtime (attempt 1, 25.46 s, 0.7684 versus attempt 5, 25.34 s, 0.9128) the violation cost about 0.14 of reward for no benefit.

**The long-running configuration of attempts 3 and 7.** Ruled out: run to ~1692 s twice, no evaluation row ever crossed the threshold in the declared direction, both perturbations failed, reward 0.0000 both times. Re-running this shape without changing what prevents convergence is not exploration and not exploitation — and the record shows it was already done twice, the second time after a 0.9128 result was in hand. That specific repetition must not happen again.

**Spending more wall clock to buy accuracy.** Ruled out by the ordering of the clean attempts: 73.62 s → 0.8385, 50.03 s → 0.8719, 25.34 s → 0.9128. Longer qualifying budgets scored strictly worse among conformant runs, and the two longest runs of all (1692 s) scored zero. Nothing in the data shows a longer run buying a better score.

**Optimising `compute_efficiency` as a reward proxy.** Ruled out: attempt 4 achieved compute_efficiency 1.0 and scored 0.8719, below attempt 5's 0.9128 at compute_efficiency 0.7728. The two do not co-rank.

**Work aimed at robustness to held-out variants or to reseeding, as a way to raise the score.** Ruled out as a lever: `all_perturbations_held` was true in all five records that reached the primary target, and the only perturbation failures were collateral to a primary target that was never reached. There is no headroom here.

**Anything aimed at `validity` or at avoiding a red line.** Ruled out: validity is 1.0 and red_line_crossed is 0.0 in all seven records. Neither has ever bound.

# 5. Open leads

**Lead 1 — reproduce Class A exactly, at or under the ~25 s qualifying budget of attempt 5, and change nothing else first.** Attempt 5's profile is the target: rule_conformance 1.0, no failed checks, primary_target_reached 1.0, both perturbations reached, task_pass 1.0, qualifying_budget 25.34 s, reward 0.9128. Establishing that baseline is the prerequisite for any further change, because two of the last five submissions gave the whole score away.

**Lead 2 — push the qualifying budget below ~25 s while holding conformance and target.** This is the one lever the data actually supports, and it is a clean monotone trend across the three conformant attempts (73.62 → 50.03 → 25.34 s giving 0.8385 → 0.8719 → 0.9128). Concretely: fewer epochs/steps, earlier stopping the moment the evaluation row crosses the threshold in the declared direction, cheaper per-step work, less redundant evaluation. The hard constraint is that C-TARGET-REACHED and C-PERTURBATION-REACHED must still hold on both the primary run and both held-out runs — cutting the budget too far converts a 0.91 into a 0.0000, which is precisely what happened in attempts 3 and 7. Trim in small increments and keep a margin above the threshold rather than sitting on it.

**Lead 3 — audit the module body before submitting, every time.** Read the finished file top to bottom and confirm the module scope contains only `import`/`from` statements, simple constant assignments, and `def`/`class` definitions. Nothing else: no seeding call, no device probe, no data download, no logging, no `if`/`for`/`try` at top level, no `if __name__ == "__main__"` block if that is not a permitted definition. This check has cost 0.14 and 0.35 of reward on two separate occasions and is entirely mechanical to prevent.

**Lead 4 — separate the two failure modes when experimenting.** Attempt 6 shows they compound: a C-API-SURFACE violation plus a 204 s budget produced the worst non-zero score, 0.5615. Change one thing per submission — either the budget or the code structure — so that a regression is attributable.

**Lead 5 — if the target margin is unknown, measure it.** The gap between attempt 5's converging 25 s run and the non-converging runs is not characterised by any term supplied. Knowing how much headroom exists above the threshold at 25 s would tell you how far Lead 2 can safely go before it turns into another 0.0000.

**Call: exploit.** Take Class A — specifically the attempt 5 configuration that scored 0.9128 — and improve it along the single dimension the measurements support, a shorter qualifying budget with rule_conformance held at 1.0 and both perturbation runs still reaching their thresholds. The scored approach has not stopped improving (0.8385 → 0.8719 → 0.9128 across three clean submissions), so structural exploration is not yet warranted, and the two structural departures attempted so far both returned 0.0000 with the same three check failures.
