# Shipped orders and average order value — local validation

**Date:** 2026-11-07. **Status:** implemented and checked locally; review and versioned evidence are pending. [AWBI-13](https://angel231995.atlassian.net/browse/AWBI-13) depends on the shipped sales measure in [AWBI-11](https://angel231995.atlassian.net/browse/AWBI-11), which remains in review.

## Definitions

The main workbook's `SalesOrderDetail` model table contains:

```dax
Shipped Orders = CALCULATE(DISTINCTCOUNT('SalesOrderDetail'[SalesOrderID]), KEEPFILTERS('SalesOrderHeader'[Status] = 5))
Shipped AOV = DIVIDE([Shipped Sales], [Shipped Orders])
```

Excel Power Pivot displayed the two definitions. The order ID comes from sales lines so product filters affect the count. When a category is selected, the numerator is the sales of eligible lines in that category and the denominator is the distinct orders containing those lines: this is category sales per participating order, not the full order value for those orders. The measure returns blank when its denominator is blank or zero.

## Checks

An independent Python aggregation used decimal source line totals, joined headers and product categories, and counted distinct order IDs in each group. It used the same selected files as the initial sales validation; the main source files were not changed.

| Scenario | Excel output | Independent calculation |
| --- | ---: | ---: |
| Original sample: shipped orders | 31465 | 31465 |
| Original sample: shipped AOV | 3491.0656729663974 | 3491.065672966407 |
| Mixed status: shipped orders | 31464 | 31464 |
| Mixed status: shipped AOV | 3490.5230034098554 | 109825815.779288 / 31464 |

For both scenarios, all 40 territory-by-category order counts matched exactly. The maximum AOV difference from independent decimal aggregation was below 0.000000001. In the mixed-status fixture from [AWBI-11 validation](2026-11-07-awbi-11-prototype.md), a diagnostic DAX context selecting status 1 returned blank for both shipped measures, while a control counted 26 units in the non-shipped order. This is a DAX context test, not a test of an interactive report-filter selector; the full diagnostic formulas were not separately read back.

The `SalesMeasuresCheck` PivotTable was refreshed and read back after formatting. Order counts use `#,##0`; AOV uses `#,##0.00`. The original-sample totals remained unchanged. A pre-change rollback copy is local at `data/AWBI-13-before.xlsx`; test files are untracked and must not be included in a commit. The main workbook and test copy were saved.

## Limits and review

The full refresh and original shipped sales/unit checks belong to the previous AWBI-11 checkpoint; this task refreshed the measures PivotTable, not all source queries. Excel MCP's direct DAX/DMV route remains unavailable. Power Pivot was used for measure inspection, and the PivotTables for output readback. The checks were performed by the project assistant and are not an independent review. Confirm currency and returns before publication, and test interactive filters when building dashboards.
