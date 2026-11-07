# AdventureWorks — Excel Business Intelligence

**Status: In development.** The repository includes an initial workbook, Power Query loads and a data model. Dashboards and production KPIs are not yet complete. See [Current State](docs/CURRENT_STATE.md) for verified progress and limitations.

AdventureWorks — Excel Business Intelligence is a portfolio project that will turn **Microsoft AdventureWorks OLTP transactional data** into a practical **commercial decision-support solution in Excel 365 Desktop**. It will explore sales, customers, products, territories, profitability where cost data allow, and business scenarios.

The distinction from ProcureFlow is intentional: **commercial intelligence and dimensional modeling**, not procurement, replenishment, or VBA-heavy operations.

For project context and task-specific reading guidance, see [REPO_CONTEXT.md](REPO_CONTEXT.md).

## Planned outcome

An interactive Excel BI workbook with reproducible ingestion, auditable business measures, useful dashboards and scenario analysis. The project will use AI to **create and modify workbook components**, not merely explain how to build them.

| Technology | Planned role |
| --- | --- |
| Excel 365 Desktop, Power Query, Power Pivot | Data preparation, analytical model and interactive workbook |
| Codex with Terra (Medium / High / Extra High) | Development, analysis, review and tool coordination |
| User's Excel MCP for Codex | Direct Excel actions **after its actual capabilities are verified** |
| ChatGPT for Excel | Supported formula, sheet, formatting and chart work |
| Jira | Lightweight planning and task tracking |
| GitHub | Versioned artifacts, documentation and implementation evidence |

## Project plan

Four phases are planned: **data design**, **ingestion and modeling**, **AI-assisted analytics and dashboards**, and **validation and publication**. The initial estimate is **8–12 working days (approximately 24–48 hours of effort)**; it will be revised after the data and tool checks. See the [Roadmap](docs/ROADMAP.md).

The exact scope is deliberately smaller than the full OLTP database. No historical performance claims or profit figures are published before validating their underlying data.

## Where to go next

| Need | Read |
| --- | --- |
| Goals, requirements and exclusions | [Project Brief](docs/PROJECT_BRIEF.md) |
| Phases, estimates and milestones | [Roadmap](docs/ROADMAP.md) |
| Data flow, model and workbook design | [Architecture](docs/ARCHITECTURE.md) |
| Candidate AdventureWorks OLTP source tables | [Source Map](docs/SOURCE_MAP.md) |
| Proposed metric definitions | [KPI Catalog](docs/KPI_CATALOG.md) |
| Division of work between AI tools and Excel | [AI Workflow](docs/AI_WORKFLOW.md) |
| Jira board, epics, tasks and GitHub links | [Jira Workflow](docs/JIRA_WORKFLOW.md) |
| Test plan and acceptance checks | [Validation Plan](docs/VALIDATION_PLAN.md) |
| What's actually complete and what's pending | [Current State](docs/CURRENT_STATE.md) |

## Data and documentation sources

- [Microsoft's AdventureWorks sample documentation](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure) and [selected OLTP source revision](https://github.com/microsoft/sql-server-samples/tree/8fe3fd0c9a825fef3ae6d601e97537b612d7b214/samples/databases/adventure-works/oltp-install-script). The workbook contains sample data; the original source files are excluded from Git. See [source provenance](docs/validation/2026-11-06-initial-sales-load.md) and [third-party notices](THIRD_PARTY_NOTICES.md).
- Documentation presentation follows the owner's [Repository Documentation Readability Guide (RDR)](https://github.com/angel-wm/repository-documentation-readability/blob/main/GUIDE.md), not the unrelated Research–Design–Review methodology. A repository-local copy of the owner's [Codex documentation skill](.agents/skills/repository-documentation-readability/SKILL.md) supports repeat use.

## Implementation boundary

The repository is private during development. A public portfolio release requires separate approval. Original data files and local backups are excluded from Git.

## License

Project-authored material is licensed under the [MIT License](LICENSE). Microsoft's AdventureWorks sample has its own copyright and license notice, reproduced in [Third-party notices](THIRD_PARTY_NOTICES.md).
