# Validation & Acceptance Plan

**State:** DRAFT. Every check below is **NOT RUN**. Passing a design review does not mean the workbook or dataset has been validated.

## Evidence tiers

- **Documented:** external reference or source documentation supports the claim.
- **Verified:** checked directly against the selected data, working Excel object, or executed tests.
- **Assumed:** provisional design hypothesis; must be resolved if material.

## Planned tests

| ID | Area | Acceptance check | Status |
| --- | --- | --- | --- |
| DV-01 | Source provenance | Official source version/URL, original file checksums and file-list recorded | NOT RUN |
| DV-02 | Schema | Delimiter, encoding, types, and mapping match selected official install script | NOT RUN |
| DV-03 | Key integrity | Core sales-line and order keys unique at intended grain; nulls measured | NOT RUN |
| DV-04 | Relationship integrity | Foreign keys match; unassigned members surfaced; no accidental many-to-many | NOT RUN |
| DV-05 | Join cardinality | Sales-line count and pre/post-join amount preserved | NOT RUN |
| DV-06 | Temporal rules | Observed date range, chosen order date, status filtering, partial periods tested | NOT RUN |
| DV-07 | Sales reconciliation | Sum of eligible line amounts and units matches source at same filter | NOT RUN |
| DV-08 | Header reconciliation | Sum of eligible lines and header SubTotal compared with documented exclusions; Tax/Freight not silently mixed | NOT RUN |
| DV-09 | KPI accuracy | Counts, AOV, growth, weighted discount and segmentation sampled independently | NOT RUN |
| DV-10 | Profitability | Historical cost chosen and effective-date rules validated or KPI excluded | NOT RUN |
| DV-11 | Pivot/filter behavior | Cross-filter totals consistent and slicers point to compatible sources | NOT RUN |
| DV-12 | Scenario isolation | Changing assumptions does not rewrite historical sales facts | NOT RUN |
| DV-13 | Refresh | Re-run ingestion without manual source edits; no error or stale outputs | NOT RUN |
| DV-14 | Excel MCP | Tool capability trials, readback, save/reopen and failure handling verified | NOT RUN |
| DV-15 | Usability | Dashboard readability, navigation, labels, empty states and definitions inspected | NOT RUN |
| DV-16 | Portfolio release | Documentation, source credits, licensing choices and evidence complete | NOT RUN |

## Independent calculation examples

- Compare a sample of `SalesOrderID` orders from raw `SalesOrderDetail` with transformed fact rows.
- Check distinct order count separately from the count of line items.
- Recalculate weighted discount by multiplying line quantity × unit price and subtracting stored eligible line sale amount.
- For one customer, inspect chronological orders before accepting RFM frequency/recency.
- For one product with cost changes, confirm exactly one applicable cost interval, or make profit unavailable.
- Test null/unknown territory without dropping transaction value from the total.
- Recalculate a monthly sales period directly from the source to catch filter and date errors.

## Gate rules

- Phase 1: no unverified critical assumptions in the agreed model or KPI contracts.
- Phase 2: DV-01 through DV-08 and DV-13 pass, with documented exceptions.
- Phase 3: DV-09 through DV-12, DV-14 and relevant visual checks pass.
- Phase 4: DV-01 through DV-16 pass or have explicitly accepted, visible noncritical exclusions.

**No test results or business numbers have been asserted here.** Add date, owner, workbook version, evidence location and findings when checks are actually executed.
