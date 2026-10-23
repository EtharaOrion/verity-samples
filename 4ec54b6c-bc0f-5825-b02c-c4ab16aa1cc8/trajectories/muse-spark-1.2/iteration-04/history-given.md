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

    All one attempts since have scored lower than it.
    An earlier attempt reached this standing. Do not discard the approach the prose
    below describes without a measured reason to.

  attempt  reward   rule conformance  perturbations  target reached  qualifying budget 
  1        0.6694   1.000             2 of 2         yes             17                
  2 *      0.7155   1.000             2 of 2         yes             17                
  3        0.6279   1.000             2 of 2         yes             20                

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

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 3 -- reward 0.6279, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 20
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

## 1. Results so far

Three attempts have been graded, and all three produced a measurement (`measurement_status: measured`). Ranked worst to best by reward:

- **Attempt 3 — reward 0.6279.** `standing_against_best_so_far: worse_than_an_earlier_attempt`. This is plainly a regression, not progress: it scored below both attempt 1 and attempt 2. Compute efficiency 0.6033, wall clock 20.3003 s, qualifying budget 20.3003, per-step cost ratio 1.5225.
- **Attempt 1 — reward 0.6694.** `standing_against_best_so_far: first_measured_attempt` (the baseline). Compute efficiency 0.5488, wall clock 17.4264 s, qualifying budget 17.4264, per-step cost ratio 1.5134.
- **Attempt 2 — reward 0.7155.** `standing_against_best_so_far: better_than_every_earlier_attempt`. Compute efficiency 0.6205, wall clock 17.4531 s, qualifying budget 17.4531, per-step cost ratio 1.5175.

**Attempt 2 holds the highest reward, 0.7155, and it is the one to beat.**

Every one of the three attempts was fully valid and fully conformant: `task_pass: 1.0`, `validity: 1.0`, `rule_conformance: 1.0`, `conformance_fraction: 1.0`, `primary_target_reached: 1.0`, `red_line_crossed: 0.0`, `zero_reason_code: 0`, `all_perturbations_held: true`. No attempt has ever scored zero and no attempt has ever been unmeasured. The entire spread between 0.6279 and 0.7155 therefore comes from the efficiency/cost terms, not from correctness or conformance.

Held-out runs: each record declared 2 perturbation units (`perturbations_declared: 2.0`), one of kind `held_out_variant` and one of kind `ruleset`. In all three records, both reached their thresholds with no failed checks. Aggregate across the graded work: 6 of 6 held-out runs reached threshold — 3 of 3 for kind `held_out_variant`, 3 of 3 for kind `ruleset`. No check has ever stopped a held-out run of either kind.

## 2. Approach classes tried

The measured terms carry no source code, so the approaches can only be characterised by the cost/efficiency profile each one produced. On that basis the three attempts fall into two classes, and the class boundary is sharp:

**Class A — same-budget variants (attempts 1 and 2).** Both finished in essentially identical wall clock, 17.4264 s and 17.4531 s (a difference of 0.027 s, i.e. runtime was held fixed), with near-identical per-step cost ratio, 1.5134 and 1.5175. What changed between them was compute efficiency: 0.5488 → 0.6205, a gain of 0.0717. Reward moved 0.6694 → 0.7155, a gain of 0.0461. This class is the productive one: it shows that at fixed budget, raising compute efficiency raises reward at roughly 0.64 reward per unit of efficiency. Attempt 2 is the best-scoring member and the current high-water mark.

**Class B — longer-budget variant (attempt 3).** Wall clock rose to 20.3003 s, +2.85 s (about +16%) over class A, and per-step cost ratio rose slightly to 1.5225. Compute efficiency landed at 0.6033 — above attempt 1 but *below* attempt 2. Reward fell to 0.6279, below both class-A attempts. Spending more wall clock did not buy back the reward it cost; the extra budget was strictly harmful.

Two facts hold across every attempt regardless of class: the task and all held-out variants pass unconditionally, and per-step cost ratio sits in a tight band of 1.5134–1.5225, always above 1.5. Nothing tried so far has moved the per-step cost ratio meaningfully in either direction.

## 3. Checks that failed

None. `failed_checks` is empty in all three records, for the primary run and for both perturbation units of both kinds in every record. There is no repeated check failure to diagnose, no named check identifier to fix, and no conformance defect anywhere in the record: `conformance_fraction` is 1.0 and `rule_conformance` is 1.0 throughout, and `all_perturbations_held` is true throughout. No held-out run of kind `held_out_variant` and no held-out run of kind `ruleset` has been stopped by a check.

