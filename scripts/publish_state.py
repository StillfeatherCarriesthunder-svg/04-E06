#!/usr/bin/env python3
"""Publish one Master Manifest revision as a verified git commit.

Checks lineage against state/published.jsonl, commits the Manifest (plus any
--also files, such as the State Capsule), then reads the committed blob back and
confirms its hash. Prints the commit and hash as persistence evidence.

Persistence scope is the local git repository only. A local commit is not remote
durability, and this script never pushes.

Usage:
  python scripts/publish_state.py state/C03-D05_Master_Manifest_v2.json \
      --delta C03-D05-T1-001 --also state/C03-D05_State_Capsule_v2.md
"""
import argparse
import datetime
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _job import job_root  # noqa: E402

ROOT = job_root()  # jobs/<ID>/, from --job
PUBLISHED = ROOT / "state" / "published.jsonl"


def git(*args, binary=False):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        sys.exit(f"PUBLISH FAILED at 'git {' '.join(args)}': {r.stderr.decode(errors='replace').strip()}\n"
                 f"State is NOT published.")
    return r.stdout if binary else r.stdout.decode().strip()


def last_published():
    if not PUBLISHED.exists():
        return None
    lines = [l for l in PUBLISHED.read_text(encoding="utf-8").splitlines() if l.strip()]
    return json.loads(lines[-1]) if lines else None


def rel(p):
    path = (ROOT / p).resolve() if not Path(p).is_absolute() else Path(p).resolve()
    try:
        return path, path.relative_to(ROOT).as_posix()
    except ValueError:
        sys.exit(f"ERROR: {p} is outside the job workspace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--delta", required=True, help="Delta ID for this transition")
    ap.add_argument("--also", nargs="*", default=[], help="Other files to commit with it")
    args = ap.parse_args()

    mpath, mrel = rel(args.manifest)
    if not mpath.exists():
        sys.exit(f"ERROR: {mrel} not found")
    try:
        manifest = json.loads(mpath.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: {mrel} is not valid JSON ({e}). State is NOT published.")

    for key in ("job_id", "state_version", "parent_state_version", "state"):
        if key not in manifest:
            sys.exit(f"ERROR: Manifest lacks '{key}'. State is NOT published.")

    prev = last_published()
    version, parent = manifest["state_version"], manifest["parent_state_version"]
    if prev is None:
        if parent is not None or version != 1:
            sys.exit("ERROR: first publication must have state_version 1 and parent_state_version null.")
    else:
        if parent != prev["state_version"]:
            sys.exit(f"ERROR: parent_state_version {parent} does not match last published "
                     f"version {prev['state_version']}. Lineage broken; State is NOT published.")
        if version != parent + 1:
            sys.exit(f"ERROR: state_version must be {parent + 1}. State is NOT published.")
        if manifest["job_id"] != prev["job_id"]:
            sys.exit("ERROR: job_id differs from last published state. State is NOT published.")

    data = mpath.read_bytes()
    digest = "sha256:" + hashlib.sha256(data).hexdigest()
    entry = {
        "job_id": manifest["job_id"],
        "state_version": version,
        "parent_state_version": parent,
        "state": manifest["state"],
        "delta": args.delta,
        "manifest_path": mrel,
        "manifest_sha256": digest,
        "published_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    PUBLISHED.parent.mkdir(parents=True, exist_ok=True)
    original = PUBLISHED.read_bytes() if PUBLISHED.exists() else None
    with PUBLISHED.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    paths = [mrel, PUBLISHED.relative_to(ROOT).as_posix()] + [rel(p)[1] for p in args.also]
    try:
        git("add", "--", *paths)
        git("commit", "-m", f"STATE V{version}: {args.delta}", "--", *paths)
    except SystemExit:
        if original is None:
            PUBLISHED.unlink(missing_ok=True)
        else:
            PUBLISHED.write_bytes(original)
        raise

    commit = git("rev-parse", "HEAD")
    blob = git("show", f"HEAD:./{mrel}", binary=True)
    committed = "sha256:" + hashlib.sha256(blob).hexdigest()
    if committed != digest:
        sys.exit(f"PUBLISH FAILED: committed bytes hash {committed} differs from {digest}.")

    print(f"PUBLISHED V{version} (parent {parent if parent is not None else 'null'}) delta {args.delta}")
    print(f"  manifest  {mrel}")
    print(f"  sha256    {digest}")
    print(f"  commit    {commit}")
    print("  persistence: local git commit verified by read-back; not remote-durable")


if __name__ == "__main__":
    main()
