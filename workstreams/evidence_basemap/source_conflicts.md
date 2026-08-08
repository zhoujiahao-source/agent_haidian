# Source Conflicts & Reconciliation Log

This file preserves conflicting or differently scoped evidence. A conflict is not resolved by majority vote; authority and fitness for the claim control the decision.

## C-01 — 43.6 km² / 11.4 km² / 368.4 ha vs “about 37 km²”

- **Evidence A (Official/formal-ready):** official competition announcement and `design_brief.json` define coordinated research area ≈43.6 km², overall design area ≈11.4 km², detailed key area ≈368.4 ha.
- **Evidence B (Verified background):** Beijing science/technology reporting describes a north-south-east-west-center “三区两翼” industrial layout of about 37 km².
- **Decision:** keep both as different scopes. Never use 37 km² as the competition overall-design polygon or area. Never use the 11.4 km² competition scope as proof of the full industrial network extent.
- **Integration impact:** every map/table must name the scope explicitly.

## C-02 — AI Origin Community “about 3 km²” vs 104.3 ha key area

- **Evidence A:** public Haidian program material describes an AI Origin Community / surrounding innovation ecosystem of about 3 km² and gives broad directional bounds.
- **Evidence B:** competition task package gives the key detailed-design reference area as 104.3 ha, with exact polygon still missing.
- **Decision:** treat 3 km² as a broader operational/innovation-community context, not the key-area geometry. Treat 104.3 ha as official reference area only, not a polygon.
- **Integration impact:** universities/talent/enterprise statistics tied to the 3 km² context must not be spatially clipped or attributed to the 104.3 ha area without new evidence.

## C-03 — “学北园AI自主创新加速区” wording vs “众智园AI自主创新加速区”

- **Evidence A:** April 2026 public reporting uses “北部学北园AI自主创新加速区” in one narrative and identifies 学北园 as a major northern anchor.
- **Evidence B:** cleared taskbook/competition materials use “众智园AI自主创新加速区”; July 2026 Beijing Urban Renewal Service Platform also names the update area “众智园AI自主创新加速区” and lists 众智园、腾讯学知园、东升三期604 as anchors.
- **Decision:** use **众智园AI自主创新加速区** as the workstream/competition area name. Treat 学北园/学知园 as an anchor asset, not a substitute area name.

## C-04 — Urban-renewal project extents vs competition key areas

- **Evidence:** July 2026 urban-renewal pages provide textual boundaries for the 众智园 and 大钟寺 update areas. Competition package gives reference areas 192.1 ha and 72.0 ha but no official polygons.
- **Decision:** the renewal extents are **Verified current program extents**, not competition `KEY_AREA` polygons. Do not convert their textual boundaries into official competition geometry.
- **Integration impact:** they can guide field survey/source discovery and contextual diagrams, but cannot overwrite canonical `key_areas.geojson`.

## C-05 — Jing-Zhang Park phase-II schedule vs current 2026 built condition

- **Evidence:** 2024 official reporting stated phase II had started/was planned for construction with a 2025 target. The same sources verify the intended 9 km, about 70 ha corridor and the already-open phase I.
- **Gap:** this evidence pass did not obtain an authoritative as-built 2026 completion survey for the entire corridor.
- **Decision:** mark 9 km corridor as verified planning/public-space framework; mark **full 2026 phase-II completion status Unknown** until an up-to-date official completion source or site survey is obtained.

## C-06 — Publicity statistics vs spatially attributable inventory

- District/innovation-community pages publish counts for enterprises, scientists, developers, students, patents and industry scale.
- These are useful ecosystem indicators but are not a geocoded feature inventory and may use different statistical boundaries and dates.
- **Decision:** preserve them as contextual Verified statistics only with scope/date labels. Do not fabricate heat maps or allocate counts to parcels/buildings.

## C-07 — OSM/public imagery vs statutory geometry

- OSM and public imagery may be useful to check current physical roads/buildings/green space if license and date are recorded.
- They cannot establish legal property, road redline, heritage-control line, approved land-use control or official boundary.
- **Decision:** keep statutory attributes separate from physical geometry. Any OSM-derived layer remains Verified/Derived physical evidence with ODbL attribution, never Official planning control.

## C-08 — Existing “Legible AI Belt” proposal vs new locked City OS constitution

- The existing submission is a reusable prior asset and includes useful sources/global cases.
- The new 36 locked decisions elevate the long-term logic to City OS / Capability Backbone / Urban Capability Exchange Network.
- **Decision:** this evidence workstream does not rename or redesign the proposal. It supplies evidence compatible with the new constitution and flags old conceptual language for Integration Agent review.
