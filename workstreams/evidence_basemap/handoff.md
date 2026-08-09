# Handoff — Evidence & Basemap Agent

## 1. Repository state

- latest upstream ref re-audited: `open-city-ai/haidian@e533da38c89c2766aee202b19b9d053057385ef6` on 2026-08-08
- fork proposal base ref: `submission/zhoujiahao-source/jingzhang-legible-ai-belt@796d29a69774f4722fd7b5012505a3f20bb2e35d`
- branch: `agent/evidence-basemap`
- final branch HEAD: returned by the executing Agent after this handoff update and final compare

## 2. What I completed

### Rule / repository baseline
- Re-read the latest upstream Skill and required brief/data/geometry inputs again after upstream advanced during this session.
- Confirmed latest upstream `brief/site-package/geometry/` still has only provisional boundaries/basis and study bbox; no official coordinate-bearing SITE_BOUNDARY / KEY_AREA file is present.
- Audited the user's prior submission as reusable design work without treating conceptual geometry as present-state truth.
- Kept all work isolated under `workstreams/evidence_basemap/`; canonical submission remains untouched.

### Evidence inventory and uncertainty
- Built a source inventory with explicit formal/background/provisional/review-needed status and limitations.
- Built source-conflict and missing-data registers instead of silently reconciling incompatible scopes.
- Defined Official / Verified / Derived / Assumed / Unknown and Known / Estimated / Proposed / Unknown protocols.
- Preserved official reference area values separately from provisional calculated geometry.

### Three areas / two wings and spatial diagnosis
- Built source-addressable evidence profiles for all three areas and two wings, each with at least five verifiable characteristics.
- Identified 12 spatial findings and prioritized the 10 most design-critical opportunities/constraints.
- Re-verified six global AI/urban-innovation ecosystem cases and extracted transferable mechanisms plus non-transferable limits.

### Existing-condition basemap executable closure
- Added `data/basemap_config.json` with provisional discovery extent, EPSG:4326 exchange CRS, EPSG:4548 analysis CRS, source/license policy and `official_boundary=false`.
- Added `scripts/fetch_osm_basemap.py` to acquire OSM roads, rail, water, green, POI and optional buildings through Overpass with ODbL attribution and timestamped provenance.
- Added `scripts/fetch_microsoft_buildings.py` to acquire Microsoft Global ML Building Footprints under CDLA Permissive 2.0, compute required L9 tiles and bbox-filter candidate building footprints.
- The provisional overall-design discovery bbox resolves to Bing L9 quadkey `132100103`.
- Added `scripts/validate_basemap_outputs.py` for generated GeoJSON/provenance validation.
- Added `scripts/test_basemap_helpers.py` and executed its exact helper logic offline; bbox→quadkey and Overpass query composition passed.
- Added `basemap_acquisition.md` with run sequence, source promotion thresholds and cross-validation rules.

### Building evidence
- Kept old proposal buildings classified as conceptual program envelopes, not Existing.
- Added Microsoft Global ML Building Footprints as an independent **Derived** footprint candidate, not an official/current building survey.
- Kept height/floor/use/ownership and demolition/retention conclusions Unknown where unsupported.

### Source-registry handoff
- Added `data/source_registry_promotion_candidate.json` containing review-ready candidate source records for current official Beijing/Haidian evidence, OSM and Microsoft footprints.
- Did not modify project-wide `data/source_registry.json`; candidate records explicitly state allowed/prohibited uses.

### Field verification closure
- Added `data/field_audit_targets.csv` with 15 bounded targets across 众智园、AI原点、大钟寺、中关村服务翼、小月河 and the Jing-Zhang corridor.
- Added `field_audit_protocol.md` with privacy-safe capture fields, evidence promotion rules, repeatability and completion gates.
- No on-site observation is fabricated; all targets remain `pending_field` until physically observed.

### Upstream collaboration
- Searched upstream open Issues for official boundary / SITE_BOUNDARY / KEY_AREA missing-data discussion and found no matching open issue.
- Attempted to create a scoped Issue in `open-city-ai/haidian`; GitHub returned HTTP 403 `Resource not accessible by integration`.
- Preserved the complete ready-to-post issue at `upstream_issue_draft.md`.

