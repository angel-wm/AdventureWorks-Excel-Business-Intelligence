# AdventureWorks — Excel Business Intelligence

> **Status: PLANNING** · Repository: private · Implementation: **not started**

An AI-assisted Microsoft Excel 365 Business Intelligence portfolio project using the **official Microsoft AdventureWorks OLTP** sample data. The goal is to transform transactional data into a reproducible commercial analytics model and interactive decision-support workbook.

## What the project will analyze

- Sales performance, growth, products, territories, and online/offline sales context.
- Customer behavior, recurrence, and segmentation.
- Product profitability, subject to validated historical-cost semantics.
- Commercial scenarios for pricing, discounting, and sales targets.
- Optional manufacturing analysis only when it materially enriches the commercial story.

This is **not** a reimplementation of ProcureFlow's procurement, inventory, or VBA automation system.

## Planned stack

- Excel 365 Desktop: tables, formulas, charts, PivotTables, and dashboards.
- Power Query for repeatable ingestion and preparation.
- Power Pivot / Excel Data Model for appropriate dimensional relationships.
- ChatGPT for Excel and Codex with the user's Excel MCP integration for AI-assisted workbook construction.
- Git/GitHub for version control and traceability.

Capabilities of the installed Excel MCP must be checked before relying on automation. AI output is not accepted without validation.

## Documentation and RDR

This repository uses a lean **Research–Design–Review (RDR)** approach to document consequential architecture choices *before* implementation. The RDRs are drafts until reviewed and explicitly accepted. Their findings distinguish **Verified**, **Documented**, and **Assumed** evidence.

| Start here | Purpose |
| --- | --- |
| [Project Brief](docs/PROJECT_BRIEF.md) | Scope, audience, requirements, exclusions, and success criteria |
| [Roadmap](docs/ROADMAP.md) | Four phases, milestones, estimates, and gates |
| [Architecture](docs/ARCHITECTURE.md) | Proposed data and workbook layers |
| [Source Map](docs/SOURCE_MAP.md) | Candidate OLTP tables, keys, grains, and data questions |
| [KPI Catalog](docs/KPI_CATALOG.md) | Proposed business definitions and semantic cautions |
| [AI Workflow](docs/AI_WORKFLOW.md) | Codex/MCP/ChatGPT execution and verification policy |
| [Validation Plan](docs/VALIDATION_PLAN.md) | Technical and business acceptance checks |
| [Current State](docs/CURRENT_STATE.md) | Facts about what exists and what remains open |
| [RDR Index](docs/rdr/README.md) | Pre-implementation research/design/review records |

## Planned execution

1. **Data Design & Preparation** — choose tables, establish metric definitions and keys.
2. **Data Ingestion & Modeling** — build and verify Power Query and the model.
3. **AI-Assisted Analytics & Dashboards** — implement analytical measures, visuals, and scenarios.
4. **Validation, Documentation & Publication** — reconcile, test, and package portfolio evidence.

**Planning estimate:** 8–12 working days and roughly 24–48 hours of effort; this is not a commitment and will be reassessed after an MCP capability test and source validation.

## Source data policy

Official Microsoft source: [AdventureWorks OLTP install-script directory](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works/oltp-install-script). [Microsoft's sample guidance](https://learn.microsoft.com/sql/samples/adventureworks-install-configure) explains the OLTP, DW, and LT variants.

Raw datasets are external artifacts: preserve source files unchanged, track provenance and any redistribution terms, and do not commit unnecessary bulk source data.

## Current boundary

Documentation exists to support future implementation. **No raw data has been downloaded for this project, no workbook or transformation has been built, and no KPI has been computed or validated.** Those activities require separate explicit authorization.

**License:** to be selected before public release. Do not assume Microsoft's sample data is automatically covered by a future repository license.
