# Formal Baseline Audit

## Audit principle

The existing `submissions/zhoujiahao-source/jingzhang-legible-ai-belt/` package is treated as a **validated historical baseline / rollback point**, not as proof that the package remains current after upstream changes.

Every integration pass must re-run the latest upstream validation after edits.

## Historically established baseline

The previous formal package had already reached a reviewable structure and had passed its then-current CI / self-check workflow. That historical success is valuable because it means the integration should preferentially **reuse structurally valid artifacts** rather than scaffold from zero.

Historical non-blocking warnings included organizer data / translation limitations such as provisional boundary precision and bilingual counterpart completeness. These warnings must be re-evaluated under the latest rules rather than copied forward blindly.

## What must be re-read before reuse

### Manifest / package state

Verify current schema requires and package currently contains:

- `package_type = professional_design_package`
- `package_state = ready_for_review`
- legacy `submission_stage = formal` only where still required
- fresh file hashes after any migration
- correct proposal language / translation linkage

Status: **REVALIDATE**

### Proposal

Verify:

- all current mandatory headings / evidence tags
- `[source:...]`, `[standard:...]`, `[depth:...]`, `[data:...]`, `[metric:...]` references
- all agent.1–agent.6 tasks readable in prose
- no stale claim from old concept
- no visual / prose claim contradicts geometry or metrics

Concept status: **MAJOR REWRITE REQUIRED**

Reason: the old `Legible AI` headline is no longer the master thesis. Its valid transparency ideas may remain as a subordinate governance / information-design layer.

### Geometry

Do not redraw merely to match the new narrative.

Verify current geometry against latest allowed-design-space and organizer geometry:

- SITE_BOUNDARY role / precision
- KEY_AREA role / precision
- locked layers
- editable layers
- required layers
- generated features inside allowed boundary
- feature IDs / properties / CRS rules
- current organizer boundary availability

Status: **PRESERVE UNTIL VERIFIED; THEN MODIFY ONLY WHERE NECESSARY**

### Metrics

Verify conventional planning metrics are still reproducible from current geometry and formulas. Do not change numerical values merely to fit a new story.

Add custom city-learning metrics only with explicit status and formulas.

Status: **CONVENTIONAL METRICS REVALIDATE; CUSTOM METRICS ADD**

### Sources

Re-check every source against latest `data/source_registry.json` and current availability / license / limitation.

Status: **REVALIDATE SOURCE QUALITY; PRESERVE TRACEABILITY**

### Assumptions

Old assumptions about provisional boundary, missing official controls and other data gaps should be retained if still true, but must be updated if upstream now supplies new trusted geometry / data.

Status: **REVALIDATE**

### Compliance matrix

All official announcement tasks and `agent.1`–`agent.6` must still be explicitly mapped.

Status: **REMAP NEW CONCEPT TO EXISTING IDS; DO NOT INVENT IDS**

### Standards matrix

Keep existing mappings only if the standard IDs and local reference snapshots are unchanged.

Status: **REVALIDATE AGAINST LATEST STANDARDS INDEX**

### Design-depth matrix

All required formal design depth items must remain complete after migration.

Status: **REVALIDATE AFTER SPATIAL REWRITE**

### Figures

The previous required five figures may be structurally reusable but must be regenerated if they communicate the old concept incorrectly.

Status: **REGENERATE / RECAPTION AFTER MACHINE-READABLE PACKAGE STABILIZES**

### HTML / A3 / A0

Derived exports must be regenerated last.

Status: **DO NOT HAND-EDIT AS SOURCE OF TRUTH**

## Baseline-to-new-concept decision table

| Component | Reuse | Rewrite | New | Rule |
|---|---:|---:|---:|---|
| Existing valid source records | Yes | only limitations if needed | add new sources | Never lose provenance |
| Existing legal geometry | Yes | only required spatial proposal features | new allowed design features | Geometry remains authoritative |
| Conventional metrics | Yes | if geometry changes | custom metrics | Recompute, never hand-wave |
| Proposal structure | partial | **Yes** | City OS chapters | New thesis required |
| Legible AI governance ideas | partial | subordinate | transparency layer | Not headline |
| Scenarios | partial | align with new lifecycle | fill to >=10 | Must be spatial + measurable |
| Personas | partial | ensure diversity | fill to >=5 | Must affect design decisions |
| Ecosystem cases | partial / unknown | source check | fill to 5–8 | Transfer lessons required |
| Public-space ideas | partial | **Yes** | Public Capability Interface | Avoid AI spectacle |
| Landmarks | partial | **Yes** | 1909/2026/Future + retired archive | Memory as Place |
| Operations | partial | **Yes** | annual version release | Public Stewardship |
| VI | partial | **Yes** | Open Node / public service system | Evidence-first visual |
| PDFs / HTML | No as source | regenerate | — | Derived outputs only |

## Current highest-risk migration errors

1. Changing narrative without changing spatial design.
2. Adding custom metrics with invented observed values.
3. Showing precise provisional geometry as if official.
4. Retaining multiple competing main concepts.
5. Treating `City OS` as a software metaphor without real public-space / governance / spatial consequences.
6. Treating AI capability supply as more important than real public need.
7. Failing to revalidate old source licenses / limitations.
8. Editing figures before geometry / metrics / matrices are stable.
9. Losing traceability while modernizing prose.
10. Claiming Public Stewardship as an existing committed institution rather than a proposed governance framework.

## Baseline acceptance gate

Before the first canonical submission edit, record:

- latest upstream commit used for rule audit
- current participant branch / base SHA
- current organizer geometry status
- current schema versions / IDs relevant to submission
- current self-check result of the untouched baseline if runnable
- current CI state of the baseline PR / branch

Until this gate is completed, the integration workstream may add research and migration documents but should not overwrite trusted baseline machine-readable data.
