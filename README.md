<div align="center">

# [verity-samples](#contact)

## [Abstract](#contact)

This repository is the delivery surface of the Verity corpus. It holds authored task bundles in the Harbor format, one directory per task, each named by a content-derived UUID. A bundle carries everything a run pins, everything it grades, and everything it forbids: a manifest, the agent-visible instruction, a container environment holding the seed submission, a verifier tree that grades the submitted bytes, and a private solution tree holding the reference submission and its derivation record.

Thirty bundles are present at this revision, each a distinct design across two upstream workloads and five archetypes. Every one of them is self-contained and reviewable from the outside: the manifest and the run specification together state the full contract, and no grading behaviour lives only in verifier code.

## [Summary](#contact)

| Property                   | Value                                                                       |
| -------------------------- | --------------------------------------------------------------------------- |
| Bundles                    | 30                                                                          |
| Delivery format            | Harbor bundle manifest, version 1.3                                         |
| Substrate                  | MLCommons AlgoPerf: Training Algorithms, vendored and pinned                |
| Framework                  | PyTorch, on all 30                                                          |
| Tuning ruleset             | Self-tuning, on all 30                                                      |
| Workloads                  | `mnist_fine_grained` and `cifar`                                        |
| Archetypes                 | 5, spanning 4 durable failure modes                                         |
| Graded axis                | Accumulated submission time in seconds at the qualifying evaluation         |
| Conformance rules          | 18, compiled from upstream prose into deterministic checks                  |
| Graded runs per submission | 3, all conjuncts, plus a seed anchor run                                    |
| Pass predicate             | Conjunctive over rule conformance, metric threshold, and every perturbation |
| Reward                     | Continuous in the closed interval 0 to 1, separate from the pass            |
| Declared tier              | Baseline                                                                    |

## [Coverage](#contact)

Two upstream workloads are represented across five archetypes.

| Archetype                         | `mnist_fine_grained` | `cifar`   | Total        |
| --------------------------------- | ---------------------- | ----------- | ------------ |
| AR1 Long-Horizon State Collapse   | 4                      | 3           | 7            |
| AR3 Tool-Chaining Brittleness     | 3                      | 1           | 4            |
| AR6 Silent-Execution Failures     | 4                      | 2           | 6            |
| AR7 Ambiguous Intermediate States | 4                      | 2           | 6            |
| AR9 Temporal-Reasoning Gap        | 7                      | 0           | 7            |
| **Total**                   | **22**           | **8** | **30** |

Each bundle also names the durable failure mode it is built to provoke, which is the property that has to survive the perturbation runs rather than merely appear once.

| Durable failure mode           | Bundles |
| ------------------------------ | ------- |
| `silent-change-survival`     | 10      |
| `chained-precision-survival` | 7       |
| `temporal-revision-survival` | 7       |
| `backend-writeback-survival` | 6       |

Every bundle sets `replicate_count = 1` and carries a distinct `design_id`, so the thirty directories are thirty distinct designs rather than replicates of a smaller set. Slot identifiers are unique, 22 in the `M` series and 8 in the `C` series.

## [Bundle structure](#contact)

