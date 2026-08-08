# Handoff — AI Governance & Metrics Agent

## 1. Repository state

- upstream ref reviewed: `open-city-ai/haidian@b3d6fdaa2331fdc60a3e618019fd8e6596532fff`
- fork base ref: `zhoujiahao-source/agent_haidian@5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1`
- branch: `agent/ai-governance-metrics`
- final commit SHA: use the branch HEAD reported in the final Agent response. A Git commit cannot embed its own final SHA in the file content without changing that SHA; this field therefore intentionally points to the external handoff response as the authoritative final SHA.
- major write scope: `workstreams/ai_governance_metrics/`
- canonical submission modified: **no**

## 2. What I completed

- Audited the latest upstream SKILL/brief/taskbook/design-space/source/standard/schema/data-workflow/review-rubric/geometry state and sampled the user's prior Legible AI Belt proposal/metrics.
- Recorded fork/upstream drift and the unresolved geometry-scoring wording conflict.
- Defined City Agent data/causality boundaries and a strict `eligible_issue` gate so raw model alerts cannot inflate governance metrics.
- Unified Problem Track and Capability Track behind one evidence/risk/public-value gate.
- Defined Low / Medium / High / Not Eligible risk tiers across eight consequence dimensions.
- Created an authorization matrix with human responsibility, review participation, notice/consent expectations, override, stop/rollback and scale restrictions.
- Defined the full Urban Learning Protocol, experiment card, incident/version rules, public-value floors and STOP/MODIFY/CONTINUE/SCALE decision semantics.
- Defined Urban Adaptation Rate with an auditable denominator/numerator, proposed 90-day operational and 365-day durable horizons, confidence/coverage rules and anti-gaming controls.
- Kept Responsible STOP as a separate learning/safety outcome instead of inflating UAR.
- Defined 17 custom AI-city metric candidates; all remain unknown/null until real operating records exist.
- Defined Capability Backbone transfer/revalidation rules, public/professional dashboard architecture, anti-gaming controls and five governance figure briefs.
- Performed workstream-level validation and recorded what was intentionally not run.

## 3. Key decisions / findings

### Finding A — UAR must begin after eligibility, not Agent detection
- evidence: `problem_diagnosis.md`, `urban_adaptation_rate.md`
- confidence: high as a governance-design conclusion
- why it matters: prevents alert volume, duplicate complaints and hallucinated problems from becoming the denominator or an incentive.

### Finding B — Responsible STOP is successful learning but not adaptation
- evidence: `experiment_protocol.md`, `public_value_framework.md`, `urban_adaptation_rate.md`
- confidence: high
- why it matters: avoids an incentive to continue a harmful/low-value pilot merely to protect a deployment-success KPI, while keeping the semantic distinction that the underlying public problem may still be unresolved.

### Finding C — risk authority follows consequence, not model capability
- evidence: `risk_tiers.md`, `authorization_matrix.csv`
- confidence: high
- why it matters: preserves human/public stewardship for safety-, rights- and privacy-consequential action.

### Finding D — SCALE is context-specific
- evidence: `capability_transfer_rules.md`
- confidence: high
- why it matters: Capability Backbone should exchange evidence-bearing capabilities, not auto-deploy a successful source-area system into a materially different target context.

### Finding E — headline UAR should stay legible
- evidence: `urban_adaptation_rate.md`
- confidence: medium-high design recommendation
- why it matters: unweighted headline UAR is easier to audit; severity/equity weighting can be a pre-registered companion with sensitivity analysis rather than an opaque master score.

### Finding F — no operational metric values exist yet
- evidence: `metric_proposals.json`, lack of a real issue/experiment/outcome registry in this workstream
- confidence: high
- why it matters: all proposed metric values must remain `unknown/null`; formula readiness must not be presented as measured city performance.

### Finding G — repository geometry/scoring text is internally inconsistent
- evidence: `audit/rule_audit.md`, latest upstream files reviewed at the ref above
- confidence: high for the audited repository state
- why it matters: Integration must not silently turn provisional geometry into official redlines, but organizer-missing geometry should also not be used to erase content evaluation if the latest SKILL/rubric still says so.

