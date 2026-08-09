# Legacy Submission Audit｜历史候选包复用审计

## 1. Scope

Historical branch inspected:

`submission/zhoujiahao-source/jingzhang-legible-ai-belt`

Historical package inspected:

`submissions/zhoujiahao-source/jingzhang-legible-ai-belt/`

This package is treated as **design heritage / reusable concept material**, not current authority and not current validation evidence. Final naming remains the responsibility of the Final Integration Agent.

## 2. Reuse classification

### A. Reusable as concept heritage — strong candidates

These ideas remain compatible with Window 6 if re-integrated against current rules and evidence:

- reversible / approximately 100-day pilot logic;
- public legibility and L0–L3 autonomy/legibility gradient;
- explicit human/non-AI alternative path;
- public record of failed/stopped trials rather than success-only storytelling;
- developer/open-city annual event direction;
- scenario/persona structure as an organizing device;
- public-facing explanation of system state, responsibility and stop conditions;
- explicit disclosure that geometry/controls/implementation remain provisional or Unknown where sources are missing.

Reuse rule: retain the mechanism, rewrite it into the current operations/governance architecture, and re-link every claim to current sources/metrics/matrices.

### B. Reusable only after regeneration / current validation

- `proposal.md` narrative sections: useful source material, but must be reconciled with all current Window outputs and latest upstream Skill.
- `geometry/*.geojson`: may be useful as conceptual/provisional design layers, but the current repository still lacks official exact polygons; every layer must be revalidated against current schema/source rules.
- `metrics.json`: useful as a provisional calculation record only. Spatial ratios and areas derived from provisional geometry are not statutory values and must be recalculated if geometry changes.
- `sources.json` / `assumptions.json`: useful provenance scaffolding; must be refreshed against current `data/source_registry.json`, current source statuses and new legal/governance sources where applicable.
- matrices: structural format is reusable, but evidence mappings and semantic statuses require current review.
- `report/proposal.html` / `visual/index.html`: regenerate from the integrated narrative and current figures; do not assume old rendering proves current content consistency.

### C. Do **not** reuse as proof of current readiness

- old `self_check.json`;
- old `manifest.json` hash state;
- old PR/CI status;
- old A3/A0 files without regeneration/visual inspection;
- old tiny proposal figures without current visual review;
- old `ready_for_review` package state as a substitute for current four-gate validation;
- any design-depth `complete` status that depends on data currently known to be missing.

## 3. Concrete findings

### 3.1 Manifest state is internally insufficient as current proof

The historical manifest declares:

- `package_type = professional_design_package`;
- `package_state = ready_for_review`;

but its `validation_claim.self_checked` is **false**.

Therefore the package-state label cannot be treated as proof that the latest deterministic/spatial/visual/professional-evidence checks passed.

### 3.2 Historical self-check is too narrow for the current review contract

The historical `self_check.json` contains only five hand-authored checks. The current advisory-review contract separates four gate families:

1. deterministic validation;
2. spatial review;
3. visual review;
4. professional evidence review.

The five old checks do not substitute for running the current repository tools against the exact integrated head.

### 3.3 Validation PR has no recorded check evidence

The fork contains draft PR #1 for the historical submission. Its inspected head was `796d29a69774f4722fd7b5012505a3f20bb2e35d`.

Connector inspection found:

- no workflow runs for that head;
- commit status `pending`;
- zero status contexts.

Therefore this PR is **not evidence of a successful current CI/preflight**.

### 3.4 Figures are anomalously small

The five required historical PNG figures are present, but the inspected file sizes were only roughly 1.2–1.4 KB each. Presence alone is not a visual-quality gate.

Action: regenerate/review all required figures from current machine-readable data and the integrated narrative. Ensure each figure has hierarchy, legend, source note, status labels and no implied official boundary.

### 3.5 A3/A0 PDFs are anomalously small

Historical files existed at:

- `drawings/a3-booklet.pdf`
- `drawings/a0-boards.pdf`

The inspected repository metadata showed only about 1.1 KB per PDF. An attempted PDF visual inspection in the current connector environment did not yield an inspectable page image, so no claim is made about their visible contents.

Action: **do not reuse as final drawings**. Rebuild true A3/A0 review documents, confirm physical page dimensions/page count/searchable or inspectable content, and run current visual review.

### 3.6 Design-depth statuses are semantically optimistic

