# Current State

**Reviewed:** 2026-11-08. This is a dated snapshot. Jira is authoritative for live work status; Git and GitHub establish publication.

## Delivered artifact

`AdventureWorks-BI.xlsx` contains the sales/customer dashboards, shipped sales/units/orders/AOV, fixed-window customer RFM and a fixed-volume sales scenario. Its structure is 20 sheets (17 visible), 9 query loads, 7 model tables, 6 active relationships, 5 PivotTables and 10 charts. [Architecture](ARCHITECTURE.md) explains dependencies; [Handoff](HANDOFF.md) identifies the exact workbook and current control layout.

The [business review](BUSINESS_REVIEW.md) adds reproducible order-entry-method, complete-year volume and person/store comparisons using the existing seven files. It is a fixed-source report, not an extra workbook slicer or model measure. `scripts/verify.py` recomputes source expectations and checks saved outputs; current results and the 14-point disposition are in the [audit closure](validation/2026-11-08-audit-closure.md).

## Acceptance and current work

| Work | Recorded state |
| --- | --- |
| Phase 1 — [AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2) | Done on 2026-11-06 |
| Phase 2 — [AWBI-3](https://angel231995.atlassian.net/browse/AWBI-3) | Done on 2026-11-06 |
| Phase 3 — [AWBI-4](https://angel231995.atlassian.net/browse/AWBI-4) | Done on 2026-11-07 |
| Phase 4 — [AWBI-5](https://angel231995.atlassian.net/browse/AWBI-5) | Done on 2026-11-08, with accepted coverage boundaries |
| Audit follow-up — [AWBI-21](https://angel231995.atlassian.net/browse/AWBI-21) | Local implementation and checks complete; In Review pending owner commit, publication and version-linked acceptance |

Original phase acceptance was performed by the project assistant. The owner later reported completing a human workbook review; this does not imply independent repetition of each technical check. Subsequent fixes do not retrospectively change the earlier test baselines. Use the [evidence index](validation/README.md) to distinguish them.

## Local and published state

At the audit baseline, local HEAD and public GitHub `main` matched **30b4ea8f37e3ee6ab3ba1af6260708591ee00ac4**. The owner had authorized publication, and the repository was public. The follow-up workbook/document/script changes are local and uncommitted until the owner publishes them; no new commit, push, tag or GitHub Release is claimed by this record.

The exact designated local artifact is **AWBI-2026-11-08-audit-closure**, identified by the hash in [handoff.json](handoff.json). The containing commit will identify its immutable repository snapshot after the owner commits it. This avoids confusing the previous public workbook with the local corrected one.

## Maintained decisions

The owner accepted original amounts with currency unconfirmed and no conversion as a closed source limitation on 2026-11-08. Return adjustments are excluded, historical margin is unavailable, RFM remains descriptive across mixed person/store populations, and broader portability/source/filter checks remain outside accepted coverage. These decisions, their rationale and optional KPI dispositions are maintained in [Scope decisions](DECISIONS.md), not as an open implementation backlog here.

[AI Workflow](AI_WORKFLOW.md) records exercised tools and failed routes. [Validation Plan](VALIDATION_PLAN.md) records coverage rather than blanket verification.