### QA / handoff
- Expanded `scripts/validate_evidence_workstream.py` so Definition-of-Done covers original evidence files plus basemap acquisition, field targets, source-promotion candidate and blocked issue draft.
- Updated `qa_report.md`, `audit_log.md`, `README.md` and this handoff to reflect the continuation pass.
- Did not modify canonical submission geometry, proposal, metrics, sources, assumptions, figures, HTML/PDF or locked upstream layers.

## 3. Key decisions / findings

- **Finding:** exact official SITE_BOUNDARY and KEY_AREA polygons remain unavailable at the latest upstream ref.  
  **evidence:** latest upstream `brief/site-package/geometry/` inventory contains provisional boundaries/basis and study bbox only.  
  **confidence:** High.  
  **why it matters:** all boundary-derived current metrics remain intake-grade; do not present as statutory precision.

- **Finding:** competition official scales (43.6 km² / 11.4 km² / 368.4 ha; 192.1 / 104.3 / 72.0 ha key-area references) are different scopes from the ~37 km² public “三区两翼” industrial-layout narrative.  
  **evidence:** SRC-REG-OFFICIAL-ANNOUNCEMENT vs SRC-BJ-KW-THREE-WINGS-20260403.  
  **confidence:** High.  
  **why it matters:** never merge these numbers or use one as the other's polygon.

- **Finding:** AI Origin Community's public ~3 km² operational/innovation context is broader than the 104.3 ha competition reference area.  
  **evidence:** SRC-BJ-AIORIGIN-20260105 / SRC-BJ-AIORIGIN-20260324 vs competition brief.  
  **confidence:** High.  
  **why it matters:** ecosystem statistics cannot be spatially assigned to the 104.3 ha key area without new evidence.

- **Finding:** 众智园 and 大钟寺 both have 2026 official urban-renewal evidence, but renewal extents are not competition KEY_AREA polygons.  
  **evidence:** SRC-BJ-CITYUPDATE-ZZY-20260713 / SRC-BJ-CITYUPDATE-DZS-20260713.  
  **confidence:** High.  
  **why it matters:** use as implementation/current-context evidence, never boundary replacement.

- **Finding:** Jing-Zhang Park provides a real north-south public-space framework while the historic railway east-west barrier/stitching problem is documented.  
  **evidence:** SRC-BJ-JZPARK-20240920 / SRC-BJ-JZPARK-20211216.  
  **confidence:** High for framework/history; full 2026 phase-II as-built continuity remains Unknown.  
  **why it matters:** Capability Backbone can attach to a real spatial/public-memory structure, but exact crossings need GIS/field audit.

- **Finding:** Xiaoyuehe has active 2026 waterfront/water-engineering evidence; construction/ecology/water safety must precede scenario siting.  
  **evidence:** SRC-BJ-XIAOYUEHE-WATER-20260112 / SRC-BJ-XIAOYUEHE-WORKS-20260121.  
  **confidence:** High for project scope/status, not final as-built completion.

- **Finding:** old submission building/road/green/public-space values are conceptual/provisional and must not be reused as Existing.  
  **evidence:** prior submission `metrics.json` and `assumptions.json`.  
  **confidence:** High.

- **Finding:** an open, legal, reproducible current-basemap path exists without commercial map tiles: OSM for multi-layer bootstrap + Microsoft Global ML Building Footprints as an independent footprint candidate + official public pages/field audit for validation.  
  **confidence:** High for source/license workflow; actual local currentness remains feature-by-feature after retrieval.

- **Finding:** the five learning units should remain differentiated: 众智园=technology production/validation; AI Origin=social feedback/talent/public-service learning; 大钟寺=market/AI-native service validation; 中关村翼=professional-resource exchange; 小月河翼=public-space/real-city testing.  
  **evidence:** taskbook + current differentiated resource profiles.  
  **confidence:** High for task roles; variable for exact geography/resource density.

## 4. Files added or modified

