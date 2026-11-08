# Validation evidence index

Read [Handoff](../HANDOFF.md) for the designated workbook and current controls, [Validation Plan](../VALIDATION_PLAN.md) for coverage, and [Scope decisions](../DECISIONS.md) for accepted exceptions. Jira owns live issue status. A dated record preserves what was observed on its own baseline, including any then-pending work; it is not automatically a current instruction.

## Current follow-up

- [2026-11-08 verifier hardening](2026-11-08-verifier-hardening.md): complete saved-output populations, 29 executable regression tests, mandatory package checks and publication-state reconciliation, without workbook edits.
- [Current verifier result](results/2026-11-08-verifier-hardening.json): verifier version 2, fresh source expectations and complete saved-output comparison for the designated workbook hash.
- [2026-11-08 audit closure](2026-11-08-audit-closure.md): original 14 dispositions and workbook readback, subsequently published in `431284a`; the [original result](results/2026-11-08-checks.json) preserves that earlier verifier's schema and execution.
- [Verification script](../../scripts/verify.py) and [regression tests](../../tests/test_workbook_checks.py): rerun using [Handoff](../HANDOFF.md#reproduce-the-checks). These do not refresh Excel or repeat every historical interaction test.

The current README previews were captured from the connected Excel workbook during this follow-up, after blank-category visibility and customer-note corrections. They are native range images, not the earlier PDF exports. Screenshot appearance is evidence of the captured view, not every possible filter state.

## Checkpoint progression

| Record | What it establishes | Later change / reading rule |
| --- | --- | --- |
| [Initial load, Nov 6](2026-11-06-initial-sales-load.md) | Pinned provenance, hashes, schema and source amounts | Hashes remain the input contract; initial workbook hash is historical |
| [Model relationships, Nov 6](2026-11-06-model-relationships.md) | Initial relationships, group reconciliation and local folder move | Initial diagnostic measures were followed by explicit shipped measures |
| [Audit remediation, Nov 7](2026-11-07-audit-remediation.md) | Query-based key checks, invalid-subcategory fixture and bounded metadata scan | Scope/acceptance decisions now live in the maintained decision record |
| [AWBI-11 sales/units](2026-11-07-awbi-11-prototype.md) | Shipped measures and mixed-status fixture | Original publication questions were later decided; original fixture remains historical |
| [AWBI-13 orders/AOV](2026-11-07-awbi-13-orders-aov.md) | Distinct line-order count and denominator semantics | Current catalog defines delivered metrics; pending review text is historical |
| [AWBI-14 sales view](2026-11-07-awbi-14-sales-view.md) | Initial chart/filter checks and historical failed routes | Fixed category chart/hidden errors corrected in workbook improvements; view later hidden |
| [AWBI-15 RFM base](2026-11-07-awbi-15-customer-rfm.md) | Fixed window and initial customer results | Product-context last date corrected in AWBI-20 |
| [AWBI-16 scores](2026-11-07-awbi-16-rfm-segments.md) | Fixed bands, ties and segment priority | Global bands retained as descriptive; cohort interpretation added in business review |
| [AWBI-17 scenario](2026-11-07-awbi-17-sales-scenario.md) | Fixed-volume, representative/invalid inputs and source isolation | Visible control guidance corrected in current audit closure |
| [AWBI-18 monthly sales](2026-11-07-awbi-18-monthly-sales.md) | Original 38-month trend and filter fixture | Fixed range/window replaced with dynamic source-span formulas in improvements |
| [AWBI-19 customer overview](2026-11-07-awbi-19-customer-overview.md) | Initial counts/chart and later layout-guard fixtures | Limits/warning logic changed in improvements; view later hidden |
| [AWBI-20 category RFM](2026-11-07-awbi-20-category-rfm.md) | Corrected category last-order propagation and bounded checks | Improvements tested all four categories; dashboards tested all 30 category/segment selections |
| [Currency/returns review](2026-11-07-currency-returns-review.md) | Historical warnings and a corrected old Validation reference | Current currency decision is accepted/closed; current controls are at different cells |
| [Phase 3 review](2026-11-07-phase-3-review.md) | Evidence/dependency review before acceptance | Jira subsequently accepted the tasks; guards/dynamic ranges gained later checks |
| [Sheet review](2026-11-07-workbook-sheet-review.md) | Historical inventory, redundancy and defects identified then | Workbook improvements correct its listed warning/range/control issues |
| [Workbook improvements](2026-11-07-workbook-improvements.md) | Dynamic ranges, consolidated controls and bounded regression | Dashboard additions renamed the helper; later model detail moved to A38 |
| [Dashboards, Nov 8](2026-11-08-dashboards.md) | Dashboard build, refresh, 30 customer combinations and combined sales test | Later navigation hides legacy views; captures/notes superseded by current follow-up |
| [Owner review follow-up](2026-11-08-workbook-review-follow-up.md) | Reported human review, A38 model detail and blank-item hiding | Current audit adds note corrections and new preview captures |

Keep original measurements and failures intact. A later successful route does not prove that an earlier failed API now works. Historical source fixtures and ignored local diagnostics are not required to rerun the current public checker; they remain evidence of the specific past tests, not a claim that every fixture is distributed.
