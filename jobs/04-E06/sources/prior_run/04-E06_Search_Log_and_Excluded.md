# 04-E06 — Search log and excluded sources

Candidate: 04-E06 (CANDIDATE / UNACTIVATED). Companion to `04-E06_Source_Register.csv`. All entries dated 2026-10-09.

## SEARCH_LOG

| query | date | sources found |
| --- | --- | --- |
| fetch: laws-lois.justice.gc.ca Indian Act page-6 | 2026-10-09 | Indian Act ss. 49-57 (page showed current to 2024-12-15; treated as stale) |
| fetch: laws-lois.justice.gc.ca Indian Act index | 2026-10-09 | none — site disallowed automated access to index |
| fetch: Indian Act page-5 | 2026-10-09 | ss. 48-55 → S03 |
| fetch: Indian Act page-4 | 2026-10-09 | ss. 29-47 → S02 |
| fetch: Indian Estates Regulations page-1 | 2026-10-09 | full regulations → S04 |
| fetch: Indian Act page-1 | 2026-10-09 | ss. 1-6 incl. s. 4(3) → S01 |
| Framework Agreement on First Nation Land Management Act laws-lois.justice.gc.ca | 2026-10-09 | FAFNLMA index and full text; repealed FNLMA point-in-time versions |
| fetch: FAFNLMA page-1 | 2026-10-09 | ss. 1-13 → S05 |
| Indigenous Services Canada estates wills First Nations sac-isc.gc.ca | 2026-10-09 | ISC Estate services page; band-hosted copies of ISC material; secondary articles |
| fetch: ISC Estate services | 2026-10-09 | full page → S08 |
| fetch: ISC Administering an Indian Act Estate | 2026-10-09 | none — site disallowed automated access |
| "Administering an Indian Act estate" general information for administrators sac-isc | 2026-10-09 | ISC booklet extract → S10; publications.gc.ca catalogue record; Legal Aid BC guide |
| sac-isc.gc.ca "Why is it important to have a will" First Nations reserve will kit | 2026-10-09 | ISC will page → S09; ISC 'Do you have a will?' page; community legal clinic will kit |
| fetch: FHRMIRA page-1 | 2026-10-09 | ss. 1-12 → S07 |
| New Brunswick Probate Court Act laws.gnb.ca | 2026-10-09 | Probate Court Act; Reg. 84-74; Reg. 2023-10 |
| fetch: laws.gnb.ca P-17.1 | 2026-10-09 | full Act → S11 |
| New Brunswick Rules of Court Rule 76 probate laws.gnb.ca | 2026-10-09 | Probate Rules 84-9; Rules of Court amendment regs |
| fetch: laws.gnb.ca 84-9, W-9, D-9 | 2026-10-09 | full texts → S12, S13, S14 |
| First Nations Gazette publication of First Nation laws fng.ca | 2026-10-09 | FNG Part II volumes; FNG publication policy 2023 |
| Indian Lands Registry System ILRS public search Indigenous Services Canada | 2026-10-09 | ISC Land Registration → S15; Registration Manual → S16; ILRS public site notice |
| fetch: ISC Land Registration | 2026-10-09 | full page → S15 |
| Lands Advisory Board land codes operational First Nations list labrc.com | 2026-10-09 | LAB pages; land codes collection; ISC/LAB MOU news release |
| Framework Agreement on First Nation Land Management consolidated version text | 2026-10-09 | third-party copies (NWAC, Treaty 1, Fort McKay, FAO); LABRC resource page |
| fetch: fng.ca | 2026-10-09 | home page → S17 |
| labrc.com Framework Agreement on First Nation Land Management PDF | 2026-10-09 | LABRC resource listing; LABRC summaries |
| Indian Act section 86 by-laws publication internet site First Nations Gazette | 2026-10-09 | Indian Act s. 86 → S19; Courthouse Libraries BC note; FNG policy |
| fetch: labrc.com/framework-agreement/ | 2026-10-09 | link to Dec 2022 agreement text → S06 |
| fetch: labrc.com/resource/land-codes/ | 2026-10-09 | land codes collection → S18 |
| Canard v. Attorney General of Canada 1976 SCR 170 Indian Act estate | 2026-10-09 | Réseau DIALOG summary; vLex headnote; Federal Court estate decision; Miller Thomson; All About Estates |
| fetch: allaboutestates.ca Estate Planning and the Indian Act | 2026-10-09 | secondary; cites Canard, Brooks 2022 FC 1064, FHRMIRA |
| scc-csc.lexum.com Attorney General of Canada v. Canard 1976 | 2026-10-09 | no issuer page returned |
| fetch: millerthomson.com Indian Act estates article | 2026-10-09 | secondary; cites Canard, Re Williams Estate, Earl, Dickson, Bonneau, Toney, self-government agreements |
| decisions.scc-csc.ca "Canard" Indian Act 1975 | 2026-10-09 | no issuer page returned |
| rcaanc-cirnac.gc.ca self-government agreements list | 2026-10-09 | CIRNAC Final Agreements index → S20; publications.gc.ca agreement records |
| fetch: CIRNAC Final Agreements index | 2026-10-09 | index page → S20 |
| fetch: decisions.scc-csc.ca date browse 1975 | 2026-10-09 | none — bot detection blocked request |
| "[1976] 1 S.C.R. 170" Canard scc-csc decisions | 2026-10-09 | no issuer page returned → S23 recorded with limit |
| fetch: gazette.gc.ca Part II index | 2026-10-09 | none — 404 |
| Royal Gazette New Brunswick online gnb.ca | 2026-10-09 | About the Royal Gazette → S22; issue PDFs |
| Canada Gazette Part II SOR/2024-280 Indian Estates Regulations amendment | 2026-10-09 | SOR/2024-280 → S21; Justice Laws amendment table |

