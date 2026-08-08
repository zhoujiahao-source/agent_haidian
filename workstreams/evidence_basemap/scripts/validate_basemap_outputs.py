#!/usr/bin/env python3
"""Validate generated basemap GeoJSON provenance and minimum geometry quality."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

REQUIRED_PROPS={"source_id","retrieved_at","evidence_class","drawing_class","limitations"}
ALLOWED_GEOM={"Point","LineString","Polygon","MultiPoint","MultiLineString","MultiPolygon"}

def walk_coords(v):
    if isinstance(v,list) and len(v)>=2 and all(isinstance(q,(int,float)) for q in v[:2]):
        yield v[:2]
    elif isinstance(v,list):
        for q in v: yield from walk_coords(q)

def validate_file(path:Path):
    errs=[]
    try: obj=json.loads(path.read_text(encoding="utf-8"))
    except Exception as e: return [f"{path}: invalid JSON: {e}"],0
    if obj.get("type")!="FeatureCollection": errs.append(f"{path}: not FeatureCollection")
    feats=obj.get("features",[])
    seen=set()
    for i,f in enumerate(feats,1):
        if f.get("type")!="Feature": errs.append(f"{path} feature {i}: not Feature"); continue
        g=f.get("geometry")
        if not g or g.get("type") not in ALLOWED_GEOM: errs.append(f"{path} feature {i}: invalid geometry")
        else:
            for x,y in walk_coords(g.get("coordinates",[])):
                if not (math.isfinite(x) and math.isfinite(y) and -180<=x<=180 and -90<=y<=90): errs.append(f"{path} feature {i}: invalid coordinate {x},{y}"); break
        p=f.get("properties") or {}
        miss=REQUIRED_PROPS-set(p)
        if miss: errs.append(f"{path} feature {i}: missing properties {sorted(miss)}")
        fid=p.get("feature_id") or p.get("id") or f.get("id")
        if fid:
            if fid in seen: errs.append(f"{path}: duplicate feature id {fid}")
            seen.add(fid)
        if p.get("source_id")=="SRC-REG-PROVISIONAL-BOUNDARY" and str(p.get("official_boundary",False)).lower() not in {"false","0","none"}:
            errs.append(f"{path} feature {i}: provisional geometry marked official")
    return errs,len(feats)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("paths",nargs="*",default=["workstreams/evidence_basemap/data/generated"]); args=ap.parse_args()
    files=[]
    for raw in args.paths:
        p=Path(raw)
        if p.is_dir(): files += sorted(p.rglob("*.geojson"))
        elif p.suffix.lower()==".geojson": files.append(p)
    if not files: raise SystemExit("NO DATA: no GeoJSON outputs found")
    errors=[]; total=0
    for f in files:
        e,n=validate_file(f); errors+=e; total+=n
    if errors:
        print("FAIL")
        for e in errors: print("-",e)
        raise SystemExit(1)
    print(f"PASS: {len(files)} GeoJSON files, {total} features")
if __name__=="__main__": main()
