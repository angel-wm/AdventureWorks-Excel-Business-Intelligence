# Jira Workflow — AdventureWorks Excel BI

**Workflow:** Jira is authoritative for current work status. The original four-phase closure and later follow-up are summarized in [Current State](CURRENT_STATE.md); this document defines the process.

Jira tracks **work status and review**. GitHub contains the versioned source, workbook artifacts and technical documentation. Keep task descriptions focused; do not duplicate the canonical metric or source definitions in Jira.

## Kanban board

- **Project:** [AdventureWorks - Excel Business Intelligence (AWBI)](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2), team-managed software project.
- **Board:** [AWBI board](https://angel231995.atlassian.net/jira/software/projects/AWBI/boards/2), Kanban. No sprint ceremony required.
- **Columns:** **To Do → In Progress → In Review → Done**, all confirmed in the board configuration.
- **Work types:** Epic, Task and Bug; use Subtasks only for separable work.
- **Work-in-progress:** Prefer one primary active workbook task at a time to prevent conflicting agent edits. Flag blocked tasks with a reason rather than inventing a new status.

## Four existing Epics

| Issue | Phase | Example deliverables |
| --- | --- | --- |
| [AWBI-2](https://angel231995.atlassian.net/browse/AWBI-2) | Data Design & Preparation | Confirm source package, select tables/keys, define KPIs, verify Excel MCP tools |
| [AWBI-3](https://angel231995.atlassian.net/browse/AWBI-3) | Data Ingestion & Modeling | Build Power Query staging, facts/dimensions and relationships; validate refresh |
| [AWBI-4](https://angel231995.atlassian.net/browse/AWBI-4) | AI-Assisted Analytics & Dashboards | Implement KPIs, customer RFM, dashboards, scenarios and interaction checks |
| [AWBI-5](https://angel231995.atlassian.net/browse/AWBI-5) | Validation, Documentation & Publication | Run regression/UAT, review documentation, prepare validated portfolio assets |

These Epics have descriptions and acceptance criteria. Read live status and child tasks from Jira. The phases and exit requirements are defined in the [Roadmap](ROADMAP.md).

## What belongs in a Jira task

- **Title:** A specific business or technical outcome, not a vague activity.
- **Description:** Scope, purpose and target workbook/query/report.
- **Acceptance criteria:** Observable result plus source reconciliation, readback or functional test.
- **Dependencies / risks:** Only meaningful prerequisites.
- **Evidence:** Link to the GitHub commit/PR, workbook revision or test record.
- **AI involvement:** Optionally name the AI tool and specify what was independently verified.

Illustrative task (not created): **Create a monthly sales summary from validated line sales.** Completion requires matching totals to eligible source sales lines and a chart that filters correctly by territory.

## How issues move

1. **To Do:** Scope and acceptance criteria are recorded.
2. **In Progress:** Implementation is happening; serialize direct edits to a shared workbook.
3. **In Review:** Examine the real artifact and independently reconcile the output; link evidence.
4. **Done:** The deliverable works, acceptance checks pass or an explicit exception is accepted, and its version/evidence is traceable.

A blocked task remains visible with its blocker and next action. An AI tool success response alone does not satisfy Done.

## Jira, Codex and GitHub

```text
Jira task (scope and acceptance)
    ↓
ChatGPT / Codex + verified Excel tools (execution)
    ↓
Excel/source readback and independent checks
    ↓
GitHub artifact and evidence linked to issue
    ↓
Jira review and Done
```

Codex has read, created, edited and transitioned Jira issues, and linked GitHub evidence manually. Automatic GitHub–Jira linking remains unverified. Jira remains authoritative for live task status; [Current State](CURRENT_STATE.md) is a dated high-level record.

## Continuing the workflow

1. Keep new tasks small, with clear checks and traceable evidence.
2. Verify Excel operations by readback and independently reconcile relevant results.
3. Evidence links are maintained manually; automatic GitHub linking is optional and not relied upon.

## Definition of Done

Mark a task Done only when the artifact exists and its relevant [Validation Plan](VALIDATION_PLAN.md) checks pass, or an explicit exception is accepted, with evidence retained. Close an Epic only once all required phase deliverables pass its [Roadmap](ROADMAP.md) exit gate.
