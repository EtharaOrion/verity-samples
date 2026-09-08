# Improve the MNIST handwritten-digit classification training algorithm

You are handed a working training algorithm and asked to make it better. The algorithm at `/submission/submission.py` runs to completion and produces a valid evaluation log today. What it does not do is reach the bar, because it takes plain gradient steps at a small fixed rate with no momentum, no adaptivity, and no schedule. Your job is to replace it with a training algorithm that does reach the bar, and to reach it as early as it can.

## What you are working on

The substrate is MLCommons AlgoPerf: Training Algorithms, vendored and pinned inside this environment. The runner, the workload, the model, the data pipeline, the loss, the evaluation cadence, and the bar are all fixed. The only code you write is the five-function submission module, which is the same contract the upstream benchmark defines. The vendored upstream documentation is in the environment and is the authority on that contract.

The workload is `mnist_fine_grained` under the `pytorch` framework and the self-tuning ruleset. The self-tuning ruleset means your submission exposes no hyperparameters at all: there is no search space, no tuning trial loop, and no external process that will pick values for you. Whatever your algorithm needs it must decide for itself, on the clock, from information the harness gives it.

## What is graded

Your submission is run 4 times. One run is the primary objective. The other 3 are perturbation runs against the same submitted bytes, and they are graded conjuncts rather than diagnostics: a submission that clears the primary run and misses a perturbation does not pass. A further run also executes, but it runs the original algorithm you were handed rather than your bytes: it exists to anchor the per-step cost ratio, and it neither grades nor scores anything you wrote.

The primary objective is to reach `validation/accuracy` strictly above the workload's own published validation target of **0.97**, and to reach it as early as possible. That target is readable from the vendored workload class, so nothing about the bar is hidden from you.

3 perturbation runs also execute, of kinds `held_out_variant`, `seed`, `ruleset`. You are told that they run and you are told their kinds, and you are not told their parameters. That is deliberate and it is the same design the upstream benchmark uses when it keeps its held-out variant selection private, because a submitter who knows exactly what will be perturbed can fit to it instead of generalising past it. Write an algorithm that does not need to know.

The graded axis is accumulated submission time at the qualifying evaluation, in seconds, as the runner accumulates it: your training work is charged and the harness's own evaluations are not. Evaluation fires on that same clock every 3 seconds, so the budget you are recorded at is the first evaluation row that crosses the bar rather than the instant you crossed it. Finishing sooner is worth exactly as much as the grid can see.

There is a ceiling on per-step compute for the same reason. The change in accumulated submission time over the change in global step is measured on every run and recorded whether or not it passes. A submission whose per-step cost runs more than three times the shipped algorithm's is crossing a red line rather than taking a fast route, because the axis you are graded on multiplies steps by a batch size you chose. Take better steps, not larger ones.

## The rules your submission must satisfy

These are the upstream disallowed-submission rules, compiled into deterministic checks over the bytes you submit. Each one names a syntactic pattern and rejects that pattern and nothing else. Read them as hard constraints rather than as guidance.

Your module may contain, at module level, only imports, constant assignments, and the definitions of the permitted functions. Private helpers whose names begin with an underscore are permitted.

Your submission may not identify the workload. Comparing any value against a workload registry key, keying a mapping by registry keys, or subscripting by a registry key is rejected wherever the result selects a hyperparameter or an update rule. A single setting that works across every workload is explicitly allowed by the upstream rules, and it is the conforming way to answer this.

Your submission may not fingerprint the model. Comparing a parameter shape, a parameter count, or a model-state key set against a literal is rejected. Specialising on generic properties such as layer type is allowed.

Your submission may not ship a search-space file under this ruleset, may not assign into the process environment, may not import or call a runtime compilation surface such as a C or CUDA extension builder or a kernel JIT, and may not create a thread, a process, or a device stream.

Your submission may not add a dependency, may not carry a credential, and may not modify the pinned harness tree. The harness is re-hashed after your phase and any difference is a red-line crossing rather than a scoring penalty.

Your phase runs sealed. The only endpoint you can reach is the one serving you; the public internet is not resolvable, and package indexes and code hosts are explicitly unreachable. Everything this task depends on is already in the container: the pinned harness carries the vendored upstream documentation and the workload class, and that tree is the authority on the submission contract. Read it there. Attempting to fetch anything costs you turns and returns nothing. The verifier phase is closed as well.

Only the verifier writes the reward file. Writing it yourself is a red-line crossing.

## The loop

You get multiple attempts in one episode, carrying a summary of what you tried and what it earned into the next attempt. The last attempt is the one reported, so an attempt that scores below one you already had costs you the difference. Each attempt is a full training run plus its 3 perturbation runs, so an attempt costs real time and a change worth making is worth reasoning about before you spend one.

## Where things are

Your submission is at `/submission/submission.py`. `/submission` is the only path that is graded and the only one that persists, so your algorithm belongs there and nowhere else. `/tmp` is writable scratch if you want somewhere to run trial training, and nothing written there is read, graded, or retained. The pinned harness, including the vendored upstream documentation and the workload class, is in the environment and is read-only. The dataset is mounted at `/data/mnist` and already prepared.

Whatever is at `/submission/submission.py` when your phase ends is what gets graded. Your phase ends when you say you are finished or when it is cut, and the cut is hard: it can land in the middle of what you are doing, and nothing warns you first. Keep `/submission/submission.py` holding your best runnable algorithm at all times rather than writing it once you are finished: a phase that ends while your work is still in scratch space grades the algorithm you were handed, which scores zero, and it spends one of your attempts to do it.

Training runs you perform in this container do not predict the budget you will be graded on, and the difference is structural rather than a matter of noise. Evaluations are scheduled on a wall clock, the graded budget is read from whichever evaluation row first crosses the bar, and the graded runs execute in a separate container on their own clock, sharing the device with the other graded runs beside them. The same submitted bytes therefore land on a different qualifying budget here than there, in a direction you cannot correct for. Use this container to establish that your algorithm runs and conforms, which is worth doing and cheap. Do not use it to search for hyperparameters against a measurement that does not transfer: the ruleset you are graded under expects the algorithm itself to adapt at run time, and a constant fitted to this container is fitted to the wrong run.

Spend your time in the proportion the work rewards. This container cannot tell you whether your algorithm is fast, only whether it runs and conforms, so reading the harness past the point where you can write conforming code buys you nothing measurable.

The turn ends when you say you are finished. There is no reward for occupying the clock and no penalty for handing back a submission you are satisfied with: grading happens on the submitted bytes, not on how long you took to write them. When your algorithm is written, conforms, and you have no further change you can justify from the feedback you were given, submit and end the turn rather than filling the remaining time.

Start by reading the workload class and the upstream submission contract, then read the algorithm you were given and decide what is actually costing it examples.
