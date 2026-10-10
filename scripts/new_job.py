#!/usr/bin/env python3
"""Create a new job folder in the hub.

  python3 scripts/new_job.py JOB_ID              create the job folder
  python3 scripts/new_job.py JOB_ID --register   list new files in sources/

Creates jobs/JOB_ID/ with empty evidence, state, draft and inbox folders, a
sources/ folder for the job's own governing files, a copy of the hub's default
domain list, and a gate/required_sources.json that binds the shared kernel,
Worker instructions and B-Series index by their current hashes.

The operator adds the job's topic file and operator instruction to
jobs/JOB_ID/sources/. --register then lists every top-level file there that the
gate file does not yet list, with sha256 null. Bind them with
verify_gate.py --job JOB_ID --bind. Creating refuses if the folder exists.
"""
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent
SHARED = [
    ("SRC-KERNEL", "sources/governing/UAEP_WORKER_KERNEL.md", "governing Worker specification, UAEP-PORTABLE-3.0.0"),
    ("SRC-WORKER-INSTR", "sources/governing/WORKER_INSTRUCTIONS.md", "Worker instructions, UAEP-PORTABLE-3.0.0"),
    ("SRC-INDEX", "sources/governing/00-B_SERIES_INDEX.md", "B-Series category taxonomy"),
]


def register(job):
    root = HUB / "jobs" / job
    gate_path = root / "gate" / "required_sources.json"
    if not gate_path.is_file():
        sys.exit(f"ERROR: jobs/{job} has no gate/required_sources.json")
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    listed = {s["path"] for s in gate["sources"]}
    added = []
    for f in sorted((root / "sources").iterdir()):
        rel = f"sources/{f.name}"
        if f.is_file() and rel not in listed:
            sid = "SRC-" + re.sub(r"[^A-Za-z0-9]+", "-", f.stem).strip("-").upper()[:40]
            gate["sources"].append({"id": sid, "path": rel, "role": "job governing file (set role)", "sha256": None})
            added.append(rel)
    gate_path.write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")
    print(f"REGISTERED {len(added)} file(s): {', '.join(added) or 'none'}")
    if added:
        print(f"  next: python3 scripts/verify_gate.py --job {job} --bind")


def main():
    if len(sys.argv) == 3 and sys.argv[2] == "--register":
        return register(sys.argv[1])
    if len(sys.argv) != 2 or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", sys.argv[1]):
        sys.exit("Usage: python3 scripts/new_job.py JOB_ID   (letters, digits, . _ -)")
    job = sys.argv[1]
    root = HUB / "jobs" / job
    if root.exists():
        sys.exit(f"REFUSED: jobs/{job} already exists")

    sources = []
    for sid, rel, role in SHARED:
        path = HUB / rel
        if not path.is_file():
            sys.exit(f"ERROR: shared governing file missing: {rel}")
        sources.append({"id": sid, "path": f"../../{rel}", "role": role,
                        "sha256": "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()})

    for sub in ("evidence/raw", "evidence/text", "state", "draft", "inbox", "sources", "gate"):
        (root / sub).mkdir(parents=True)
    for sub in ("evidence/raw", "evidence/text", "state", "draft", "inbox"):
        (root / sub / ".gitkeep").touch()
    shutil.copyfile(HUB / "templates" / "source_domains.json", root / "gate" / "source_domains.json")
    gate = {"job_id": None,
            "note": "Shared files are bound by current hash. Add this job's topic file and operator "
                    "instruction with sha256 null, then run verify_gate.py --job " + job + " --bind.",
            "sources": sources}
    (root / "gate" / "required_sources.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")
    print(f"CREATED jobs/{job}/")
    print("  next: add the topic file and operator instruction to sources/, list them in gate/required_sources.json")


if __name__ == "__main__":
    main()
