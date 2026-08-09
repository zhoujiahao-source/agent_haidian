# Incremental Upstream Check — 2026-08-08

Status: **workstream audit only; not canonical submission**

## Refs compared

- prior workstream upstream baseline: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff`
- current upstream `main` re-read: `a3c14da8431f6ca63ff2059c90733132c2d4e8eb`
- fork branch before this continuation pass: `eedad9ace4967b7afc9be7fb53554fb2c7cf5402`

## Result

GitHub comparison reports the current upstream is **107 commits ahead** of the prior workstream baseline. The changed-file set is submission content; none of the governance Agent's normative input paths changed in that interval:

- `skills/urban-design-ai-submission/SKILL.md`
- `brief/site-package/design_brief.json`
- `brief/site-package/agent_taskbook.json`
- `brief/site-package/allowed_design_space.json`
- `brief/site-package/sources.json`
- `brief/site-package/ranges/planning_limits.json`
- `brief/site-package/standards/**`
- `brief/site-package/schemas/metrics.schema.json`
- `data/source_registry.json`
- `docs/data-workflow.md`
- `docs/review-rubric.md`
- organizer geometry inputs

The current `SKILL.md` still states that organizer-missing official polygons do not block content scoring or reduce the participant score, while provisional geometry must remain clearly disclosed. The current metrics schema still allows custom metrics under the `metrics` object and retains the required fields/status semantics used by `metric_proposals.json`.

## Governance impact

**No substantive governance redesign is required.** Existing conclusions remain valid. This pass therefore adds implementation contracts and validation support instead of rewriting the protocol.

## Continuing Unknowns

- organizer-issued exact `SITE_BOUNDARY` / `KEY_AREA` polygons;
- statutory FAR/height/density/green-ratio/setback controls not supplied by an authoritative source;
- production operating institution, named role holders, SLAs and retention/access architecture;
- real operating records and measured values for all custom governance metrics.

## Integration instruction

Final Integration must still re-read upstream at its own execution time because the repository is a living task environment. This incremental check only establishes that no relevant rule-path change occurred between the two refs above.
