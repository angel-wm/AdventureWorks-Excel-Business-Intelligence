# Initial sales view — local checkpoint

**Date:** 2026-11-07. **Status:** partial implementation in the local workbook; [AWBI-14](https://angel231995.atlassian.net/browse/AWBI-14) remains in progress. The underlying measures in AWBI-11 and AWBI-13 are in review.

## Built

`SalesOverview` contains the four shipped-order measures by product category, territory and category slicers, and an order-date timeline. `SalesByDate` shows the same measures by order date. The three controls are connected to both PivotTables. The overview states that category order counts can overlap and explains the filtered AOV denominator. It identifies the sample's partial periods and the sales amount boundary.

Both tables use two-decimal sales and AOV formats and whole-number units and orders. The timeline and slicers were returned to their cleared state. The saved workbook has a local pre-change backup at `data/AWBI-14-before.xlsx`; the backup and raw source files are not versioned.

## Checks

| Selection | Sales | Units | Distinct orders | AOV |
| --- | ---: | ---: | ---: | ---: |
| All data, both PivotTables | 109846381.3998877 | 274914 | 31465 | 3491.0656729663974 |
| Australia, Bikes, June 2022, both PivotTables | 199477.93459999998 | 59 | 59 | 3380.981942372881 |
| Independent decimal source aggregation for that selection | 199477.934600 | 59 | 59 | 3380.981942372881 |

Excel MCP applied and read back the combined slicer and timeline selection, and read both PivotTable outputs. The independent aggregation joined the original headers, lines, territory and product category and applied shipped status, order date and the two selected dimensions. The first three daily rows for Australia and Bikes were also checked against source before applying the date timeline. Visual inspection of both sheets showed readable dates and totals. These checks cover the stated selections; they do not establish every possible interactive combination, other refresh paths, or behavior on another computer.

## Remaining work

- Creating a PivotChart through Excel MCP failed with a COM error and bound the newly created chart to the wrong PivotTable. The incomplete chart and its temporary source sheet were removed; no chart is delivered. Find and verify a reliable chart route before representing the analytical view as complete.
- Verify any remaining required filter interactions and the view on the final workbook baseline. Link the version and evidence in Jira before review.
- The direct DAX/DMV provider limitation and the pending currency and returns decisions remain documented in the KPI catalog and earlier validations.

These checks were performed by the project assistant, not an independent reviewer.
