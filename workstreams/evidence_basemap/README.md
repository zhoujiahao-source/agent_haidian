# Evidence & Basemap Workstream

This workstream is owned by WINDOW 1 — Evidence & Basemap Agent. It builds a traceable evidence layer for the Centennial Jing-Zhang AI Innovation Belt without modifying the canonical submission geometry or claiming statutory certainty.

## Repository baseline

- Upstream repository: `open-city-ai/haidian`
- Latest upstream main re-audited at: `e533da38c89c2766aee202b19b9d053057385ef6` (2026-08-08 continuation pass)
- User fork: `zhoujiahao-source/agent_haidian`
- User submission baseline: `submission/zhoujiahao-source/jingzhang-legible-ai-belt` at `796d29a69774f4722fd7b5012505a3f20bb2e35d`
- Work branch: `agent/evidence-basemap`
- Exchange CRS for GeoJSON: EPSG:4326; official area-calculation CRS reference: EPSG:4548, subject to official survey confirmation.

## Evidence rule

Every factual, measured, inferred, assumed, proposed, or unknown item must remain distinguishable. Data classes: Official / Verified / Derived / Assumed / Unknown. Drawing classes: Known / Estimated / Proposed / Unknown.

Official scope areas and textual extents may be cited from the official announcement. Exact official SITE_BOUNDARY / KEY_AREA polygons are still absent from the latest upstream geometry directory; repository provisional geometry may be used only as a provisional constraint for temporary generation, visualization and self-check, never as an official redline or precise statutory area basis.

## Core files

- `audit_log.md` — repository/rule baseline and phase checkpoints.
- `source_inventory.csv` — source provenance, reuse and formal-use status.
- `source_conflicts.md` — conflicts and resolution notes.
- `confidence_framework.md` — uncertainty taxonomy and drawing legend.
- `area_profiles.md` — evidence-backed profiles for the three areas and two wings.
- `global_ai_ecosystem_cases.md` — global cases and transferability analysis.
- `spatial_findings.md` — spatial opportunities/constraints.
- `missing_data.md` — blocking and non-blocking data gaps.
- `field_dictionary.md` — data fields for integration.
- `building_proxy_method.md` — allowed hierarchy for future building facts/proxies.
- `qa_report.md` — connector/source/runtime QA and explicit caveats.
- `handoff.md` — integration handoff.

## Existing-condition GIS acquisition package

- `basemap_acquisition.md` — executable acquisition / cross-validation workflow.
- `data/basemap_config.json` — provisional discovery bbox, CRS, OSM and Microsoft source configuration.
- `scripts/fetch_osm_basemap.py` — ODbL-attributed roads / rail / water / green / POI fetcher; optional OSM buildings.
- `scripts/fetch_microsoft_buildings.py` — Microsoft Global ML Building Footprints candidate extractor; current site is within L9 quadkey `132100103`.
- `scripts/validate_basemap_outputs.py` — GeoJSON/provenance validator for generated outputs.
- `scripts/test_basemap_helpers.py` — network-free bbox/quadkey/query unit test.
- `data/source_registry_promotion_candidate.json` — maintainer-review candidate records; not the project registry.

Generated network data, when available, belongs under `data/generated/` and remains Derived until cross-checked.

## Field / external-dependency package

- `field_audit_protocol.md` — privacy-safe public-space field protocol.
- `data/field_audit_targets.csv` — 15 bounded survey targets.
- `upstream_issue_draft.md` — ready-to-post missing official geometry issue; upstream issue creation was attempted after duplicate search but blocked by integration HTTP 403.

## Validation sequence

From a networked checkout:

```bash
python3 workstreams/evidence_basemap/scripts/test_basemap_helpers.py
python3 workstreams/evidence_basemap/scripts/fetch_osm_basemap.py
python3 workstreams/evidence_basemap/scripts/fetch_microsoft_buildings.py
python3 workstreams/evidence_basemap/scripts/validate_basemap_outputs.py workstreams/evidence_basemap/data/generated
python3 workstreams/evidence_basemap/scripts/validate_evidence_workstream.py
```

The helper logic has been independently exercised in this conversation and returned the expected L9 quadkey `132100103`; live network payload acquisition could not run because the available execution container has no public DNS/network access.

## Non-goals

This branch does not finalize the project name, brand, landmark design, statutory controls, land ownership, exact road redlines, FAR, building heights, demolition decisions, or canonical submission geometry. Those remain outside this Agent's authority.