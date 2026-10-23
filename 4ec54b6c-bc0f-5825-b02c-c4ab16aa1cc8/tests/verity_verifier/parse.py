"""The only reader of eval_measurements.csv.

Both the verifier and the authoring feasibility pass call this module, so the two cannot disagree about
whether a target was crossed. It never calls scoring/score_submissions.py, which does not execute under
the harness's own pinned NumPy floor, and it never trusts the runner exit value, which returns the lowest
trial index rather than the fastest timing.
"""

import csv
import math

REQUIRED_COLUMNS = ("global_step", "accumulated_submission_time", "score")


class MalformedLog(ValueError):
    """The log cannot be read as a curve. Distinct from a curve that never reached a target."""


def _to_float(raw):
    if raw is None:
        return None
    text = raw.strip()
    if text == "":
        return None
    try:
        value = float(text)
    except ValueError:
        return None
    return value


def read_curve(path, metric_column):
    """Parse a log into an ordered list of rows.

    Raises MalformedLog on a truncated final row, a missing declared metric column, or a step column
    that decreases. A NaN metric value is not malformed: it parses, and the threshold comparison then
    reads it as not reached, which is the honest treatment of an evaluation that produced no number.
    """
    with open(path, "r", newline="", encoding="utf-8") as handle:
        text = handle.read()

    if text and not text.endswith("\n"):
        raise MalformedLog("final row is truncated: the file does not end with a newline")

    reader = csv.DictReader(text.splitlines())
    fieldnames = reader.fieldnames or []
    if metric_column not in fieldnames:
        raise MalformedLog("declared metric column %r is absent from the log" % metric_column)
    for column in REQUIRED_COLUMNS:
        if column not in fieldnames:
            raise MalformedLog("required column %r is absent from the log" % column)

    rows = []
    width = len(fieldnames)
    for index, record in enumerate(reader):
        if None in record or len(record) != width:
            raise MalformedLog("row %d has a different field count than the header" % index)
        if any(record[name] is None for name in fieldnames):
            raise MalformedLog("row %d is truncated" % index)
        step = _to_float(record["global_step"])
        if step is None:
            raise MalformedLog("row %d has an unparseable global_step" % index)
        rows.append(
            {
                "index": index,
                "global_step": step,
                "accumulated_submission_time": _to_float(record["accumulated_submission_time"]),
                "score": _to_float(record["score"]),
                "metric": _to_float(record[metric_column]),
                "raw": record,
            }
        )

    if not rows:
        raise MalformedLog("the log carries a header and no evaluation row")

    previous = None
    for row in rows:
        if previous is not None and row["global_step"] < previous:
            raise MalformedLog("global_step decreases at row %d, so the log is not a single ordered curve" % row["index"])
        previous = row["global_step"]

    return rows


def crossed(value, threshold, comparator):
    """Apply the declared comparator. A NaN never crosses, under any comparator."""
    if value is None or math.isnan(value):
        return False
    if comparator == "strictly_greater":
        return value > threshold
    if comparator == "strictly_less":
        return value < threshold
    if comparator == "at_least":
        return value >= threshold
    if comparator == "at_most":
        return value <= threshold
    raise ValueError("unknown comparator %r" % comparator)


def qualifying_row(rows, threshold, comparator):
    """The earliest row whose metric crosses the threshold, derived from the metric column directly.

    A latched target flag is never consulted, so a resumed run cannot inherit a target it did not reach.
    """
    for row in rows:
        if crossed(row["metric"], threshold, comparator):
            return row
    return None


def budget_position(row, budget_kind, batch_size):
    """The position of a row on the declared budget axis."""
    if budget_kind == "wall_clock_sec":
        return row["accumulated_submission_time"]
    if budget_kind == "global_steps":
        return row["global_step"]
    if budget_kind == "eval_index":
        return float(row["index"])
    if budget_kind == "train_examples":
        if batch_size is None:
            raise ValueError("the train_examples axis needs the resolved batch size")
        return row["global_step"] * float(batch_size)
    raise ValueError("unknown budget kind %r" % budget_kind)


def best_metric(rows, direction):
    values = [r["metric"] for r in rows if r["metric"] is not None and not math.isnan(r["metric"])]
    if not values:
        return None
    return max(values) if direction == "max" else min(values)
