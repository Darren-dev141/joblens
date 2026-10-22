# JobLens — Is this job posting still real?

**In one breath:** JobLens checks whether a job posting is still real. It follows each listing back to the employer's own website and writes down what it finds — a working apply link, an expired post, or an honest "couldn't verify." Missing evidence is never dressed up as proof of a fake job.

**Live demo:** the dashboard in this repo (`index.html`) runs entirely in your browser — no server, no tracking, works offline. Open it and click any posting to see its full evidence trail.

## What the pilot found (10 postings, October 22, 2026)

| Evidence class | Count | Meaning |
|---|---|---|
| Employer apply link observed | 2 / 10 | The employer's own site had a live apply path at snapshot time |
| Expired on the board | 1 / 10 | The job board itself marked the post expired |
| Employer requisition unavailable | 1 / 10 | No matching requisition found on the employer's system |
| Employer match, apply unresolved | 2 / 10 | Employer listing/index matched; the apply flow could not be confirmed |
| Employer status unresolved | 4 / 10 | Not enough employer-side evidence to classify — reported as unverified |

Half the sample (5 of 10 rows) was independently re-checked by a second reviewer against the original sources. One row stays **unverified** even though a third-party board showed it live, because the employer's own portal never resolved — that discipline is the point of the tool.

## How it works

1. **Collect** — postings are recorded with source URL and timestamp.
2. **Trace** — each posting is followed to the employer's own careers system (the board's word is never taken at face value).
3. **Classify** — deterministic evidence classes (above), never vibes: a posting is only called expired when the board or employer says so.
4. **Show the trail** — every row in the dashboard opens its sources and observer notes; the full dataset exports to CSV.

## What's in this repo

- `index.html` — the standalone dashboard (dark edition): search, evidence-status filters, per-posting evidence trail, CSV export. Zero dependencies.
- `joblens-v1.1-light-original.html` — the original light-theme v1.1 file, preserved as shipped.
- `RELEASE-NOTES-v1.1.md` — provenance, classification detail, and the release gate this snapshot passed.

## Honest limitations

- The pilot sample is small and nonrandom (10 postings, one metro area, one day). It demonstrates a method, not a job-market statistic.
- Classifications are a snapshot as of October 22, 2026 — "apply link observed" means observed then, not live now.
- The companion Python CLI (collector/classifier) was tested by its author (13/13 unit tests, headless-browser smoke) but is not part of this repo snapshot; the dashboard and its embedded dataset are the independently reviewed artifact — a second reviewer re-checked the data and executed the shipped app independently.

## Skills demonstrated

Python · Data validation · Evidence auditing · HTML / CSS / JavaScript · Dashboard design · Technical writing

---

Built by **Darren Foote** — Information Systems (UMBC, 2026); data analysis, CRM and automation work at Constellation Energy. JobLens grew out of a real job search: when you're applying every day, knowing which postings are still real is worth real hours.