| file | purpose | status |
|---|---|---|
| `README.md` | workstream boundary / execution guide | complete |
| `audit_log.md` | Phase 0–10 audit + continuation | complete |
| `source_inventory.csv` | provenance/use/licence/confidence inventory | complete for this pass |
| `source_conflicts.md` | conflict register | complete for this pass |
| `confidence_framework.md` | evidence/drawing uncertainty protocol | complete |
| `area_profiles.md` | three areas/two wings evidence profiles | complete |
| `global_ai_ecosystem_cases.md` | six global cases | complete |
| `spatial_findings.md` | 12 findings + top 10 | complete |
| `missing_data.md` | 18 missing-data items | complete; unresolved items remain Unknown |
| `field_dictionary.md` | downstream evidence interface | complete |
| `building_proxy_method.md` | building fact/proxy hierarchy | complete |
| `basemap_acquisition.md` | executable real-basemap acquisition workflow | complete |
| `field_audit_protocol.md` | public-space field audit protocol | complete protocol; physical execution pending |
| `upstream_issue_draft.md` | blocked upstream official-geometry issue | complete draft; posting blocked by 403 |
| `qa_report.md` | QA evidence/runtime caveats | complete |
| `data/area_reference_values.csv` | official area values separate from geometry | complete |
| `data/spatial_evidence_register.csv` | evidence feature register | complete |
| `data/basemap_config.json` | acquisition extent/CRS/source policy | complete |
| `data/field_audit_targets.csv` | 15 on-site verification targets | complete register; all pending_field |
| `data/source_registry_promotion_candidate.json` | maintainer-review source candidates | complete candidate package |
| `maps/01...06_*.svg` | uncertainty-safe evidence schematics | complete schematic |
| `scripts/fetch_osm_basemap.py` | OSM existing-condition acquisition | complete executable; live fetch pending networked checkout |
| `scripts/fetch_microsoft_buildings.py` | Microsoft footprint candidate acquisition | complete executable; live fetch pending networked checkout |
| `scripts/validate_basemap_outputs.py` | generated GeoJSON/provenance QA | complete executable |
| `scripts/test_basemap_helpers.py` | offline bbox/quadkey/query test | complete; helper logic passed |
| `scripts/validate_evidence_workstream.py` | whole-workstream deterministic QA | complete; checkout execution pending |
| `handoff.md` | this integration handoff | complete |

## 5. Sources and licenses

Primary source classes:
- competition official announcement / Beijing planning authority — formal-ready only within recorded scope;
- cleared Agent taskbook — formal task alignment, not statutory geometry;
- repository provisional geometry — `provisional_only`;
- Beijing/Haidian official public pages and procurement records — current/program evidence, candidate for maintainer source-registry review;
- OpenStreetMap / Overpass — ODbL 1.0, explicit `© OpenStreetMap contributors` attribution, bootstrap existing-condition data only;
- Microsoft Global ML Building Footprints — CDLA Permissive 2.0, ML-derived footprint candidate only;
- global city/government/primary institutional cases — `background_only`;
- no commercial map tiles, private maps, sensitive personal data or non-redistributable GIS.

Full source IDs/use limits: `source_inventory.csv` and `data/source_registry_promotion_candidate.json`.

## 6. Data / design status

- **Official:** competition/project task facts and official approximate reference areas within their documented scope.
- **Verified:** current urban-renewal projects, selected public-service/road/waterfront facts, Jing-Zhang public-space/history facts, primary-source global-case mechanisms.
- **Derived:** repository provisional geometry; evidence schematics; future OSM candidate layers; Microsoft building footprints; calculated discovery tile/quadkey.
- **Assumed:** no new present-state Assumed statistic is used.
- **Unknown:** exact official SITE_BOUNDARY / KEY_AREA / two-wing polygons; statutory FAR/height/density/green/setback controls; ownership; complete current building use/floors/heights; complete transport/facility capacities; heritage GIS; underground infrastructure; legal fine-grained mobility/activity data; full 2026 park as-built continuity.
- **Pending external execution:** live OSM/Microsoft materialization; field audit; organizer/authority official geometry/control acquisition.

## 7. Conflicts or risks

