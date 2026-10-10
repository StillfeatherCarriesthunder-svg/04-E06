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
| 55 | 2026-10-10T16:44:28Z | capture.py (http) | https://www.legisquebec.gouv.qc.ca/en/document/cs/CCQ-1991 | CAPTURED CAP-20261010T164428Z-a71ceb5b (QC-CIVIL-CODE) |
| 56 | 2026-10-10T16:45:07Z | capture.py (http) | https://www.legisquebec.gouv.qc.ca/en/document/cs/C-25.01 | CAPTURED CAP-20261010T164507Z-28a94dbd (QC-CODE-CIVIL-PROCEDURE) |
| 57 | 2026-10-10T16:45:28Z | capture.py (http) | laws.gnb.ca/en/document/cs/P-17.1, cr/84-9, cs/W-9, cs/D-9 | CAPTURED CAP-20261010T164528Z-27bc9434, CAP-20261010T164529Z-ebc02c21, CAP-20261010T164529Z-d2b949ea, CAP-20261010T164530Z-c6064080 (NB) |
| 58 | 2026-10-10T16:46:07Z | capture.py (http) | nslegislature.ca/sites/default/files/legc/statutes/wills.htm, intestate%20succession.htm, probate.htm | REFUSED by site: 244-byte 'Request Rejected' pages captured (CAP-20261010T164607Z-a749bcc2, CAP-20261010T164608Z-7aa2422f, CAP-20261010T164608Z-c2492cb5), NOT_ADMITTED; GAP-001..003 |
| 59 | 2026-10-10T16:46Z | WebSearch | Nova Scotia Probate Court Practice, Procedure and Forms Regulations novascotia.ca just regulations | novascotia.ca/just/regulations/regs/probregs.htm |
| 60 | 2026-10-10T16:46:35Z | capture.py (http) | https://novascotia.ca/just/regulations/regs/probregs.htm | CAPTURED CAP-20261010T164635Z-7775a3aa (NS-PROBATE-REGS) |
| 61 | 2026-10-10T16:47Z | WebSearch | princeedwardisland.ca legislation Probate Act P-21 Wills Act Intestate Succession PDF Prince Edward Island | qatauth.gpei.ca copy; bac-lac archive; secondary (estateexec.com, taxtips.ca, lovable.app) |
| 62 | 2026-10-10T16:47Z | capture.py (http) | https://www.princeedwardisland.ca/sites/default/files/legislation/p-21-probate_act.pdf | FAILED: HTTP 403 (site refusal); GAP-004 |
| 63 | 2026-10-10T16:47Z | WebSearch | Prince Edward Island "Wills Act" RSPEI ... princeedwardisland.ca legislation pdf | No PEI wills statute located; GAP-005 |
| 64 | 2026-10-10T16:47Z | WebSearch | courts.pe.ca Rules of Civil Procedure Rule 74 estates ... | courts.pe.ca rules index; PEI Rule 74 is Small Claims |
| 65 | 2026-10-10T16:47Z | curl (locate only) | https://www.courts.pe.ca/rules-of-civil-procedure | HTTP 403 (site refusal); GAP-006 |
| 66 | 2026-10-10T16:48:06Z | capture.py (http) | assembly.nl.ca/Legislation/sr/statutes/w10.htm ; i21.htm | CAPTURED CAP-20261010T164806Z-f35d401b (NL-WILLS-ACT), CAP-20261010T164807Z-c5069825 (NL-INTESTATE-SUCCESSION) |
| 67 | 2026-10-10T16:48Z | WebSearch | assembly.nl.ca Rules of the Supreme Court 1986 Rule 55 probate ... | court.nl.ca probate page and forms (Rule 56) |
| 68 | 2026-10-10T16:49Z | curl (locate only) | https://www.court.nl.ca/supreme/?p=1635 | Links to Rule 56 (assembly.nl.ca RulesSC/Rc86ru56.htm) and Resealing Order rc960744 |
| 69 | 2026-10-10T16:49:16Z | capture.py (http) | https://www.assembly.nl.ca/legislation/sr/regulations/RulesSC/Rc86ru56.htm | CAPTURED CAP-20261010T164916Z-bf2961e4 (NL-RULE-56) |
| 70 | 2026-10-10T16:49Z | WebSearch | laws.yukon.ca Wills Act Estate Administration Act Yukon consolidated PDF ; justice.gov.nt.ca ... ; nunavutlegislation.ca ... | Yukon: archived gov.yk.ca PDFs, yukon.ca guidance; NWT: justice.gov.nt.ca PDFs, laws.opennwt.ca copies; Nunavut: nunavutlegislation.ca downloads 393, 7788 |
| 71 | 2026-10-10T16:50Z | capture.py (http) + curl | laws.yukon.ca PDFs 2002-0230, 2002-0077; laws.yukon.ca home | FAILED: HTTP 403 on PDFs and home page (site refusal); GAP-007, GAP-008 |
| 72 | 2026-10-10T16:50:25Z | capture.py (http) | justice.gov.nt.ca/en/files/legislation/wills/wills.a.pdf ; intestate-succession/intestate-succession.a.pdf | CAPTURED CAP-20261010T165025Z-1a826f29 (NT-WILLS-ACT), CAP-20261010T165027Z-6238ba2f (NT-INTESTATE-SUCCESSION) |
| 73 | 2026-10-10T16:51Z | WebSearch | Northwest Territories probate rules Supreme Court ... | Estate Administration Rules R-123-2016 (judicature.r9.pdf) |
| 74 | 2026-10-10T16:51:04Z | capture.py (http) | https://www.justice.gov.nt.ca/en/files/legislation/judicature/judicature.r9.pdf | CAPTURED CAP-20261010T165104Z-e483a9f6 (NT-ESTATE-ADMIN-RULES) |
| 75 | 2026-10-10T16:51Z | curl (locate only) | nunavutlegislation.ca/en/file-download/download/public/393, 7788, 6437 | HTTP 403 (site refusal); GAP-009..011 |
| 76 | 2026-10-10T16:52:04Z | capture.py (http) | https://www.assembly.nl.ca/Legislation/sr/statutes/j04.htm | CAPTURED CAP-20261010T165204Z-1c4dff2f (NL-JUDICATURE-ACT) |
| 77 | 2026-10-10T16:53:40Z | capture.py (http) | https://www.sac-isc.gc.ca/eng/1100100034803 ; https://www.rcaanc-cirnac.gc.ca/eng/1100100030583/1529420498350 ; https://www.gazette.gc.ca/rp-pr/p2/2025/2025-01-01/html/sor-dors280-eng.html | CAPTURED CAP-20261010T165340Z-9f44bc33 (ISC-LAND-REGISTRATION), CAP-20261010T165341Z-9ebace95 (CIRNAC-FINAL-AGREEMENTS-INDEX), CAP-20261010T165342Z-86d0a164 (CANADA-GAZETTE-SOR-2024-280) |
| 78 | 2026-10-10T16:54:22Z | capture.py (http) | https://fng.ca/ ; https://labrc.com/resource/land-codes/ | CAPTURED CAP-20261010T165422Z-c7dae726 (FIRST-NATIONS-GAZETTE), CAP-20261010T165426Z-05e5d4f1 (LABRC-LAND-CODES-COLLECTION); publication points only |
| 79 | 2026-10-10T16:55Z | WebSearch | Attorney General of Canada v. Canard [1976] 1 SCR 170 decisions.scc-csc.ca | Secondary only (reseaudialog.ca, vlex, Wikipedia, erudit.org, alexi.com) |
| 80 | 2026-10-10T16:55Z | WebSearch | "ordinarily resident" reserve estate Indian Act section 4(3) court decision province jurisdiction estate deceased canlii | Secondary (allaboutestates.ca, hullandhull.com, bmo.com, fultonco.com); committee evidence; 1975 CanLII 137 identified |
| 81 | 2026-10-10T16:55Z | capture.py (http) | https://www.canlii.org/en/ca/scc/doc/1975/1975canlii137/1975canlii137.html | FAILED: HTTP 403 (one hand-picked page; refusal); GAP-012 |
| 82 | 2026-10-10T16:55Z | WebSearch | scc-csc.lexum.com OR decisions.scc-csc.ca "Canard" 1975 "item" ... | No SCC page; reseaudialog.ca, vlex, decision.tcc-cci.gc.ca FC decision 64640, millerthomson.com |
| 83 | 2026-10-10T16:55Z | curl (locate only) | decisions.scc-csc.ca search for 'Canard' 1975-1976 | HTTP 403 (refusal) |
| 84 | 2026-10-10T16:56Z | curl (reachability probe) | decisions.fct-cf.gc.ca, decisions.fca-caf.gc.ca, www.yukoncourts.ca, www.bccourts.ca, www.courts.gov.bc.ca | FC and FCA 403; Yukon courts 200; bccourts.ca connection reset; courts.gov.bc.ca TLS verification failure |
| 85 | 2026-10-10T16:56Z | WebSearch | Dickson Estate 2012 YKSC 71 yukoncourts.ca Indian Act ordinarily resident reserve estate | yukoncourts.ca PDF; secondary (millerthomson.com, legalline.ca, hammerco.ca) |
| 86 | 2026-10-10T16:56Z | curl HEAD (locate only) | yukoncourts.ca .../documents/en/ and /fr/ 2012_yksc_71_dickson_estate.pdf | Both 301 to www.yukoncourts.ca |
| 87 | 2026-10-10T16:56:45Z | capture.py (http) | https://yukoncourts.ca/sites/default/files/documents/fr/2012_yksc_71_dickson_estate.pdf | CAPTURED CAP-20261010T165645Z-90dbfd2f (CASE-DICKSON-2012-YKSC-71) |
| 88 | 2026-10-10T16:57Z | WebSearch | court decision estate deceased First Nation member which law governs provincial probate court jurisdiction Indian Act section 44 ... | estateably.com, hullandhull.com, aboriginal.legalaid.bc.ca (secondary); FC decision 521878 (s. 44 transfer, 2021) |
| 89 | 2026-10-10T16:57Z | curl (locate only) | decision.tcc-cci.gc.ca/fc-cf/decisions/en/521878/1/document.do ; .../64640/1/document.do | HTTP 403 (refusal); GAP-015 |
| 90 | 2026-10-10T16:58Z | WebSearch | "Indian Act" estate "ordinarily resident" reserve "letters of administration" ... manitobacourts.mb.ca OR albertacourts.ca OR courts.ns.ca | No provincial court-site decisions beyond Dickson; decisions.fca-caf.ca 526480 (host refuses) |

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
| qatauth.gpei.ca copy of PEI Probate Act | Host appears to be a non-production mirror, not an official publication point |
| Library and Archives Canada web-archive copies (PEI 2003, Yukon 2020) | Archived copies, not current consolidations |
| estateexec.com, taxtips.ca, will-kit-prospects.lovable.app, willful.co, cwilson.com, canadianlawyermag.com | Secondary sources |
| court.nl.ca probate forms and 2011 probate booklet | Court forms and guidance; Rule 56 and Judicature Act Part VI captured instead |
| NL Resealing of Foreign Grants of Probate and Administration Order (rc960744) | Reciprocal-jurisdiction order for resealing; not opened; add if activation needs it |
| yukon.ca wills and estates guidance pages; Yukon bill news releases | Territorial guidance and news, not the statutes; statutes recorded as gaps |
| laws.opennwt.ca and gazette.opennwt.ca copies | Third-party parses of GNWT PDFs; justice.gov.nt.ca originals captured |
| legislation.nt.gov.au (Northern Territory, Australia) | Not a Canadian jurisdiction |
| nunavutcourts.ca probate forms; pravo.hse.ru copy of Nunavut Wills Act | Forms only / third-party copy |
| NWT Judicature Act | Enabling statute for the Estate Administration Rules; rules captured; Act not opened |
| ISC land registry search interfaces | Not opened; registries described by ISC-LAND-REGISTRATION capture |
| Items listed on the First Nations Gazette home page and individual land codes in the LABRC collection | Nation-specific instruments; operator has requested none (§3) |
| jurisprudence.reseaudialog.ca, Wikipedia, erudit.org, alexi.com, millerthomson.com, hullandhull.com, allaboutestates.ca, bmo.com, fultonco.com, estateably.com, legalline.ca, hammerco.ca, aboriginal.legalaid.bc.ca | Secondary sources; pointers only |
| vlex case pages | Login or trial gated; secondary |
| House of Commons AANO committee evidence and reports | Parliamentary testimony and reports, not primary law or decisions |
| Canard, Manitoba Court of Appeal (1972) | Lower-court stage of the same matter; SCC decision recorded as GAP-012 |
| Mitchell v. Canada (Indigenous Services), 2024 FC 148 | Per secondary source, concerns valuation of reserve property, not which regime governs |
| Brooks v. Canada (Indigenous Services), 2022 FC 1064 | Secondary sources cite it for forum practice; relevance to which regime governs unverified; Federal Court hosts refuse automated access |
| Toney v. Toney Estate, 2018 NSSC 179; Okanagan Indian Band v. Bonneau, 2003 BCCA 299 | Secondary sources cite them for intestacy and family-home points, not which regime governs; not verified |
| decisions.fca-caf.ca/fc-cf/decisions/en/526480 | Unidentified Federal Court decision in a search result; host refuses automated access |

Coverage (from draft/04-E06_Source_Register.csv): 55 captures, 15 gaps. Stage 1: 7 captures. Stage 2: 6 captures. Stage 3: 35 captures (31 admitted or qualified, 4 NOT_ADMITTED: one JavaScript shell, three NS refusal pages), 11 gaps (NS statutes, PE, YT, NU). Stage 4: 8 captures (Indian Act and First Nations Land Registry Regulations shared with Stage 1). Stage 5: 1 capture, 4 gaps.
