# Rule & Existing-Content Audit — AI Governance & Metrics

Status: **workstream evidence only; not canonical submission**
Audit date: 2026-08-08
Upstream main inspected: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff`
Fork main base: `5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1`
Branch: `agent/ai-governance-metrics`

## 1. Files inspected

The audit checked the current upstream versions of:

- `skills/urban-design-ai-submission/SKILL.md`
- `brief/site-package/design_brief.json`
- `brief/site-package/agent_taskbook.json`
- `brief/site-package/allowed_design_space.json`
- `brief/site-package/sources.json`
- `brief/site-package/ranges/planning_limits.json`
- `brief/site-package/standards/standards.json`
- `brief/site-package/standards/references/index.json`
- `brief/site-package/visual_style_recommendations.json`
- `brief/site-package/schemas/metrics.schema.json`
- `data/source_registry.json`
- `docs/data-workflow.md`
- `docs/review-rubric.md`
- `brief/site-package/geometry/`
- the user's existing `submission/zhoujiahao-source/jingzhang-legible-ai-belt` proposal and `metrics.json`.

## 2. Rule changes / live-state findings

1. **Upstream is newer than the fork base.** Upstream `main` was `b3d6fdaa2331fdc60a3e618019fd8e6596532fff` while the fork `main` used to create this branch was `5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1`. This workstream therefore treats upstream rules as normative reading context while keeping changes isolated on the writable fork branch.
2. **Official precise geometry is still absent.** `brief/site-package/geometry/` contains provisional boundaries and a study-area bbox, but no organizer-supplied exact `SITE_BOUNDARY` / `KEY_AREA` polygon.
3. **There is a rule-text conflict about geometry and scoring.**
   - `design_brief.json`, `allowed_design_space.json`, and `data/source_registry.json` retain wording that exact official geometry is required for formal professional scoring / that provisional geometry is not usable for formal professional scoring.
   - the latest `SKILL.md`, `docs/data-workflow.md`, and `docs/review-rubric.md` state that organizer-supplied geometry gaps do **not** block content scoring or justify a content-score penalty.
   - **Workstream treatment:** do not resolve this silently. Treat provisional geometry as non-statutory and unusable for precise legal/planning claims; flag the scoring-language conflict for the Integration Agent / maintainers.
4. The latest `metrics.schema.json` permits custom metrics through `additionalProperties` under `metrics`, but every metric still needs `status`, `value`, `unit`, `source_files`, `formula`, `confidence`, and `assumptions`.
5. The existing user proposal already has a mature **Legibility / L0–L3** governance idea and clearly discloses provisional geometry. It does **not** yet contain the complete City OS governance protocol or an operational Urban Adaptation Rate. Its current `metrics.json` mainly reports geometry, counts, and legibility-level metrics.

## 3. Existing assets worth reusing

- Existing proposal's disclosure language around provisional geometry and non-statutory status.
- Existing L0–L3 legibility gradient as a **communication / interface layer**, not as the new master governance logic.
- Existing scenario, persona and landmark structure for future experiment-card attachment.
- Existing evidence-chain idea (`proposal -> figures -> GeoJSON -> metrics -> matrices -> sources/assumptions -> self_check`).

## 4. Required conceptual upgrade

The workstream keeps the locked City OS logic:

`city problem -> diagnosis -> risk authorization -> bounded experiment -> public-value review -> STOP/MODIFY/CONTINUE/SCALE -> capability exchange -> revalidation -> public metrics -> memory / retirement`

Governance must not collapse back into an “Issue -> PR -> Merge” metaphor. “Legible AI” remains useful as a governance/visual sub-principle, while the governing mechanism is **Urban Learning Protocol + Capability Backbone + Public Value + Urban Adaptation Rate**.

## 5. Data / claim status

### Official / verified
- Project name, three positioning statements, five functions, three areas/two wings, and official text/area figures listed in the repository taskbook / official announcement snapshots.
- Current repository rules and schemas at the upstream SHA above.

### Derived
- This workstream's governance framework, risk tiers, formulas, metric definitions, dashboard architecture, transfer tests, anti-gaming controls.

### Assumed
- Pilot owners, SLAs, thresholds and operational time windows are design proposals until adopted by a real public steward.
- A 90-day operational and 365-day durable UAR reporting horizon are proposed standard horizons, not official project requirements.

### Unknown
- Exact official polygons/redlines.
- Approved FAR, building height, building density, green ratio and setbacks.
- Future operating entity, legal controller/processor roles, staffing, procurement and vendor architecture.
- Any actual operational values for the proposed AI-city metrics.

## 6. Checkpoint — Phase 0

Completed: latest-rule audit, geometry status, schema check, existing proposal/metrics review.
Key finding: the current proposal has useful legibility assets but lacks the full learning-and-governance operating protocol required by the new design constitution.
Unknown: official geometry and actual operating governance institution.
Next dependency: define City Agent diagnosis boundaries and eligibility gate without inventing operational data.
