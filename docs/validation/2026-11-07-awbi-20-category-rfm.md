# Customer RFM by product category — local validation

**Date:** 2026-11-07. **Status:** implemented and checked locally; [AWBI-20](https://angel231995.atlassian.net/browse/AWBI-20) is in progress pending versioning and review. It depends on the RFM base and scores in AWBI-15 and AWBI-16, both in review.

## Semantics and correction

When a product category is selected, the last order date means the latest qualifying shipped order containing a line in that category. Frequency counts distinct qualifying orders containing such lines; monetary value sums qualifying lines in the category. Recency is measured from that last order to the fixed 2025-06-29 cutoff. Scores and segment rules continue to use the fixed whole-sample bands in `RFMGuide`; they are not recalculated percentiles for the selected category. A customer with no qualifying lines in the category has blank measures and does not appear in the PivotTable.

The original last-order measure read the order header without receiving the product filter. In the mixed-status test copy with Bikes selected, it displayed 9,400 customers without Bikes lines and gave a non-category last-order date for 102 of the 9,719 matching customers. Frequency and monetary values matched for those 9,719 customers.

The revised measure temporarily enables reverse propagation along the existing order-detail/order-header relationship for this calculation only. Power Pivot displayed the following definition in the main workbook:

```dax
RFM Last Order = CALCULATE(MAX('SalesOrderHeader'[OrderDate]), KEEPFILTERS('SalesOrderHeader'[Status] = 5), KEEPFILTERS('SalesOrderHeader'[OrderDate] >= DATE(2022,5,30)), KEEPFILTERS('SalesOrderHeader'[OrderDate] < DATE(2025,6,30)), CROSSFILTER('SalesOrderDetail'[SalesOrderID], 'SalesOrderHeader'[SalesOrderID], BOTH))
```

`CustomerRFM` has a dedicated category slicer. `CustomerOverview` counts the resulting customer rows; the overview and `RFMGuide` disclose the category semantics and testing scope. The filter was cleared after testing.

## Checks

| Workbook and context | Customers compared | Result |
| --- | ---: | --- |
| Mixed-status copy, Bikes | 9719 | Last date, recency, orders and decimal sales matched independent source aggregation; scores and segments also matched a separate calculation |
| Mixed-status copy, Accessories | 15461 | Last date, recency, orders and decimal sales matched independent source aggregation |
| Mixed-status copy, no category filter | 19119 | Last date, orders and decimal sales matched independent source aggregation |
| Main workbook, Bikes | 9719 | Last date, recency, orders and decimal sales matched independent original-source aggregation |
| Main workbook, no category filter | 19119 | Last date, recency, orders and decimal sales matched independent original-source aggregation |

All monetary comparisons used the existing absolute tolerance below 0.005. In the mixed-status copy, a status-1 diagnostic context returned blank for the RFM measures and scores while a control still found 26 units. In the main workbook, the Bikes selection updated `CustomerOverview` to 9,719 customers and its five segment counts summed to that number; clearing it restored 19,119 and the earlier segment counts. The Bikes filter was applied and read back through the Excel slicer tool; this is not a claim that every interactive filter combination works.

The original unfiltered sales overview still returned 109846381.3998877 sales, 274914 units and 31465 orders. Excel read back six active model relationships and 25 zero key checks. This is not a full source refresh. The saved local pre-change copy is `data/AWBI-20-before.xlsx`; the test workbook and backup are untracked. The checks were performed by the project assistant, not an independent reviewer.

## Remaining limits

Only the stated category selections and contexts were checked. Other product-level, multi-category, date and territory combinations need their own tests before relying on them. Fixed score thresholds are sample-specific; segments remain descriptive and do not establish future behavior. Version and review the workbook and evidence before Done.
