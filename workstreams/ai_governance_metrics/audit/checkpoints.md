# Phase Checkpoints — AI Governance & Metrics

Status: **design/research workstream complete; machine-readable operating contracts added; live implementation and measured values remain future work**
Latest upstream re-check: `a3c14da8431f6ca63ff2059c90733132c2d4e8eb`

| phase | completed | key finding / output | remaining Unknown / Assumed | integration dependency |
|---|---|---|---|---|
| 0 — rule & existing-content audit | yes | upstream rules audited; fork/upstream drift and geometry-scoring wording tension recorded; continuation compare found no relevant rule-path changes | exact official SITE_BOUNDARY / KEY_AREA remain unavailable to this workstream | Integration Agent should re-read latest SKILL before canonical edits |
| 1 — problem diagnosis | yes | City Agent is diagnostic/proposal actor; raw alerts/correlations cannot enter the UAR denominator; `eligible_issue.schema.json` now defines the machine-readable intake object | production data catalogue and controller/operator roles | operational data governance |
| 2 — dual entry | yes | Problem Track and Capability Track share one evidence/risk/public-value gate; capability novelty cannot manufacture demand | actual intake institution and service owners | Public Steward operating model |
| 3 — risk tiers | yes | Low/Medium/High/Not Eligible defined across safety, rights/equity, privacy, scale, reversibility, autonomy, detectability and lock-in | exact legal applicability is use-case/jurisdiction specific | specialist/legal review for deployed cases |
| 4 — authorization | yes | human approval owner, participants, notice/consent expectations, override, stop/rollback and scale rules defined per tier | exact department titles and numeric maximum durations are not official | adopting institution must register owners/SLAs |
| 5 — experiment design | yes | baseline, falsifiable hypothesis, comparator, bounded scope, monitoring, stop conditions, incident logging, rollback and versioning defined; `experiment_card.schema.json` makes the minimum record implementable | scenario-specific thresholds/targets remain future registrations | scenario owners must predeclare targets before pilot |
| 6 — public value review | yes | common floors + scenario outcomes; STOP/MODIFY/CONTINUE/SCALE semantics defined; average-only success prohibited | scenario-specific meaningful-change thresholds/weights | scenario evidence and affected-group review |
| 7 — Urban Adaptation Rate | yes | auditable eligible-issue denominator and adapted-issue numerator defined; Responsible STOP kept out of adaptation numerator; proposed 90d/365d horizons; 17 metric candidates remain unknown/null | no live eligible-issue cohort; 90/365 horizons are proposals | future issue/experiment/public-value registry |
| 8 — capability transfer | yes | cross-area transfer requires target baseline, re-tiering, local authorization and bounded revalidation; `capability_record.schema.json` requires `transfer_requires_revalidation=true` | target-area data and operating institutions | Capability Backbone implementation |
| 9 — dashboard & audit | yes | public layer + professional audit layer + annual release/correction rules defined; `dashboard_data_contract.json` and `city_version_release.schema.json` make the disclosure/version interfaces explicit | production dashboard platform, access controls and retention schedule | digital product / governance operations |

## Implementation-readiness checkpoint

Added in the continuation pass:

- `schemas/eligible_issue.schema.json`
- `schemas/experiment_card.schema.json`
- `schemas/capability_record.schema.json`
- `schemas/city_version_release.schema.json`
- `dashboard_data_contract.json`
- `integration_crosswalk.md`
- `validate_workstream.py`

These are **proposed interface contracts**, not evidence that a production governance platform exists.

## Overall checkpoint

The requested governance logic is complete at proposal/specification/interface level:

`diagnosis -> eligibility -> risk -> human authorization -> bounded experiment -> public-value review -> STOP/MODIFY/CONTINUE/SCALE -> transfer/revalidation or retirement -> audit/learning -> annual version release`.

No file in this workstream claims that the protocol is already adopted by government or that any custom AI-city metric has a measured operational value.
