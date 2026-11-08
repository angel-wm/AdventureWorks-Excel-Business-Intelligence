# Initial sales view — local checkpoint

> **Historical checkpoint:** status, sheet positions and limitations below describe this record's original baseline. They are not live task status or current instructions. See the [evidence index](README.md) for later corrections and the current handoff.

**Date:** 2026-11-07. **Status:** implemented and checked locally; [AWBI-14](https://angel231995.atlassian.net/browse/AWBI-14) remains in progress pending versioning and review. The underlying measures in AWBI-11 and AWBI-13 are in review.

## Built

`SalesOverview` contains the four shipped-order measures by product category, territory and category slicers, and an order-date timeline. `SalesByDate` shows the same measures by order date. The three controls are connected to both PivotTables. The overview states that category order counts can overlap and explains the filtered AOV denominator. It identifies the sample's partial periods and the sales amount boundary.

Both tables use two-decimal sales and AOV formats and whole-number units and orders. The timeline and slicers were returned to their cleared state. The saved workbook has a local pre-change backup at `data/AWBI-14-before.xlsx`; the backup and raw source files are not versioned.

The overview also has a standard bar chart of shipped sales by category. Its source is the `SalesChartData` worksheet, whose `GETPIVOTDATA` formulas read the category PivotTable and follow its filters. The chart covers the four named categories in the pinned sample, not future new or unknown categories; review and update the source if the category set changes. A filtered or unavailable category yields `#N/A` in the source and a chart gap. The formula also converts other lookup errors to `#N/A`, so inspect the source PivotTable when a result is unavailable rather than interpreting a gap as zero.

## Checks

| Selection | Sales | Units | Distinct orders | AOV |
| --- | ---: | ---: | ---: | ---: |
| All data, both PivotTables | 109846381.3998877 | 274914 | 31465 | 3491.0656729663974 |
| Australia, Bikes, June 2022, both PivotTables | 199477.93459999998 | 59 | 59 | 3380.981942372881 |
| Independent decimal source aggregation for that selection | 199477.934600 | 59 | 59 | 3380.981942372881 |

Excel MCP applied and read back the combined slicer and timeline selection, and read both PivotTable outputs. The independent aggregation joined the original headers, lines, territory and product category and applied shipped status, order date and the two selected dimensions. The first three daily rows for Australia and Bikes were also checked against source before applying the date timeline. Visual inspection of both sheets showed readable dates and totals. These checks cover the stated selections; they do not establish every possible interactive combination, other refresh paths, or behavior on another computer.

With Australia, Bikes and June 2022 selected, Excel read back 199477.93459999998 for the Bikes chart point and gaps for the other three categories; the visible chart displayed one bar. With Australia and all dates and categories, all four chart points matched the overview PivotTable within 0.005. After clearing all controls, the four points matched the unfiltered PivotTable. The chart source formulas and plotted values were read back in Excel. The chart was visually inspected in the combined-filter state.

## Remaining work

- Creating a PivotChart through Excel MCP failed with a COM error and bound the newly created chart to the wrong PivotTable. A second chart creation also inherited the selected PivotTable and failed to bind its intended range. Both incomplete charts were removed. Selecting a cell outside the PivotTable first allowed a standard chart to be created from the formula-backed range; this is the route tested above.
- Verify any remaining required filter interactions and the view on the final workbook baseline. Link the version and evidence in Jira before review.
- The direct DAX/DMV provider limitation and the pending currency and returns decisions remain documented in the KPI catalog and earlier validations.

These checks were performed by the project assistant, not an independent reviewer.
