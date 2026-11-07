# Shipped sales measures — prototype validation

**Date:** 2026-11-07. **Status:** measures implemented and checked locally in the main workbook; this evidence has not been independently reviewed.

## Scope and method

A copy of the saved workbook was opened with Excel MCP. Two measures were created in its `SalesOrderDetail` model table, and their values were read from a native Data Model PivotTable:

```dax
Shipped Sales = CALCULATE(SUM('SalesOrderDetail'[LineTotal]), KEEPFILTERS('SalesOrderHeader'[Status] = 5))
Shipped Units = CALCULATE(SUM('SalesOrderDetail'[OrderQty]), KEEPFILTERS('SalesOrderHeader'[Status] = 5))
```

The original sample contains only status 5. In a separate copy of the seven source files, order 43659 was changed from status 5 to 1. The original source files were not edited. The copied workbook was refreshed from the copied files: Excel MCP reported eight query loads, the model connection and four PivotTables refreshed without failure.

## Results

| Check | Excel PivotTable | Independent decimal aggregation |
| --- | ---: | ---: |
| Original sample sales | 109846381.3998877 | 109846381.399888 (prior source reconciliation) |
| Original sample units | 274914 | 274914 (prior source reconciliation) |
| Mixed-status sales | 109825815.7792877 | 109825815.779288 |
| Mixed-status units | 274888 | 274888 |
| Excluded order sales and units | Difference: 20565.6206 and 26 | 20565.620600 and 26 |

All ten territory groups and all 40 territory-by-product-category intersections matched the independent aggregation within the existing absolute sales tolerance of 0.005; units matched exactly. The largest absolute sales difference among the 40 intersections was approximately 0.00000125. The independent aggregation joined copied headers and detail by order ID, selected status 5, and joined products to subcategories and categories. These are grouping tests, not tests of interactive report-filter controls or every dimension.

Adding order status as another row group displayed values only for status 5 in this fixture. This does not establish the behavior of every explicit status-filter selection.

In the same mixed-status test copy, three diagnostic measures applied `Status = 1`: `CALCULATE([Shipped Sales], 'SalesOrderHeader'[Status] = 1)`, `CALCULATE([Shipped Units], 'SalesOrderHeader'[Status] = 1)` and a control using `CALCULATE(SUM('SalesOrderDetail'[OrderQty]), 'SalesOrderHeader'[Status] = 1)`. A native PivotTable returned blank for both shipped measures and 26 for the control. This tests a DAX filter context with known non-shipped rows, not an interactive report-filter selection. Excel showed the diagnostic measures in Manage Measures, but the full diagnostic expressions were not independently read back in that dialog.

## Main workbook

The same two formulas were created in the main workbook. Power Pivot's Manage Measures dialog read both formulas back, overcoming the Excel MCP measure-read failure for this inspection. The `SalesMeasuresCheck` PivotTable returned 109846381.3998877 sales and 274914 units. All 40 territory-by-category intersections matched a separate decimal aggregation of the original source files within 0.005, with exact unit agreement; the maximum sales difference was approximately 0.00000125.

After a full refresh, Excel MCP reported eight query loads, the model connection and four PivotTables refreshed without failure. The two grand totals were unchanged and all 25 key checks returned zero. The main workbook was saved. A pre-change rollback copy was saved locally in `data/AWBI-11-before.xlsx`; that untracked copy is not a versioned artifact. The mixed-status test was performed in the separate copy, not by changing the main workbook's sources.

The `SalesMeasuresCheck` value fields were formatted with `#,##0.00` for sales and `#,##0` for units. Excel read back those formats from the PivotTable after a PivotTable refresh. This is display formatting; it does not round each line or change the calculation.

## Remaining work

- Excel MCP measure listing and direct measure read still report `Class not registered`; Power Pivot's dialog provided the formula readback above. Direct DAX/DMV querying and automated OLAP report-filter selection remain unverified.
- Confirm the reporting and return policy before publication. Floating-point model totals are not fixed-decimal accounting values; the working presentation policy is documented in the [KPI catalog](../KPI_CATALOG.md).
- Validate interactive filter behavior and any additional dimensions required by the eventual dashboards. Version the workbook and evidence, then review the actual baseline against [AWBI-11](https://angel231995.atlassian.net/browse/AWBI-11) before Done.

The local test workbook and source fixture are untracked, are not a release artifact, and contain Microsoft sample data. The checks were performed by the project assistant, not an independent reviewer.
