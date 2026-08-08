# QA Report — Evidence & Basemap

Date: 2026-08-08

## Scope isolation

GitHub compare from base `796d29a69774f4722fd7b5012505a3f20bb2e35d` to `agent/evidence-basemap` returned **ahead, behind_by=0**. At the pre-handoff checkpoint every changed path was under `workstreams/evidence_basemap/`; no canonical `submissions/...` file and no locked upstream layer was modified.

## Source QA

- `source_inventory.csv` contains 25 source records plus header after source-ID repair.
- Required provenance dimensions are present: source ID, topic, publisher, title, URL/path, retrieval/publication dates where known, license/reuse statement, formal-use status, confidence and limitation.
- Newly discovered public Beijing/Haidian sources are retained as `needs_registry_review` rather than promoted to repository-wide formal-ready status.
- Global case sources remain `background_only`.
- Repository provisional geometry remains `provisional_only`.
- No commercial map tiles or non-public spatial data are included.

## Spatial / uncertainty QA

- `data/area_reference_values.csv` keeps the six official reference area values separate from provisional geometry calculations.
- `data/spatial_evidence_register.csv` uses Official / Verified / Derived and Known / Estimated distinctions; provisional boundary records have `official_boundary=false`.
- Exact official SITE_BOUNDARY / KEY_AREA polygons remain Unknown.
- Exact two-wing geometry remains Unknown.
- FAR, height, density, green ratio and setbacks remain Unknown.
- Current building facts remain incomplete; `building_proxy_method.md` prohibits arbitrary height/floor guessing and requires calibration for any future Derived estimate.

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

## Deliverable QA

- each of the five areas/wings has at least five source-addressable resource characteristics;
- 12 spatial findings are recorded, with the 10 highest-impact items prioritized;
- six global cases are documented with primary/authoritative sources, mechanisms, value, limitations and transfer judgment;
- 18 missing-data items are recorded with impacts and resolution paths;
- six evidence schematics are present and visibly marked schematic / not to scale / uncertainty-safe;
- deterministic validator exists at `scripts/validate_evidence_workstream.py`.

## Runtime limitation / no fabricated PASS

The GitHub connector used in this session provides repository read/write/compare operations but not a shell on the remote checkout. Therefore the committed validator was **not** represented as having run on the branch. Connector-level inspection and compare checks were performed directly.

After checking out the branch, run:

```bash
python3 workstreams/evidence_basemap/scripts/validate_evidence_workstream.py
```

Then, if integrating candidate GIS later, additionally run repository GeoJSON/schema validators and CRS/topology checks required by the latest `SKILL.md`. The absence of new workstream GeoJSON in this pass is intentional: authoritative detailed geometry was not available, so no fake GIS layer was generated merely to satisfy a file count.

## Result

**Connector-level evidence QA: PASS with one explicit execution caveat** — the repository-local deterministic validator remains to be run in a shell checkout. This caveat is non-blocking for the evidence handoff but must not be misreported as a formal submission preflight pass.
