#!/usr/bin/env python3
from __future__ import annotations

import csv, gzip, io, json, math, os, statistics
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

from shapely.geometry import shape, mapping, box, Polygon, LineString, Point
from shapely.strtree import STRtree
from shapely.ops import transform
from pyproj import Transformer

BBOX=(116.3397,39.9390,116.3553,40.0265) # west,south,east,north; provisional overall-design envelope
OUT=Path(os.environ.get('JZ_BASEMAP_OUT','workstreams/evidence_basemap/live_2026-08-09'))
OUT.mkdir(parents=True,exist_ok=True)
OVERPASS='https://overpass-api.de/api/interpreter'
MS_LINKS='https://bfppub.blob.core.windows.net/$web/2026-07-24/dataset-links.csv'
UA='agent-haidian-basemap-audit/1.0 (open-city-ai urban design evidence audit)'

def get(url, data=None, timeout=180):
    req=Request(url,data=data,headers={'User-Agent':UA})
    with urlopen(req,timeout=timeout) as r:
        return r.read(), dict(r.headers), r.status

def tile_xy(lat,lon,z=9):
    n=2**z; lat_rad=math.radians(lat)
    return int((lon+180)/360*n), int((1-math.asinh(math.tan(lat_rad))/math.pi)/2*n)

def quadkey(x,y,z=9):
    out=''
    for i in range(z,0,-1):
        mask=1<<(i-1); d=0
        if x&mask:d+=1
        if y&mask:d+=2
        out+=str(d)
    return out

def fc(features,name):
    return {'type':'FeatureCollection','name':name,'features':features}

def save_geojson(path,features,name):
    path.write_text(json.dumps(fc(features,name),ensure_ascii=False,separators=(',',':')),encoding='utf-8')

def osm_to_feature(el):
    geom=el.get('geometry') or []
    tags=el.get('tags',{})
    if el.get('type')=='node':
        if 'lat' not in el or 'lon' not in el:return None
        g=Point(el['lon'],el['lat'])
    elif len(geom)>=2:
        coords=[(p['lon'],p['lat']) for p in geom]
        if coords[0]==coords[-1] and len(coords)>=4:g=Polygon(coords)
        else:g=LineString(coords)
    else:return None
    return {'type':'Feature','id':f"osm-{el.get('type')}-{el.get('id')}",'properties':{'source_type':'osm','osm_type':el.get('type'),'osm_id':el.get('id'),**tags},'geometry':mapping(g)}

