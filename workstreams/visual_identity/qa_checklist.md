# QA Checklist — Visual Identity Workstream

Observed against branch `agent/visual-identity`.

## Scope checks

- [x] Branch is isolated from canonical final-integration work.
- [x] Compare against working base `796d29a69774f4722fd7b5012505a3f20bb2e35d` shows workstream changes only.
- [x] No `submissions/...` file changed by Window 5.
- [x] No other Agent workstream changed.

## Minimum deliverable checks

- [x] `visual_principles.md`
- [x] `visual_audit.md`
- [x] `logo_system.md`
- [x] `naming_options.md`
- [x] `color_typography.md`
- [x] `map_language.md`
- [x] `evidence_status_system.md`
- [x] `experiment_status_system.md`
- [x] `risk_visualization.md`
- [x] `iconography.md`
- [x] `version_identity.md`
- [x] `layout_system.md`
- [x] `figure_style_guide.md`
- [x] `assets_drafts/`
- [x] `handoff.md` prepared in final QA commit.

## Definition-of-Done checks

- [x] Open Node is structurally distinct from generic AI/brain/chip marks.
- [x] Three logo geometry families documented; Family A recommended.
- [x] Evidence status and design status are visually separable.
- [x] Experiment status and risk level are independent systems.
- [x] All critical status families have non-color redundancy.
- [x] Known / Estimated / Proposed / Unknown map grammar defined.
- [x] A3 / A0 / HTML / figures / scenario cards / dashboard share one layout logic.
- [x] Exact HEX, line width, font stack, type scale and spacing tokens provided.
- [x] Annual City Version Release and Retired Capability Archive have visual rules.
- [x] Provisional geometry cannot visually masquerade as official redline under the proposed map grammar.

## Asset checks

- [x] Open Node Family A SVG present.
- [x] Open Node Family B SVG present.
- [x] Open Node Family C SVG present.
- [x] Semantic state legend SVG present.
- [x] Offline-safe CSS design tokens present; no remote font/script import.

## Repository-rule checks

- [x] Latest upstream Skill was read at observed upstream head `b3d6fdaa2331fdc60a3e618019fd8e6596532fff`.
- [x] `design_brief.json`, `agent_taskbook.json`, `allowed_design_space.json` and `visual_style_recommendations.json` were read.
- [x] Upstream geometry directory was checked: only provisional geometry + bbox were observed; no official polygon file present.
- [x] Existing candidate proposal and five required core figure filenames were audited.
- [x] Current Skill vs brief/allowed-design provisional-boundary scoring conflict recorded rather than silently resolved.

## Remaining non-blocking QA

- [ ] Pixel-level inspection of the old five PNG figures was not completed in this connector-only pass; their tiny file sizes are flagged as rebuild candidates, not asserted as conclusive visual failure.
- [ ] Final print proof / ICC / paper-stock test requires the eventual production environment.
- [ ] Optical correction of logo SVGs at final 16 px / 4 mm output should be performed during Integration.
- [ ] Full submission self-check is intentionally not run because Window 5 did not modify canonical submission and must not claim final package validation.