The historical `design_depth_matrix.json` marks many required items `complete`, including items whose site-specific professional facts are explicitly unavailable elsewhere in the package (for example official development intensity/control conditions or definitive building decisions).

Current schema permits `complete`, `incomplete`, or `data_gap`, but semantic status still has to match evidence.

Integration rule:

- `complete` may be used when the **required design response** is complete at the allowed conceptual depth and its limitations are evidenced;
- if a required item itself needs official controls/survey/ownership/engineering data not present, prefer `data_gap` or clearly explain that only the **gap disclosure / conceptual response** is complete;
- never convert `Unknown` professional facts into `complete` merely because a narrative paragraph exists.

## 4. Legacy metric status

The old package includes provisional/conceptual metrics such as:

- overall design area derived from provisional geometry;
- conceptual green/public-space ratios;
- conceptual mobility-network length;
- concept building-footprint area;
- counts of scenarios, tests, personas, landmarks and legibility levels;
- statutory-type controls such as FAR explicitly left `unknown`.

Window 6 does not promote those values into Official facts. Final Integration must distinguish:

- official text area values from the announcement;
- geometry-derived provisional values;
- concept/design-target counts;
- Unknown statutory/engineering controls.

## 5. Current upstream drift relevant to reuse

The upstream repository is a living task environment. During this Window 6 continuation pass, `main` advanced beyond the original workstream audit baseline. Recent upstream discussions also show active work around:

- stale manifest SHA-256 entries after post-finalization edits;
- generated gallery data drift;
- strengthened visual/PDF review and bilingual review packages.

Therefore Final Integration must use **current main tools at the time of integration**, not copy old hashes or assume an older validation sequence remains sufficient.

## 6. Required regeneration sequence for Final Integration

1. Sync latest upstream `main`.
2. Read latest Skill, taskbook, data workflow, source registry, standards, schemas and open relevant Issues/PRs.
3. Create/update the canonical submission from the latest scaffold/current package contract.
4. Integrate Window workstreams semantically, not by blind file copy.
5. Refresh `proposal.md`, translations and evidence references.
6. Recalculate affected GeoJSON-derived metrics.
7. Regenerate required figures from machine-readable source data where possible.
8. Regenerate `report/proposal.html` and bilingual counterparts if present.
9. Rebuild A3/A0 PDFs and inspect physical size/page content.
10. Revisit `compliance_matrix.json`, `standard_matrix.json`, `design_depth_matrix.json` status/evidence row by row.
11. Refresh all manifest hashes with the repository's current supported method.
12. Run current render/finalize/self-check/preflight and all four review gate families.
13. Fix every participant-controlled blocker before opening/updating the real submission PR.

## 7. Reuse decision table

| asset | reuse decision | reason |
|---|---|---|
| reversible pilot / 100-day logic | **reuse + strengthen** | aligned with locked reversibility/STOP decisions |
| L0–L3 legibility logic | **reuse + map to governance** | useful human-understandability layer |
| human/non-AI alternative | **reuse as must-have principle** | supports Human Override and public rights |
| failure museum / public failure record | **reuse as Retired Capability Archive / Learning Assembly** | avoids success-only memory |
| annual open-city event concept | **reuse but reframe** | must become accountability + City Version Release, not product expo |
| old scenario/persona counts | **candidate** | revalidate against current integrated proposal |
| old provisional geometry | **conditional** | non-official; current source/geometry rules apply |
| old provisional ratios/areas | **conditional** | recalculate after any geometry change |
| old sources/assumptions | **refresh** | current source registry/status may change |
| old matrices | **structure only** | evidence/status must be re-audited |
| old self_check | **do not use as proof** | not current four-gate evidence |
| old manifest hashes | **do not reuse** | hashes are content-specific and may be stale |
| old figures | **regenerate/review** | anomalously tiny, quality unverified |
| old A3/A0 PDFs | **regenerate** | anomalously tiny; page inspection not verified |
| final proposal name | **Integration decides** | Window 6 has no authority to freeze final identity |

## 8. Bottom line

The historical submission is valuable as a **conceptual ancestor**, not as a validated final package. The strongest reuse path is to preserve its reversible/human-readable/open-learning ideas while replacing its validation, metric-governance, institutional-accountability, rights, maintenance, retirement and long-term stewardship layers with the current Window 6 system and then rebuilding all presentation/evidence artifacts against latest upstream rules.