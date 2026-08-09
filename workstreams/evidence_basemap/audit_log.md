# Audit Log — Evidence & Basemap

**Audit date:** 2026-08-08

## Phase 0 — repository and rule baseline

### Repository state
- Initial upstream `main` observed: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff`.
- Continuation-pass upstream `main` re-checked at: `e533da38c89c2766aee202b19b9d053057385ef6`.
- User fork `main` was older than the latest proposal-specific user branch.
- Existing user submission branch observed at `796d29a69774f4722fd7b5012505a3f20bb2e35d`; this remains the workstream base because it contains the user's latest proposal-specific assets.
- Work branch: `agent/evidence-basemap`.

### Mandatory files re-read from upstream
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

The latest Skill was re-read again after upstream advanced to `e533da38...`; the Evidence & Basemap conclusions below remain compatible with the current rules.

### Active rule impacts
1. Current package logic distinguishes artifact type/readiness from legacy `submission_stage`; this Agent does not write review status into canonical files.
2. `usable_for_formal=yes`, `background_only`, `provisional_only`, `needs_review/no` cannot be silently promoted.
3. Exact organizer-supplied SITE_BOUNDARY / KEY_AREA polygons remain absent at latest upstream ref; the geometry directory still contains provisional boundaries/basis and study bbox only.
4. FAR, height, density, green ratio and setback official controls remain missing; schema sanity bounds are not approval values.
5. Provisional geometry is temporary generation/visualization/self-check material only and cannot become official redline, approval basis, precise statutory area, ownership or engineering boundary.
6. Existing `Jing-Zhang Legible AI Belt` submission is reusable prior work, but its conceptual geometry/low-confidence metrics do not constitute a present-state basemap.
7. Latest Skill requires external credible data to preserve publisher, URL, retrieval/publication time, spatial/temporal coverage, license, transformations and limitations; important claims should be independently cross-checked.

**Checkpoint:** repository/rules audited twice against a moving upstream; hard spatial and statutory gaps identified; no canonical file modified.

## Phase 1 — source inventory
Created `source_inventory.csv` covering competition authority, taskbook, provisional geometry, current Beijing/Haidian evidence, Jing-Zhang park history/current program evidence, Xiaoyuehe engineering, professional-service evidence and six global cases.

**Checkpoint:** each inventory row has source_id, publisher, URL/path, date, use status, confidence and limitation; current evidence was assigned explicit IDs rather than prose-only references.

## Phase 2 — legality / usability rating
Applied `yes / background_only / provisional_only / needs_registry_review` distinctions. Newly discovered public official sources are intentionally `needs_registry_review` until maintainers decide whether to promote them into the repository-wide source registry.

Continuation work adds `data/source_registry_promotion_candidate.json` so maintainers can review candidate records without editing the project-wide registry from this specialist branch. It includes explicit allowed/prohibited uses for current urban-renewal, mobility, waterfront, public-service, OSM and Microsoft building sources.

**Checkpoint:** no external source was silently upgraded to formal statutory evidence; no commercial map tile/private dataset entered the workstream.

## Phase 3 — multi-source spatial baseline
Initial pass intentionally did **not** fabricate a conventional basemap where authoritative detailed GIS was absent. It created `data/spatial_evidence_register.csv`, official reference-area table and six uncertainty-safe evidence schematics.

Continuation pass closes the executable-data gap with a reproducible candidate basemap stack:
- `data/basemap_config.json` — provisional discovery extent, CRS and source policy;
- `scripts/fetch_osm_basemap.py` — OSM/Overpass roads, rail, water, green, POI and optional buildings with ODbL attribution;
- `scripts/fetch_microsoft_buildings.py` — Microsoft Global ML Building Footprints under CDLA Permissive 2.0, bbox-filtered from L9 tile `132100103`;
- `scripts/validate_basemap_outputs.py` — generated GeoJSON/provenance checks;
- `scripts/test_basemap_helpers.py` — offline bbox→quadkey/query-composition unit test;
- `basemap_acquisition.md` — execution, license, cross-validation and promotion protocol.

The output remains `Derived / Estimated` until cross-checking; download success can never make a layer Official.

**Checkpoint:** an actual reproducible existing-condition GIS acquisition path now exists without overwriting upstream locked/provisional layers.

## Phase 4 — building facts and proxies
Audited the old submission's building layer as conceptual program envelopes rather than existing buildings. Building footprints, use, floors, height, age, condition and ownership remain materially incomplete. `building_proxy_method.md` defines the future reproducible hierarchy and prohibits uncalibrated image-guessing.

Continuation adds Microsoft Global ML Building Footprints as an independent candidate footprint source. Microsoft documents global ML-derived building footprints from imagery of varying vintage and CDLA Permissive 2.0 licensing. This does not resolve currentness or officiality: discrepancies with OSM/official/field evidence remain conflicts.

**Checkpoint:** no building height/FAR/demolition inference was promoted to fact; building acquisition is now executable and explicitly Derived.

## Phase 5 — three areas / two wings profiles
Created `area_profiles.md` with at least five source-addressable characteristics for each of 众智园、AI原点社区、大钟寺、中关村科技服务翼、小月河场景赋能翼.

**Checkpoint:** profiles explicitly separate competition role from built fact and identify scope conflicts such as AI Origin ~3 km² context vs 104.3 ha competition reference area.

## Phase 6 — spatial problems and opportunities
Created `spatial_findings.md` with 12 findings and an explicit top-10 priority list covering north-south continuity, east-west seams, update complexity, blue-green construction, service-network uncertainty, official geometry and statutory-control gaps.

**Checkpoint:** design interfaces are phrased as evidence-led opportunities/constraints, not approved actions.

## Phase 7 — conflicts and missing data
Created `source_conflicts.md` and `missing_data.md`. Major conflicts include 37 km² industrial-layout narrative vs competition scope values; AI Origin 3 km² program context vs 104.3 ha reference; urban-renewal extents vs competition key areas; historic construction targets vs 2026 as-built status.

Continuation converts two vague missing-data tasks into executable interfaces:
- physical GIS acquisition has scripts/config/validation;
- field verification has `field_audit_protocol.md` and `data/field_audit_targets.csv` with 15 bounded targets.

The actual official geometry/statutory controls and on-site observations remain Unknown/pending rather than falsely completed.

**Checkpoint:** unresolved facts remain Unknown; resolution paths are now explicit and reproducible.

## Phase 8 — global AI ecosystem cases
Re-verified six cases: Punggol Digital District, Seoul Digital Inclusion, Toyota Woven City, Decidim Barcelona, Kalasatama and Enabling Village. Each records real mechanism, transfer value and limits.

**Checkpoint:** no case is treated as a master model; transfer portfolio = interoperability/testing + lived feedback + human inclusion + traceability + everyday urban embedding.

## Phase 9 — design-facing evidence interface
Created `field_dictionary.md`, stable source IDs, evidence/drawing classes, spatial register, area reference values and six evidence schematics. Downstream agents can cite sources and distinguish Known / Estimated / Proposed / Unknown without relying on color alone.

Continuation adds:
- generated-data schema/provenance validation;
- source-registry promotion candidates;
- field-audit targets/protocol;
- ready-to-post upstream official-geometry data-gap Issue.

**Checkpoint:** interface is ready for Integration Agent while canonical geometry remains untouched.

## Phase 10 — QA, collaboration and handoff
QA actions include:
- comparing branch against base submission and checking workstream-only scope;
- re-reading source inventory and spatial register after source-ID repairs;
- checking provisional entries retain `official_boundary=false`;
- separating official reference area values from provisional calculated geometry;
- checking source license/use limitations;
- checking six SVGs are explicitly schematic/not-to-scale;
- committing deterministic `scripts/validate_evidence_workstream.py` and expanding it to cover the new acquisition/field/source-candidate files;
- computing the provisional overall-design discovery bbox L9 Bing quadkey and exercising the exact helper logic offline: `132100103`;
- verifying Overpass query composition offline without claiming live network retrieval.

### External collaboration attempt
Latest Skill recommends opening/joining Issues for shared missing-data problems. The Agent searched upstream open issues for official boundary / SITE_BOUNDARY / KEY_AREA missing-data discussion and found no matching open issue. It then attempted to create a scoped upstream Issue; GitHub returned HTTP 403 `Resource not accessible by integration`. The fully researched ready-to-post text is saved in `upstream_issue_draft.md`.

### Runtime limitation / no fabricated PASS
The available execution container cannot resolve public network hosts, and the connected GitHub environment does not expose a shell in the remote repository. Therefore:
- current OSM/Microsoft payloads were not falsely reported as downloaded;
- the repository-local full validator was not falsely reported as executed against a checkout;
- source/rule/branch checks were performed through GitHub; helper logic was executed offline in the available Python runtime.

From a networked checkout the closure sequence is:

```bash
python3 workstreams/evidence_basemap/scripts/test_basemap_helpers.py
python3 workstreams/evidence_basemap/scripts/fetch_osm_basemap.py
python3 workstreams/evidence_basemap/scripts/fetch_microsoft_buildings.py
python3 workstreams/evidence_basemap/scripts/validate_basemap_outputs.py workstreams/evidence_basemap/data/generated
python3 workstreams/evidence_basemap/scripts/validate_evidence_workstream.py
```

**Final checkpoint:** every remaining task that can be completed within this Agent's authority has been converted into committed evidence, executable acquisition/validation code, or a bounded handoff interface. Only organizer/authority-supplied official data, live network materialization, and physical on-site observation remain external dependencies; none is disguised as complete.