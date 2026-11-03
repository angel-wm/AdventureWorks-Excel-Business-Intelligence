# Validation Plan

**Status:** Not executed. Each test below is **NOT RUN**. A documented requirement is not evidence of a working workbook.

## What will be checked

| ID | Check | Initial status |
| --- | --- | --- |
| DV-01 | Record Microsoft source version, file provenance and hashes | NOT RUN |
| DV-02 | Validate CSV/schema mapping, data types and null handling | NOT RUN |
| DV-03 | Check primary keys, duplicates and nulls at intended grains | NOT RUN |
| DV-04 | Confirm join cardinalities and foreign-key completeness | NOT RUN |
| DV-05 | Confirm sales-line counts and amounts survive enrichment | NOT RUN |
| DV-06 | Validate order date/status logic and incomplete periods | NOT RUN |
| DV-07 | Reconcile eligible line sales and units with original source | NOT RUN |
| DV-08 | Compare header SubTotal with summed detail where appropriate; separate tax/freight | NOT RUN |
| DV-09 | Independently test order, customer, growth, discount and RFM metrics | NOT RUN |
| DV-10 | Validate historical-cost intervals or exclude historical margin | NOT RUN |
| DV-11 | Test PivotTables, interactive filters and dashboard totals | NOT RUN |
| DV-12 | Ensure scenario inputs never change historical facts | NOT RUN |
| DV-13 | Repeat full Power Query refresh and check no stale values | NOT RUN |
| DV-14 | Verify Excel MCP operations by actual readback/save/reopen | NOT RUN |
| DV-15 | Inspect usability, dates, number formats, labels and empty states | NOT RUN |
| DV-16 | Review project links, source attribution and publication assets | NOT RUN |

## Independent spot checks

- Compare one selected sales order's raw header and lines to the fact table.
- Recalculate a month from source lines and compare to the dashboard.
- Ensure distinct order count differs from line count where expected.
- Validate one customer's RFM sequence against dated orders.
- Test a product with changing cost: at most one effective cost per sale.
- Confirm missing territory or product category members don't silently lose amounts.

## Acceptance and evidence

Each completed test needs a result (PASS/FAIL), date, workbook version and reproducible evidence. Jira task completion requires relevant checks to pass or have an explicit accepted exception. GitHub retains versioned formulas, source transformations and documentation.

No KPIs or test results should be described as *verified* without direct execution. See [Jira Workflow](JIRA_WORKFLOW.md) and [KPI Catalog](KPI_CATALOG.md).
