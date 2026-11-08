# Project Brief

**Status:** The agreed workbook scope was delivered and the original four phases accepted. This brief defines requirements; the [evidence index](validation/README.md), [scope decisions](DECISIONS.md) and [handoff](HANDOFF.md) establish the delivered scope and qualifications.

## Purpose

Build an Excel 365 Desktop BI solution using **Microsoft AdventureWorks OLTP**. The portfolio should demonstrate how raw operational transactions become a reliable analytical model and decisions. The main subjects are sales, customer behavior, products, territories, and commercial scenarios.

Codex and Excel MCP produced spreadsheet artifacts, with native Excel fallbacks and source-based checks. The ChatGPT add-in for Excel was exercised for the later audit corrections and readback; the [AI workflow](AI_WORKFLOW.md) distinguishes actual operations from optional capabilities. This is deliberately shorter and less tutorial-oriented than ProcureFlow.

## Business questions

- **Sales:** Where do orders, sold units and discounted sales change by month, product category, territory and order entry method? The dashboards cover the first three; the [business review](BUSINESS_REVIEW.md#order-entry-method) covers entry method.
- **Customers:** Which observed customers purchased most recently or repeatedly, and how do their original source amounts differ? Can reproducible descriptive RFM segments explain these patterns alongside separate person/store comparisons? Monetary comparability is unconfirmed; pooled RFM scores do not establish equivalent economic value across customer types.
- **Products:** Which categories sell most? Is a historically defensible margin available?
- **Commercial planning:** How do explicit price or discount assumptions affect a scenario, without rewriting historical facts?

## MVP requirements

| ID | Required capability | Acceptance condition |
| --- | --- | --- |
| FR-01 | Repeatable OLTP source ingestion | Same unaltered source produces stable results |
| FR-02 | Fact/dimension model | Source grains, joins and keys reconcile |
| FR-03 | Sales dashboard | Trend and breakdowns reconcile to eligible sales lines |
| FR-04 | Customer dashboard | Customer counts and RFM logic verified against orders |
| FR-05 | Product / territory analysis | Filters preserve totals and expose missing dimensions |
| FR-06 | Profitability (conditional) | Historical cost approach passes checks, otherwise label as unavailable |
| FR-07 | Scenario worksheet | Adjustable assumptions never change historical results |
| FR-08 | AI build evidence | Readback and independent validation of edits |
| FR-09 | Portfolio documentation | README, source attribution, tests and release evidence up to date |

The [audit closure](validation/2026-11-08-audit-closure.md) maps these requirements to evidence. Conditional margin exclusion satisfies FR-06. Report-only comparisons, optional metrics and accepted test limits are explicit in [Scope decisions](DECISIONS.md).

## Out of scope

Full ERP, procurement/replenishment management, standalone forecasting, manufacturing execution, heavy VBA orchestration, and importing every OLTP table by default. Manufacturing analysis is optional and must answer a distinct useful question.

## Constraints and decisions

- **Dataset variant:** AdventureWorks OLTP, pinned to the [selected source revision](SOURCE_MAP.md).
- **Ingestion:** Selected official install files and Power Query; SQL Server remains a fallback if needed.
- **Model:** Excel Data Model with seven source tables and six active relationships; no arbitrary advanced-feature support is implied.
- **Project duration:** four phases, approximately 8–12 working days / 24–48 working hours (planning estimate).
- **Tracking:** Jira for work status; GitHub for source/version history, per [Jira Workflow](JIRA_WORKFLOW.md).
- **Documentation:** owner’s [RDR presentation guide](https://github.com/angel-wm/repository-documentation-readability/blob/main/GUIDE.md), keeping explanations concise without removing technical conditions.
- **Safety of results:** never invent figures, silently modify source data, or call an untested AI result validated.

See the [Source Map](SOURCE_MAP.md) for candidate tables and the [Validation Plan](VALIDATION_PLAN.md) for acceptance evidence.
