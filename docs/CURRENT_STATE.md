# Current State

**Last reviewed:** 2026-11-06. This is a dated project snapshot, not a live Jira or local-workbook feed.

## What exists

- The private GitHub repository `angel-wm/AdventureWorks-Excel-Business-Intelligence`, including planning documentation, root [repository context map](../REPO_CONTEXT.md), and [Codex guidance](../AGENTS.md).
- Documentation covering the AdventureWorks OLTP scope, four phases, candidate data model, KPIs, AI workflow, Jira and validation.
- Documentation presentation guided by the owner's [Repository Documentation Readability Guide](https://github.com/angel-wm/repository-documentation-readability/blob/main/GUIDE.md) and repository-local Codex skill.
- A verified [Jira AWBI Kanban board](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2) with **To Do → In Progress → In Review → Done** and four Epics ([AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2), [AWBI-3](https://angel231995.atlassian.net/browse/AWBI-3), [AWBI-4](https://angel231995.atlassian.net/browse/AWBI-4), [AWBI-5](https://angel231995.atlassian.net/browse/AWBI-5)), all in **To Do** at this review. No implementation tasks were found in that snapshot.
- ChatGPT's Atlassian integration has been used to inspect and update those Jira Epics. The user reports `excel-mcp` as enabled in Codex Desktop; functional Excel operations remain untested.

## Agreed decisions

- Use **Microsoft AdventureWorks OLTP**, not AdventureWorksDW or LT.
- Build **commercial analytics** in Excel 365 Desktop: sales, customers, products, territories and scenarios; profitability depends on historical-cost validity.
- Prefer Power Query, with Power Pivot / Excel Data Model where appropriate; use ChatGPT for Excel and Codex/Terra plus Excel MCP only for verified operations.
- Organize delivery into **four phases**, with a provisional **8–12 working-day / 24–48-hour** effort estimate.
- Jira owns live work status; GitHub owns versioned artifacts; [REPO_CONTEXT.md](../REPO_CONTEXT.md) maps relevant context sources.
- Explain progress briefly in Spanish and maintain repository documentation in English.
- Remain in **PLANNING** until explicitly authorized to begin implementation.

## Not yet done

- No selected AdventureWorks OLTP source snapshot has been profiled or downloaded into this project.
- No BI workbook, Power Query pipeline, Excel Data Model, formulas, charts or dashboards have been implemented.
- No source totals, KPIs, profit calculations or workbook acceptance tests have passed.
- The connected Excel MCP's identity, tool inventory, live permissions and save/readback behavior have **not** been verified from Codex.
- Codex-to-Jira task automation and GitHub/Jira issue linking have **not** been verified.
- No public release or licensing decision has been approved.

## Next planning checks

1. Confirm the exact official AdventureWorks OLTP source package and its reproducible schema mapping.
2. From Codex, inspect the installed Excel MCP tool inventory; test on a disposable workbook only after authorizing a technical test.
3. Prepare a small first Jira task within [AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2), confirm Phase 1 scope and separately authorize implementation.

For planned deliverables see [Project Brief](PROJECT_BRIEF.md), [Roadmap](ROADMAP.md) and [Validation Plan](VALIDATION_PLAN.md). For live issue status, query Jira rather than treating this dated document as a live source.
