# KPI Catalog — Draft Business Definitions

**Status:** The four initial shipped sales measures have been implemented and checked locally; see [sales and units validation](validation/2026-11-07-awbi-11-prototype.md) and [orders and AOV validation](validation/2026-11-07-awbi-13-orders-aov.md). Fixed-window RFM and the dashboard summaries below are also implemented and checked within their recorded scope. Other definitions remain planned and subject to validation.

## Order eligibility

For the main sales analysis, include orders with `SalesOrderHeader.Status = 5` (shipped). This does not establish payment or accounting revenue recognition. Analysis of pending orders is deferred for a future decision. Other date, return and calculation assumptions remain subject to validation.

The initial sales view uses `OrderDate` as the proposed analysis date, with the first four metrics below as its priority. The selected source contains order dates from 2022-05-30 through 2025-06-29; these are sample dates, not current business activity. Partial periods and the treatment of returns require review before publishing comparisons.

## Core sales metrics

| KPI | Intended rule | Important boundary |
| --- | --- | --- |
| Discounted Line Sales | Sum eligible `SalesOrderDetail.LineTotal` | Candidate sales measure; verify calculation against the selected source |
| Order Count | Distinct eligible `SalesOrderID` | Never count sales lines as orders |
| Units Sold | Sum eligible `SalesOrderDetail.OrderQty` | Sales-line grain |
| Average Order Value | Discounted Line Sales / Order Count | Numerator and denominator must cover the same orders |
| Monthly Sales Growth | Current monthly sales / prior comparable month − 1 | Missing/partial months need clear treatment |
| Purchasing Customers | Distinct qualifying `CustomerID` | Selected time window and order status |
| Repeat Customer Rate | Qualifying customers with at least two orders / purchasing customers | Observed behavior, not necessarily lifetime behavior |
| Sales Share | Selected product/territory sales / relevant total | Explicit denominator and filters |
| Weighted Discount Rate | (Undiscounted line value − discounted line value) / undiscounted line value | Do not average discount percentages unweighted |
| Gross Profit / Margin | Line sales − justified cost of goods; gross profit / line sales | **Conditional** on a defensible historical-cost method |

Under a product-category filter, AOV divides the selected category's eligible line sales by the distinct orders containing those lines. It is not the full value of those orders. Order counts across categories can overlap and must not be added together.

**Sales labeling matters:** Do not silently mix order-header `TotalDue` (which can include taxes/freight) with discounted line sales. Define dates, status exclusions, discounts, returns, cancellations, and all monetary amounts precisely before dashboard release.

For the initial analytical view, display aggregated line sales to two decimal places without rounding individual lines before summing. The model uses floating-point values; compare against decimal source aggregation with an absolute tolerance below 0.005, not as fixed-decimal accounting. `LineTotal` represents discounted order-line value; it excludes header tax and freight.

### Returns boundary

Describe sales as **shipped order-line sales without return or refund adjustments**. The shipped-sales measure sums eligible line values and does not join or subtract a return or refund dataset. A later return therefore is not reflected as a separate reduction by this measure; the presence or absence of actual returns is not established. Do not describe the result as net sales after returns or as recognized accounting revenue. This limitation also applies to AOV, RFM monetary values and the scenario baseline derived from shipped sales. The scenario does not model returns. If net-after-returns reporting becomes a requirement, it needs an appropriate source, matching rules and separate validation.

### Currency boundary

The owner accepted using **source monetary amounts; currency not confirmed** as the interim description while the source semantics are investigated. Do not label amounts as confirmed USD or apply a currency conversion without evidence. The current aggregate has not been established as a sum of values in a single currency; it must not be presented as a confirmed comparable monetary total across currencies.

In the pinned sample, 13,976 of 31,465 order headers have a `CurrencyRateID`; the other 17,489 have none. The referenced IDs match 2,514 distinct records in Microsoft's [CurrencyRate.csv at the pinned revision](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script/CurrencyRate.csv), all with USD as the source currency and AUD, CAD, FRF, GBP, DEM or EUR as destinations. The [source schema](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script/instawdb.sql) defines the rate reference and line-total calculation, but the reviewed definitions do not establish the currency stored in each line or the interpretation of missing rate IDs. These observations do not prove whether a conversion is required.

Currency warnings were added to the sales, scenario and customer RFM views and read back in Excel; see [currency and returns review](validation/2026-11-07-currency-returns-review.md). Continue seeking source evidence for the currency interpretation.

## Customer intelligence

Use a stated `CustomerID`, analysis-as-of date and observation window for **RFM**:

- **Recency:** days since the last observed qualifying order.
- **Frequency:** number of distinct qualifying orders.
- **Monetary:** discounted line sales for those orders.

Scoring bands, ties and customer segment names must be recorded as modeling choices. The first purchase **observed in the sample** may not be the customer's first-ever transaction.

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

The fixed observation window, cutoff, return exclusions and unresolved monetary comparability also apply here. [Dashboard validation](validation/2026-11-08-dashboards.md) reconciles all 30 exposed category/segment combinations and the empty category against independent source aggregation.

## Channel, cost and scenarios

`OnlineOrderFlag` is a possible order-type dimension. Its semantics must be checked before calling it Internet/reseller or online/offline in a published chart.

A product's current standard cost may not represent the cost at an older sale. Use validated cost history or omit the historical gross-profit metric. Pricing and discount scenario assumptions do **not** prove actual demand responses.

## Reconciliation tests

At the same eligibility filters, sales, units, distinct order count and customer count must match source data. Category and territory breakdown totals must reconcile including unknown members. Test customer RFM calculations against specific orders, and ensure a historical-cost join never multiplies sales rows.

See [Validation Plan](VALIDATION_PLAN.md). Jira tracks the implementation and review tasks; metric definitions live in this catalog.
