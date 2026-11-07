# Customer RFM base — local validation

**Date:** 2026-11-07. **Status:** implemented and tested locally; [AWBI-15](https://angel231995.atlassian.net/browse/AWBI-15) awaits versioning and review. This base depends on shipped measures in AWBI-11 and AWBI-13, both in review.

## Scope and definitions

`CustomerRFM` lists customers with observed qualifying orders. The fixed observation window is 2022-05-30 through 2025-06-29, inclusive; the as-of date is 2025-06-29. Only shipped orders (`Status = 5`) qualify. These are sample observations, not lifetime customer histories. A fixed cutoff makes the analysis reproducible; a later data refresh does not advance the cutoff.

The `SalesOrderDetail` model table contains these measures, read back through Power Pivot's measure editor:

```dax
RFM Last Order = CALCULATE(MAX('SalesOrderHeader'[OrderDate]), KEEPFILTERS('SalesOrderHeader'[Status] = 5), KEEPFILTERS('SalesOrderHeader'[OrderDate] >= DATE(2022,5,30)), KEEPFILTERS('SalesOrderHeader'[OrderDate] < DATE(2025,6,30)))
RFM Recency Days = IF(ISBLANK([RFM Last Order]), BLANK(), DATEDIFF([RFM Last Order], DATE(2025,6,29), DAY))
RFM Orders = CALCULATE([Shipped Orders], KEEPFILTERS('SalesOrderHeader'[OrderDate] >= DATE(2022,5,30)), KEEPFILTERS('SalesOrderHeader'[OrderDate] < DATE(2025,6,30)))
RFM Sales = CALCULATE([Shipped Sales], KEEPFILTERS('SalesOrderHeader'[OrderDate] >= DATE(2022,5,30)), KEEPFILTERS('SalesOrderHeader'[OrderDate] < DATE(2025,6,30)))
```

Existing filters intersect the fixed window. The delivered table uses customer context and has no product filter. Product filters are not validated: last order uses the header while frequency and monetary values use sales lines, so product context may affect them differently. Do not interpret the measures as a product-filtered RFM without further work. At this checkpoint no scores, bands or segments were implemented; see the [later scoring validation](2026-11-07-awbi-16-rfm-segments.md).

## Checks

An independent Python aggregation of the pinned original source joined headers and sales lines, applied the same status and dates, and calculated each customer's most recent date, elapsed calendar days, distinct order IDs and decimal line sales. All **19,119** customers with qualifying sales lines matched the Excel PivotTable: dates, recency and counts exactly; the largest absolute sales difference was below 0.000000002, within the existing 0.005 tolerance.

| Customer | Last order | Days | Orders | Sales |
| --- | --- | ---: | ---: | ---: |
| 11091 | 2025-06-09 | 20 | 28 | 1189.33 |
| 28389 | 2022-05-30 | 1126 | 1 | 3399.99 |
| 29825 | 2025-02-28 | 121 | 12 | 422706.602251 |

In the AWBI-11 mixed-status copy, order 43659 is status 1. Customer 29825 returned 11 orders and 402140.981651 sales; customer 11091 returned 28 and 1189.33, and customer 28389 returned one and 3399.99. Those values and dates matched a separate source aggregation. A diagnostic DAX context selecting status 1 returned blank for the four RFM measures while an independent model control counted 26 non-shipped units. This tests that context, not the interactive selection of all possible filters; the diagnostic expressions were not separately read back.

The main PivotTable was refreshed, formatted and saved. Power Pivot displayed the four formulas, and Excel read back the displayed date, count and sales formats. Grand totals were removed because aggregate recency is not a customer value. The local pre-change rollback is `data/AWBI-15-before.xlsx`; the fixture and backup are untracked. No full source refresh was performed as part of this task. The checks were performed by the project assistant, not an independent reviewer.

## Remaining work

Version and review the actual workbook and this evidence; review the underlying measures first. Define and validate scoring bands, ties and segments as separate work. Validate product-filtered or other cross-dimension RFM before using it. Currency and return treatment remain subject to the KPI catalog's publication boundary.
