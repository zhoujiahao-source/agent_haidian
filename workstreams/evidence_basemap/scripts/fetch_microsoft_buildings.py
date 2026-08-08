#!/usr/bin/env python3
"""Fetch Microsoft Global ML Building Footprints tile(s) intersecting the study bbox.

The output is a candidate existing-building layer only. It preserves Microsoft
provenance and CDLA-Permissive-2.0 licensing, and labels every feature Derived.
Python stdlib only.
"""
from __future__ import annotations
import argparse, csv, datetime as dt, gzip, io, json, math, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CONFIG=ROOT/"data/basemap_config.json"

def tile_xy(lat,lon,z):
    n=1<<z
    x=int((lon+180.0)/360.0*n)
    lat=max(min(lat,85.05112878),-85.05112878)
    y=int((1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*n)
    return x,y

def quadkey(x,y,z):
    out=[]
    for i in range(z,0,-1):
        d=0; m=1<<(i-1)
        if x&m: d+=1
        if y&m: d+=2
        out.append(str(d))
    return ''.join(out)

def required_quadkeys(bbox,z):
    w,s,e,n=bbox
    x0,y0=tile_xy(n,w,z); x1,y1=tile_xy(s,e,z)
    return {quadkey(x,y,z) for x in range(min(x0,x1),max(x0,x1)+1) for y in range(min(y0,y1),max(y0,y1)+1)}

def geom_bbox(g):
    xs=[]; ys=[]
    def walk(v):
        if isinstance(v,list) and len(v)>=2 and all(isinstance(q,(int,float)) for q in v[:2]): xs.append(v[0]); ys.append(v[1])
        elif isinstance(v,list):
            for q in v: walk(q)
    walk(g.get("coordinates",[]))
    return (min(xs),min(ys),max(xs),max(ys)) if xs else None

def intersects(a,b):
    return not (a[2]<b[0] or a[0]>b[2] or a[3]<b[1] or a[1]>b[3])

def open_text(url):
    req=urllib.request.Request(url,headers={"User-Agent":"jingzhang-evidence-basemap/1.0"})
    return urllib.request.urlopen(req,timeout=180)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",default=str(ROOT/"data/generated/microsoft")); args=ap.parse_args()
    cfg=json.loads(CONFIG.read_text(encoding="utf-8")); mc=cfg["microsoft_buildings"]
    bbox=tuple(cfg["bbox_wgs84"]); qks=required_quadkeys(bbox,int(mc["lod"]))
    with open_text(mc["dataset_links_url"]) as r:
        text=io.TextIOWrapper(r,encoding="utf-8-sig")
        rows=list(csv.DictReader(text))
    selected=[r for r in rows if r.get("Location")==mc["location"] and r.get("QuadKey") in qks]
    if not selected:
        raise SystemExit(f"No dataset link found for {mc['location']} quadkeys={sorted(qks)}")
    stamp=dt.datetime.now(dt.timezone.utc).isoformat(); feats=[]; tile_meta=[]
    for row in selected:
        url=row["Url"]; count=0
        with open_text(url) as resp:
            gz=gzip.GzipFile(fileobj=resp)
            for raw in gz:
                if not raw.strip(): continue
                obj=json.loads(raw)
                g=obj.get("geometry")
                if not g: continue
                gb=geom_bbox(g)
                if not gb or not intersects(gb,bbox): continue
                props={k:v for k,v in obj.items() if k!="geometry"}
                props.update({
                    "source_id":mc["source_id"],"retrieved_at":stamp,"license":mc["license"],
                    "source_quadkey":row.get("QuadKey"),"evidence_class":"Derived","drawing_class":"Estimated",
                    "confidence_class":"medium",
                    "limitations":"ML-derived footprint; imagery vintage varies and may predate current site conditions. Cross-check with OSM/official/field evidence before Verified use."
                })
                feats.append({"type":"Feature","geometry":g,"properties":props}); count+=1
        tile_meta.append({"quadkey":row.get("QuadKey"),"url":url,"selected_feature_count":count})
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    fc={"type":"FeatureCollection","name":"jingzhang_microsoft_buildings_candidate","metadata":{"source_id":mc["source_id"],"retrieved_at":stamp,"license":mc["license"],"bbox_wgs84":bbox,"official":False,"evidence_class":"Derived","tile_meta":tile_meta},"features":feats}
    (out/"buildings.geojson").write_text(json.dumps(fc,ensure_ascii=False,indent=2),encoding="utf-8")
    (out/"LICENSE-NOTE.md").write_text("# License note\n\nBuilding footprints are sourced from Microsoft Global ML Building Footprints and licensed under CDLA Permissive 2.0. They are model-derived candidate geometry, not official survey footprints.\n",encoding="utf-8")
    print(json.dumps({"retrieved_at":stamp,"quadkeys":sorted(qks),"features":len(feats)},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
