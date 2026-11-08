# KPI Catalog — Delivered Definitions

**Status:** Delivered workbook definitions and explicitly scoped report metrics. The [evidence index](validation/README.md) identifies current and historical checks; [Scope decisions](DECISIONS.md#metric-scope) explains exclusions. A listed optional definition is not a delivered workbook feature.

## Order eligibility

For the main sales analysis, include orders with `SalesOrderHeader.Status = 5` (shipped). This does not establish payment or accounting revenue recognition. Analysis of pending orders is deferred for a future decision. Return exclusions and accepted verification boundaries are recorded in [Scope decisions](DECISIONS.md).

The sales dashboard uses `OrderDate` as its analysis date and the four delivered sales measures below. The selected source contains order dates from 2022-05-30 through 2025-06-29; these are sample dates, not current business activity. Boundary months and selected date ranges can be partial; use comparable complete periods for comparisons. Return adjustments are excluded.

## Core sales metrics

| KPI | Rule | Delivery status / boundary |
| --- | --- | --- |
| Discounted Line Sales | Sum eligible `SalesOrderDetail.LineTotal` | Workbook: `Shipped Sales`; currency unconfirmed |
| Order Count | Distinct eligible detail `SalesOrderID` | Workbook: `Shipped Orders`; not line count |
| Units Sold | Sum eligible detail `OrderQty` | Workbook: `Shipped Units` |
| Average Order Value | Shipped Sales / Shipped Orders | Workbook: `Shipped AOV`; selected lines per qualifying order |
| Purchasing Customers | Distinct qualifying `CustomerID` | Workbook RFM population and customer dashboard |
| Repeat Customer Rate | Customers with at least two qualifying orders / purchasing customers in the same cohort/window | Source-derived business review; not a workbook KPI |
| Comparable-year volume growth | Current complete-year units or orders / prior complete-year value − 1 | Business review: 2024 vs 2023; not monetary growth |
| Monthly Sales Growth | Current monthly sales / prior comparable month − 1 | Not implemented; partial contexts and currency require explicit treatment |
| Sales Share | Selected sales / relevant filtered total | Not implemented as a separate KPI; denominator/currency semantics would need validation |
| Weighted Discount Rate | (Undiscounted − discounted line value) / undiscounted line value | Not implemented; no discount-effectiveness requirement |
| Gross Profit / Margin | Sales − justified historical cost; profit / sales | Conditional exclusion: historical-cost method unvalidated |

Under a product-category filter, AOV divides the selected category's eligible line sales by the distinct orders containing those lines. It is not the full value of those orders. Order counts across categories can overlap and must not be added together.

**Sales labeling matters:** Do not silently mix order-header `TotalDue` (which can include taxes/freight) with discounted line sales. Use the eligibility, amount and return boundaries in this catalog; these define the delivered measures.

For the initial analytical view, display aggregated line sales to two decimal places without rounding individual lines before summing. The model uses floating-point values; compare against decimal source aggregation with an absolute tolerance below 0.005, not as fixed-decimal accounting. `LineTotal` represents discounted order-line value; it excludes header tax and freight.

### Returns boundary

Describe sales as **shipped order-line sales without return or refund adjustments**. The shipped-sales measure sums eligible line values and does not join or subtract a return or refund dataset. A later return therefore is not reflected as a separate reduction by this measure; the presence or absence of actual returns is not established. Do not describe the result as net sales after returns or as recognized accounting revenue. This limitation also applies to AOV, RFM monetary values and the scenario baseline derived from shipped sales. The scenario does not model returns. If net-after-returns reporting becomes a requirement, it needs an appropriate source, matching rules and separate validation.

### Currency boundary

The owner accepted **original source monetary amounts; currency unconfirmed; no conversion** on 2026-11-08. Source semantics and the meaning of missing exchange-rate references were investigated but not resolved by the reviewed Microsoft OLTP documentation. This is a closed, accepted source limitation for this scope, not a pending conversion task.

Do not label amounts as confirmed USD, assume that different currencies are mixed, or claim verified monetary comparability. The qualification applies to AOV, monetary RFM scores/segments and scenario amounts. The [currency decision](DECISIONS.md#currency) retains the official sources and rationale. Workbook disclosures and independent arithmetic checks do not establish common-currency meaning.

## Customer intelligence

RFM uses `CustomerID`, the fixed observation window and analysis-as-of date described below:

- **Recency:** days since the last observed qualifying order.
- **Frequency:** number of distinct qualifying orders.
- **Monetary:** discounted line sales for those orders.

Scoring bands, ties and customer segment names are explicit modeling choices recorded in `RFMGuide` and the [scoring evidence](validation/2026-11-07-awbi-16-rfm-segments.md). The first purchase **observed in the sample** may not be the customer's first-ever transaction.

The local RFM base uses the fixed 2022-05-30 to 2025-06-29 sample window and a 2025-06-29 as-of date. Under a category filter, measures refer to qualifying orders and lines in that category; the fixed whole-sample score bands do not change. Bikes and Accessories were checked in the historical mixed-status fixture; all four category selections and their segment counts were reconciled in the [workbook improvements regression](validation/2026-11-07-workbook-improvements.md). The dashboard checks below extend this to category/segment combinations; other product-level contexts remain unverified. See [category RFM validation](validation/2026-11-07-awbi-20-category-rfm.md). Fixed scoring bands, tie handling and descriptive segments are documented in [RFM scoring validation](validation/2026-11-07-awbi-16-rfm-segments.md); they do not predict customer behavior.

### Customer dashboard summaries

`DashboardCustomers` summarizes the qualifying customer rows in `CustomerRFM`, intersected with the product-category selection and the RFM segment selector. `All` removes the segment restriction. Category changes the qualifying purchases used for RFM; segment selection narrows the resulting customer population without recomputing score thresholds.

| Indicator | Calculation |
| --- | --- |
| Observed customers | Count of numeric customer IDs in the selected population |
| Median recency | Median of the selected customers' RFM recency days |
| Median orders | Median of the selected customers' distinct qualifying order counts |
| Median customer sales | Median of the selected customers' unrounded RFM sales totals; display to two decimals |

These are customer-level medians, not averages of subgroup medians. The four charts show customer counts by segment, recency band, order-count band and rounded-sales band. The bands reuse the fixed rules in `RFMGuide` and [RFM scoring validation](validation/2026-11-07-awbi-16-rfm-segments.md); only monetary band assignment rounds each customer's total to two decimals. No-match selections show zero customers, unavailable medians and zero chart counts. A source-layout failure remains distinct from an empty selection.

The fixed observation window, cutoff, return exclusions and unresolved monetary comparability also apply here. The pooled person/store population uses shared bands for sample description, not equivalent commercial value; use the [separate cohort analysis](BUSINESS_REVIEW.md#customer-populations) before discussing actions. [Dashboard validation](validation/2026-11-08-dashboards.md) reconciles all 30 exposed category/segment combinations and the empty category against independent source aggregation.

## Channel, cost and scenarios

`OnlineOrderFlag` records order entry: 0 = salesperson placed, 1 = customer placed online, per the [official source](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script/instawdb.sql#L6420). The [business review](BUSINESS_REVIEW.md#order-entry-method) delivers a pinned-source comparison. This is not automatically reseller classification and is not an additional dashboard filter.

A product's current standard cost may not represent the cost at an older sale. Use validated cost history or omit the historical gross-profit metric. Pricing and discount scenario assumptions do **not** prove actual demand responses.

## Reconciliation tests

At the same eligibility filters, sales, units, distinct order count and customer count must match source data. Category and territory breakdown totals must reconcile including unknown members. Test customer RFM calculations against specific orders, and ensure a historical-cost join never multiplies sales rows.

See [Validation Plan](VALIDATION_PLAN.md). Jira tracks the implementation and review tasks; metric definitions live in this catalog.
