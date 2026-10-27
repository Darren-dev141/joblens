# JobLens — Release Notes v1.2 (dashboard update)

October 27, 2026. This update brings the public dashboard current with what the
JobLens pipeline has actually done since the v1.1 founding snapshot
(October 22, 2026). The founding dataset is unchanged — byte-for-byte the same
records — and now sits next to the pipeline's current output.

## What changed

- `index.html` — the dashboard now carries two datasets behind a selector:
  - **Verified feed — Oct 27, 2026 (80 records, default view).** The pipeline's
    current verified-live postings, each with the employer's own posting URL
    and the pipeline's verification note shown verbatim as its evidence trail.
  - **Founding audit — Oct 22, 2026 (10 records).** The original hand audit,
    preserved exactly as shipped in v1.1, including its classifications and
    independent-review marks.
  - Headline stat boxes now show pipeline figures (below) instead of
    pilot-only numbers. The founding audit's own stats remain visible inside
    its dataset view (method panel and bars).
  - CSV export follows the selected dataset.
- `README.md` — rewritten around the pipeline's current state; the founding
  pilot keeps its own labeled section.
- `tools/build_feed_dataset.py` — new. The generator that produced the feed
  dataset from the pipeline's feed snapshot (see Data sources).
- `RELEASE-NOTES-v1.2.md` — this file.
- Unchanged: `joblens-v1.1-light-original.html`, `RELEASE-NOTES-v1.1.md`.

## Headline numbers and where each came from

Every number in the dashboard and README was counted from a pipeline file at
build time; nothing was estimated or carried over from a summary.

| Figure | Value | Counted from |
|---|---|---|
| Postings screened & classified | 1,510 unique after dedupe (22 verified open · 1,298 not yet checked · 101 unverifiable · 83 excluded · 6 dead) | Master list header counts, `MASTER-LIST-2026-10-26.md` (Oct 26, 2026); status counts sum to the total |
| Verified live in current feed | 80 | Feed snapshot written by refresh Run 55, completed Oct 27, 2026 (`step3_after.json`: `live_count` 80, 80 entries, all status `live`) |
| Feed verification routes | 78 via employer ATS open-list API · 2 via employer page + apply path | Derived per record from each entry's own `verification_note` in that snapshot (route phrases matched mechanically by the generator) |
| Feed churn at Run 55 | 4 added · 4 archived | The snapshot's own `last_refresh` record |
| Applications with confirmed submission | 187 of 232 ledger records | Application ledger `applied_auto.json` (snapshot Oct 25, 2026): 158 entries stamped `confirmed` + 29 stamped `rejected` whose entries carry submission-confirmation text; the other 45 (27 `unconfirmed`, 3 `incomplete`, 15 unstamped) are disclosed, not counted |

Known staleness, stated rather than smoothed over: the ledger snapshot is from
October 25 and the master list from October 26, while the feed is from
October 27. Each figure is labeled with its own date in the dashboard.

## How the feed dataset was built

`tools/build_feed_dataset.py` converts a pipeline feed snapshot into the
dashboard's record shape:

- Copied verbatim: title, employer, location, pay, work mode, employment
  type, discovery source, employer posting URL, and the verification note
  (as the record's evidence finding).
- Derived mechanically: the verification route (from the note's wording),
  and the requisition ID (extracted from the note when the note itself
  records one — 77 of 80 records; the other 3 show "Not stated").
- Feed records carry `independently_reviewed: false` semantics by design:
  they are machine-verified, and the dashboard says so wherever the founding
  audit claims human review.

## Privacy

The public update contains job-posting data only (titles, employers,
locations, pay as posted, and public employer posting URLs). It contains no
personal identifiers — no street address, no phone number, no GPA, no email.
The feed snapshot was scanned for identifier patterns before conversion; the
single pattern hit was a digit sequence inside a public Greenhouse posting
ID, not personal data.

## Verification performed for this release

- Founding dataset in the new file is deep-equal to the v1.1 dataset
  (parsed and compared programmatically — identical).
- Both inline scripts pass `node --check`.
- A scripted DOM smoke of the updated page (jsdom: both datasets render,
  tab switching, search, status filter, reviewed-only filter, detail
  panel, verbatim evidence note) — 21/21 checks pass. (A Chromium
  headless `--dump-dom` run was attempted in the build sandbox and hung;
  the jsdom run is the executed smoke of record.)
- The live GitHub Pages demo was fetched after the push and checked for the
  new dataset (80 feed records / Run 55 markers) — result in the release
  report; Pages can lag a push by a few minutes.
