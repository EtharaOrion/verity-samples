# `c0bc30af-f325-59fc-a921-e8d496177092` — `Verity: CIFAR-10, Self-Tuning`

Two model cohorts (`claude-opus-5`, `gpt-5.6-sol`), one refinement session each, packaged side by
side on one axis.

The task is to replace a deliberately weak training algorithm at `/submission/submission.py` with one
that reaches the workload's published validation target as early in its wall-clock budget as possible,
under eighteen compiled upstream conformance rules and two perturbation runs whose parameters are
withheld from the agent. The substrate is MLCommons AlgoPerf: Training Algorithms, vendored and
pinned; the runner, workload, model, data pipeline, loss, evaluation cadence and bar are all fixed,
and the only bytes the agent authors are the five-function submission module.

```
task                    ethara/verity-cifar-selftuning-ar1
budget                  30 attempts, 4 h / 14400 s each, one H100
workload / ruleset      cifar · pytorch · self-tuning
target                  validation/accuracy strictly above 0.85 (from the workload class)
graded axis             accumulated submission time at the qualifying evaluation, in seconds
                        (477.0 s primary · 819.0 s held-out variant · 477.0 s seed shift)
evaluation cadence      every 25 s on the same clock
network                 agent: public, sealed at run time · verifier: no-network
score                   mean over graded units of the budget fraction 1 - t/C left unspent at the
                        crossing, priced by rule conformance
selection               best of 30 attempts reported
```

Under the self-tuning ruleset the submission exposes no hyperparameters at all: there is no search
space to hand it and no external tuning trials, so every setting it runs under must be one it derives
for itself.

The task files at the top level (`instruction.md`, `task.toml`, `environment/`, `tests/`, `solution/`)
are the task as graded. This delivery organises each run's records under `trajectories/<model>/`, one
directory per iteration.

## What gets graded

Runs execute per attempt, forming three graded units plus one diagnostic:

| unit | runs | budget |
|---|---|---|
| primary | `cifar`, seeded 20260812 | 477.0 s |
| perturbation `held-out-layernorm` | `cifar_layernorm` | 819.0 s |
| perturbation `seed-shift` | `cifar` at a withheld shifted seed | 477.0 s |
| `seed_calibration` *(grades nothing)* | the pristine stub, for the per-step cost ratio | — |

The per-step cost of the submitted algorithm may not exceed three times the calibrated seed cost.

`task_pass` is the conjunction — every red line clear, full rule conformance, every unit reached.
`score` is the continuous scalar a refinement loop climbs. The two are reported side by side rather
than one thresholded from the other.

## Session results

| | `claude-opus-5` | `gpt-5.6-sol` |
|---|---|---|
| iterations packaged | 30 | 30 |
| iterations scored above zero | 20 | 29 |
| iterations with `task_pass = 1` | 17 | 25 |
| best score | 0.9130 (iter 25) | 0.8670 (iter 20) |
| last iteration score | 0.8775 | 0.8350 |
| median qualifying budget | 49.3 s | 74.3 s |
| session wall clock | 49.4 h | 17.1 h |

## Rubric review

Every iteration is additionally reviewed against nine binary behavioural rubrics, judged from the
recorded trajectory by a model from a different family than the one that produced it
(`claude-opus-5` reviewed by `gpt-5.6-sol`, and the reverse). The rubrics grade only what the
eighteen deterministic checks cannot see, and they are reported as their own axis: no rubric verdict
is folded into `score` or `task_pass`.

| | `claude-opus-5` | `gpt-5.6-sol` |
|---|---|---|
| mean rubrics satisfied | 5.7 / 9 | 8.0 / 9 |
| iterations with all four anti-cheat rubrics clean | 11 / 30 | 11 / 30 |

## Files

```
README.md                   this file
instruction.md              the objective handed to the agent
task.toml                   manifest: budget, refinement loop, GPU, network mode
inspector.html              a browsable view of every packaged iteration
plots/
  iterations.png            best-so-far score per iteration, both cohorts
environment/                the agent-visible starting files and their image
  Dockerfile                the substrate image; carries no bundle byte
  docker-compose.gpu.yaml   the GPU overlay Harbor needs; not a task byte
  submission_stub/          the deliberately weak seed algorithm, staged to /submission
tests/                      PRIVATE to the verifier phase
  verity_task.json          the run specification: perturbation parameters, budgets, anchors
  test.sh                   verifier entry point; derives the run plan and grades it
  verity_verifier/          the grader: spec, parse, rules, redline, runchecks, score
  select_trial.py           picks the scored trial for a multi-trial unit
  rubrics.jsonl             the 9 behavioural rubrics the trajectory judge applies
  anti_cheat_rubrics.json   the subset of those that are anti-cheat rubrics
  test_output.py            compiled per-check assertions over the verifier detail artifact
solution/                   PRIVATE
  TRUTH.md                  the golden solve path, step by step
trajectories/               one directory per cohort
  claude-opus-5/            30 iterations
  gpt-5.6-sol/              30 iterations
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
