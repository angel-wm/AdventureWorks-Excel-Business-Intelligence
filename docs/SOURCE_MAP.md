# Source Map — Candidate OLTP Inputs

**Status:** PROVISIONAL. This is a candidate selection based on Microsoft AdventureWorks OLTP naming; do not treat as validated column mapping or dataset profiling.

Official source: [Microsoft SQL Server samples — AdventureWorks OLTP](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works/oltp-install-script).

## Priority source candidates

| Source table/file | Planned role | Proposed join or grain | Verification needed |
| --- | --- | --- | --- |
| `SalesOrderDetail` | Core transactional sales fact | Line, `SalesOrderID` / `SalesOrderDetailID` | Keys, `LineTotal`, prices, discounts, quantity |
| `SalesOrderHeader` | Order date, territory, customer and channel | One row per order, `SalesOrderID` | Date choice, canceled/order status, `OnlineOrderFlag`, header totals |
| `Product` | Product attributes/cost candidate | `ProductID` | Current cost versus sale-time cost |
| `ProductSubcategory` | Product hierarchy | `ProductSubcategoryID` | Missing / null hierarchy |
| `ProductCategory` | Product hierarchy | `ProductCategoryID` | Category completeness |
| `Customer` | Customer dimension bridge | `CustomerID` | `PersonID` / `StoreID` and duplicate effects |
| `Person` | Individual customer attributes | `BusinessEntityID` where applicable | Scope, available non-sensitive fields |
| `Store` | Store customer attributes | `BusinessEntityID` where applicable | Distinct store/customer relationship |
| `SalesTerritory` | Commercial geography | `TerritoryID` | Territory nulls and source of truth |
| `ProductCostHistory` | Historical cost candidate | Product + effective dates | Applicability to shipped sales, interval overlap |
| `ProductListPriceHistory` | Pricing history candidate | Product + effective dates | Price-history rules and missing intervals |
| `SpecialOffer` | Promotion metadata (optional) | `SpecialOfferID` | Discount interpretation and join cardinality |
| `SalesOrderHeaderSalesReason` / `SalesReason` | Sales reasons (optional) | Many-to-many bridge | Cannot join directly to a line fact without duplication |

## Deferred unless justified

`WorkOrder`, `WorkOrderRouting`, `BillOfMaterials`, `ProductInventory`, `PurchaseOrderHeader`, `PurchaseOrderDetail`, `Vendor`, `TransactionHistory`, HR, credit-card and other unrelated sources.

They are part of OLTP's wider scope, not approved analytics inputs by default.

## Ingestion choices to investigate

1. **Official install-script CSV files (preferred candidate):** easier standalone Excel refresh, but installation files may rely on positional columns and SQL script definitions. Inspect delimiter, quote handling, type mapping, `NULL` representations, encoding and schema order before import.
2. **Restored SQL Server database:** native typed schema and keys but requires service/SQL Server setup. Use only if CSV consistency proves insufficient or analytical requirements justify it.

Do not infer column names from positional CSV content without checking Microsoft's installation script.

## Required Phase 1 profiling

- Exact source release/version, per-file SHA-256 and provenance.
- Row count per included source, key uniqueness, nulls, minimum and maximum dates.
- Detected encoding/delimiter and stable column order.
- Foreign-key coverage and many-to-one join validation.
- Monetary type/precision and date/time locale.
- Explicit status and order inclusion/exclusion rules.
- Row-count preservation after joins and records with unavailable dimension keys.

**No source profiling has been performed in this repository.** Update this file with verified findings and actual row counts only after implementation is authorized.
