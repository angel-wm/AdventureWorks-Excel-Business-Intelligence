# AdventureWorks OLTP — Source Map

**Status:** Provisional source selection; no dataset has been downloaded or profiled in this project.

The [official Microsoft OLTP installation directory](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works/oltp-install-script) contains table-named files and `instawdb.sql`. The installation CSVs may use positional fields and SQL-script-defined schemas. **Verify column names, types, delimiters and null handling from the selected version**, not file names alone.

## Priority source candidates

| OLTP source | Intended analytical role | Critical check |
| --- | --- | --- |
| `SalesOrderDetail` | One sales-order line per fact record | Key uniqueness, quantities, prices and `LineTotal` semantics |
| `SalesOrderHeader` | Order, customer, date, territory, status, order type | Order/line cardinality; avoid adding header totals per line |
| `Product` | Product key and descriptive attributes | Stable `ProductID`, current vs historic costs |
| `ProductSubcategory`, `ProductCategory` | Product category drill-down | Preserve product cardinality and handle missing hierarchy |
| `Customer` | Sales customer reference | Person vs store linkage and null values |
| `Person`, `Store` | Optional customer attributes | Appropriate use and one-to-one/many-to-one joins |
| `SalesTerritory` | Territory grouping | Missing values and order-level territory semantics |
| `ProductCostHistory` | Conditional gross-margin calculation | Effective-date intervals and cost applicability |
| `ProductListPriceHistory` | Optional price history | Dates, gaps and discounts |
| `SpecialOffer` | Optional promotion analysis | Discount grain and join cardinality |
| `SalesOrderHeaderSalesReason`, `SalesReason` | Optional reason analysis | Many-to-many bridge; prevent inflated sales totals |

## Deferred unless justified

Manufacturing (`WorkOrder`, `WorkOrderRouting`, `BillOfMaterials`), stock (`ProductInventory`), purchasing (`PurchaseOrderHeader`, `PurchaseOrderDetail`, `Vendor`), transaction history, and employee/HR tables. OLTP gives us room to explore, but **MVP scope is commercial analytics**, not full ERP recreation.

## Ingestion decisions still open

| Option | Why consider it | Limitation |
| --- | --- | --- |
| **Official install CSVs + Power Query** (preferred candidate) | Portable source, no SQL Server installation required | Positional mappings, explicit types and relationship checks |
| SQL Server backup/database + Power Query | Native schema and server constraints | Requires database setup and a reproducible connection |

## Phase 1 source verification

Record source version and URL, hashes where applicable, file counts and schema layout; then check key uniqueness, observed date span, row counts, missing foreign keys and join cardinalities. Keep the source files unchanged.

**No source row counts, monetary totals or join results have been validated yet.** See [Architecture](ARCHITECTURE.md) and [Validation Plan](VALIDATION_PLAN.md).
