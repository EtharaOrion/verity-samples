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

    All seven attempts since have scored lower than it.
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
  6 earlier attempt(s) are not detailed here; their measured row is above.

    attempt 1 -- reward 0.6694, first measured attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 1.000, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: every rule check the verifier ran held.

    attempt 9 -- reward 0.5164, worse than an earlier attempt
      approach: not measured -- the unverified prose below is the only account of it
      measured: rule conformance 0.857, target reached yes, qualifying budget 17
      perturbation runs: 2 of 2 reached
      narrative: the verifier recorded these checks as not holding
        C-API-SURFACE -- module-level statements outside imports, constants, and permitted definitions

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

  Checks that did not hold, and the attempts they did not hold on:
    C-API-SURFACE failed on attempt 9.

# What earlier attempts were trying, as summarised prose (UNVERIFIED)

# 1. Results so far

Eleven records were supplied. Nine carry a reward; two do not.

Ranked worst to best by reward:

| Rank | Attempt | reward | standing_against_best_so_far |
|---|---|---|---|
| 1 (worst) | 9 | 0.5164 | worse than an earlier attempt |
| 2 | 8 | 0.5444 | worse than an earlier attempt |
| 3 | 4 | 0.5792 | worse than an earlier attempt |
| 4 | 10 | 0.5983 | worse than an earlier attempt |
| 5 | 3 | 0.6279 | worse than an earlier attempt |
| 6 | 5 | 0.6587 | worse than an earlier attempt |
| 7 | 11 | 0.6639 | worse than an earlier attempt |
| 8 | 1 | 0.6694 | first measured attempt |
| 9 (best) | 2 | 0.7155 | better than every earlier attempt |

**Attempt 2 holds the highest reward, 0.7155. That is the score to beat.**

Attempts 6 and 7 have measurement_status `harbor_exception`. They produced **no measurement at all** — no reward, no compute_efficiency, no conformance, no perturbation units. They did not score zero; they were never scored, and nothing about the quality of their approach can be inferred from them in either direction.

The plain shape of the record is that attempt 2 was reached early and never surpassed. Every measured attempt from 3 onward — 3, 4, 5, 8, 9, 10, 11 — scored **lower** than attempt 2, and the verifier marks each of them `worse_than_an_earlier_attempt`. Attempt 11 (0.6639) is the strongest of the later attempts and it is still below attempt 1 (0.6694) as well as attempt 2. This is a regression-dominated history, not a progression, and it should not be read as convergence.

Supporting terms for the measured records:

| Attempt | reward | compute_efficiency | per_step_cost_ratio | wall_clock_sec | task_pass | rule_conformance |
|---|---|---|---|---|---|---|
| 1 | 0.6694 | 0.5488 | 1.5134 | 17.43 | 1.0 | 1.0 |
| 2 | 0.7155 | 0.6205 | 1.5175 | 17.45 | 1.0 | 1.0 |
| 3 | 0.6279 | 0.6033 | 1.5225 | 20.30 | 1.0 | 1.0 |
| 4 | 0.5792 | 0.8832 | 1.1656 | 17.51 | 1.0 | 1.0 |
| 5 | 0.6587 | 0.6098 | 1.6262 | 20.53 | 1.0 | 1.0 |
| 8 | 0.5444 | 0.9679 | 0.9674 | 26.10 | 1.0 | 1.0 |
| 9 | 0.5164 | 0.6647 | 1.4988 | 17.12 | **0.0** | **0.857** |
| 10 | 0.5983 | 0.5686 | 1.5152 | 20.15 | 1.0 | 1.0 |
| 11 | 0.6639 | 0.8424 | 1.0166 | 20.06 | 1.0 | 1.0 |

`red_line_crossed` is 0.0 and `zero_reason_code` is 0 on every measured record. `validity` is 1.0 on every measured record, including attempt 9. No submission was ever invalidated outright.

# 2. Approach classes tried

The supplied terms are measurements, not source. No record carries a description of the code that produced it, so the classes below are grouped by their measured signature — the combination of compute_efficiency, per_step_cost_ratio and wall_clock_sec that each submission produced. The next attempt should treat these as *signatures to reproduce or avoid*, not as recipes it can copy directly.

**Class A — the baseline-cost, short-wall configuration (attempts 1, 2).** per_step_cost_ratio ≈ 1.513–1.518, compute_efficiency 0.549–0.620, wall clock 17.43–17.45 s. This class contains both the best result (attempt 2, 0.7155) and the second-best (attempt 1, 0.6694). Between attempt 1 and attempt 2 the cost ratio and wall clock are essentially identical (1.5134→1.5175, 17.43→17.45 s) while compute_efficiency rose 0.549→0.620 and reward rose 0.669→0.716. Whatever changed between attempts 1 and 2 improved the score without changing the per-step cost or the runtime. This is the single most valuable transition in the whole record.

