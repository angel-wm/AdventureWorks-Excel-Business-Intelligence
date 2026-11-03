# RDR-002 — Reproducible OLTP Ingestion and Semantic Model

- **Type:** Architecture
- **Status:** DRAFT
- **Priority:** High
- **Created:** 2026-11-03
- **Gate:** NOT RUN
- **Owner approval:** PENDING
- **Depends on:** [RDR-001](RDR-001-scope-and-oltp.md)

## Problem statement

Transform OLTP order transactions into repeatable analytics without double counting sales, relying on unstable manual worksheet imports or presenting a flat joined table as a validated dimensional model.

## Research findings

| Class | Finding | Evidence | Check |
| --- | --- | --- | --- |
| DOCUMENTED | Official AdventureWorks OLTP is distributed via install scripts/data files and via SQL Server backups. | [Microsoft Learn](https://learn.microsoft.com/sql/samples/adventureworks-install-configure) | Select and pin snapshot |
| DOCUMENTED | SQL Server samples contains OLTP files named `SalesOrderHeader`, `SalesOrderDetail`, `Product`, `Customer` and other entities. | [Official OLTP directory](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works/oltp-install-script) | Inspect exact columns |
| ASSUMED | The CSV approach will be simpler to reproduce from Excel without SQL Server installation. | Architectural reasoning | Trial one source and compare |
| ASSUMED | An Excel Data Model can support the required star-schema-style joins at adequate performance. | Design hypothesis | Test actual workbook, memory and refresh |

## Alternatives

| Option | Benefit | Risk |
| --- | --- | --- |
| CSV + Power Query (proposed) | Portable and reproducible without server | Need positional field mappings and explicit key/type validation |
| SQL Server + Power Query | Native relational types and constraints | Additional database installation and configuration |
| Flat Excel sheet joins | Easy initial visuals | Duplication, file bloat, poor model semantics |

## Proposed design

- Read **unaltered official source files** via parameterized Power Query.
- Separate source access (`src_*`), staging (`stg_*`) and model outputs (`fact_*`, `dim_*`).
- Build one core sales fact at **SalesOrderDetail line grain**.
- Join/relate selected header attributes without counting header totals once per line.
- Build Date, Product, Customer, Territory and validated Channel/OrderType dimensions.
- Keep optional cost-history matching outside core sales until historical grain is verified.
- Use Power Pivot for relationships and measures if native capabilities allow. Use Excel sheets only where they provide clear value.
- Record each table's grain, row count, key checks and date coverage during Phase 1–2.

## Critical assumptions and tests

1. CSV headers/schema order: inspect Microsoft installation SQL script and verify imported field positions.
2. Sales order-line key uniqueness: profile raw values.
3. Joins: check sales lines count, subtotal and null dimensions before/after each enrichment.
4. Historic cost: require non-overlapping effective intervals or exclude margin.
5. Refresh: test one repeatable end-to-end refresh with stable output and saved workbook.
6. MCP: native Power Query and Data Model edits may require desktop fallback.

## Review and decision gate

- Structural review: NOT RUN
- Assumption audit: NOT RUN
- Independent critique: NOT RUN
- Owner acceptance: PENDING
- RDR status: DRAFT

## Implementation outcome

**NOT IMPLEMENTED.** No source data, Power Query M or Excel model generated.

## References

[Architecture](../ARCHITECTURE.md) · [Source Map](../SOURCE_MAP.md) · [Validation Plan](../VALIDATION_PLAN.md)
