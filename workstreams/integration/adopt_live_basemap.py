#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('submission_dir')
    parser.add_argument('evidence_dir')
    args = parser.parse_args()
    root = Path(args.submission_dir).resolve()
    evidence = Path(args.evidence_dir).resolve()
    summary = json.loads((evidence / 'crosscheck_summary.json').read_text(encoding='utf-8'))
    probe = json.loads((evidence / 'ms_index_probe.json').read_text(encoding='utf-8'))

    osm = summary['osm']
    ms = summary['microsoft']
    cross = summary['building_crosscheck']

    if summary.get('status') != 'live_executed' or osm.get('http_status') != 200 or probe.get('http_status') != 200:
        raise SystemExit('live evidence is incomplete; refuse canonical adoption')

    sources_path = root / 'sources.json'
    sources = json.loads(sources_path.read_text(encoding='utf-8'))
    by_id = {s.get('id'): s for s in sources.get('sources', []) if isinstance(s, dict)}

    osm_src = by_id.get('SRC-OSM-OVERPASS-LIVE')
    if not osm_src:
        raise SystemExit('missing SRC-OSM-OVERPASS-LIVE')
    osm_src['retrieved_date'] = '2026-08-09'
    osm_src['usage'] = (
        f"Live Overpass candidate existing-condition audit within the provisional envelope: "
        f"{osm.get('feature_count')} usable OSM features including {osm.get('building_polygon_count')} building polygons; "
        "used for context and named-anchor cross-checks, not as statutory survey evidence."
    )
    osm_src['limitation'] = (
        "Community-maintained OSM data are candidate context only; they do not establish official redlines, ownership, "
        "complete as-built inventory, statutory controls, or guaranteed current conditions. Re-run after organizer geometry arrives."
    )

    ms_src = by_id.get('SRC-MS-GLOBAL-BUILDINGS-20260724')
    if not ms_src:
        raise SystemExit('missing SRC-MS-GLOBAL-BUILDINGS-20260724')
    ms_src['retrieved_date'] = '2026-08-09'
    ms_src['usage'] = (
        f"Live query of Microsoft 2026-07-24 dataset-links.csv for project L9 quadkey {ms.get('l9_quadkey')}; "
        f"index HTTP {probe.get('http_status')}, {probe.get('row_count')} rows, exact target partitions {probe.get('exact_quadkey_count')}, "
        f"China rows {probe.get('china_location_row_count')}."
    )
    ms_src['limitation'] = (
        "The current published Microsoft index contains no target/China partition for this site, so no Microsoft building footprints "
        "were available for site-level OSM↔Microsoft IoU comparison. This is a coverage result, not evidence that buildings are absent."
    )
    sources_path.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    zh_path = root / 'proposal.md'
    zh = zh_path.read_text(encoding='utf-8')
    zh_old = 'OSM 与 Microsoft Global ML Building Footprints 已登记许可与交叉验证工作流，但本次执行环境尚未完成 live materialization，因此它们没有被伪装成 Verified 现状底图。'
    zh_new = (
        f"OSM 已于 2026-08-09 通过 Overpass 完成 live materialization：provisional envelope 内取得 {osm.get('feature_count')} 个可用 features，"
        f"其中 {osm.get('building_polygon_count')} 个建筑面；它们仅晋级为候选现状证据，不晋级为官方测绘或法定边界。"
        f"Microsoft 2026-07-24 的公开分区索引也已真实查询（HTTP {probe.get('http_status')}，{probe.get('row_count')} 行），"
        f"但目标 L9 quadkey `{ms.get('l9_quadkey')}` 精确分区为 {probe.get('exact_quadkey_count')}、China 行为 {probe.get('china_location_row_count')}，"
        "因此当前没有可用于本场地的 Microsoft 建筑分区，不能制造 OSM↔Microsoft 建筑吻合率。"
    )
    if zh_old not in zh and 'OSM 已于 2026-08-09 通过 Overpass 完成 live materialization' not in zh:
        raise SystemExit('expected Chinese basemap status sentence not found')
    zh = zh.replace(zh_old, zh_new)
    zh_old2 = '外部开放底图的许可、获取和未完成 materialization 则由两条独立来源记录承担，不与官方规划事实混为一类。[source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]'
    zh_new2 = (
        f"外部开放底图的 live 审计结果单独记录：OSM 的 {osm.get('feature_count')} 个 features / {osm.get('building_polygon_count')} 个建筑面已落盘，"
        f"Microsoft 当前索引对 `{ms.get('l9_quadkey')}` 无发布分区；这两类结果都只用于验证队列和设计语境，不与官方规划事实混为一类。"
        '[source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]'
    )
    if zh_old2 in zh:
        zh = zh.replace(zh_old2, zh_new2)
    zh_path.write_text(zh, encoding='utf-8')

    en_path = root / 'proposal.en.md'
    en = en_path.read_text(encoding='utf-8')
    en_old = 'OSM and Microsoft Global ML Building Footprints have licence records and a triangulation workflow, but live materialization has not been completed in this execution environment, so they are not presented as Verified existing conditions.'
    en_new = (
        f"OSM was live-materialized through Overpass on 2026-08-09: {osm.get('feature_count')} usable features inside the provisional envelope, "
        f"including {osm.get('building_polygon_count')} building polygons. They are promoted only to candidate existing-condition evidence, never to official survey or statutory geometry. "
        f"The Microsoft 2026-07-24 published partition index was also queried live (HTTP {probe.get('http_status')}, {probe.get('row_count')} rows), "
        f"but it contains {probe.get('exact_quadkey_count')} exact partition for target L9 quadkey `{ms.get('l9_quadkey')}` and {probe.get('china_location_row_count')} China rows; "
        "therefore no site Microsoft building partition is currently available and no OSM↔Microsoft building match rate is manufactured."
    )
    if en_old not in en and 'OSM was live-materialized through Overpass on 2026-08-09' not in en:
        raise SystemExit('expected English basemap status sentence not found')
    en = en.replace(en_old, en_new)
    en_old2 = 'The licence, acquisition path and still-unmaterialized status of external open basemap candidates are documented separately from official planning facts. [source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]'
    en_new2 = (
        f"The live open-basemap audit is recorded separately: {osm.get('feature_count')} OSM features / {osm.get('building_polygon_count')} building polygons were materialized, "
        f"while the current Microsoft index publishes no partition for `{ms.get('l9_quadkey')}`. Both results remain evidence for verification queues and design context, not official planning facts. "
        '[source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]'
    )
    if en_old2 in en:
        en = en.replace(en_old2, en_new2)
    en_path.write_text(en, encoding='utf-8')

    print(json.dumps({
        'adopted': True,
        'osm_feature_count': osm.get('feature_count'),
        'osm_buildings': osm.get('building_polygon_count'),
        'microsoft_target_partition_count': probe.get('exact_quadkey_count'),
        'microsoft_china_rows': probe.get('china_location_row_count'),
        'crosscheck_note': 'No Microsoft partition available; no fabricated IoU metric.'
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
