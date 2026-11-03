---
name: repository-documentation-readability
description: Apply clear, reader-centered, mobile-friendly presentation guidance when creating, rewriting, reviewing, or restructuring repository documentation such as READMEs, guides, runbooks, architecture notes, troubleshooting, and Markdown diagrams. Preserve project-native semantics, specifications, and required structures.
---

# Repository Documentation Readability

Use this skill for repository-documentation work. Do not invoke it for code-only tasks that do not create or modify documentation.

## Default operating rules

Apply these without loading additional references unless the task needs more depth.

1. **Preserve technical truth first.** Never change required semantics, schemas, contracts, identifiers, fields, or project-native structures merely to make documentation look simpler.
2. **Identify reader intent.** Decide whether the section primarily teaches by doing, helps complete a task, provides reference facts, or explains why something works. Separate modes when mixing them would make the document harder to use.
3. **Expose context early.** When relevant, make audience, prerequisites, limitations, and expected outcomes visible before the reader depends on them.
4. **Use the simplest useful representation.**
   - explanation or rationale → short prose;
   - comparison or reference → Markdown table;
   - ordered procedure → numbered list;
   - literal code, commands, config, logs → fenced code block;
   - filesystem structure → text tree;
   - branching, relationships, states, or interactions → Mermaid only when it reduces reader effort.
5. **Use progressive disclosure.** Start with orientation and the smallest useful path, then expose concepts, edge cases, evidence, and deep reference progressively.
6. **Keep the documentation set usable.** Prefer content that is discoverable, directly linkable, cumulative, clear about its scope, and not maintained redundantly in multiple places.
7. **Keep source text authoritative.** Essential meaning must remain understandable without Mermaid rendering, color, screenshots, or platform-specific visual features.
8. **Write for scanning.** Use descriptive headings, short paragraphs, stable terminology, descriptive links, parallel lists, and direct language that works on mobile and desktop.
9. **Treat examples as technical claims.** Check commands, links, outputs, and compatibility statements when practical. Label illustrative output when it is not from a real run.
10. **Keep READMEs as entry points.** A reader should quickly learn what the project is, why it matters, whether it is relevant, how to start, and where deeper material lives. Move exhaustive detail out when it obscures the entry path.
11. **Structure troubleshooting around recovery.** Prefer symptom → likely cause → resolution → verification.
12. **Avoid decorative complexity.** Do not add diagrams, tables, badges, headings, or duplicated explanations unless they materially improve comprehension.

## Reference-loading policy

The compact rules above are the normal path. Load supporting material only when it changes the quality of the answer.

Read **targeted sections** of `references/GUIDE.md` when the task involves:

- a substantial README or documentation rewrite;
- choosing between competing representations;
- complex Mermaid, accessibility, mobile-readability, or renderer-portability concerns;
- troubleshooting design;
- documentation-set organization or duplication;
- ambiguous conflicts between readability and a required contract;
- a detailed review against the guide.

Use the heading names in the full guide to retrieve only the relevant section whenever possible.

Read **all of `references/GUIDE.md`** only for:

- a comprehensive documentation audit;
- a broad redesign of a repository's documentation system;
- an explicit request to apply or verify the complete guide.

Read `references/before-after.md` only when examples would materially help, such as when demonstrating a transformation or deciding how to refactor a difficult section.

## Useful reference map

| Task | Consult these guide sections |
| --- | --- |
| New or rewritten README | Start with the reader's intent; Audience and relevance; Progressive disclosure; README guidance |
| Procedure or runbook | Procedures; Troubleshooting; Validate documentation claims |
| Reference-heavy documentation | Choose the simplest useful representation; Tables; Code, commands, and technical excerpts |
| Architecture or flow explanation | Mermaid diagrams; Accessibility and visual independence; Avoid duplication |
| Mobile/readability cleanup | Prose; Headings and navigation; Mobile and desktop balance |
| Terminology, links, Markdown portability | Micro-style and Markdown portability |
| Full review | Review checklist; then only the sections implicated by findings |
| Questions about borrowed practices | Influences and boundaries |

## Completion check

Before finishing, verify that:

- technical meaning and required project structures are preserved;
- the reader's likely intent and next action are clear;
- the representation is simpler than the information it explains;
- essential meaning survives plain Markdown;
- examples and links were checked when practical;
- no unnecessary duplication or visual complexity was introduced.

The bundled references provide full coverage for complex cases. Do not read them merely because they exist.
