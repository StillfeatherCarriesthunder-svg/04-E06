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
| 21 | 2026-10-10T16:30:05Z | capture.py (http) | https://www.sac-isc.gc.ca/eng/1100100032357/1581866877231 | CAPTURED CAP-20261010T163005Z-a3c088a0 (ISC-ESTATE-SERVICES) |
| 22 | 2026-10-10T16:30:53Z | capture.py (http) | https://www.sac-isc.gc.ca/eng/1475591157216/1581869169920 | CAPTURED CAP-20261010T163053Z-d0e2d1ec (ISC-WILLS, infographic) |
| 23 | 2026-10-10T16:30:54Z | capture.py (http) | https://www.sac-isc.gc.ca/eng/1476815262545/1581869354739 | CAPTURED CAP-20261010T163054Z-4c9dc05e (ISC-ADMINISTERING-ESTATE). Prior run reported this page blocked; it was retrievable here |
| 24 | 2026-10-10T16:31:20Z | capture.py (http) | https://www.sac-isc.gc.ca/eng/1100100032530 | CAPTURED CAP-20261010T163120Z-b716c04b (ISC-WHY-WILL); redirected to /eng/1100100032530/1581868983148 |
| 25 | 2026-10-10T16:31Z | WebSearch | sac-isc.gc.ca OR rcaanc-cirnac.gc.ca estates land code First Nation "wills and estates" self-government agreement Indian Act estates no longer apply | No official page; secondary (indigenous.plea.org, mondaq, lawinsider), First Nation-hosted summaries (fortmckay.com, tletinqox.ca, wahnapitaefirstnation.com), labrc.com, committee report |
| 26 | 2026-10-10T16:31Z | WebSearch | rcaanc-cirnac.gc.ca matrimonial real property on reserve First Nations with own laws list Family Homes on Reserves death of spouse provisional federal rules | ISC MRP page; ISC FHRMIRA laws list; Legal Aid BC; nsfamilylaw.ca; First Nation MRP law pages |
| 27 | 2026-10-10T16:31:58Z | capture.py (http) | https://www.sac-isc.gc.ca/eng/1100100032553 | CAPTURED CAP-20261010T163158Z-2b609ed7 (ISC-MRP-ON-RESERVE) |
| 28 | 2026-10-10T16:32:00Z | capture.py (http) | https://www.sac-isc.gc.ca/eng/1408981855429 | CAPTURED CAP-20261010T163200Z-824664a5 (ISC-FHRMIRA-FN-LAWS-LIST), stage 4 publication point |
| 29 | 2026-10-10T16:32Z | WebSearch | rcaanc-cirnac.gc.ca estates Yukon Northwest Territories First Nations estate services Indian Act | CIRNAC Wills and Estates (Yukon) page; ISC page; secondary (hullandhull.com, allaboutestates.ca, willful.co, cmmns.com); lnib.net copy |
| 30 | 2026-10-10T16:32:27Z | capture.py (http) | https://www.rcaanc-cirnac.gc.ca/eng/1334096114211 | CAPTURED CAP-20261010T163227Z-74d77292 (CIRNAC-YUKON-WILLS-ESTATES) |
| 31 | 2026-10-10T16:33Z | WebSearch | bclaws.gov.bc.ca Wills, Estates and Succession Act SBC 2009 c 13 complete | BC Laws WESA URLs; free.bcpublications.ca mirror; secondary (Wikipedia, courthouselibrary.ca, lslap.bc.ca, lawsociety.bc.ca, nanaimolaw.com) |
| 32 | 2026-10-10T16:33Z | WebSearch | kings-printer.alberta.ca Wills and Succession Act W-12.2 Estate Administration Act Surrogate Rules PDF | open.alberta.ca catalogue; secondary (lesaonline.org, carters.ca, alri.ualberta.ca) |
| 33 | 2026-10-10T16:33Z | WebSearch | publications.saskatchewan.ca The Wills Act, 1996 The Intestate Succession Act, 2019 The Administration of Estates Act | Intestate Succession Act, 2019 download (product 102827); saskatchewan.ca guidance; secondary (mltaikins.com, bcli.org, mondaq) |
| 34 | 2026-10-10T16:33Z | WebSearch | web2.gov.mb.ca laws statutes ccsm Wills Act w150 Intestate Succession Act i85 Court of King's Bench Surrogate Practice Act | Manitoba Laws w150, c290 pages; secondary (manitobalawreform.ca, Law Society MB) |
| 35 | 2026-10-10T16:34:06Z | capture.py (http) | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/09013_01 | CAPTURED CAP-20261010T163406Z-d0e36cdf (BC-WESA) |
| 36 | 2026-10-10T16:34Z | WebSearch | bclaws.gov.bc.ca Supreme Court Civil Rules Part 25 estates "168/2009" rule 25-3 | Located 168_2009_03_1 and related documents; cbabc.org consultation (secondary) |
| 37 | 2026-10-10T16:34Z | curl (locate only) | bclaws.gov.bc.ca .../statreg/168_2009_03, 168_2009_03_1, 168_2009_04, 168_2009_04_1 | 168_2009_03_1 holds 'Part 25 — Estates' |
| 38 | 2026-10-10T16:34:56Z | capture.py (http) | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/168_2009_03_1 | CAPTURED CAP-20261010T163456Z-b280f253 (BC-SCCR-PART25) |
| 39 | 2026-10-10T16:35Z | curl (locate only) | https://open.alberta.ca/publications/w12p2 | 200; links to kings-printer.alberta.ca catalogue |
| 40 | 2026-10-10T16:35:22Z | capture.py (http) | kings-printer.alberta.ca/documents/Acts/W12P2.pdf ; /Acts/E12P5.pdf ; /Regs/1995_130.pdf | CAPTURED CAP-20261010T163522Z-a61250a7 (AB-WILLS-SUCCESSION), CAP-20261010T163526Z-c2b2a897 (AB-ESTATE-ADMIN), CAP-20261010T163528Z-cdf149c2 (AB-SURROGATE-RULES) |
| 41 | 2026-10-10T16:36Z | WebSearch | publications.saskatchewan.ca "Wills Act, 1996" W-14.1 download | Product 940 (English), 2485 (French); secondary (mltaikins.com, cbasask.org, lawsociety.sk.ca, lawreformcommission.sk.ca) |
| 42 | 2026-10-10T16:36Z | WebSearch | publications.saskatchewan.ca "Administration of Estates Act" A-4.1 download | Product 389 (Act), 110054 (Regulations); saskatchewan.ca guidance; vlex (gated) |
| 43 | 2026-10-10T16:36:20Z | capture.py (http) | publications.saskatchewan.ca products 940/1517, 102827/113952, 389/419 | CAPTURED CAP-20261010T163620Z-f8e81b1f (SK-WILLS-ACT), CAP-20261010T163621Z-6c249703 (SK-INTESTATE-SUCCESSION), CAP-20261010T163622Z-793810c9 (SK-ADMIN-ESTATES) |
| 44 | 2026-10-10T16:37Z | WebSearch | Saskatchewan King's Bench Rules Part 16 estates sasklawcourts.ca PDF | Publications Saskatchewan product 73108; sasklawcourts.ca Part 16 forms; Law Society SK webinar notice (Part 16 revisions, fall 2025) |
| 45 | 2026-10-10T16:37Z | curl (locate only) | sasklawcourts.ca rules pages (one 404; home; /kings-bench/rules-practice-directives/) | Court page links the King's Bench Rules to publications.saskatchewan.ca product 73108 |
| 46 | 2026-10-10T16:37:37Z | capture.py (http) | https://publications.saskatchewan.ca/api/v1/products/73108/formats/81637/download | CAPTURED CAP-20261010T163737Z-f6c8ab1e (SK-KB-RULES) |
| 47 | 2026-10-10T16:38:16Z | capture.py (http) | web2.gov.mb.ca/laws/statutes/ccsm/w150.php, i085.php, c290.php (?lang=en) | CAPTURED CAP-20261010T163816Z-cd2868ad (MB-WILLS-ACT), CAP-20261010T163817Z-1ba9c681 (MB-INTESTATE-SUCCESSION), CAP-20261010T163818Z-95835e04 (MB-SURROGATE-PRACTICE) |
| 48 | 2026-10-10T16:38Z | curl (locate only) | web2.gov.mb.ca/laws/regs/current/_pdf-regs.php?reg=553/88 ; /553-88.php?lang=en | Both 200; HTML contains RULE 74 |
| 49 | 2026-10-10T16:38:58Z | capture.py (http) | https://web2.gov.mb.ca/laws/regs/current/553-88.php?lang=en | CAPTURED CAP-20261010T163858Z-b0f1ba68 (MB-KB-RULES) |
| 50 | 2026-10-10T16:40:35Z | capture.py (http) | https://www.ontario.ca/laws/statute/90s26 | CAPTURED CAP-20261010T164035Z-815e351a but body is the e-Laws JavaScript shell only; NOT_ADMITTED |
| 51 | 2026-10-10T16:41Z | capture.py (--browser) | https://www.ontario.ca/laws/statute/90s26 | FAILED: Playwright 1.63 expected a Chromium build not installed; installed Playwright 1.56.0 to match the preinstalled Chromium 1194 |
| 52 | 2026-10-10T16:42:12Z | capture.py (--browser) | https://www.ontario.ca/laws/statute/90s26 | CAPTURED CAP-20261010T164212Z-7394e647 (ON-SLRA), rendered DOM |
| 53 | 2026-10-10T16:42:34Z | capture.py (--browser) | https://www.ontario.ca/laws/statute/90e21 ; /90e22 | CAPTURED CAP-20261010T164234Z-3ac41a2f (ON-ESTATES-ACT), CAP-20261010T164239Z-38e66325 (ON-ESTATES-ADMIN-ACT) |
| 54 | 2026-10-10T16:43:01Z | capture.py (--browser) | https://www.ontario.ca/laws/regulation/900194 | CAPTURED CAP-20261010T164301Z-c33f6b35 (ON-RULES-CIVIL-PROCEDURE) |

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
| indigenous.plea.org, mondaq.com, lawinsider.com, hullandhull.com, allaboutestates.ca, willful.co, Legal Aid BC, nsfamilylaw.ca | Secondary sources; pointers only |
| First Nation-hosted summaries of Indian Act sections that cease to apply (fortmckay.com, tletinqox.ca, wahnapitaefirstnation.com) and lnib.net / cmmns.com copies of ISC material | Not issuer copies or secondary; Nation-hosted material not opened under §3 |
| First Nation MRP law pages (aamjiwnaang.ca, fisherriver.ca) | Nation-specific instruments; operator has requested none (§3) |
| Community profiles linked from the ISC FHRMIRA laws list | Nation-specific; not opened |
| CIRNAC NWT-specific estates page | None located; NWT covered only by the ISC national page statement |
| Wikipedia, courthouselibrary.ca, lslap.bc.ca, Law Society of BC checklists, nanaimolaw.com, cbabc.org | Secondary sources (BC) |
| free.bcpublications.ca copies of BC statutes and rules | Mirror; BC Laws (bclaws.gov.bc.ca) copies captured instead |
| lesaonline.org, carters.ca, alri.ualberta.ca; open.alberta.ca catalogue page | Secondary sources / catalogue entry (AB) |
| French consolidation of The Wills Act, 1996 (product 2485) | Same Act in French; English consolidation captured |
| The Administration of Estates Regulations (SK, A-4.1 Reg 2) | Procedural regulations; not identified as bearing on which law governs; not opened |
| mltaikins.com, cbasask.org, lawsociety.sk.ca, lawreformcommission.sk.ca, bcli.org, mondaq.com | Secondary sources (SK) |
| manitobalawreform.ca report; Law Society of Manitoba education materials | Secondary sources (MB) |
| Manitoba bilingual PDF versions | HTML versions captured; pages state the bilingual PDF is the official copy (recorded as QUALIFIED) |
| CAP-20261010T164035Z-815e351a (Ontario SLRA, HTTP) | Captured JavaScript shell without statute text; NOT_ADMITTED; superseded by browser capture |
