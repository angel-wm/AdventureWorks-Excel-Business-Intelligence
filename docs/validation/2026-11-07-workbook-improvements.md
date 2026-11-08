# Workbook improvements and consolidated controls

> **Historical checkpoint:** status, sheet positions and limitations below describe this record's original baseline. They are not live task status or current instructions. See the [evidence index](README.md) for later corrections and the current handoff.

**Date:** 2026-11-07. **Scope:** local Excel 365 workbook changes, source reconciliation and functional regression performed by the project assistant. This is not independent human acceptance or a public release.

## Baselines

The pre-change backup `data/backups/AdventureWorks-before-controls-simplification.xlsx` has SHA-256 `8b5aa45a23f49e9f1dd74dc95627045a99a5efe506dbe3bd7aed816890028e86`. The final saved review copy `data/AWBI-improvements-final.xlsx` has SHA-256 `f2c5b5d4242e4578e464d731b9eec4fa1146ba4e125233c6c682736802e02883`. Both are local ignored files. The final copy was saved from the main workbook after its full refresh and final readback.

## Corrections

- `CustomerOverview` shows its source warning only when reconciliation fails and now discloses the unresolved currency/comparability limitation.
- Category chart data spills from the current sales PivotTable rather than enumerating four categories or converting every lookup error to `#N/A`. Filtered categories leave the plotted series; source errors remain visible in the support data.
- Monthly dates spill from the loaded shipped-order date span. Sales use dynamic daily ranges, with expected gaps for months outside the selected context. The fixed 38-month output and 5,000-row source bound were replaced.
- Customer counts and segment counts use dynamic named ranges and find the segment column by header. They check the expected row-header structure, a single segment header, non-empty IDs and consistency with the number of numeric IDs in the source column. The 20,000-row limit was removed. Gaps or incompatible headers produce a visible source check.
- The sales overview's date caption follows loaded shipped-order dates. Explanatory notes were moved outside the expanding category PivotTable footprint; its top captions retain the amount, AOV, order-count and margin boundaries.

These formulas rely on the current contiguous native PivotTable row layout and its expected header/total labels. They do not establish support for arbitrary schema changes. RFM retains its original fixed observation window and score thresholds.

The connector could not bind chart series to dynamic workbook names. Four chart reference fields were updated in the disposable workbook package, which was reopened in Excel. Native chart readback verified the named references and plotted values. Excel's subsequent Save As updated the workbook qualifiers to `AdventureWorks-BI.xlsx`; final refresh and chart readback retained the references. Chart names are now unique.

## Four control sheets reduced to two

The workbook now has **18 visible worksheets**. `Validation` and `KeyChecks` replace the previous four control sheets:

| Sheet | Role |
| --- | --- |
| `Validation` | 18 live results and an overall status. Compares current source-query totals with loaded sheets and a native Data Model PivotTable. The detailed territory/category PivotTable, now at `G43`, retains shipped sales, units, orders, AOV and the all-status line-sales measure. A link opens that detail. |
| `KeyChecks` | The existing 25 key/join checks plus the new `SourceChecks` query table, containing 15 current-source metrics, including shipped eligibility, pricing-expression mismatches and per-order subtotal differences of at least 0.005. |

The old `Validation` summary was replaced, `SalesMeasuresCheck` was consolidated and renamed to `Validation`, and the three overlapping `ModelChecks` PivotTables were removed. The original diagnostic measures were retained in the model. Fixed decimal reference totals are labeled as informational pinned-sample references and are excluded from the live overall status.

Final order: `SalesOverview`, `SalesMonthly`, `CustomerOverview`, `SalesScenario`, `SalesByDate`, `CustomerRFM`, `RFMGuide`, `Validation`, `KeyChecks`, `SalesChartData`, `SourceConfig`, followed by the seven loaded source sheets.

## Executed checks

| Check | Outcome |
| --- | --- |
| Complete refresh on disposable copy and final main workbook | Both succeeded: 9 Power Query loads, the model connection and 4 PivotTables; no reported failures |
| Final structure | 18 sheets, 10 worksheet tables, 7 model tables, 6 active relationships, 4 PivotTables and 3 charts |
| Native error scan after main refresh | Zero error cells across the used ranges of all 18 sheets in the restored unfiltered state |
| Source preservation and workbook links | All seven original CSV hashes still matched the initial source record; Excel reported no external workbook links |
| Final formula inspection | No `#REF!` in saved worksheet formulas; no cached error cells in reviewed analysis/control sheets |
| Final live controls | All 18 results `OK`; all 25 key/join controls zero |
| Source reconciliation | 109846381.399888 decimal sales versus 109846381.3998877 in Excel; 274914 units and 31465 shipped orders matched exactly |
| Monthly reconciliation | All 38 months matched independent decimal aggregation within 0.005; maximum difference 0.0000000597 |
| Full customer RFM reconciliation | All 19119 customer rows matched the source-based fixed-window values, scores and segments; customer sets matched and no duplicate customer rows were found |
| Combined sales interaction | Australia, Bikes, June 2022: 199477.9346 source sales, 59 units, 59 orders; overview, monthly result, scenario baseline and the one-point category chart matched |
| Scenario | +10% price and 5% additional discount on that selection produced 208454.441657, a 4.5% change; +150% input produced unavailable output; inputs restored to zero |
| RFM category filters | Bikes: 9719 customers; Accessories: 15461; Clothing: 7327; Components: 580. All five segment counts in each category matched independent source aggregation. Filter restored to all categories |
| Dynamic chart fixtures | A fifth synthetic support-data category produced five plotted points; an extra output month produced 39 points. These test range/series growth, not an end-to-end refresh with new source categories or dates. Formulas restored |
| Error visibility fixture | A deliberate division-by-zero in chart support remained visible as an error; source formula restored |
| Customer source guards | An isolated numeric ID at row 20000 and a changed segment header each produced `CHECK SOURCE`; clearing/restoring them returned to `OK` and removed the warning |
| Daily source guard | An isolated numeric date at row 5000 made monthly output unavailable; clearing it restored the output |
| Live control failure fixture | Overriding the copied source line-sales metric caused `CHECK DETAILS`; restoring it returned `OK` |

Failure fixtures ran only in the disposable copy and were restored before it became the main workbook. The original main workbook's cell contents were compared with the pre-change backup before replacement and had no differences. Final promotion restored the workbook-relative source-folder formula and native readback confirmed the intended local source directory.

The workbook was saved and left visible on `Validation`. These checks do not cover every filter combination, arbitrary data growth, every refresh path or another computer. Currency interpretation remains unresolved; return/refund adjustments remain excluded. The owner declined a cross-computer test. Commit, remote publication and human review remain separate steps.
