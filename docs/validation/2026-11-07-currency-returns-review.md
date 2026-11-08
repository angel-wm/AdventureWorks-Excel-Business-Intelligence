# Currency and returns — bounded workbook review

> **Historical checkpoint:** status, sheet positions and limitations below describe this record's original baseline. They are not live task status or current instructions. See the [evidence index](README.md) for later corrections and the current handoff.

**Scope:** A local disposable copy of `AdventureWorks-BI.xlsx`, SHA-256 `827a1332b20d46370f63e6a3be4130d4e12bfb4aea138411cb862f6d9955f344`, matching the saved main workbook at copy time. Excel MCP opened and read the copy; it was closed without saving. No refresh, workbook modification or exhaustive formatting audit was performed.

## Currency readback

Excel read back the titles and initial cells of `SalesOverview`, `SalesByDate`, `SalesMonthly`, `SalesScenario`, `CustomerRFM` and `RFMGuide`. The reviewed text did not state that currency is unconfirmed. Sampled monetary cells in these views used the number format `#,##0.00`, with no currency symbol. The checks cover sampled worksheet cells, not all cells, chart axes, tooltips or possible filter states.

The owner accepted the interim description in the [KPI catalog](../KPI_CATALOG.md#currency-boundary). At this initial checkpoint, the workbook did not communicate that description in the reviewed views. Currency semantics and aggregate comparability remain unverified.

## Subsequent workbook disclosure

The main workbook was backed up locally and edited with Excel MCP after the review above. Currency warnings were added to `SalesOverview!A4`, `SalesByDate!A3`, `SalesMonthly!A3`, `SalesScenario!A4`, `CustomerRFM!A3` and `RFMGuide!A17:B17`; Excel read back each warning and the workbook was saved. Visual inspection covered the overview, monthly, scenario and customer RFM views. The overview's total remained 109846381.3998877 sales and 274914 units; the scenario baseline remained 109846381.3998877 and the customer overview retained 19,119 customers. These are bounded readbacks, not a full refresh or comprehensive regression. The currency and cross-currency comparability remain unverified.

## Returns readback and policy

`SalesOverview` states that sales are discounted order-line amounts and exclude tax, freight and return adjustments. `SalesScenario` states that returns are not modeled. The documented [shipped-sales measure](2026-11-07-awbi-11-prototype.md) sums `LineTotal` under shipped status and does not make a separate return or refund adjustment.

The [returns boundary](../KPI_CATALOG.md#returns-boundary) defines the intended description and its consequences for AOV, RFM monetary values and scenarios. These facts do not establish whether returns occurred in the sample, or prove every view displays the limitation. The review was performed by the project assistant; it is not an independent human review.

## Validation sheet reference correction

During a subsequent worksheet inventory, `Validation!B19` returned `#REF!` because its `COUNTBLANK` formula contained a broken reference. After saving a local backup, the formula was replaced with `=COUNTBLANK(Product[ProductSubcategoryID])`. Excel read back the formula and result of 209 after saving, matching a separate count of blank subcategory fields in the 504 local `Product.csv` records. This checks the current loaded worksheet and source snapshot; no full refresh or changed-source test was performed.
