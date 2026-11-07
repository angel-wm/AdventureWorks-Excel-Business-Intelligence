# Current State

**Last reviewed:** 2026-11-07. This is a dated snapshot, not a live Jira or remote-publication feed.

## What exists

- The repository contains the project plan, source map, KPI definitions and validation guidance. It is intended for public portfolio use; local changes do not prove remote publication.
- Seven files from the selected Microsoft AdventureWorks OLTP revision have been downloaded and profiled locally. Their provenance, hashes and checks are in [initial sales load validation](validation/2026-11-06-initial-sales-load.md).
- A local `AdventureWorks-BI.xlsx` workbook contains seven Power Query worksheet and Data Model loads and six active relationships. Source counts and category/territory PivotTable checks are recorded in [sales model validation](validation/2026-11-06-model-relationships.md). Shipped sales and units measures are implemented locally and checked in [AWBI-11 validation](validation/2026-11-07-awbi-11-prototype.md); dashboards are not yet built. Review remains pending; consult Git and Jira for the versioned and live status.
- Excel MCP and Jira have been used from Codex. Excel operations have been checked by readback and GitHub evidence linked manually in Jira; automatic linking and some advanced model operations remain unverified.
- Jira is authoritative for live work status. Phase 1 ([AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2)) and phase 2 ([AWBI-3](https://angel231995.atlassian.net/browse/AWBI-3)) are Done. Phase 2 evidence and the tested workbook are versioned in commit `7baf498280cb67531bbf2c6b9dabbc7b0a288bcc`. Consult the [AWBI board](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2) for current status.
- Audit remediation and public-portfolio preparation are in progress under [AWBI-12](https://angel231995.atlassian.net/browse/AWBI-12), alongside the planned phase 3 work. See the [audit follow-up](validation/2026-11-07-audit-remediation.md).

## Decisions and boundaries

- Use the selected OLTP install files and Power Query for commercial analytics. The initial sales grain is one order line, and the main sales view includes shipped orders (`Status = 5`).
- Prioritize sales, units, distinct orders and average order value. Historical margin remains conditional on a defensible historical-cost method.
- A workbook and early ingestion were explicitly authorized. Publishing remains subject to separate approval. Raw files stay local and ignored by Git.
- A two-decimal presentation and source reconciliation policy is documented in the KPI catalog; sub-cent floating-point differences remain and the model is not fixed-decimal accounting.

## Next steps

1. Review and version the shipped-order measures and mixed-status evidence in [AWBI-11](https://angel231995.atlassian.net/browse/AWBI-11); confirm currency and returns treatment before publication.
2. Test handoff on a different computer before relying on the workbook-relative source configuration.
3. Review workbook metadata and Git history for public visibility; current and earlier workbook versions contain local user-identifying information.

The project uses MIT for project-authored material and retains Microsoft's third-party notice. Public visibility may be considered during development; check current visibility and review workbook metadata and Git history before changing it. See the [Roadmap](ROADMAP.md) for phase gates and the [Jira Workflow](JIRA_WORKFLOW.md) for review and Done.
