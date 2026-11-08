# Saved-output verifier hardening and publication reconciliation

**Date:** 2026-11-08. **Tracking:** [AWBI-22](https://angel231995.atlassian.net/browse/AWBI-22). The owner authorized the five re-audit follow-ups in order **3 → 4 → 5 → 1 → 2**: complete output enumeration, executable failure tests, qualified customer wording, publication-state correction and Jira evidence/acceptance reconciliation.

## Artifact and scope

The owner-published audit snapshot is [commit 431284a](https://github.com/angel-wm/AdventureWorks-Excel-Business-Intelligence/commit/431284ac4cfd255a8082a36b88cff1951f0d61a8). Local HEAD and public GitHub `main` matched that commit before this maintenance. The workbook is unchanged: SHA-256 `ec7aba23a1954af5a8e99a093ef65b8e4cf99e7373f898f3108dc4b2cb352662`, 33,281,291 bytes. Its original source calculations and business-review results are unchanged.

Only Python verification, tests and documentation changed. No workbook cells, formulas, queries, model definitions, charts or saved bytes were edited. No Excel refresh, source download, new dataset, Git commit or push was performed for this maintenance. The prior currency decision and accepted validation boundaries remain in force.

## Changes and executed checks

| Follow-up | Implemented result | Executed evidence |
| --- | --- | --- |
| 3 — Full output populations | Enumerate every populated A:I output row in CustomerRFM and A:B output row in SalesMonthly, including data after gaps; verify headers, complete source membership, uniqueness, contiguity and values | Current saved package passes: 19,119 unique customers and 38 unique months, no missing/extra/duplicate/invalid rows, no header or value mismatch |
| 4 — Regression and mandatory gates | Shared production checks exercised with synthetic failures; package errors/links, sheet names/visibility, chart/PivotTable counts and required manifest identity gate PASS | 29 tests pass; the changed-source CLI fixture exits 1 with FAIL before opening a workbook; fresh full verifier exits 0 with PASS |
| 5 — Customer question | Brief asks about observed recency, repetition and source amounts; explicitly qualifies unconfirmed monetary comparability and person/store economic equivalence | Brief agrees with the existing RFM and currency interpretation; no new economic-value claim or analytical model |
| 1 — Publication state | Maintained documents identify the audit artifact as published in `431284a`, distinguish the earlier baseline and preserve original result JSON | Actual public `main` and local HEAD checked; designated workbook hash matches the published handoff |
| 2 — Jira closure evidence | Original AWBI-21 evidence links use immutable `431284a` paths; original audit acceptance is separate from this later maintenance | AWBI-21 transitioned to Done after version-linked review; AWBI-22 transitioned to In Review for this maintenance |

Run the commands in [Handoff](../HANDOFF.md#reproduce-the-checks). The [retained version-2 result](results/2026-11-08-verifier-hardening.json) records fresh source reconciliation, complete output-population diagnostics, package inventory, documentation checks and workbook identity. The [original result](results/2026-11-08-checks.json) remains unchanged as evidence for the earlier verifier. Version 2 nests RFM/month diagnostics under `saved_output_comparison.customers` and `.monthly` and reports `verifier_version: 2`.

The [29 tests](../../tests/test_workbook_checks.py) cover valid populations and deliberate extra, duplicate, missing, gapped and orphan rows; wrong headers and each customer value column; invalid IDs/dates, nonfinite/nonnumeric amounts and monetary tolerance; missing/extra/duplicate sheets, visibility, chart/PivotTable counts, saved errors, external links and missing/wrong manifest identity. The CLI fixture generates its own seven temporary files and changes one hash without changing row width. It does not use or modify real raw data. The suite needs Python only; the full reconciliation additionally needs the pinned files and workbook.

Formula-element counts and repeated long paragraphs remain diagnostics; they are not silently presented as tested acceptance gates. Package counts are the contract for this designated workbook and need deliberate revision if the artifact's structure changes.

## Performance and verification limits

The checker runs outside Excel and reads saved XML. Full population enumeration examines the populated saved cells already loaded by the parser; it does not scan Excel's empty grid. Completed XML rows are released during parsing. There are no added workbook calculations, refresh operations or runtime checks, so this change adds no workbook recalculation or interaction cost. No comparative Python runtime benchmark is claimed.

Source-derived totals and the complete saved outputs reconcile, including 40 territory/category groups and current cards/scenario defaults. This does not establish currency comparability, causality, every interactive-filter context, new refresh behavior or DAX-definition identity. Synthetic tests validate verifier behavior, not Excel runtime behavior. The same project assistant implemented and ran these checks; no independent human technical review is implied.

## Publication and tracking

The published workbook remains identified by `431284a` and its manifest hash. At this execution checkpoint, the maintenance was checked locally and had not been committed or pushed. Its containing Git commit identifies the maintenance once the owner commits it; a successful local check alone does not establish remote publication.

[AWBI-21](https://angel231995.atlassian.net/browse/AWBI-21) received the original audit's immutable evidence and transitioned to Done after the assistant's version-linked review. AWBI-22 records this later maintenance and was moved to In Review, with the owner's publication and immutable evidence linkage as the remaining closure step. Live Jira remains authoritative for subsequent status changes; the four original phase closures and accepted limitations are unchanged.
