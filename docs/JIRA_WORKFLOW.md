# Jira Workflow — AdventureWorks Excel BI

**Status:** Planned. The Jira project, board and issues have **not** been created or verified.

Jira will track **what we are doing and what has passed review**. GitHub will contain the actual versioned source, workbook and technical documentation. Avoid copying full specifications into Jira comments.

## Proposed board

Use **one Jira software project** for AdventureWorks, preferably a **Kanban board**. This is a short, incremental, AI-accelerated project, so fixed sprints and a heavyweight Scrum ceremony are unnecessary.

- **Project name:** AdventureWorks — Excel Business Intelligence (proposed; not created).
- **Project key:** choose an available short key in Jira, such as `AWBI` (illustrative only; no key has been reserved).
- **Issue types:** Epic, Task and Bug; add Subtasks only for genuinely separate deliverables.
- **Statuses:** use Jira's available workflow, ideally **To Do → In Progress → In Review → Done**. If `In Review` does not exist, record review in the issue and use the board's standard statuses. Use the board's blocking/flag mechanism instead of creating a custom `Blocked` status unless needed.
- **Work-in-progress:** one active primary task at a time where practical; limit parallel work to avoid workbook edit conflicts.

## Four epics

| Epic | Phase | Example tasks |
| --- | --- | --- |
| 1 — Data Design & Preparation | Phase 1 | Confirm source package; map chosen tables/keys; define metrics; test Excel MCP capabilities |
| 2 — Data Ingestion & Modeling | Phase 2 | Configure Power Query; build facts/dimensions; build relationships; validate refresh and joins |
| 3 — AI-Assisted Analytics & Dashboards | Phase 3 | Implement verified KPIs; customer RFM; sales/product visuals; scenarios; integration checks |
| 4 — Validation & Portfolio Release | Phase 4 | Regression and UAT; documentation review; release screenshots; publishing checks |

The epics reflect the [Roadmap](ROADMAP.md); dates, assignees and Jira issue keys will be added only after setup.

## What belongs in a Jira task

Keep the issue short but actionable:

- **Title:** business/technical outcome, not a vague activity.
- **Description:** what should change, why it matters and target workbook/query/report.
- **Acceptance criteria:** observable result, plus the source reconciliation or readback needed.
- **Dependencies / risks:** only meaningful prerequisites.
- **Evidence:** link to the GitHub commit/PR, workbook version, test record or screenshot.
- **AI involvement:** optional one-line note naming the tool and what was independently verified.

Illustrative issue:

> **Create a monthly sales summary from validated line sales.** Done when monthly totals reconcile to the chosen eligible detail rows and the chart filters correctly by the selected territory.

This is an example, **not an actual Jira issue or test result**.

## How issues move

1. **To Do:** clearly scoped; prerequisite and acceptance criteria recorded.
2. **In Progress:** assigned and being implemented; keep direct edits to the workbook serialized.
3. **In Review:** test the actual artifact, independently reconcile the result, and link evidence.
4. **Done:** the deliverable works, validation is recorded, documentation updated if relevant, and GitHub history is linked.

A blocked task stays visible with a reason, dependency and next action. A failed check stays open; an AI tool return alone does not satisfy Done.

## Jira, Codex and GitHub together

```text
Jira task (scope and acceptance)
    ↓
ChatGPT/Codex + Excel MCP / ChatGPT for Excel (supported execution)
    ↓
Excel/source readback and independent QA
    ↓
GitHub commit/PR with task key where available
    ↓
Jira review and Done
```

Use Jira for **work status**, GitHub for **versioned artifacts**, and [Current State](CURRENT_STATE.md) for the project's high-level factual status. Do not maintain competing versions of KPIs, source mappings or technical decisions in issue descriptions.

## Setup checklist — not yet executed

1. Confirm Jira workspace permissions, project name/key and board workflow.
2. Create one Kanban project and the four epics, after authorization.
3. Add only the next small set of phase tasks; avoid dozens of speculative tickets.
4. Verify whether GitHub/Jira linking is available and record the actual integration method.
5. Optionally connect the Atlassian integration to ChatGPT/Codex **if available and approved**; connection is not required to use Jira manually.
6. Start tracking implementation only after the separate authorization to implement.

## Definition of Done

An issue can be Done only when the stated artifact exists, the relevant [Validation Plan](VALIDATION_PLAN.md) checks pass (or an explicit exception is accepted), and GitHub/evidence links are available. Close the corresponding epic only when all required phase deliverables pass its roadmap exit gate.
