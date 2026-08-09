# 京张底图 Live Cross-Validation / Basemap Evidence Audit

- Executed: 2026-08-09T11:29:47.117956Z
- Provisional bbox WGS84: `116.3397,39.939,116.3553,40.0265`
- OSM live: 5532 features; 1898 building polygons.
- Microsoft L9 quadkey: `132100103`; partition found: **False**; buildings clipped to bbox: 0.
- OSM↔Microsoft buildings matched at IoU≥0.25: 0/1898 (0.0%).
- Median OSM best-IoU: 0.000.
- Named OSM anchors: {"大钟寺南小街": 0, "小月河": 12, "京张铁路遗址公园": 0, "大钟寺": 0, "清河": 17}.

## Evidence status
This is a **real live retrieval and cross-check**, but only candidate existing-condition evidence. It does not convert OSM or Microsoft ML footprints into official redlines, statutory controls, ownership, as-built survey, or approved planning data. Use the intersections to prioritize manual/official verification; preserve disagreements instead of silently overwriting one source with another.