## 4. Files added or modified

| file | purpose | status |
|---|---|---|
| `audit/rule_audit.md` | latest rule/existing-content/geometry/schema audit | complete |
| `audit/checkpoints.md` | phase-by-phase checkpoint and unknown register | complete |
| `problem_diagnosis.md` | City Agent data boundary, causal discipline, eligible issue + dual intake | complete |
| `risk_tiers.md` | eight-dimensional risk tiers and escalation overrides | complete |
| `authorization_matrix.csv` | human authorization/override/rollback/scale matrix | complete |
| `urban_learning_protocol.md` | full lifecycle, states, objects, responsibilities and audit events | complete |
| `experiment_protocol.md` | bounded experiment card, baseline/comparator/monitoring/incident/version rules | complete |
| `public_value_framework.md` | common floors + scenario outcomes + decision gate | complete |
| `urban_adaptation_rate.md` | UAR formula, cohort, horizons, STOP separation, confidence and anti-gaming | complete |
| `anti_gaming.md` | denominator, target, reporting, labour, complaint, transfer and audit gaming controls | complete |
| `custom_metrics_catalog.md` | 17 AI-city metric candidates and readiness states | complete |
| `metric_proposals.json` | current-schema-compatible candidate metric records, all unknown/null | complete |
| `capability_transfer_rules.md` | cross-Learning-Unit revalidation gates | complete |
| `audit_and_dashboard.md` | public layer + professional audit layer + annual release architecture | complete |
| `figure_briefs.md` | five governance/metrics evidence-figure briefs | complete |
| `sources_and_evidence.md` | project + external governance reference register | complete |
| `validation_report.md` | workstream-level structural/governance validation | complete |
| `handoff.md` | Integration Agent handoff | complete |

## 5. Sources and licenses / authority

See `sources_and_evidence.md` for the full register.

Key project sources:
- latest upstream SKILL / design brief / agent taskbook / allowed design space / sources / planning limits / standards / metrics schema / data workflow / review rubric / geometry folder;
- user's historical `submission/zhoujiahao-source/jingzhang-legible-ai-belt` assets.

External cross-checks:
- NIST AI RMF — authoritative U.S. government voluntary guidance; design reference only here.
- OECD AI Principles — intergovernmental principles; design reference.
- EU AI Act (Regulation (EU) 2024/1689) — comparative lifecycle/human-oversight reference; not assumed applicable to this Beijing proposal.
- PRC Personal Information Protection Law — legal reference relevant to future personal-information/automated-decision deployments; actual deployment obligations require fact-specific compliance review.
- GB/T 45392-2025 — current Chinese national recommended standard for security requirements in personal-information automated decision making; implementation benchmark, not planning control.

No third-party dataset or licensed map layer was copied into this workstream.

## 6. Data / design status

### Official
- Repository taskbook/brief language, three positioning statements, five functions and published area-reference text as present in the reviewed upstream sources.
- Competition repository schemas/rules at the recorded upstream ref.

### Verified
- Reviewed upstream/fork refs and file state.
- Official exact `SITE_BOUNDARY` / `KEY_AREA` was not present in the geometry directory at audit time.
- Existing user proposal has reusable L0–L3 legibility/disclosure/evidence-chain assets.

### Derived / Proposed
- Urban Learning Protocol.
- Risk tiers/authorization design.
- UAR definition and all companion/custom metrics.
- Transfer/revalidation, dashboard/audit and anti-gaming protocols.
- Five figure briefs.

### Assumed
- `A-GOV-OPS-001`: the governance metrics are schema-ready design proposals, but there is no adopted live issue/experiment/public-value registry; therefore operational values remain unknown.
- 90-day operational and 365-day durable UAR horizons are proposed defaults, not official competition requirements.
- Exact institutional names, SLAs, pilot duration caps and scenario thresholds will be set by a future Public Steward / operating body.

