# JobLens — Release Notes v1.2.1 (visual polish)

October 27, 2026. A cosmetic-only pass over the v1.2 dashboard. Every dataset,
every number, every line of copy, and all behavior are exactly as shipped in
v1.2 — this release changes how the page looks, not what it says.

## What changed

- `index.html` — one addition: a `polish-v121` style block layered after the
  existing light base and dark-edition stylesheets. Nothing else in the file
  was edited; the diff against v1.2 is the inserted block only.
  - **Typography** — antialiased text rendering, a 1.55 base line-height,
    looser intro leading, and tabular numerals for the stat figures,
    result counts, and bar values so columns of numbers align.
  - **Spacing rhythm** — panel headers, filter rows, ledger rows, and the
    detail panel now share a consistent 24px horizontal grid; stat cards
    and section gaps rebalanced to match.
  - **Header treatment** — the sidebar gains a hairline right border and a
    soft shadow on the brand mark; the top bar is closed off with a
    hairline rule; non-active nav items get a hover state.
  - **Stat cards** — softer depth (inset top highlight plus a low shadow),
    and the lead card carries a 2px green top accent.
  - **Controls** — buttons and inputs share a 10px radius, transitions on
    hover/focus, a defined focus border on search and the status selector,
    and a muted placeholder color.
  - **List readability** — ledger rows get slightly more air and smoother
    hover transitions; the ledger and detail panes get thin, theme-matched
    scrollbars.
  - **Accessibility** — a green text-selection color, and all transitions
    are disabled under `prefers-reduced-motion`.
- `RELEASE-NOTES-v1.2.1.md` — this file.
- Unchanged: both datasets and all scripts in `index.html`, `README.md`,
  `RELEASE-NOTES-v1.2.md`, `RELEASE-NOTES-v1.1.md`,
  `joblens-v1.1-light-original.html`, `tools/build_feed_dataset.py`.

## Constraints held

- Vanilla CSS only, inside the same single self-contained HTML file.
  No frameworks, no CDN webfonts (system font stack, as before), no
  external assets, no new dependencies.
- No layout structure changes; the existing responsive breakpoints are
  untouched apart from padding values inside the ≤760px block, and the
  print stylesheet is unaffected.
- No personal identifiers added (none exist in the page).

## Verification performed for this release

- Diff of the polished `index.html` against the pushed v1.2 file: additions
  only — the single style block. Data payload and scripts byte-identical.
- The scripted DOM smoke from the v1.2 release (jsdom: both datasets
  render 80/10, tab switching, search narrowing and reset, row-click
  detail, status filter, reviewed-only filter, verbatim evidence note) —
  21/21 checks pass against the polished file.
- The live GitHub Pages demo was fetched after the push and byte-compared
  against the pushed file — result in the release report; Pages can lag a
  push by a few minutes.