**Class B — the same cost profile at a longer wall clock (attempts 3, 10, and 5).** per_step_cost_ratio 1.515–1.626, compute_efficiency 0.569–0.610, but wall clock stretched to 20.15–20.53 s. Rewards: 0.6279 (attempt 3), 0.5983 (attempt 10), 0.6587 (attempt 5). All three sit below both Class A results. Holding the cost ratio near 1.5 and letting the wall clock grow from ~17.4 s to ~20.3 s coincided with a reward drop of roughly 0.06–0.12 relative to attempt 2. Attempt 5 pushed the per-step cost ratio highest of any record (1.6262) and still landed at 0.6587.

**Class C — the efficiency-maximising configuration (attempts 4, 11, 8).** This class drove per_step_cost_ratio down toward and past 1.0 and compute_efficiency up toward 1.0. Attempt 4: cost ratio 1.1656, efficiency 0.8832, wall 17.51 s, reward 0.5792. Attempt 11: cost ratio 1.0166, efficiency 0.8424, wall 20.06 s, reward 0.6639. Attempt 8: cost ratio 0.9674 (the only record below 1.0), efficiency 0.9679 (the highest recorded), wall 26.10 s (the longest recorded), reward 0.5444 (the lowest of any passing submission). The class is internally inconsistent — attempt 11 scored 0.6639 while attempt 4, with a *shorter* wall clock and comparable efficiency, scored 0.5792 — which is itself informative: efficiency alone does not order these results.

**Class D — the variant that broke the API surface (attempt 9).** Cost ratio 1.4988 and wall clock 17.12 s put it squarely in the Class A cost profile, and it recorded the shortest runtime of any attempt, but it failed the `C-API-SURFACE` check, took `task_pass` 0.0 and `rule_conformance` 0.857, and scored 0.5164 — the lowest reward of any record. See section 3.

**Class E — attempts that never reached measurement (attempts 6, 7).** Both terminated with `harbor_exception`. Nothing is known about what they attempted or whether the idea was good; the harness never got far enough to say. They are not evidence against anything.

**The finding that spans all classes.** On every measured record except attempt 9, `task_pass` is 1.0, `validity` is 1.0, `conformance_fraction` is 1.0, `rule_conformance` is 1.0, `primary_target_reached` is 1.0, `all_perturbations_held` is true, and `red_line_crossed` is 0.0 — yet reward ranges from 0.5444 to 0.7155. Every gate-style term is saturated and reward still varies by 0.17. Therefore reward carries a continuous quality component that none of the exposed terms reports directly, and it is not compute_efficiency: the two highest efficiencies in the record (0.9679 at attempt 8, 0.8832 at attempt 4) belong to the two lowest-scoring passing submissions. The next attempt must not treat "make it faster / cheaper per step" as a proxy for "make reward go up." The measured record contradicts that.

# 3. Checks that failed

**`C-API-SURFACE` — "module-level statements outside imports, constants, and permitted definitions."** Failed **once**, on attempt 9, and on no other record. Because it appears in exactly one record, it is not a recurring finding and there is no basis for saying that some persistent, unchanged element causes it; the eight other measured submissions passed it. The reason string is specific and directly actionable: the submission module executed statements at import time that were neither imports, nor constant assignments, nor permitted definitions (functions/classes). The fix is mechanical — move any top-level executable code (setup calls, seeding, config construction, prints, `if` blocks, loops, dataset instantiation, anything evaluated on import) inside the permitted function or class definitions, and leave only imports, plain constant assignments, and defs at module scope.

The cost of that one failure was severe and worth stating precisely: attempt 9 kept `validity` 1.0 and passed both perturbation units, but `rule_conformance` fell to 0.8571 (6 of 7), `task_pass` went to 0.0, and reward landed at 0.5164, the worst in the record — despite attempt 9 having the *shortest* wall clock of any submission (17.12 s) and a cost profile matching the winning Class A. Read plainly: attempt 9 may well have been a competitive submission that was cut down by a module-scope-statement violation. Reproducing its algorithmic content while obeying `C-API-SURFACE` is a concrete lead, not a speculation about a new method.

No other check failed anywhere in the record. `failed_checks` is empty for attempts 1, 2, 3, 4, 5, 8, 10 and 11, and empty for the two `harbor_exception` records — for those two, the empty list reflects that no checks were ever evaluated, not that all checks passed.

# 4. Ruled-out directions

**Pushing per_step_cost_ratio to or below 1.0 as a route to higher reward — ruled out.** Attempt 8 achieved cost ratio 0.9674 and compute_efficiency 0.9679, the best cost and efficiency figures in the entire record, and scored 0.5444, the lowest reward of any passing submission. Attempt 11 (cost ratio 1.0166, efficiency 0.8424) scored 0.6639 and attempt 4 (cost ratio 1.1656, efficiency 0.8832) scored 0.5792. All three are below attempt 2's 0.7155, which ran at cost ratio 1.5175. Three independent samples in this direction, all worse than the baseline profile. Cheapening the per-step work is buying efficiency at the expense of whatever the unexposed quality term measures.

