# Current State

**Last reviewed:** 2026-11-08. This is a dated snapshot, not a live Jira or remote-publication feed.

## What exists

- The repository contains the project plan, source map, KPI definitions and validation guidance. It is intended for public portfolio use; local changes do not prove remote publication.
- Seven files from the selected Microsoft AdventureWorks OLTP revision have been downloaded and profiled locally. Their provenance, hashes and checks are in [initial sales load validation](validation/2026-11-06-initial-sales-load.md).
- `AdventureWorks-BI.xlsx` contains seven Power Query worksheet and Data Model loads and six active relationships. Source counts and category/territory PivotTable checks are recorded in [sales model validation](validation/2026-11-06-model-relationships.md). Shipped sales and units are checked in [AWBI-11 validation](validation/2026-11-07-awbi-11-prototype.md), and shipped orders and AOV in [AWBI-13 validation](validation/2026-11-07-awbi-13-orders-aov.md). An initial filterable sales view and chart are checked in [AWBI-14 validation](validation/2026-11-07-awbi-14-sales-view.md).
- A customer RFM base is implemented locally with a fixed sample cutoff; its scope and checks are in [AWBI-15 validation](validation/2026-11-07-awbi-15-customer-rfm.md). Fixed scores and descriptive segments are recorded in [AWBI-16 validation](validation/2026-11-07-awbi-16-rfm-segments.md).
- A fixed-volume sales scenario is implemented locally; its assumptions and checks are in [AWBI-17 validation](validation/2026-11-07-awbi-17-sales-scenario.md). It is an arithmetic sensitivity, not a demand forecast.
- A fixed-window monthly shipped-sales trend is implemented locally; its filter and reconciliation checks are in [AWBI-18 validation](validation/2026-11-07-awbi-18-monthly-sales.md).
- An initial customer segment overview is implemented locally; its checks and source-layout limitations are in [AWBI-19 validation](validation/2026-11-07-awbi-19-customer-overview.md).
- Category-filtered customer RFM is corrected locally. All four category selections and their segment counts were checked in the [workbook improvements regression](validation/2026-11-07-workbook-improvements.md). The later [dashboard validation](validation/2026-11-08-dashboards.md) checks all 30 category/segment combinations exposed by the new customer dashboard; other product-level filters remain unverified.
- `DashboardSales` and `DashboardCustomers` are implemented locally with coherent dark backgrounds, light chart panels, green accents and native filters. They lead the workbook, followed by `SalesScenario`. Their scope, source reconciliation, refresh results and automation limitations are recorded in [dashboard validation](validation/2026-11-08-dashboards.md). The three overlapping legacy views remain in the workbook as hidden sheets because the dashboards and controls depend on them.
- The README presents both dashboards with Excel-generated sample previews and links to setup, metric definitions and validation evidence. The repository was public on 2026-11-08; consult Git and GitHub for the exact revision available locally and remotely.
- The owner reported completing a human workbook review on 2026-11-08. Navigation and readability refinements discussed during that review, and the scope of their checks, are recorded in [workbook review follow-up](validation/2026-11-08-workbook-review-follow-up.md).
- Excel MCP and Jira have been used from Codex. Excel operations have been checked by readback and GitHub evidence linked manually in Jira; automatic linking and some advanced model operations remain unverified.
- Jira is authoritative for live work status. Phases 1 ([AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2)), 2 ([AWBI-3](https://angel231995.atlassian.net/browse/AWBI-3)) and 3 ([AWBI-4](https://angel231995.atlassian.net/browse/AWBI-4)) were marked Done on 2026-11-07. Phase 3's acceptance was performed by the project assistant, not an independent human reviewer; see the [evidence review](validation/2026-11-07-phase-3-review.md) and the later AWBI-19 guard checks. Consult the [AWBI board](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2) for live status.
- Phase 4 ([AWBI-5](https://angel231995.atlassian.net/browse/AWBI-5)) was marked Done on 2026-11-08 after the owner reported completing the workbook review. The issue links the follow-up evidence and records the owner's accepted coverage boundaries.
- Audit remediation and public-portfolio preparation are tracked under [AWBI-12](https://angel231995.atlassian.net/browse/AWBI-12). See the [audit follow-up](validation/2026-11-07-audit-remediation.md) and live Jira status.

## Decisions and boundaries

- Use the selected OLTP install files and Power Query for commercial analytics. The initial sales grain is one order line, and the main sales view includes shipped orders (`Status = 5`).
- Prioritize sales, units, distinct orders and average order value. Historical margin remains conditional on a defensible historical-cost method. The owner accepted the documented currency limitation and declined a second-computer refresh test for this project phase.
- A workbook and early ingestion were explicitly authorized. Publishing remains subject to separate approval. Raw files stay local and ignored by Git.
- A two-decimal presentation and source reconciliation policy is documented in the KPI catalog; sub-cent floating-point differences remain and the model is not fixed-decimal accounting.
- The owner accepted describing amounts provisionally as source monetary amounts with currency unconfirmed. The common-currency interpretation remains unverified; see the [currency boundary](KPI_CATALOG.md#currency-boundary).
- Following the [initial worksheet review](validation/2026-11-07-workbook-sheet-review.md), [workbook improvements](validation/2026-11-07-workbook-improvements.md) corrected disclosures and dynamic ranges and consolidated four control sheets into `Validation` and `KeyChecks`. That checkpoint had 18 sheets and 4 PivotTables. The workbook now has 20 sheets, of which 17 are visible, 9 query loads, 5 PivotTables and 10 charts. The existing chart helper was renamed `DashboardData` and reused. Full refresh and bounded interaction checks passed; currency interpretation and broader coverage remain limited as documented.

## Next steps

The agreed phase scope is complete. Preserve the documented limitations: currency is unconfirmed, returns are not deducted from shipped sales, refresh on another computer was not tested, and product-level RFM filters beyond the tested category/segment combinations remain unverified. See the [currency and returns review](validation/2026-11-07-currency-returns-review.md).

The project uses MIT for project-authored material and retains Microsoft's third-party notice. The owner accepted exposure of the identified Windows user name and local paths; the bounded scan in the [audit follow-up](validation/2026-11-07-audit-remediation.md) does not establish that all other information is safe to publish. Consult the [Roadmap](ROADMAP.md) for phase gates.
