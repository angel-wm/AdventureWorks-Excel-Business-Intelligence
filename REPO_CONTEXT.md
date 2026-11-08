# Repository context

## Project

- **Project:** AdventureWorks — Excel Business Intelligence, a commercial analytics portfolio built with Excel 365 Desktop and Microsoft AdventureWorks OLTP.
- **Convention version:** **0.1**. See the [AI Repository Context specification](https://github.com/angel-wm/ai-repository-context/blob/main/SPEC.md).
- **Description:** [README](README.md) and [Project Brief](docs/PROJECT_BRIEF.md).
- **Work Unit:** A Jira **Epic** represents one of the four delivery phases; related **Tasks/Bugs** track testable deliverables. This is existing project terminology, not a new lifecycle.
- **Work Model:** [Roadmap](docs/ROADMAP.md) for phases and exit conditions; [Jira Workflow](docs/JIRA_WORKFLOW.md) for work status, evidence and definition of done.

## Published state

- **Repository:** [angel-wm/AdventureWorks-Excel-Business-Intelligence](https://github.com/angel-wm/AdventureWorks-Excel-Business-Intelligence), normally read at the selected GitHub ref (default branch `main` when no ref is specified). It is intended for public portfolio use; verify actual visibility rather than inferring it from intent.
- **Publication / handoff sources:** [Handoff](docs/HANDOFF.md) and [manifest](docs/handoff.json) identify the designated workbook by hash and immutable published commit; [Current State](docs/CURRENT_STATE.md) distinguishes that artifact from later maintenance. A manifest alone is not proof of remote publication.
- **Visibility rule:** A remote reader reports only the retrieved repository/ref snapshot. Changes that exist only locally are **Unknown**. A local reader distinguishes uncommitted edits, commits and confirmed remote publication; a clean worktree or commit alone does not prove a release.

## Source map

| Topic / purpose | Source | Authority | Read when |
| --- | --- | --- | --- |
| Project goals and scope | [Project Brief](docs/PROJECT_BRIEF.md), [README](README.md) | Brief defines intended requirements; README is an entry-point summary | Understanding business goals, exclusions or outcomes |
| Work model and phase exit gates | [Roadmap](docs/ROADMAP.md), [Jira Workflow](docs/JIRA_WORKFLOW.md) | Phase plan and Jira process respectively | Planning, starting or completing a phase |
| State / Current Work | [Live Jira AWBI board](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2) and [Current State](docs/CURRENT_STATE.md) | Jira is authoritative for live issue status; Current State is a dated high-level snapshot | Identifying in-progress or in-review work; check both and disclose differences |
| Last Completed Work | [Jira AWBI issues](https://angel231995.atlassian.net/issues/?jql=project%20%3D%20AWBI) and their linked GitHub evidence; [Current State](docs/CURRENT_STATE.md) | A verified Done issue with acceptance evidence establishes recorded completion; issue numbers and edit times do not | Reviewing the most recently accepted deliverable or phase |
| Planned Work | [Roadmap](docs/ROADMAP.md) and [Jira AWBI issues](https://angel231995.atlassian.net/issues/?jql=project%20%3D%20AWBI) | Roadmap defines planned phase scope; Jira tracks queued tasks | Selecting next work; a plan is not execution authorization |
| Architecture and data sources | [Architecture](docs/ARCHITECTURE.md), [Source Map](docs/SOURCE_MAP.md) | Intended flow and selected mappings; validation records establish implemented behavior | Model, ingestion, keys, source-grain or workbook structure |
| Source setup | [Data Setup](docs/DATA_SETUP.md), [Source Map](docs/SOURCE_MAP.md) | Setup procedure and source selection; validation records establish tested behavior | Obtaining excluded raw files or refreshing the workbook |
| Business calculations | [KPI Catalog](docs/KPI_CATALOG.md), [Business Review](docs/BUSINESS_REVIEW.md) | Delivered definitions and separately identified source-derived findings; calculation status is explicit | Creating or reviewing measures, dashboards or commercial conclusions |
| Recorded decisions / rationale | [Scope Decisions](docs/DECISIONS.md), [Project Brief](docs/PROJECT_BRIEF.md#constraints-and-decisions) | Maintained analytical boundaries, accepted exceptions and optional-metric rationale | Investigating decisions, assumptions or scope |
| Validation / evidence | [Validation Plan](docs/VALIDATION_PLAN.md), [Evidence Index](docs/validation/README.md), selected Jira issue | Plan defines coverage; the index distinguishes historical checkpoints and current executable checks | Accepting work, auditing calculations or reviewing a release |
| AI tool boundaries | [AI Workflow](docs/AI_WORKFLOW.md) | Exercised Codex, Excel MCP, native Excel and add-in operations, with verification limits | Assigning automation or assessing actual capability |
| Documentation conventions | [Repository Documentation Readability skill](.agents/skills/repository-documentation-readability/SKILL.md) | Author's local RDR guidance for documentation presentation, not project business logic | Writing or substantially reviewing repository documentation |

**Missing information:** **None** means the native records explicitly show no such work; **Not documented** means no maintained source exists; **Unknown** means the available snapshot or permissions cannot establish the answer. If Jira cannot be reached, do not infer live issue status from this map or an older state document.

## Loading rules

1. Read applicable [repository guidance](AGENTS.md) and this map; then load **only** sources required by the task. Follow the project's approval rules before making implementation changes.
2. **State:** Read the dated [Current State](docs/CURRENT_STATE.md), then query live Jira for current issue status. Active work is work actually in progress or review; queued Epics are planned, not active. Report discrepancies or unavailable live data.
3. **Review:** Select the actual Jira issue and its acceptance criteria; open its linked evidence and only the affected architecture, KPIs or validations.
4. **Plan:** Read the roadmap and queued Jira issues, check dependencies and any required preceding-phase acceptance evidence. Planning is not permission to implement.
5. **Architecture or calculation:** Start with the relevant section of [Architecture](docs/ARCHITECTURE.md), [Source Map](docs/SOURCE_MAP.md) or [KPI Catalog](docs/KPI_CATALOG.md); expand to observed workbook/source evidence only when necessary.
6. **History or validation:** Search the targeted recorded decision or test; select its issue and artifact baseline. Do not mistake a draft check or an AI success response for a verified outcome.
7. Resolve relative paths from this file; a directory or link is not an instruction to read everything. Apply topic-specific authority, disclose conflicting or unavailable sources, and stop once the relevant evidence answers the task or establishes a specific gap.
8. Update this map when **source locations, authority or routing rules** change. Keep routine progress in Jira and [Current State](docs/CURRENT_STATE.md), not in this map.
