# KPI Catalog — Proposed Commercial Semantics

**Status:** DRAFT · All metrics require source validation. **No observed values, targets or baselines exist yet.**

## Principles

- Every KPI specifies **grain**, calculation, date basis, dimensions, exclusions, and validation.
- Never mix **order-header totals** with **sales-line totals** as though they had the same additive grain.
- `SalesOrderDetail.LineTotal` is a candidate canonical discounted line-sales amount; validate how it is computed and stored.
- Sales totals must specify whether tax, freight, returns and canceled orders are included.
- Use the sample's observed dates; do not invent recent 2026 sales.
- Segment thresholds and scenario inputs are **assumptions**, not discovered business truths.

## Priority KPIs

| ID | KPI | Proposed definition | Grain / notes |
| --- | --- | --- | --- |
| KPI-01 | Line Sales | `SUM(SalesOrderDetail[LineTotal])` for valid selected orders | Sales line; amount after applicable line discount, before header-level charges, subject to verification |
| KPI-02 | Order Count | `DISTINCTCOUNT(SalesOrderHeader[SalesOrderID])` for selected orders | Header count, not line count |
| KPI-03 | Units Sold | `SUM(SalesOrderDetail[OrderQty])` | Sales line |
| KPI-04 | Average Order Value | KPI-01 / KPI-02 | Only comparable when line/header populations match |
| KPI-05 | Month-over-Month Sales Growth | (Current month KPI-01 / Previous comparable month KPI-01) - 1 | Blank/N/A for no valid prior period; avoid partial-month misinterpretation |
| KPI-06 | Distinct Purchasing Customers | Distinct `CustomerID` with qualifying orders | Selected time range and order status |
| KPI-07 | Repeat Customer Rate | Customers with 2+ qualifying orders / purchasing customers | Same defined window; cannot infer lifetime behavior without historical coverage |
| KPI-08 | Revenue Share by Product / Territory | Group KPI-01 / all eligible KPI-01 | Cross-filter context and denominators documented |
| KPI-09 | Average Discount Rate | Weighted difference between undiscounted line price and realized line sales divided by undiscounted value | Prefer quantity-weighted discount, not arithmetic mean of rates |
| KPI-10 | Gross Profit / Gross Margin | Sales minus matched cost of goods; Gross Profit / Sales | **Conditional**: only if historical product cost at the sale date is justified |

## Customer segmentation (proposed)

**RFM** will be based on eligible orders: 
- **Recency:** elapsed days from a defined analysis/as-of date to the most recent qualifying order.
- **Frequency:** qualifying distinct orders, not line rows.
- **Monetary:** cumulative KPI-01 over the agreed observation window.
- **Customer identity:** `CustomerID`, with Person and Store subtypes labeled accurately.

Any RFM scoring cutoffs (quantiles, fixed bands) and handling of tied scores must be disclosed as model choices. New versus repeat is based on first **observed** purchase in the available dataset, not necessarily the customer's actual first-ever transaction.

## Channels and profitability

- `OnlineOrderFlag` is a candidate segmentation field; its exact meaning must be verified before labeling chart series. Do not claim offline = reseller automatically.
- Do not merge manufacturer, reseller and Internet concepts without field-level evidence.
- List prices and standard costs may change. Using **current** `Product.StandardCost` against older transactions can materially misstate historical margin. Validate `ProductCostHistory` effective intervals or omit KPI-10.
- Simulated price/discount changes affect a **scenario**, not the observed historical record; demand elasticity is not inferred.

## Control and reconciliation requirements

1. KPI-01 equals the eligible source line-total sum at identical filters.
2. Header-level and line-level order populations match under the chosen inclusion rule.
3. KPI-02 is not multiplied by order detail cardinality.
4. Territory/category/customer totals reconcile to KPI-01 including explicit '(Unknown)' members where needed.
5. Weighted discount calculation matches source arithmetic for sampled orders.
6. Historical-cost join preserves one cost row per eligible sales line.
7. Date comparisons exclude or flag incomplete periods.

Related: [RDR-004](rdr/RDR-004-metric-semantics.md), [Validation Plan](VALIDATION_PLAN.md).
