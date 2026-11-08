# Proposed Architecture

**Status: Local model and initial analytics.** Seven source tables load into worksheets and the Data Model; six relationships are active. Shipped sales, units, distinct orders and average order value have been implemented and checked locally. See [model validation](validation/2026-11-06-model-relationships.md), [sales and units validation](validation/2026-11-07-awbi-11-prototype.md) and [orders and AOV validation](validation/2026-11-07-awbi-13-orders-aov.md). These checks do not establish every filter interaction or publication readiness.

## How data will move

```text
Official AdventureWorks OLTP sources (unchanged)
    ↓
Power Query: source access → staging → analytical tables
    ↓
Validated facts and dimensions
    ↓
Excel Data Model / Power Pivot (if appropriate)
    ↓
Measures and analytical tables / PivotTables
    ↓
Sales, Customers, Products and Scenario dashboards
```

## Logical model

The selected **sales fact grain** is one `SalesOrderDetail` line, with order-header attributes from `SalesOrderHeader`. Do not sum header-level totals after repeating them across detail rows.

The following screenshot shows the local Power Pivot model on 2026-11-06. The named sales calculations shown in the diagram were created for validation and are not approved production KPIs.

![Power Pivot diagram showing seven sales, customer, territory and product tables with their relationships](images/sales-data-model.png)

| Entity | Proposed key/grain | Role |
| --- | --- | --- |
| Sales fact | `SalesOrderID` + `SalesOrderDetailID` | Amounts, units, product and order linkage |
| Order header | `SalesOrderID` | Order date, customer, territory, order type and status |
| Product | `ProductID` | Attributes, subcategory and category hierarchy |
| Customer | `CustomerID` | Person/store customer behavior and segmentation |
| Territory | `TerritoryID` | Geographic commercial analysis |
| Date | One calendar date | Monthly/yearly comparisons |
| Assumptions | Independent input records | Scenarios, not actual sales |

The selected source's keys and joins were checked locally; initial workbook relationships and category/territory filters were also checked. See the [Source Map](SOURCE_MAP.md) and [model validation](validation/2026-11-06-model-relationships.md).

## Rules that prevent wrong analytics

1. Preserve original data and record its version / source.
2. Explicitly check types, currencies, missing keys and date ranges.
3. Confirm joins do not multiply sales lines or financial totals.
4. Define the sales measure, its exclusions and discount treatment before charting.
5. **Do not claim historical gross margin** until applicable historic costs have been validated; current product cost may not represent past cost.
6. Differentiate observed sales from assumed changes in scenario sheets.
7. Avoid importing unrelated manufacturing, purchasing and HR modules by default.

## Suggested workbook presentation

- `00_README`: purpose, refresh, definitions.
- `01_CONTROLS`: as-of period, scenario assumptions and quality indicators.
- `10_DASH_Sales`: time series, products, territories and order type.
- `11_DASH_Customers`: recurrence and RFM groups.
- `12_DASH_Products`: commercial product breakdowns; margins only if validated.
- `13_SCENARIOS`: clearly marked assumptions.

These names are provisional. Supporting analysis sheets should be kept to the minimum needed.

## Tool boundary

Excel MCP has created and refreshed Power Query loads, model relationships and validation PivotTables in the local workbook. Direct DAX/DMV evaluation encountered an unregistered provider. [AI Workflow](AI_WORKFLOW.md) describes the tested operations, their limits and the Excel Desktop fallback.

Use Jira to track work items, not as the location of SQL, M code, business rules or authoritative calculation definitions. See [Jira Workflow](JIRA_WORKFLOW.md). GitHub holds versioned documents and deliverables.
