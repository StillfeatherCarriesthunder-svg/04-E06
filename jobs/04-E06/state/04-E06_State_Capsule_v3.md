```text
UAEP-WORKER | RELEASE:UAEP-PORTABLE-3.0.0 | SCHEMA:UAEP-CW/2 | JOB:04-E06-ACQ-2026-10-10 | V:3 | STATE:ACTIVE
M:jobs/04-E06/state/04-E06_Master_Manifest_v3.json | rev 3 | parent 2 | delta 04-E06-D003-M1-COMPLETE | sha256 in state/published.jsonl
CONTRACT:04-E06-CONTRACT rev 1 = INITIALIZE_FROM SRC-OPERATOR (04-E06-OP-ACQ-001 rev 3) + SRC-04-E06 + SRC-INDEX
OBJ:Acquire fresh primary sources for 04-E06 source-identification method; collect only, no answer
DONE:stages 1-5 each captured or gapped; draft/04-E06_Source_Register.csv; draft/04-E06_Search_Log.md; ledger verify PASS; final state pushed | policy LOCAL
ACTIVE:M2 Stage 2 federal administrative guidance
NEXT:T2-01..T2-03 captures; then M3
S:SRC-KERNEL 3.0.0, SRC-WORKER-INSTR 3.0.0, SRC-INDEX, SRC-04-E06, SRC-OPERATOR rev3 all COMPLETE | gate PASS (rechecked verify_gate.py 2026-10-10T16:25Z, unchanged)
C:primary sources from issuer sites only; --issuer for unlisted sites; CanLII one page at a time; no Nation instrument without operator request; cutoff 2026-10-10; prior_run locate-only; never touch evidence/raw|text; no push to main/force/amend/reset/rebase
A:APV-001 init + Stage 1 (operator Go); operator 'Start' resumes after BLK-001; APPROVAL_REQUIRED: Nation instrument, scope change; PROHIBITED: analysis, activation, other candidates, governing-file edits, main, legal advice
U:FAFNLMA s. 7 federal publication of Framework Agreement not located (LABRC copy QUALIFIED)
T:M1 COMPLETE (T1-01..T1-05); T2-01 IN_PROGRESS; T2-02, T2-03 READY; M3-M6 READY
E:ledger 7 captures (INDIAN-ACT, INDIAN-ESTATES-REGS, FAFNLMA, FHRMIRA, FRAMEWORK-AGREEMENT, FN-LAND-REGISTRY-REGS, CONSTITUTION-ACTS), ANN-0001..0022, verify PASS; search log rows 1-20
R:ORDINARY; no material risk open
Δ:BLK-001 resolved (egress restored); Stage 1 captured, currency confirmed by reading, pinpoints recorded
PLAN:no CONTROL packet; 04-E06-PLAN v1 EXECUTION_PLAN_SECURED
CTX:LOW | BASIS:one module active, evidence in ledger, no corrections | HOP:NO
```