- 37 km² industrial narrative vs 43.6/11.4/3.684 km² competition scopes.
- AI Origin ~3 km² program context vs 104.3 ha competition reference area.
- Urban-renewal extents vs competition key-area extents.
- Historic/planned completion dates vs verified current as-built status.
- Public ecosystem statistics vs parcel-level POI/heat-map claims.
- OSM/Microsoft physical geometry vs statutory geometry/current authoritative survey.
- Microsoft imagery vintage/model error can create stale/missing/false building footprints.
- Field observation can verify a condition at a time/place but cannot create Official planning status.
- Upstream issue write is blocked by connector permission; issue text is preserved locally.

## 8. What the Final Integration Agent should adopt

### Must adopt
- uncertainty classes and visible boundary-status language;
- scope conflict separation;
- official area-reference table separated from provisional geometry metrics;
- differentiated evidence profiles for all five learning units;
- explicit Unknowns for controls/ownership/heritage/utilities;
- source IDs and limitations for current-state claims;
- rule that old conceptual building/road/green/public-space layers are not Existing evidence;
- basemap promotion rule: successful download ≠ Verified ≠ Official.

### Strong candidate
- use Jing-Zhang public-space continuity as the spatial host for Capability Backbone while preserving heritage/daily-life priority;
- use Xiaoyuehe as a low-risk public-space testing interface only after construction/ecology/safety checks;
- use current 众智园/大钟寺 urban-renewal programs as implementation-context evidence;
- use OSM + Microsoft footprint disagreement as a targeted field/imagery verification queue;
- promote approved records from `source_registry_promotion_candidate.json` through maintainer review;
- reuse the six schematic figure stories after replacing schematic alignment with validated GIS.

### Exploratory only
- precise crossing locations, service catchments, building retain/renovate decisions, population heat maps, wing extents and detailed scenario siting until new data arrives.

## 9. What I intentionally did NOT modify

- `submissions/zhoujiahao-source/jingzhang-legible-ai-belt/**`
- canonical geometry / metrics / proposal / sources / assumptions / figures / HTML/PDF
- upstream `data/source_registry.json`
- locked SITE_BOUNDARY / EXISTING_PRIMARY_ROAD / EXISTING_RAIL / EXISTING_WATER / HERITAGE_PROTECTION / REGULATORY_CONTROL
- final project name/brand/Logo/landmark design
- statutory FAR/height/road-redline/ownership/demolition conclusions

## 10. Validation performed

- check: latest upstream main / latest Skill / geometry inventory.  
  result: rules re-read at `e533da38...`; official exact polygons remain unavailable.
- check: source/license/use-status review.  
  result: OSM and Microsoft candidates have explicit open licenses/use limits; no commercial/private GIS.
- check: exact helper logic for `scripts/test_basemap_helpers.py` in isolated Python runtime.  
  result: `PASS: basemap helper tests; L9 quadkey=132100103; Overpass layer query composition valid`.
- check: upstream duplicate Issue search.  
  result: no matching open issue found.
- action: upstream issue creation.  
  result: blocked by HTTP 403 `Resource not accessible by integration`; full issue saved in `upstream_issue_draft.md`.
- check: network access for repository/container execution.  
  result: public DNS unavailable in execution container; live OSM/Microsoft download cannot be truthfully claimed.
- pending command in a networked checkout:

```bash
python3 workstreams/evidence_basemap/scripts/test_basemap_helpers.py
python3 workstreams/evidence_basemap/scripts/fetch_osm_basemap.py
python3 workstreams/evidence_basemap/scripts/fetch_microsoft_buildings.py
python3 workstreams/evidence_basemap/scripts/validate_basemap_outputs.py workstreams/evidence_basemap/data/generated
python3 workstreams/evidence_basemap/scripts/validate_evidence_workstream.py
```

## 11. Remaining dependencies, not remaining design work

The remaining items cannot be completed by a remote text/GitHub Agent without fabricating evidence:

1. **Organizer/authority dependency:** official SITE_BOUNDARY / KEY_AREA, statutory controls, heritage/utilities/ownership if not publicly cleared.
2. **Network execution dependency:** materialize current OSM/Microsoft candidate geometry and run the committed validators in a real networked checkout.
3. **Physical observation dependency:** execute the 15-target public-space field audit.
4. **Permission dependency:** post the prepared upstream data-gap Issue using an account/integration with upstream Issue write permission.

Everything else within the Evidence & Basemap Agent's role has been completed or converted into an executable/reviewable interface.