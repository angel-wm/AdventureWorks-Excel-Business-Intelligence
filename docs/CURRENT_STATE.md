# Current State

**Last reviewed:** 2026-11-03

## What exists

- The private GitHub repository `angel-wm/AdventureWorks-Excel-Business-Intelligence`.
- Planning documentation covering the OLTP scope, four phases, candidate model, KPIs, AI execution, Jira and validation.
- Documentation presentation based on the owner's [Repository Documentation Readability Guide](https://github.com/angel-wm/repository-documentation-readability/blob/main/GUIDE.md), with the repository-local Codex skill.

## What is agreed

- Use **Microsoft AdventureWorks OLTP**, not AdventureWorksDW or LT.
- Build **commercial analytics** in Excel 365 Desktop: sales, customers, products, territory and scenarios, with profitability conditional on cost validity.
- Use Power Query ingestion, Power Pivot/Data Model where appropriate, ChatGPT for Excel, Codex/Terra and the user's Excel MCP.
- Keep **four phases**, with a provisional **8–12 working-day / 24–48-hour** effort estimate.
- Use **Jira** to track epics and implementation tasks, and GitHub for versioned artifacts.
- Give brief, practical explanations to the user in Spanish. Write repository documents in English.
- Remain in **PLANNING** until explicitly authorized to begin implementation.

## Not yet done

- No selected source snapshot has been profiled or downloaded into this project.
- No workbook, Power Query pipeline, Data Model, formulas, charts or dashboards have been implemented.
- No source totals, business KPIs, profit calculations or acceptance tests have passed.
- The exact Excel MCP server capabilities are **not yet verified**.
- Jira project, board, task IDs, GitHub integration and Atlassian account access have **not been set up or checked**.
- No public release or license has been approved.

## Next planning checks

1. Confirm the exact AdventureWorks OLTP data package and reproducible mapping.
2. Inspect the user's Excel MCP tools in Codex.
3. Review the proposed Jira workflow and establish the actual Jira project after authorization.
4. Approve Phase 1 scope, then separately authorize implementation.

The authoritative deliverable descriptions are in the [Project Brief](PROJECT_BRIEF.md), the [Roadmap](ROADMAP.md) and the [Validation Plan](VALIDATION_PLAN.md). This page records **observed project status**, not a second copy of the technical design.
