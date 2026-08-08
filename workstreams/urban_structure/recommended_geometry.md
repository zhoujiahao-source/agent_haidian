# Recommended Geometry — Integration Guidance

## Status and authority

This workstream does **not** modify canonical submission geometry. Files under `geometry_candidates/` are integration candidates only. They inherit the uncertainty of the existing proposal and the repository's provisional boundary package.

The Final Integration Agent should treat the following hierarchy as authoritative:

1. future organizer-supplied official geometry, if/when added;
2. latest verified / cleared existing-condition data;
3. candidate design geometry in this workstream;
4. old schematic proposal geometry retained only where it still helps explain intent.

## 1. Locked layers — do not replace here

- `SITE_BOUNDARY`: keep repository/user submission provisional status until official polygon is supplied. Never reinterpret it as official redline.
- `KEY_AREA`: keep current provisional role until official key-area polygons are supplied.
- `EXISTING_PRIMARY_ROAD`, `EXISTING_RAIL`, `EXISTING_WATER`, `HERITAGE_PROTECTION`, `REGULATORY_CONTROL`: this Agent has not created replacements because verified authoritative geometry is absent.

## 2. ROAD_CENTERLINE recommendation

### Existing `ROAD-001`

**Recommendation:** retain as a **candidate north-south continuity study axis**, not a confirmed greenway alignment.

Integration action:

- preserve its coordinates only as a design-study reference;
- rename / attribute it as `candidate_continuity_axis`;
- do not count its length as existing transport infrastructure;
- once verified route/rail/road data is available, snap/rebuild the line to real accessible public routes rather than preserving the schematic geometry for visual continuity.

Candidate file: `geometry_candidates/backbone_lines.geojson#US-BB-001`.

### Existing `ROAD-002`–`ROAD-006`

**Recommendation:** retain only as **Class C / concept-study east-west axes** until each receives a crossing evidence card.

Do not draw them as bridges, tunnels, official streets or guaranteed passages. Candidate file: `geometry_candidates/stitch_study_axes.geojson`.

## 3. SCENARIO_NODE / PUBLIC_SPACE recommendation

The old public-space polygons are useful as conceptual anchors but their footprints are not evidence-backed. For integration, convert them first to **point anchors** that express a desired node relationship without implying land take or approved footprint.

Candidate point anchors:

- `US-N-DZS-01`: Dazhongsi market/service learning node, derived from old `PUBLIC-003` center.
- `US-N-MEM-01`: central memory / retirement node, derived from old `PUBLIC-004` center.
- `US-N-BG-01`: blue-green / sensor-light interface candidate, derived from old `PUBLIC-005` center; relation to Xiaoyuehe must still be verified.
- `US-N-ORIGIN-01`: AI Origin neighborhood learning + memory interface, derived from old `PUBLIC-001` center.
- `US-N-ZZY-01`: Zhongzhiyuan verification + memory interface, derived from old `PUBLIC-002` center.

Candidate file: `geometry_candidates/capability_nodes.geojson`.

The point anchor is **not** a final node footprint. Final node polygons/building hosts should only be created after ownership, building, public-space, fire, accessibility, heritage and operating conditions are verified.

## 4. LAND_USE recommendation

The old four longitudinal `LAND_USE` polygons are visually useful as an early functional diagram but are too schematic to function as final parcel-level planning geometry.

Recommended integration treatment:

- preserve their **capability/function narrative** as a diagrammatic background only;
- do not present them as approved land-use changes;
- do not use their areas to infer statutory land-use proportions;
- when verified parcel/current-land-use data becomes available, rebuild the final `land_use.geojson` from real parcel/current-condition geometry and clearly separate Existing / Proposed / Unknown.

The more important final structure is not four stripes, but the relationship between the Capability Backbone and the five differentiated learning units.

## 5. PUBLIC_SPACE / GREEN_SPACE recommendation

Do not copy old conceptual polygons forward merely to make spatial ratios look complete.

Final integration should:

1. establish verified existing public/green-space base layers where possible;
2. add Proposed improvements only where a host is plausible;
3. tag new design components by `implementation_layer = permanent | adaptive | experimental`;
4. retain sensor-light / analog refuge space as a required program principle without inventing a parcel before evidence exists.

## 6. PHASE recommendation

The old submission uses three large phase polygons. Those polygons imply a geographic certainty that the design does not yet have.

**Recommended replacement:** phase **components**, not broad site bands.

Suggested feature attributes for future canonical design layers:

- `implementation_layer`: `permanent | adaptive | experimental`
- `delivery_phase`: `evidence_no_regret | adaptive_network | selective_permanent | continuous_pilot`
- `reversibility`: `low | medium | high`
- `evidence_status`: `Official | Verified | Derived | Assumed | Unknown`
- `drawing_status`: `Known | Estimated | Proposed | Unknown`
- `host_verification_required`: boolean
- `risk_tier`: project-specific value after governance review
- `human_override_required`: boolean where relevant

This makes phasing auditable even when exact site geometry changes.

## 7. Geometry changes by canonical file

| Canonical file | Current useful asset | Recommended Final Integration action | Current certainty |
|---|---|---|---|
| `site_boundary.geojson` | repository provisional overall polygon | keep provisional until official replacement | provisional-only |
| `key_areas.geojson` | three provisional polygons | keep role labels; replace coordinates when official arrives | provisional-only |
| `roads.geojson` | ROAD-001 + five cross axes | reinterpret as study geometry; rebuild on verified routes | Proposed / low-medium |
| `land_use.geojson` | four conceptual function bands | use narrative only; rebuild from verified current/parcel data | Proposed / low |
| `buildings.geojson` | conceptual envelopes | do not infer retain/demolish/new-build without survey | Proposed / low |
| `green_space.geojson` | conceptual green structure | rebuild on verified existing landscape/water | Proposed / low |
| `public_space.geojson` | five conceptual landmark/public-space polygons | convert first to point anchors; later choose evidence-backed hosts | Proposed / low-medium |
| `phasing.geojson` | three broad time polygons | replace with component-level phase/layer attributes | Proposed / low |

## 8. Candidate geometry rules

Every candidate in this workstream follows these rules:

- EPSG:4326 exchange coordinates.
- `geometry_role=design_proposal`.
- No candidate is official, statutory or an ownership boundary.
- Geometry reused from the old user submission records its source feature.
- Candidate lines remain study geometry until snapped/rebuilt against verified existing-condition data.
- Candidate node points represent **relationships**, not construction footprints.

## 9. Phase 8 geometry conclusion

The spatial proposal is now integrable without overclaiming certainty: one candidate Backbone axis, five evidence-gated stitch study axes and five node anchors can be carried into final graphics, while official/locked layers remain untouched and the old schematic land-use/phasing geometry is explicitly demoted from “answer” to “working diagram”.
