#!/usr/bin/env python3
from pathlib import Path
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('submission_dir')
args=parser.parse_args()
root=Path(args.submission_dir)

zh=root/'proposal.md'
text=zh.read_text(encoding='utf-8')
old='[source:SOURCE-REGISTRY] [source:OFFICIAL-ANNOUNCEMENT] [source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]'
new='[source:SOURCE-REGISTRY] [source:OFFICIAL-ANNOUNCEMENT]\n\n外部开放底图的许可、获取和未完成 materialization 则由两条独立来源记录承担，不与官方规划事实混为一类。[source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]'
if old in text:
    text=text.replace(old,new)
zh.write_text(text,encoding='utf-8')

en=root/'proposal.en.md'
text=en.read_text(encoding='utf-8')
old='[source:SOURCE-REGISTRY] [source:OFFICIAL-ANNOUNCEMENT] [source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]'
new='[source:SOURCE-REGISTRY] [source:OFFICIAL-ANNOUNCEMENT]\n\nThe licence, acquisition path and still-unmaterialized status of external open basemap candidates are documented separately from official planning facts. [source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]'
if old in text:
    text=text.replace(old,new)
en.write_text(text,encoding='utf-8')
print('evidence markers normalized')
