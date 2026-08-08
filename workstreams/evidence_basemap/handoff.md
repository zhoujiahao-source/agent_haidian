# Handoff — Evidence & Basemap Agent

## 1. Repository state

- upstream ref: `open-city-ai/haidian@b3d6fdaa2331fdc60a3e618019fd8e6596532fff` observed on 2026-08-08
- fork base ref: `submission/zhoujiahao-source/jingzhang-legible-ai-belt@796d29a69774f4722fd7b5012505a3f20bb2e35d`
- branch: `agent/evidence-basemap`
- final content/QA commit before this handoff file: `e6552d473700fad3efbca03bf1e6c6104f4f37f9`
- final branch HEAD including this handoff file: self-referential; exact SHA is returned by the executing Agent in the final chat response.

## 2. What I completed

- Re-read latest upstream Skill, brief, taskbook, allowed design space, source registry, planning limits, standards/reference index, visual guidance, schema inventory, data workflow, review rubric and geometry availability.
- Audited the user's latest prior submission as reusable prior work without treating its conceptual geometry as present-state truth.
- Built a source inventory with explicit formal/background/provisional/review-needed status and limitations.
- Built source-conflict and missing-data registers rather than silently reconciling mismatched scopes.
- Built source-addressable evidence profiles for all three areas and two wings, each with at least five verifiable characteristics.
- Identified 12 spatial findings and prioritized the 10 most design-critical opportunities/constraints.
- Re-verified six global AI/urban-innovation ecosystem cases and extracted transferable mechanisms plus non-transferable limits.
- Defined Official / Verified / Derived / Assumed / Unknown and Known / Estimated / Proposed / Unknown protocols.
- Added an integration-facing field dictionary, official reference-area table, spatial evidence register and building proxy method.
- Added six uncertainty-safe evidence schematics without commercial map tiles or invented official geometry.
- Added a deterministic workstream validator and documented connector-level QA.
- Did not modify canonical submission geometry, proposal, metrics or locked upstream layers.

## 3. Key decisions / findings

- **Finding:** exact official SITE_BOUNDARY and KEY_AREA polygons remain unavailable in latest upstream geometry.  
  **evidence:** upstream `brief/site-package/geometry/` contains provisional boundaries/basis and study bbox only; source registry marks provisional geometry `provisional_only`.  
  **confidence:** High.  
  **why it matters:** all boundary-derived current metrics remain intake-grade; do not present as statutory precision.

- **Finding:** competition official scales (43.6 km² / 11.4 km² / 368.4 ha; 192.1 / 104.3 / 72.0 ha key-area references) are different scopes from the ~37 km² public “三区两翼” industrial-layout narrative.  
  **evidence:** SRC-REG-OFFICIAL-ANNOUNCEMENT vs SRC-BJ-KW-THREE-WINGS-20260403.  
  **confidence:** High.  
  **why it matters:** do not merge these numbers or use one as the other's polygon.

- **Finding:** AI Origin Community's public ~3 km² operational/innovation context is broader than the 104.3 ha competition reference area.  
  **evidence:** SRC-BJ-AIORIGIN-20260105 / SRC-BJ-AIORIGIN-20260324 vs competition brief.  
  **confidence:** High.  
  **why it matters:** ecosystem statistics cannot be spatially assigned to the 104.3 ha key area without new evidence.

- **Finding:** 众智园 and 大钟寺 both have 2026 official urban-renewal evidence, but the renewal extents are not competition KEY_AREA polygons.  
  **evidence:** SRC-BJ-CITYUPDATE-ZZY-20260713 / SRC-BJ-CITYUPDATE-DZS-20260713.  
  **confidence:** High.  
  **why it matters:** these are strong real-world implementation contexts, not boundary replacements.

- **Finding:** Jing-Zhang Park provides a real north-south public-space framework and the historic railway's east-west barrier/stitching problem is explicitly documented.  
  **evidence:** SRC-BJ-JZPARK-20240920 / SRC-BJ-JZPARK-20211216.  
  **confidence:** High for framework/history; full 2026 phase-II as-built continuity remains Unknown.  
  **why it matters:** Capability Backbone can attach to a real spatial/public-memory structure while crossing-level design still needs survey.

