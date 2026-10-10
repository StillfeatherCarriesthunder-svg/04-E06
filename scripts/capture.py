#!/usr/bin/env python3
"""Capture one source into a job's evidence ledger (jobs/<ID>/evidence/).

Fetches the source, saves the exact bytes, computes SHA-256, writes a plain-text
derivative for cheap searching, lists currency-date candidates found in the text,
and appends one CAPTURE record to evidence/ledger.jsonl.

The script never confirms a currency date. It only lists candidates. The Worker
reads the source and confirms the date with scripts/ledger.py annotate.

Usage:
  python scripts/capture.py URL --source-id FHRMIRA --stage 1 2 --kind statute
  python scripts/capture.py URL --source-id NB-ROC --stage 4 --kind rules --browser
  python scripts/capture.py URL --source-id CASE-2019-ONSC-1234 --stage 6 --kind case \
      --from-file inbox/stage6/2019-ONSC-1234.pdf

--from-file ingests a file the operator saved in their own browser from URL. The
file is copied into evidence/raw (the original is left in place) and the record
marks it retrieved_by=operator.
"""
import argparse
import datetime
import hashlib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _job import job_root  # noqa: E402

ROOT = job_root()  # jobs/<ID>/, from --job
RAW_DIR = ROOT / "evidence" / "raw"
TEXT_DIR = ROOT / "evidence" / "text"
LEDGER = ROOT / "evidence" / "ledger.jsonl"
DOMAINS = ROOT / "gate" / "source_domains.json"

USER_AGENT = "Mozilla/5.0 (compatible; UAEP-source-capture/1.0; operator-run legal research)"
KINDS = ["statute", "regulation", "rules", "case", "gazette", "first-nation-law", "agreement", "guidance", "registry", "official-other"]

DATE = r"(\d{4}-\d{2}-\d{2}|[A-Z][a-z]+\.? \d{1,2},? \d{4}|\d{1,2} [A-Z][a-z]+ \d{4})"
CURRENCY_PATTERNS = [
    ("current_to", r"[Cc]urrent\s+to\s*[:\-]?\s*" + DATE),
    ("current_as_of", r"[Cc]urrent\s+(?:as\s+of|as\s+at)\s*[:\-]?\s*" + DATE),
    ("consolidated_to", r"[Cc]onsolidat\w*\s+(?:to|as\s+of|up\s+to)\s*[:\-]?\s*" + DATE),
    ("last_amended", r"[Ll]ast\s+amended\s+(?:on\s+)?[:\-]?\s*" + DATE),
    ("point_in_time", r"[Pp]oint[\s\-]in[\s\-]time\s*[:\-]?\s*" + DATE),
    ("in_force", r"[Ii]n\s+force\s+(?:on|as\s+of|from)\s*[:\-]?\s*" + DATE),
    ("decision_date", r"[Dd]ate\s*(?:of\s+decision|:)\s*" + DATE),
]


class TextExtractor(HTMLParser):
    """Strip HTML to readable text. Skips script and style blocks."""

    BLOCK = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
             "section", "article", "dt", "dd", "table", "blockquote"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.skip += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self.skip:
            self.skip -= 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def text(self):
        raw = "".join(self.parts)
        lines = [re.sub(r"[ \t ]+", " ", ln).strip() for ln in raw.splitlines()]
        out, blank = [], False
        for ln in lines:
            if ln:
                out.append(ln)
                blank = False
            elif not blank:
                out.append("")
                blank = True
        return "\n".join(out).strip() + "\n"


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc)


def fetch_http(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return {
            "bytes": resp.read(),
            "final_url": resp.geturl(),
            "http_status": resp.status,
            "content_type": resp.headers.get("Content-Type", ""),
            "method": "http_raw",
        }


def fetch_browser(url, timeout):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("ERROR: --browser needs Playwright. Install with:\n"
                 "  pip install playwright\n  python -m playwright install chromium")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent=USER_AGENT)
        resp = page.goto(url, wait_until="networkidle", timeout=timeout * 1000)
        html = page.content()
        final_url = page.url
        browser.close()
    return {
        "bytes": html.encode("utf-8"),
        "final_url": final_url,
        "http_status": resp.status if resp else None,
        "content_type": "text/html; charset=utf-8 (browser-rendered DOM)",
        "method": "browser_rendered",
    }


