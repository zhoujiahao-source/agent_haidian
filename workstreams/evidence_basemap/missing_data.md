# Missing Data Register

Unknown is a valid result. The absence of organizer/official geometry is not converted into invented precision.

| id | missing item | status | impact | resolution path | priority |
|---|---|---|---|---|---|
| MD-01 | exact official SITE_BOUNDARY polygon | Unknown | blocks formal spatial scoring and precise area/intersection metrics | organizer-cleared GIS/CAD/PDF boundary + CRS/source/version | P0 |
| MD-02 | exact official KEY_AREA polygons for 3 detailed areas | Unknown | blocks parcel-level detailed siting and exact key-area metrics | organizer-cleared geometry | P0 |
| MD-03 | exact boundaries of Zhongguancun service wing and Xiaoyuehe scenario wing | Unknown | blocks reliable wing resource counts/coverage | official/cleared project geometry or integration decision clearly marked Proposed | P0/P1 |
| MD-04 | approved FAR / building height / density / green ratio / setbacks | Unknown | blocks statutory development-intensity conclusions | approved regulatory planning conditions and relevant official attachments | P0 |
| MD-05 | official road redlines, sections and junction controls | Unknown | blocks engineering-level street redesign and setback claims | municipal/transport official GIS/CAD and survey | P0 |
| MD-06 | parcel/land ownership and implementation rights | Unknown | blocks acquisition/demolition/implementation claims | cadastral/ownership data cleared for use; legal review | P0 |
| MD-07 | complete current building footprints with use/floors/height/age/condition | Unknown/partial | blocks retain-renovate-demolish audit and reliable floor-area baseline | licensed/open building data + field survey + official verification | P1 |
| MD-08 | current 2026 as-built status of full Jing-Zhang Park phase II | Unknown | affects public-space continuity assumptions | official completion/as-built source + site survey | P1 |
| MD-09 | heritage protection GIS and exact control requirements | Unknown | blocks precise landmark/structure placement | competent heritage authority/open official data | P0/P1 |
| MD-10 | complete current road/rail/walking/cycling network with barriers and crossings | Partial | blocks accessibility/connectivity diagnosis | OSM snapshot under ODbL + official transport data + field verification | P1 |
| MD-11 | transit station entrances, barrier-free paths, pedestrian counts and transfer friction | Partial/Unknown | blocks TOD/15-minute access claims | station open data + field audit + counts | P1 |
| MD-12 | public facilities/POI full inventory, capacity, opening hours and accessibility | Partial | blocks service-equity assessment | official facility directories + OSM/POI cross-check + field audit | P1 |
| MD-13 | current park/green-space entrances, usable area and construction status | Partial | blocks true public-space access analysis | park authority data + site survey | P1 |
| MD-14 | Xiaoyuehe/清河 as-built waterfront geometry, construction phase and closures | Partial | affects safe scenario siting | water authority project data + construction/as-built updates + field survey | P1 |
| MD-15 | utilities, drainage, flood, power, telecom, underground infrastructure | Unknown | blocks robotics/edge-compute/energy/municipal feasibility | competent utility/municipal data; likely professional controlled-access workflow | P0/P1 |
| MD-16 | legal fine-grained population/mobility/activity data | Unknown | blocks precise activity heatmaps and vulnerable-group exposure | public statistics / consented survey / privacy-reviewed aggregate data | P1 |
| MD-17 | service-wing institution geocoding and service capacity | Unknown/partial | blocks IP/capital/professional-service coverage map | public institution registry + address verification + interviews | P1 |
| MD-18 | experiment/AI system incident, complaint, human-takeover baseline | Unknown | blocks pre-deployment Urban Adaptation Rate baseline | future public stewardship operational registry; cannot be backfilled as fact | P2 |

## Data that should **not** be “solved” with proxies

- statutory boundary/redline/ownership;
- approved development controls;
- heritage control line;
- underground utility safety;
- individual-level movement or sensitive personal attributes.

## Data that may use disclosed proxies

- broad land-use/function mix from verified POI + building tags;
- pedestrian-access opportunity from public street graph + entrances;
- building height only when a reproducible public tag/remote-sensing method exists and is labelled Derived;
- activity tendency from public facilities/urban form/research, never as an invented individual heatmap.

## Field survey minimum package

1. geo-tagged crossing/entrance audit; 2. barrier-free path audit; 3. building-use/ground-floor interface observation; 4. public-space use time slices; 5. active construction/closure status; 6. service node opening/access conditions; 7. heritage element photo/log with public-location only; 8. conflict notes where web evidence differs from site state.
