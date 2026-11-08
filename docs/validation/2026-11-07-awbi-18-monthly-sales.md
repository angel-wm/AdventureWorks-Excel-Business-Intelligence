# Monthly shipped sales — local validation

> **Historical checkpoint:** status, sheet positions and limitations below describe this record's original baseline. They are not live task status or current instructions. See the [evidence index](README.md) for later corrections and the current handoff.

**Date:** 2026-11-07. **Status:** implemented and checked locally; [AWBI-18](https://angel231995.atlassian.net/browse/AWBI-18) is in progress pending versioning and review. The view depends on the shipped measures and date PivotTable in AWBI-11 and AWBI-14, both in review.

## Scope

`SalesMonthly` groups the `SalesByDate` PivotTable's shipped line sales by order month for the fixed May 2022–June 2025 sample and charts the 38 values. It follows the territory, category and date controls connected to the underlying PivotTable. May 2022 and June 2025 are partial source months; an applied date selection can make any displayed month partial. The chart is descriptive, not a forecast.

Month formulas use a bounded `SalesByDate` range `A5:B5000`. They return `#N/A` when no dates fall in the selected month, creating a chart gap rather than treating the month as zero. A numeric date in A5000 also forces `#N/A` to avoid silently truncating an enlarged PivotTable; this guard was read back but its 5,000-row boundary was not exercised. Review the range and fixed window if the source changes. Inspect `SalesByDate` and refresh status when results are unavailable; the formula does not certify source freshness.

## Checks

An independent decimal aggregation of the original shipped order lines by header order month matched all 38 Excel values within 0.005; the maximum absolute difference was below 0.00000006. After restoring the formulas and clearing filters, their sum was 109846381.39988767, matching the current shipped-sales PivotTable within the same tolerance. The first and last sample months returned 517737.4369000006 and 47491.55 respectively.

With Australia, Bikes and June 2022 selected through the existing controls, the June cell and chart point returned 199477.93459999995, matching the independently reconciled AWBI-14 selection. The other 37 months returned `#N/A` and chart gaps. The chart source and plotted values were read back; the filtered and unfiltered view were visually inspected. The filters were cleared afterwards. This covers the stated selections, not all combinations or every refresh path.

The workbook was saved and a pre-change rollback retained locally at `data/AWBI-18-before.xlsx`; that copy includes the previously saved local AWBI-17 scenario and is untracked. No full source refresh was performed. Checks were performed by the project assistant, not an independent reviewer. Version and review the final workbook and evidence before Done.

The `SalesOverview` sheet also labels historical margin as unavailable because historical cost has not been validated. Excel read the label back; no margin measure or cost data was added.
