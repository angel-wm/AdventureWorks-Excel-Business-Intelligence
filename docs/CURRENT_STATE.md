# Current State

**Last reviewed:** 2026-11-07. This is a dated snapshot, not a live Jira or remote-publication feed.

## What exists

- The repository contains the project plan, source map, KPI definitions and validation guidance. It is intended for public portfolio use; local changes do not prove remote publication.
- Seven files from the selected Microsoft AdventureWorks OLTP revision have been downloaded and profiled locally. Their provenance, hashes and checks are in [initial sales load validation](validation/2026-11-06-initial-sales-load.md).
- `AdventureWorks-BI.xlsx` contains seven Power Query worksheet and Data Model loads and six active relationships. Source counts and category/territory PivotTable checks are recorded in [sales model validation](validation/2026-11-06-model-relationships.md). Shipped sales and units are checked in [AWBI-11 validation](validation/2026-11-07-awbi-11-prototype.md), and shipped orders and AOV in [AWBI-13 validation](validation/2026-11-07-awbi-13-orders-aov.md). An initial filterable sales view and chart are checked in [AWBI-14 validation](validation/2026-11-07-awbi-14-sales-view.md).
- A customer RFM base is implemented locally with a fixed sample cutoff; its scope and checks are in [AWBI-15 validation](validation/2026-11-07-awbi-15-customer-rfm.md). Fixed scores and descriptive segments are recorded in [AWBI-16 validation](validation/2026-11-07-awbi-16-rfm-segments.md).
- A fixed-volume sales scenario is implemented locally; its assumptions and checks are in [AWBI-17 validation](validation/2026-11-07-awbi-17-sales-scenario.md). It is an arithmetic sensitivity, not a demand forecast.
- A fixed-window monthly shipped-sales trend is implemented locally; its filter and reconciliation checks are in [AWBI-18 validation](validation/2026-11-07-awbi-18-monthly-sales.md).
- An initial customer segment overview is implemented locally; its checks and source-layout limitations are in [AWBI-19 validation](validation/2026-11-07-awbi-19-customer-overview.md).
- Category-filtered customer RFM is corrected locally and checked for the selections recorded in [AWBI-20 validation](validation/2026-11-07-awbi-20-category-rfm.md); other product and combined filters remain unverified.
- Excel MCP and Jira have been used from Codex. Excel operations have been checked by readback and GitHub evidence linked manually in Jira; automatic linking and some advanced model operations remain unverified.
- Jira is authoritative for live work status. Phases 1 ([AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2)), 2 ([AWBI-3](https://angel231995.atlassian.net/browse/AWBI-3)) and 3 ([AWBI-4](https://angel231995.atlassian.net/browse/AWBI-4)) were marked Done on 2026-11-07. Phase 3's acceptance was performed by the project assistant, not an independent human reviewer; see the [evidence review](validation/2026-11-07-phase-3-review.md) and the later AWBI-19 guard checks. Consult the [AWBI board](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2) for live status.
- Audit remediation and public-portfolio preparation are tracked under [AWBI-12](https://angel231995.atlassian.net/browse/AWBI-12). See the [audit follow-up](validation/2026-11-07-audit-remediation.md) and live Jira status.

## Decisions and boundaries

- Use the selected OLTP install files and Power Query for commercial analytics. The initial sales grain is one order line, and the main sales view includes shipped orders (`Status = 5`).
- Prioritize sales, units, distinct orders and average order value. Historical margin remains conditional on a defensible historical-cost method.
- A workbook and early ingestion were explicitly authorized. Publishing remains subject to separate approval. Raw files stay local and ignored by Git.
- A two-decimal presentation and source reconciliation policy is documented in the KPI catalog; sub-cent floating-point differences remain and the model is not fixed-decimal accounting.

## Next steps

1. Confirm currency and returns treatment before publication. Other product and combined RFM filters remain unverified.
2. Test handoff on a different computer before relying on the workbook-relative source configuration.
3. Review workbook metadata and Git history for public visibility; current and earlier workbook versions contain local user-identifying information.

These next steps are not authorization to begin additional phase 4 work or publish changes.

The project uses MIT for project-authored material and retains Microsoft's third-party notice. Public visibility may be considered during development; check current visibility and review workbook metadata and Git history before changing it. See the [Roadmap](ROADMAP.md) for phase gates and the [Jira Workflow](JIRA_WORKFLOW.md) for review and Done.
