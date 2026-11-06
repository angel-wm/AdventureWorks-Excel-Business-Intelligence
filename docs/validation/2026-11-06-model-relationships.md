# Sales model — local validation

**Date:** 2026-11-06. **Status:** local workbook evidence; not yet versioned or reviewed. The workbook remains open, so no file hash was taken for this state.

## Model and checks

The local `AdventureWorks-BI.xlsx` loads the seven selected Power Query tables into worksheets and the Excel Data Model. Excel MCP read back seven model tables with the expected row counts and six active relationships described in the [Source Map](../SOURCE_MAP.md).

The `KeyChecks` sheet reads the worksheet tables and reports zero duplicate keys, unmatched references and missing required keys across 24 checks. Product subcategory is optional: 209 source products have no subcategory and none occurs in the selected sales lines.

Two Data Model PivotTables on `ModelChecks` aggregate line sales by order territory and product category. Their grand total is 109846381.3998877. Each territory and category total matched an independent decimal aggregation of the source at two decimal places; the exact source total is 109846381.399888. The current source has only status 5 orders. These PivotTables do not implement an explicit shipped-order filter and must not be treated as production KPIs for a changed source.

A third PivotTable cross-tabulates territory and product category. All 40 intersections differed from independent decimal source calculations by less than 0.005. This validates the tested combinations for the selected snapshot, not all future filters or other dimensions.

For each of the 31,465 source orders, the header subtotal equals the sum of source line totals rounded to four decimal places using decimal half-up rounding. This observed agreement explains the pattern consistently but does not prove the upstream implementation. For these reconciliation checks, compare aggregate values with an absolute tolerance strictly below 0.005; do not round each line before summing. A final business reporting and currency precision policy remains open.

An Excel MCP refresh of all eight queries and both PivotTables reported success; the key-check sheet still returned zeros afterwards. `KeyChecks` references worksheet tables, so future refresh ordering and stale-check behavior must be reviewed before relying on it for a changed source.

The source path now derives from the saved workbook directory and `data/raw/adventureworks-oltp-8fe3fd0c/`. A temporary copy of the workbook and the seven source files was placed in a different local directory. After opening the copy, Excel showed the new source path, refreshed all queries and both PivotTables, returned zeros for all 24 key checks and preserved the grand total. This checks a local directory move, not another device, cloud path or missing-source recovery. Raw files remain excluded from Git and must be obtained separately.

## Limitations

- The Excel MCP DAX/DMV evaluation route failed because its reported `MSOLAP.7` provider was not registered. Native Excel Data Model PivotTables worked and were used for the checks above; this does not establish that other DAX operations work.
- The relative folder structure and source files must be preserved; cloud paths, a different computer and missing-source recovery remain untested. Version the workbook and evidence before handoff.
- The filter checks cover territory and category, not every customer, date, scenario or dashboard interaction. Define the monetary precision policy and handle unknown members explicitly before production analytics.

## Workbook organization

The unused blank `Sheet1` was removed after checking that its used range and shape count were empty. The remaining sheets are ordered as validation, model and key checks; order, product and customer/territory sources; then source configuration. The workbook remains open in the same Excel session.
