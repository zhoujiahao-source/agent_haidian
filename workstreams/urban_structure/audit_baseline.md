# Urban Structure Agent — Audit Baseline

## Status

- Role: `WINDOW 2 — Urban Structure Agent`
- Branch: `agent/urban-structure`
- Upstream repository: `open-city-ai/haidian`
- Upstream ref audited: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff` (2026-08-08)
- User proposal baseline: `796d29a69774f4722fd7b5012505a3f20bb2e35d`
- User proposal branch: `submission/zhoujiahao-source/jingzhang-legible-ai-belt`
- Canonical submission modified by this Agent: **No**

## 1. Latest-rule audit

The latest upstream Skill, `brief/site-package/`, source registry, review rubric and schema directory were re-read before design work. The following rule changes / clarifications materially affect this workstream:

1. `package_type=professional_design_package` describes the artifact, while review state is separate; legacy `submission_stage=formal` is not itself a review decision.
2. Organizer-supplied official polygons are still absent from `brief/site-package/geometry/`. The directory contains only `provisional_boundaries.geojson`, its basis note, and `study_area_bbox.geojson`.
3. Provisional geometry remains acceptable for temporary generation, visualization, non-statutory discussion and intake/self-check, but it must not be described as official redline, ownership, statutory planning control or precise implementation boundary.
4. The latest Skill and review rubric clarify that organizer geometry gaps alone do not block content scoring. This supersedes any stale interpretation that the participant should be penalized merely because official polygons have not yet been supplied.
5. Official project-specific FAR, building height, building density, green ratio and setbacks remain `missing` in `ranges/planning_limits.json`; schema sanity bounds are not approval values.
6. Editable layers remain LAND_USE, PARCEL, BUILDING_FOOTPRINT, ROAD_CENTERLINE, ROAD_AREA, GREEN_SPACE, PUBLIC_SPACE, PHASE, AI_SERVICE_ZONE and SCENARIO_NODE. Locked layers remain SITE_BOUNDARY, EXISTING_PRIMARY_ROAD, EXISTING_RAIL, EXISTING_WATER, HERITAGE_PROTECTION and REGULATORY_CONTROL.

## 2. Existing submission assets audited

### Reusable assets

The old `Jing-Zhang Legible AI Belt` package contains useful spatial and compliance assets that should be upgraded rather than discarded:

- `geometry/roads.geojson`: one conceptual north-south greenway spine (`ROAD-001`) plus five conceptual east-west connectors (`ROAD-002`–`ROAD-006`).
- `geometry/public_space.geojson`: five concept nodes, including three pilgrimage / memory landmarks, one honor node and one low-sensing refuge.
- `geometry/key_areas.geojson`: three explicitly provisional key-area polygons for Zhongzhiyuan, Beijing AI Origin Community and Dazhongsi.
- `geometry/land_use.geojson`: four conceptual longitudinal function bands.
- `geometry/phasing.geojson`: three broad phase polygons.
- `proposal.md`: mature compliance language, legibility / consent logic, a 100-day reversible pilot idea, personas, scenarios and international cases.
- `assumptions.json`: correctly records missing official controls, road data, building facts, heritage GIS, public-space ownership and municipal capacity.

### Assets that should be retained only as sub-principles

- “Legible AI / 可读 AI” is valuable as a governance and interface principle, but should no longer be the master urban concept.
- L0–L3 legibility levels can inform risk/interface design, but should sit beneath the locked City OS / Capability Backbone logic.
- Existing pilgrimage landmarks can be reinterpreted as `Landmark as Memory` rather than technology monuments.

### Assets requiring redesign

1. **Backbone is under-specified spatially.** The old package is essentially one center line + five connectors. It does not yet combine heritage memory, mobility, public space, blue-green ecology, capability nodes and event/operations as six visible layers.
2. **East-west stitching is diagrammatic.** The five east-west lines are conceptual; no current evidence proves that each line is an existing legal crossing, public passage or constructible connection. They must be classified as `must improve / can improve / concept study` only after official road/rail/ownership evidence is available.
3. **North-south continuity is too close to “one greenway”.** Continuity must include sequences of daily services, innovation interfaces, culture, blue-green spaces, markets, neighborhoods and time-based operations.
4. **Node hierarchy is incomplete.** Existing public-space polygons do not define service radius, target users, capability exchange, ambient/consent split, human override, reversibility or risk tier.
5. **Phasing conflates time with land polygons.** The future package should distinguish Permanent Infrastructure, Adaptive Layer and Experimental Layer, then phase each layer rather than assigning the whole site to three coarse time bands.
6. **Land-use bands are too schematic.** They are useful as conceptual functional structure but should not be read as parcel-level land-use change or approved land-use classification.
7. **No detailed section catalogue.** The workstream must add at least a railway/east-west stitch section, Xiaoyuehe public capability interface section, and one key-area section.

## 3. Evidence and certainty register

### Official / formal-ready

- Official text scale: coordinated study area about 43.6 km²; overall design area about 11.4 km²; key detailed design area about 368.4 ha.
- Key-area taskbook reference values: Zhongzhiyuan about 192.1 ha; Beijing AI Origin Community about 104.3 ha; Dazhongsi about 72.0 ha.
- Three fixed positionings: Centennial Jing-Zhang Cultural Belt; Metropolitan AI Life Experience Belt; AI Integrated Innovation Belt.
- Five fixed functions and official Three Areas / Two Wings task roles as recorded in the site package.

### Verified repository state

- No new official `SITE_BOUNDARY` or `KEY_AREA` polygon exists in upstream geometry directory at audited ref.
- Latest source registry still marks the repository boundary dataset `provisional_only`.
- Existing user geometry uses `design_proposal` / `provisional_constraint` semantics rather than claiming approval.

### Derived / design-proposal

- Existing submitted provisional site polygon area: 11,412,825.386 sqm (medium confidence in old metrics; not an official area computation).
- Existing conceptual mobility network length: 15,355.339 m (low confidence; design lines, not surveyed roads).
- Existing green/public-space ratios are design-derived and low confidence; they are not current-condition statutory metrics.

### Assumed / conceptual

- Exact locations and dimensions of future capability nodes.
- Feasibility of individual east-west crossings.
- Reuse potential of particular buildings or parcels.
- Underground infrastructure capacity, fire access and station interfaces.

### Unknown

- Exact official overall and key-area polygons / redlines.
- Unified authoritative base map / survey CRS package.
- Approved FAR, height, density, green-ratio, setbacks and road redlines.
- Parcel ownership and detailed existing building facts.
- Heritage GIS controls, underground utilities, measured mobility demand and verified crossing constraints.

## 4. Spatial design problem statement

The design problem is not to place more AI objects along the Jing-Zhang corridor. It is to build a **city capability exchange system that is physically legible and continuously reachable**: different districts produce, test, exchange, revalidate and retire public capabilities, while public life remains the primary spatial experience.

The core spatial translation for this workstream is:

> `Capability Backbone = continuous public-realm armature + differentiated learning units + a hierarchy of capability interfaces + reversible test spaces + public memory of what the city learned.`

This sentence is the starting point for all subsequent files.

## 5. Phase 0 checkpoint

**Completed:** latest-rule audit; current geometry-directory audit; old proposal / metrics / assumptions / key geometry audit; CI/PR status check.

**Found:** mature reusable compliance assets, but the old spatial structure does not yet meet the new City OS / Capability Exchange Network constitution.

**Unknown:** official polygons, road/rail crossing facts, approved controls, detailed existing conditions.

**Next dependency:** define the six-layer Capability Backbone and map distinct spatial prototypes for Three Areas / Two Wings without inventing statutory facts.
