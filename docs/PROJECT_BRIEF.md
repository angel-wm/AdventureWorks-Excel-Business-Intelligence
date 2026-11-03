# Project Brief

**State:** Planning baseline · **Implementation:** Not started

## Problem and goal

AdventureWorks OLTP records business transactions, not a ready-made dimensional analytics model. The project will produce an Excel BI solution that helps commercial stakeholders explain sales performance, customer behavior, product economics and scenario tradeoffs.

The portfolio goal is to demonstrate **OLTP-to-BI modeling**, practical Excel analytics and **active AI-assisted implementation**, without reproducing ProcureFlow's operational workflow complexity.

## Intended audience and questions

- **Sales manager:** How are revenue, order volume and selling mix changing over time, territory, product and order type?
- **Commercial analyst:** Which customers buy repeatedly? How do value and frequency vary by segment?
- **Product manager:** Which categories drive sales and, if trustworthy cost data allow, gross profit?
- **Decision-maker:** What would an assumed price or discount adjustment do to selected sales scenarios?

## Required capabilities (planned)

| ID | Requirement | Acceptance intent |
| --- | --- | --- |
| FR-01 | Reproducible import from official OLTP sources | Re-run refresh from the same unchanged source files |
| FR-02 | Explicit grain and relationships | Model relationships and row counts are documented and verified |
| FR-03 | Sales time-series and segmentation | Results reconcile to selected source facts |
| FR-04 | Product and territory analysis | Correct slicing without duplication or many-to-many inflation |
| FR-05 | Customer analysis | Clearly scoped customer population and time window |
| FR-06 | Profitability if cost history is defensible | Historical costs handled or gross-margin KPI postponed |
| FR-07 | Scenario worksheet | Inputs labeled as assumptions; baseline preserved |
| FR-08 | Interactive and polished Excel dashboard | Usability, filters, formulas and visuals tested |
| FR-09 | AI execution provenance | AI-generated work distinguished from manually verified facts |

## Quality constraints

- Excel 365 Desktop is the target runtime; specific OS and add-in/tool versions will be captured before execution.
- The design must not require all OLTP source tables; minimize imported columns and row copies.
- Source data stays unchanged; transformations are readable and repeatable.
- No invented sales numbers, benchmarks, margin baselines or dates.
- No misleading 'real-time' labels for historical sample data.
- No mandatory VBA automation; consider only if demonstrated necessity.

## Out of scope initially

Full ERP replacement, operational replenishment, supplier-risk workflows, demand forecasting models, manufacturing execution systems, live SQL service deployment and duplicative end-to-end ProcureFlow features.

## Open decisions

1. Exact source packaging (official CSV installation scripts versus SQL restored database) and version/date coverage.
2. Sales semantics (ordered vs shipped, line vs header level, freight and tax).
3. Channel definition and correct use of `OnlineOrderFlag`.
4. Historic product cost availability and validity.
5. Actual Excel MCP tool coverage and how to operate Power Query/Power Pivot.
6. Which dashboards are essential versus optional.

**Change control:** Consequential options and supporting research belong in [RDRs](rdr/README.md); nothing is considered tested until [Validation Plan](VALIDATION_PLAN.md) is executed.
