# Setup — 04-E06 workspace in a Claude Code cloud session

## 1. Cloud environment (once, at claude.ai/code)

Open the environment selector, then the environment's settings.

- **Network access:** Custom. List every host in `gate/source_domains.json`. Tick "Also include default list".
- **Setup script** (adds PDF text extraction):

```
#!/bin/bash
pip install --break-system-packages pypdf || true
```

## 2. GitHub

Protect `main` in the repository settings (Settings → Branches). The session works on its own branch. You merge it into `main` when satisfied.

## 3. First session

Start a session on this repository with that environment. First prompt:

```
Run CLAUDE.md session start, initial entry, for candidate 04-E06.
Activation instruction: [paste it, or say "none yet — candidate scan only"].
```

Expected first result: verify_gate.py output, then the SOURCES / SOURCE GATE declaration.

Run `/permissions` once to confirm the rules from `.claude/settings.json` loaded.

## 4. Pages a site refuses to serve

The Worker names the exact page. Save it from your browser into `inbox/`, upload it to the session's branch on GitHub, and tell the Worker. It ingests the file with `capture.py --from-file`.
