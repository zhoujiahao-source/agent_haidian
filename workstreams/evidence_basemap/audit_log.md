# Audit Log — Evidence & Basemap

## Phase 0 — repository and rule baseline

**Audit date:** 2026-08-08

### Repository state

- Latest upstream `main` observed: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff`.
- User fork `main` observed behind upstream at `5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1`.
- Existing user submission branch observed at `796d29a69774f4722fd7b5012505a3f20bb2e35d`; this is used as the workstream base because it contains the user's latest proposal-specific assets.
- Work branch: `agent/evidence-basemap`.

### Mandatory files re-read from latest upstream

- `skills/urban-design-ai-submission/SKILL.md`
- `brief/site-package/design_brief.json`
- `brief/site-package/agent_taskbook.json`
- `brief/site-package/allowed_design_space.json`
- `brief/site-package/ranges/planning_limits.json`
- `data/source_registry.json`
- `docs/data-workflow.md`
- `docs/review-rubric.md`
- `brief/site-package/geometry/` directory listing

The existing user proposal and `sources.json` were also audited on `submission/zhoujiahao-source/jingzhang-legible-ai-belt`.

### Rule changes / active rules that affect this Agent

1. The latest Skill treats `package_type=professional_design_package` as artifact type and `package_state=ready_for_review` as package readiness; legacy `submission_stage=formal` is compatibility only. This workstream will not write review status into canonical files.
2. Public-source classification remains strict: `usable_for_formal=yes`, `background_only`, `provisional_only`, and `no` cannot be silently upgraded.
3. Exact organizer-supplied SITE_BOUNDARY / KEY_AREA polygons are still absent. The upstream geometry directory currently contains only `provisional_boundaries.geojson`, its basis note, and `study_area_bbox.geojson`.
4. Official numeric planning controls for FAR, height, density, green ratio and setback remain missing in `planning_limits.json`; schema sanity bounds are not approval values.
5. The Skill now emphasizes continuous participation, progressive peer reading, issue collaboration and external-data provenance. This Agent records a future recheck action rather than treating today's evidence snapshot as permanent.
6. Official/project text allows provisional boundaries for temporary generation and discussion, but forbids using them as official redline, approval basis, precise area calculation, statutory control or ownership/engineering boundary.

### Existing submission reuse audit

The existing proposal already contains a usable evidence skeleton: six global cases, clear provisional-boundary disclaimers, a three-area/two-wing role structure, and machine-readable source references. It is reusable as prior work, but its global-case claims and area descriptions must be re-verified against authoritative sources and cannot substitute for a present-state basemap.

### Checkpoint

- Completed: upstream/fork verification, latest rule read, geometry availability check, existing proposal/source audit.
- Found: official textual scopes and official area values exist; exact official polygons and key statutory controls still do not.
- Unknown: official parcel boundaries, property rights, current complete building inventory, building heights/floors, road redlines, heritage-control GIS, underground infrastructure, full transit counts, and precise two-wing geometry.
- Next dependency: build source inventory and formal-use ratings; then profile real resources and spatial constraints without overstating precision.