**Letting the wall clock grow past ~20 s — ruled out.** Every record at 20.05–26.10 s (attempts 3, 5, 10, 11, 8) scored below attempt 2 at 17.45 s. The worst of all passing results, attempt 8, is also the longest run at 26.10 s. Note the important qualification: the reverse does not hold — attempts 4 (17.51 s, 0.5792) and 9 (17.12 s, 0.5164) were short and still scored poorly. A short wall clock is necessary in the observed data but demonstrably not sufficient. Do not "optimise for runtime" as an end in itself.

**Any submission with executable statements at module scope — ruled out by rule, not by score.** `C-API-SURFACE` converts an otherwise-passing run into `task_pass` 0.0. There is no version of this that is worth risking for convenience.

**Treating attempts 6 and 7 as evidence — ruled out.** They carry `harbor_exception` and no measurement. Whatever they contained is neither validated nor invalidated. They must not be counted as zeros, and their absence must not be used to argue that some direction "failed."

**Not ruled out, and specifically worth saying so: the perturbation dimension.** Nothing in the record has ever failed there. Redesigning for robustness against the held-out runs would be solving a problem that has never manifested. See section 5.

# 5. Open leads

**Perturbation status, reported in full.** Every measured record declared `perturbations_declared` 2.0 and returned exactly two perturbation units. By kind:

- **`held_out_variant`** — appears once in each of the nine measured records. Reached its threshold in all nine. `failed_checks` empty in all nine. Failure count by this kind: **zero**.
- **`ruleset`** — appears once in each of the nine measured records. Reached its threshold in all nine. `failed_checks` empty in all nine. Failure count by this kind: **zero**.

In aggregate that is **18 held-out perturbation runs across 9 measured attempts, 18 reached, 0 failed, and no check named as stopping any of them.** `all_perturbations_held` is true on every measured record. Attempts 6 and 7 returned empty `perturbation_units` because they were never measured, not because their runs failed.

The runs are deliberately unidentified. No name, number or position was given for any of them; the only thing distinguishing them is `kind`. Nothing here licenses a claim that any particular run recurs across records, and none is made. Notably, attempt 9 passed **both** perturbation units while failing `C-API-SURFACE` on the primary path — the perturbation checks and the API-surface check are independent, and passing the former says nothing about the latter.

**Leads worth trying next, in order of expected value:**

1. **Reconstruct the attempt-2 operating point and treat it as the floor.** Target the measured signature: wall clock ≈ 17.45 s, per_step_cost_ratio ≈ 1.52, compute_efficiency ≈ 0.62. Every deviation from that point so far has cost reward. Get a submission back into that envelope before attempting anything else, and verify the reward is near 0.7155 before layering changes on it.

2. **Chase the attempt-1 → attempt-2 delta.** That transition raised reward 0.6694 → 0.7155 (+0.046) while per_step_cost_ratio moved only 1.5134 → 1.5175 and wall clock only 17.43 → 17.45 s; compute_efficiency moved 0.549 → 0.620. This is the only unambiguous improvement in the record and it came from work that did *not* change the cost or runtime profile. It is the strongest evidence that the headroom lies in the unexposed quality term — model capacity, optimiser schedule, initialisation, regularisation, number of effective update steps at a fixed per-step cost — rather than in throughput. Push further along whatever axis that was: at fixed per-step cost near 1.52 and fixed wall clock near 17.4 s, spend the budget on better updates.

3. **Recover attempt 9's content under a compliant module structure.** Attempt 9 had the shortest wall clock of any record and a Class-A cost profile, and lost `task_pass` solely to module-level statements outside imports, constants and permitted definitions. Rebuild it with everything executable moved inside function or class bodies — module scope limited to imports, constant assignments and defs — and measure what it was actually worth. This is a cheap test of a data point that has never been fairly scored.

4. **Probe the wall-clock band between 17.4 s and 20.0 s.** There is a gap in the sampled data: the record contains points at ~17.1–17.5 s and at ~20.0–20.5 s and nothing between. If reward degrades smoothly with runtime in the Class-A cost regime, the 17.5–19 s band is unexplored and might hold a configuration that buys additional quality for a tolerable time cost. This is a secondary lead — pursue it only after (1) has re-established the baseline.

5. **Do not spend effort on perturbation robustness.** 18 of 18 held-out runs reached threshold with no failed check. There is no measured deficiency there to fix, and changes made in its name would only risk the primary path.

**Explore or exploit: exploit.** The exploit target is attempt 2 at reward 0.7155 — reproduce its operating point, then extend the attempt-1 → attempt-2 quality axis at constant per-step cost and runtime, and separately recover attempt 9's configuration under a `C-API-SURFACE`-compliant module layout. Exploration is not warranted here: the approach that scored best has not been re-tried since it scored, so it cannot be said to have stopped improving. What the later record does show is a pattern worth naming — attempts 4, 8 and 11 each re-entered the same efficiency-maximising direction after it had already scored below baseline, without changing the thing that made it score below baseline. That is neither exploration nor exploitation, and it should not be repeated.
