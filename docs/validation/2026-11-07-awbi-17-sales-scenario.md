# Fixed-volume sales scenario — local validation

> **Historical checkpoint:** status, sheet positions and limitations below describe this record's original baseline. They are not live task status or current instructions. See the [evidence index](README.md) for later corrections and the current handoff.

**Date:** 2026-11-07. **Status:** implemented and checked locally; [AWBI-17](https://angel231995.atlassian.net/browse/AWBI-17) remains in progress pending versioning and review. The baseline depends on the sales measures and view in AWBI-11 and AWBI-14, both in review.

## Scope

`SalesScenario` uses `GETPIVOTDATA` to read the shipped line-sales total from `SalesOverview`, including its territory, category and order-date selections. Two editable inputs represent a price change from −100% to +100% and an additional discount from 0% to 100%. Excel data validation is configured to reject out-of-range interactive entry; formulas independently guard both ranges because programmatic writes or pastes can bypass validation.

The calculation is `baseline × (1 + price change) × (1 − additional discount)`. The additional discount applies after the price change to already-discounted line sales. Volume is assumed fixed; this is arithmetic sensitivity, not evidence of demand response. It does not calculate margin, tax, freight or returns and does not modify historical facts. Currency and return handling remain subject to the KPI catalog's publication boundary.

## Checks

| Selection and inputs | Baseline | Scenario | Change |
| --- | ---: | ---: | ---: |
| All data, 0% and 0% | 109846381.3998877 | 109846381.3998877 | 0 |
| All data, +10% and 5% | 109846381.3998877 | 114789468.56288265 | +4.5% |
| Australia, Bikes, June 2022, +10% and 5% | 199477.93459999998 | 208454.441657 | +4.5% |

Excel read back the formulas, values and validation settings. An independent arithmetic check uses the multiplier `1.10 × 0.95 = 1.045`; the filtered baseline was previously reconciled to source in [AWBI-14](2026-11-07-awbi-14-sales-view.md). A programmatic input of +150% bypassed Excel's interactive validation, and the formula guard returned `#N/A` for the scenario and derived changes. The invalid value was restored; the stop-style interactive validation configuration was read back but its dialog was not manually exercised. A zero baseline yields an unavailable percentage; an empty-baseline filter was not tested.

Both inputs and all three overview filters were restored to their defaults. The final baseline and scenario matched, and change was zero. Excel read back six active model relationships and 25 zero key checks; this was not a full source refresh or proof that no other workbook state changed. The scenario sheet was visually inspected and the workbook saved. The pre-change rollback is `data/AWBI-17-before.xlsx`, which is untracked.

These checks were performed by the project assistant, not an independent reviewer. Version the workbook and evidence, then review the actual baseline before Done.