def read_operator_file(path_str, url):
    """Read a file the operator saved from URL in their own browser."""
    path = Path(path_str)
    if not path.is_absolute():
        path = ROOT / path  # relative to the job folder
    if not path.is_file():
        sys.exit(f"ERROR: --from-file {path_str} not found. Nothing written.")
    suffix = path.suffix.lower()
    content_type = {
        ".pdf": "application/pdf",
        ".html": "text/html",
        ".htm": "text/html",
        ".txt": "text/plain",
        ".xml": "application/xml",
    }.get(suffix)
    if content_type is None:
        sys.exit(f"ERROR: --from-file supports .pdf, .html, .htm, .txt, .xml; got '{suffix}'. Nothing written.")
    mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime, datetime.timezone.utc)
    return {
        "bytes": path.read_bytes(),
        "final_url": url,
        "http_status": None,
        "content_type": content_type + " (operator-saved file)",
        "method": "operator_saved_file",
        "operator_file": path.name,
        "operator_file_mtime_utc": mtime.isoformat(),
    }


def extension_for(content_type, url):
    ct = content_type.lower()
    if "pdf" in ct or url.lower().endswith(".pdf"):
        return ".pdf"
    if "xml" in ct or url.lower().endswith(".xml"):
        return ".xml"
    if "html" in ct:
        return ".html"
    if "text/plain" in ct:
        return ".txt"
    return ".bin"


def decode(data, content_type):
    m = re.search(r"charset=([\w\-]+)", content_type, re.I)
    for enc in ([m.group(1)] if m else []) + ["utf-8", "cp1252", "latin-1"]:
        try:
            return data.decode(enc)
        except (LookupError, UnicodeDecodeError):
            continue
    return data.decode("utf-8", errors="replace")


def to_text(data, ext, content_type):
    if ext in (".html", ".xml"):
        parser = TextExtractor()
        parser.feed(decode(data, content_type))
        return parser.text(), None
    if ext == ".txt":
        return decode(data, content_type), None
    if ext == ".pdf":
        try:
            import io
            from pypdf import PdfReader
        except ImportError:
            return None, "pypdf not installed; no text derivative (pip install pypdf)"
        reader = PdfReader(io.BytesIO(data))
        pages = []
        for i, page in enumerate(reader.pages, start=1):
            pages.append(f"\n===== PDF PAGE {i} =====\n{page.extract_text() or ''}")
        return "".join(pages).strip() + "\n", None
    return None, "no text extractor for this content type"


def currency_candidates(text, limit=12):
    found, seen = [], set()
    for label, pattern in CURRENCY_PATTERNS:
        for m in re.finditer(pattern, text):
            key = (label, m.group(1))
            if key in seen:
                continue
            seen.add(key)
            start, end = max(0, m.start() - 60), min(len(text), m.end() + 60)
            found.append({
                "label": label,
                "date": m.group(1),
                "context": re.sub(r"\s+", " ", text[start:end]).strip(),
            })
            if len(found) >= limit:
                return found
    return found


ISSUER_TYPES = ["federal", "provincial", "territorial", "court", "first_nation",
                "indigenous_body", "intergovernmental", "other"]


