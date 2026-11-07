# Roadmap — Four-Phase Delivery

**Current work:** Phases 1 and 2 are complete. Phase 3 analytics are next; public-portfolio preparation has started alongside them. Live status belongs to Jira.

The target is a **short, AI-accelerated** BI project. The 8–12 working-day estimate (about 24–48 hours of effort) is provisional, not a promise. The ranges below are directional and may overlap or require rework.

| Phase | Planning range | Outcome and exit check |
| --- | --- | --- |
| 1. Data Design & Preparation | 1–2 days | Dataset version, source tables, grains, KPIs and workbook outline reviewed |
| 2. Data Ingestion & Modeling | 2–3 days | Power Query pipeline and model refresh/reconcile correctly |
| 3. AI-Assisted Analytics & Dashboards | 3–4 days | Sales, customer, product and scenario outputs tested |
| 4. Validation, Documentation & Publication | 1–3 days | Regression, usability, traceability and release checks complete |

## Phase 1 — Data Design & Preparation

Inspect the official AdventureWorks OLTP snapshot and only the tables required by the commercial questions. Define key relationships, a sales-line grain, status/date semantics and the priority KPIs. Check the installed **Excel MCP tool inventory from Codex** before assigning direct Excel tasks.

**Exit:** confirmed source selection, validated mapping assumptions and approved scope. Jira Epic 1.

## Phase 2 — Data Ingestion & Modeling

Create a reproducible Power Query pipeline after authorization, with source → staging → analytical outputs. Build relationships in the Excel Data Model / Power Pivot where appropriate. Check keys, row counts, date handling and additive sales measures.

**Exit:** refresh and reconciliation tests pass. Jira Epic 2.

## Phase 3 — AI-Assisted Analytics & Dashboards

Use Codex/Terra, Excel MCP and ChatGPT for Excel to construct formulas, summaries, charts, customer RFM, commercial views and scenario worksheets, delegating only capabilities actually supported by those tools. Use Excel Desktop where native functions are unsupported.

**Exit:** key outputs independently validated against transformed/source data. Jira Epic 3.

## Phase 4 — Validation, Documentation & Publication

Test repeatable refresh, formulas, model filters, scenarios and workbook usability. Record limitations, results, source attribution, screenshots and versioned release artifacts. Publication itself needs explicit approval.

**Exit:** the [Validation Plan](VALIDATION_PLAN.md) is fulfilled or documented exceptions accepted. Jira Epic 4.

## Working approach

Jira holds epics and short tasks; no separate heavyweight phase-closeout dossier is required. Use an issue only for work with a clear deliverable and test. Keep GitHub commits and PRs linked to Jira keys where practical. See [Jira Workflow](JIRA_WORKFLOW.md).

After each meaningful step, summarize **built → verified → pending**. Reassess scope and timeline after the Phase 1 data and MCP checks rather than treating estimates as validated.
