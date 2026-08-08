# Risk Tiers for Urban AI Experiments

## Principle

Risk tier is based on **real-world consequence, rights impact, data sensitivity, reversibility, autonomy and detectability**, not on model size or technical sophistication.

## 1. Assessment dimensions

Each proposal is assessed across:

1. **physical safety** — credible bodily/property harm;
2. **rights & equity** — access to public services, opportunity, discrimination, exclusion;
3. **privacy / data sensitivity** — anonymous aggregate -> personal -> sensitive/biometric;
4. **scale** — single user/small site -> community -> cross-area/citywide;
5. **reversibility** — immediate rollback -> recoverable -> hard/irreversible;
6. **autonomy** — information -> recommendation -> constrained actuation -> autonomous execution;
7. **failure detectability** — obvious/realtime -> delayed/hidden;
8. **dependency / lock-in** — substitutable -> operationally dependent -> structurally locked.

These are ordinal review dimensions, not pseudo-precise scientific measurements.

## 2. Tiers

### LOW — bounded, reversible, low-consequence

Typical conditions:
- no sensitive personal information;
- no material rights/eligibility decision;
- no meaningful physical-safety actuation;
- small spatial/population scope;
- immediate or near-immediate rollback;
- failure is visible;
- AI advises or operates an ambient low-risk service.

Examples: non-personal wayfinding suggestions; aggregated park microclimate optimization with safe manual fallback.

### MEDIUM — consequential but containable

Any of the following can raise a proposal to Medium:
- individual-level personalization without high-impact rights decision;
- limited physical actuation with engineered safety envelope;
- public-service workflow changes that may cause material inconvenience/exclusion;
- broader community exposure;
- failure may be delayed;
- rollback requires coordinated operational action.

Medium experiments require professional review, documented human override, explicit monitoring and bounded duration.

### HIGH — high-impact / sensitive / difficult-to-reverse

High applies when the use could materially affect:
- safety;
- access to essential/public services or opportunities;
- sensitive personal information / biometric identification;
- significant rights or equity outcomes;
- citywide or multi-area systems with hidden failure;
- autonomous physical action with serious harm potential;
- high dependence where exit is costly or service continuity is threatened.

High-risk AI does **not** receive autonomous final authority. It requires senior Public Steward authorization, specialist reviews, human decision authority, stronger public notice/participation, independent audit and tested rollback.

### NOT ELIGIBLE / STOP BEFORE PILOT

A proposal is not eligible for an urban experiment when, for the proposed design, any of the following is true:

- unlawful or uncleared data use;
- covert sensitive-person inference incompatible with the public purpose;
- no accountable human owner;
- no feasible safe rollback for a material safety/rights function;
- unacceptable residual risk after mitigation;
- the only way to “succeed” is to deny meaningful consent/appeal where those safeguards are required;
- the experiment would fabricate statutory authority or approved planning control.

## 3. Escalation overrides

Regardless of any aggregate score:

- sensitive/biometric data + consequential individual decision -> **High at minimum**;
- serious physical-harm potential + autonomous actuation -> **High at minimum**;
- material rights impact + no meaningful human review -> **Not eligible**;
- no reliable incident detection + high consequence -> **High / Not eligible until mitigated**;
- pilot crosses into a materially different population/data/physical context -> re-tier before transfer.

## 4. Required review evidence

Every tier record must identify:
`risk_dimensions`, `tier`, `rationale`, `human_owner`, `specialist_reviewers`, `public_notice`, `consent_mode`, `override`, `stop_conditions`, `rollback`, `incident_owner`, `audit_interval`.

## 5. External framework crosswalk (non-statutory for this project)

- NIST AI RMF: continuous risk management and trustworthiness-oriented governance.
- OECD AI Principles: human rights/fairness/privacy, transparency, robustness/safety, accountability, override/decommission.
- EU AI Act: comparative reference for lifecycle risk management and proportionate human oversight of high-risk systems.
- PRC Personal Information Protection Law: relevant to necessity, automated decision transparency/fairness, significant-impact explanation/refusal rights, public-place image/identification safeguards, and impact assessment obligations.
- GB/T 45392-2025: current Chinese national standard specifically addressing security requirements for automated decision-making based on personal information.

These references guide design due diligence; applicability to a deployed system must be separately determined by qualified legal/compliance owners.
