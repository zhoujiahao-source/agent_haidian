# Urban Learning Protocol

## Status

This is a **conceptual governance and urban-design protocol** for the competition proposal. It is not a statement of current law, a committed government operating procedure, or an approved administrative process.

It must be adapted to applicable laws, public-sector responsibilities and real operator capacity if implementation is later deepened.

# 1. Purpose

The City OS exists to answer one question:

> How can a city safely convert emerging AI capability into tested, measurable and transferable public capability?

The protocol therefore separates:

- problem detection;
- authority;
- experimentation;
- evaluation;
- scaling;
- transfer;
- retirement.

No single actor controls all seven stages.

# 2. Core lifecycle

`OBSERVE → DIAGNOSE → QUALIFY → AUTHORIZE → SANDBOX → PILOT → REVIEW → STOP / MODIFY / CONTINUE / SCALE → REGISTER CAPABILITY → TRANSFER + REVALIDATE → VERSION RELEASE → RETIRE / REPLACE`

Use this lifecycle in diagrams rather than a GitHub Pull Request metaphor.

# 3. Stage definitions

## 3.1 OBSERVE

Inputs may include only data appropriate to the task and compliant with the competition's public / cleared-data rules.

Purpose:

- understand existing conditions;
- establish a baseline;
- detect change.

Output:

- observation record;
- evidence class;
- limitations.

No design intervention is authorized at this stage.

## 3.2 DIAGNOSE

City Agent or human teams identify a possible urban problem / mismatch.

Examples:

- heat-risk pattern;
- accessibility break;
- public-service mismatch;
- mobility reliability issue;
- underused public facility;
- emergency-service coordination gap.

Output:

- problem hypothesis;
- affected groups;
- evidence confidence;
- potential public-value dimensions.

Important:

**Diagnosis is not a decision.**

## 3.3 QUALIFY

Human / institutional review determines whether the problem is suitable for an AI-enabled intervention at all.

Questions:

1. Is the problem real enough to justify a test?
2. Could a simpler non-AI intervention solve it better?
3. Is the required data lawful / proportionate / available?
4. Are vulnerable groups affected?
5. Is the intervention reversible?
6. Is there a meaningful public-value baseline?

Possible result:

- `NO TEST` — problem not suitable / evidence insufficient;
- `NON-AI FIRST` — simpler intervention preferred;
- `PROCEED TO RISK CLASSIFICATION`.

This stage prevents technology-supply-driven urbanism.

# 4. Dual entry routes

## 4.1 Problem Track

`City Agent / public institution identifies problem → publishes / frames challenge → teams propose capability → qualify → risk classify → test`

Key rule:

The problem exists before the technology vendor.

## 4.2 Capability Track

`university / developer / company / community proposes capability → demonstrates real public need → identifies target problem + baseline → qualify → risk classify → test`

Key rule:

A capability without a demonstrated public need does not enter the city test system merely because it is technically novel.

# 5. Risk tiers

Risk is based on **real-world consequence**, not model sophistication.

## Tier L — Low Risk

Typical characteristics:

- limited physical / service consequence;
- no or minimal personal data;
- easy to reverse;
- clear non-AI fallback;
- small spatial / temporal scope;
- failure produces limited harm.

Potential conceptual examples:

- non-personal environmental information;
- temporary wayfinding assistance with clear conventional signage fallback;
- public-space scheduling suggestions that do not restrict access.

Governance expectation:

- streamlined professional authorization;
- predefined rollback;
- local monitoring;
- visible experiment status.

## Tier M — Medium Risk

Typical characteristics:

- affects access to services / mobility / recommendations;
- may process personal or sensitive contextual information;
- failure can disadvantage groups or disrupt service;
- human override required;
- larger spatial / temporal scope.

Governance expectation:

- professional review;
- explicit data / privacy assessment;
- affected-user testing;
- human fallback;
- independent / cross-disciplinary review where appropriate;
- more frequent monitoring.

## Tier H — High Risk

