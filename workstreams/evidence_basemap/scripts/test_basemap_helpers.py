#!/usr/bin/env python3
"""Offline unit tests for basemap acquisition helpers; no network required."""
from __future__ import annotations
from fetch_microsoft_buildings import required_quadkeys
from fetch_osm_basemap import make_query

BBOX=[116.3397,39.938,116.3553,40.0265]

def main():
    qk=required_quadkeys(BBOX,9)
    assert qk=={"132100103"}, f"unexpected L9 quadkeys: {qk}"
    q=make_query(BBOX,False)
    for token in ['way["highway"]','way["railway"]','way["waterway"]','node["amenity"]','out tags geom center qt']:
        assert token in q, f"missing Overpass token: {token}"
    assert 'way["building"]' not in q
    qb=make_query(BBOX,True)
    assert 'way["building"]' in qb
    print("PASS: basemap helper tests; L9 quadkey=132100103; Overpass layer query composition valid")
if __name__=="__main__": main()