Coverage: S1 7 rows, S2 3, S3 4, S4 8, S5 1.

Not searched in this run (possible gaps for the operator): First Nations Land Registry Regulations under the Framework Agreement regime; any NB-specific ISC estates contact or regional guidance; Federal Courts Rules for s. 47 appeals.

## EXCLUDED

| source | reason |
| --- | --- |
| ILRS / FNLRS public search interface (services.aadnc-aandc.gc.ca/ILRS_Public) | ISC states an account is needed to use the registries; gated. |
| Framework Agreement copies on NWAC, Treaty 1, Fort McKay, FAO (FAOLEX) sites | Not issuer copies; LABRC copy registered instead (S06). |
| First Nations Land Management Act, S.C. 1999, c. 24 (point-in-time versions) | Repealed and replaced December 2022 by FAFNLMA. Add only if activation fixes a pre-2023 period. |
| Westbank, Sioux Valley Dakota Nation and Tla'amin self-government agreements (named by Miller Thomson) | Nation-specific; operator selected no Nation. Index registered instead (S20). |
| Individual land codes within the LABRC collection | Nation-specific; operator selected no Nation. |
| Re Williams Estate (1960), 32 W.W.R. 686 (B.C.S.C.) | Named by Miller Thomson beside Canard; issuer copy not located; not verified. |
| Brooks v Canada (Indigenous Services), 2022 FC 1064 | Cited by a secondary blog for forum practice, not identified as settling which regime governs; not verified on issuer site. |
| Earl v. Canada, 2004 FC 897; Dickson (Estate of), 2012 YKSC 71 | Cited for the meaning of 'ordinarily resident', not identified as settling which regime governs. Candidate for operator decision. |
| Okanagan Indian Band v. Bonneau, 2003 BCCA 299; Toney v Toney Estate, 2018 NSSC 179 | Cited for intestacy and family-home points, not for which regime governs. |
| Federal Court estate-administrator decision (Longboat / Bomberry estates) | Concerns standard of review of ministerial estate decisions, not which regime governs. |
| R. v. Francis, [1988] 1 S.C.R. 1025 | NB case on provincial law on reserve generally; not an estates decision. |
| All About Estates, Miller Thomson, Réseau DIALOG, Clicklaw, Legal Aid BC guide, Hull & Hull, Anishinabek News | Secondary sources; used only as pointers. |
| vLex case pages | Login or trial gated. |
| Band-hosted copies of ISC material (lnib.net, fwfn.com, splatsin.ca) | Not issuer copies. |
| ISC 'Do you have a will?' page | Duplicates S09. |
| ISC estates management funding page | Funding program, not estates guidance. |
| NB Reg. 84-74 (judicial districts and probate offices) | Venue logistics only; schedule repealed 2023. |
| NB Rules of Court | Residual to Probate Rules (Rule 4.04); not separately verified. |
| NB Marital Property Act | Family-property statute outside the S3 list; cross-referenced from Devolution of Estates Act s. 22. Add if activation needs it. |
| publications.gc.ca catalogue record for the ISC booklet | Catalogue entry only; issuer page registered (S10). |
