# Setup — B-Series hub in Claude Code cloud sessions

## 1. Cloud environment (once, at claude.ai/code)

Open the environment selector, then the environment's settings.

- **Network access:** Custom. List every host in `templates/source_domains.json`, plus any a job has approved. Tick "Also include default list".
- **Setup script** (adds PDF text extraction):

```
#!/bin/bash
pip install --break-system-packages pypdf || true
```

## 2. GitHub

Protect `main` in the repository settings (Settings → Branches). Each session works on its own branch. You merge it into `main` when satisfied.

## 3. Run a job

Start a session on this repository with that environment. First prompt for 04-E06:

```
Job 04-E06. Run CLAUDE.md session start, initial entry.
```

Expected first result: verify_gate.py output, then the SOURCES / SOURCE GATE declaration.

To resume later: `Job 04-E06. Resume from the current Manifest.`

Run `/permissions` once to confirm the rules from `.claude/settings.json` loaded.

## 4. Start another job

1. In a session: `Create job <ID>.` It creates and pushes `jobs/<ID>/`.
2. On GitHub, upload the topic file and operator instruction to `jobs/<ID>/sources/` on that branch.
3. Tell the session they're there. It registers and binds them, then runs the session start.

## 5. Pages a site refuses to serve

The Worker names the exact page. Save it from your browser, upload it to `jobs/<ID>/inbox/` on the session's branch on GitHub, and tell the Worker. It ingests the file with `capture.py --from-file`.
