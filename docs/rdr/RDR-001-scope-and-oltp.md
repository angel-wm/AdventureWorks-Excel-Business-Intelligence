# RDR-001 — OLTP Scope and Portfolio Direction

- **Type:** Architecture
- **Status:** DRAFT
- **Priority:** High
- **Created:** 2026-11-03
- **Gate:** NOT RUN
- **Owner approval:** PENDING (OLTP choice already expressed; formal RDR review pending)
- **Related:** [RDR-002](RDR-002-ingestion-and-model.md), [Project Brief](../PROJECT_BRIEF.md)

## Problem statement

Choose a source variant and project boundary that demonstrates commercial analytics and BI while remaining materially different from the previously completed ProcureFlow operational system.

## Research findings

| Class | Finding | Evidence | Remaining check |
| --- | --- | --- | --- |
| DOCUMENTED | Microsoft provides AdventureWorks OLTP, Data Warehouse and Lightweight variants. | [Microsoft Learn](https://learn.microsoft.com/sql/samples/adventureworks-install-configure) | Confirm exact source snapshot |
| DOCUMENTED | Microsoft's official repository includes an OLTP installation script and per-table data files. | [Official source directory](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works/oltp-install-script) | Inspect schema and file formats during Phase 1 |
| VERIFIED (conversation decision) | Project owner selected OLTP and emphasized accelerated implementation with AI. | Project planning conversation, 2026-11-03 | Scope and RDR gate review |
| ASSUMED | A focused sales/customer/profitability slice can be completed in about 8–12 working days. | Planning estimate | Re-estimate after tool and data trials |

## Alternatives

| Option | Benefits | Tradeoffs |
| --- | --- | --- |
| OLTP | Rich source relationships; demonstrates transformation from transactions to BI | More schema analysis, joining and verification |
| AdventureWorksDW | Dimensional facts and attributes ready for analytics | Less original dimensional modeling work |
| AdventureWorksLT | Smallest and fastest source | Less analytical breadth |
| All OLTP modules | Maximum exploration | Uncontrolled complexity and duplicated operations use cases |

## Proposed design

Use **AdventureWorks OLTP**, but ingest only the sources needed for **Sales Performance, Customer Intelligence, Product/Profitability, Territory/Order-Type Analysis, and Scenarios**. Manufacturing remains optional and must justify scope expansion.

Build a decision-support analytical workbook rather than a procurement/inventory operations system. Favor meaningful KPI definitions and dimensional modeling over VBA orchestration and a very large sheet count.

## Assumptions and risks

- Sample source dates may not align with the present day. **Mitigation:** label actual observation periods.
- 'More OLTP tables' could expand scope. **Mitigation:** accept any additional table only against a question/KPI.
- Cost and channel semantics may be weaker than expected. **Mitigation:** downgrade or exclude metrics lacking support.
- Time estimate may be optimistic. **Mitigation:** recalibrate after first technical spike.

## Review and decision gate

- Structural review: NOT RUN
- Assumption audit: NOT RUN
- Independent critique: NOT RUN
- Owner acceptance: PENDING
- RDR status: DRAFT

## Implementation outcome

**NOT IMPLEMENTED.** The dataset has not been downloaded and no workbook exists.

## References

[Official Microsoft AdventureWorks installation guide](https://learn.microsoft.com/sql/samples/adventureworks-install-configure) · [RDR Index](README.md)
