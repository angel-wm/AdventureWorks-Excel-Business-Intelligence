# AdventureWorks OLTP — Source Map

**Status:** Seven files selected and profiled; six workbook relationships and the documented sales and customer dashboard contexts have been checked. Arbitrary changed sources and broader filter contexts remain unverified; see [dashboard validation](validation/2026-11-08-dashboards.md).

The [official Microsoft OLTP installation directory](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works/oltp-install-script) contains table-named files and `instawdb.sql`. The installation CSVs may use positional fields and SQL-script-defined schemas. **Verify column names, types, delimiters and null handling from the selected version**, not file names alone.

The selected snapshot is [revision `8fe3fd0c9a825fef3ae6d601e97537b612d7b214`](https://github.com/microsoft/sql-server-samples/tree/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script). The seven selected files use tab-separated positional columns without headers. File hashes, field counts and local checks are recorded in [initial sales load validation](validation/2026-11-06-initial-sales-load.md). The chosen route is these install files with Power Query; SQL Server is a fallback, not a dependency.

## Initial source relationships

| Source → lookup | Fields | Intended cardinality |
| --- | --- | --- |
| `SalesOrderDetail` → `SalesOrderHeader` | `SalesOrderID` | Many lines to one order |
| `SalesOrderDetail` → `Product` | `ProductID` | Many lines to one product |
| `SalesOrderHeader` → `Customer` | `CustomerID` | Many orders to one customer |
| `SalesOrderHeader` → `SalesTerritory` | `TerritoryID` | Many orders to one territory |
| `Product` → `ProductSubcategory` | `ProductSubcategoryID` | Many products to an optional subcategory |
| `ProductSubcategory` → `ProductCategory` | `ProductCategoryID` | Many subcategories to one category |

Source checks found no unmatched non-empty references for these links. The 209 products without a subcategory require an unknown member if they later appear in sales. These are source observations, not evidence that workbook model relationships exist.

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

## Ingestion options

| Option | Why consider it | Limitation |
| --- | --- | --- |
| **Official install files + Power Query** (selected) | No SQL Server installation required | Positional mappings, explicit types and relationship checks; workbook-relative paths have been tested locally, not on another computer |
| SQL Server backup/database + Power Query | Native schema and server constraints | Requires database setup and a reproducible connection |

## Phase 1 source verification

Record source version and URL, hashes where applicable, file counts and schema layout; then check key uniqueness, observed date span, row counts, missing foreign keys and join cardinalities. Keep the source files unchanged.

See [Architecture](ARCHITECTURE.md), [local validation](validation/2026-11-06-initial-sales-load.md) and [Validation Plan](VALIDATION_PLAN.md) for completed checks and remaining work.
