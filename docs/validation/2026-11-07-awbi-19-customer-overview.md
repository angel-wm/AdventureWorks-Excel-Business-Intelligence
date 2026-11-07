# Customer segment overview — local validation

**Date:** 2026-11-07. **Status:** implemented and checked locally; [AWBI-19](https://angel231995.atlassian.net/browse/AWBI-19) remains in progress pending versioning and review. The customer RFM base and segments in AWBI-15 and AWBI-16 are in review.

## Scope

`CustomerOverview` presents the number of observed customers, counts for the five mutually exclusive RFM segments and a bar chart. It uses the customer rows and segment labels in `CustomerRFM`, with the fixed sample window and cutoff documented in [RFM scoring validation](2026-11-07-awbi-16-rfm-segments.md). Segment labels describe the sample; they are not a prediction of future behavior, and the sample is not lifetime history. Product-filtered RFM is not validated.

The product-filter limitation above describes this checkpoint. A later category correction and checks of overview counts are documented in [AWBI-20](2026-11-07-awbi-20-category-rfm.md).

The formulas count the current `CustomerRFM` PivotTable rows, not an independent model population. They check the expected segment column header, an upper bound at row 20000 and the presence of numeric customer IDs. If these checks fail, the displayed count is unavailable. A separate reconciliation checks that the five known segment counts sum to the customer count. Review both the source PivotTable and its refresh state if the view is unavailable or shows a check message. These guards cannot detect every stale or semantically incorrect source result; the fixed row bound and column layout must be reassessed if the workbook changes.

## Checks

An independent Python aggregation of original source orders and lines, applying the AWBI-16 bands and segment priority, matched the Excel totals: **19,119 customers**, including 964 Champions, 695 Frequent, 6,359 Recent, 2,273 Less recent repeat and 8,828 Other. The bar chart source and five plotted values were read back and visually inspected.

Temporarily replacing the summary label `Other` with `Unrecognized` caused the reconciliation to show `CHECK SEGMENTS`; restoring the label returned `OK`. This tests an omitted known label, not all possible source corruption. The source-header and row-limit failure guards were read back as formulas but not exercised. Existing scenario and first monthly values were read after the change. No full source refresh was performed. The workbook was saved; `data/AWBI-19-before.xlsx` is an untracked local pre-change copy that includes the saved AWBI-17 and AWBI-18 work.

Checks were performed by the project assistant, not an independent reviewer. Version and review the final workbook and evidence before Done.

## Subsequent guard checks

On 2026-11-07, the project assistant tested the delivered formulas in a disposable copy of workbook commit `5bf42e1504a24841eb78ef1e59c59721a8bbf83f`. With the unfiltered customer view, `CustomerOverview!B5` initially returned 19,119. Entering a numeric value in `CustomerRFM!A20000` made that result `#N/A`; clearing it removed the row-boundary condition. Changing the PivotTable's `CustomerRFM!I5` header from `RFM Segment` to `Changed header` also made the result `#N/A`. Restoring the header returned 19,119. Excel read back each result. The copy was closed without saving and the main workbook was not edited for these checks.

These tests exercise the stated numeric boundary and expected-header guards, not every possible source-layout change. The checks and acceptance review were performed by the project assistant, not an independent human reviewer.
