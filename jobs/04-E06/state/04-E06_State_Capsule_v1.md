```text
UAEP-WORKER | RELEASE:UAEP-PORTABLE-3.0.0 | SCHEMA:UAEP-CW/2 | JOB:04-E06-ACQ-2026-10-10 | V:1 | STATE:ACTIVE
M:jobs/04-E06/state/04-E06_Master_Manifest_v1.json | rev 1 | parent null | delta 04-E06-D001-INIT | sha256 in state/published.jsonl
CONTRACT:04-E06-CONTRACT rev 1 = INITIALIZE_FROM SRC-OPERATOR (04-E06-OP-ACQ-001 rev 3) + SRC-04-E06 + SRC-INDEX
OBJ:Acquire fresh primary sources for 04-E06 source-identification method; collect only, no answer
DONE:stages 1-5 each captured or gapped; draft/04-E06_Source_Register.csv; draft/04-E06_Search_Log.md; ledger verify PASS; final state pushed | policy LOCAL
ACTIVE:M1 Stage 1 federal legislation and regulations
NEXT:T1-01..T1-05 captures, confirm currency/pinpoints, publish V2
S:SRC-KERNEL 3.0.0, SRC-WORKER-INSTR 3.0.0, SRC-INDEX, SRC-04-E06, SRC-OPERATOR rev3 all COMPLETE | gate PASS verify_gate.py --bind 2026-10-10
C:primary sources from issuer sites only; --issuer for unlisted sites; CanLII one page at a time; no Nation instrument without operator request; cutoff 2026-10-10; prior_run locate-only; never touch evidence/raw|text; no push to main/force/amend/reset/rebase
A:APV-001 init + Stage 1 (operator Go); APPROVAL_REQUIRED: Nation instrument, scope change; PROHIBITED: analysis, activation, other candidates, governing-file edits, main, legal advice
U:none material
T:T1-01 IN_PROGRESS; T1-02..T1-05 READY; M2-M6 READY
E:gate check verify_gate.py PASS; ledger empty
R:ORDINARY (no conclusions; rows state limits); residual: site refusals -> gaps/operator inbox requests
Δ:initialized job; contract, plan 04-E06-PLAN v1 EXECUTION_PLAN_SECURED; M1 started
PLAN:no CONTROL packet; 04-E06-PLAN v1 Worker-authored, EXECUTION_PLAN_SECURED
CTX:LOW | BASIS:fresh session, single module active, no corrections | HOP:NO
```