Typical characteristics:

- safety-critical / rights-affecting / high-consequence decisions;
- sensitive recognition or profiling;
- meaningful restriction / allocation / emergency consequences;
- difficult-to-reverse impacts;
- vulnerable populations disproportionately affected.

Governance expectation:

- no autonomous deployment based on the proposal alone;
- stringent legal / ethical / professional authorization;
- public-interest and affected-group review where appropriate;
- independent audit;
- very clear human authority / shutdown;
- narrow test scope if testing is legally and ethically permissible at all.

The formal proposal must not imply that this conceptual tiering replaces existing laws or regulatory obligations.

# 6. Authorization matrix

A final structured matrix should record at least:

| Field | Meaning |
|---|---|
| experiment_id | unique stable identifier |
| problem_id | linked real problem |
| capability_id | proposed capability |
| area / node | spatial location |
| evidence_class | Official / Verified / Derived / Assumed / Unknown |
| risk_tier | L / M / H |
| data_scope | minimum required data |
| consent_mode | Ambient / explicit consent / not applicable |
| approving_role | conceptual human / institutional authority |
| human_override | exact fallback / stop mechanism |
| rollback_plan | how intervention is removed / restored |
| start_condition | requirements before test |
| stop_condition | safety / public-value / data trigger |
| baseline_metrics | before-test state |
| review_date | required review moment |
| public_notice | what is made visible |

# 7. Sandbox before real-world pilot

Where appropriate, capabilities should be tested in a lower-consequence environment before public-space deployment.

Sandbox can mean:

- simulation;
- synthetic / historical public dataset test;
- controlled environment;
- non-operational demonstration;
- staff / expert dry run;
- limited closed pilot.

Sandbox success does **not** automatically authorize a real-world pilot.

# 8. Real-world pilot design

Every pilot must be bounded in:

- place;
- time;
- user group / applicability;
- data scope;
- function;
- risk tier;
- rollback method.

A pilot should be **reversible by design**.

The public-facing interface should make relevant information legible without overwhelming users, such as:

- what is being tested;
- whether participation is optional;
- what capability is provided;
- how to access a human alternative;
- where feedback / complaint can be made;
- when the pilot ends / is reviewed.

# 9. Public Value Review

The review asks:

> Is the city condition measurably better, fairer, safer and more sustainable than the baseline, with acceptable cost and risk?

## 9.1 Mandatory baseline dimensions

- Safety
- Equity
- Privacy
- Environment
- Cost

## 9.2 Scenario-specific dimensions

Each scenario adds 2–4 measures directly linked to the problem.

## 9.3 Distribution, not average only

The review must inspect:

- average outcome;
- vulnerable-group outcome;
- worst-case / tail outcome;
- spatial distribution;
- time-of-day distribution;
- complaints;
- manual takeover / fallback use;
- failures / near misses;
- unintended effects.

# 10. Four decisions

## STOP

Use when:

- safety / rights / privacy threshold breached;
- public value is negative or insufficient;
- inequity worsens materially;
- simpler non-AI solution clearly outperforms;
- data quality inadequate;
- cost / maintenance disproportionate;
- public / institutional trust conditions fail.

STOP can count as successful learning if it prevents further harm and the failure is documented.

## MODIFY

Use when:

- core need remains valid;
- public value is plausible but uneven / insufficient;
- risk can be reduced through redesign;
- data / interface / spatial scope needs adjustment.

Modification must produce a new version and new review condition.

## CONTINUE

Use when:

- evidence is positive but insufficient for scaling;
- seasonal / population / temporal variation still needs testing;
- risk remains bounded.

Continuation is not permanent authorization.

## SCALE

Use only when:

- public-value improvement is demonstrated;
- mandatory thresholds remain acceptable;
- affected groups do not show unacceptable harm;
- operation / maintenance / human fallback are viable;
- documentation is complete.

Scaling to a different district triggers **context revalidation**, not automatic copy-paste.

# 11. Capability Registry

