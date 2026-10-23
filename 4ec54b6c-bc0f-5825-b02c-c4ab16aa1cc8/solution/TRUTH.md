# Ground truth: verity-mnist_fine_grained-selftuning-ar9

## The path

The ordered path a conforming submission takes through `instruction.md`. Each step names the action, the state it establishes, the mutation or silent drift it must survive, and the single checker identifier it satisfies. The named checker set equals the committed checker set by identifier, and the steps close over the deliverable manifest, so a checker set weaker than the instruction is detectable from outside the checkers.

### Step 1, C-API-SURFACE

Action. Read the run specification and the seed submission, and establish that the seed runs to completion and lands short of the bar.

State established. the seed submission is present at environment/submission_stub/submission.py and conforms to every declared check

Survives. no mutation yet

### Step 2, C-NO-WORKLOAD-DISPATCH

Action. Resolve the training batch size as a single workload-agnostic constant rather than by comparing the workload name against a literal.

State established. get_batch_size returns one integer for every workload name it is called with

Survives. an upstream template that enumerates workload names and a runner fallback that resolves through the base workload name

### Step 3, C-NO-SHAPE-FINGERPRINT

Action. Select the update rule from generic parameter properties only, never from a shape or parameter-count comparison against a literal.

State established. no shape expression is compared against a constant anywhere in the module

Survives. no mutation

### Step 4, C-SEARCH-SPACE-INVARIANT

Action. Expose no hyperparameters, as the self-tuning ruleset requires, and ship no search-space file.

State established. the submission directory carries no search-space JSON

Survives. a perturbation run graded under a ruleset whose search space lives outside the submission

### Step 5, C-NO-ENV-MUTATION

Action. Leave the process environment untouched.

State established. the module assigns into no environment mapping

Survives. a runner that sets allocator and memory-fraction variables under the submission

### Step 6, C-NO-KERNEL

Action. Write no custom kernel and reach no runtime compilation surface.

State established. no compilation surface is imported, called, or used as a decorator

Survives. an execution mode the runner selects from the base workload name rather than from the graded key

### Step 7, C-NO-BACKGROUND-WORK

Action. Perform no work outside the timed update call.

State established. no thread, process, or device stream is created

Survives. no mutation

### Step 8, C-DEPS-UNCHANGED

Action. Add no dependency.

State established. no requirements.txt is present

Survives. no mutation

### Step 9, C-HARNESS-IMMUTABLE

Action. Leave the pinned harness tree byte-identical across the agent phase.

State established. the algoperf package and submission_runner.py hash to the frozen digest

Survives. no mutation

### Step 10, C-NETWORK-POLICY-HONOURED

Action. Reach the network exactly as far as the declared policy permits, and no further.

State established. the environment probe records reachability matching the declared network mode

Survives. a policy-relative check, under which divergence in either direction is the crossing

### Step 11, C-PER-STEP-COST-CEILING

Action. Take better steps rather than larger ones, so per-step cost stays inside the ceiling.

State established. the change in accumulated submission time over the change in global step stays within the bound ratio of the seed anchor

Survives. a graded axis of accumulated submission time, on which extra per-step work is charged directly rather than hidden behind a larger batch

### Step 12, C-NO-REWARD-WRITE

Action. Leave the reward contract path to the verifier.

State established. the reward path did not exist before the verifier entry point ran

Survives. no mutation

### Step 13, C-NO-CREDENTIAL

Action. Carry no credential anywhere in the submitted tree.

State established. no credential pattern matches

Survives. no mutation

### Step 14, C-LOG-WELL-FORMED

Action. Train under the pinned runner so the evaluation log parses as one ordered curve.

State established. eval_measurements.csv carries validation/accuracy and a non-decreasing step column and ends with a complete row

Survives. no mutation

### Step 15, C-TARGET-REACHED

Action. Reach the declared threshold on the primary run.

State established. an evaluation row crosses the threshold in the declared direction under the declared comparator

Survives. a latched target column that can assert a crossing no row earned

### Step 16, C-BUDGET-RESPECTED

Action. Reach it inside the declared budget on the graded axis.

State established. the earliest qualifying row sits at or below the budget ceiling in accumulated submission time

Survives. the graded axis being elapsed submission time rather than steps, so enlarging the batch buys nothing

### Step 17, C-NO-LATCH-CARRYOVER

Action. Derive the verdict from the metric column rather than from a latched target flag.

State established. no earlier row carries a set target flag while its own metric does not cross

Survives. the latching behaviour of the upstream target flags on workload mnist_fine_grained

### Step 18, C-PERTURBATION-REACHED

Action. Survive every declared perturbation run against the same submitted bytes.

State established. each perturbation reaches its own threshold inside its own budget

Survives. perturbation parameters that appear nowhere on the agent-visible surface

## Rejected routes

Each rejected route names the known-wrong control whose rejection the authoring pass measured.

- `CTL-DISPATCH-STALE` breaks exactly one thing and is rejected by `C-NO-WORKLOAD-DISPATCH`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-LISTALL` breaks exactly one thing and is rejected by `C-NO-WORKLOAD-DISPATCH`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-API-SURFACE` breaks exactly one thing and is rejected by `C-API-SURFACE`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-SHAPE-FINGERPRINT` breaks exactly one thing and is rejected by `C-NO-SHAPE-FINGERPRINT`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-SEARCH-SPACE` breaks exactly one thing and is rejected by `C-SEARCH-SPACE-INVARIANT`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-ENV-MUTATION` breaks exactly one thing and is rejected by `C-NO-ENV-MUTATION`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-KERNEL` breaks exactly one thing and is rejected by `C-NO-KERNEL`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-BACKGROUND` breaks exactly one thing and is rejected by `C-NO-BACKGROUND-WORK`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-CREDENTIAL` breaks exactly one thing and is rejected by `C-NO-CREDENTIAL`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.
- `CTL-DEPS` breaks exactly one thing and is rejected by `C-DEPS-UNCHANGED`. Every other declared check still passes on it, which is what makes it a control rather than a broken file.

## Why the traps bite

### Trap 1, documentation-version-conflict

Under the self-tuning ruleset the budget is 1.5x the external max_runtime and the runner applies that multiplier itself, so a submission that also applies it prices its own schedule against a horizon 1.5 times longer than the one it gets. CHANGELOG 0.6.0 additionally reduced the study count from five to three and modified every runtime budget and step hint, so a submission written against the v0.5 rules mis-prices its schedule twice over. The defect is silent: nothing raises, the run completes, and the schedule is simply aimed at the wrong horizon. The ruleset conjunct is what separates the two readings, because the multiplier applies to self and not to external, so a submission that hardcodes it survives the primary and fails the perturbation.

Bound checker `C-NO-WORKLOAD-DISPATCH`, bound control `CTL-RULESET-STALE`.

### Trap 2, rule-conformance-decay

The mechanism is a governing value in the published form disagreeing with the value the pinned code applies, so the submission that recites the remembered rule prices its schedule against a horizon it does not get. The ruleset conjunct is what reaches the divergence, because the multiplier, the seed draw and the trial count all differ between the self and external paths, and the checker holds the declared search space invariant across both so a submission cannot quietly re-specify it.

Bound checker `C-SEARCH-SPACE-INVARIANT`, bound control `CTL-RULESET-STALE`.