[The layout is uniform across all 30 bundles.](#contact)

| Path                                                                         | Role                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `task.toml`                                                                | Harbor manifest, version 1.3. Carries`[task]`, `[metadata]`, `[environment]`, `[agent]`, `[verifier]`, and `[verifier.environment]`. Every Verity field lives in `[metadata]`, which Harbor treats as a free-form mapping, so the manifest loads under a strict Harbor loader |
| `instruction.md`                                                           | The only agent-visible prose in the bundle                                                                                                                                                                                                                                                  |
| `environment/Dockerfile`                                                   | The agent image build                                                                                                                                                                                                                                                                       |
| `environment/submission_stub/submission.py`                                | The working baseline the agent is handed and must beat: plain SGD at a small fixed rate, with no momentum, adaptivity, or schedule                                                                                                                                                          |
| `tests/test.sh`                                                            | Verifier entrypoint, executed inside the verifier environment                                                                                                                                                                                                                               |
| `tests/verity_task.json`                                                   | The run specification: objective, perturbations, conformance set, submission surface, and upstream provenance                                                                                                                                                                               |
| `tests/verity_verifier/`                                                   | The committed checkers, as`main`, `rules`, `reward`, `redline`, `parse`, `runchecks`, and `spec`                                                                                                                                                                              |
| `tests/rubrics.jsonl`, `tests/select_trial.py`, `tests/test_output.py` | Rubric carrier, trial selection, and output assertions                                                                                                                                                                                                                                      |
| `solution/`                                                                | Private. Reference submission,`solve.sh`, generated `TRUTH.md`, `grounding.yaml`, `recompute.py`, provenance pair, rubrics, and a tuning search space in 15 of the 30                                                                                                               |

The manifest declares three collected artifacts: the submitted `/submission/submission.py`, the run logs under `/logs/runs` excluding checkpoints, and the verifier output under `/logs/verifier`.

## [Why it is hard](#contact)

Five properties compose, and each one closes a route that would otherwise be shorter than solving the task.

| Property                            | What it closes                                                                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Conjunctive pass over three runs    | A submission tuned to the primary objective still has to hold under both perturbations, against the same submitted bytes                         |
| Withheld perturbation parameters    | The kinds are disclosed so the target is legible; the parameters are not, so the answer has to generalise rather than anticipate                 |
| Self-tuning ruleset                 | No hyperparameters are exposed and no search space is shipped, so a tuning sweep is not available as a substitute for an algorithm               |
| Eighteen compiled conformance rules | Workload identification and model fingerprinting are rejected at the syntax level, so one setting that works everywhere is the conforming answer |
| Per-step compute red line           | Buying the metric with larger steps crosses a red line instead of paying a penalty                                                               |
| Sealed agent phase                  | Everything needed is already in the container, so the work is authoring rather than retrieval                                                    |

## [Scoring](#contact)

The verifier driver runs nine steps in a fixed order and writes the reward contract path on every code path, including every early exit. A file the agent left behind can never survive, and a zero is always attributable to a named reason rather than to an unwritten file.

The same code serves the graded path and the authoring feasibility pass over frozen logs, so a bundle is checked by the instrument that will grade it. A short step-capped calibration run of the bundle's own seed stub executes on the same device in the same verifier phase and backs the compute-efficiency term alone.

The pass is a conjunction because the upstream rules are disqualifying rather than merely costly, and a weighted blend would let a rule violation be bought back with speed. The reward is continuous because a pass-or-fail signal gives a refinement loop no gradient to climb.

## [Execution environment](#contact)

| Property               | Value                                 | Why                                                                                                                                                                                                                                                            |
| ---------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent image            | Pinned by digest                      | Reproducibility of the authoring surface                                                                                                                                                                                                                       |
| Verifier image         | Named by tag, uniquely per workload   | Harbor sets`skip_tests_upload` for separate-environment mode and expects the image to already own `/tests/test.sh`. A digest would cycle, because writing it changes the bundle bytes, which changes the content-derived UUID, which stales the baked copy |
| `[environment] gpus` | `0`                                 | Harbor's Docker backend declares no GPU capability and refuses a non-zero request. The device is granted by the orchestrator compose overlay instead.`gpu_types` is documentation                                                                            |
| Verifier mode          | `separate`, `no-network`          | `[verifier.environment]` is required. Without it Harbor derives the separate verifier baseline from `[environment]`, which is public, and refuses                                                                                                          |
| Agent network          | Declared`public`, sealed at runtime | The orchestrator seals the agent onto an internal network reaching only the solver proxy. A declared no-network would ask Docker for a post-start network switch it cannot perform, and the trial would refuse to start                                        |
| Agent timeout          | A backstop, not a budget share        | Derived so the per-attempt ceiling gate holds against the minimum attempt floor. The figure is withheld from`instruction.md`                                                                                                                                 |

The agent image deliberately differs from the graded image. It carries the agent scaffold and the package manager but not the held-out variant classes.

The agent phase runs sealed: the solver endpoint is reachable, package indexes and code hosts are not. Everything needed is already in the container, because the pinned harness carries the vendored upstream documentation and the workload class. The verifier phase is closed as well, and its deterministic red line fails closed when the probe record is absent.

## [Pins](#contact)

Every bundle pins the same two upstream trees by commit:

| Component | Commit                                       |
| --------- | -------------------------------------------- |
| Harness   | `966bbfbcc0b6a33e7af5e670433ab5f4d84ad83a` |
| Harbor    | `f78dd6854d99ba7cbf9f00649a4e85ce5d99046f` |

The verifier holds a frozen set of pinned packages. An added dependency that re-pins one of them is a red-line crossing.

## [The private boundary](#contact)

The boundary is enforced rather than described. The solution tree, the reference submission, the identity of every pinned perturbation, and the reference evaluation log never appear on the agent-visible surface.

`solution/TRUTH.md` is generated by `solution/recompute.py` from `solution/grounding.yaml` and is never hand-authored. It opens with a canary block of four derived identifiers and then states the ordered path a conforming submission takes through the instruction. Each step names the action, the state it establishes, the mutation or silent drift it must survive, and exactly one checker identifier it satisfies. The named checker set equals the committed checker set by identifier, and the steps close over the deliverable manifest, so a checker set weaker than the instruction is detectable from outside the checkers.

`solution/grounding.yaml` holds only what the bundle cannot reconstruct from itself or from the pinned harness. Workload targets, budgets, metric names, the registry, and optimizer settings are all readable elsewhere and are not copied into it.

`solution/provenance.yaml` and its signature carry the fork ancestry digest, the canonical upstream repository identity, and the atom result digests for the screening and sanitization passes.

## [Reading a bundle](#contact)

This repository carries no runner. A bundle is executed by the orchestrator in the parent repository, which supplies the device overlay and the agent seal.

Read `task.toml` first. No grading behaviour lives only in verifier code, so the manifest and the run specification together state the full contract.

## [Attribution](#contact)

Built on MLCommons AlgoPerf: Training Algorithms, Apache-2.0. No Verity number is an AlgoPerf result and no MLCommons endorsement is implied.

The upstream benchmark must be cited separately and is not superseded by this work.

## [License](#contact)

MIT. See `LICENSE`.

The vendored upstream harness is Apache-2.0 and its licence and notice travel with it. MLCommons AlgoPerf is named in every delivered artifact, and the Verity name never substitutes for naming it.

## [Contact](#contact)

Organization: Ethara.AI

Security and benchmark-integrity disclosure follows the parent repository's `SECURITY.md`. Do not open a public issue for a contamination finding or a leaked task byte.
