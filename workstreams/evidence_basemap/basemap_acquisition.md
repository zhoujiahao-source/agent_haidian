# Existing-condition basemap acquisition

## Status

This workstream now contains a reproducible acquisition path for the missing real existing-condition GIS. The scripts are intentionally separate from the canonical submission and write only to `workstreams/evidence_basemap/data/generated/` when run in a networked checkout.

**Important:** no generated layer becomes Official merely because it was downloaded successfully. Output defaults to `Derived / Estimated`; important physical claims require cross-checking before promotion to `Verified / Known`.

## Latest rule check

Upstream was re-read at `open-city-ai/haidian@e533da38c89c2766aee202b19b9d053057385ef6` on 2026-08-08. The latest `brief/site-package/geometry/` still contains only provisional boundaries/basis and study bbox. No official coordinate-bearing `SITE_BOUNDARY` or `KEY_AREA` file was available in the repository at that ref.

Targeted public-source checks on 2026-08-08 also found current official announcements, urban-renewal extents and planning narratives, but no publicly downloadable cleared GIS/CAD boundary with CRS/coordinates. Therefore the acquisition extent remains a **provisional discovery/clip extent**, not an official redline.

## Source stack

### 1. OpenStreetMap / Overpass

Use for bootstrap physical layers:
- roads / paths;
- rail / stations / subway entrances;
- water;
- parks / green-space tags;
- public facilities / POI;
- optionally OSM buildings.

License: ODbL 1.0. Required attribution: `© OpenStreetMap contributors`.

Script: `scripts/fetch_osm_basemap.py`.

The script stores retrieval time, endpoint, query and per-feature source ID. Completeness and currentness are not guaranteed, so the default evidence class is `Derived`.

### 2. Microsoft Global ML Building Footprints

Use as a second independent footprint candidate where official building outlines are unavailable. The current Microsoft dataset documents global ML-derived footprints from imagery of varying vintage and releases them under **CDLA Permissive 2.0**. The provisional overall-design bbox falls inside Bing L9 quadkey `132100103`.

Script: `scripts/fetch_microsoft_buildings.py`.

Do **not** treat Microsoft height values or footprints as current official building facts without cross-checking. Imagery vintage can predate 2026 and automated extraction has false positives/omissions.

### 3. Official Beijing / Haidian public sources

Official current project pages remain the preferred source for program status, named road/water projects, public-service nodes, official scope text and public-space operations. These sources can verify attributes or named facilities but often do not supply redistributable GIS.

## Reproducible run

From a networked repository checkout:

```bash
python3 workstreams/evidence_basemap/scripts/fetch_osm_basemap.py
python3 workstreams/evidence_basemap/scripts/fetch_microsoft_buildings.py
python3 workstreams/evidence_basemap/scripts/validate_basemap_outputs.py workstreams/evidence_basemap/data/generated
python3 workstreams/evidence_basemap/scripts/validate_evidence_workstream.py
```

Optional OSM building extraction for cross-check:

```bash
python3 workstreams/evidence_basemap/scripts/fetch_osm_basemap.py --include-buildings
```

## Expected generated structure

```text
workstreams/evidence_basemap/data/generated/
  osm/
    roads.geojson
    rail.geojson
    water.geojson
    green.geojson
    poi.geojson
    buildings_osm.geojson          # optional
    manifest.json
    ODbL-ATTRIBUTION.md
  microsoft/
    buildings.geojson
    LICENSE-NOTE.md
```

Generated data should be reviewed before commit. Large or stale raw extracts should not be committed merely to increase file count.

## Cross-validation rules

1. **Road/rail/water**: OSM geometry may be a base candidate; named project status should be checked against an official source where available.
2. **Buildings**: compare OSM vs Microsoft footprints; disagreements remain conflict records until imagery/field/official evidence resolves them.
3. **POI**: POI proves a location/category clue, not capacity, service quality, opening hours or accessibility unless separately sourced.
4. **Green/public space**: separate actual mapped land cover from planned/under-construction public-space projects.
5. **Official controls**: FAR, height-control, road redline, ownership, heritage control and statutory setbacks remain Unknown unless organizer/authority files support them.

## Promotion thresholds

- `Derived / Estimated`: one open source, algorithmic extraction, geocoding or unconfirmed tag.
- `Verified / Known`: two independent compatible sources, or an authoritative current public source plus geometry check.
- `Official`: only an official/cleared source that actually supports the claim and intended use.

## Environment limitation in this conversation

The current execution container cannot resolve public network hosts, and the GitHub connector does not expose an interactive shell in the repository. Therefore the network-fetch scripts are committed and reviewable but cannot truthfully be reported as having downloaded current OSM/Microsoft payloads in this conversation. Connector-side rule/source checks were completed; the scripts are the executable closure for a networked checkout.
