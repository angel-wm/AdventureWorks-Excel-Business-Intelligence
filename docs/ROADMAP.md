# Roadmap — Four Phases

**Status:** PLANNING · Durations are estimates, not actuals.

| Phase | Estimated effort | Exit gate |
| --- | --- | --- |
| 1 — Data Design & Preparation | 1–2 working days | Selected scope, source schemas, grains, semantics and MVP approved |
| 2 — Data Ingestion & Modeling | 2–3 working days | Power Query refresh, facts/dimensions and model relationships verified |
| 3 — AI-Assisted Analytics & Dashboards | 3–4 working days | Required KPIs, customer segmentation, visualizations and scenarios reconciled |
| 4 — Validation, Documentation & Publication | 1–3 working days | Regression, documentation and portfolio readiness verified |

**Overall planning range:** 8–12 working days / ~24–48 hands-on hours. Ranges are not additive day-by-day guarantees; overlap and rework may change totals. Estimate will be recalibrated after Phase 1.

## Phase 1 — Data Design & Preparation

- Inspect official source metadata, file structure, delimiters, encoding and field mappings.
- Confirm one fact grain for sales; distinguish header and line-level amounts.
- Select minimum tables for Date, Product, Customer, Territory and Channel.
- Define target metric semantics, scope boundaries and source-to-target mapping.
- Discover installed Excel MCP tools in Codex with a non-destructive capability check.
- **Gate:** write down what is verified vs assumed; no unverified model relationship enters implementation.

## Phase 2 — Data Ingestion & Modeling

- Obtain approved source files without modifying originals.
- Build parameterized, reproducible Power Query source/staging/final layers.
- Normalize data types, keys and date handling; prevent join-based row multiplication.
- Build the Excel Data Model / Power Pivot relationships where practical.
- Reconcile fact counts and representative totals to source facts.
- **Gate:** refresh, data-quality checks and model-grain tests pass.

## Phase 3 — AI-Assisted Analytics & Dashboards

- Create formulas/measures using a division of work based on actual Excel MCP capabilities.
- Build commercial views: trend, product, customer and territory.
- Implement justified RFM/recurrence definitions and segmentation.
- Add scenario assumptions with controls and baseline isolation.
- Create/edit charts, PivotTables or compatible substitutes and visual layouts.
- **Gate:** formulas, pivots, visuals and outputs agree with verified source-level totals.

## Phase 4 — Validation, Documentation & Publication

- Run regression, refresh and usability tests; capture reproducible evidence.
- Review time windows, missing values, filter effects, performance and profit disclaimers.
- Update RDR outcomes, current-state evidence and public README.
- Decide source-data redistribution policy/license and capture portfolio screenshots.
- **Gate:** acceptance criteria met; publication requires explicit authorization.

## Workflow discipline

- Complete and verify meaningful components before progressing.
- Use RDR drafts for design exploration; accept only after review.
- Codex/Excel MCP and ChatGPT for Excel are execution tools, not trusted calculation authorities.
- Keep docs concise; do not produce large phase-closeout files unless a concrete issue demands them.
- No source data, workbook or code implementation will be created by documentation planning alone.