- **Finding:** Xiaoyuehe has active 2026 public waterfront/water-engineering evidence; treatment segment is about 6.41 km and water-bureau construction content includes greening/path improvements.  
  **evidence:** SRC-BJ-XIAOYUEHE-WATER-20260112 / SRC-BJ-XIAOYUEHE-WORKS-20260121.  
  **confidence:** High for project scope/status, not for final as-built completion.  
  **why it matters:** it is the strongest real linear public-space test context, but construction/ecology/water safety must precede AI scene siting.

- **Finding:** old submission building/road/green/public-space values are conceptual/provisional and must not be reused as Existing.  
  **evidence:** prior submission `metrics.json` and `assumptions.json`.  
  **confidence:** High.  
  **why it matters:** replace those layers before claiming current building footprint, green ratio, public-space ratio or mobility length.

- **Finding:** the five learning units should remain differentiated: 众智园=technology production/validation; AI Origin=social feedback/talent/public-service learning; 大钟寺=market/AI-native service validation; 中关村翼=professional-resource exchange; 小月河翼=public-space/real-city testing.  
  **evidence:** taskbook + current differentiated resource profiles.  
  **confidence:** High for task roles; variable for exact geography/resource density.  
  **why it matters:** avoid five identical AI districts.

## 4. Files added or modified

| file | purpose | status |
|---|---|---|
| `README.md` | workstream boundary/readme | complete |
| `audit_log.md` | phase 0–10 checkpoints and rule audit | complete |
| `source_inventory.csv` | source provenance/use/licence/confidence table | complete for this pass |
| `source_conflicts.md` | conflicting scopes/evidence reconciliation | complete for this pass |
| `confidence_framework.md` | evidence/drawing uncertainty protocol | complete |
| `area_profiles.md` | three areas/two wings evidence profiles | complete |
| `global_ai_ecosystem_cases.md` | six global cases | complete |
| `spatial_findings.md` | 12 findings + top 10 | complete |
| `missing_data.md` | 18 missing-data items | complete |
| `field_dictionary.md` | downstream evidence interface | complete |
| `building_proxy_method.md` | reproducible future building proxy hierarchy | complete |
| `data/area_reference_values.csv` | official area values separated from geometry | complete |
| `data/spatial_evidence_register.csv` | evidence-layer feature register | complete |
| `maps/README.md` | evidence-map caveats | complete |
| `maps/01_existing_structure_evidence.svg` | current structure evidence schematic | complete schematic |
| `maps/02_mobility_breaks.svg` | mobility/seam audit schematic | complete schematic |
| `maps/03_blue_green_public_space.svg` | blue-green/public-space schematic | complete schematic |
| `maps/04_innovation_service_resources.svg` | innovation/service evidence schematic | complete schematic |
| `maps/05_three_areas_two_wings_profiles.svg` | differentiated-unit schematic | complete schematic |
| `maps/06_confidence_status.svg` | uncertainty legend schematic | complete |
| `scripts/validate_evidence_workstream.py` | deterministic local QA | committed; shell execution pending |
| `qa_report.md` | QA evidence/caveat | complete |
| `handoff.md` | this integration handoff | complete |

## 5. Sources and licenses

Primary source classes used:
- competition official announcement / Beijing planning authority — formal-ready only within recorded scope;
- cleared Agent taskbook — formal task alignment, not statutory geometry;
- repository provisional geometry — `provisional_only`, never official redline/control;
- Beijing/Haidian official public pages and public procurement records — present-state/program evidence, entered as `needs_registry_review` for project-wide promotion;
- OSM license reference is recognized, but no new OSM extract was committed in this pass;
- global city/government/primary institutional case sources — `background_only`;
- no commercial map tiles, private maps, sensitive personal data or non-redistributable GIS added.

Full source IDs, URLs, dates, reuse status and limitations: `source_inventory.csv`.

## 6. Data / design status

