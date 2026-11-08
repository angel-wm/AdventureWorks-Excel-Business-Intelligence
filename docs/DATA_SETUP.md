# Prepare the AdventureWorks source files

The workbook contains the current sample data, so it can be inspected without the original files. To refresh it, use Excel 365 Desktop and place the seven source files alongside the workbook using the structure below. Excel may request source or privacy confirmation during refresh.

## Download the selected source

1. Save `AdventureWorks-BI.xlsx` in a local project folder. Create `data/raw/adventureworks-oltp-8fe3fd0c` beneath that folder.
2. Open the [official Microsoft files at the selected revision](https://github.com/microsoft/sql-server-samples/tree/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script).
3. Download the raw contents of these files into that folder, keeping their names unchanged:
   - `SalesOrderHeader.csv` and `SalesOrderDetail.csv`
   - `Product.csv`, `ProductSubcategory.csv` and `ProductCategory.csv`
   - `Customer.csv` and `SalesTerritory.csv`
4. Compare each file's SHA-256 hash with the [recorded source hashes](validation/2026-11-06-initial-sales-load.md#baseline). In PowerShell, run the following from the project folder:

   ```powershell
   Get-FileHash data/raw/adventureworks-oltp-8fe3fd0c/*.csv -Algorithm SHA256
   ```

5. Open and save the workbook in Excel. Check that the `SourceConfig` sheet points to the source folder, then use **Data → Refresh All**. Review refresh errors, the overall status and individual results in `Validation`, and the key/join results and source summary in `KeyChecks`. Use the [current control layout](HANDOFF.md#current-control-layout); older validation records retain their historical sheet positions.

```text
project folder/
├── AdventureWorks-BI.xlsx
└── data/raw/adventureworks-oltp-8fe3fd0c/
    ├── Customer.csv
    ├── Product.csv
    ├── ProductCategory.csv
    ├── ProductSubcategory.csv
    ├── SalesOrderDetail.csv
    ├── SalesOrderHeader.csv
    └── SalesTerritory.csv
```

The files are tab-delimited and have no header row; the workbook's queries assign column names. The selected files and workbook contain fictional Microsoft sample data. Raw files are excluded from Git, but the workbook includes loaded data. Retain the [Microsoft attribution and license](../THIRD_PARTY_NOTICES.md) when redistributing the workbook.

Refresh has been tested after a local folder move on one computer. Other computers, cloud paths, missing files and refresh ordering under changed source data remain unverified. The main sales rule is shipped orders only. `Validation` compares both all-status and shipped totals; a historical mixed-status fixture was checked, but this does not establish every changed-source case. See the [workbook improvements record](validation/2026-11-07-workbook-improvements.md).

## Check the saved artifact

After saving a refreshed, unfiltered workbook, run the [reproducible checks](HANDOFF.md#reproduce-the-checks). They inspect saved outputs and pinned files; they do not initiate refresh or certify new source versions. Accepted portability and changed-source limits are recorded in [Scope decisions](DECISIONS.md#accepted-verification-boundary).
