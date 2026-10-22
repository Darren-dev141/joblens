# JobLens — Working Portfolio Delivery (v1.1; supersedes Jinxo file #761)
Oct 22, 2026, 2:05 PM Eastern. Owner directive message #33035; portfolio task #617 completed.

## Shipped artifact
JobLens is a **built, local author-tested** offline-first Python/vanilla JS project. Darren received in his current ChatGPT conversation: complete source ZIP, standalone interactive HTML dashboard, README with reproducible commands, provenance methodology, desktop/mobile screenshots, test log. ZIP not attached in Jinxo; **no room bot can claim independent code execution from this note**.

## Inputs, provenance, correction
Original collector evidence: room file #746, first 10 ranked HiringCafe Baltimore-area analyst source rows, nonrandom. Independent Fo source observations: room file #749, rows 1,3,4,7,8. Row7 explicitly marked expired on BOTH HiringCafe source pages by Fo; original U remains provenance; second URL is a linked *possible* duplicate, not certified unique req identity. See adjudication #33067 and Fo acceptance #33148.

## Exact evidence classification at observation, Oct 22, 2026
- Employer-authorized Apply link observed: **2 rows** (1 Blue Raster; 8 Nationals), independently source-reviewed.
- Source board explicitly marked expired: **1 row** (7 Robertson etc.), independently reviewed.
- Employer requisition URL/ID search unavailable: **1 row** (3 AES), independently reviewed.
- Employer listing/index match, Apply flow unresolved: **1 row** (2 Giant Food), collector-only.
- Historical employer-index evidence, current Apply unresolved: **1 row** (10 Highline Warren), collector-only.
- Employer application status unresolved: **4 rows** (4 Cherokee, 5 Booz Allen, 6 Global Skills X-Change, 9 HITT). **Row 4 is UNVERIFIED** despite Fo confirming a live *third-party* ClearanceJobs listing, because the employer Oracle portal never resolved.

Independent source review coverage: **5/10 source rows** (1,3,4,7,8). No inference of employer intent, no sample-representative job-fraud rate, no universal current availability. **Removed the misleading hardcoded '0 fabricated' pseudo-stat in v1.1; dashboard instead shows derived 4/10 employer-state unresolved.** No verified fabricated/fake listings claim is attempted.

## Actual software
- Python 3 standard-library CLI `python -m joblens audit|build|serve`, schema/url/evidence validator, deterministic classification, exact-requisition duplicate guard, snapshot metadata.
- Self-contained offline HTML/CSS/JS dashboard with evidence trail, source links, responsive layout, interactive search and category/reviewer filters, CSV export.
- Versioned 10-record JSON; docs methodology, README, MIT license; image screenshots.
- Author-run tests: **13/13 Python unit tests PASS**, headless Chromium UI smoke PASS for list/search/filter/detail/reviewer-only/CSV/mobile, zip integrity PASS. No external deployment, no independent code audit, no PC/accounts touched.

## Release gate
Fo completed **independent data/provenance reading** against #749 (#33158), with row4 taxonomy correction explained in #33165. This does NOT count as independent software replication. Once Darren transfers ZIP to this room, a separate tester must unpack, run commands, inspect output and security/privacy before any claim 'independently reproducible' or external publication. Public GitHub/LinkedIn change requires Darren's item-specific OK.