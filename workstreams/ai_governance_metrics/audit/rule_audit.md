# Rule & Existing-Content Audit — AI Governance & Metrics

Status: **workstream evidence only; not canonical submission**
Audit date: 2026-08-08
Original upstream baseline: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff`
Latest upstream re-check: `a3c14da8431f6ca63ff2059c90733132c2d4e8eb`
Fork main base: `5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1`
Branch: `agent/ai-governance-metrics`

## 1. Files inspected

The audit checked the upstream versions of:

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

A continuation pass then compared the original upstream baseline with `a3c14da8431f6ca63ff2059c90733132c2d4e8eb`. That interval is 107 commits ahead, but the changed files are submission content rather than the rule/schema/data-workflow inputs above. See `audit/upstream_increment_2026-08-08.md`.

## 2. Rule / live-state findings

1. **Upstream is newer than the fork base.** The writable workstream remains on the user's fork, while upstream rules are treated as the normative reading context.
2. **No relevant rule-path change occurred during the continuation interval.** The current SKILL and metrics schema preserve the semantics used by this workstream.
3. **Official precise geometry is still not established by this workstream.** No organizer-supplied exact `SITE_BOUNDARY` / `KEY_AREA` polygon has been promoted into this Agent's facts. Provisional geometry must stay non-statutory.
4. **There is a repository wording tension about geometry and scoring.**
   - some brief/data wording retains stronger language around official geometry and formal professional scoring;
   - the current `SKILL.md`, data-workflow and review-rubric treatment states that organizer-supplied geometry gaps do not block content scoring or justify a score penalty;
   - workstream treatment: do not silently turn provisional geometry into official redlines and do not use missing organizer geometry as a reason to erase content evaluation.
5. **Custom metrics remain schema-compatible.** `metrics.schema.json` allows custom metric IDs under `metrics`, while each metric still requires `status`, `value`, `unit`, `source_files`, `formula`, `confidence`, and `assumptions`; `unknown` requires `value:null` plus a reason.
6. The existing user proposal has reusable **Legibility / L0–L3** governance and disclosure assets, but it does not by itself provide the complete City OS learning protocol, risk authorization model or operational UAR registry.

## 3. Existing assets worth reusing

- disclosure language around provisional geometry and non-statutory status;
- L0–L3 legibility as a communication/interface layer, not the master governance logic;
- scenario, persona and landmark structure for experiment-card attachment;
- evidence chain linking proposal, figures, GeoJSON, metrics, matrices, sources/assumptions and self-check.

## 4. Required conceptual upgrade

The workstream keeps the locked City OS logic:

`city problem -> diagnosis -> eligibility -> risk authorization -> bounded experiment -> public-value review -> STOP/MODIFY/CONTINUE/SCALE -> capability exchange -> target-context revalidation -> public metrics -> memory / retirement`

Governance must not collapse into an `Issue -> PR -> Merge` master metaphor. “Legible AI” remains useful as a governance/visual sub-principle while the governing mechanism is **Urban Learning Protocol + Capability Backbone + Public Value + Urban Adaptation Rate**.

## 5. Data / claim status

### Official / Verified
- project taskbook/brief language, the three fixed positioning statements, five functions and area-reference text as present in the reviewed repository sources;
- repository rules and metrics schema at the refs recorded above.

### Derived / Proposed
- governance framework, risk tiers, formulas, metric definitions, dashboard architecture, transfer tests, anti-gaming controls;
- governance object schemas and dashboard data contract added by this continuation pass.

### Assumed
- pilot owners, SLAs, thresholds and operational time windows are design proposals until adopted by a real Public Steward;
- 90-day operational and 365-day durable UAR reporting horizons are proposed defaults, not official competition requirements.

### Unknown
- exact official polygons/redlines;
- approved FAR, building height, building density, green ratio and setbacks;
- future operating entity, legal controller/processor roles, staffing, procurement and vendor architecture;
- any actual operational values for the proposed AI-city metrics.

## 6. Phase 0 checkpoint

Completed: rule audit, geometry status, metrics-schema check, existing proposal/metrics review and incremental upstream re-check.
Key finding: the rule inputs relevant to this Agent did not change between the two upstream refs, so the completed governance model remains valid.
Unknown: official geometry and actual operating governance institution.
Next dependency: Final Integration should adopt selectively, then run the then-current canonical submission pipeline.
