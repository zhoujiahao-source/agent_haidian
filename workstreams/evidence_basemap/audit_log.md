# Audit Log — Evidence & Basemap

**Audit date:** 2026-08-08

## Phase 0 — repository and rule baseline

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
- `brief/site-package/sources.json`
- `brief/site-package/ranges/planning_limits.json`
- `brief/site-package/standards/standards.json`
- `brief/site-package/standards/references/index.json`
- `brief/site-package/visual_style_recommendations.json`
- `brief/site-package/schemas/` listing
- `data/source_registry.json`
- `docs/data-workflow.md`
- `docs/review-rubric.md`
- `brief/site-package/geometry/` listing and provisional geometry
- existing user proposal, metrics, sources, assumptions and geometry inventory

### Active rule impacts
1. Current package logic distinguishes artifact type/readiness from legacy `submission_stage`; this Agent does not write review status into canonical files.
2. `usable_for_formal=yes`, `background_only`, `provisional_only`, `needs_review/no` cannot be silently promoted.
3. Exact organizer-supplied SITE_BOUNDARY / KEY_AREA polygons remain absent; upstream geometry contains provisional boundaries and study bbox only.
4. FAR, height, density, green ratio and setback official controls remain missing; schema sanity bounds are not approval values.
5. Provisional geometry is temporary generation/visualization/self-check material only and cannot become official redline, approval basis, precise statutory area, ownership or engineering boundary.
6. Existing `Jing-Zhang Legible AI Belt` submission is reusable prior work, but its conceptual geometry/low-confidence metrics do not constitute a present-state basemap.

**Checkpoint:** repository/rules audited; hard spatial and statutory gaps identified; no canonical file modified.

## Phase 1 — source inventory
Created `source_inventory.csv` covering competition authority, taskbook, provisional geometry, current Beijing/Haidian evidence, Jing-Zhang park history/current program evidence, Xiaoyuehe engineering, professional-service evidence and six global cases.

**Checkpoint:** each inventory row has source_id, publisher, URL/path, date, use status, confidence and limitation; current evidence was assigned explicit IDs rather than prose-only references.

## Phase 2 — legality / usability rating
Applied `yes / background_only / provisional_only / needs_registry_review` distinctions. Newly discovered public official sources are intentionally `needs_registry_review` until maintainers decide whether to promote them into the repository-wide source registry.

**Checkpoint:** no external source was silently upgraded to formal statutory evidence; no commercial map tile/private dataset entered the workstream.

## Phase 3 — multi-source spatial baseline
Because authoritative detailed GIS is not publicly present, the workstream does **not** fabricate a conventional basemap. It instead created `data/spatial_evidence_register.csv`, official reference-area table and six uncertainty-safe evidence schematics. The upstream provisional polygons remain referenced, not overwritten.

**Checkpoint:** spatial evidence exists as traceable candidate/interface data; precise road/building/facility geometry remains Unknown where unsupported.

## Phase 4 — building facts and proxies
Audited the old submission's building layer as conceptual program envelopes rather than existing buildings. Building footprints, use, floors, height, age, condition and ownership remain materially incomplete. `building_proxy_method.md` defines the future reproducible hierarchy and prohibits uncalibrated image-guessing.

**Checkpoint:** no building height/FAR/demolition inference was promoted to fact.

## Phase 5 — three areas / two wings profiles
Created `area_profiles.md` with at least five source-addressable characteristics for each of 众智园、AI原点社区、大钟寺、中关村科技服务翼、小月河场景赋能翼.

**Checkpoint:** profiles explicitly separate competition role from built fact and identify scope conflicts such as AI Origin ~3 km² context vs 104.3 ha competition reference area.

## Phase 6 — spatial problems and opportunities
Created `spatial_findings.md` with 12 findings and an explicit top-10 priority list covering north-south continuity, east-west seams, update complexity, blue-green construction, service-network uncertainty, official geometry and statutory-control gaps.

**Checkpoint:** design interfaces are phrased as evidence-led opportunities/constraints, not approved actions.

## Phase 7 — conflicts and missing data
Created `source_conflicts.md` and `missing_data.md`. Major conflicts include 37 km² industrial-layout narrative vs competition scope values; AI Origin 3 km² program context vs 104.3 ha reference; urban-renewal extents vs competition key areas; historic construction targets vs 2026 as-built status.

**Checkpoint:** unresolved facts remain Unknown rather than being reconciled through arithmetic or visual guesswork.

## Phase 8 — global AI ecosystem cases
Re-verified six cases: Punggol Digital District, Seoul Digital Inclusion, Toyota Woven City, Decidim Barcelona, Kalasatama and Enabling Village. Each records real mechanism, transfer value and limits.

**Checkpoint:** no case is treated as a master model; transfer portfolio = interoperability/testing + lived feedback + human inclusion + traceability + everyday urban embedding.

## Phase 9 — design-facing evidence interface
Created `field_dictionary.md`, stable source IDs, evidence/drawing classes, spatial register, area reference values and six evidence schematics. Downstream agents can cite sources and distinguish Known / Estimated / Proposed / Unknown without relying on color alone.

**Checkpoint:** interface is ready for Integration Agent while canonical geometry remains untouched.

## Phase 10 — QA and handoff
QA actions:
- compared branch against base submission and confirmed all workstream additions/edits are under `workstreams/evidence_basemap/`;
- re-read current source inventory and spatial register after source-ID repairs;
- checked provisional entries retain `official_boundary=false` and do not claim exact redlines;
- checked required official reference area values are preserved separately from provisional calculated geometry;
- checked new evidence uses public/official/primary sources or cleared repository sources and states limitations;
- checked six SVGs are explicitly schematic/not-to-scale and contain no remote tile dependency;
- committed deterministic `scripts/validate_evidence_workstream.py` for repeatable local CSV/SVG/file checks.

Runtime limitation: the connected GitHub environment supports repository read/write/compare but does not expose a shell on the remote repository. Therefore the committed validator could not be truthfully claimed as executed against a checkout in this session. `qa_report.md` records the connector-level checks and the exact local command Integration Agent should run after checkout. No PASS is fabricated.

**Final checkpoint:** core workstream delivery complete; remaining items are non-blocking external-data/field-survey upgrades and official geometry/control acquisition.
