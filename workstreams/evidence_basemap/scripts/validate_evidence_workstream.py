#!/usr/bin/env python3
"""Deterministic QA for workstreams/evidence_basemap using Python stdlib only."""
from __future__ import annotations
import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "audit_log.md", "source_inventory.csv", "source_conflicts.md",
    "confidence_framework.md", "area_profiles.md", "global_ai_ecosystem_cases.md",
    "spatial_findings.md", "missing_data.md", "field_dictionary.md", "handoff.md",
    "building_proxy_method.md", "qa_report.md", "basemap_acquisition.md",
    "field_audit_protocol.md", "upstream_issue_draft.md",
    "data/area_reference_values.csv", "data/spatial_evidence_register.csv",
    "data/basemap_config.json", "data/field_audit_targets.csv",
    "data/source_registry_promotion_candidate.json",
    "scripts/fetch_osm_basemap.py", "scripts/fetch_microsoft_buildings.py",
    "scripts/validate_basemap_outputs.py", "scripts/test_basemap_helpers.py",
]
MAPS = [
    "maps/01_existing_structure_evidence.svg",
    "maps/02_mobility_breaks.svg",
    "maps/03_blue_green_public_space.svg",
    "maps/04_innovation_service_resources.svg",
    "maps/05_three_areas_two_wings_profiles.svg",
    "maps/06_confidence_status.svg",
]
SOURCE_REQUIRED = {"source_id","topic","publisher","title","source_url","retrieved_at","license","formal_use_status","confidence_class","limitations"}
SPATIAL_REQUIRED = {"feature_id","feature_class","name_zh","evidence_class","drawing_class","confidence","source_id","geometry_status","limitations"}
ALLOWED_EVIDENCE = {"Official","Verified","Derived","Assumed","Unknown"}
ALLOWED_DRAWING = {"Known","Estimated","Proposed","Unknown"}


def read_csv(rel: str):
    path = ROOT / rel
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED + MAPS:
        p = ROOT / rel
        if not p.is_file() or p.stat().st_size == 0:
            errors.append(f"missing/empty: {rel}")

    src = read_csv("source_inventory.csv")
    if src:
        missing = SOURCE_REQUIRED - set(src[0])
        if missing: errors.append(f"source_inventory missing columns: {sorted(missing)}")
        ids = [r.get("source_id","") for r in src]
        if len(ids) != len(set(ids)): errors.append("duplicate source_id in source_inventory.csv")
        for i,r in enumerate(src,2):
            if not r.get("source_id"): errors.append(f"source row {i}: blank source_id")
            if not r.get("limitations"): errors.append(f"source row {i}: blank limitations")

    spatial = read_csv("data/spatial_evidence_register.csv")
    if spatial:
        missing = SPATIAL_REQUIRED - set(spatial[0])
        if missing: errors.append(f"spatial register missing columns: {sorted(missing)}")
        ids = [r.get("feature_id","") for r in spatial]
        if len(ids) != len(set(ids)): errors.append("duplicate feature_id")
        for i,r in enumerate(spatial,2):
            if r.get("evidence_class") not in ALLOWED_EVIDENCE:
                errors.append(f"spatial row {i}: invalid evidence_class {r.get('evidence_class')!r}")
            if r.get("drawing_class") not in ALLOWED_DRAWING:
                errors.append(f"spatial row {i}: invalid drawing_class {r.get('drawing_class')!r}")
            if r.get("geometry_status") == "provisional_constraint" and r.get("official_boundary","").strip().lower() != "false":
                errors.append(f"spatial row {i}: provisional geometry must official_boundary=false")

    areas = read_csv("data/area_reference_values.csv")
    expected = {"coordinated_research_area","overall_design_area","key_detailed_design_area","zhongzhiyuan_key_area","ai_origin_key_area","dazhongsi_key_area"}
    got = {r.get("metric_id") for r in areas}
    if not expected <= got: errors.append(f"area reference values missing {sorted(expected-got)}")

    field = read_csv("data/field_audit_targets.csv")
    if len(field) < 15:
        errors.append(f"field_audit_targets expected >=15 records, got {len(field)}")
    if any(r.get("status") != "pending_field" for r in field):
        errors.append("field audit targets must remain pending_field until real observation exists")

    try:
        cfg=json.loads((ROOT/"data/basemap_config.json").read_text(encoding="utf-8"))
        if cfg.get("official_boundary") is not False: errors.append("basemap_config official_boundary must be false")
        if cfg.get("boundary_status") != "provisional_constraint": errors.append("basemap_config boundary_status must be provisional_constraint")
        bbox=cfg.get("bbox_wgs84")
        if not isinstance(bbox,list) or len(bbox)!=4: errors.append("basemap_config bbox_wgs84 invalid")
        qks=cfg.get("microsoft_buildings",{}).get("quadkeys",[])
        if "132100103" not in qks: errors.append("basemap_config missing expected Microsoft L9 quadkey 132100103")
    except Exception as exc:
        errors.append(f"basemap_config invalid JSON: {exc}")

    try:
        cand=json.loads((ROOT/"data/source_registry_promotion_candidate.json").read_text(encoding="utf-8"))
        if cand.get("status") != "candidate_only_not_project_registry": errors.append("source promotion file must remain candidate_only")
        if len(cand.get("candidates",[])) < 8: errors.append("source promotion candidate list unexpectedly small")
    except Exception as exc:
        errors.append(f"source_registry_promotion_candidate invalid JSON: {exc}")

    for rel in MAPS:
        text = (ROOT/rel).read_text(encoding="utf-8")
        if "<svg" not in text or "</svg>" not in text: errors.append(f"invalid SVG wrapper: {rel}")

    if errors:
        print("FAIL")
        for e in errors: print("-", e)
        return 1
    print(f"PASS: {len(src)} sources, {len(spatial)} spatial evidence records, {len(field)} field targets, {len(MAPS)} evidence maps")
    return 0

if __name__ == "__main__":
    sys.exit(main())
