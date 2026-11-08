# Validation Plan

**Status:** The owner accepted the documented coverage boundaries for phase 4, which was marked Done on 2026-11-08. Several broader checks remain unperformed; results below describe coverage, not blanket verification. See the [source evidence](validation/2026-11-06-initial-sales-load.md), [model evidence](validation/2026-11-06-model-relationships.md), [audit follow-up](validation/2026-11-07-audit-remediation.md), [dashboard validation](validation/2026-11-08-dashboards.md) and [owner review follow-up](validation/2026-11-08-workbook-review-follow-up.md) for baselines, dates and limitations.

## Coverage and accepted exclusions

| ID | Check | Coverage |
| --- | --- | --- |
| DV-01 | Record Microsoft source version, file provenance and hashes | Recorded for the selected snapshot |
| DV-02 | Validate CSV/schema mapping, data types and null handling | Partial: selected source checked; changed-source handling remains |
| DV-03 | Check primary keys, duplicates and nulls at intended grains | Partial: initial source and workbook checks; changed-source coverage remains |
| DV-04 | Confirm join cardinalities and foreign-key completeness | Partial: initial relationships checked; ongoing coverage needs review |
| DV-05 | Confirm sales-line counts and amounts survive enrichment | Partial: selected model breakdowns reconcile; broader enrichment remains |
| DV-06 | Validate order date/status logic and incomplete periods | Partial: shipped eligibility and a mixed-status fixture checked; representative date selection and partial-period disclosures checked; broader cases remain |
| DV-07 | Reconcile eligible line sales and units with original source | Selected snapshot and historical mixed-status fixture reconciled; currency semantics remain unresolved |
| DV-08 | Compare header SubTotal with summed detail where appropriate; separate tax/freight | Partial: source subtotals checked; broader reporting treatment remains |
| DV-09 | Independently test order, customer, growth, discount and RFM metrics | Sales, orders, units, AOV and fixed-sample RFM checked; the later business review adds cohort repeat rate and complete-year units/orders growth. Monthly monetary growth and weighted discount are excluded by scope |
| DV-10 | Validate historical-cost intervals or exclude historical margin | Historical margin excluded and labeled unavailable; historical cost remains unvalidated |
| DV-11 | Test PivotTables, interactive filters and dashboard totals | Combined sales selection, all 30 exposed RFM category/segment combinations, empty customer selection and restored totals checked; representative native chart values matched. Other filter dimensions and arbitrary combinations remain outside this coverage |
| DV-12 | Ensure scenario inputs never change historical facts | Fixed-volume formulas, representative inputs and invalid-input guard checked; not a demand model |
| DV-13 | Repeat full Power Query refresh and check no stale values | Nine-query full refresh and final readback passed on the main workbook; arbitrary changed-source ordering and freshness remain unestablished |
| DV-14 | Verify Excel MCP operations by actual readback/save/reopen | Partial: exercised operations checked; other operations remain unverified |
| DV-15 | Inspect usability, dates, number formats, labels and empty states | The assistant inspected dashboard captures and native exports; the owner subsequently reported completing a workbook review. The owner's report does not imply independent repetition of each technical check |
| DV-16 | Review project links, source attribution and publication assets | Source notice, README and dashboard previews recorded; the repository was made public with owner authorization. Current previews are native Excel range captures from the audit follow-up; earlier exports remain historical evidence |

The table records historical phase coverage. Broader cases described as remaining were accepted as outside this delivery's coverage in [AWBI-5](https://angel231995.atlassian.net/browse/AWBI-5), rather than being an implicit open backlog. The [scope decision record](DECISIONS.md#accepted-verification-boundary) owns these exceptions. Current previews and saved-output checks are indexed in [validation evidence](validation/README.md).

## Executable follow-up

Run the [regression suite and verification command](HANDOFF.md#reproduce-the-checks). Synthetic tests exercise valid and deliberately invalid output populations, values, headers, package structure and handoff identity; a disposable changed-source CLI fixture must exit 1. They do not validate Excel runtime behavior.

Against the pinned raw files and designated saved workbook, the verifier independently recomputes complete monthly/customer populations and group outputs, checks source hashes/schema/keys, dashboard cards, scenario defaults, package structure/errors, local links and required handoff identity. It also generates the entry-method, complete-year volume and person/store summaries in the business review. The [hardening record](validation/2026-11-08-verifier-hardening.md) and its retained result identify the execution and exact workbook hash.

This is saved-output verification: no Excel refresh, new interactive-filter run, direct DAX readback or independent human technical review is implied. The audit correction changed five text cells; native add-in readback/images and a before/after package comparison check preservation. The [closure record](validation/2026-11-08-audit-closure.md) records executed outcomes and failure-fixture results.

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
