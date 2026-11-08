# What the sample supports

**Question:** how do order volume and observed repeat purchasing differ across entry methods and customer populations?

This report uses the seven pinned OLTP files, shipped orders and eligible lines from **2022-05-30 through 2025-06-29**. Customer recency is measured at **2025-06-29**. It is a fixed-source case study, not a live dashboard selection or a forecast. Reproduce the tables with [the verification command](HANDOFF.md#reproduce-the-checks); exact results are retained in the [checked output](validation/results/2026-11-08-checks.json).

## Order entry method

The [official source](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script/instawdb.sql#L6420) defines `OnlineOrderFlag` as entry method, not a complete reseller/customer classification.

| Entry method | Shipped orders with lines | Units | Source amount, currency unconfirmed |
| --- | ---: | ---: | ---: |
| Placed by salesperson (0) | 3,806 | 214,516 | 80,487,704.18 |
| Placed online by customer (1) | 27,659 | 60,398 | 29,358,677.22 |
| Total | 31,465 | 274,914 | 109,846,381.40 |

Online entry accounts for **87.9% of orders**, while salesperson entry accounts for **78.0% of units**. The mix shows that order count alone does not describe operational volume. It does not establish that one entry method causes larger orders or higher profitability.

**Proposed action:** size order-handling and fulfillment questions using both orders and units, and investigate customer/product mix before changing channel investment. Revenue comparisons remain conditional on the [currency decision](DECISIONS.md#currency).

## Comparable complete years

| Calendar year | Shipped orders with lines | Units |
| --- | ---: | ---: |
| 2023 | 3,830 | 66,441 |
| 2024 | 14,244 | 131,936 |
| Change | +271.9% | +98.6% |

Order volume grew faster than units in these two complete years. This supports investigating changes in order size and customer/product mix; it does not identify their cause. The report excludes the partial 2022 and 2025 source years from this comparison. Dashboard boundary months or user-selected dates can also be partial. No monetary growth or forecast is claimed.

## Customer populations

The counting grain is a qualifying `CustomerID`. Store-linked customers take precedence over person-linked contacts; person-only customers have a `PersonID` and no `StoreID`. This classification is distinct from order entry method.

| Cohort | Observed customers | Customers with at least two orders | Repeat rate | Median orders | Median recency, days |
| --- | ---: | ---: | ---: | ---: | ---: |
| Person only | 18,484 | 6,865 | 37.1% | 1 | 168 |
| Store linked | 635 | 605 | 95.3% | 4 | 91 |

Repeat rate is repeat customers divided by observed purchasing customers **within the same cohort and fixed window**. It is not lifetime retention, churn probability, or evidence that an intervention will work. Different exposure histories and commercial relationships may contribute; those explanations have not been tested.

Store-linked customers are **3.3% of the population** but **45.3% of the global Champions segment** (437 of 964). This demonstrates that pooled score interpretation depends materially on population mix. It does not establish superior profitability or equivalent monetary value, especially with currency unresolved.

**Decision:** retain global RFM bands as a descriptive view of this sample, and separate cohorts when discussing commercial actions. **Proposed action:** investigate follow-up opportunities among person-only customers with one observed order and account-service questions among stores separately. No automatic campaign, contact action, or cohort-specific score was implemented.

## Scenario as a decision aid

On `DashboardSales`, choose category, territory and dates. Open `SalesScenario`: its baseline follows those selections. A **+10% price change followed by a 5% additional discount** applies a multiplier of **1.045**, or **+4.5%** at fixed volume. Existing source reconciliation and scenario tests are indexed in [validation evidence](validation/README.md).

This shows the arithmetic required to offset a discount; it does not establish customer willingness to pay, demand elasticity, margin, tax, freight or returns. Restore both assumptions to zero and clear filters after exploring.

## Evidence and interpretation

`scripts/verify.py` independently joins source headers, lines and dimensions and reconstructs the fixed-window RFM values and cohort summaries. A separate SQLite aggregation checked entry-method orders/units and cohort repeat counts during this follow-up. Both were executed by the project assistant, not independent human reviewers.

Source amounts are reproduced unchanged and rounded only for display. Their currency and common-currency comparability remain unconfirmed. Monetary observations are illustrative; the operational findings above use counts, units and within-cohort frequencies. Source limitations, exclusions and the reason for retaining global RFM are maintained in [Scope decisions](DECISIONS.md).