- **Official:** project/competition names and task requirements; official approximate scope/reference-area values; three-area/two-wing roles where defined by task materials.
- **Verified:** current urban-renewal projects, selected public-service/road/waterfront program facts, Jing-Zhang public-space/history facts, primary-source global-case mechanisms.
- **Derived:** repository provisional geometry and any schematic relationship representation; must remain labelled.
- **Assumed:** no new present-state Assumed statistic is used; future design assumptions belong in design/integration layers.
- **Unknown:** exact official boundaries/key areas/two-wing polygons, formal FAR/height/density/green/setback controls, ownership, full building facts, complete current transport/POI/capacity data, heritage GIS, underground infrastructure, fine-grained legal mobility/activity data, full 2026 park as-built status.

## 7. Conflicts or risks

- Scope-number collision is the largest presentation risk: 37 km² industrial narrative must not be confused with 43.6/11.4/3.684 km² competition scopes.
- AI Origin 3 km² operational context must not become a fake 104.3 ha evidence boundary.
- Urban-renewal textual extents are valuable but cannot overwrite competition provisional/official geometry.
- Historic planned completion dates must not be upgraded to current as-built status.
- Public ecosystem statistics are not parcel-level POI data and cannot support fabricated heat maps.
- Current branch adds schematics, not survey-grade GIS; they must not be presented as formal basemap drawings.
- New official public sources require maintainer review before project-wide source-registry promotion.

## 8. What the Final Integration Agent should adopt

### Must adopt
- uncertainty classes and visible boundary-status language;
- scope conflict separation;
- official area-reference table separated from provisional geometry metrics;
- the differentiated evidence profiles of the five learning units;
- explicit Unknowns for statutory controls/ownership/heritage/utilities;
- source IDs and limitations for any current-state claim;
- rule that old conceptual building/road/green/public-space layers are not Existing evidence.

### Strong candidate
- use Jing-Zhang public-space continuity as the spatial host for Capability Backbone while preserving heritage/daily-life priority;
- use Xiaoyuehe as a low-risk public-space testing interface only after construction/ecology/safety checks;
- use current 众智园/大钟寺 urban-renewal programs as implementation-context evidence;
- use the six-case portfolio rather than copying one global smart-city model;
- reuse the six schematic figure stories after replacing schematic alignment with verified GIS.

### Exploratory only
- precise crossing locations, service catchments, building-retain/renovate decisions, population heat maps, wing extents and any detailed scenario siting until new data arrives.

## 9. What I intentionally did NOT modify

- `submissions/zhoujiahao-source/jingzhang-legible-ai-belt/**`
- canonical `geometry/**`, `metrics.json`, proposal, sources, assumptions, figures, HTML/PDF
- locked SITE_BOUNDARY / EXISTING_PRIMARY_ROAD / EXISTING_RAIL / EXISTING_WATER / HERITAGE_PROTECTION / REGULATORY_CONTROL layers
- final project name/brand/Logo/landmark design
- statutory FAR/height/road redline/ownership/demolition conclusions

## 10. Validation performed

- command/check: GitHub compare base submission → work branch.  
  result: branch ahead, no behind; all changed paths confined to `workstreams/evidence_basemap/` at QA checkpoint.
- command/check: current upstream geometry directory + provisional metadata read.  
  result: official exact polygons still unavailable; provisional status preserved.
- command/check: current source inventory and spatial register re-read after source-ID repair.  
  result: key current claims source-addressable; provisional boundary records retain `official_boundary=false`.
- command/check: source/license/use-status review.  
  result: no commercial map tile/private spatial source; new public evidence is not silently promoted to formal-ready.
- command/check: deterministic script `python3 workstreams/evidence_basemap/scripts/validate_evidence_workstream.py`.  
  result: **not executed in this connector-only repository runtime**; script is committed and exact execution caveat is recorded in `qa_report.md`. Do not report a fabricated local PASS.

## Integration next actions

1. Re-fetch upstream `main` and latest Skill before integration.
2. Run the committed validator in a real checkout.
3. Promote newly discovered public sources into repository `data/source_registry.json` only after maintainer review.
4. Acquire/verify official SITE_BOUNDARY / KEY_AREA and statutory controls; rerun all spatial metrics/figures.
5. Build the actual existing-condition GIS from licensed/open/official roads, buildings, blue-green and facility data with timestamps/CRS/provenance.
6. Conduct field audit for crossings, entrances, accessibility, ground-floor uses, construction closures and public-space use.
