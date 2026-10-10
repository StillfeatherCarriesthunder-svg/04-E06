# 04-E06 — Search log (job 04-E06-ACQ-2026-10-10)

Candidate 04-E06 stays CANDIDATE / UNACTIVATED. Every search and fetch in this job is logged here, with every excluded source and its reason. Times are UTC. Search results locate sources only; they are not evidence.

## SEARCH AND FETCH LOG

| # | UTC | tool | query or URL | result |
|---|---|---|---|---|
| 1 | 2026-10-10T11:42:42Z | capture.py (http) | https://laws-lois.justice.gc.ca/eng/acts/I-5/FullText.html | FAILED: egress proxy refused CONNECT (403, connect_rejected). Nothing written. |
| 2 | 2026-10-10T11:43Z | curl HEAD probe | https:// root of laws.justice.gc.ca, www.sac-isc.gc.ca, www.rcaanc-cirnac.gc.ca, gazette.gc.ca, www.canlii.org, decisions.scc-csc.ca, laws.gnb.ca, www.ontario.ca, fng.ca | All refused by egress proxy (CONNECT 403). github.com reachable. Reachability probe only; nothing captured. |
| 3 | 2026-10-10T11:44Z | WebFetch | https://laws-lois.justice.gc.ca/eng/acts/I-5/FullText.html | FAILED: getaddrinfo ENOTFOUND. Locate-only tool; would not be evidence. |
| 4 | 2026-10-10T11:44Z | WebSearch | Indian Estates Regulations C.R.C., c. 954 laws-lois.justice.gc.ca | Located issuer URLs: /eng/regulations/C.R.C.,_c._954/FullText.html (laws-lois and laws mirrors), PDF at laws.justice.gc.ca/PDF/C.R.C.,_c._954.pdf, point-in-time index. Snippets report conflicting "current to" dates; not relied on. |

## EXCLUDED

| source | reason |
|---|---|
| (none yet) | |
