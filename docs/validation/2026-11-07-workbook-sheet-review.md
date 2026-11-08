# Workbook sheets, errors and navigation review

**Date:** 2026-11-07. **Method:** assistant review of the open workbook through Excel MCP and local source reconciliation. The review is not independent human acceptance. The workbook was backed up before reordering. No sheets were deleted or hidden, and no full refresh or new interactive-filter test was performed.

## Baselines and checks

The pre-change saved review copy has SHA-256 `a6444fd1078c81f84e784abf33cc12558eb3fedd5efd1a9d4ab4d436c358a8e1`. The post-change saved review copy has SHA-256 `ec68d631352533f0b28ad1279d44df2f6c310f87536cfe1dc680c6ebc91df17a`. These hashes identify local review copies, not a published release.

| Check | Result and limit |
| --- | --- |
| Workbook structure | 20 visible worksheets, 9 worksheet tables, 8 Power Query queries, 7 PivotTables and 6 active model relationships read back |
| Native error scan | Excel reported zero error cells in the used range of each of the 20 worksheets in the current unfiltered state |
| Worksheet formulas | Saved-package inspection found 67 formulas and no formula containing `#REF!`; this does not inspect DAX definitions inside the binary model |
| External workbook links | Excel reported none; Power Query's local CSV dependencies remain |
| Controls | The 25 loaded `KeyChecks` results were zero; `Validation!B19` returned 209 |
| Source reconciliation | Decimal line sales were 109846381.399888 versus 109846381.3998877 in the overview; units and distinct shipped orders matched at 274914 and 31465 |
| Monthly reconciliation | All 38 months matched source aggregation within 0.005; maximum difference was 0.0000000597 |
| Customer RFM | The 19,119 loaded customer rows checked against source orders and lines had no value, score or segment mismatches under the fixed sample rules; interactive contexts were not exercised |
| Reorder preservation | Saved cell addresses, types, values and formula texts matched before and after on all 20 sheets; 67 formulas remained and no cached error cells were found |

The scenario remained at zero price change and zero additional discount; its baseline and result were 109846381.3998877. The customer overview retained 19,119 customers and reconciliation `OK`. Existing [currency and returns limitations](2026-11-07-currency-returns-review.md) still apply to interpreting the monetary results.

## Necessity and redundancy

No worksheet was found empty or established as safe to remove without changing the current design. The seven source queries load both to worksheets and to the Data Model. Their worksheet copies duplicate storage, but `Validation` reads those worksheet data; changing load modes would need dependency and refresh checks.

`SalesChartData` supplies the category chart; `SalesByDate` supplies `SalesMonthly`; `CustomerRFM` supplies `CustomerOverview`; `SourceConfig` supplies the source-folder table used by Power Query. These support sheets have current dependents.

`Validation`, `KeyChecks`, `SalesMeasuresCheck` and `ModelChecks` overlap as diagnostics but are not equivalent. `KeyChecks` tests query keys and joins; `Validation` reads worksheet counts and sums against fixed source benchmarks; `SalesMeasuresCheck` exercises the shipped measures; `ModelChecks` retains initial model aggregates without the production shipped-status rule. The current all-shipped sample makes several totals identical. Consolidating their presentation is possible, but deleting a sheet now would also remove distinct diagnostic coverage.

## Findings to address

- `CustomerOverview!A14` always displays `CHECK: inspect CustomerRFM.` even while `B13` is `OK`. This static instruction looks like a failing check; make it conditional or reword it as neutral guidance.
- `CustomerOverview` does not directly show the currency warning. Its named segments depend partly on monetary scores, so the overview should disclose the same unresolved currency/comparability limitation as `CustomerRFM` and `RFMGuide`.
- `SalesChartData` fixes the chart to four named sample categories and maps all lookup errors to `#N/A`. Its disclosure is present, but that behavior requires maintenance if categories change and can conceal errors as chart gaps.
- `SalesMonthly` uses a fixed 38-month window and a bounded daily source range. `CustomerOverview` uses fixed source columns and a 20,000-row boundary. These are disclosed design limits, not proof of reliable behavior for arbitrary larger or changed datasets.
- `Validation` contains fixed source benchmark totals. Its checks must be interpreted against the pinned source snapshot and are not automatic certification for new source files.

These findings were recorded without expanding the reorder into worksheet deletion or a formula redesign.

## Saved worksheet order

| Positions | Purpose | Worksheets, in order |
| --- | --- | --- |
| 1–4 | Main analysis | `SalesOverview`, `SalesMonthly`, `CustomerOverview`, `SalesScenario` |
| 5–7 | Detail and interpretation | `SalesByDate`, `CustomerRFM`, `RFMGuide` |
| 8–11 | Quality and diagnostics | `KeyChecks`, `Validation`, `SalesMeasuresCheck`, `ModelChecks` |
| 12–13 | Chart support and configuration | `SalesChartData`, `SourceConfig` |
| 14–20 | Loaded source data | `SalesOrderHeader`, `SalesOrderDetail`, `Product`, `ProductSubcategory`, `ProductCategory`, `Customer`, `SalesTerritory` |

Excel read back this order after the moves. The workbook was saved and left open on `SalesOverview`.
