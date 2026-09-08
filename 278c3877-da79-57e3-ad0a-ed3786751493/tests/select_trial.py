#!/usr/bin/env python3
"""Choose which trial's evaluation log represents an external-tuning unit.

External tuning runs `num_tuning_trials` trials and writes `trial_1/` .. `trial_N/`, each with its
own `eval_measurements.csv`, and AlgoPerf scores the unit on the best of them. Lifting whichever the
filesystem yields first grades an arbitrary trial, which understates the unit and reads downstream as
solver variance rather than as a selection artefact.

Prints the chosen path, or nothing when there is no curve to choose from. Never raises: an unreadable
trial is skipped rather than allowed to fail the graded unit, and an empty result lets the caller fall
back to its own search.
"""

import csv
import glob
import json
import os
import sys


def _unit(spec, unit_name):
    for entry in spec.get("perturbations", []):
        if unit_name == "perturbation_%s" % entry["id"]:
            return entry
    return spec["objective"]


def _reading(path, column, threshold, direction):
    crossed = None
    best = None
    try:
        with open(path, "r", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                try:
                    value = float(row[column])
                    position = float(row["accumulated_submission_time"])
                except (KeyError, TypeError, ValueError):
                    continue
                if best is None or (value > best if direction == "max" else value < best):
                    best = value
                reached = value >= threshold if direction == "max" else value <= threshold
                if reached and crossed is None:
                    crossed = position
    except OSError:
        return None, None
    return crossed, best


def main(argv):
    out_dir, spec_path, unit_name = argv[1], argv[2], argv[3]
    paths = sorted(glob.glob(os.path.join(out_dir, "**", "eval_measurements.csv"), recursive=True))
    paths = [p for p in paths if os.path.dirname(p) != os.path.abspath(out_dir)]
    if not paths:
        return 0
    if len(paths) == 1:
        print(paths[0])
        return 0

    with open(spec_path, "r", encoding="utf-8") as handle:
        unit = _unit(json.load(handle), unit_name)
    column = unit["metric"]
    threshold = unit["threshold"]
    direction = unit["direction"]

    scored = [(path,) + _reading(path, column, threshold, direction) for path in paths]

    reached = [row for row in scored if row[1] is not None]
    if reached:
        print(min(reached, key=lambda row: (row[1], row[0]))[0])
        return 0

    measured = [row for row in scored if row[2] is not None]
    if measured:
        sign = -1.0 if direction == "max" else 1.0
        print(min(measured, key=lambda row: (sign * row[2], row[0]))[0])
        return 0

    print(paths[0])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
