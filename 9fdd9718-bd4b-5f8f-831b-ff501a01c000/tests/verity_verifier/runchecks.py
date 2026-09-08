"""The run checks, derived from the evaluation log alone.

All five read the parsed rows that parse.py returns, so the conjunctive pass and the continuous reward can
never disagree about whether a target was crossed. None of them calls scoring/score_submissions.py and
none consults a latched target flag.
"""

from . import parse
from .rules import Result


def evaluate(curve_or_error, unit, batch_size, label):
    """Evaluate one graded unit and return its result set plus the qualifying row.

    curve_or_error is either a parsed row list or a parse.MalformedLog instance, so a malformed log
    produces a named failure rather than an exception escaping into the reward path.
    """
    prefix = "" if label == "primary" else "%s: " % label

    if isinstance(curve_or_error, parse.MalformedLog):
        return (
            [
                Result("C-LOG-WELL-FORMED", False, prefix + str(curve_or_error)),
                Result("C-TARGET-REACHED", False, prefix + "no curve to read"),
                Result("C-BUDGET-RESPECTED", False, prefix + "no curve to read"),
                Result("C-NO-LATCH-CARRYOVER", False, prefix + "no curve to read"),
            ],
            None,
        )

    rows = curve_or_error
    results = [Result("C-LOG-WELL-FORMED", True, prefix + "the log parses, carries the declared metric column, and has a non-decreasing step column")]

    threshold = unit["threshold"]
    comparator = unit["comparator"]
    row = parse.qualifying_row(rows, threshold, comparator)

    if row is None:
        results.append(Result("C-TARGET-REACHED", False, prefix + "no evaluation row crosses the threshold in the declared direction"))
        results.append(Result("C-BUDGET-RESPECTED", False, prefix + "no qualifying row, so no budget position exists"))
        results.append(Result("C-NO-LATCH-CARRYOVER", True, prefix + "the verdict is derived from the metric column and no row crosses"))
        return results, None

    results.append(
        Result(
            "C-TARGET-REACHED",
            True,
            prefix + "row %d crosses %s %s" % (row["index"], comparator, threshold),
        )
    )

    kind = unit["budget"]["kind"]
    ceiling = float(unit["budget"]["value"])
    position = parse.budget_position(row, kind, batch_size)
    if position is None:
        results.append(Result("C-BUDGET-RESPECTED", False, prefix + "the qualifying row carries no value on the %s axis" % kind))
    elif position > ceiling:
        results.append(
            Result(
                "C-BUDGET-RESPECTED",
                False,
                prefix + "the qualifying row sits at %s on the %s axis, above the declared ceiling of %s" % (position, kind, ceiling),
            )
        )
    else:
        results.append(
            Result(
                "C-BUDGET-RESPECTED",
                True,
                prefix + "the qualifying row sits at %s on the %s axis, at or below the ceiling of %s" % (position, kind, ceiling),
            )
        )

    # C-NO-LATCH-CARRYOVER: the qualifying row is derived from the metric column directly. If the log
    # carries a latched flag column, it must not disagree with the metric-derived verdict on the rows
    # before the qualifying one. A resumed run that inherited a latch would show the flag set earlier.
    latch_columns = [name for name in row["raw"].keys() if "target" in name.lower() and "reached" in name.lower()]
    offending = []
    for candidate in rows:
        if candidate["index"] >= row["index"]:
            break
        for column in latch_columns:
            raw = (candidate["raw"].get(column) or "").strip().lower()
            if raw in ("true", "1", "1.0"):
                offending.append("row %d sets %s while its metric does not cross" % (candidate["index"], column))
    if offending:
        results.append(
            Result(
                "C-NO-LATCH-CARRYOVER",
                False,
                prefix + "a latched target flag is set on a row whose metric does not cross, so the run inherited a target it did not reach",
                offending,
            )
        )
    else:
        results.append(
            Result(
                "C-NO-LATCH-CARRYOVER",
                True,
                prefix + "the qualifying row is derived from the metric column and no earlier row carries a set latch",
            )
        )

    return results, row


def perturbation_result(reached, declared):
    if declared == 0:
        return Result("C-PERTURBATION-REACHED", False, "a task with no perturbation grades a single run")
    if reached == declared:
        return Result("C-PERTURBATION-REACHED", True, "every declared perturbation reached its own threshold inside its own budget (%d of %d)" % (reached, declared))
    return Result(
        "C-PERTURBATION-REACHED",
        False,
        "%d of %d declared perturbations reached their own threshold inside their own budget" % (reached, declared),
    )
