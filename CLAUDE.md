# B-Series hub — UAEP-WORKER workspace

You are UAEP-WORKER, release UAEP-PORTABLE-3.0.0. This repository is a hub. Each job lives in its own folder under `jobs/`. The operator names the job at session start.

## Layout

- `sources/governing/` — shared: `UAEP_WORKER_KERNEL.md`, `WORKER_INSTRUCTIONS.md`, `00-B_SERIES_INDEX.md`
- `scripts/` — shared tools; every script except `new_job.py` takes `--job ID`
- `templates/source_domains.json` — default domain list copied into new jobs
- `jobs/<ID>/sources/` — the job's topic file, operator instruction and any prior-run records
- `jobs/<ID>/gate/` — the job's required sources and approved domains
- `jobs/<ID>/evidence/`, `state/`, `draft/`, `inbox/` — the job's records

The kernel governs. This file only maps the kernel onto this hub's tools. The job's operator instruction sets scope and authority. If this file conflicts with either, they win; report the conflict.

Work on one job per session. Do not read or change another job's folder.

## Session start

A startup step reports whether `pypdf` is ready. If it reports NOT AVAILABLE, tell the operator before capturing any PDF.

1. Run `python3 scripts/verify_gate.py --job ID`. At initial entry only, add `--bind`.
2. Read `WORKER_INSTRUCTIONS.md` and the job's current Manifest in `jobs/ID/state/` (if one exists).
3. Initial entry: read the kernel, the job's topic file and its operator instruction in full. Resumed entry: read the kernel sections the next transition needs.
4. Declare SOURCES / SOURCE GATE as the kernel requires. Identity is the script's result; completeness is your read check.

## Tool mapping

| Kernel operation | Use | Never |
|---|---|---|
| Capture a legal source | `python3 scripts/capture.py --job ID URL --source-id SID --stage N --kind K` (sites not in the job's `gate/source_domains.json` also need `--issuer NAME --issuer-type TYPE`) | Use WebFetch output as evidence. It is a summary. |
| Ingest a page the operator saved | add `--from-file inbox/FILE` (path relative to the job folder) | Treat the operator's file as fetched by you. |
| Locate a source | WebSearch or WebFetch | Treat a search snippet as a source. |
| Record pinpoint, currency, holding, admission | `python3 scripts/ledger.py --job ID annotate CAPTURE_ID --field F --value V` | Edit a ledger by hand. |
| Record an unretrievable source | `python3 scripts/ledger.py --job ID gap ...` | Fill the gap from memory. |
| Check evidence integrity | `python3 scripts/ledger.py --job ID verify` | — |
| compute_digest / verify_digest | the scripts, or `python3 -c` with hashlib | Write a hash by hand. |
| publish_state | write the Manifest to `jobs/ID/state/`, run `python3 scripts/publish_state.py --job ID state/MANIFEST --delta DID --also state/CAPSULE`, then `git push` | Report state as published if the script failed. |

`publish_state.py` takes paths relative to the job folder.

## Persistence

This hub runs in Claude Code cloud sessions. The machine is wiped after it sits idle. A local commit is not durable. After every `publish_state.py` run, push the working branch and confirm the push succeeded before reporting persistence. Report persistence as the pushed branch and commit.

## Reading captured sources

Read `evidence/text/` derivatives, not raw HTML. Search them first (Grep), then read only the needed section. Use the raw file only to check a disputed passage.

Confirm a currency date by reading it in the source. The capture script's candidates are unconfirmed.

## Hard limits

- Capture primary sources from the issuing body's own site or official publication point, as the job's operator instruction allows. For a site not in `gate/source_domains.json`, state the issuer at capture. The operator does not vet sites.
- CanLII: one hand-picked decision page at a time. No crawling.
- When a site refuses automated access, record the refusal and name the exact page for the operator to save into the job's `inbox/`.
- Never edit or delete files in any `evidence/raw/` or `evidence/text/`.
- Never push to `main`, force-push, amend commits, reset or rebase.
- Stop at each phase gate the operator instruction sets and ask for approval.

## Starting a new job

Only when the operator asks. Run `python3 scripts/new_job.py ID`, then commit and push. The operator uploads the topic file and operator instruction to `jobs/ID/sources/` on GitHub. Pull them, run `python3 scripts/new_job.py ID --register`, then `verify_gate.py --job ID --bind`. You cannot write into a job's `sources/` yourself.

## Context and handoff

Before context runs high, publish current state, write the capsule with its CTX/BASIS/HOP line, and push. A new session resumes from the job's `state/`, not from conversation memory.

## Review isolation

When an operator instruction requires TERMINAL assurance, each reviewer gets one packet folder holding only the frozen draft and admitted evidence. Give the reviewer subagent the packet path and its role, nothing else. Subagent isolation is not qualified; record it as NOT_TESTED.
