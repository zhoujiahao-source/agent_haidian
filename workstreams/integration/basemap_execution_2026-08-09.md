# Basemap Acquisition Execution Status

The Evidence Agent's `fetch_osm_basemap.py`, `fetch_microsoft_buildings.py`, helper tests, source-promotion rules and field-audit queue are adopted as the canonical evidence workflow.

## Attempt in this execution environment
- direct Git/HTTP access from the container: DNS unavailable;
- OSM API live materialization: not possible without network access;
- Microsoft Global ML Building Footprints live tile retrieval: not possible without network access.

No un-downloaded feature is presented as Verified. The canonical package therefore improves the proposed spatial geometry and evidence disclosure while keeping existing-condition basemap promotion pending.

## Required networked command sequence
```bash
python3 workstreams/evidence_basemap/scripts/test_basemap_helpers.py
python3 workstreams/evidence_basemap/scripts/fetch_osm_basemap.py
python3 workstreams/evidence_basemap/scripts/fetch_microsoft_buildings.py
python3 workstreams/evidence_basemap/scripts/validate_basemap_outputs.py workstreams/evidence_basemap/data/generated
python3 workstreams/evidence_basemap/scripts/validate_evidence_workstream.py
```

Promotion requires OSM/Microsoft disagreement review plus official/public/field cross-check; download success alone never equals Verified or Official.
