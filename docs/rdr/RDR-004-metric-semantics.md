# RDR-004 — Sales, Customer and Profitability Metric Semantics

- **Type:** Architecture
- **Status:** DRAFT
- **Priority:** High
- **Created:** 2026-11-03
- **Gate:** NOT RUN
- **Owner approval:** PENDING
- **Depends on:** [RDR-001](RDR-001-scope-and-oltp.md), [RDR-002](RDR-002-ingestion-and-model.md)

## Problem statement

An attractive dashboard can produce misleading totals if sales lines, orders, discounts, costs, dates and customer identities are defined inconsistently. The project requires one documented semantic contract before the first KPI is built.

## Research findings

| Class | Finding | Evidence | Check |
| --- | --- | --- | --- |
| DOCUMENTED | AdventureWorks is an OLTP sample with distinct sales header/detail entities. | [Microsoft official OLTP sources](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works/oltp-install-script) | Validate exact fields, source version |
| ASSUMED | `SalesOrderDetail.LineTotal` is a suitable canonical measure of discounted line sales. | Standard model interpretation | Verify expression, status inclusion and reconciliation |
| ASSUMED | Product cost history permits historically correct gross margin per sales line. | Candidate field availability | Test effective date coverage/semantics |
| ASSUMED | OnlineOrderFlag alone determines user-friendly commercial channel categories. | Field-name inference | Verify business meaning; prevent incorrect reseller label |
| ASSUMED | Customer purchases can support meaningful RFM scores across sample dates. | Analytical design | Check customer population and observed windows |

## Alternatives

| Option | Advantage | Risk |
| --- | --- | --- |
| Header-level `TotalDue` as 'revenue' | Includes order-level charges | Mixed tax/freight and duplication if joined to details |
| **Line-based discounted sales** (proposed) | Additive by product, territory and customer | Excludes separately modeled tax/freight; labels must be exact |
| Use current product cost for all historic transactions | Simple | Historically incorrect margin |
| Defer profit until temporal cost is verified | Preserves integrity | Fewer initial KPIs |

## Proposed design

- Use **eligible sales-line discounted amount** as the primary sales measure, with a name that does not imply collected cash or tax-inclusive revenue.
- Count orders distinctly at header level; count units at detail level.
- Use a clearly defined `OrderDate` or other selected event date, filter statuses consistently and identify incomplete periods.
- Define weighted discount by eligible undiscounted line value, not by unweighted averaging.
- Segment by observed `CustomerID`, with Person/Store classifications validated.
- Use RFM based on the observed history and an explicit analysis-as-of date.
- Treat **historical gross margin** as a conditional extension; omit it if a trustworthy cost matching rule cannot be demonstrated.
- Simulate pricing/discounting without altering actual historical facts, and do not imply customer price elasticity.

## Critical assumptions and mitigations

1. **Business date/status:** Phase 1 sampling and status-aware reconciliation.
2. **Header/line totals:** separate amount concepts and test no multiplication.
3. **Historical cost:** interval uniqueness and effective-date test; block margin until PASS.
4. **Channels:** precise source field descriptions and honest naming.
5. **Unknown dimensions:** explicit category to avoid silently losing sales.

## Review and decision gate

- Structural review: NOT RUN
- Assumption audit: NOT RUN
- Independent critique: NOT RUN
- Owner acceptance: PENDING
- RDR status: DRAFT

## Implementation outcome

**NOT IMPLEMENTED.** No actual KPI values, RFM scores or gross margins generated.

## References

[KPI Catalog](../KPI_CATALOG.md) · [Validation Plan](../VALIDATION_PLAN.md) · [Source Map](../SOURCE_MAP.md)
