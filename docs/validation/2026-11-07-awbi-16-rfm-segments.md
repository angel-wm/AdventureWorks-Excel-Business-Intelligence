# Customer RFM scoring and segments — local validation

> **Historical checkpoint:** status, sheet positions and limitations below describe this record's original baseline. They are not live task status or current instructions. See the [evidence index](README.md) for later corrections and the current handoff.

**Date:** 2026-11-07. **Status:** implemented and checked locally; [AWBI-16](https://angel231995.atlassian.net/browse/AWBI-16) awaits versioning and review. It depends on the AWBI-15 RFM base and earlier shipped measures, which are in review.

## Scope and scoring

`CustomerRFM` shows three scores and one descriptive segment per qualifying customer. The window and cutoff are fixed by [AWBI-15](2026-11-07-awbi-15-customer-rfm.md): shipped orders from 2022-05-30 through 2025-06-29, as of 2025-06-29. `RFMGuide` records the rules in the workbook. The sample is not customer lifetime history; these segments are not a validated prediction of future behavior.

Scores run from 1 to 5, with higher scores representing more recent activity, more qualifying orders, or higher discounted line sales. Equal input values receive the same score; groups are not required to be equal-sized. Blank RFM inputs yield blank scores and segment.

| Score | Recency days | Orders | Customer sales rounded to two decimals |
| --- | --- | --- | --- |
| 1 | 289 or more | 1 | At most 39.98 |
| 2 | 205–288 | 2 | Above 39.98 through 98.96 |
| 3 | 130–204 | 3 | Above 98.96 through 1236.78 |
| 4 | 72–129 | 4 | Above 1236.78 through 3578.27 |
| 5 | 0–71 | 5 or more | Above 3578.27 |

Recency and monetary thresholds were chosen from the nearest-rank 20th, 40th, 60th and 80th percentiles of the pinned sample; monetary sales are rounded to two decimals for scoring. The model remains floating-point and does not round each source line. Frequency uses explicit counts because 11,649 of 19,119 customers have exactly one order; forcing equal quintiles would split ties. The thresholds are fixed, not recomputed on refresh; reassess them before applying to another population.

Segments use the first matching rule in this order:

1. **Champions:** R ≥ 4, F ≥ 3 and M ≥ 4.
2. **Frequent:** F ≥ 3 and R ≥ 3.
3. **Recent:** R ≥ 4.
4. **Less recent repeat:** R ≤ 2 and F ≥ 2.
5. **Other:** all remaining scored customers.

## Checks

Power Pivot's measure editor displayed the four score and segment formulas. Excel read back the customer PivotTable, including the values after a PivotTable refresh. A separate Python aggregation of the original source, using decimal sales and the stated bands and priorities, matched all **19,119** customer scores and segment labels. In the mixed-status fixture from AWBI-11, the independently calculated scores and labels also matched all 19,119 displayed customers.

For the original source, segment counts were: Champions 964; Frequent 695; Recent 6,359; Less recent repeat 2,273; Other 8,828. These are counts from this sample, not inferred customer outcomes. Boundary checks used observed customers at each recency, frequency and monetary cutoff and the next observed value; all returned the stated scores. For example, 71 and 72 days scored 5 and 4, and rounded sales of 39.98 and 39.99 scored 1 and 2.

A diagnostic DAX context selecting status 1 returned blanks for all three scores and the segment while a model control found 26 non-shipped units. This checks that context, not all interactive selections; the diagnostic formulas were not separately read back. Product-filtered RFM remains unvalidated, as described in AWBI-15. Visual inspection covered the workbook's rule guide. The workbook and test copy were saved; a local pre-change backup is `data/AWBI-16-before.xlsx`. The fixture and backup are untracked. No full source refresh was performed in this task.

The product-filter limitation above describes this checkpoint. See [AWBI-20](2026-11-07-awbi-20-category-rfm.md) for the later correction and its tested category scope.

The checks were performed by the project assistant, not an independent reviewer. Version and review the workbook and evidence before marking the task Done.
