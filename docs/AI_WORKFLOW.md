# AI-assisted Excel workflow

Use AI for bounded workbook work, then inspect the real result and reconcile consequential calculations against source. A successful tool reply alone does not establish correctness.

## Exercised tools

| Tool | Recorded use | Boundary |
| --- | --- | --- |
| Codex | Requirements, source analysis, implementation, documentation and coordination | Reasoning is not evidence that Excel changed |
| Excel MCP | Power Query loads/refresh, relationships, measures creation, PivotTables, slicers/timeline, layout, save and readback | Only exercised operations are supported by project evidence |
| Native Excel / targeted native automation | Historical Power Pivot formula inspection and specific unsupported layout/save operations | Individual successful fallbacks do not establish general automation coverage |
| ChatGPT add-in for Excel | Audit follow-up: five text-cell corrections across four sheets, exact readback and native range images | Original dashboard build did not use the add-in; no broad DAX/refresh capability is claimed |
| Jira and GitHub | Live work tracking and manually linked versioned evidence | Automatic linking is optional and not relied upon |

The original implementation records name Codex with Terra. This is historical tool attribution, not a requirement to use a particular model or reasoning level to maintain the project.

## Known route limitations

Direct DAX/DMV and measure listing/reading through Excel MCP encountered an unregistered provider. Historical Power Pivot dialogs supplied bounded formula readback. Native model PivotTables and several measure-creation operations succeeded. OLAP report-filter manipulation failures do not mean that native slicers/timelines are unavailable: later recorded selections worked.

A historical PivotChart creation attempt failed; standard charts backed by formulas were used and checked instead. Later dashboard work also encountered RPC/disconnection and path-reservation failures, with recovery described in its [validation record](validation/2026-11-08-dashboards.md). Do not retry an uncertain mutation blindly.

The [evidence index](validation/README.md) identifies the baseline and operations behind each claim. Tool installation or advertised capability is not proof that the project exercised it.

## Implementation loop

1. Select a Jira task with observable acceptance criteria and identify the actual workbook/session.
2. Inspect the installed tool inventory and relevant formulas/objects. Preserve a local rollback before edits.
3. Perform a bounded authorized change through a supported tool; serialize edits to the shared workbook.
4. Read values, formulas and affected native objects back. Inspect changed presentation using native images.
5. Reconcile consequential outputs against original source or an independent calculation; distinguish computation independence from reviewer independence.
6. Save and inspect the actual artifact. Run the [saved-package checks](HANDOFF.md#reproduce-the-checks), link its version/evidence and apply the [Jira workflow](JIRA_WORKFLOW.md).

When using the ChatGPT add-in, keep the intended workbook and signed-in pane active and verify that the connected session matches it. The owner opens the pane when requested; session discovery and advertised schemas govern supported operations. Excel MCP may separately perform supported native operations such as saving.

## Documentation

Use the owner's [local documentation skill](../.agents/skills/repository-documentation-readability/SKILL.md). Keep project documentation in English and communicate with the owner in Spanish. State built, checked and unverified behavior separately; [Scope decisions](DECISIONS.md) holds analytical exceptions and [Current State](CURRENT_STATE.md) holds the dated work/publication snapshot.
