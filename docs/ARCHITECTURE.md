# Proposed Architecture

**Design status:** DRAFT — no workbook, query or relationship currently exists.

## Data flow

```text
Official AdventureWorks OLTP sources (immutable)
    |
    v
Power Query: source access (src) -> preparation (stg)
    |
    v
Validated semantic layer: facts + dimensions
    |                           |
    v                           v
Excel Data Model / Power Pivot   limited Excel tables as needed
    |                           |
    +-----------+---------------+
                v
         KPIs and measures
                |
                v
      PivotTables / formulas
                |
                v
    Sales, Customers, Products
     and Scenario dashboards
```

## Intended grains and entities

- **Core sales fact:** one `SalesOrderDetail` line, uniquely identified by `SalesOrderID` + `SalesOrderDetailID` (verify source constraints).
- **Sales header attributes:** `SalesOrderHeader` joined many lines to one order. Do **not** repeat header-level monetary amounts as additive line measures.
- **Date:** one row per calendar day across the observed sale-date range.
- **Product:** one row per product; enrichment with product subcategory/category must preserve uniqueness.
- **Customer:** one row per customer identifier with careful differentiation of person and store customers; relationships to Person, Store and SalesTerritory need verified treatment.
- **Territory:** one row per territory, joined using the selected order-level territory where present.
- **Order type/channel:** derive from documented source attributes (e.g. `OnlineOrderFlag`); do not claim online/offline equals Internet/reseller without validation.
- **Scenario assumptions:** separate inputs table/sheet, not joined to transaction fact rows.

The above is a proposal, not a verified schema mapping; see [Source Map](SOURCE_MAP.md).

## Boundaries and modeling rules

1. Source files remain unchanged and must not be overwritten by tools.
2. Explicit data types, culture/decimal handling and null policy in Power Query.
3. Preserve row-count granularity across many-to-one enrichment; detect accidental duplicate product/customer keys.
4. Use a star-schema-like model where practical, without importing unrelated OLTP tables.
5. Use a single canonical sales measure and define optional headline variants explicitly.
6. Historical cost fields need effective-date or actual transaction-cost justification before publishing a gross-margin calculation.
7. Protect assumptions from being confused with observed historical sales.
8. Acknowledge that Excel Data Model relationships, DAX measures, slicers and Power Query steps may need direct desktop actions if the MCP lacks support.

## Proposed workbook navigation

- `00_README` — purpose, definitions, source and refresh notes.
- `01_CONTROLS` — date window / scenario inputs / data validation indicators.
- `10_DASH_Sales` — commercial overview.
- `11_DASH_Customers` — segmentation and recurrence.
- `12_DASH_Products` — product/territory and validated profitability.
- `13_SCENARIOS` — assumed price/discount outcomes.
- Supporting analysis sheets only where necessary; avoid one worksheet per source table.

These names may change after Phase 1.

## Refresh and maintainability

- Prefer explicit Refresh All and documented dependency order before custom VBA.
- Store source-path parameters outside hard-coded user-specific paths.
- Capture original source URL, snapshot/version, schema and checksum where possible.
- Track Power Query M and DAX/formula definitions as readable text when technically feasible, while the workbook remains the executable source.
- Document the observed refresh outcome, not an assumed success.

## RDR links

- [RDR-001](rdr/RDR-001-scope-and-oltp.md) — source selection and scope.
- [RDR-002](rdr/RDR-002-ingestion-and-model.md) — ingestion and dimensional model.
- [RDR-003](rdr/RDR-003-ai-execution.md) — AI automation boundaries.
- [RDR-004](rdr/RDR-004-metric-semantics.md) — metric definitions and guardrails.
