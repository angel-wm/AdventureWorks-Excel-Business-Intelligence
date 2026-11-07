# Initial sales load — local validation

**Date:** 2026-11-06. **Status:** historical local evidence, versioned in Git. This record is not itself a public release or independent review.

## Baseline

- Microsoft OLTP install files at [revision 8fe3fd0c9a825fef3ae6d601e97537b612d7b214](https://github.com/microsoft/sql-server-samples/tree/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script).
- Validated workbook snapshot: `AdventureWorks-BI.xlsx`; SHA-256 after save and close: `df81ed3b47a7a5b51ad822f999658520b4a38d39a69de71ba8cbc0e6643daf87`. Later presentation changes mean this hash does not identify the current workbook.
- The raw files are local and ignored by Git. This snapshot used an absolute path; a later workbook-relative approach is described in [model validation](2026-11-06-model-relationships.md).

| Source file | SHA-256 |
| --- | --- |
| Customer.csv | `4704aa5b46aed326599014524c821aca50e938587e6a1133c0f6d9aae5c5efc6` |
| Product.csv | `df0379a7cba8b11b97ea5d104cf1313ef9f683137b6426f2fac6bb8c74c2a2ea` |
| ProductCategory.csv | `d86dde135e023960633ed1d6a2fb72f56b74aa2f7d07af983b6bff5e33dfceb2` |
| ProductSubcategory.csv | `a90dce80f310044b99a920790cbf60b83982079af421a5935fda7bc7ab69bc75` |
| SalesOrderDetail.csv | `220129977aa63e34fa4a1d66c2604bd2184373151efb09c98b343371ba77ab8a` |
| SalesOrderHeader.csv | `cf637c7d58006ebbc13daf0b8ed6cf7f738165d298ae0b5479a59237429c1882` |
| SalesTerritory.csv | `cb087c101765605e848635f6127123b1a0814397635ce5faebe52f516ccfc861` |

## Checks performed

- The seven files are tab-delimited without headers. Every row has the expected number of fields from the official schema: Customer 7, Product 25, ProductCategory 4, ProductSubcategory 5, SalesOrderDetail 11, SalesOrderHeader 26 and SalesTerritory 10.
- The candidate primary keys have no empty or duplicate values. Detail-to-header, detail-to-product, header-to-customer, header-to-territory and subcategory-to-category references have no missing or unmatched keys. Of 504 products, 209 have no subcategory; none occurs in the sales detail.
- All 31,465 order headers have status 5. Observed order dates run from 2022-05-30 through 2025-06-29. The agreed main sales scope includes shipped orders; payment and accounting recognition are not established.
- Excel MCP loaded and refreshed 31,465 headers and 121,317 detail rows. Both queries reported success. After saving, closing and reopening, the validation sheet and both query definitions were read back.
- Independent decimal sums from the source are 109846381.4039 for header subtotals and 109846381.399888 for line totals. Excel readback matches each at two decimal places. This is the comparison precision for this check, not a claim of exact decimal equality.
- All 121,317 source line totals equal `UnitPrice * (1 - UnitPriceDiscount) * OrderQty` under decimal arithmetic. Of 31,465 orders, 30,770 header subtotals exactly equal their summed detail; 695 differ by less than one cent, with a maximum absolute difference of 0.000050. The difference is observed, not root-caused. Excel floating-point summation introduces additional sub-cent differences.

## Remaining work

At this snapshot, relationships, business measures and dashboards had not been implemented. The evidence and a later workbook were versioned; portability beyond a local folder move and monetary precision require further review. See [subsequent model validation](2026-11-06-model-relationships.md).

## Subsequent local load

After the validated snapshot above, the same workbook was extended with Power Query worksheet loads for Product (504 rows), ProductSubcategory (37), ProductCategory (4), Customer (19,820) and SalesTerritory (10). Excel readback after refreshing all seven queries confirmed these counts and 209 products without a subcategory. The initial workbook hash above does not cover this later state. See [model validation](2026-11-06-model-relationships.md) for subsequent checks and outstanding work.
