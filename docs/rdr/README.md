# RDR Index — Research–Design–Review

Research–Design–Review (RDR) captures the **problem**, **evidence**, **alternatives**, **proposed design**, and **review outcome** *before implementation*. Keep records as short as the decision allows.

This is an intentionally lightweight Markdown implementation inspired by the [Nexus RDR guide](https://github.com/Hellblazer/nexus/blob/main/docs/rdr.md). The Nexus CLI/gate is **not installed or used here**. Metadata states in this repository are maintained manually and must not claim automatic lifecycle validation.

## Records

| ID | Topic | Type | Status | Gate |
| --- | --- | --- | --- | --- |
| [RDR-001](RDR-001-scope-and-oltp.md) | OLTP scope, dataset and portfolio direction | Architecture | DRAFT | NOT RUN |
| [RDR-002](RDR-002-ingestion-and-model.md) | Source ingestion and fact/dimension model | Architecture | DRAFT | NOT RUN |
| [RDR-003](RDR-003-ai-execution.md) | ChatGPT / Codex / Excel MCP execution | Architecture | DRAFT | NOT RUN |
| [RDR-004](RDR-004-metric-semantics.md) | Sales/customer/profitability definitions | Architecture | DRAFT | NOT RUN |

Use [TEMPLATE.md](TEMPLATE.md) for new consequential design choices. Not every implementation detail needs a new RDR.

## RDR lifecycle

- **DRAFT** — options and evidence may be revised; not approved to implement.
- **ACCEPTED** — reviewed with evidence and explicit owner approval.
- **CLOSED** — implemented or otherwise resolved; record reason and evidence.
- **SUPERSEDED / ABANDONED / DEFERRED** — explicitly explain why.

No record is accepted merely because a Markdown file was committed. No record is implemented merely because a design was described.

## Evidence classifications

- **VERIFIED** — directly checked against inspected source code/schema or a working test, with evidence.
- **DOCUMENTED** — corroborated by official/reference documentation, but not tested locally.
- **ASSUMED** — inference or unverified hypothesis. Record risk/verification plan for critical assumptions.

## Gate checklist (manual)

1. Problem and alternatives are unambiguous.
2. Source evidence and assumptions are tagged correctly.
3. Decision explains tradeoffs and dependencies.
4. Critical assumptions have verification plans.
5. An independent critique or review finds no blocking issue.
6. Owner expressly accepts; add accepted date and reviewer.
7. After implementation, record tests and close with reason.

An external agent can assist with critique but may not assert that a nonexistent independent review happened.

## Project boundary

The RDR documentation itself is **planning work only**. Data ingestion, workbook creation, model building and publishing remain unauthorized until separately requested.
