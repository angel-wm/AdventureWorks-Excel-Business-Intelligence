# AI-Assisted Excel Development

**Status:** Excel MCP has been used on the local workbook to create, refresh and read back seven Power Query worksheet loads. Model relationships, PivotTables, charts and slicers remain unverified in this project.

The purpose is to let AI **do supported Excel work**, with short explanations and verifiable results. We do not want to repeat ProcureFlow's manual, highly tutorial-oriented build process.

## Division of work

| Tool | Intended use | Verification boundary |
| --- | --- | --- |
| **Codex + Terra** | Analyze requirements, implement repeatable operations, debug and coordinate tool calls | Reasoning alone does not prove workbook edits happened |
| **User's Excel MCP for Codex** | Direct workbook creation/editing/inspection for capabilities exposed by the installed server | Discover actual commands before committing tasks |
| **ChatGPT for Excel** | Supported spreadsheet formulas, tables, formatting, charts and refinements | Read back changed objects, formulas and totals |
| **Excel 365 Desktop** | Native Power Query, Power Pivot, PivotTables and any unsupported feature | Run refresh and functional tests in the real workbook |
| **ChatGPT project chat** | Decisions, concise explanations, calculations review and quality checkpoints | Mark draft versus executed evidence accurately |

**Terra reasoning levels:** Medium for routine operations; High for transformations, complex formulas and dashboard assembly; Extra High for difficult modeling, debugging and final cross-layer review. Extra High is a selective tool, not the default for every edit.

## First technical check

From Codex, inspect the connected **Excel MCP server identity, tool list and access permissions**. Test basic open/read/edit/save/readback on a safe temporary workbook before relying on it. Specifically verify whether the installed MCP can create/refresh Power Query, manage Excel Data Model/Power Pivot, create PivotTables/charts and manage slicers. Do not infer coverage from the tool name or marketing material.

If an advanced feature is unsupported, do it through Excel Desktop or another verified method.

## Implementation loop

1. Select a small Jira task with observable acceptance criteria.
2. Inspect the target workbook/version and preserve a rollback copy before broad edits.
3. Ask Codex or ChatGPT for Excel to perform a **bounded** change.
4. Read the resulting workbook state back, not just the tool's success message.
5. Reconcile the business output with the source or an independent calculation.
6. Link the versioned artifact and evidence to Jira; only then mark the task Done.

Do not allow concurrent agents to edit the same workbook without controlled serialization or version handling.

## Prompt shape

> In the current workbook copy, create a monthly sales summary and chart using the **validated** Line Sales measure. Leave all source tables and Power Query queries unchanged. Read back the chart source, formulas, monthly totals and any errors. If you cannot perform a step, report it as unsupported.

This example is **illustrative**, not evidence of a completed operation.

## Documentation with the owner's RDR

Documentation follows the [Repository Documentation Readability Guide](https://github.com/angel-wm/repository-documentation-readability/blob/main/GUIDE.md), using the owner's [local Codex skill](../.agents/skills/repository-documentation-readability/SKILL.md) for repeated documentation work. **RDR means Repository Documentation Readability in this project, not Research–Design–Review.**

The guide governs presentation, not business semantics. Keep source contracts and verified figures authoritative. Use GitHub for documentation and [Jira](JIRA_WORKFLOW.md) for work tracking. Explanations to the user should remain short, practical and in Spanish.
