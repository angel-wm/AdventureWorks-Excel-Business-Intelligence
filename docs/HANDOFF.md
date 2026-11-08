# Workbook handoff

The designated artifact is the `AdventureWorks-BI.xlsx` whose SHA-256 is recorded in [handoff.json](handoff.json), under artifact ID **AWBI-2026-11-08-audit-closure**. The manifest, workbook and [closure evidence](validation/2026-11-08-audit-closure.md) must travel together.

The owner published this workbook in [commit 431284a](https://github.com/angel-wm/AdventureWorks-Excel-Business-Intelligence/tree/431284ac4cfd255a8082a36b88cff1951f0d61a8). Use that immutable tree and verify the manifest hash. Later verifier and documentation maintenance does not change the designated workbook. No GitHub Release or tag is required or claimed.

## Inspect the workbook

1. Open the workbook in Excel 365 Desktop; loaded sample data is included.
2. Start with `DashboardSales`. Choose a product category, territory or order-date selection, then clear it to restore the full view.
3. On `DashboardCustomers`, category changes the qualifying purchases; the segment dropdown narrows the resulting customers. The RFM window stays fixed.
4. On `SalesScenario`, change price and additional discount. The baseline follows `DashboardSales`; reset assumptions to zero afterwards.
5. Read the [business review](BUSINESS_REVIEW.md) for the separate source-derived entry-method and customer-cohort comparisons. These static report tables do not follow workbook filters.

Interpret monetary figures under the [accepted currency limitation](DECISIONS.md#currency). The global RFM labels do not imply equivalent customer value across persons and stores.

## Reproduce the checks

Requirements: Python **3.12 or later**, using only the standard library, plus the seven unaltered files obtained using [Data Setup](DATA_SETUP.md). No Python packages, network access, SQL Server or Excel automation are needed to inspect the saved package.

Run the synthetic verifier regression suite from the repository root. It needs Python only, with no raw files or workbook:

```powershell
python -m unittest discover -s tests -v
```

Then run the source/workbook reconciliation with the seven pinned files available:

```powershell
python scripts/verify.py --output data/validation/latest.json
```

Exit **0** means the implemented checks passed; **1** means a failed check or pinned-source mismatch. Missing files or incompatible output structure fail visibly as Python errors rather than being treated as a pass. Read the output JSON for detailed results. The script does not refresh, recalculate, edit or save Excel; it compares cached values in the saved workbook with a fresh decimal source aggregation. Save the workbook in its restored unfiltered/default state before verifying.

Checks include pinned hashes/schema, source keys/joins, pricing identities, 40 territory/category groups, dashboard indicators and scenario defaults. The complete saved RFM and monthly populations must match the source's 19,119 customers and 38 months, including headers and values; extra, duplicate, missing, invalid or noncontiguous output rows fail, including populated rows after gaps. Empty formatted cells are ignored.

Saved cell/reference errors, external workbook links, a changed 20-sheet inventory or visibility, a chart count other than 10, a PivotTable count other than 5, broken local links/anchors, and missing or mismatched handoff identity also fail. Formula-element count and repeated long paragraphs remain diagnostics rather than acceptance gates. These package counts describe this designated artifact, not every valid Excel workbook.

Expected values are recomputed from source; retained JSON is evidence, not an input used to make a run pass. [Verifier hardening](validation/2026-11-08-verifier-hardening.md) records executable positive/negative cases and the current result. See [Validation Plan](VALIDATION_PLAN.md) for coverage limits.

Inspect the designated workbook directly. Close the saved workbook first if Excel holds a file lock that prevents `Get-FileHash` from opening it:

```powershell
Get-FileHash AdventureWorks-BI.xlsx -Algorithm SHA256
git rev-parse HEAD
git status --short
```

The Git commands establish the checkout and uncommitted differences, not remote publication. If the workbook is intentionally changed, validate it again and update the manifest, retained result and closure evidence together. A new save can alter the package hash even when displayed totals remain unchanged; do not silently replace the hash to bypass a failed handoff check.

## Current control layout

`Validation!D4` is the overall result; the 18 checks occupy rows 8–25. Its model-detail PivotTable is at `A38:Z51`, headed at `A36`. `KeyChecks` holds 25 key/join results in columns A:B and the current-source summary in D:E. `SourceConfig!A2` derives the source folder from the saved workbook location.

The three hidden legacy views and dual worksheet/model source loads retain active dependencies. They are part of the designated artifact; no cleanup deletion is required for this handoff.
