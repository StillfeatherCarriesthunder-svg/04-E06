# OPERATOR INSTRUCTION — 04-E06 SOURCE ACQUISITION JOB

Instruction ID: 04-E06-OP-ACQ-001
Revision: 1
Date: 2026-10-10
Operator: Aaron
Governing release: UAEP-PORTABLE-3.0.0 (UAEP_WORKER_KERNEL)
Host: Claude Code cloud session, B-Series hub repository, job folder `jobs/04-E06/`
Initializer: INITIALIZE_FROM this instruction, the B-Series Index and the 04-E06 topic file

## 1. Job

This instruction authorizes one bounded source-acquisition job for candidate **04-E06**.

It does not activate 04-E06. The candidate stays CANDIDATE / UNACTIVATED. The topic file's activation rule is unchanged.

Job ID: `04-E06-ACQ-2026-10-10`

## 2. Candidate question

What method should a future paper use to identify the governing estate or succession instrument when federal, provincial, and First Nation sources all appear relevant?

This job collects the sources such a paper would need. It does not answer the question.

## 3. Fixed frame

| Element | Fixed value |
|---|---|
| Province | New Brunswick. |
| Nation | None selected. Do not research or assert facts about any real Nation. |
| Nation-specific instruments | Locate where they are published or registered. Do not open an individual Nation's land code, law or agreement. |
| Legal cutoff | 2026-10-10. Later access dates are access dates, not new cutoffs. |

## 4. Source stages

Use these as the `--stage` numbers.

1. **Federal legislation and regulations.** The Indian Act estates provisions and their application provision, the Indian Estates Regulations, the Framework Agreement on First Nation Land Management Act, the Family Homes on Reserves and Matrimonial Interests or Rights Act, and any other federal enactment the Worker finds bears on which instrument governs a succession.
2. **Federal administrative guidance.** Indigenous Services Canada and Crown-Indigenous Relations material on when the department, a province or a First Nation handles an estate.
3. **New Brunswick probate and succession law.** The Probate Court Act, the Probate Rules, the Wills Act, the Devolution of Estates Act, and any rule or statute these make governing.
4. **Registries and publication points.** Official places where land interests, First Nation laws, land codes, by-laws and self-government agreements are registered or published.
5. **Judicial treatment.** Decisions that address which regime governs a deceased's estate, with citation, court and date. Record the holding separately from context. Do not analyse it.

## 5. Fresh acquisition

Acquire every source fresh in this job.

The register and search log in `sources/prior_run/` are records of an earlier scan. Use them only to locate candidates. A row there is not evidence and does not count toward acceptance.

Source selection is the Worker's task. The operator does not choose sources.

## 6. Acceptance

For each source:
- the official URL
- the retrieval time in UTC
- the SHA-256 of the captured bytes, computed by tool
- the source's own currency date, confirmed by reading it in the source
- the pinpoint provision, page or paragraph
- the stage tag
- for cases: court, date, neutral citation, and the holding kept separate from context

Record a gap in place of any source that cannot be retrieved or verified. A gap is a finding, not a failure.

The job is done when:
- every stage has at least one captured source or a recorded gap explaining why none could be captured;
- `jobs/04-E06/draft/04-E06_Source_Register.csv` lists every capture and gap, with its capture or gap ID;
- `jobs/04-E06/draft/04-E06_Search_Log.md` lists every search and fetch, and every source excluded with its reason;
- `ledger.py verify` passes;
- the final state is published and pushed.

## 7. Hard constraints

- Source acquisition only. No essay, analysis, holding analysis, or conclusion about which regime governs.
- No legal advice or entitlement determination.
- No real Nation's law, facts or status.
- No other candidate under this instruction.
- Official primary sources only. Secondary commentary may help locate a source. It does not substitute for one.
- Respect each site's terms of use. No bulk scraping. CanLII: one hand-picked decision page at a time.
- When a site refuses automated access, record the refusal and name the exact page for the operator to save.

## 8. Authority

| Gate | Actions |
|---|---|
| ALLOWED | Initialize this job. Search, retrieve and capture public sources from domains in `gate/source_domains.json`. Record gaps. Compute hashes. Write the register and search log. Publish state. Commit and push the working branch. |
| APPROVAL_REQUIRED | Adding a domain to `gate/source_domains.json`. Using `--allow-other-domain`. Any scope change. |
| PROHIBITED | Drafting the paper or any analysis. Activating 04-E06. Work on another candidate. Editing the topic file, the B-Series Index or the governing files. Pushing to `main`. Legal advice. |

## 9. Risk and completion

Risk classification: **ORDINARY**. The output is a source register with no conclusions, and every row states its limits.

Completion policy: **LOCAL**.

If the Worker finds the job meets the kernel's high-stakes threshold, it reclassifies under the kernel and reports why.

## 10. Required sources for the initial gate

| ID | File | SHA-256 |
|---|---|---|
| SRC-KERNEL | `sources/governing/UAEP_WORKER_KERNEL.md` (hub) | bound in `gate/required_sources.json` |
| SRC-WORKER-INSTR | `sources/governing/WORKER_INSTRUCTIONS.md` (hub) | bound in `gate/required_sources.json` |
| SRC-INDEX | `sources/governing/00-B_SERIES_INDEX.md` (hub) | bound in `gate/required_sources.json` |
| SRC-04-E06 | `jobs/04-E06/sources/04-E06_Topic.md` | bound in `gate/required_sources.json` |
| SRC-OPERATOR | this file | bound in `gate/required_sources.json` |

No earlier Contract, Manifest or State Capsule exists for this job. Initialization creates the first ones.

## 11. Evidence destination

`jobs/04-E06/` in the hub repository, on the session's working branch.

Each published state version is a commit. Persistence is established only when the commit is pushed to GitHub.

## 12. First transition

Module: Stage 1 acquisition.

Action: Capture the federal Acts and Regulations named in Stage 1.

Acceptance: Each source meets §6.
