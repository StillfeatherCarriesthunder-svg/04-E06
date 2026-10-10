# Setup — B-Series hub in Claude Code cloud sessions

## 1. Cloud environment (once, at claude.ai/code)

Click the cloud icon showing the environment name, just above the message box. Hover over the environment, click the gear, and set **Network access** to **Full**. Save.

Full lets sessions reach any website. Sources can come from any issuing body's site, so a fixed list would block them. `capture.py` records the issuer of every source from a site it doesn't already know.

Nothing else is needed. `pypdf` installs itself at session start.

## 2. Run a job

Start a session on this repository with that environment. First prompt for 04-E06:

```
Job 04-E06. Run CLAUDE.md session start, initial entry.
```

Expected first result: verify_gate.py output, then the SOURCES / SOURCE GATE declaration.

To resume later: `Job 04-E06. Resume from the current Manifest.`

Run `/permissions` once to confirm the rules from `.claude/settings.json` loaded.

## 3. Start another job

1. In a session: `Create job <ID>.` It creates and pushes `jobs/<ID>/`.
2. On GitHub, upload the topic file and operator instruction to `jobs/<ID>/sources/` on that branch.
3. Tell the session they're there. It registers and binds them, then runs the session start.

## 4. Pages a site refuses to serve

The Worker names the exact page. Save it from your browser, upload it to `jobs/<ID>/inbox/` on the session's branch on GitHub, and tell the Worker. It ingests the file with `capture.py --from-file`.

## 5. After every session: merge

A new session starts from `main`. If a session's branch isn't merged, the next session won't see its progress.

1. In the session at claude.ai/code, click **Create PR**.
2. On GitHub, open the pull request and click **Merge**.
