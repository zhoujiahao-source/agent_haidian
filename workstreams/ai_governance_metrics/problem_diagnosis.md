# Problem Diagnosis & Dual-Entry Intake Protocol

## Purpose

City Agent is a **diagnostic and proposal actor**, not a sovereign decision-maker. It may discover patterns, propose hypotheses and assemble evidence, but it does not receive higher execution authority simply because its model is more capable.

## 1. Data boundary for City Agent

### Class A — public / non-personal urban evidence
Examples: published planning documents, open mobility counts, weather/environmental observations, public facility inventories, aggregated service statistics.  
Default: allowed when provenance, license, spatial/temporal coverage and uncertainty are recorded.

### Class B — cleared aggregate operational data
Examples: anonymized queue lengths, aggregated energy use, service uptime, complaint categories.  
Default: allowed only for the stated purpose and minimum necessary scope, with an accountable data owner.

### Class C — personal information
Examples: identifiable trip histories, account-level service use, device-linked traces.  
Default: **not available to City Agent diagnosis**. If a use case cannot be meaningfully evaluated without personal information, it leaves the default diagnosis path and enters a separate higher-risk privacy/impact review.

### Class D — sensitive personal / biometric / high-impact inference
Examples: face/voice identification, health, precise behavioral profiling, sensitive attribute inference.  
Default: **prohibited from routine City Agent diagnosis**. Any exceptional proposal requires explicit lawful basis, purpose limitation, separate authorization, impact assessment, consent/notice where applicable, human oversight and an exit path. No workstream metric assumes access to these data.

## 2. Diagnosis is not causation

Every detected pattern must be recorded as one of:

- `observation`: measured descriptive state;
- `association`: variables move together, without causal claim;
- `hypothesis`: testable explanation;
- `validated_problem`: accepted public problem after evidence and governance review.

City Agent may rank **attention candidates**, not people's entitlement, legal status or final public-service priority.

## 3. Problem Track eligibility gate

A problem becomes `eligible_issue` only when all minimum fields exist:

1. stable issue ID and duplicate check;
2. plain-language problem statement;
3. affected population and/or space;
4. public-value relevance;
5. baseline or a credible plan to establish one;
6. evidence sources with status and limitations;
7. uncertainty / alternative explanations;
8. named human public-service owner;
9. at least one potentially reversible intervention path;
10. risk pre-screen completed.

Raw alerts, duplicates, model hallucinations and unsupported correlations stay outside the Urban Adaptation Rate denominator.

## 4. Capability Track eligibility gate

A proposed capability enters the same governance pipeline only if it supplies:

- the public problem(s) it claims to address;
- intended users and non-users;
- required data categories;
- intended autonomy level;
- failure modes and foreseeable misuse;
- non-AI / lower-tech comparator where plausible;
- human owner and maintenance owner;
- rollback / decommission concept;
- dependency and vendor-lock-in disclosure.

A capability is not eligible simply because it is technically novel.

## 5. Need validation

Before authorization, the human owner checks:

- Is the problem materially real and current?
- Who defines “improvement”?
- Which groups could lose even if the average improves?
- Is AI needed, or is a process/space/staffing change better?
- Is the proposed evidence good enough for a bounded test?
- What evidence would falsify the hypothesis?

## 6. Priority without “AI says so”

Priority is a human-governed portfolio decision using documented factors such as severity, number of people affected, equity burden, time sensitivity, reversibility and resource cost. The Agent may provide a reproducible ranking **with sensitivity analysis**, but the Public Steward records the final priority and reasons.

## 7. Phase checkpoints

### Phase 1 — diagnosis
Completed: data classes, causal-language boundary, issue eligibility gate.
Unknown: future operational data catalogue and controller roles.
Dependency: risk tiering and authorization.

### Phase 2 — dual entry
Completed: Problem Track and Capability Track converge on the same risk/public-value gate.
Key control: a technology proposal cannot create its own demand signal.
