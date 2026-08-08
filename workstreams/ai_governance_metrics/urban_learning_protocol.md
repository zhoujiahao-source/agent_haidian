# Urban Learning Protocol｜城市学习协议

> Status: governance design proposal for integration. It is **not** a claim of adopted government procedure.

## 1. Purpose

The Urban Learning Protocol turns “a city that learns” into an auditable operating loop. The city does not learn because it deploys more AI. It learns when a verified public problem is diagnosed, a bounded intervention is lawfully authorised, evidence is collected, public value is reviewed, and the result is either improved, modified, stopped, scaled, transferred for revalidation, or retired with a public record.

The protocol is the governance layer of the City OS concept and works with the spatial **Capability Backbone** and area-level **Learning Units**.

## 2. Canonical lifecycle

`DIAGNOSE → ELIGIBILITY → RISK → AUTHORIZE → EXPERIMENT → EVALUATE → STOP / MODIFY / CONTINUE / SCALE → TRANSFER / RETIRE → AUDIT → LEARN`

No step may be skipped merely because a model is technically mature or commercially available.

## 3. Governance objects

### Issue Record
A reproducible record of a public problem candidate. It stores evidence, uncertainty, affected population/space, baseline, public-value relevance, human owner and risk pre-screen.

### Capability Record
A service, spatial mechanism, organisational process, technical module or combination that may address one or more eligible issues. It stores intended users/non-users, data requirements, autonomy, dependencies, failure modes, maintenance and retirement path.

### Experiment Record
A bounded test connecting one or more eligible issues to one capability version, one authorisation decision, predeclared measures, stop conditions and rollback.

### Decision Record
A signed, dated public-value decision: `STOP`, `MODIFY`, `CONTINUE`, or `SCALE`. It records evidence considered, minority/uncertain findings, human decision owner and next review date.

### Capability Release Record
A versioned capability that has passed the required review for a defined context. `SCALE` is context-specific; it does not imply universal portability.

### Retirement Record
A record of why a capability was withdrawn, what value it produced, which harms/limitations were observed, what replaced it, what data/configuration must be retained for audit, and which dependencies must be decommissioned.

## 4. State model

1. `OBSERVED` — a pattern or complaint exists but is not yet an eligible issue.
2. `ELIGIBLE_ISSUE` — evidence and governance intake requirements are met.
3. `RISK_SCREENED` — risk tier and required reviewers are recorded.
4. `AUTHORIZED_FOR_TEST` — the authorised experiment scope/version/expiry is fixed.
5. `EXPERIMENT_ACTIVE` — monitoring, notice, override and incident logging are live.
6. `EVIDENCE_REVIEW` — primary outcomes, guardrails, subgroups, complaints and incidents are reviewed.
7. One of:
   - `STOPPED`
   - `MODIFY_REQUIRED`
   - `CONTINUING`
   - `SCALE_APPROVED`
8. If scaled: `CAPABILITY_ACTIVE` for the specified context/version.
9. If moved to another Learning Unit: `TRANSFER_REVIEW → REVALIDATING`.
10. When no longer justified or supported: `RETIRED`.

Every state transition requires `who`, `when`, `why`, `evidence_ref`, `version`, and `next_action`.

## 5. Human accountability

Minimum accountable roles:

- **problem_owner** — confirms that a candidate problem is real, material and appropriately framed;
- **authorization_owner** — accepts responsibility for permitting a bounded experiment;
- **experiment_owner** — runs the approved test and monitoring plan;
- **incident_owner** — has immediate authority to invoke safe stop/rollback;
- **public_value_review_owner** — signs the STOP/MODIFY/CONTINUE/SCALE decision;
- **maintenance_owner** — owns the operational capability after SCALE;
- **retirement_owner** — owns decommissioning, archive and continuity.

For High-risk experiments, authorisation, operation and independent review should not collapse into one person/team where practical. A City Agent may recommend but cannot replace these accountable roles.

## 6. Two entry tracks, one governance gate

### Problem Track
Begins with a verified public need. The City Agent may help discover evidence and formulate hypotheses. Only accepted `eligible_issue` records proceed.

