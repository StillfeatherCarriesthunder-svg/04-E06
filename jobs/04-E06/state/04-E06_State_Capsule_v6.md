```text
UAEP-WORKER | RELEASE:UAEP-PORTABLE-3.0.0 | SCHEMA:UAEP-CW/2 | JOB:04-E06-ACQ-2026-10-10 | V:6 | STATE:ACTIVE
M:jobs/04-E06/state/04-E06_Master_Manifest_v6.json | rev 6 | parent 5 | delta 04-E06-D006-M3-COMPLETE | sha256 in state/published.jsonl
CONTRACT:04-E06-CONTRACT rev 1 = INITIALIZE_FROM SRC-OPERATOR (04-E06-OP-ACQ-001 rev 3) + SRC-04-E06 + SRC-INDEX
OBJ:Acquire fresh primary sources for 04-E06 source-identification method; collect only, no answer
DONE:stages 1-5 each captured or gapped; draft/04-E06_Source_Register.csv; draft/04-E06_Search_Log.md; ledger verify PASS; final state pushed | policy LOCAL
ACTIVE:M4 Stage 4 registries and publication points
NEXT:T4-01 captures; then M5 judicial treatment; then M6 register/log/verify
S:SRC-KERNEL 3.0.0, SRC-WORKER-INSTR 3.0.0, SRC-INDEX, SRC-04-E06, SRC-OPERATOR rev3 all COMPLETE | gate PASS (rechecked verify_gate.py 2026-10-10T16:25Z, unchanged)
C:primary sources from issuer sites only; --issuer for unlisted sites; CanLII one page at a time; no Nation instrument without operator request; cutoff 2026-10-10; prior_run locate-only; never touch evidence/raw|text; no push to main/force/amend/reset/rebase
A:APV-001 init + Stage 1 (operator Go); operator 'Start' resumes after BLK-001; APPROVAL_REQUIRED: Nation instrument, scope change; PROHIBITED: analysis, activation, other candidates, governing-file edits, main, legal advice
U:FAFNLMA s. 7 federal publication not located (LABRC copy QUALIFIED); PEI wills/intestacy statute not identified
T:M1-M3 COMPLETE; T4-01 IN_PROGRESS; T5-01, M6 READY; EXT-001 operator saves for GAP-001..011 (non-blocking)
E:ledger 49 captures (4 NOT_ADMITTED), 11 gaps (NS, PE, YT, NU site refusals), ANN-0001..0143, verify PASS; search log rows 1-76
R:ORDINARY; no material risk open
Δ:Stage 3 complete: QC, NB, NL, NT captured; NS statutes, PE, YT, NU recorded as gaps (site refusals) with exact pages for operator
PLAN:no CONTROL packet; 04-E06-PLAN v1 EXECUTION_PLAN_SECURED
CTX:MEDIUM | BASIS:long session, high evidence churn, state fully in ledger/manifest | HOP:NO
```
