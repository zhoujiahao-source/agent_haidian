# Audit Baseline — Public Space & Landmarks

Date: 2026-08-08
Role: WINDOW 4 — Public Space & Landmark Agent
Branch: `agent/public-space-landmarks`
Canonical submission modified: **No**

## Repository refs checked

- Upstream: `open-city-ai/haidian` main @ `b3d6fdaa2331fdc60a3e618019fd8e6596532fff` (latest observed at start of work).
- Fork: `zhoujiahao-source/agent_haidian` main @ `5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1`.
- Historical candidate branch audited: `submission/zhoujiahao-source/jingzhang-legible-ai-belt` @ `796d29a69774f4722fd7b5012505a3f20bb2e35d`.

## Required rules / evidence read

1. Latest upstream `skills/urban-design-ai-submission/SKILL.md`.
2. `brief/site-package/design_brief.json`.
3. `brief/site-package/agent_taskbook.json`, with emphasis on agent.3 / agent.4 / agent.5 / agent.6.
4. `brief/site-package/allowed_design_space.json`.
5. `brief/site-package/ranges/planning_limits.json`.
6. `brief/site-package/visual_style_recommendations.json`.
7. `data/source_registry.json`.
8. `docs/review-rubric.md`.
9. `brief/site-package/geometry/` directory status.
10. Historical `proposal.md` and `geometry/public_space.geojson` from the user's prior formal candidate.

## Rule changes / current state that affect this workstream

- Upstream is ahead of the fork at the start of this work. This workstream therefore records the upstream rule reference explicitly and does **not** claim the fork main is the latest ruleset.
- Current upstream geometry directory contains only `provisional_boundaries.geojson`, its basis note, and `study_area_bbox.geojson`. No cleared official `SITE_BOUNDARY` / `KEY_AREA` polygon was observed. All exact landmark placement and area statements therefore remain **Proposed / Assumed**, not official.
- The current Skill distinguishes artifact type (`professional_design_package`) from review status; this workstream does not alter package state and does not claim formal review readiness.
- `agent.4` requires: Jing-Zhang heritage park AI public space, east-west stitching / north-south continuity, Dazhongsi AI-native consumption/business scenarios, >=3 landmarks, honor display system, and a public-space component library.
- `agent.3` requires >=10 scenario cards, >=3 testing/validation scenarios, >=5 personas, scene-space-operation mapping, privacy and human-review boundaries.
- `agent.5` requires a Jing-Zhang railway + Zhongguancun + AI cultural narrative, spatial cultural system, signage/symbol direction, and international communication.
- The public source registry permits provisional geometry only for temporary generation / visualization / design discussion and explicitly prohibits treating it as official redline, statutory control, precise area basis, or implementation basis.

## Historical asset audit

The prior `Jing-Zhang Legible AI Belt` candidate contains reusable mechanisms:

- 7 personas.
- 12 scenario cards, including 4 testing/validation scenarios.
- Explicit non-AI alternatives, human review and shutdown language for higher-risk scenes.
- Five public-space features: AI Mile Zero, Open Source Century Station, Legibility Observatory, Contributor Scale Wall, Sensor-Light Garden.
- A useful `L0–L3` legibility / autonomy gradient and AI-service disclosure concept.

These are **assets, not the new constitution**. The current design constitution upgrades the main logic to: City OS → public value → continuous city learning → Capability Backbone → Public Capability Interface → Landmark as Memory → Annual City Version Release → Retired Capability Archive → Urban Capability Exchange Network.

## External public evidence checked for the 1909 / park narrative

- Beijing Municipal Commission of Planning and Natural Resources / historic-city-protection case material: records 1909 completion and opening of the Beijing–Zhangjiakou Railway and describes it as the first state trunk railway designed and built independently by Chinese engineers; use as high-confidence historical background, not as a parcel-level heritage-control source.
- Beijing Municipal Forestry and Parks Bureau: Jing-Zhang Railway Heritage Park Phase I (Qinghuadong Road–Zhichun Road) was completed/opened in 2023; official description emphasizes protection/recovery of railway remains, old tracks, switches, rolling stock elements, Qinghuayuan station, public life and east-west stitching.
- Beijing municipal / Haidian public information: later park planning continues a north-south linear public-space strategy and east-west stitching; exact future project status must be rechecked at integration time.

## Status taxonomy

- **Official**: taskbook positioning / functions / textual scope and published area values; 1909 completion fact from official public-history sources.
- **Verified**: current repository file/rule status; prior branch content; Phase I park public-space facts from Beijing government sources.
- **Derived**: this workstream's spatial/programmatic synthesis and capability-node relationships.
- **Assumed**: exact node location, footprint, route, technical capacity, staffing model, costs and operating hours unless separately verified.
- **Unknown**: official exact site/key-area polygons; parcel ownership; detailed heritage GIS; statutory FAR/height/density/green ratio/setbacks; utilities; underground constraints; current footfall/thermal/accessibility counts.

## Phase 0 checkpoint

Completed: latest-rule audit, taskbook audit, geometry-status check, historical asset audit, initial public-history verification.

Found: prior scenario/persona work is worth reusing, but the old landmark system is too centered on 'legibility/display' and lacks the required 1909→2026→Future learning-memory structure and retirement logic.

Unknown: exact legal/heritage boundaries and definitive node sites.

Next dependency: design a node family that works independent of exact parcel geometry, then orchestrate personas/scenarios and the three-time landmark network.