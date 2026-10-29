#!/usr/bin/env python3
"""Build the JobLens dashboard's "verified feed" collection from a pipeline
feed snapshot (the JSON the JobLens verification pipeline writes after each
refresh run: {as_of, live_count, last_refresh, entries[]}).

Every dashboard field is copied or mechanically derived from the snapshot —
nothing is invented here:

- title / employer / location / pay / work mode / employment type: copied.
- posting_url: the entry's source_url (the employer's own ATS posting).
- evidence finding: the entry's verification_note, verbatim.
- verification_route: "ats_api" when the note records an open-list API check,
  "employer_page" when it records an employer page + apply-path check.
- requisition: extracted from the verification_note when the note itself
  records a posting ID; otherwise null (shown as "Not stated").

Usage: build_feed_dataset.py <feed_snapshot.json> <output.json>
"""
import json
import re
import sys

REQ_PATTERNS = [
    r"posting ID ([\w-]{6,})",
    r"Ashby ID ([\w-]{6,})",
    r"Greenhouse ID (\d{6,})",
    r"ID (\d{7,})",
]


def extract_requisition(note):
    for pat in REQ_PATTERNS:
        m = re.search(pat, note or "")
        if m:
            return m.group(1)
    return None


def build(snapshot):
    entries = snapshot["entries"]
    routes = {"ats_api": 0, "employer_page": 0}
    records = []
    for i, e in enumerate(entries, 1):
        note = e.get("verification_note") or ""
        # Notes that record an open-list API check are ats_api; everything
        # else is an employer page + apply-path check.
        route = "ats_api" if "open-list API" in note else "employer_page"
        routes[route] += 1
        verified = (e.get("verified_at") or snapshot["as_of"])[:10]
        records.append({
            "id": f"F{i:03d}",
            "title": e["title"],
            "employer": e["company"],
            "location": e["location"],
            "pay": e.get("pay"),
            "work_mode": e.get("work_mode"),
            "employment_type": e.get("employment_type"),
            "discovered_via": e.get("source_name"),
            "posting_url": e["source_url"],
            "requisition": extract_requisition(note),
            "first_seen_at": (e.get("first_seen_at") or "")[:10] or None,
            "verified_at": verified,
            "verification_route": route,
            "status": "FEED_LIVE",
            "status_label": "Verified live — employer source",
            "evidence": [{
                "signal": "employer_verified_live",
                "observer": "pipeline",
                "date": verified,
                "url": e["source_url"],
                "finding": note,
            }],
        })
    refresh = snapshot.get("last_refresh") or {}
    return {
        "dataset_id": f"VERIFIED-FEED-{snapshot['as_of'][:10]}",
        "dataset_title": "Verified live feed — postings confirmed open at the employer's own source",
        "collected_at": snapshot["as_of"],
        "scope": ("Every posting the JobLens pipeline currently carries as verified live: "
                  "each was re-checked against the employer's own ATS open list or careers "
                  "page at the last refresh. A snapshot — postings close, and this feed "
                  "drops them at the next refresh."),
        "collection_method": ("Automated verification pipeline (JobLens gate): postings are "
                              "accepted only on employer-side evidence — the employer's ATS "
                              "open-list API or the employer's own posting page with an apply "
                              "path. Board listings alone never count."),
        "refresh": {
            "completed_at": refresh.get("completed_at"),
            "added_count": refresh.get("added_count"),
            "archived_count": refresh.get("archived_count"),
            "message": refresh.get("message"),
        },
        "records": records,
        "metrics": {
            "total": len(records),
            "status_counts": {"FEED_LIVE": len(records)},
            "routes": routes,
        },
    }


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, out = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        snapshot = json.load(f)
    data = build(snapshot)
    # "<" is escaped so the JSON stays safe when embedded in an inline
    # <script> block: a posting title containing "</script>" or "<!--" cannot
    # end or alter the script element. The escaped text is still valid JSON.
    text = json.dumps(data, indent=1).replace("<", "\\u003c")
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {out}: {data['metrics']['total']} records, routes {data['metrics']['routes']}")


if __name__ == "__main__":
    main()
