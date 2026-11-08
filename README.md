# AdventureWorks — Excel Business Intelligence

An Excel 365 Desktop portfolio that turns Microsoft AdventureWorks OLTP transactions into interactive sales analysis, descriptive customer RFM and a fixed-volume pricing scenario. Power Query prepares the data; the Data Model connects sales, customers, products and territories.

**Delivery:** the original four phases were accepted. The later audit corrections and exact workbook identity are recorded in [Current State](docs/CURRENT_STATE.md) and [Handoff](docs/HANDOFF.md). A local correction is not automatically a published update.

## What the analysis shows

- Online customer entry accounts for **87.9% of orders**, while salesperson entry accounts for **78.0% of units**: order count alone does not describe fulfillment volume.
- Observed repeat purchasing differs between **person-only customers (37.1%)** and **store-linked customers (95.3%)**. Global RFM bands describe the combined sample; they do not imply equivalent customer value.
- The scenario makes the price/discount arithmetic explicit: **+10% price and 5% additional discount yield +4.5% at fixed volume**. This is not a demand or profit forecast.

The [business review](docs/BUSINESS_REVIEW.md) provides source-backed comparisons, complete-period volume changes, cohort definitions and proposed decisions. These are sample observations, not causal conclusions or lifetime customer behavior.

**Monetary limitation:** original source amounts are preserved, with currency unconfirmed and no conversion. Monetary comparability has not been established. The owner accepted this as a closed source limitation for this scope; see the [investigation and decision](docs/DECISIONS.md#currency).

## Explore the dashboards

**Sales performance** presents shipped line sales, units, distinct orders and average order value, a monthly trend, and category/territory comparisons. Filter by order date, category and territory.

![Sales dashboard with shipped sales, units, orders, average order value, monthly trend and category/territory controls](docs/images/dashboard-sales.png)

**Customer intelligence** presents observed customers and median recency, orders and customer sales, plus RFM distributions. Category changes the qualifying purchases; the segment dropdown narrows the resulting population. The fixed observation window is **30 May 2022–29 June 2025**, measured at **29 June 2025**.

![Customer dashboard with fixed-window RFM indicators, distributions and category/segment controls](docs/images/dashboard-customers.png)

The previews show unfiltered sample views. Their capture baselines are recorded in [validation evidence](docs/validation/README.md). Open the workbook for interactive controls; the source-derived business-review tables are separate and do not follow workbook filters.

## Open, explore and verify

1. Open [AdventureWorks-BI.xlsx](AdventureWorks-BI.xlsx) in **Excel 365 Desktop**. Loaded sample data is included; inspection needs no source download.
2. Start with `DashboardSales` or `DashboardCustomers`. Clear filters to restore the full sample.
3. Open `SalesScenario`, the third visible tab. Its baseline follows the sales dashboard. Restore price and discount inputs to zero after exploration.
4. To refresh, follow [Data Setup](docs/DATA_SETUP.md). To reproduce source/package checks, follow [Handoff](docs/HANDOFF.md#reproduce-the-checks).

Sales are discounted shipped order-line amounts before tax, freight and separate return/refund adjustments. Category order counts can overlap; category AOV is selected line sales per participating order. Historical margin is unavailable because a historical-cost method was not validated. See the [KPI definitions](docs/KPI_CATALOG.md) and [accepted boundaries](docs/DECISIONS.md).

## Implementation and evidence

Seven official source files feed Power Query and the Excel Data Model. Relationships, DAX measures, native PivotTables and formula-backed charts support the views. Codex, Excel MCP and native Excel operations built and checked the original workbook. The ChatGPT add-in for Excel was subsequently exercised for audit text corrections, readback and native range images; broader add-in capabilities are not implied. See [AI Workflow](docs/AI_WORKFLOW.md).

Source-based computations are independent of the workbook formulas, but were run by the same project assistant. The owner reported completing a workbook review. The [evidence index](docs/validation/README.md) separates historical tests, current checks and unperformed cases.

## Documentation

| Need | Read |
| --- | --- |
| Business findings and proposed decisions | [Business review](docs/BUSINESS_REVIEW.md) |
| Goals, requirements and optional scope | [Project Brief](docs/PROJECT_BRIEF.md) and [Scope decisions](docs/DECISIONS.md) |
| Model and source grain | [Architecture](docs/ARCHITECTURE.md) and [Source Map](docs/SOURCE_MAP.md) |
| Calculations | [KPI Catalog](docs/KPI_CATALOG.md) |
| Exact artifact, walkthrough and verification command | [Handoff](docs/HANDOFF.md) |
| Acceptance coverage and historical tests | [Validation Plan](docs/VALIDATION_PLAN.md) and [Evidence index](docs/validation/README.md) |
| Phase plan and live work tracking | [Roadmap](docs/ROADMAP.md) and [Jira Workflow](docs/JIRA_WORKFLOW.md) |
| Dated local/published state | [Current State](docs/CURRENT_STATE.md) |

[REPO_CONTEXT.md](REPO_CONTEXT.md) maps authoritative sources for maintainers. Documentation presentation follows the owner's [Repository Documentation Readability guide](https://github.com/angel-wm/repository-documentation-readability/blob/main/GUIDE.md), supported by its [local skill](.agents/skills/repository-documentation-readability/SKILL.md).

## Source and license

The workbook uses fictional Microsoft sample data from the [pinned OLTP source revision](https://github.com/microsoft/sql-server-samples/tree/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script). Original raw files and local backups are excluded from Git; loaded data is included in the workbook. [Provenance and hashes](docs/validation/2026-11-06-initial-sales-load.md) support reproduction.

Project-authored material uses the [MIT License](LICENSE); Microsoft's notice is preserved in [Third-party notices](THIRD_PARTY_NOTICES.md). The owner accepted the identified local author/path metadata exposure; the historical scan was bounded, as recorded in [Scope decisions](docs/DECISIONS.md#delivery-and-publication).
