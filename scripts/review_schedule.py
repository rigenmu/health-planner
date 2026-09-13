#!/usr/bin/env python3
"""Read-only review window calculation. No records, scheduling, or notifications."""

import argparse
import calendar
import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError("Timestamps must include a timezone offset")
    return result


def pending_reviews(state, as_of):
    if state.get("schema_version") != 1:
        raise ValueError("Unsupported review state schema")
    if as_of.tzinfo is None or as_of.utcoffset() is None:
        raise ValueError("as_of must be timezone-aware")
    zone = ZoneInfo(state["timezone"])
    today = as_of.astimezone(zone).date()
    anchor = date.fromisoformat(state["anchor_date"])
    closed = state.get("closed_through")
    closed = date.fromisoformat(closed) if closed else None
    if closed and (closed > today or closed < anchor):
        raise ValueError("closed_through must be between anchor_date and today")
    # Today's window can be delivered only after explicit daily closure.
    cutoff = today if closed == today else today - timedelta(days=1)
    delivered = set()
    generated = {}
    for report in state.get("reviews", []):
        ids = report.get("period_ids", [])
        if not isinstance(ids, list) or not all(isinstance(i, str) for i in ids):
            raise ValueError("period_ids must be a list of strings")
        if report.get("generated_at") and report.get("report_path"):
            if timestamp(report["generated_at"]) > as_of:
                raise ValueError("generated_at is in the future")
            for period_id in ids:
                generated[period_id] = report["report_path"]
        if report.get("delivered_at") and report.get("conversation_ref"):
            if timestamp(report["delivered_at"]) > as_of:
                raise ValueError("delivered_at is in the future")
            delivered.update(ids)

    windows = []

    def add(kind, start, end, partial=False):
        period_id = f"{kind}:{start.isoformat()}:{end.isoformat()}"
        if end <= cutoff and period_id not in delivered:
            windows.append({
                "period_id": period_id,
                "kind": kind,
                "start": start.isoformat(),
                "end": end.isoformat(),
                "calendar_days": (end - start).days + 1,
                "partial_month": partial,
                "existing_report": generated.get(period_id),
            })

    for width in (7, 14):
        start = anchor
        while start + timedelta(days=width - 1) <= cutoff:
            end = start + timedelta(days=width - 1)
            add(f"{width}d", start, end)
            start = end + timedelta(days=1)
    month = anchor.replace(day=1)
    while month <= cutoff:
        end = month.replace(day=calendar.monthrange(month.year, month.month)[1])
        start = max(anchor, month)
        add("month", start, end, start != month)
        month = end + timedelta(days=1)

    priority = {"month": 0, "14d": 1, "7d": 2}
    windows.sort(key=lambda w: (w["end"], priority[w["kind"]]))
    batches = []
    for window in windows:
        if not batches or batches[-1]["end"] != window["end"]:
            batches.append({"end": window["end"], "primary": window["kind"], "windows": []})
        batches[-1]["windows"].append(window)
    return {"as_of_local_date": today.isoformat(), "eligible_through": cutoff.isoformat(),
            "delivery_batches": batches}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--as-of", help="Optional ISO timestamp including timezone offset")
    args = parser.parse_args()
    try:
        state = json.loads(args.state.read_text(encoding="utf-8"))
        now = timestamp(args.as_of) if args.as_of else datetime.now(timezone.utc)
        print(json.dumps(pending_reviews(state, now), ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError, ZoneInfoNotFoundError) as error:
        parser.exit(2, f"Cannot calculate review windows: {error}\n")


if __name__ == "__main__":
    main()
