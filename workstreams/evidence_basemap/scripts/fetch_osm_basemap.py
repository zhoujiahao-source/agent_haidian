#!/usr/bin/env python3
"""Fetch OSM existing-condition candidate layers through Overpass.

Outputs GeoJSON with explicit provenance. OSM output is bootstrap evidence only;
it is never promoted to official boundary/regulatory control by this script.
Python stdlib only.
"""
from __future__ import annotations
import argparse, datetime as dt, json, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "data/basemap_config.json"

POLYGON_KEYS = {"building","leisure","landuse","natural","amenity"}

def post(endpoint: str, query: str) -> dict:
    data = urllib.parse.urlencode({"data": query}).encode()
    req = urllib.request.Request(endpoint, data=data, headers={"User-Agent":"jingzhang-evidence-basemap/1.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)

def make_query(bbox, include_buildings=False):
    w,s,e,n = bbox
    b = f"{s},{w},{n},{e}"
    parts = [
        f'way["highway"]({b});',
        f'way["railway"]({b});', f'node["railway"~"station|halt|subway_entrance"]({b});',
        f'way["waterway"]({b});', f'way["natural"="water"]({b});', f'relation["natural"="water"]({b});',
        f'way["leisure"~"park|garden|nature_reserve|playground|pitch"]({b});',
        f'relation["leisure"~"park|garden|nature_reserve"]({b});',
        f'way["landuse"~"grass|recreation_ground|forest"]({b});',
        f'node["amenity"]({b});', f'way["amenity"]({b});',
        f'node["healthcare"]({b});', f'way["healthcare"]({b});',
        f'node["historic"]({b});', f'way["historic"]({b});',
        f'node["tourism"]({b});', f'node["public_transport"]({b});'
    ]
    if include_buildings:
        parts.append(f'way["building"]({b});')
    return '[out:json][timeout:120];(' + ''.join(parts) + ');out tags geom center qt;'

def layer_for(tags):
    if "highway" in tags: return "roads"
    if "railway" in tags: return "rail"
    if "waterway" in tags or tags.get("natural") == "water": return "water"
    if "leisure" in tags or tags.get("landuse") in {"grass","recreation_ground","forest"}: return "green"
    if "building" in tags: return "buildings_osm"
    return "poi"

def geometry_for(el):
    typ = el.get("type")
    if typ == "node" and "lat" in el and "lon" in el:
        return {"type":"Point","coordinates":[el["lon"],el["lat"]]}
    geom = el.get("geometry") or []
    if typ == "way" and geom:
        coords = [[p["lon"],p["lat"]] for p in geom]
        tags = el.get("tags",{})
        closed = len(coords) >= 4 and coords[0] == coords[-1]
        if closed and any(k in tags for k in POLYGON_KEYS) and "highway" not in tags and "railway" not in tags and "waterway" not in tags:
            return {"type":"Polygon","coordinates":[coords]}
        return {"type":"LineString","coordinates":coords}
    c = el.get("center")
    if c:
        return {"type":"Point","coordinates":[c["lon"],c["lat"]]}
    return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--include-buildings", action="store_true")
    ap.add_argument("--out", default=str(ROOT/"data/generated/osm"))
    args=ap.parse_args()
    cfg=json.loads(CONFIG.read_text(encoding="utf-8"))
    query=make_query(cfg["bbox_wgs84"], args.include_buildings)
    payload=None; used=None; errors=[]
    for ep in cfg["osm"]["endpoints"]:
        try:
            payload=post(ep,query); used=ep; break
        except Exception as exc:
            errors.append(f"{ep}: {exc}"); time.sleep(2)
    if payload is None:
        raise SystemExit("Overpass failed: " + " | ".join(errors))
    stamp=dt.datetime.now(dt.timezone.utc).isoformat()
    groups={k:[] for k in ["roads","rail","water","green","poi","buildings_osm"]}
    for el in payload.get("elements",[]):
        g=geometry_for(el)
        if not g: continue
        tags=el.get("tags",{})
        lyr=layer_for(tags)
        props={
            "feature_id":f"osm-{el.get('type')}-{el.get('id')}",
            "osm_type":el.get("type"),"osm_id":el.get("id"),"tags":tags,
            "source_id":cfg["osm"]["source_id"],"retrieved_at":stamp,
            "license":"ODbL-1.0","attribution":"© OpenStreetMap contributors",
            "evidence_class":"Derived","drawing_class":"Estimated","confidence":"medium",
            "limitations":"Crowdsourced geometry/tags; currentness and completeness vary; cross-check before promotion to Verified."
        }
        groups[lyr].append({"type":"Feature","geometry":g,"properties":props})
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    manifest={"retrieved_at":stamp,"endpoint":used,"bbox_wgs84":cfg["bbox_wgs84"],"query":query,"counts":{}}
    for lyr, feats in groups.items():
        if not feats: continue
        fc={"type":"FeatureCollection","name":f"jingzhang_{lyr}_osm_candidate","metadata":{"source_id":cfg["osm"]["source_id"],"retrieved_at":stamp,"endpoint":used,"license":"ODbL-1.0","attribution":"© OpenStreetMap contributors","boundary_status":"provisional_clip_extent","official":False},"features":feats}
        (out/f"{lyr}.geojson").write_text(json.dumps(fc,ensure_ascii=False,indent=2),encoding="utf-8")
        manifest["counts"][lyr]=len(feats)
    (out/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    (out/"ODbL-ATTRIBUTION.md").write_text("# OpenStreetMap attribution\n\nContains information from OpenStreetMap, which is made available under the Open Database License (ODbL). © OpenStreetMap contributors.\n",encoding="utf-8")
    print(json.dumps(manifest,ensure_ascii=False,indent=2))
if __name__ == "__main__": main()
