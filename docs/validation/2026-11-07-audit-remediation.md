# Audit follow-up — 2026-11-07

**Scope:** local documentation, the current workbook, Jira status and the Git objects reachable from local refs. This record is not a security certification or public-release approval.

## Workbook checks

`KeyChecks` now references the seven source Power Query queries directly. It includes a 25th check for non-empty product subcategory IDs that do not match a subcategory. Empty subcategory values remain allowed. These checks inspect query results; they do not independently detect arbitrary manual changes made only to worksheet cells.

The saved local workbook's SHA-256 at this checkpoint is `421a5aab7605e92ab61c4e74588b768193d03c2888a07a9e1cf73f66f16cf1b4`. It includes pre-existing local workbook changes. A backup was saved outside Git before the audit edits.

| Check | Observed result |
| --- | --- |
| Original source snapshot, full MCP refresh | Eight queries and three PivotTables refreshed; all 25 controls returned zero; six model relationships remained active |
| Disposable copy with one non-empty invalid product subcategory | Full MCP refresh reported one invalid product subcategory; the other controls returned zero |
| Same copy after restoring its source file | Full MCP refresh returned the invalid-subcategory control to zero |
| Source preservation | The original `Product.csv` SHA-256 remained `df0379a7cba8b11b97ea5d104cf1313ef9f683137b6426f2fac6bb8c74c2a2ea` |

The test uses Excel MCP's full-refresh operation and a local copied dataset. It does not prove the behavior of every Excel refresh path, concurrent changes, another machine or a missing source. Review refresh failures before trusting any displayed check results.

## Public-portfolio review

The tracked workbook contains Microsoft sample data, workbook author metadata and cached local filesystem paths that identify a Windows user and project location. Earlier workbook versions in local Git history also contain local paths. Ignoring raw files does not remove data loaded into the workbook or content from history.

A targeted pattern scan covered 64 text blob versions and XML/relationship parts of three workbook blob versions reachable from the local Git refs. The current workbook's binary Data Model was also scanned as raw bytes for the same patterns. The scan found no matches for the specific GitHub, AWS and OpenAI token formats or private-key headers checked. It is limited: raw byte scanning is not structured inspection of the Data Model, older binary models were not scanned, and no scan covers every possible secret format. A remote heads-and-tags check on 2026-11-07 returned only `main` at the previously synchronized commit and no tags; it does not cover other remote reference types. Git author/committer addresses observed in local history used GitHub's no-reply domain.

No repository deletion or history rewrite was performed. Before changing repository visibility, decide whether the exposed author identity and paths are acceptable, inspect the chosen remote refs and binary content as appropriate, and review the current workbook's metadata. Removing a path from a new workbook revision alone does not erase it from earlier commits. Any history rewrite or public visibility change is a separate operation.