Validated capabilities become entries in a **City Capability Registry**.

Each entry should contain:

- capability name / version;
- problem types addressed;
- validation areas / contexts;
- evidence status;
- risk tier(s);
- required inputs / infrastructure;
- public-value results;
- known failure modes;
- prohibited / unvalidated contexts;
- Human Override requirements;
- transfer / revalidation requirements;
- current lifecycle state: TEST / MODIFY / ACTIVE / RETIRED.

This registry supports the Capability Backbone concept without turning the city into an app store.

# 12. Capability transfer rules

A capability validated in one area may be transferred only after checking:

1. user population difference;
2. spatial morphology difference;
3. service / institutional context;
4. data availability / quality;
5. risk change;
6. infrastructure compatibility;
7. cultural / accessibility factors;
8. public-value baseline difference.

Transfer outcomes:

- `REUSE` — context sufficiently similar, limited verification required;
- `REVALIDATE` — new pilot required;
- `MODIFY` — capability must be adapted;
- `DO NOT TRANSFER` — context / risk incompatible.

# 13. Human Override

Every operational AI capability must define what happens when the AI is unavailable, wrong, contested or refused.

Human Override can include:

- human service desk / staff;
- conventional signage / wayfinding;
- manual environmental controls;
- non-AI emergency procedure;
- alternative accessible route;
- explicit service opt-out;
- shutdown / rollback authority.

A system with no credible fallback should not be described as resilient public infrastructure.

# 14. Public transparency layer

This is where the earlier `Legible AI` idea remains valuable.

The public should be able to understand, at an appropriate level:

- capability purpose;
- current lifecycle state;
- whether a node is existing service or experiment;
- evidence / uncertainty status;
- risk / consent mode;
- responsible human / public authority category;
- how to object / provide feedback;
- last review / next review;
- version / retirement history.

Transparency should use the Public Service Aesthetic rather than dense technical disclosure at every location.

# 15. Annual City Version Release

At least annually, the proposed operating institution publishes a public changelog of:

- new capabilities;
- modified capabilities;
- scaled capabilities;
- stopped capabilities;
- retired capabilities;
- unresolved urban problems;
- key public-value changes;
- major incidents / lessons where appropriate;
- next-year challenge priorities.

The annual event is not merely a showcase. It is a public accountability ritual.

# 16. Retirement

A capability should retire when:

- public need disappears;
- better non-AI or AI alternative exists;
- maintenance burden becomes disproportionate;
- data / privacy basis is no longer appropriate;
- risk becomes unacceptable;
- infrastructure is obsolete;
- performance no longer meets public-value threshold.

Retirement process:

`decision → service transition → data / hardware decommission plan → public notice where needed → archive evidence / lessons → physical trace / object curated if culturally valuable → registry status RETIRED`

Important cases enter the **Retired Capability Archive**.

# 17. Anti-capture rules

The conceptual system should guard against:

- vendor lock-in;
- technology looking for a problem;
- optimization for easy metrics only;
- permanent pilots that never receive a decision;
- shifting public responsibility to a private platform;
- hiding failed tests;
- excluding digitally less-capable users;
- treating consent as a one-time checkbox;
- scaling based only on average benefit.

# 18. Diagram-ready protocol

The final figure should show three parallel layers:

## Layer 1 — Problem / capability flow

Problem Track + Capability Track → qualification → test → capability registry → transfer / retire.

## Layer 2 — Authority / risk

Risk tier → authorization → consent → human override → independent review.

## Layer 3 — public value / memory

Baseline → metric observation → STOP/MODIFY/CONTINUE/SCALE → annual version release → learning archive.

# 19. Formal package integration notes

When this protocol enters the formal proposal:

- clearly call it a **proposed governance framework**;
- cite relevant official / professional sources where required;
- do not represent risk tiers as current law unless sourced;
- map scenarios to real spatial nodes;
- use custom metrics with schema-compliant status / formula / source files;
- distinguish current evidence from future monitoring.
