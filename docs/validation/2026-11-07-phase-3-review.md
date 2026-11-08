# Phase 3 evidence review

> **Historical checkpoint:** status, sheet positions and limitations below describe this record's original baseline. They are not live task status or current instructions. See the [evidence index](README.md) for later corrections and the current handoff.

**Date:** 2026-11-07. **Baseline:** local commit `5bf42e1504a24841eb78ef1e59c59721a8bbf83f`. This is an assistant review of the recorded evidence, not an independent human review or acceptance. Live issue status is maintained in Jira.

## Review scope

The assistant compared the phase 3 task criteria and dependencies with the validation records linked below. The current workbook file matched the Git blob at the baseline commit. The open Excel workbook was reported saved with AutoSave off. Readback covered the sales overview, scenario, monthly trend and customer overview; it did not repeat every prior interaction or read every model formula.

The original `SalesOrderHeader.csv` and `SalesOrderDetail.csv` hashes matched the initial load record. A new decimal aggregation of those files selected status 5 and compared the result with the current workbook:

| Check | Source calculation | Excel readback |
| --- | ---: | ---: |
| Shipped line sales | 109846381.399888 | 109846381.3998877 |
| Shipped units | 274914 | 274914 |
| Distinct shipped orders with lines | 31465 | 31465 |
| Monthly line sales | 38 months | All 38 matched within 0.005; maximum difference below 0.00000006 |

The current scenario readback showed a zero price change and zero additional discount, with scenario sales equal to the baseline. The customer overview showed 19,119 customers and segment counts of 964, 695, 6,359, 2,273 and 8,828, with reconciliation `OK`. These readbacks do not independently establish every customer score, interactive filter, chart or refresh path on the current baseline.

## Evidence and review boundaries

| Tasks | Evidence available | Review boundary |
| --- | --- | --- |
| [AWBI-11](2026-11-07-awbi-11-prototype.md), [AWBI-13](2026-11-07-awbi-13-orders-aov.md) | Original and mixed-status source reconciliations, grouping tests and formula readback | Interactive status selection was not established; currency and returns treatment remain open for publication. |
| [AWBI-14](2026-11-07-awbi-14-sales-view.md), [AWBI-18](2026-11-07-awbi-18-monthly-sales.md) | Source reconciliation and a representative territory/category/date interaction; chart and formula readback | Not all filter combinations or refresh paths were tested. The monthly range guard was read but its boundary was not exercised. |
| [AWBI-15](2026-11-07-awbi-15-customer-rfm.md), [AWBI-16](2026-11-07-awbi-16-rfm-segments.md), [AWBI-19](2026-11-07-awbi-19-customer-overview.md), [AWBI-20](2026-11-07-awbi-20-category-rfm.md) | Customer-level source comparisons, fixed scoring rules, segment checks and bounded category-filter tests | The category correction supersedes the earlier product-filter warning for the specific contexts tested. Other product and combined filters remain unverified; overview layout and row-limit guards were not exercised. |
| [AWBI-17](2026-11-07-awbi-17-sales-scenario.md) | Formula and input readback, arithmetic and representative filtered checks | Interactive validation dialog and an empty-baseline filter were not exercised; the scenario assumes fixed volume. |

The original records identify tests performed by the project assistant. Source aggregation is independent of Excel's computation, but that does not make the assistant an independent reviewer. Some historical record headers still describe their original pre-commit status; Jira and Git provide current status and versioning.

## Closure

The phase 3 exit gate requires key outputs independently validated against transformed or source data. The task workflow requires deliverables to work, relevant checks to pass or explicit exceptions to be accepted, and evidence to be traceable. The nine phase 3 tasks are in review, with dependencies between measures and views. Review their evidence and limitations before accepting the tasks and closing the epic; this record does not mark them Done. The baseline commit is local and publication has not been confirmed.