### Unknown
- exact official SITE_BOUNDARY / KEY_AREA polygons;
- approved FAR/height/density/green ratio/setbacks and other missing statutory controls;
- actual future operating institution, accountable titles, controller/processor roles, staffing/procurement/vendor architecture;
- live values for every custom AI-city metric;
- production dashboard access-control/retention architecture.

## 7. Conflicts or risks

1. **Geometry/scoring wording conflict:** latest SKILL/data-workflow/review-rubric say organizer-missing official geometry should not block/penalize content scoring, while other repository files retain stronger “official geometry required for formal professional scoring” language. Re-read latest state during final integration and preserve provisional/non-statutory disclosure.
2. **Legal applicability risk:** external AI-governance/legal references cannot be converted into generic deployment permission. Every real scenario needs fact-specific privacy/safety/sector review.
3. **Metric institutionalization risk:** a powerful UAR target could itself be gamed. Keep fixed cohorts, intake/rejection ledger, unresolved cases, failures, complaints, manual intervention and independent audit visible.
4. **Composite-index opacity:** `data_minimization_compliance_index` and `vendor_exit_readiness_index` should not be published until component rubrics are adopted and visible.
5. **Automation-authority drift:** High-risk capability maturity must never silently relax the human authorization tier.

## 8. What the Final Integration Agent should adopt

### Must adopt
- UAR eligibility gate and fixed-cohort discipline.
- Meaningful public-value improvement as UAR numerator; AI deployment/activity is not success.
- Responsible STOP reported separately from adaptation credit.
- Common public-value floors and explicit STOP/MODIFY/CONTINUE/SCALE semantics.
- Eight-dimension risk tier + named human responsibility + override/stop/rollback.
- cross-context revalidation before Capability Backbone transfer receives target-area credit.
- unknown/null for all unmeasured governance metrics.
- public dashboard failure/complaint/override/manual intervention visibility and professional audit traceability.
- anti-gaming rules and preserved metric-version history.

### Strong candidate
- UAR-90 + UAR-365 two-horizon reporting, subject to scenario feasibility.
- the 17-metric catalog, selectively added to canonical `metrics.json` without replacing statutory/geometric metrics.
- dashboard information architecture and five governance figure briefs.
- Annual City Version Release delta: new / modified / scaled / stopped-retired / unresolved / metric-audit changes.

### Exploratory only until operationally specified
- numeric pilot duration caps, SLAs and scenario success thresholds;
- data-minimization and vendor-exit composite indices;
- exact institutional role titles and organisational separation model.

## 9. What I intentionally did NOT modify

- canonical `submissions/<login>/<slug>/...` files;
- final canonical `metrics.json`;
- geometry, SITE_BOUNDARY, KEY_AREA or planning-control layers;
- other Agents' workstreams;
- project master naming/Logo decision;
- any official approval, construction scale, property ownership or statutory-control claim.

## 10. Validation performed

- command/check: reviewed latest upstream rule/schema/data/geometry files and user's existing proposal/metrics.
  - result: complete for workstream scope; rule conflict recorded.
- command/check: `metric_proposals.json` structural/schema validation against the reviewed current metrics schema.
  - result: PASS; 17 metric candidates; required fields present; all operational values remain unknown/null.
- command/check: required workstream file inventory.
  - result: PASS after this handoff commit.
- command/check: governance DoD coverage.
  - result: PASS at proposal/specification level; phases 0–9 addressed.
- command/check: canonical participant preflight.
  - result: NOT RUN BY DESIGN; canonical submission is owned by Final Integration Agent.

## Integration sequence

1. Re-read the **latest** upstream `SKILL.md` and repository rules at integration time.
2. Preserve canonical planning/geometric metrics; selectively add the governance metrics that improve judging clarity.
3. If adopting the metric candidates, create/retain assumption `A-GOV-OPS-001` and keep all values `unknown/null` until real records exist.
4. Link scenario/agent content to the experiment/risk/public-value protocol rather than repeating generic AI claims.
5. Turn the five figure briefs into evidence graphics consistent with the Public Service Aesthetic and provisional-geometry disclosure.
6. Re-run the then-current render/finalize/self-check/participant-preflight workflow on the canonical submission.
