# JobLens — Is this job posting still real?

**In one breath:** JobLens checks whether a job posting is still real. It follows each listing back to the employer's own website and writes down what it finds — a working apply link, an expired post, or an honest "couldn't verify." Missing evidence is never dressed up as proof of a fake job.

**Live demo:** the dashboard in this repo (`index.html`) runs entirely in your browser — no server, no tracking, works offline. It now carries two datasets: the pipeline's current verified feed and the founding hand audit. Click any posting to see its evidence trail.

## Where it stands (October 27, 2026)

What began as a 10-posting hand audit is now a running verification pipeline behind a real job search. Every figure below is counted from the pipeline's own files — the file and date are named with each number, because that is the whole point of the tool.

| Figure | Count | Source |
|---|---|---|
| Postings screened & classified | **1,510** | Master list, October 26, 2026 |
| — verified open on the employer's own page | 22 | Master list status counts |
| — not yet checked / unverifiable / excluded / dead | 1,298 / 101 / 83 / 6 | Master list status counts |
| Verified live in the current feed | **80** | Feed refresh Run 55, October 27, 2026 |
| Applications with a confirmed submission | **187** of 232 recorded | Application ledger snapshot, October 25, 2026 |

The feed's churn is part of the evidence: at the Run 55 refresh, 4 postings carried in the previous feed were absent from their employers' open lists and were dropped, and 4 new verified postings took their place.

The application ledger is kept under the same discipline. Of its 232 records, 158 are stamped confirmed and 29 confirmed-then-rejected (a rejection is an employer's answer to a submitted application — the confirmation text is in the ledger). The remaining 45 are **not** counted as confirmed applications here: 27 are recorded as unconfirmed, 3 as incomplete, and 15 carry no outcome stamp. (The ledger snapshot predates the feed by two days; applications submitted after October 25 are not in this file and are not in this count.)

## The current feed (80 postings, October 27, 2026)

Each feed record was re-verified at the employer's own source during the Run 55 refresh:

- **78 postings** — employer's ATS open-list API (Greenhouse / Ashby / Lever / SmartRecruiters) contains the posting ID with a matching title.
- **2 postings** — employer's own posting page opened live with title match and an apply path (employers not on an open-list API).

The verification note recorded by the pipeline is shown verbatim in each record's evidence trail. Feed records are machine-verified; none are independently human-reviewed — a different evidence class from the founding audit, and the dashboard labels them as such.

## The founding pilot (10 postings, October 22, 2026)

| Evidence class | Count | Meaning |
|---|---|---|
| Employer apply link observed | 2 / 10 | The employer's own site had a live apply path at snapshot time |
| Expired on the board | 1 / 10 | The job board itself marked the post expired |
| Employer requisition unavailable | 1 / 10 | No matching requisition found on the employer's system |
| Employer match, apply unresolved | 2 / 10 | Employer listing/index matched; the apply flow could not be confirmed |
| Employer status unresolved | 4 / 10 | Not enough employer-side evidence to classify — reported as unverified |

Half the sample (5 of 10 rows) was independently re-checked by a second reviewer against the original sources. One row stays **unverified** even though a third-party board showed it live, because the employer's own portal never resolved — that discipline is the point of the tool. The pilot dataset is preserved in the dashboard exactly as shipped, next to the feed.

## How it works

1. **Collect** — postings are recorded with source URL and timestamp.
2. **Trace** — each posting is followed to the employer's own careers system (the board's word is never taken at face value).
3. **Classify** — deterministic evidence classes (above), never vibes: a posting is only called expired when the board or employer says so, and only called live when the employer's own system says so.
4. **Show the trail** — every row in the dashboard opens its sources and observer notes; the displayed dataset exports to CSV.
5. **Re-verify or drop** — the feed is rebuilt every refresh; a posting that stops verifying is removed, and the removal is recorded.

## What's in this repo

- `index.html` — the standalone dashboard (dark edition): two datasets (verified feed + founding audit), search, evidence-status filters, per-posting evidence trail, CSV export. Zero dependencies.
- `joblens-v1.1-light-original.html` — the original light-theme v1.1 file, preserved as shipped.
- `RELEASE-NOTES-v1.1.md` — provenance, classification detail, and the release gate the founding snapshot passed.
- `RELEASE-NOTES-v1.2.md` — what changed in this update, where every number came from, and how the feed dataset was built.
- `RELEASE-NOTES-v1.2.1.md` — the CSS-only visual polish pass; data and behavior unchanged.
- `tools/build_feed_dataset.py` — the generator that converts a pipeline feed snapshot into the dashboard's feed dataset. Every field is copied or mechanically derived from the snapshot; nothing is hand-entered.

## Honest limitations

- The founding pilot sample is small and nonrandom (10 postings, one metro area, one day). It demonstrates a method, not a job-market statistic.
- The feed is a snapshot as of the Run 55 refresh (October 27, 2026) — "verified live" means verified then. Four of the previous feed's 80 postings were already gone by this refresh; expect the same churn after it.
- The master-list counts describe one person's search funnel (one metro focus, one profile), not the job market.
- The companion Python CLI (collector/classifier) was tested by its author (13/13 unit tests, headless-browser smoke) but is not part of this repo snapshot; the dashboard and its embedded datasets are the reviewed artifact — a second reviewer re-checked the founding data and executed the shipped app independently.

## Skills demonstrated

Python · Data validation · Evidence auditing · HTML / CSS / JavaScript · Dashboard design · Technical writing

---

Built by **Darren Foote** — Information Systems (UMBC, 2026); data analysis, CRM and automation work at Constellation Energy. JobLens grew out of a real job search: when you're applying every day, knowing which postings are still real is worth real hours.