### Capability Track
Begins with a proposed technical/organisational capability. It must identify the public problem it addresses, non-AI comparator, risks, data, human owner, maintenance and exit path. A technology proposal cannot manufacture its own demand signal.

Both tracks converge before authorisation at the same public-value, evidence and risk gate.

## 7. Risk authorisation

Risk tiering considers physical safety, rights/equity, privacy/data sensitivity, scale, reversibility, autonomy, failure detectability and dependency/lock-in.

- Low: bounded and readily reversible.
- Medium: consequential but containable; professional review required.
- High: high-impact/sensitive/hard-to-reverse; senior Public Steward authorisation, stronger oversight, independent review and tested rollback.
- Not Eligible: unacceptable/legal/ownership/rollback failures; do not pilot.

The detailed controls live in `risk_tiers.md` and `authorization_matrix.csv`.

## 8. Bounded experiment rule

An experiment cannot start without:

- a baseline;
- a falsifiable hypothesis;
- the exact capability/model/rule version;
- population/space boundaries and exclusions;
- an expiry/review date;
- data/provenance plan;
- primary public-value measure and guardrails;
- subgroup/equity review where relevant;
- public notice and consent/choice logic appropriate to the use;
- human override;
- incident owner;
- predeclared stop conditions;
- rollback/decommission route.

The experiment card schema is defined in `experiment_protocol.md`.

## 9. Public-value gate

Technical accuracy, uptime or adoption are supporting evidence only. The common floor is:

- safety;
- rights/equity;
- privacy/data minimisation;
- environmental burden;
- total public cost / dependency;
- meaningful human control and exit.

Each scenario adds its own outcome indicators. Average improvement is insufficient when a vulnerable subgroup, worst quantile, complaint pattern or safety tail deteriorates materially.

## 10. Decision semantics

### STOP
Use when a floor is breached, residual risk is unacceptable, lawful operation is not possible, net public value is negative, or the hypothesis is no longer worth exposing people to. STOP may be **responsible learning**, not organisational failure.

### MODIFY
The public purpose remains valuable, but evidence, design, data, safeguards or user experience must change before the next bounded test.

### CONTINUE
The current bounded test needs more evidence, the protocol remains valid and no stop condition has been triggered. CONTINUE is not SCALE.

### SCALE
The capability reaches its predeclared public-value threshold, critical floors pass, evidence confidence is adequate, maintenance/exit ownership exists, and the approved scale remains within the validated context.

## 11. Capability Backbone exchange rule

Capability Backbone means capabilities can be **discovered, described, compared and offered for transfer**. It is not an automatic deployment bus.

A capability moving from one Learning Unit to another must pass `capability_transfer_rules.md`. Population, spatial, data, institutional, infrastructure, model/version or rights context changes can trigger revalidation and re-authorisation.

Candidate role mapping:

- 众智园 — capability production, technical validation and governance testing;
- 北京 AI 原点社区 — social feedback, talent/community and public-service learning;
- 大钟寺 — AI-native service/market validation;
- 中关村科技服务翼 — innovation resources, capital, IP and professional-service exchange;
- 小月河场景赋能翼 — public-space and real-city scenario testing.

These are design roles aligned to the project taskbook, not statutory land-use approvals.

## 12. Memory and retirement

Learning is incomplete if only successful deployments are visible. `Landmark as Memory`, Annual City Version Release and Retired Capability Archive should expose:

- what was tried;
- what changed;
- what was stopped and why;
- unresolved problems;
- incidents and overrides at an appropriate privacy-preserving level;
- what was retired/replaced;
- what evidence should be reused in the next cycle.

## 13. Minimum audit event

Every material action emits an audit event with at least:

`event_id, timestamp, object_type, object_id, actor_role, human_accountable_owner, action, previous_state, new_state, capability_version, evidence_refs, risk_tier, authorization_ref, reason, incident_ref, rollback_ref`.

The audit log must not expose raw personal data to the public dashboard.

## 14. Phase status

Phases 1–6 are structurally closed by the linked workstream documents. Phases 7–9 are completed in the UAR, transfer and dashboard specifications. Real operational adoption and metric values remain future implementation work.
