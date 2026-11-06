# Current State

**Last reviewed:** 2026-11-06. This is a local snapshot, not a live Jira or remote-publication feed.

## What exists

- The private repository contains the project plan, source map, KPI definitions and validation guidance. Local changes are not evidence of remote publication.
- Seven files from the selected Microsoft AdventureWorks OLTP revision have been downloaded and profiled locally. Their provenance, hashes and checks are in [initial sales load validation](validation/2026-11-06-initial-sales-load.md).
- A local `AdventureWorks-BI.xlsx` workbook contains seven Power Query worksheet loads. Refresh and readback succeeded; the Data Model, business measures and dashboards are not yet built.
- Excel MCP and Jira have been used from Codex. Excel operations have been checked by readback; advanced model capabilities and GitHub–Jira linking remain unverified.
- Jira is authoritative for live work status. The phase 1 and 2 Epics and their initial tasks have been started; consult the [AWBI board](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2) for current status.

## Decisions and boundaries

- Use the selected OLTP install files and Power Query for commercial analytics. The initial sales grain is one order line, and the main sales view includes shipped orders (`Status = 5`).
- Prioritize sales, units, distinct orders and average order value. Historical margin remains conditional on a defensible historical-cost method.
- A workbook and early ingestion were explicitly authorized. Publishing remains subject to separate approval. Raw files stay local and ignored by Git.
- A two-decimal source-to-workbook comparison passed, while sub-cent differences remain recorded and require a monetary precision decision.

## Next steps

1. Review and version the phase 1 source, scope and evidence before closing its Epic.
2. Verify workbook-level keys and relationships, then build and reconcile the analytical model in phase 2.
3. Replace machine-specific source paths with a reproducible approach before handoff.

No public release or licensing decision has been approved. See the [Roadmap](ROADMAP.md) for phase gates and the [Jira Workflow](JIRA_WORKFLOW.md) for review and Done.