def main():
    west,south,east,north=BBOX
    now=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    # OSM live extraction
    q=f'''[out:json][timeout:120];(
      way["building"]({south},{west},{north},{east});
      way["highway"]({south},{west},{north},{east});
      way["railway"]({south},{west},{north},{east});
      way["waterway"]({south},{west},{north},{east});
      way["natural"="water"]({south},{west},{north},{east});
      nwr["amenity"]({south},{west},{north},{east});
      nwr["leisure"]({south},{west},{north},{east});
    );out geom tags;'''
    raw,headers,status=get(OVERPASS,q.encode('utf-8'))
    osm=json.loads(raw)
    osm_features=[f for f in (osm_to_feature(e) for e in osm.get('elements',[])) if f]
    osm_buildings=[f for f in osm_features if f['properties'].get('building') and f['geometry']['type']=='Polygon']
    osm_context=[f for f in osm_features if f not in osm_buildings]
    save_geojson(OUT/'osm_buildings.geojson',osm_buildings,'osm_live_buildings')
    save_geojson(OUT/'osm_context.geojson',osm_context,'osm_live_context')

    # Microsoft latest published L9 partition for project bbox.
    cx,cy=tile_xy((south+north)/2,(west+east)/2,9); qk=quadkey(cx,cy,9)
    links_bytes,_,links_status=get(MS_LINKS)
    text=links_bytes.decode('utf-8-sig')
    rows=list(csv.DictReader(io.StringIO(text)))
    # Be tolerant to column-name changes.
    def pick(row,*names):
        low={k.lower():v for k,v in row.items()}
        for n in names:
            if n.lower() in low:return low[n.lower()]
        return ''
    matches=[]
    for r in rows:
        rq=pick(r,'QuadKey','quadkey','quad_key')
        loc=pick(r,'Location','location','country')
        if rq==qk or (rq.endswith(qk) and len(rq)>=len(qk)):
            matches.append(r)
    # Exact quadkey is preferred. If duplicate vintages exist, use the last row in current link table.
    exact=[r for r in matches if pick(r,'QuadKey','quadkey','quad_key')==qk]
    selected=(exact or matches)[-1] if (exact or matches) else None
    ms_features=[]; ms_url=None; ms_location=None; ms_bytes=0
    if selected:
        ms_url=pick(selected,'Url','url','URL')
        ms_location=pick(selected,'Location','location','country')
        if ms_url:
            req=Request(ms_url,headers={'User-Agent':UA})
            with urlopen(req,timeout=300) as resp:
                compressed=resp.read(); ms_bytes=len(compressed)
            with gzip.GzipFile(fileobj=io.BytesIO(compressed)) as gz:
                clip=box(*BBOX)
                for line in gz:
                    try: obj=json.loads(line)
                    except Exception: continue
                    try: g=shape(obj.get('geometry'))
                    except Exception: continue
                    if g.is_empty or not g.intersects(clip):continue
                    props=obj.get('properties') or {}
                    ms_features.append({'type':'Feature','properties':{'source_type':'agent_inferred_from_public_data','source_dataset':'Microsoft Global ML Building Footprints','source_quadkey':qk,'source_location':ms_location,**props},'geometry':mapping(g.intersection(clip))})
    save_geojson(OUT/'microsoft_buildings.geojson',ms_features,'microsoft_live_buildings')

    # Building concordance in UTM 50N. IoU>=0.25 is a cross-check match, not an official validation threshold.
    project=Transformer.from_crs('EPSG:4326','EPSG:32650',always_xy=True).transform
    osmg=[transform(project,shape(f['geometry'])) for f in osm_buildings]
    msg=[transform(project,shape(f['geometry'])) for f in ms_features]
    ious=[]; matched=0
    if msg:
        tree=STRtree(msg)
        for g in osmg:
            best=0.0
            for j in tree.query(g):
                h=msg[int(j)]
                inter=g.intersection(h).area
                union=g.union(h).area
                if union>0: best=max(best,inter/union)
            ious.append(best)
            if best>=0.25:matched+=1
    osm_area=sum(g.area for g in osmg)
    ms_area=sum(g.area for g in msg)

    # Named-anchor cross-check from official public references already in canonical sources.
    names=['大钟寺南小街','小月河','京张铁路遗址公园','大钟寺','清河']
    name_hits={n:[] for n in names}
    for f in osm_features:
        p=f['properties']; vals=' '.join(str(p.get(k,'')) for k in ('name','name:zh','alt_name','official_name'))
        for n in names:
            if n in vals:name_hits[n].append(f['id'])

    summary={
      'generated_at':now,'bbox_wgs84':{'west':west,'south':south,'east':east,'north':north},
      'status':'live_executed','promotion_rule':'candidate evidence only; never official redline/statutory survey without independent authority',
      'osm':{'endpoint':OVERPASS,'http_status':status,'license':'ODbL-1.0','element_count':len(osm.get('elements',[])),'feature_count':len(osm_features),'building_polygon_count':len(osm_buildings),'context_feature_count':len(osm_context)},
      'microsoft':{'dataset_links_url':MS_LINKS,'dataset_links_http_status':links_status,'license':'CDLA-Permissive-2.0','l9_quadkey':qk,'partition_found':bool(selected),'location':ms_location,'partition_url':ms_url,'downloaded_compressed_bytes':ms_bytes,'building_polygon_count_in_bbox':len(ms_features)},
      'building_crosscheck':{'method':'max polygon IoU in EPSG:32650; match if IoU>=0.25','osm_buildings_compared':len(osmg),'microsoft_buildings_compared':len(msg),'matched_osm_buildings':matched,'osm_match_rate':(matched/len(osmg) if osmg else None),'median_best_iou':(statistics.median(ious) if ious else None),'osm_total_footprint_area_sqm':osm_area,'microsoft_total_footprint_area_sqm':ms_area},
      'official_named_anchor_check':name_hits,
      'limitations':['competition SITE_BOUNDARY / KEY_AREA remain provisional','OSM is community-maintained and not a statutory survey','Microsoft footprints are ML-derived from imagery and may be stale/false-positive/false-negative','named-anchor absence in OSM is not evidence of real-world absence','candidate data are clipped to the provisional envelope and must be re-run when organizer geometry arrives']
    }
    (OUT/'crosscheck_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    report=f'''# 京张底图 Live Cross-Validation / Basemap Evidence Audit\n\n- Executed: {now}\n- Provisional bbox WGS84: `{west},{south},{east},{north}`\n- OSM live: {len(osm_features)} features; {len(osm_buildings)} building polygons.\n- Microsoft L9 quadkey: `{qk}`; partition found: **{bool(selected)}**; buildings clipped to bbox: {len(ms_features)}.\n- OSM↔Microsoft buildings matched at IoU≥0.25: {matched}/{len(osmg)} ({(matched/len(osmg)*100 if osmg else 0):.1f}%).\n- Median OSM best-IoU: {(statistics.median(ious) if ious else 0):.3f}.\n- Named OSM anchors: {json.dumps({k:len(v) for k,v in name_hits.items()},ensure_ascii=False)}.\n\n## Evidence status\nThis is a **real live retrieval and cross-check**, but only candidate existing-condition evidence. It does not convert OSM or Microsoft ML footprints into official redlines, statutory controls, ownership, as-built survey, or approved planning data. Use the intersections to prioritize manual/official verification; preserve disagreements instead of silently overwriting one source with another.\n'''
    (OUT/'crosscheck_report.md').write_text(report,encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
