# QA Report — Evidence & Basemap

Date: 2026-08-08

## Scope isolation

GitHub compare from base `796d29a69774f4722fd7b5012505a3f20bb2e35d` to `agent/evidence-basemap` has remained **ahead, behind_by=0** throughout this workstream. All changes are confined to `workstreams/evidence_basemap/`; no canonical `submissions/...` file and no locked upstream layer has been modified.

## Latest upstream / rule QA

- Upstream `main` was re-fetched during the continuation pass and had advanced to `e533da38c89c2766aee202b19b9d053057385ef6`.
- Latest `skills/urban-design-ai-submission/SKILL.md` was re-read at that ref.
- Latest `brief/site-package/geometry/` still contains only `provisional_boundaries.geojson`, `provisional_boundaries_basis.md`, and `study_area_bbox.geojson`.
- No official coordinate-bearing `SITE_BOUNDARY` / `KEY_AREA` file was found in the latest upstream repository.
- Targeted public web checks on official Beijing/organizer sources found text extents, official reference areas and current urban-renewal/program evidence, but no cleared downloadable GIS/CAD boundary with CRS/coordinates.

## Source QA

- Existing `source_inventory.csv` retains source-addressable current-condition evidence and formal/background/provisional distinctions.
- `data/source_registry_promotion_candidate.json` now packages new official/current/open-data sources for maintainer review without silently changing project-wide `data/source_registry.json`.
- Newly discovered public Beijing/Haidian sources remain candidate/needs-review rather than automatically formal-ready.
- OpenStreetMap is used only as a bootstrap acquisition source under ODbL 1.0 with explicit attribution.
- Microsoft Global ML Building Footprints is treated as a **Derived building candidate** under CDLA Permissive 2.0, not an official survey layer.
- No commercial map tiles, private spatial data or sensitive personal data are included.

## Spatial / uncertainty QA

- `data/area_reference_values.csv` keeps the six official reference area values separate from provisional geometry calculations.
- `data/spatial_evidence_register.csv` uses Official / Verified / Derived and Known / Estimated distinctions; provisional boundary records have `official_boundary=false`.
- `data/basemap_config.json` explicitly preserves `boundary_status=provisional_constraint`, `official_boundary=false`, exchange CRS EPSG:4326 and analysis CRS EPSG:4548.
- Exact official SITE_BOUNDARY / KEY_AREA polygons remain Unknown.
- Exact two-wing geometry remains Unknown.
- FAR, height, density, green ratio and setbacks remain Unknown.
- Current building facts remain incomplete; `building_proxy_method.md` prohibits arbitrary height/floor guessing.
- The Microsoft footprint acquisition path is a second-source geometry candidate, not a shortcut around currentness/officiality checks.

## Basemap acquisition QA

New reproducible acquisition components:

- `scripts/fetch_osm_basemap.py`: roads / rail / water / green / POI, optional OSM buildings; writes provenance, retrieval timestamp, license/attribution, limitations and default `Derived / Estimated` status.
- `scripts/fetch_microsoft_buildings.py`: computes Bing L9 quadkeys, retrieves only the required China tile(s), bbox-filters building footprints and records CDLA provenance/limitations.
- `scripts/validate_basemap_outputs.py`: validates FeatureCollection structure, geometry coordinate ranges, required provenance properties and duplicate IDs.
- `scripts/test_basemap_helpers.py`: network-free unit test for the discovery bbox, L9 quadkey and Overpass query composition.

The exact helper logic was executed in the assistant's isolated Python runtime on 2026-08-08 and returned:

```text
PASS: basemap helper tests; L9 quadkey=132100103; Overpass layer query composition valid
```

This proves the bbox→quadkey and query-composition helpers, **not** successful network retrieval of current GIS payloads.

## Network/runtime limitation

The execution container in this conversation cannot resolve public network hosts, while the GitHub connector exposes repository read/write/compare but not a shell inside the repository checkout. Therefore:

- the network-fetch scripts are committed but were not falsely reported as having downloaded OSM or Microsoft data;
- the original repository-local `validate_evidence_workstream.py` still cannot truthfully be claimed as executed against a real checkout in this environment;
- connector-side file/compare QA and an isolated exact helper test were executed.

From a networked checkout, run:

```bash
python3 workstreams/evidence_basemap/scripts/test_basemap_helpers.py
python3 workstreams/evidence_basemap/scripts/fetch_osm_basemap.py
python3 workstreams/evidence_basemap/scripts/fetch_microsoft_buildings.py
python3 workstreams/evidence_basemap/scripts/validate_basemap_outputs.py workstreams/evidence_basemap/data/generated
python3 workstreams/evidence_basemap/scripts/validate_evidence_workstream.py
```

## Conflict QA

`source_conflicts.md` explicitly preserves, rather than silently reconciles:
1. competition scopes 43.6 km² / 11.4 km² / 368.4 ha vs ~37 km² industrial-layout context;
2. AI Origin ~3 km² public-program context vs 104.3 ha competition reference area;
3. 众智园 naming/anchor ambiguity;
4. urban-renewal extents vs competition key-area extents;
5. historic construction schedule vs verified 2026 as-built status;
6. publicity statistics vs geocoded inventories;
7. physical open-data geometry vs statutory geometry;
8. old Legible AI proposal language vs the newer locked City OS constitution.

## Field-audit closure

The physical-site gap is no longer an undefined TODO. It is converted into:
- `field_audit_protocol.md`;
- `data/field_audit_targets.csv` with 15 bounded targets and explicit questions/evidence requirements.

No physical field observation is fabricated. Field status remains `pending_field` until a human/on-site sensing workflow actually executes it.

## Upstream collaboration QA

The Agent searched open upstream issues for official boundary / SITE_BOUNDARY / KEY_AREA missing-data discussions and found no matching open issue. It then attempted to create a scoped issue in `open-city-ai/haidian`, but GitHub returned HTTP 403 `Resource not accessible by integration`. The full ready-to-post issue is preserved at `upstream_issue_draft.md`.

## Deliverable QA

- each of the five areas/wings has at least five source-addressable resource characteristics;
- 12 spatial findings are recorded, with the 10 highest-impact items prioritized;
- six global cases are documented with primary/authoritative sources, mechanisms, value, limitations and transfer judgment;
- 18 missing-data items are recorded with impacts and resolution paths;
- six uncertainty-safe evidence schematics remain present;
- reproducible OSM + Microsoft building acquisition path now exists;
- generated-basemap validator and offline helper test now exist;
- 15-target field-audit package now exists;
- source-registry promotion candidates and blocked upstream issue draft now exist.

## Result

**Evidence-workstream QA: PASS at connector/source/design-interface level, with two external dependencies explicitly unresolved rather than hidden:**

1. networked execution is still required to materialize live OSM/Microsoft candidate GeoJSON and run the repository-local full validator;
2. physical field audit and organizer-supplied official geometry require capabilities/data not present in this conversation.

Neither dependency is represented as completed or Official. No formal submission preflight claim is made.