The practical consequence for the next attempt: correctness and conformance are solved and must be *preserved*, not chased. Reward is being lost entirely in the efficiency and budget terms. Any change that risks `task_pass`, `validity`, `rule_conformance`, or a held-out run in exchange for speed is trading a solved constraint for an unsolved one and will be caught by the harness.

## 4. Ruled-out directions

- **Spending more wall clock / a larger qualifying budget.** Attempt 3 ran 20.3003 s against class A's ~17.44 s and scored 0.6279 versus attempt 2's 0.7155 — a loss of 0.0876. It achieved this while still passing every check and holding both perturbations, so the loss is attributable to the budget/cost terms, not to any failure. `qualifying_budget` tracks `wall_clock_sec` exactly in all three records, so wall clock *is* the budget being charged. Longer-running variants are ruled out.
- **Chasing compute efficiency at the cost of runtime.** Attempt 3 had efficiency 0.6033, higher than attempt 1's 0.5488, yet scored *lower* than attempt 1 (0.6279 vs 0.6694). An efficiency gain of 0.0545 did not survive a runtime increase of 2.87 s. Efficiency gains only paid off in class A, where runtime was pinned. Ruled out: any efficiency improvement bought with additional wall clock.
- **Further work aimed at conformance, validity, or the held-out runs.** Zero failed checks in three of three records, 6 of 6 held-out runs reached, `red_line_crossed: 0.0` every time. There is no reward available here; effort spent is effort wasted.
- **Re-running the attempt-3 configuration unchanged.** Whatever structural change pushed wall clock to 20.3 s must be reverted or replaced. Repeating it without removing the runtime cost would repeat the regression.

## 5. Open leads

1. **Restore the attempt-2 operating point first, then improve on it.** Attempt 2's profile is the target to reproduce: wall clock ≈ 17.45 s, compute efficiency ≈ 0.6205, per-step cost ratio ≈ 1.5175, all checks passing. Treat ~17.4 s as a hard runtime ceiling and do not exceed it.

2. **Push compute efficiency above 0.6205 at fixed ~17.4 s wall clock.** This is the only movement the record shows actually paying. The attempt-1 → attempt-2 pair gives an observed exchange rate of about 0.64 reward per unit of compute efficiency when runtime is held constant. Efficiency at 0.6205 still leaves substantial headroom toward 1.0; closing even a further 0.05 would be worth roughly +0.03 reward on that rate.

3. **Attack the per-step cost ratio, which has never moved.** It has sat at 1.5134, 1.5175, 1.5225 across three attempts — a total spread of 0.009 — meaning every change made so far left the per-step cost essentially untouched. It is above 1.5 in all three records, suggesting each step costs about half again a reference step. This is the one dimension of the profile that is both unexplored and plausibly reducible; a genuine reduction here should show up as more work done inside the same 17.4 s and hence as higher compute efficiency.

4. **Reduce wall clock below 17.4 s if it can be done without giving back efficiency.** The record only shows the penalty for going *up* in runtime (attempt 3), never the reward for going down; both class-A attempts sat at effectively the same runtime. A shorter run at attempt-2-level efficiency is untested and is the cheapest untested direction available. A rough two-point extrapolation from attempt 3 against attempt 2 suggests roughly 0.027 reward per second of wall clock, but this rests on a single contrast and should be treated as a hypothesis to test, not a coefficient to optimise against.

5. **Change one factor at a time and record the resulting (wall_clock, compute_efficiency, per_step_cost_ratio) triple.** The class-A pair is informative precisely because runtime was pinned and only efficiency moved; attempt 3 moved two things at once and is correspondingly harder to read. Keeping runtime pinned isolates the efficiency signal.

**Call: exploit.** Attempt 2 scored 0.7155 and its approach class is still improving — the class-A pair went 0.6694 → 0.7155 with runtime held fixed, and has not plateaued. There are no failed checks to repair and no structural blocker to route around, so a structurally different idea would be abandoning a working, fully conformant approach with visible headroom in compute efficiency and an entirely untouched per-step cost ratio. Rebuild the attempt-2 configuration, hold wall clock at or below ~17.45 s, and drive compute efficiency above 0.6205.
