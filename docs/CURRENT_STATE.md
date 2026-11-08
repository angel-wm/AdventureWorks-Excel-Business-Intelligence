# Current State

**Reviewed:** 2026-11-08. This is a dated snapshot. Jira is authoritative for live work status; Git and GitHub establish publication.

## Delivered artifact

`AdventureWorks-BI.xlsx` contains the sales/customer dashboards, shipped sales/units/orders/AOV, fixed-window customer RFM and a fixed-volume sales scenario. Its structure is 20 sheets (17 visible), 9 query loads, 7 model tables, 6 active relationships, 5 PivotTables and 10 charts. [Architecture](ARCHITECTURE.md) explains dependencies; [Handoff](HANDOFF.md) identifies the exact workbook and current control layout.

The [business review](BUSINESS_REVIEW.md) adds reproducible order-entry-method, complete-year volume and person/store comparisons using the existing seven files. It is a fixed-source report, not an extra workbook slicer or model measure. The [audit closure](validation/2026-11-08-audit-closure.md) records the 14-point disposition. The later [verifier hardening](validation/2026-11-08-verifier-hardening.md) adds complete saved-output population checks and executable regression tests without changing the workbook.

## Acceptance and current work

| Work | Recorded state |
| --- | --- |
| Phase 1 — [AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2) | Done on 2026-11-06 |
| Phase 2 — [AWBI-3](https://angel231995.atlassian.net/browse/AWBI-3) | Done on 2026-11-06 |
| Phase 3 — [AWBI-4](https://angel231995.atlassian.net/browse/AWBI-4) | Done on 2026-11-07 |
| Phase 4 — [AWBI-5](https://angel231995.atlassian.net/browse/AWBI-5) | Done on 2026-11-08, with accepted coverage boundaries |
| Audit follow-up — [AWBI-21](https://angel231995.atlassian.net/browse/AWBI-21) | Done on 2026-11-08 after version-linked review of published `431284a` |
| Verifier maintenance — [AWBI-22](https://angel231995.atlassian.net/browse/AWBI-22) | 29 regression tests and full verifier v2 PASS; current publication/acceptance status belongs to the live issue |

Original phase acceptance was performed by the project assistant. The owner later reported completing a human workbook review; this does not imply independent repetition of each technical check. Subsequent fixes do not retrospectively change the earlier test baselines. Use the [evidence index](validation/README.md) to distinguish them.

## Published artifact and later maintenance

The owner published the 14-point audit corrections in [commit 431284a](https://github.com/angel-wm/AdventureWorks-Excel-Business-Intelligence/commit/431284ac4cfd255a8082a36b88cff1951f0d61a8). Local HEAD and public GitHub `main` were verified at that commit on 2026-11-08 before the later verifier maintenance. Commit `30b4ea8f37e3ee6ab3ba1af6260708591ee00ac4` is the earlier audit baseline.

The designated workbook is **AWBI-2026-11-08-audit-closure**, identified by [handoff.json](handoff.json) and published in commit `431284a`. The subsequent verifier, test and documentation maintenance leaves its bytes unchanged. Its own checks and publication boundary are recorded in the [maintenance evidence](validation/2026-11-08-verifier-hardening.md); the owner performs Git commits. No tag or GitHub Release is required or claimed.

## Maintained decisions

The owner accepted original amounts with currency unconfirmed and no conversion as a closed source limitation on 2026-11-08. Return adjustments are excluded, historical margin is unavailable, RFM remains descriptive across mixed person/store populations, and broader portability/source/filter checks remain outside accepted coverage. These decisions, their rationale and optional KPI dispositions are maintained in [Scope decisions](DECISIONS.md), not as an open implementation backlog here.

[AI Workflow](AI_WORKFLOW.md) records exercised tools and failed routes. [Validation Plan](VALIDATION_PLAN.md) records coverage rather than blanket verification.
