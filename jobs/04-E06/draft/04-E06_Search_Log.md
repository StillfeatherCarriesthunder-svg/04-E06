# 04-E06 — Search log (job 04-E06-ACQ-2026-10-10)

Candidate 04-E06 stays CANDIDATE / UNACTIVATED. Every search and fetch in this job is logged here, with every excluded source and its reason. Times are UTC. Search results locate sources only; they are not evidence.

## SEARCH AND FETCH LOG

| # | UTC | tool | query or URL | result |
|---|---|---|---|---|
| 1 | 2026-10-10T11:42:42Z | capture.py (http) | https://laws-lois.justice.gc.ca/eng/acts/I-5/FullText.html | FAILED: egress proxy refused CONNECT (403, connect_rejected). Nothing written. |
| 2 | 2026-10-10T11:43Z | curl HEAD probe | https:// root of laws.justice.gc.ca, www.sac-isc.gc.ca, www.rcaanc-cirnac.gc.ca, gazette.gc.ca, www.canlii.org, decisions.scc-csc.ca, laws.gnb.ca, www.ontario.ca, fng.ca | All refused by egress proxy (CONNECT 403). github.com reachable. Reachability probe only; nothing captured. |
| 3 | 2026-10-10T11:44Z | WebFetch | https://laws-lois.justice.gc.ca/eng/acts/I-5/FullText.html | FAILED: getaddrinfo ENOTFOUND. Locate-only tool; would not be evidence. |
| 4 | 2026-10-10T11:44Z | WebSearch | Indian Estates Regulations C.R.C., c. 954 laws-lois.justice.gc.ca | Located issuer URLs: /eng/regulations/C.R.C.,_c._954/FullText.html (laws-lois and laws mirrors), PDF at laws.justice.gc.ca/PDF/C.R.C.,_c._954.pdf, point-in-time index. Snippets report conflicting "current to" dates; not relied on. |
| 5 | 2026-10-10T16:25:04Z | capture.py (http) | https://laws-lois.justice.gc.ca/eng/acts/I-5/FullText.html | CAPTURED CAP-20261010T162504Z-784f1e81 (INDIAN-ACT). Egress restored; BLK-001 resolved. |
| 6 | 2026-10-10T16:25:19Z | capture.py (http) | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._954/FullText.html | CAPTURED CAP-20261010T162519Z-11f84813 (INDIAN-ESTATES-REGS) |
| 7 | 2026-10-10T16:25:20Z | capture.py (http) | https://laws-lois.justice.gc.ca/eng/acts/F-31.46/FullText.html | CAPTURED CAP-20261010T162520Z-83ae82e5 (FAFNLMA) |
| 8 | 2026-10-10T16:25:21Z | capture.py (http) | https://laws-lois.justice.gc.ca/eng/acts/F-1.2/FullText.html | CAPTURED CAP-20261010T162521Z-c0a7e892 (FHRMIRA) |
| 9 | 2026-10-10T16:26Z | WebSearch | Framework Agreement on First Nation Land Management consolidated version rcaanc-cirnac.gc.ca | No federal copy returned; third-party copies (leap.unep.org, faolex, lnib.net, fortmckay.com) and Justice Laws Act pages |
| 10 | 2026-10-10T16:26Z | WebSearch | First Nation Lands Register Regulations Framework Agreement on First Nation Land Management Act laws-lois.justice.gc.ca | Act pages; CIRNAC page 1554132464892; secondary summaries (treaty1.ca, doigriverfn.com, fwfn.com) |
| 11 | 2026-10-10T16:26Z | WebFetch | https://www.rcaanc-cirnac.gc.ca/eng/1554132464892 ; https://labrc.com/framework-agreement/ | FAILED: ENOTFOUND (WebFetch has no route; shell fetch used instead for locating) |
| 12 | 2026-10-10T16:26Z | curl (locate only, scratchpad) | https://www.rcaanc-cirnac.gc.ca/eng/1554132464892 | 200; title 'Regulations (Amending) the First Nations Land Registry Regulations...'; date modified 2026-04-01. Regulatory proposal notice; excluded |
| 13 | 2026-10-10T16:26Z | curl (locate only, scratchpad) | https://labrc.com/framework-agreement/ | 200; links to FA Dec 2022 PDF, FAFNLMA PDF, FA executive summaries |
| 14 | 2026-10-10T16:27Z | WebSearch | "Framework Agreement on First Nation Land Management" text Minister make available public section 7 ... | No federal publication found; third-party copies (treaty1.ca, nwac.ca, fortmckay.com, faolex) |
| 15 | 2026-10-10T16:27:04Z | capture.py (http) | https://labrc.com/wp-content/uploads/2023/03/Framework-Agreement-on-First-Nation-Land-Management-Dec-2022.pdf | CAPTURED CAP-20261010T162704Z-2feaf46c (FRAMEWORK-AGREEMENT), issuer stated, QUALIFIED |
| 16 | 2026-10-10T16:27Z | curl (locate only) | https://laws-lois.justice.gc.ca/eng/acts/F-31.46/index.html | 200; no regulation links found on page |
| 17 | 2026-10-10T16:27Z | WebSearch | "First Nations Land Registry Regulations" SOR laws-lois.justice.gc.ca | Located SOR/2007-231 FullText |
| 18 | 2026-10-10T16:27:54Z | capture.py (http) | https://laws-lois.justice.gc.ca/eng/regulations/SOR-2007-231/FullText.html | CAPTURED CAP-20261010T162754Z-379c38f3 (FN-LAND-REGISTRY-REGS), stages 1 and 4 |
| 19 | 2026-10-10T16:27:54Z | capture.py (http) | https://laws-lois.justice.gc.ca/eng/const/FullText.html | CAPTURED CAP-20261010T162754Z-c93adda0 (CONSTITUTION-ACTS) |
| 20 | 2026-10-10T16:29Z | WebSearch | federal Act Canada First Nation self-government "wills and estates" OR "succession" law-making power Indian Act sections 42 to 52 cease to apply | Committee materials on Bill C-428 (ourcommons.ca), BC Indian Act transition schedule, Law Society BC checklists. No further Canada-wide federal enactment identified; self-government Acts are Nation-specific |

## EXCLUDED

| source | reason |
|---|---|
| Third-party copies of the Framework Agreement (treaty1.ca, nwac.ca, fortmckay.com, doigriverfn.com, faolex.fao.org, leap.unep.org) | Not issuer copies; LABRC copy captured (QUALIFIED) |
| LABRC Framework Agreement executive summaries; treaty1.ca, fwfn.com, lnib.net summaries | Secondary summaries |
| CIRNAC page 1554132464892 (proposal to amend First Nations Land Registry Regulations) | Regulatory proposal notice, not law or estates guidance |
| First Nations Land Management Act, S.C. 1999, c. 24 | Repealed and replaced by FAFNLMA (2022); add only if activation fixes a pre-2023 period |
| Bill C-428 committee report and evidence (ourcommons.ca / noscommunes.ca) | Parliamentary materials on an unenacted bill; current Indian Act capture shows ss. 42-47 in force |
| Law Society of BC practice checklists G-1, G-3 | Secondary practice material |
| BC 'Indian Act transition' schedule (leg.bc.ca, bcpublications.ca) | Treaty-implementation bill schedule tied to specific Nations; Nation-specific |
| Federal self-government and modern-treaty implementing Acts | Nation-specific instruments; operator has requested none (§3). Located via CIRNAC index in Stage 4 instead |
