# Field Dictionary — Evidence Layer Interface

This dictionary defines fields that downstream agents may safely consume. It does not alter canonical schemas.

| field | type | required | meaning / allowed values |
|---|---|---:|---|
| feature_id | string | yes | stable workstream identifier |
| feature_class | string | yes | boundary/building/road/rail/water/green/public_space/facility/poi/research/enterprise/service/heritage/constraint |
| name_zh | string | yes | public/verified Chinese name or explicit placeholder |
| name_en | string/null | no | verified or descriptive English label; not branding |
| area_role | string/null | no | zhongzhiyuan / ai_origin / dazhongsi / zhongguancun_service_wing / xiaoyuehe_scene_wing / corridor / context |
| evidence_class | enum | yes | Official / Verified / Derived / Assumed / Unknown |
| drawing_class | enum | yes | Known / Estimated / Proposed / Unknown |
| confidence | enum | yes | high / medium / low / unknown |
| source_id | string | yes unless Unknown | key in `source_inventory.csv` or upstream approved registry |
| cross_check_source_ids | string[] | no | independent supporting/contradicting source IDs |
| source_url | string/null | no | public URL when applicable |
| publisher | string/null | no | issuing organization |
| retrieved_at | date | yes for web data | YYYY-MM-DD |
| temporal_coverage | string/null | no | date/year/status represented |
| geometry_status | enum | yes | official / verified_physical / provisional_constraint / derived_proxy / none |
| official_boundary | boolean/null | required for boundary | false for all provisional workstream geometry |
| crs | string/null | required when geometry exists | EPSG:4326 for exchange; record original CRS if transformed |
| transformation | string/null | no | reproducible method/script |
| license | string/null | yes for external data | license/reuse statement |
| formal_use_status | enum | yes | yes / background_only / provisional_only / needs_registry_review / no |
| limitations | string | yes | what this feature does **not** prove |
| conflict_ids | string[] | no | references into `source_conflicts.md` |
| notes | string/null | no | integration note |

## Geometry rules

- `geometry_status=official` only after source/version/CRS is verified from authorized official/cleared data.
- OSM-derived physical geometry should be `verified_physical` or `derived_proxy` and include ODbL attribution and snapshot date.
- Repository rough boundaries remain `provisional_constraint`, `official_boundary=false`.
- Proposed scenario nodes must not enter this existing-condition evidence table as `Known`.

## Recommended stable citations

Downstream text should cite `source_id` and, for derived items, `feature_id` + transformation. Example: `Evidence: EB-SF-001 / SRC-BJ-JZPARK-20211216 / Verified / high`.
