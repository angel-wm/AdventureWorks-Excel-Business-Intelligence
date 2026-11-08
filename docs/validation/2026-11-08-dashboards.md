# Sales and customer dashboards

**Date:** 2026-11-08. **Scope:** local implementation, source reconciliation and Excel verification by the project assistant. This is not independent human acceptance, a Jira transition or a public release.

## Delivered workbook

At the dashboard validation checkpoint, `AdventureWorks-BI.xlsx` opened on `DashboardSales`, followed by `DashboardCustomers`, and had SHA-256 `ffc8d791577212586d7d917708d938c3510bfe3f7fbe3d8eb569abefebd79259`. The subsequent sheet-visibility change below produced a newer workbook version.

The workbook contains 20 worksheets, 9 Power Query loads, 7 model tables, 6 relationships, 5 PivotTables and 10 charts. Two presentation sheets and one territory PivotTable were added. The existing `SalesChartData` helper was renamed `DashboardData` and extended; no new raw dataset was downloaded. Local backups are `data/backups/AdventureWorks-before-dashboards.xlsx` and `data/backups/AdventureWorks-before-dashboard-polish.xlsx`.

Both dashboards use a dark green background, light panels and green accents. The revised landscape canvas is 1414.5 by 617.25 points, with equal KPI cards and a filter panel at the right. Both sheet views are saved at 100% zoom and A1. KPI values use 28-point text, labels 12 points, chart titles 15 points and axis labels 11.5-12 points. All ten territory labels are shown. Slicers have equal horizontal insets and two button columns; their final heights accommodate the last item row. Print areas include the full dashboard.

## Measurements and filters

| View | Indicators and charts | Controls |
| --- | --- | --- |
| Sales | Shipped line sales, units, distinct orders and AOV; monthly sales, category comparison and territory comparison | Native product-category and territory slicers and order-date timeline, connected to all three supporting sales PivotTables |
| Customers | Selected customer count, median recency, median orders and median customer sales; customer counts by RFM segment, recency band, order-count band and monetary band | Native category slicer plus a validated segment dropdown at `AF34`; all four cards and charts use the same selected customer population |

Sales reuses the existing four shipped measures. Customer summaries reuse the fixed-window `CustomerRFM` results, with dynamic header-based source columns and a filtered spill in `DashboardData`. Medians use customer-level values, not subgroup averages. Monetary band assignment rounds each customer's total to two decimals, while median customer sales uses the unrounded totals. Rules and boundaries are in the [KPI catalog](../KPI_CATALOG.md#customer-dashboard-summaries) and `RFMGuide`.

Currency remains unconfirmed and monetary comparability is unresolved. Shipped line sales exclude tax, freight and return/refund adjustments. Category order counts may overlap. Monthly periods follow the selected dates and may be partial. RFM retains the 2022-05-30 through 2025-06-29 observation window, the 2025-06-29 cutoff and fixed descriptive score bands. It is not lifetime history or a validated prediction. These limitations remain visible in the workbook.

## Executed checks

