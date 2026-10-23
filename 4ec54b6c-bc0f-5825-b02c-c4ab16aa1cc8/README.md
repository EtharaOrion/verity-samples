# `4ec54b6c-bc0f-5825-b02c-c4ab16aa1cc8` — `Verity: MNIST Fine-Grained, Self-Tuning`

Three model cohorts (`claude-opus-5`, `gpt-5.6-sol`, `muse-spark-1.2`), one refinement session each,
packaged side by side on one axis.

The task is to replace a deliberately weak training algorithm at `/submission/submission.py` with one
that reaches the workload's published validation target as early in its wall-clock budget as possible,
under eighteen compiled upstream conformance rules and two perturbation runs whose parameters are
withheld from the agent. The substrate is MLCommons AlgoPerf: Training Algorithms, vendored and
pinned; the runner, workload, model, data pipeline, loss, evaluation cadence and bar are all fixed,
and the only bytes the agent authors are the five-function submission module.

```
task                    ethara/verity-mnist_fine_grained-selftuning-ar9
budget                  25 attempts, 3 h / 10800 s each, one H100
workload / ruleset      mnist_fine_grained · pytorch · self-tuning
target                  validation/accuracy strictly above 0.97 (from the workload class)
graded axis             accumulated submission time at the qualifying evaluation, in seconds
                        (31.1 s primary · 45.4 s held-out variant · 31.1 s external ruleset)
evaluation cadence      every 3 s on the same clock
network                 agent: public, sealed at run time · verifier: no-network
score                   mean over graded units of the budget fraction 1 - t/C left unspent at the
                        crossing, priced by rule conformance
selection               last attempt reported
```

The task files at the top level (`instruction.md`, `task.toml`, `environment/`, `tests/`, `solution/`)
are the task as graded. This delivery organises each run's records under `trajectories/<model>/`, one
directory per iteration.

## What gets graded

Six runs execute per attempt, forming three graded units plus one diagnostic:

| unit | runs | budget |
|---|---|---|
| primary | `mnist_fine_grained`, seeds 73 / 4242 / 8821, reduced by median | 31.1 s |
| perturbation `held-out-layernorm` | `mnist_layernorm`, seed 73 | 45.4 s |
| perturbation `external-ruleset` | `mnist_fine_grained`, external ruleset, 5 trials | 31.1 s |
| `seed_calibration` *(grades nothing)* | the pristine stub, 100 steps, for the per-step cost ratio | — |

`task_pass` is the conjunction — every red line clear, full rule conformance, every unit reached.
`score` is the continuous scalar a refinement loop climbs. The two are reported side by side rather
than one thresholded from the other.

## Session results

| | `claude-opus-5` | `gpt-5.6-sol` | `muse-spark-1.2` |
|---|---|---|---|
| iterations packaged | 23 | 25 | 25 |
| iterations scored above zero | 20 | 21 | 24 |
| iterations with `task_pass = 1` | 18 | 17 | 20 |
| best score | 0.9151 (iter 23) | 0.6964 (iter 06) | 0.7322 (iter 19) |
| reported under `last` | 0.9151 | 0.4899 | 0.6392 |
| median qualifying budget | 13.92 s | 27.81 s | 19.98 s |
| session wall clock | 48.9 h | 33.5 h | 18.4 h |

## Files

```
README.md                   this file
instruction.md              the objective handed to the agent
task.toml                   manifest: budget, refinement loop, GPU, network mode
plots/
  iterations.png            best-so-far score per iteration, all three cohorts
environment/                the agent-visible starting files and their image
  Dockerfile                the substrate image; carries no bundle byte
  docker-compose.gpu.yaml     the GPU overlay Harbor needs; not a task byte
  submission_stub/          the deliberately weak seed algorithm, staged to /submission
tests/                      PRIVATE to the verifier phase
  verity_task.json          the run specification: perturbation parameters, budgets, anchors
  test.sh                   verifier entry point; derives the run plan and grades it
  verity_verifier/          the grader: spec, parse, rules, redline, runchecks, score
  select_trial.py           picks the scored trial for an external-tuning unit
  rubrics.jsonl             the 9 behavioural rubrics the trajectory judge applies
  anti_cheat_rubrics.json   the subset of those that are anti-cheat rubrics
  test_output.py            compiled per-check assertions over the verifier detail artifact
solution/                   PRIVATE
  TRUTH.md                  the golden solve path, step by step
trajectories/               one directory per cohort
  claude-opus-5/            23 iterations
  gpt-5.6-sol/              25 iterations
  muse-spark-1.2/           25 iterations
  <cohort>/iteration-NN/
    config.json             the trial as configured
    iteration.json          outcome, score, tokens, timing, submission digest
    result.json             the trial as it ended (embeds config and the reward contract)
    history.md              the memory document this iteration produced for the next
    history-given.md        the memory document this iteration was handed
    agent/trajectory.json   the structured agent trajectory
    artifacts/submission.py the submitted bytes
    verifier/reward.json    the verifier's measurement — the authority
    verifier/outcomes.json  per-check pass/fail behind that measurement
    verifier/rubric_verdicts.json  the rubric review: overall pass, per-rubric verdicts
```
