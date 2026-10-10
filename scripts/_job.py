"""Select the job folder for the hub scripts.

Every hub script takes --job ID (or --job=ID). The job folder is jobs/ID/.
The flag is removed from sys.argv before the script parses its own arguments.
"""
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent
JOBS = HUB / "jobs"


def _existing_jobs():
    if not JOBS.is_dir():
        return []
    return sorted(p.name for p in JOBS.iterdir() if p.is_dir())


def job_root():
    argv = sys.argv
    job = None
    for i, arg in enumerate(argv[1:], 1):
        if arg == "--job":
            if i + 1 >= len(argv):
                sys.exit("ERROR: --job needs a job ID")
            job = argv[i + 1]
            del argv[i:i + 2]
            break
        if arg.startswith("--job="):
            job = arg.split("=", 1)[1]
            del argv[i]
            break
    if not job:
        sys.exit(f"ERROR: --job ID is required. Jobs: {', '.join(_existing_jobs()) or 'none'}")
    root = (JOBS / job).resolve()
    if root.parent != JOBS.resolve() or not root.is_dir():
        sys.exit(f"ERROR: no job folder jobs/{job}. Jobs: {', '.join(_existing_jobs()) or 'none'}")
    return root