| Check | Result |
| --- | --- |
| Independent source aggregation | Python read the seven pinned tab-delimited CSVs, joined orders and product categories, applied shipped status and the RFM window, and calculated distinct customer orders, decimal sales, dates, scores, segments and medians |
| Customer controls | All 30 combinations of All/four categories and All/five segments matched source-based expectations for all four KPIs and every bin in the four chart-support distributions |
| Baseline customer values | 19119 customers; median recency 165 days; median orders 1; median sales 548.98. Segment counts: 964, 695, 6359, 2273 and 8828 |
| Combined customer charts | Bikes and Champions: 869 customers. Native series values matched source expectations in all four charts, including the 391/478 recency split and 487/182/200 counts for three/four/five-or-more orders |
| Empty selection | The blank product-category member returned zero customers, unavailable medians and four zero-valued native chart series. Support state was `EMPTY`, distinct from a source-layout failure |
| Combined sales controls and charts | Australia, Bikes, June 2022 returned 199477.9346 sales, 59 units, 59 orders and AOV 3380.981942372881. Category and territory charts each showed the selected member; the monthly series had one positive selected month. Native values matched source aggregation within 0.005 |
| Complete refresh | Excel MCP refreshed all 9 query loads, `ThisWorkbookDataModel` and all 5 PivotTables; no query, connection or PivotTable failures were reported |
| Restored values | Sales 109846381.3998877, units 274914, orders 31465 and AOV 3491.0656729663974. Customer values returned to the baseline above. Category, territory, date and segment filters were reset |
| Controls | All 18 live validation results and overall `Validation!D4` were `OK`; the 25 key/join controls were zero |
| Saved package | All 20 worksheet XML parts had zero cached error cells and no `#REF!` worksheet formulas. No external-workbook link parts were present. The model, 5 PivotTable parts and 10 chart parts remained present |
| Source preservation | All seven raw CSV hashes matched the independent check's input hashes. The final `SourceConfig!A2` retains its workbook-relative formula and resolves to the original source folder from the main workbook |
| Visual checks | Excel captures and native Excel PDF renders covered both complete views, footnotes, chart labels and filter panels. The final export was checked for complete filter rows; views were restored to A1 at 100% |

The local ignored review directory `data/data/dashboard-review/` retains the independent expected summaries, 30-case MCP results, final native readback, package check and native visual previews. The source-only computation is independent of the Excel formulas, but both analyses were executed by the same project assistant.

## Automation limits and recovery

The installed MCP successfully handled the bulk layout, formatting, native slicers, timeline, dropdown, chart placement and fonts, filter tests, full refresh and readback. It also produced repeated Excel/RPC disconnections, including during a broad error scan and screenshot view restoration. A clean saved `.xlsx` was used after the autorrecovered copy proved unstable. The failing broad live error scan was not counted as a pass; the saved package was scanned separately instead.

Narrowly targeted native Excel COM calls set two properties that the MCP did not expose: category-axis `TickLabelSpacing = 1` and slicer `RowHeight = 20`. A native call also restored the timeline's exact position and size after an MCP height update displaced it. Native before/after reads and subsequent Excel rendering verified these changes. A stale MCP path reservation prevented Save As to the main path, despite discovery confirming that file was not open. Native Save As preserved a backup, checked the exact source and destination, restored the relative source path and read back the main workbook. A later MCP `get-info` confirmed the actual `.xlsx` main path.

The final saved file was reopened in Excel after the last screenshot disconnection and left on `DashboardSales`. Windows did not permit MCP to force the foreground window; the owner may need to select Excel from the taskbar. The ChatGPT add-in was not used or tested here, so this evidence makes no claim that it would resolve the observed automation failures.

## Retained overlap

`SalesOverview`, `SalesMonthly` and `CustomerOverview` overlap with the new presentation. They still own PivotTables or calculated results used by the dashboards. Removing them would require moving or repointing those dependencies and validating the result. `CustomerRFM`, `SalesByDate`, `RFMGuide` and the two control sheets retain distinct detail, calculation or validation roles.

### Later navigation change

At the owner's request on 2026-11-08, `SalesScenario` was moved immediately after the two dashboards and the three overlapping views were hidden using Excel's normal hidden-sheet setting. No worksheet was deleted. The workbook retained 20 sheets, including 17 visible sheets. A local pre-change copy is `data/backups/AdventureWorks-before-sheet-hiding.xlsx`.

After the change, both dashboards' four KPI values matched their pre-change values and `Validation!D4` remained `OK`. The customer category filter returned 9719 customers for Bikes and was cleared again. The sales category filter returned 94651172.7047309 for Bikes and its category chart displayed one point; clearing the filter restored the original sales total. These are bounded interaction checks, not a fresh full refresh or a test of every filter combination.

No commit, push, visibility change or Jira status transition was performed. Arbitrary source/schema changes, other product-level filters and another computer remain outside this validation.
