#!/usr/bin/env python3
"""Check the identity of the governing sources listed in gate/required_sources.json.

This proves identity only: the file is present and its bytes match the bound hash.
It does not prove completeness. The Worker still reads each source and declares
COMPLETE | PARTIAL | MISSING | INACCESSIBLE | VERSION_UNCERTAIN.

Usage:
  python scripts/verify_gate.py          check and print the table
  python scripts/verify_gate.py --bind   also write computed hashes into empty
                                         (null) slots; never overwrites a bound hash
Exit code 1 if any source is missing or mismatched, or if any slot is still unbound.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GATE = ROOT / "gate" / "required_sources.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bind", action="store_true")
    args = ap.parse_args()

    spec = json.loads(GATE.read_text(encoding="utf-8"))
    fail = unbound = 0
    changed = False
    print(f"{'ID':<18} {'STATUS':<22} PATH")
    for src in spec["sources"]:
        path = ROOT / src["path"]
        if not path.exists():
            status = "MISSING"
            fail += 1
        else:
            digest = "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
            expected = src.get("sha256")
            if expected is None:
                if args.bind:
                    src["sha256"] = digest
                    changed = True
                    status = "BOUND_NOW"
                else:
                    status = "PRESENT_UNBOUND"
                    unbound += 1
                print(f"{'':<18} computed {digest}")
            elif digest == expected:
                status = "IDENTITY_OK"
            else:
                status = "VERSION_UNCERTAIN"
                fail += 1
                print(f"{'':<18} expected {expected}\n{'':<18} actual   {digest}")
        print(f"{src['id']:<18} {status:<22} {src['path']}")

    if changed:
        GATE.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Bound hashes written to {GATE.relative_to(ROOT).as_posix()}")

    if fail:
        print(f"IDENTITY CHECK: FAIL ({fail} source(s)). Source gate cannot pass.")
    elif unbound:
        print(f"IDENTITY CHECK: INCOMPLETE ({unbound} unbound). Run with --bind at initial entry.")
    else:
        print("IDENTITY CHECK: PASS. Completeness still requires the Worker's read check.")
    sys.exit(1 if (fail or unbound) else 0)


if __name__ == "__main__":
    main()
