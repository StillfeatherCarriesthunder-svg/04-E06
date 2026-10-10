#!/usr/bin/env python3
"""Append-only operations on evidence/ledger.jsonl.

Records are never edited or deleted. Corrections are new ANNOTATION records;
the latest annotation for a field wins in the view.

Commands:
  annotate CAPTURE_ID --field FIELD --value VALUE [--note TEXT]
  gap --source-id ID --stage N [N ...] --reason TEXT [--url URL]
  view [--csv]          fold the ledger into one row per capture
  verify                re-hash every raw and text file against the ledger

Fields for annotate:
  currency_date_confirmed  pinpoint  stages  court  decision_date  citation
  holding  context  exceptions  admission  admission_reason  supersedes
"""
import argparse
import csv
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "evidence" / "ledger.jsonl"
VIEW_CSV = ROOT / "evidence" / "ledger_view.csv"

FIELDS = ["currency_date_confirmed", "pinpoint", "stages", "court", "decision_date",
          "citation", "holding", "context", "exceptions", "admission",
          "admission_reason", "supersedes"]
ADMISSION_VALUES = {"ADMITTED", "QUALIFIED", "NOT_ADMITTED"}


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def load():
    if not LEDGER.exists():
        return []
    records = []
    with LEDGER.open(encoding="utf-8") as f:
        for n, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                sys.exit(f"ERROR: ledger line {n} is not valid JSON ({e}). Stop and repair.")
    return records


def append(record):
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def cmd_annotate(args):
    records = load()
    ids = {r["capture_id"] for r in records if r.get("record_type") == "CAPTURE"}
    if args.capture_id not in ids:
        sys.exit(f"ERROR: no CAPTURE record {args.capture_id}")
    if args.field not in FIELDS:
        sys.exit(f"ERROR: field must be one of: {', '.join(FIELDS)}")
    if args.field == "admission" and args.value not in ADMISSION_VALUES:
        sys.exit(f"ERROR: admission must be one of {sorted(ADMISSION_VALUES)}")
    n = sum(1 for r in records if r.get("record_type") == "ANNOTATION") + 1
    rec = {
        "record_type": "ANNOTATION",
        "annotation_id": f"ANN-{n:04d}",
        "capture_id": args.capture_id,
        "field": args.field,
        "value": args.value,
        "note": args.note,
        "utc": utc_now(),
    }
    append(rec)
    print(f"ANNOTATED {rec['annotation_id']}: {args.capture_id} {args.field} = {args.value}")


def cmd_gap(args):
    records = load()
    n = sum(1 for r in records if r.get("record_type") == "GAP") + 1
    rec = {
        "record_type": "GAP",
        "gap_id": f"GAP-{n:03d}",
        "source_id": args.source_id,
        "stages": sorted(set(args.stage)),
        "url": args.url,
        "reason": args.reason,
        "utc": utc_now(),
    }
    append(rec)
    print(f"GAP RECORDED {rec['gap_id']}: {args.source_id} stages {rec['stages']} - {args.reason}")


def fold(records):
    rows = {}
    for r in records:
        if r.get("record_type") == "CAPTURE":
            rows[r["capture_id"]] = {
                "capture_id": r["capture_id"],
                "source_id": r["source_id"],
                "stages": " ".join(map(str, r["stages"])),
                "kind": r["kind"],
                "final_url": r["final_url"],
                "retrieved_utc": r["retrieved_utc"],
                "method": r["method"],
                "sha256": r["sha256"],
                "raw_path": r["raw_path"],
                "text_path": r.get("text_path") or "",
                **{f: "" for f in FIELDS if f != "stages"},
            }
    for r in records:
        if r.get("record_type") == "ANNOTATION" and r["capture_id"] in rows:
            rows[r["capture_id"]][r["field"]] = r["value"]
    gaps = [r for r in records if r.get("record_type") == "GAP"]
    return list(rows.values()), gaps


def cmd_view(args):
    rows, gaps = fold(load())
    if args.csv:
        cols = list(rows[0].keys()) if rows else ["capture_id"]
        with VIEW_CSV.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
        print(f"Wrote {VIEW_CSV.relative_to(ROOT).as_posix()} ({len(rows)} rows)")
    for row in rows:
        cur = row["currency_date_confirmed"] or "UNCONFIRMED"
        adm = row["admission"] or "-"
        print(f"{row['capture_id']}  {row['source_id']:<18} st[{row['stages']}]  "
              f"currency {cur:<12} pin {row['pinpoint'] or '-':<16} adm {adm}")
    for g in gaps:
        print(f"{g['gap_id']}  {g['source_id']:<18} st[{' '.join(map(str, g['stages']))}]  GAP: {g['reason']}")
    if not rows and not gaps:
        print("Ledger is empty.")


def sha(path):
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def cmd_verify(args):
    bad = 0
    captures = [r for r in load() if r.get("record_type") == "CAPTURE"]
    for r in captures:
        for key, hkey in (("raw_path", "sha256"), ("text_path", "text_sha256")):
            if not r.get(key):
                continue
            p = ROOT / r[key]
            if not p.exists():
                print(f"MISSING   {r['capture_id']} {r[key]}")
                bad += 1
            elif sha(p) != r[hkey]:
                print(f"MISMATCH  {r['capture_id']} {r[key]}")
                bad += 1
    print(f"VERIFY: {len(captures)} captures checked, {bad} problem(s)")
    sys.exit(1 if bad else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("annotate")
    a.add_argument("capture_id")
    a.add_argument("--field", required=True)
    a.add_argument("--value", required=True)
    a.add_argument("--note", default="")
    a.set_defaults(func=cmd_annotate)

    g = sub.add_parser("gap")
    g.add_argument("--source-id", required=True)
    g.add_argument("--stage", nargs="+", type=int, required=True, choices=range(1, 7))
    g.add_argument("--reason", required=True)
    g.add_argument("--url", default=None)
    g.set_defaults(func=cmd_gap)

    v = sub.add_parser("view")
    v.add_argument("--csv", action="store_true")
    v.set_defaults(func=cmd_view)

    c = sub.add_parser("verify")
    c.set_defaults(func=cmd_verify)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
