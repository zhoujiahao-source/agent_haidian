# Upstream issue draft — official geometry / existing-condition GIS gap

## Attempt status

On 2026-08-08 this Agent searched open issues in `open-city-ai/haidian` for `official boundary`, `SITE_BOUNDARY`, `KEY_AREA geometry missing` and found no matching open issue. It then attempted to create the issue through the connected GitHub integration, but GitHub returned HTTP 403 `Resource not accessible by integration`.

This file preserves the exact actionable issue so a maintainer/human with issue-write permission can post it without redoing the research.

## Proposed title

`Data gap: official SITE_BOUNDARY / KEY_AREA polygons and current existing-condition GIS still unavailable`

## Proposed body

### Scope
Evidence & Basemap work for the Centennial Jing-Zhang AI Innovation Belt open call.

### Current upstream state checked
- upstream main checked at `e533da38c89c2766aee202b19b9d053057385ef6` on 2026-08-08;
- `brief/site-package/geometry/` contains only `provisional_boundaries.geojson`, `provisional_boundaries_basis.md`, and `study_area_bbox.geojson`;
- latest Skill still requires trusted official `SITE_BOUNDARY` / `KEY_AREA` when available;
- public official searches found text extents and current program/update evidence, but no cleared coordinate-bearing GIS/CAD boundary file.

### Why this matters
Participants can use provisional geometry for intake and visualization but cannot responsibly calculate statutory-precision areas, parcel-level controls, or conflate competition KEY_AREA boundaries with broader public program/urban-renewal extents. The same gap prevents the existing-condition basemap from being clipped to an authoritative competition polygon.

### Requested next step
If organizer-cleared files exist, please add or point participants to:
1. official/cleared `SITE_BOUNDARY` polygon;
2. official/cleared three `KEY_AREA` polygons;
3. CRS / survey datum and version date;
4. if available, redistributable current roads / rail / water / heritage-control layers.

Until then preserve:
- `official_boundary=false`;
- `geometry_role=provisional_constraint`;
- `boundary_precision=provisional_rough`;
- statutory controls and exact area-derived metrics as Unknown.

### Reproducibility note
Checked latest upstream files and public official sources on 2026-08-08. No private/commercial map source was used.
