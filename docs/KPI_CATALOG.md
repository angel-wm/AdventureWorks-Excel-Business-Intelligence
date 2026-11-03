# KPI Catalog — Draft Business Definitions

**Status:** Planned. No KPI has been calculated or verified. Definitions become final only after the source/date/status choices are confirmed.

## Core sales metrics

| KPI | Intended rule | Important boundary |
| --- | --- | --- |
| Discounted Line Sales | Sum eligible `SalesOrderDetail.LineTotal` | Candidate sales measure; verify calculation and which statuses are eligible |
| Order Count | Distinct eligible `SalesOrderID` | Never count sales lines as orders |
| Units Sold | Sum eligible `SalesOrderDetail.OrderQty` | Sales-line grain |
| Average Order Value | Discounted Line Sales / Order Count | Numerator and denominator must cover the same orders |
| Monthly Sales Growth | Current monthly sales / prior comparable month − 1 | Missing/partial months need clear treatment |
| Purchasing Customers | Distinct qualifying `CustomerID` | Selected time window and order status |
| Repeat Customer Rate | Qualifying customers with at least two orders / purchasing customers | Observed behavior, not necessarily lifetime behavior |
| Sales Share | Selected product/territory sales / relevant total | Explicit denominator and filters |
| Weighted Discount Rate | (Undiscounted line value − discounted line value) / undiscounted line value | Do not average discount percentages unweighted |
| Gross Profit / Margin | Line sales − justified cost of goods; gross profit / line sales | **Conditional** on a defensible historical-cost method |

**Sales labeling matters:** Do not silently mix order-header `TotalDue` (which can include taxes/freight) with discounted line sales. Define dates, status exclusions, discounts, returns, cancellations, and all monetary amounts precisely before dashboard release.

## Customer intelligence

Use a stated `CustomerID`, analysis-as-of date and observation window for **RFM**:

- **Recency:** days since the last observed qualifying order.
- **Frequency:** number of distinct qualifying orders.
- **Monetary:** discounted line sales for those orders.

Scoring bands, ties and customer segment names must be recorded as modeling choices. The first purchase **observed in the sample** may not be the customer's first-ever transaction.

## Channel, cost and scenarios

`OnlineOrderFlag` is a possible order-type dimension. Its semantics must be checked before calling it Internet/reseller or online/offline in a published chart.

A product's current standard cost may not represent the cost at an older sale. Use validated cost history or omit the historical gross-profit metric. Pricing and discount scenario assumptions do **not** prove actual demand responses.

## Reconciliation tests

At the same eligibility filters, sales, units, distinct order count and customer count must match source data. Category and territory breakdown totals must reconcile including unknown members. Test customer RFM calculations against specific orders, and ensure a historical-cost join never multiplies sales rows.

See [Validation Plan](VALIDATION_PLAN.md). Jira tracks the implementation and review tasks; metric definitions live in this catalog.
