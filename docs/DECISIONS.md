# Scope decisions and accepted limitations

This is the maintained record of analytical boundaries. Historical tests remain in the [evidence index](validation/README.md); live work status belongs to Jira.

## Currency

**Decision accepted by the owner on 2026-11-08:** retain original source amounts, with currency unconfirmed and no conversion. This investigation is closed for the agreed scope; new authoritative evidence can reopen the interpretation.

The pinned Microsoft OLTP [schema and column descriptions](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script/instawdb.sql#L6399) describe prices, line subtotals and the exchange-rate reference, but do not explicitly identify the stored sales currency or the meaning of a missing `CurrencyRateID`. The [rate descriptions](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script/instawdb.sql#L6051) identify conversion direction and rate fields; that alone does not establish whether sales need conversion. The official [README](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/README.md) does not resolve this question.

SQL Server's [`money` type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/money-and-smallmoney-transact-sql) stores a numeric amount without currency information. Microsoft's [DAX sample model](https://learn.microsoft.com/en-us/dax/dax-sample-model) explicitly uses USD, but is a modified AdventureWorks DW model, not proof for this OLTP source.

The earlier bounded source investigation recorded 13,976 of 31,465 order headers with `CurrencyRateID` and 17,489 without it. Their referenced IDs matched 2,514 distinct records in the pinned [CurrencyRate.csv](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script/CurrencyRate.csv), with USD as source and AUD, CAD, FRF, GBP, DEM or EUR as destinations. These retained observations do not prove which currency is stored in line amounts; the current seven-file verification runner does not load or recheck CurrencyRate.csv.

Therefore neither confirmed USD nor mixed sales currencies has been established. Reconciliation establishes faithful arithmetic over source amounts, not monetary comparability. The qualification applies to sales, AOV, RFM monetary scores/segments and scenario amounts. Currency-dependent recommendations remain illustrative. Do not infer a conversion, assign a currency from territory alone, or equate a missing rate ID with USD.

## Order entry method

The original order-type question is answered by the source-derived [business review](BUSINESS_REVIEW.md#order-entry-method), using `OnlineOrderFlag`: **0 means placed by a salesperson; 1 means placed online by a customer**, according to the [official column description](https://github.com/microsoft/sql-server-samples/blob/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script/instawdb.sql#L6420).

These labels describe entry method; they are not automatically customer type, reseller classification or a causal sales-channel attribution. The delivered comparison is a reproducible pinned-source report, not a new interactive dashboard slicer. This fills the question without duplicating the existing dashboard or altering its filter contracts. Its amounts retain the currency qualification.

## Customer populations and RFM

Classify at `CustomerID`: a populated `StoreID` takes precedence; otherwise a populated `PersonID` identifies a person-only customer; otherwise classify as unknown. Store customers may also have a contact person, so counting both IDs would duplicate customers. The [business review](BUSINESS_REVIEW.md#customer-populations) compares cohorts under the same shipped-order window.

The workbook retains its fixed global RFM bands for reproducible sample description. They do not establish equivalent value or suitable common marketing treatment across store and person-only customers. Cohort differences and unresolved currency make a pooled campaign or customer-value recommendation unjustified. Use the separate cohort readout to frame questions; a future cohort-specific scoring model would require its own objectives and validation.

## Metric scope

| Item | Delivered scope / reason |
| --- | --- |
| Sales, units, orders, AOV | Implemented in the workbook; eligible shipped lines, with documented denominators |
| Purchasing customers and RFM | Implemented for the fixed observation window and exposed category/segment contexts |
| Repeat-customer rate | Delivered by cohort in the reproducible business review; not a new workbook measure |
| Comparable-period volume growth | Report compares complete calendar years 2023 and 2024 for units and orders; no monetary growth claim |
| Monthly monetary growth | Not implemented: partial selections and unresolved monetary comparability make a generic growth card misleading |
| Sales-share KPI | Not implemented as a separate measure; existing category/territory comparisons meet the MVP breakdown requirement; comparable monetary shares remain qualified |
| Weighted discount | Not implemented: no discount-effectiveness decision or demand-response evidence was agreed; the scenario answers a narrower arithmetic question |
| Historical gross profit / margin | Conditional requirement satisfied by explicit exclusion: no validated historical-cost method |
| Returns / refunds | No separate source or matching method included; sales are shipped line amounts before return/refund adjustments |

The [KPI catalog](KPI_CATALOG.md) specifies calculation meaning. The project does not promise every optional metric originally considered.

## Accepted verification boundary

Phase 4 [AWBI-5](https://angel231995.atlassian.net/browse/AWBI-5) records owner acceptance of the currency disclosure, the declined second-computer refresh test and bounded changed-source/schema and filter-combination coverage. Existing evidence establishes the tested original-source workflow and a local folder move. It does not establish arbitrary changed-source refresh ordering, every refresh path, cloud paths or every product/date/territory RFM context.

The owner reported completing a human workbook review. Technical source reconciliations and most automated checks were run by the project assistant; they are independent computations, not an independent human technical review. No new mandatory tests are inferred from this follow-up.

## Delivery and publication

The owner authorized publication and the repository was made public on 2026-11-08. The 14-point audit artifact was subsequently published in commit `431284ac4cfd255a8082a36b88cff1951f0d61a8`. [Current State](CURRENT_STATE.md) distinguishes that published artifact from later maintenance. The owner performs Git commits. [Handoff](HANDOFF.md) identifies the exact workbook by SHA-256 and immutable commit.

The identified local username/path metadata was accepted by the owner; the bounded historical scan is described in the [audit follow-up](validation/2026-11-07-audit-remediation.md). This does not certify every byte or past Git object as safe.
