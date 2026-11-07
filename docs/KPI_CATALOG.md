# KPI Catalog — Draft Business Definitions

**Status:** The four initial shipped sales measures have been implemented and checked locally; see [sales and units validation](validation/2026-11-07-awbi-11-prototype.md) and [orders and AOV validation](validation/2026-11-07-awbi-13-orders-aov.md). Other definitions remain planned and subject to validation.

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

For the initial analytical view, display aggregated line sales to two decimal places without rounding individual lines before summing. The model uses floating-point values; compare against decimal source aggregation with an absolute tolerance below 0.005, not as fixed-decimal accounting. `LineTotal` represents discounted order-line value; it excludes header tax and freight. The selected source does not establish a return or refund adjustment, so label this as shipped order-line sales, not net revenue after returns. Validate currency and return handling before publication.

## Customer intelligence

Use a stated `CustomerID`, analysis-as-of date and observation window for **RFM**:

- **Recency:** days since the last observed qualifying order.
- **Frequency:** number of distinct qualifying orders.
- **Monetary:** discounted line sales for those orders.

Scoring bands, ties and customer segment names must be recorded as modeling choices. The first purchase **observed in the sample** may not be the customer's first-ever transaction.

The local RFM base uses the fixed 2022-05-30 to 2025-06-29 sample window and a 2025-06-29 as-of date. Under a category filter, measures refer to qualifying orders and lines in that category; the fixed whole-sample score bands do not change. Bikes and Accessories were checked in the mixed-status fixture, and Bikes in the main workbook; other product and combined filters remain unverified. See [category RFM validation](validation/2026-11-07-awbi-20-category-rfm.md). Fixed scoring bands, tie handling and descriptive segments are documented in [RFM scoring validation](validation/2026-11-07-awbi-16-rfm-segments.md); they do not predict customer behavior.

## Channel, cost and scenarios

`OnlineOrderFlag` is a possible order-type dimension. Its semantics must be checked before calling it Internet/reseller or online/offline in a published chart.

A product's current standard cost may not represent the cost at an older sale. Use validated cost history or omit the historical gross-profit metric. Pricing and discount scenario assumptions do **not** prove actual demand responses.

## Reconciliation tests

At the same eligibility filters, sales, units, distinct order count and customer count must match source data. Category and territory breakdown totals must reconcile including unknown members. Test customer RFM calculations against specific orders, and ensure a historical-cost join never multiplies sales rows.

See [Validation Plan](VALIDATION_PLAN.md). Jira tracks the implementation and review tasks; metric definitions live in this catalog.
