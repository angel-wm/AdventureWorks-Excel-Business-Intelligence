# Proposed Architecture

**Status: Draft.** No analytical model or workbook has been implemented.

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

The candidate **sales fact grain** is one `SalesOrderDetail` line, with order-header attributes from `SalesOrderHeader`. Do not sum header-level totals after repeating them across detail rows.

| Entity | Proposed key/grain | Role |
| --- | --- | --- |
| Sales fact | `SalesOrderID` + `SalesOrderDetailID` (to verify) | Amounts, units, product and order linkage |
| Order header | `SalesOrderID` | Order date, customer, territory, order type and status |
| Product | `ProductID` | Attributes, subcategory and category hierarchy |
| Customer | `CustomerID` | Person/store customer behavior and segmentation |
| Territory | `TerritoryID` | Geographic commercial analysis |
| Date | One calendar date | Monthly/yearly comparisons |
| Assumptions | Independent input records | Scenarios, not actual sales |

Specific keys, fields and cardinalities must be checked against the selected source. See the [Source Map](SOURCE_MAP.md).

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

Power Query and Power Pivot are part of the technical plan, but their automation through the **user's installed Excel MCP** is not confirmed. [AI Workflow](AI_WORKFLOW.md) defines discovery, readback and Excel Desktop fallback.

Use Jira to track work items, not as the location of SQL, M code, business rules or authoritative calculation definitions. See [Jira Workflow](JIRA_WORKFLOW.md). GitHub holds versioned documents and deliverables.
