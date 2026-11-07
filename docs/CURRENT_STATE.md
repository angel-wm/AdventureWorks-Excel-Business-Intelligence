# Current State

**Last reviewed:** 2026-11-06. This is a local snapshot, not a live Jira or remote-publication feed.

## What exists

- The private repository contains the project plan, source map, KPI definitions and validation guidance. Local changes are not evidence of remote publication.
- Seven files from the selected Microsoft AdventureWorks OLTP revision have been downloaded and profiled locally. Their provenance, hashes and checks are in [initial sales load validation](validation/2026-11-06-initial-sales-load.md).
- A local `AdventureWorks-BI.xlsx` workbook contains seven Power Query worksheet and Data Model loads and six active relationships. Source counts and category/territory PivotTable checks are recorded in [sales model validation](validation/2026-11-06-model-relationships.md). Production measures and dashboards are not yet built.
- Excel MCP and Jira have been used from Codex. Excel operations have been checked by readback and GitHub evidence linked manually in Jira; automatic linking and some advanced model operations remain unverified.
- Jira is authoritative for live work status. Phase 1 ([AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2)) and phase 2 ([AWBI-3](https://angel231995.atlassian.net/browse/AWBI-3)) are Done. Phase 2 evidence and the tested workbook are versioned in commit `7baf498280cb67531bbf2c6b9dabbc7b0a288bcc`. Consult the [AWBI board](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2) for current status.

## Decisions and boundaries

- Use the selected OLTP install files and Power Query for commercial analytics. The initial sales grain is one order line, and the main sales view includes shipped orders (`Status = 5`).
- Prioritize sales, units, distinct orders and average order value. Historical margin remains conditional on a defensible historical-cost method.
- A workbook and early ingestion were explicitly authorized. Publishing remains subject to separate approval. Raw files stay local and ignored by Git.
- A two-decimal source-to-workbook comparison passed, while sub-cent differences remain recorded and require a monetary precision decision.

## Next steps

1. Implement and validate the shipped-order production measures, including a mixed-status test, in [AWBI-11](https://angel231995.atlassian.net/browse/AWBI-11).
2. Test handoff on a different computer before relying on the workbook-relative source configuration.

The project uses MIT for project-authored material and retains Microsoft's third-party notice. No public release has been approved. See the [Roadmap](ROADMAP.md) for phase gates and the [Jira Workflow](JIRA_WORKFLOW.md) for review and Done.
