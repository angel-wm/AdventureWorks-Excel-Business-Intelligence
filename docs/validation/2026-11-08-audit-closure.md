# Fourteen-point audit closure

**Date:** 2026-11-08. **Tracking:** [AWBI-21](https://angel231995.atlassian.net/browse/AWBI-21). **Artifact:** [AWBI-2026-11-08-audit-closure](../HANDOFF.md), identified by the SHA-256 in [handoff.json](../handoff.json). This record covers local corrections and assistant-run checks; the owner performs Git publication and version-linked acceptance.

## Authorization and scope

The owner explicitly accepted retaining original amounts with currency unconfirmed and no conversion, then authorized resolving all 14 audit points. Original phase acceptance and broader coverage exceptions remain intact. No new dataset was downloaded, no raw source was modified, and no external publication was performed by this follow-up.

## Audit disposition

| # | Finding | Resolution and evidence |
| --- | --- | --- |
| 1 | Currency interpretation | Closed as an accepted source limitation, with official-source investigation and consequences in [Scope decisions](../DECISIONS.md#currency); no unsupported conversion |
| 2 | Missing order-type closure | [Business review](../BUSINESS_REVIEW.md#order-entry-method) answers entry-method volume/source-amount questions using the official flag definition; report-only scope is explicit |
| 3 | Early implementation statuses | Brief and Jira workflow now distinguish delivered requirements from live issue state |
| 4 | Ambiguous KPI catalog | [Catalog](../KPI_CATALOG.md) identifies workbook metrics, report-only metrics and exclusions, with reasons in the decision record |
| 5 | Wrong phase dates | Current State records phase 1 and 2 closure on Nov 6, matching Jira status history |
| 6 | Publication wording | Current State distinguishes the previously authorized public baseline from uncommitted local corrections |
| 7 | Historical supersession | Every original dated record has a historical notice; the [evidence index](README.md) explains what changed and routes current instructions |
| 8 | Repeated maintained state | Current State owns dated state, Scope decisions owns exceptions, Handoff owns artifact/setup checks; other documents link to those sources |
| 9 | Non-rerunnable public checks | Standard-library [verification script](../../scripts/verify.py), command, retained JSON and failure behavior supplied |
| 10 | Unidentified final delivery | Artifact ID and exact workbook SHA-256 designated in the manifest; containing-commit convention avoids claiming an uncreated tag/release |
| 11 | Scenario hidden-sheet guidance | `SalesScenario!A3` now directs the reader to `DashboardSales`; its existing formula dependency is preserved |
| 12 | Intended vs exercised tools | [AI Workflow](../AI_WORKFLOW.md) distinguishes original MCP/native work from the add-in operations exercised in this follow-up |
| 13 | Missing business interpretation | Source-backed entry-method, complete-year volume and cohort findings, proposed decisions and causal limits added to the business review and README |
| 14 | Pooled customer interpretation | Cohort counts/repeat rates evaluated separately; shared bands retained only for sample description, with warnings in workbook and documentation |

## Requirements and exclusions

| Requirement | Delivered evidence |
| --- | --- |
| FR-01 Ingestion | Pinned source/hash contract and historical refresh/folder-move evidence; accepted portability limits |
| FR-02 Model | Source keys, seven model tables/six relationships and group reconciliations |
| FR-03 Sales dashboard | Current cards plus 38 monthly/40 territory-category saved-output comparisons; historical interaction checks |
| FR-04 Customer dashboard | All 19,119 fixed-window RFM rows and cards; historical 30-combination tests; cohort interpretation now explicit |
| FR-05 Product/territory | Category/territory comparisons and unknown-member/key controls, within tested scope |
| FR-06 Profitability | Permitted conditional exclusion: historical cost unvalidated and margin unavailable |
| FR-07 Scenario | Existing fixed-volume formulas/defaults and historical input tests; visible-control guidance corrected |
| FR-08 AI evidence | Exact add-in reads/writes/images, source computation and package-preservation checks; no independent human technical review implied |
| FR-09 Portfolio documentation | Maintained sources reconciled, current previews, public-ready runner and hash-addressed handoff; local publication boundary explicit |

No additional workbook entry-method filter, cohort-specific RFM score or optional monetary KPI is claimed. The business review supplies the missing analytical comparisons without adding redundant workbook views. Accepted source/schema, cross-computer and wider-filter exclusions are maintained in [Scope decisions](../DECISIONS.md#accepted-verification-boundary).

## Workbook operations

An ignored rollback was preserved at `data/backups/AdventureWorks-before-audit-closure.xlsx`. The signed-in ChatGPT pane was visually confirmed in the intended workbook before connected-session commands.

Exactly five final text-cell changes were intended: `SalesScenario!A3`, `DashboardCustomers!B55`, `CustomerRFM!A3`, and `RFMGuide!B3,B15`. The scenario instruction now names the visible dashboard. Customer notes explain the mixed population; `RFMGuide` no longer incorrectly limits category tests to Bikes and Accessories. Exact native readback confirmed the changes, scenario formulas/defaults and four customer indicators. Native images covered all four changed views and the sales dashboard. The two README previews were replaced with current native range captures.

Saving used the existing Excel MCP session; no new refresh or interactive-filter run was performed. The original workbook structure and analytical contracts are retained. Full cached-output reconciliation and an exact before/after worksheet-cell comparison are recorded below. The embedded binary model bytes differ after the native Excel save; byte identity was not established. Native metadata readback confirmed the same model tables, row counts and six active relationships. No model formula edit was requested or performed; output reconciliation provides bounded semantic evidence. Native provider failures from earlier work are not claimed to be fixed.

## Verification record

The [retained checker result](results/2026-11-08-checks.json) records its execution status and workbook hash. Source expectations are reconstructed from the seven CSVs using decimal arithmetic, not copied from workbook helper cells. A separate SQLite aggregation confirmed entry-method orders/units and cohort counts/repeat counts. All computations and workbook inspections were performed by the project assistant.

Executed outcomes:

| Check | Result |
| --- | --- |
| Public checker | PASS, exit 0; workbook hash matches designated manifest |
| Seven pinned inputs | Hashes and row widths match; source key/join checks zero |
| Full RFM comparison | 19,119 customers; customer set, dates, recency, frequency, sales, scores and segments match |
| Monthly / territory-category outputs | 38 monthly values and 40 groups match within the 0.005 monetary tolerance; counts exact |
| Current cards and scenario defaults | Match source; price/discount zero; historical scenario formulas preserved |
| Native structure/readback | 7 model tables with original row counts, 6 active relationships, 9 loads, 5 PivotTables, 10 charts; 18 controls OK |
| Before/after worksheet comparison | Exactly the five intended text cells differ; every other cell value/type/formula matches the rollback |
| Binary model comparison | Not byte-identical after Excel save; native metadata and output comparisons above passed; no full DAX definition readback claimed |
| Saved errors / links | Zero cached errors, zero worksheet formulas containing #REF!, zero external workbook link parts; local document links/anchors resolve |
| Failure fixture | A disposable source copy with a changed ProductCategory file returns FAIL and exit 1 before workbook comparison; original source untouched |
| Business report cross-check | Separate SQLite counts match Python entry-method orders/units and cohort purchasing/repeat counts |
| Presentation | Native images of the four changed views and sales dashboard inspected; current dashboard captures replace older README previews |

The preservation detail and raw live reads are local diagnostics; the table and current checker result retain the public reproducible scope. Historical refresh and interaction coverage is indexed separately; current saved-output checks do not establish arbitrary source changes or every live filter path.

## Publication and acceptance

The original public baseline is commit `30b4ea8f37e3ee6ab3ba1af6260708591ee00ac4`. The audit corrections are prepared locally. AWBI-21 stays In Review until the owner commits/publishes the artifact and the immutable version is linked and reviewed under the Jira workflow. No commit, push, tag, release or independent human acceptance of this follow-up is claimed here.
