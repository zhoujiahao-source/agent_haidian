#!/usr/bin/env python3
import csv, io, json
from pathlib import Path
from urllib.request import Request, urlopen

URL='https://bfppub.blob.core.windows.net/$web/2026-07-24/dataset-links.csv'
QK='132100103'
OUT=Path('workstreams/evidence_basemap/live_2026-08-09/ms_index_probe.json')
req=Request(URL,headers={'User-Agent':'agent-haidian-basemap-audit/1.0'})
with urlopen(req,timeout=180) as r:
    raw=r.read(); status=r.status
rows=list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
cols=list(rows[0].keys()) if rows else []
def pick(row,*names):
    low={str(k).lower():v for k,v in row.items()}
    for n in names:
        if n.lower() in low:return str(low[n.lower()] or '')
    return ''
def compact(r):
    return {'location':pick(r,'Location','country'),'quadkey':pick(r,'QuadKey','quad_key'),'url':pick(r,'Url','URL')}
exact=[r for r in rows if pick(r,'QuadKey','quad_key')==QK]
china=[r for r in rows if 'china' in pick(r,'Location','country').lower()]
beijing=[r for r in rows if 'beijing' in pick(r,'Location','country').lower()]
prefix=[r for r in rows if pick(r,'QuadKey','quad_key').startswith(QK[:5])]
result={'dataset_links_url':URL,'http_status':status,'row_count':len(rows),'columns':cols,'target_quadkey':QK,'exact_quadkey_count':len(exact),'china_location_row_count':len(china),'beijing_location_row_count':len(beijing),'target_prefix_count':len(prefix),'exact_examples':[compact(r) for r in exact[:5]],'china_examples':[compact(r) for r in china[:5]],'prefix_examples':[compact(r) for r in prefix[:10]],'conclusion':'published_partition_available' if exact else 'no_published_target_partition_in_current_index'}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
