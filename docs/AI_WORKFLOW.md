# AI-Assisted Development Workflow

**State:** PLANNING. No installed Excel MCP capability test has yet been completed for this project.

## Tool responsibilities

| Tool | Primary use | Important boundary |
| --- | --- | --- |
| ChatGPT (project chat) | Requirements, research, decisions, explanations, reviews | Explanations are not execution evidence |
| Codex / Terra | Implementation coordination, coding, analysis and debugging | Choose reasoning level proportionate to task |
| User's Excel MCP connected to Codex | Direct Excel operations **if exposed by installed tools** | Must discover actual tool list, scopes, workbook save/reopen behavior and limitations |
| ChatGPT for Excel | Build/update cells, formulas, formatting, charts and spreadsheet tasks | Confirm outcome on workbook; advanced features may not be supported |
| Excel Desktop | Native Power Query, Power Pivot, Data Model, PivotTables, slicers and final execution | Manual fallback when integrations cannot operate a feature |

The presence of an 'official' MCP label does not establish its exact tool coverage. Codex and ChatGPT for Excel may expose different operations. They must be tested separately.

## Codex reasoning choices

- **Medium:** straightforward reading, formatting, table and formula operations.
- **High:** complex Power Query, metric logic, dashboard assembly, data analysis and repair.
- **Extra High:** difficult dimensional modeling, ambiguous semantics, serious debugging or cross-layer validation.

Use Medium first for routine work. Extra High is not a substitute for test data or source evidence.

## Safe execution loop

1. **Define** one bounded task with acceptance criteria, workbook/worksheet/range and protected areas.
2. **Inspect** current workbook state; take a versioned working copy before broad mutations.
3. **Discover** MCP tools and run a small reversible trial; record exact tool versions and workbook target.
4. **Execute** only supported edits; never assume success from a tool's invocation alone.
5. **Read back** changed cells, formulas, objects, visuals, relations and refresh state where possible.
6. **Reconcile** totals and business rules with independent source checks.
7. **Commit evidence** and summarize what changed, what passed and what remains unverified.

## Phase 1 MCP capability checklist

- Can Codex enumerate/open/read/save the current workbook reliably?
- Can it create sheets, structured tables, formulas, names, formatting and charts?
- Does it support native Power Query creation/edit/refresh and result inspection?
- Can it create and inspect Excel Data Model relationships, DAX measures and PivotTables?
- Can it create connected slicers/timelines, export screenshots, and inspect refresh errors?
- Does it preserve file content and non-target sheets after save/reopen?
- Can it recover from failed actions without stale cached values?

Use **PASS / FAIL / NOT TESTED** per operation. Unsupported actions move to Excel desktop, not to unverified substitute claims.

## Prompt policy

Provide scope + intended edit + preservation rules + acceptance check. Example:

> On a copy of the open workbook, build the monthly Line Sales chart from the validated monthly summary table. Do not change Power Query queries or input sheets. Read back the resulting chart title, source range and totals. Report unsupported actions rather than simulating success.

## Verification and documentation policy

- Separate **AI-generated**, **tool-reported**, and **independently validated** outcomes.
- Preserve formula precision and source references.
- Avoid destructive edits without backups and explicit approval.
- Keep a concise change note per milestone, not a transcript of every prompt.
- For important changes, use Git for text query/measure sources and preserve workbook backup/release versions.

## References

- [OpenAI — ChatGPT for Excel](https://help.openai.com/en/articles/20001063-chatgpt-for-excel/)
- [Microsoft AdventureWorks guidance](https://learn.microsoft.com/sql/samples/adventureworks-install-configure)
- [RDR-003](rdr/RDR-003-ai-execution.md)
