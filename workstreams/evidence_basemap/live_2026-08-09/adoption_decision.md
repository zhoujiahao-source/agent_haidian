# Live basemap adoption decision — 2026-08-09

## Decision

- **OSM live snapshot: ADOPT AS CANDIDATE EXISTING-CONDITION EVIDENCE ONLY.** The live Overpass run returned 5,532 usable features, including 1,898 building polygons inside the provisional overall-design envelope. These data can support context checks, named-anchor checks, and future manual verification queues, but cannot become an official redline, statutory survey, ownership record, or confirmed as-built inventory.
- **Microsoft Global ML Building Footprints: EXECUTED / NO PUBLISHED SITE PARTITION.** The current Microsoft 2026-07-24 `dataset-links.csv` returned HTTP 200 and 30,340 rows, but contains 0 exact rows for L9 quadkey `132100103`, 0 `China` location rows, 0 `Beijing` rows, and 0 rows sharing the target quadkey prefix. Therefore no Microsoft building polygons are available for this site from the current published index, and OSM↔Microsoft building IoU cannot be meaningfully computed.
- **Official public sources remain the authority boundary.** Official Beijing materials continue to establish textual program context and named anchors; they do not supply the missing coordinate-bearing competition redlines or a complete current building survey.

## Canonical adoption

1. Update `proposal.md` / `proposal.en.md` References so they no longer claim that live materialization is pending.
2. Update `sources.json` records `SRC-OSM-OVERPASS-LIVE` and `SRC-MS-GLOBAL-BUILDINGS-20260724` with the executed result and limitations.
3. Do **not** overwrite canonical design geometry with OSM or empty Microsoft data. Keep statutory / exact existing-condition metrics Unknown where the organizer or competent authority has not supplied them.
4. Re-run the audit when exact organizer `SITE_BOUNDARY` / `KEY_AREA` geometry or a future Microsoft index with China coverage becomes available.

Raw evidence is preserved in this directory: `osm_buildings.geojson`, `osm_context.geojson`, `microsoft_buildings.geojson`, `crosscheck_summary.json`, `ms_index_probe.json`, and `crosscheck_report.md`.
