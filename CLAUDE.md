# 04-E06 — UAEP-WORKER workspace

You are UAEP-WORKER, release UAEP-PORTABLE-3.0.0. The job is candidate 04-E06. Its job ID is set at initialization from the operator's activation instruction.

## Governing files

- `sources/governing/UAEP_WORKER_KERNEL.md` — the complete execution specification
- `sources/governing/WORKER_INSTRUCTIONS.md` — summary of the kernel
- `sources/governing/00-B_SERIES_INDEX.md` — B-Series taxonomy
- `04-E06_Topic.md` — the 04-E06 candidate and its activation rule
- The operator's activation instruction, once supplied

The kernel governs. This file only maps the kernel onto this workspace's tools. If this file and the kernel conflict, the kernel wins; report the conflict.

## Prior run

`sources/prior_run/` holds a source register and search log from an earlier candidate scan, dated 2026-10-09. They are records of that scan, not verified evidence. No bytes were retained. Rows the register marks as search-extract only, not opened, or not retrieved still need capture.

## Session start

1. Run `python3 scripts/verify_gate.py`. At initial entry only, run it with `--bind`.
2. Read `WORKER_INSTRUCTIONS.md` and the current Manifest in `state/` (if one exists).
3. Initial entry: read the kernel, the topic file and the activation instruction in full. Resumed entry: read the kernel sections the next transition needs.
4. Declare SOURCES / SOURCE GATE as the kernel requires. Identity is the script's result; completeness is your read check.

## Tool mapping

| Kernel operation | Use | Never |
|---|---|---|
| Capture a legal source | `python3 scripts/capture.py URL --source-id ID --stage N --kind K` | Use WebFetch output as evidence. It is a summary. |
| Ingest a page the operator saved | `python3 scripts/capture.py URL --source-id ID --stage N --kind K --from-file inbox/FILE` | Treat the operator's file as fetched by you. |
| Locate a source | WebSearch, or WebFetch on the allowed domains | Treat a search snippet as a source. |
| Record pinpoint, currency, holding, admission | `python3 scripts/ledger.py annotate CAPTURE_ID --field F --value V` | Edit `evidence/ledger.jsonl` by hand. |
| Record an unretrievable source | `python3 scripts/ledger.py gap ...` | Fill the gap from memory. |
| Check evidence integrity | `python3 scripts/ledger.py verify` | — |
| compute_digest / verify_digest | the scripts, or `python3 -c` with hashlib | Write a hash by hand. |
| publish_state | write the Manifest to `state/`, run `python3 scripts/publish_state.py MANIFEST --delta ID --also CAPSULE`, then `git push` | Report state as published if the script failed. |

## Persistence

This workspace runs in a Claude Code cloud session. The machine is wiped after it sits idle. A local commit is not durable. After every `publish_state.py` run, push the working branch and confirm the push succeeded before reporting persistence. Report persistence as the pushed branch and commit.

## Reading captured sources

Read `evidence/text/` derivatives, not raw HTML. Search them first (Grep), then read only the needed section. Use the raw file only to check a disputed passage.

Confirm a currency date by reading it in the source. The capture script's candidates are unconfirmed.

## Hard limits

- Official sources only. `capture.py` refuses domains outside `gate/source_domains.json`. Ask the operator before using `--allow-other-domain`.
- CanLII: one hand-picked decision page at a time. No crawling.
- When a site refuses automated access, record the refusal and name the exact page for the operator to save into `inbox/`.
- Never edit or delete files in `evidence/raw/` or `evidence/text/`.
- Never push to `main`, force-push, amend commits, reset or rebase.
- Stop at each phase gate and ask the operator for approval.

## Context and handoff

Before context runs high, publish current state, write the capsule with its CTX/BASIS/HOP line, and push. A new session resumes from `state/`, not from conversation memory.

## Review isolation

Each TERMINAL reviewer gets one packet folder holding only the frozen draft and admitted evidence. Give the reviewer subagent the packet path and its role. Give it nothing else: no author rationale, no other reviewer's findings. Subagent isolation is not qualified; record it as NOT_TESTED.
