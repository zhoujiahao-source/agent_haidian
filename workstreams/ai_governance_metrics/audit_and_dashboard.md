# Open Dashboard & Professional Audit Architecture

## 1. Principle

One evidence system, two disclosure layers:

- **Public layer:** understandable without reading model internals.
- **Professional audit layer:** enough provenance, versioning and failure evidence to reproduce governance decisions.

Public transparency does not mean publishing raw personal data, security-sensitive configurations or proprietary secrets.

## 2. Public dashboard — minimum card

For each active/closed capability or experiment, show:

1. What problem are we trying to improve?
2. Why is AI / this capability being tested instead of a simpler alternative?
3. Where and for whom is the test active? (using appropriate, non-sensitive spatial granularity)
4. Current lifecycle state and next review date.
5. Risk tier with plain-language reason.
6. Named accountable public/service owner.
7. Data categories in plain language and whether personal/sensitive data are involved.
8. Notice / consent / choice / human alternative as applicable.
9. Human override / safe-stop availability.
10. Primary public-value target and current evidence confidence.
11. Overall + relevant subgroup/worst-case outcome.
12. Incidents/near misses at privacy-preserving severity level.
13. Human overrides/material manual interventions.
14. Complaints/appeals/opt-outs and how to use the channel.
15. STOP/MODIFY/CONTINUE/SCALE decision and rationale when closed/reviewed.
16. Retirement/replacement status when applicable.

## 3. Professional audit layer

Expose authorised reviewers to:

- issue/capability/experiment/decision registry IDs;
- immutable model/rule/configuration version hashes where technically appropriate;
- data provenance, license/authority status, transformation, coverage and missingness;
- baseline/comparator design;
- cohort definitions and metric formulas;
- raw aggregated distributions necessary to recompute published metrics;
- subgroup/worst-case methodology and suppression rules;
- authorisation, expiry and reviewer roles;
- incident, near-miss and failure-detection logs;
- override/manual-intervention logs;
- notice/consent/appeal process evidence;
- stop-trigger and rollback-drill records;
- audit samples/corrections;
- transfer/revalidation records;
- vendor dependency / exit evidence;
- retirement and data-deletion/decommission evidence.

Access to personal/raw sensitive records remains purpose-limited and controlled; the audit layer is not a public data dump.

## 4. Information architecture

### City overview
- open eligible issues;
- experiments by lifecycle decision;
- UAR cohort status (only when valid);
- Responsible STOPs;
- unresolved/overdue issues;
- incident/complaint summary;
- five Learning Unit activity.

### Issue page
Evidence, uncertainty, owner, baseline, interventions tried, current status and adaptation decision history.

### Capability page
Version, validated contexts, risk, dependencies, public-value evidence, transfer history and retirement status.

### Experiment page
Experiment card, monitoring, incidents, overrides, decisions and version changes.

### Audit / methodology page
Metric definitions, cohort snapshots, source/data-status vocabulary, audit corrections and anti-gaming rules.

## 5. Accessibility and legibility

Use text + icon/shape + line pattern, not colour alone. Recommended status language:

- ▶ Test active
- ◇ Evidence review
- ■ Scale approved
- △ Modify required
- ⛔ Stop
- ↺ Revalidating transfer
- ▱ Retired/archive
- ? Unknown / missing evidence

Maintain Chinese/English terminology alignment in final integration. Avoid confidence theatricality: `unknown` is a valid professional state.

## 6. Audit integrity

- append-only material decision history;
- content/version hashes for evidence snapshots where practical;
- recorded corrections rather than destructive overwrite;
- role separation for High-risk review where feasible;
- independent sample audit of denominator, incidents, overrides, manual labour and metric changes;
- retention schedules appropriate to data sensitivity and accountability needs;
- no use of dashboard engagement as proof of public value.

## 7. Annual City Version Release

The yearly release should publish a human-readable delta:

- new capabilities;
- modified capabilities;
- scaled capabilities;
- stopped/retired capabilities;
- unresolved issues;
- UAR/learning metrics with cohorts and confidence;
- major governance/audit changes;
- known data gaps and next-year learning priorities.

This creates institutional memory without implying that each annual release is a statutory planning revision.
