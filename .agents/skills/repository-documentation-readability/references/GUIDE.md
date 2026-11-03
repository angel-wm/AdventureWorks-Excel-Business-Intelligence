<!-- Bundled reference for the repository-documentation-readability skill.
The root GUIDE.md in the source repository is canonical. Keep this bundled copy synchronized before publishing a release. -->

# Repository Documentation Readability Guide

Guide version: **0.2**

## Purpose

This guide helps make repository documentation easier to understand, scan, and maintain without reducing technical precision.

It focuses on presentation: how to explain technical material, structure a README, choose between prose, tables, procedures, code blocks, file trees, and Mermaid diagrams, and keep the result usable on both mobile and desktop.

It is **not** a standard, protocol, schema, certification system, or replacement for a project's own documentation rules. Project-native semantics, required structures, specifications, and source-of-truth documents take precedence.

The core principle is:

> Preserve technical truth, then reduce reader effort.

## Quick navigation

- [Reader intent](#start-with-the-readers-intent)
- [Audience and relevance](#audience-and-relevance)
- [Choosing a representation](#choose-the-simplest-useful-representation)
- [Troubleshooting](#troubleshooting)
- [Mermaid diagrams](#mermaid-diagrams)
- [Accessibility and Markdown portability](#accessibility-and-visual-independence)
- [README guidance](#readme-guidance)
- [Worked examples](#worked-examples)
- [Review checklist](#review-checklist)
- [Influences and boundaries](#influences-and-boundaries)

## Start with the reader's intent

Before choosing a format, identify what the reader is trying to accomplish.

A useful model comes from [Diátaxis](https://diataxis.fr/), which distinguishes four documentation needs. This guide uses those needs as a diagnostic tool; it does **not** require a repository to adopt Diátaxis as its documentation architecture.

| Reader intent | Documentation mode | Typical question | Presentation tendency |
| --- | --- | --- | --- |
| Learn by doing | Tutorial | Can you teach me how this works? | Guided sequence, concrete example, visible progress |
| Complete a task | How-to guide | How do I accomplish this specific goal? | Prerequisites, numbered steps, verification |
| Look up facts | Reference | What are the options, fields, states, or commands? | Tables, concise entries, code, exact values |
| Understand | Explanation | Why does this work this way? | Prose, examples, relationships, small diagrams |

A README may contain more than one mode, but each section should have a clear reader purpose.

Status, validation evidence, compatibility, and release information are cross-cutting concerns rather than a fifth documentation mode. Present them in the form that best serves the reader.

### Avoid mixing modes without a reason

A how-to should not become a conceptual essay in the middle of a procedure. A reference section should not hide exact values inside long narrative prose. A tutorial should not assume the knowledge it is supposed to teach.

When a document needs multiple modes, separate them with clear headings or link to a more appropriate document.

## Audience and relevance

Tell readers enough to decide quickly whether the document is for them.

When relevant, make clear:

- who the intended reader is;
- what problem or task the documentation addresses;
- why the project, feature, or procedure is useful;
- what prior knowledge, tools, permissions, or environment are required;
- important limitations or situations where the guidance does not apply;
- where a reader should go instead when they are in the wrong place.

Do not add an "Audience" or "Limitations" section mechanically. Surface this information where it reduces uncertainty.

For procedures, place prerequisites before the first dependent step. For tutorials, state the expected starting knowledge and the learning outcome. For README files, explain relevance before implementation details such as frameworks or internal architecture.

## Preserve meaning before presentation

Readability work should not weaken semantics, contracts, schemas, source fidelity, or required project structure.

Use this decision rule:

```text
Can presentation improve without changing meaning or a required contract?
├── Yes → improve the presentation.
└── No  → preserve the structure and explain it clearly.
```

If a specification requires a four-column table, keep the four columns. Improve scanability through shorter cells, better headings, progressive disclosure, or nearby explanation instead of changing the contract.

Presentation preferences never override technical requirements.

## Reader-first explanation

Technical accuracy is necessary, but accuracy alone does not make documentation easy to learn from.

Prefer an explanation order that gives the reader a mental model before implementation detail:

1. State what the project, component, or concept is.
2. Explain why it exists or what problem it solves.
3. Show the simplest useful example.
4. Introduce the important terms and structure.
5. Add implementation details, edge cases, and deeper reference material.

Do not force every section into that sequence, but use it when readers need to build understanding.

### Be didactic without becoming vague

A didactic explanation should make the technical material easier to grasp, not remove it.

Prefer:

- concrete examples before abstract edge cases;
- one new idea at a time;
- short definitions near first use;
- explicit relationships between concepts;
- examples that demonstrate the real rule;
- explanations of why a command, constraint, or design choice matters.

Avoid:

- unexplained jargon;
- long conceptual preambles before the useful point;
- oversimplifications that become technically false;
- examples that contradict the actual contract.

### Make documentation engaging through clarity

Repository documentation does not need decorative language to be engaging.

Engagement usually comes from:

- visible structure;
- short feedback loops;
- concrete examples;
- useful diagrams;
- clear progress through a procedure;
- answers appearing near the questions that motivated them.

Do not add jokes, decorative diagrams, badges, animations, or marketing copy merely to make technical documentation feel more lively.

## Choose the simplest useful representation

Use the format that best matches the information.

| Information | Preferred representation |
| --- | --- |
| Simple explanation or rationale | Short prose |
| Comparison, roles, options, properties | Markdown table |
| Ordered procedure | Numbered list |
| Repository or directory structure | Text tree |
| Literal commands, code, config, logs | Fenced code block |
| Process, decision, branching, dependency | Mermaid flowchart |
| States and transitions | Mermaid state diagram |
| Interactions over time | Mermaid sequence diagram |
| Complex visual composition Mermaid cannot express clearly | External diagram as an exception |

Do not use a diagram when prose, a table, or a short list communicates the idea more clearly.

Do not use a table for narrative explanation.

Do not turn a directory tree into a diagram unless relationships, rather than filesystem structure, are the point.

## Progressive disclosure

Readers should encounter detail in layers.

A useful progression is:

```text
orientation
    ↓
small working example
    ↓
important concepts
    ↓
task-specific detail
    ↓
deep reference / evidence
```

Keep the entry point compact. Link to deeper material instead of front-loading everything.

This does not mean hiding important constraints. Put prerequisites, warnings, unsupported states, and required conditions before the reader reaches the action they affect.

## Documentation-set qualities

Readability applies to the documentation set as well as to individual pages.

The following qualities adapt useful principles from [Write the Docs](https://www.writethedocs.org/guide/writing/docs-principles/) to repository documentation:

| Quality | Practical meaning |
| --- | --- |
| Discoverable | Readers can find the right document from likely entry points |
| Addressable | Important sections have stable headings or links that can be referenced directly |
| Cumulative | Prerequisite concepts appear before content that depends on them |
| Scoped-complete | A document covers the scope it claims to cover, or states its boundaries clearly |
| Non-duplicative | Maintained facts have one authoritative home when practical |

A README can be intentionally incomplete and still be good documentation. The problem is not limited scope; the problem is an unclear scope.

Separate documents are useful when their responsibilities are clear. Avoid maintaining the same changing fact independently in several places.

## Prose

Use prose for concepts, rationale, constraints, caveats, interpretation, and information that does not depend on visual relationships.

Prefer:

- short paragraphs;
- one main idea per paragraph;
- important information early;
- concrete terminology;
- active voice when it improves clarity;
- links near the claims or concepts they support.

Avoid:

- walls of text;
- decorative introductions;
- repeating information already expressed clearly elsewhere;
- paragraphs that mix several unrelated ideas;
- headings followed by multiple dense screens without internal structure.

For long explanations, use headings to expose the argument or learning path.

## Headings and navigation

Use a stable heading hierarchy:

```text
H1 → document title
H2 → major section
H3 → subsection
H4+ → only when deeper nesting is genuinely useful
```

Headings should communicate what the reader will learn or find beneath them.

When refactoring an existing document:

- preserve established heading anchors when practical;
- check relative links before renaming headings;
- add direct reading-path links when a long document has several independent destinations;
- avoid excessive heading depth;
- do not create a heading for every short paragraph.

Navigation should reduce search effort, not create another documentation layer to maintain.

## Tables

Use Markdown tables for compact comparison, mapping, or reference.

Good uses include:

- file → responsibility;
- concept → meaning;
- option → tradeoff;
- state → interpretation;
- topic → authoritative source.

Prefer a few meaningful columns over many metadata columns.

If a table becomes very wide and its exact shape is not required, split it or move secondary detail into prose.

If a contract requires a wide table, preserve the required columns and improve readability through concise cells, nearby explanation, or sectioning.

A table and a diagram should coexist only when they answer different questions.

## Procedures

Use numbered lists when order matters.

Example:

1. Confirm prerequisites.
2. Run the setup command.
3. Verify the expected result.
4. Continue to the next configuration step.

Put commands inside the step where they are used.

Do not turn a straightforward procedure into a flowchart unless branching, loops, or multiple paths materially affect comprehension.

When a step can fail in a predictable way, place the relevant check or recovery guidance close to that step.

## Troubleshooting

Troubleshooting documentation should help readers recognize the problem, understand the likely cause, take corrective action, and confirm recovery.

A compact pattern is:

```text
Symptom
   ↓
Likely cause
   ↓
Resolution
   ↓
Verification
```

For several recurring problems, a table can work well:

| Symptom | Likely cause | Resolution | Verify |
| --- | --- | --- | --- |
| Observable failure | Most probable explanation | Concrete corrective action | Expected healthy result |

Prefer observable symptoms over vague labels such as "it doesn't work."

When possible:

- reproduce or test the proposed resolution;
- keep the fix close to the symptom it resolves;
- distinguish known causes from guesses;
- include the expected result after the fix;
- link to deeper diagnostics only when the common path is insufficient.

If troubleshooting grows into many branches, move it into a dedicated document rather than overloading the README.

## Code, commands, and technical excerpts

Use fenced code blocks for commands, source code, configuration, logs, schemas, or literal file excerpts.

Prefer:

- one purpose per block;
- the smallest excerpt that supports the explanation;
- syntax highlighting when useful;
- surrounding prose that explains why the block matters;
- examples that can be copied with minimal editing.

Avoid:

- giant logs without selection;
- entire files when only a small excerpt matters;
- unrelated commands grouped into one block;
- screenshots of text that could be selectable text;
- example output that looks authoritative when it is only illustrative.

Distinguish commands from output when confusion is possible.

## Validate documentation claims

Examples, links, commands, outputs, and compatibility statements are technical claims.

Prefer verifying them when verification is practical.

For example:

- run or test command examples against the supported project state;
- lint code samples with the project's normal tooling when that is easy to do;
- check internal links and anchors after documentation refactors;
- verify that external links still point to the intended source;
- label illustrative output when it is not captured from a real run;
- state version assumptions when behavior changes across versions.

This adapts a useful principle from [Standard Readme](https://github.com/RichardLitt/standard-readme): documentation quality includes working links and technically credible code examples.

This guide does **not** require CI, a documentation linter, or automated link checking. Use automation when its maintenance cost is justified; otherwise perform focused manual verification.

## Repository and file structures

Use text trees for filesystem structure.

```text
repository/
├── README.md
├── GUIDE.md
├── docs/
├── examples/
└── src/
```

Text trees are compact, copyable, diff-friendly, and usually easier to read on mobile than a diagram.

Use Mermaid instead when the important information is how components relate, not where files live.

## Mermaid diagrams

Mermaid is the default diagram format when a diagram materially improves comprehension and Git-hosted Markdown is the target.

Use inline Mermaid when practical.

Do not require diagrams.net, `.drawio`, generated PNG/SVG files, or a diagram build pipeline for ordinary repository documentation.

### A diagram should answer a harder visual question

Good diagram questions include:

- What happens next?
- Where does the flow branch?
- Which component depends on which other component?
- How does a state transition?
- Which actor communicates with which system?

If a diagram only restates one short sentence, remove it.

### One diagram, one idea

Prefer small diagrams over one giant diagram.

Roughly **3–7 primary nodes** is a useful default, not a hard limit.

Split a diagram when readers have to zoom, pan, or remember too many relationships at once.

### Keep labels short

Prefer:

```text
Select relevant sources
```

over a sentence-sized node.

Put the full explanation in nearby prose.

### Choose orientation from the content

Prefer top-to-bottom (`TD` or `TB`) when:

- the diagram is sequential;
- it has several levels;
- horizontal layout would become too wide;
- vertical layout materially helps mobile reading.

Prefer left-to-right (`LR`) when:

- the flow is short;
- there are few nodes;
- the relationship is naturally pipeline-like;
- it remains readable on a phone.

Do not make every diagram vertical or every diagram horizontal.

### Match the diagram type to the question

Use:

- `flowchart` for processes, branching, dependencies, and navigation;
- `stateDiagram-v2` for lifecycle states and transitions;
- `sequenceDiagram` for interactions over time.

Use more specialized Mermaid types only when they clearly improve the explanation.

## Accessibility and visual independence

Essential meaning should not depend on visual presentation alone.

Do not rely only on:

- Mermaid rendering;
- color;
- icons;
- screenshots;
- spatial position;
- images containing text.

Important rules, decisions, constraints, and outcomes should remain understandable from Markdown text.

Use screenshots when the visual state itself is the subject, such as a UI defect, design comparison, or rendered result that cannot be explained adequately as text.

Do not use color as the only distinction between pass/fail, active/inactive, required/optional, or similar states.

## Micro-style and Markdown portability

Small writing choices affect scanability, accessibility, translation, and AI-assisted reading.

### Links

Use short, descriptive link text that still makes sense when read out of context.

Prefer:

```markdown
See the [authentication troubleshooting guide](docs/auth-troubleshooting.md).
```

Avoid vague links such as `click here`, `this document`, or a bare URL when a descriptive label is practical.

Link selectively. A link creates another decision for the reader, so prefer the most relevant destination rather than several near-duplicates.

### Terminology and abbreviations

Use the same term for the same concept unless there is a technical reason to distinguish terms.

Define unfamiliar abbreviations at first meaningful use. Do not expand abbreviations that the intended audience already understands when the expansion would add noise without helping comprehension.

Avoid changing terminology merely for stylistic variety.

### Lists and procedures

Keep sibling list items parallel where practical.

For procedures, start steps with clear actions and keep conditional context close to the action it affects.

### Global and inclusive readability

Prefer direct language that survives translation and does not depend on culture-specific jokes, idioms, or metaphors.

Use precise technical terms rather than figurative language when the figure of speech could confuse readers.

These principles align with relevant guidance in the [Google Developer Documentation Style Guide](https://developers.google.com/style), while leaving project-specific editorial choices to the project.

### Source-readable Markdown

Prefer Markdown that remains understandable in source form.

[CommonMark](https://spec.commonmark.org/) provides a portable Markdown baseline, while platforms such as GitHub add extensions and renderers on top of that baseline.

Extensions such as Mermaid can improve the rendered experience, but essential meaning should not depend on a particular renderer.

Treat renderer-specific features as progressive enhancement:

```text
plain Markdown meaning
        ↓
platform rendering
        ↓
optional richer presentation
```

If a platform extension fails to render, the surrounding text should still preserve the important technical meaning.

## Avoid duplication

Do not repeat the same information in prose, a table, and a diagram.

Use different representations together when each answers a different question.

For example:

- prose explains **why** something exists;
- a table explains **what each part means**;
- a diagram explains **how the parts relate**.

If removing one representation loses no useful information, remove it.

## README guidance

A README is usually an entry point, not the entire documentation system.

A useful progressive structure is:

```text
README
│
├── Quick understanding
│   ├── what the project is
│   ├── why it is useful
│   ├── who it is for
│   ├── important limitations
│   └── project status when relevant
│
├── Practical use
│   ├── prerequisites
│   ├── installation / setup
│   ├── smallest useful example
│   ├── common next action
│   └── common troubleshooting when useful
│
└── Deeper material
    ├── architecture / concepts
    ├── reference
    ├── decisions
    ├── contributing
    ├── help / support
    └── evidence / research
```

Not every README needs every section. The shape should follow the project and its audience.

### First screen

A reader should normally be able to learn quickly:

- what the project is;
- why it is useful;
- whether it is relevant to them;
- any important limitation that changes whether they should use it;
- where to go next.

Do not make readers scroll through badges, giant logos, exhaustive tables of contents, or implementation history before reaching that information.

### Repository coherence

Keep the repository entry points consistent.

The repository description, README title, short description, documented project name, and actual supported behavior should not contradict each other.

For public projects, include help or contribution paths when they are useful to the intended audience. GitHub's own README guidance commonly emphasizes what the project does, why it is useful, how to get started, and where to get help.

Do not add community sections merely to satisfy a checklist when the repository does not need them.

### Smallest useful example

When the project is something a reader can use directly, show the smallest example that demonstrates real value.

A useful example should be:

- technically correct;
- short enough to understand quickly;
- representative of normal use;
- followed by a path to deeper configuration or reference.

### Keep deep material out of the README when necessary

Move detailed architecture, exhaustive API reference, historical decisions, long tutorials, and validation evidence into dedicated documents when they begin to obscure the entry path.

The README should link to those sources clearly.

## Mobile and desktop balance

Optimize for both contexts.

### Mobile

Prefer:

- short sections;
- clear headings;
- narrow optional tables;
- vertical multi-step diagrams;
- short diagram labels;
- small examples;
- important information near the start of a section.

Avoid:

- optional six-column tables;
- dense horizontal diagrams;
- diagrams that require zoom to understand every node;
- long unbroken sections.

### Desktop

Use available width when it improves comprehension.

A compact horizontal flow or comparison may be better on desktop and still be acceptable on mobile.

The goal is not mobile-first at all costs. The goal is readable documentation in both contexts.

## Anti-patterns

### Diagram as decoration

Do not add a diagram that says exactly what a nearby sentence already says.

### Giant architecture diagram

Do not combine every service, file, actor, state, dependency, and validation path into one diagram.

Separate concerns when multiple diagrams genuinely help.

### Paragraphs inside diagram nodes

Keep node labels short and move explanation into prose.

### Wide optional metadata tables

If many columns are optional and the table becomes difficult to scan, keep the important comparison fields and move the rest elsewhere.

### Breaking a contract for presentation

Do not remove required fields, columns, headings, or identifiers merely to make a document visually narrower.

### Screenshots of copyable text

Use code blocks for commands, configuration, errors, or logs unless the visual rendering itself is important.

### README as the whole documentation system

Do not force specification, architecture, decisions, tutorials, history, and evidence into a single README when dedicated documents would make navigation clearer.

### Technical dump before orientation

Do not begin with implementation internals when a new reader still does not know what the project is or why it matters.

### Mixed intent without boundaries

Do not bury a conceptual explanation inside a procedure or hide exact reference values inside a long tutorial narrative.

Separate the modes with headings or link to the appropriate document.

### Unverified examples

Do not publish commands, output, compatibility claims, or links that look authoritative when nobody has checked whether they still work.

Verification does not need to be automated, but documentation claims should be treated as claims.

### Vague links or renderer-only meaning

Do not use links such as "click here" when the destination can be named.

Do not place essential meaning only in Mermaid, a platform-specific extension, color, or visual layout.

## Worked examples

The guide includes three fictional before/after transformations in [examples/before-after.md](examples/before-after.md):

- a dense README section rewritten into a clearer explanation, procedure, and compact reference table;
- an overengineered Mermaid flow simplified into a numbered procedure, keeping visual structure only where it adds information;
- an unstructured troubleshooting paragraph rewritten around symptom, cause, resolution, and verification.

Use the examples to understand the reasoning behind the transformations, not as mandatory templates. The right representation still depends on the project, audience, and technical contract.

## Review checklist

Before considering a README or documentation refactor complete, check:

- [ ] Is the reader's primary intent clear: learn, complete a task, look up facts, or understand?
- [ ] Can the reader understand the purpose quickly?
- [ ] Is the intended audience or use case clear?
- [ ] Are prerequisites and important limitations visible before they matter?
- [ ] Are technical semantics and required structures preserved?
- [ ] Does important information appear before dependent detail?
- [ ] Are long explanations divided into meaningful sections?
- [ ] Is the heading hierarchy clear and stable?
- [ ] Were existing anchors and links preserved or deliberately updated?
- [ ] Is the documentation discoverable from likely entry points?
- [ ] Can important sections be linked directly?
- [ ] Does each document clearly cover the scope it claims to cover?
- [ ] Is changing information maintained in one authoritative place when practical?
- [ ] Are comparisons represented as tables where appropriate?
- [ ] Are ordered procedures represented as numbered steps?
- [ ] Do troubleshooting paths identify a symptom, corrective action, and verification result?
- [ ] Are code and command blocks focused and copyable?
- [ ] Were executable examples, important links, and compatibility claims checked when practical?
- [ ] Are file structures represented as text trees?
- [ ] Does every diagram materially improve comprehension?
- [ ] Does each diagram communicate one main idea?
- [ ] Is diagram orientation appropriate for its content?
- [ ] Are diagrams usable on narrow screens without excessive zoom?
- [ ] Does essential meaning remain available as text?
- [ ] Is Markdown understandable in source form when renderer-specific features are unavailable?
- [ ] Does anything important depend only on color or an image?
- [ ] Are link labels descriptive rather than vague?
- [ ] Is terminology consistent, and are unfamiliar abbreviations defined?
- [ ] Are sibling list items reasonably parallel in structure?
- [ ] Is information unnecessarily duplicated?
- [ ] Does the README remain an entry point instead of becoming a reference dump?
- [ ] Can readers reach deeper material progressively?
- [ ] Are examples technically correct and representative?

## Influences and boundaries

This guide does not try to replace established documentation systems. It borrows compatible ideas where they improve repository readability, then keeps the scope narrow.

| Source | What this guide adopts | What this guide deliberately does not adopt |
| --- | --- | --- |
| [Diátaxis](https://diataxis.fr/) | Reader intent through tutorial, how-to, reference, and explanation | Mandatory repository structure or documentation architecture |
| [The Good Docs Project](https://www.thegooddocsproject.dev/) | Audience, relevance, prerequisites, reader-centered README guidance, troubleshooting | A mandatory template or fixed section inventory |
| [Standard Readme](https://github.com/RichardLitt/standard-readme) | Predictable entry points, valid links, technically credible examples | Required section order, compliance claims, badges, generators, or linters |
| [Google Developer Documentation Style Guide](https://developers.google.com/style) | Descriptive links, terminology consistency, global readability, accessibility, parallel lists | Google's house word list or product-specific editorial rules |
| [Write the Docs](https://www.writethedocs.org/guide/writing/docs-principles/) | Discoverability, addressability, cumulative ordering, completeness within scope, avoiding parallel maintenance | Organizational process requirements outside this guide's presentation scope |
| [CommonMark](https://spec.commonmark.org/) | Awareness of a portable Markdown baseline and source-readable text | Re-specifying Markdown syntax |
| [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | README as a useful entry point covering purpose, usefulness, getting started, and help when relevant | Requiring every repository to include every community document |

These are influences, not conformance targets.

When one of these sources provides deeper guidance for a specialized problem, prefer linking to that source rather than reproducing its full rules here.

Original wording in this repository remains intentionally compact and project-focused; external sources retain their own licenses and terms.

## Summary

Start with the reader's intent.

Preserve technical meaning and project-native contracts.

Make audience, prerequisites, and limitations visible when they affect the reader.

Use:

**prose for explanation, tables for comparison and reference, numbered lists for ordered procedures, code blocks for literal technical material, text trees for filesystem structure, and Mermaid for relationships or flows.**

Keep the documentation set discoverable, addressable, cumulative, scoped, and non-duplicative.

Treat examples and links as technical claims worth checking.

Prefer source-readable Markdown and use richer rendering as progressive enhancement.

Teach the reader enough to build a mental model, then expose deeper detail progressively.

The objective is not more visual material.

The objective is less friction between the reader and the technical truth.
