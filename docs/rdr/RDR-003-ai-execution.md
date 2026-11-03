# RDR-003 — AI-Assisted Excel Execution and MCP Validation

- **Type:** Architecture
- **Status:** DRAFT
- **Priority:** High
- **Created:** 2026-11-03
- **Gate:** NOT RUN
- **Owner approval:** PENDING
- **Depends on:** [RDR-002](RDR-002-ingestion-and-model.md)

## Problem statement

Reduce manual Excel construction work using ChatGPT for Excel and Codex with the user's Excel MCP, without assuming tool capabilities or treating AI-generated calculations as verified.

## Research findings

| Class | Finding | Evidence | Check |
| --- | --- | --- | --- |
| DOCUMENTED | ChatGPT for Excel can assist with building/updating spreadsheets, formulas and formatting; Codex with the Excel add-in can inspect/edit workbook content in supported configurations. | [OpenAI help](https://help.openai.com/en/articles/20001063-chatgpt-for-excel/) | Validate on target Excel installation |
| DOCUMENTED | OpenAI cautions that AI output may be incomplete and macros/VBA are not necessarily fully supported. | [OpenAI help](https://help.openai.com/en/articles/20001063-chatgpt-for-excel/) | Inspect working results |
| VERIFIED (conversation decision) | User has Excel MCP connected to Codex and plans to use the Terra reasoning choices Medium/High/Extra High. | Project planning conversation | Verify installed server identity and tool inventory |
| ASSUMED | The installed Excel MCP can automate all desirable Excel advanced features. | **Unsupported assumption — do not rely on it** | Run capability matrix first |

## Alternatives

| Option | Benefit | Tradeoff |
| --- | --- | --- |
| AI-guided manual actions | Works for unautomated features | Repetitive and slow |
| Fully automated 'agent does everything' | Appears fast | Fragile when unsupported Excel features or silent errors appear |
| **Hybrid verified execution** (proposed) | Delegate supported work and retain native Excel checks | Needs a short tool-capability trial and QA |
| Desktop-only manual work | Precise control | Misses core project's AI-productivity objective |

## Proposed design

Use Codex + Excel MCP for programmatic edit/readback where the installed server permits. Use ChatGPT for Excel for supported sheet-level, formula, visual and cleanup actions. Use Excel Desktop directly for Power Query, Power Pivot and PivotTable operations when the integrations lack verified support. Prefer bounded, reversible changes over a single large all-at-once request.

Suggested thinking effort: **Medium** for routine operations, **High** for transformations, calculation logic and dashboards, **Extra High** for difficult modeling, bugs and independent architectural critiques.

Each task follows **inspect → specify → execute → read back → independently reconcile → record**. Back up workbooks before broad edits. A tool's successful return is insufficient unless the resulting Excel object/total was confirmed.

## Critical assumptions and mitigations

1. **Server identity/tools unverified:** collect actual registered tool list and server version from Codex before starting.
2. **Native workbook support unknown:** create a small reversible trial matrix; do not guess Power Query or DAX support.
3. **Data sensitivity:** use public Microsoft sample data; do not share private real-world datasets or credentials in prompts.
4. **AI hallucination:** every source-to-KPI transformation requires independent checks.
5. **Tool conflict:** serialize conflicting edits; save, reopen and re-inspect before release.

## Review and decision gate

- Structural review: NOT RUN
- Assumption audit: NOT RUN
- Independent critique: NOT RUN
- Owner acceptance: PENDING
- RDR status: DRAFT

## Implementation outcome

**NOT IMPLEMENTED.** No tool tests or workbook modifications performed.

## References

[AI Workflow](../AI_WORKFLOW.md) · [OpenAI ChatGPT for Excel](https://help.openai.com/en/articles/20001063-chatgpt-for-excel/)