def main():
    ap = argparse.ArgumentParser(description="Capture one source into the evidence ledger.")
    ap.add_argument("url")
    ap.add_argument("--source-id", required=True,
                    help="Stable ID for this source, e.g. FHRMIRA, INDIAN-ACT, NB-ROC")
    ap.add_argument("--stage", nargs="+", type=int, required=True, choices=range(1, 7),
                    help="Research stage numbers (1-6) this source serves")
    ap.add_argument("--kind", required=True, choices=KINDS)
    ap.add_argument("--browser", action="store_true",
                    help="Render with headless Chromium (for JavaScript sites)")
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--note", default="")
    ap.add_argument("--issuer", default=None,
                    help="Body that issued the source. Required when the site is not in gate/source_domains.json")
    ap.add_argument("--issuer-type", default=None, choices=ISSUER_TYPES,
                    help="Kind of issuing body. Required when the site is not in gate/source_domains.json")
    ap.add_argument("--from-file", metavar="PATH",
                    help="Ingest a file the operator saved in their own browser from URL, instead of fetching")
    args = ap.parse_args()
    if args.from_file and args.browser:
        sys.exit("ERROR: use --from-file or --browser, not both")

    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._\-]*", args.source_id):
        sys.exit("ERROR: --source-id may use letters, digits, '.', '_' and '-' only")

    host = (urllib.parse.urlsplit(args.url).hostname or "").lower()
    if not host:
        sys.exit(f"REFUSED: no host in URL {args.url!r}")
    domains = json.loads(DOMAINS.read_text(encoding="utf-8")) if DOMAINS.exists() else {}
    known = set(domains.get("official", [])) | set(domains.get("case_reporters", []))
    if host not in known and not (args.issuer and args.issuer_type):
        sys.exit(f"REFUSED: {host} is not a known official site in gate/source_domains.json. "
                 f"State who issued the source with --issuer NAME --issuer-type TYPE. Nothing written.")
    domain_class = ("official" if host in domains.get("official", []) else
                    "case_reporter" if host in domains.get("case_reporters", []) else
                    "ISSUER_STATED")

    retrieved = utc_now()
    if args.from_file:
        result = read_operator_file(args.from_file, args.url)
    else:
        result = None
    try:
        if result is None:
            result = fetch_browser(args.url, args.timeout) if args.browser else fetch_http(args.url, args.timeout)
    except urllib.error.HTTPError as e:
        sys.exit(f"CAPTURE FAILED: HTTP {e.code} for {args.url}. Nothing written. "
                 f"Retry with --browser, or record a gap with scripts/ledger.py gap.")
    except Exception as e:  # network, TLS, timeout, browser errors
        sys.exit(f"CAPTURE FAILED: {type(e).__name__}: {e}. Nothing written. "
                 f"Record a gap with scripts/ledger.py gap if retrieval cannot be restored.")

    data = result["bytes"]
    if not data:
        sys.exit("CAPTURE FAILED: empty response body. Nothing written.")

    digest = hashlib.sha256(data).hexdigest()
    stamp = retrieved.strftime("%Y%m%dT%H%M%SZ")
    capture_id = f"CAP-{stamp}-{digest[:8]}"
    ext = extension_for(result["content_type"], result["final_url"])

    raw_path = RAW_DIR / args.source_id / f"{stamp}_{digest[:12]}{ext}"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    if raw_path.exists():
        sys.exit(f"ERROR: {raw_path} already exists; refusing to overwrite evidence.")
    raw_path.write_bytes(data)

    text, text_warning = to_text(data, ext, result["content_type"])
    text_rel, text_digest, candidates = None, None, []
    if text is not None:
        text_path = TEXT_DIR / args.source_id / f"{stamp}_{digest[:12]}.txt"
        text_path.parent.mkdir(parents=True, exist_ok=True)
        text_bytes = text.encode("utf-8")
        text_path.write_bytes(text_bytes)
        text_rel = text_path.relative_to(ROOT).as_posix()
        text_digest = "sha256:" + hashlib.sha256(text_bytes).hexdigest()
        candidates = currency_candidates(text)

    record = {
        "record_type": "CAPTURE",
        "capture_id": capture_id,
        "source_id": args.source_id,
        "stages": sorted(set(args.stage)),
        "kind": args.kind,
        "requested_url": args.url,
        "final_url": result["final_url"],
        "domain_class": domain_class,
        "host": host,
        "issuer": args.issuer,
        "issuer_type": args.issuer_type,
        "http_status": result["http_status"],
        "content_type": result["content_type"],
        "method": result["method"],
        "retrieved_utc": retrieved.isoformat(),
        "retrieved_by": "operator" if result["method"] == "operator_saved_file" else "worker_tool",
        "operator_file": result.get("operator_file"),
        "operator_file_mtime_utc": result.get("operator_file_mtime_utc"),
        "sha256": "sha256:" + digest,
        "bytes": len(data),
        "raw_path": raw_path.relative_to(ROOT).as_posix(),
        "text_path": text_rel,
        "text_sha256": text_digest,
        "text_warning": text_warning,
        "currency_candidates": candidates,
        "currency_date_confirmed": None,
        "note": args.note,
    }
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"CAPTURED {capture_id}")
    print(f"  source   {args.source_id}  stages {record['stages']}  kind {args.kind}")
    print(f"  method   {result['method']}  HTTP {result['http_status']}  {len(data)} bytes")
    print(f"  final    {result['final_url']}")
    print(f"  sha256   {digest}")
    print(f"  raw      {record['raw_path']}")
    print(f"  text     {text_rel or 'NONE: ' + str(text_warning)}")
    if candidates:
        print("  currency candidates (UNCONFIRMED - read the source, then annotate):")
        for c in candidates:
            print(f"    [{c['label']}] {c['date']}  ...{c['context']}...")
    else:
        print("  currency candidates: none found - locate the currency date manually")
    if result["method"] == "browser_rendered":
        print("  NOTE: hash covers the rendered DOM, not the server's original bytes.")
    if result["method"] == "operator_saved_file":
        print(f"  NOTE: operator-saved file '{result['operator_file']}' (saved {result['operator_file_mtime_utc']}).")
        print("        Hash covers the saved file; retrieval time above is ingest time, not the operator's download time.")


if __name__ == "__main__":
    main()
