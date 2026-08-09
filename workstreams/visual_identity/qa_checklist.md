# QA Checklist — Visual Identity Workstream

Observed against branch `agent/visual-identity` during the completion pass.

## Scope checks

- [x] Branch remains isolated from canonical final-integration work.
- [x] No Window 5 change targets `submissions/...`.
- [x] No other Agent workstream is modified.
- [x] Work remains under `workstreams/visual_identity/` only.

## Minimum deliverables

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
- [x] `handoff.md`

## Definition-of-Done checks

- [x] Open Node is structurally distinct from generic AI/brain/chip marks.
- [x] Three geometry families documented; Family A remains recommended primary.
- [x] Small-size optical master created after actual 16/20/24 px testing.
- [x] 16 px micro identity remains legible in grayscale.
- [x] 24 px micro identity remains legible in grayscale.
- [x] 48 px primary identity (≈4.06 mm at 300 dpi) passes a grayscale proxy check.
- [x] Evidence provenance and design status are visually separable.
- [x] Experiment outcome and risk authorization are independent systems.
- [x] Critical states have text + non-color redundancy.
- [x] Complete state legend covers O/V/D/A/?, K/E/P/?, TEST/STOP/MODIFY/CONTINUE/SCALE, R1/R2/R3.
- [x] Known / Estimated / Proposed / Unknown map grammar defined.
- [x] Provisional geometry cannot visually masquerade as an official redline under the proposed grammar.
- [x] A3 / A0 / HTML / figures / scenario cards / dashboard share one layout logic.
- [x] Exact HEX, line width, font stack, type scale and spacing tokens provided.
- [x] Annual City Version Release and Retired Capability Archive have visual rules.

## Asset checks

- [x] Family A SVG present.
- [x] Family A Micro SVG present.
- [x] Family B and C SVGs present.
- [x] 16/24/48/256 px PNG QA exports present.
- [x] Single-ink 256 px PNG present.
- [x] Grayscale optical proof PNG present.
- [x] Complete semantic legend SVG present.
- [x] `asset_manifest.json` present and valid JSON in local pre-commit validation.
- [x] `design_tokens.css` has no remote imports/resources in local pre-commit validation.
- [x] `specimen.html` uses local relative assets and no remote URL in local pre-commit validation.
- [x] Micro and legend SVG source passed XML parsing in local pre-commit validation.
- [x] Raster QA exports opened with expected dimensions in local pre-commit validation.

## Legacy five-figure inspection

- [x] `site-overview.png` decoded and visually inspected at native 400×225.
- [x] `land-use-structure.png` decoded and visually inspected at native 400×225.
- [x] `key-areas.png` decoded and visually inspected at native 400×225.
- [x] `mobility-bluegreen.png` decoded and visually inspected at native 400×225.
- [x] `metrics-evidence.png` decoded and visually inspected at native 400×225.
- [x] All five are confirmed minimal schematic placeholders and marked **REBUILD** rather than merely “suspected”.

## Repository-rule / collaboration checks

- [x] Initial upstream Skill/brief audit completed at `b3d6fdaa...`.
- [x] Upstream re-check completed at `a3c14da8431f6ca63ff2059c90733132c2d4e8eb`.
- [x] Delta from initial audit showed 107 newer commits; returned changed paths were participant submissions, with no observed core-rule/geometry path in the compare response.
- [x] Current provisional-boundary scoring conflict remains documented.
- [x] Searched open upstream Issues before attempting a new one; no connector result matched.
- [x] Upstream Issue creation attempted and blocked by connector permission (`403`).
- [x] Fork tracking Issue attempted and blocked because Issues are disabled (`410`).
- [x] Collaboration failure/next action recorded in `collaboration_log.md` and handoff.

## Remaining non-blocking / external items

- [ ] **Physical print proof / ICC / paper-stock / final output-device test.** This requires the eventual production environment and cannot be truthfully completed inside this repository-only Agent runtime.
- [ ] **Full formal submission self-check.** Intentionally not run because Window 5 has no canonical submission modification authority. Running it here would not validate the Integration Agent's future merged package.
- [ ] **Final project master name.** Explicitly Integration-owned; Window 5 only supplies candidates.
- [ ] **Official organizer polygons.** Not observed in the audited upstream geometry package; Window 5 cannot manufacture them.

All remaining unchecked items are outside Window 5's executable authority/environment and are explicitly handed off rather than silently marked complete.
