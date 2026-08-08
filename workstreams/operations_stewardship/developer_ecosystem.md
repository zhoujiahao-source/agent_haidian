# Developer Ecosystem｜开发者与持续贡献机制

## 1. Goal

Developer participation should produce maintainable public capabilities, not a one-week hackathon archive. The durable interface is a **Capability Registry + sandbox + version/compatibility contract + maintenance/retirement obligation**.

All mechanisms below are Proposed.

## 2. Capability Registry minimum record

Each admitted capability should expose, at an appropriate public detail level:
- stable `capability_id` independent of a vendor/product name;
- plain-language purpose and public-value objective;
- lifecycle status: proposed / sandbox / trial / continue / scale / modify / suspended / retired;
- accountable public owner status;
- maintainer and support status;
- operational risk tier and authorization state;
- affected groups / beneficiary statement;
- data categories and provenance class;
- model/service/component versions where relevant;
- interface and dependency summary;
- evaluation metrics and latest evidence date;
- incidents, complaints and human-override summary links;
- interoperability / export / migration notes;
- IP/license/open-source status;
- deprecation and sunset condition;
- replacement / successor capability when retired.

The registry is a governance index, not a marketing catalogue.

## 3. Contribution path

1. Read public challenge/capability documentation.
2. Register contributor/team and license/provenance information appropriate to the contribution.
3. Submit a problem-linked proposal or reusable component.
4. Complete documentation/data/risk/maintenance checks.
5. Use synthetic/open-data sandbox first where feasible.
6. Pass controlled integration/failover checks.
7. Seek public authorization only for a bounded public trial.
8. Publish results, including negative findings and limitations.
9. Maintain, migrate, hand off or retire the contribution through the same registry.

## 4. Documentation contract

A capability should be understandable by a maintainer who did not build it. Recommended documentation:
- architecture and data-flow overview;
- API/interface contract or equivalent service interface;
- dependency inventory and version policy;
- test/failure-mode record;
- deployment and rollback procedure;
- security/privacy assumptions without exposing exploitable secrets;
- accessibility/human fallback behavior;
- evaluation method and known limits;
- maintainer runbook;
- migration/deprecation instructions.

## 5. Compatibility strategy

Use semantic, explicit compatibility rather than permanent dependence on one vendor stack:
- stable capability-level identifiers;
- documented interface versions;
- machine-readable dependency/version metadata where practical;
- backwards-compatibility window defined by competent maintainers, not invented here;
- deprecation notices linked to migration guidance;
- periodic replacement drills for critical dependencies;
- evidence records that survive model/vendor replacement.

## 6. Credit and attribution

Contribution recognition should record humans, teams, organizations and Agents where appropriate, plus source/license/provenance. Credit is earned for more than launches:
- reusable components;
- accessibility fixes;
- evaluation methods;
- high-quality datasets with lawful provenance;
- risk findings/red-team work;
- maintenance and migrations;
- responsible STOP/retirement work;
- documentation and community support.

Do not turn contribution points into an incentive for raw deployment volume.

## 7. Open-source / IP boundary

Open source is encouraged where it improves auditability, reuse and substitution, but openness alone does not authorize public deployment. Proprietary capabilities can participate if public-value, auditability, maintenance, interoperability and exit requirements can be met. Every proposal declares license/IP before trial. Unclear redistribution rights block publishing artifacts that cannot legally be shared.

## 8. Maintenance responsibility

A developer event cannot be the maintenance plan. Before SCALE, the record must identify:
- a durable maintainer;
- how security/bug fixes are handled;
- dependency monitoring;
- what happens if the original developer leaves;
- succession/handoff documentation;
- end-of-support/deprecation path;
- public service fallback while migration occurs.

## 9. Community technical participation

Developers should have standing mechanisms beyond annual events:
- open challenge brief reviews;
- documentation clinics;
- sandbox test sessions;
- issue/bug/risk reporting;
- interoperability tests;
- maintenance bounties or procurements where lawfully established;
- open evaluation method reviews;
- archive/migration sprints for retiring capabilities.

No funding mechanism is claimed to exist; these are design options for competent operators.

## 10. Relationship to the five Learning Units

Different areas can host different kinds of developer work—technical validation, social feedback/public services, AI-native service validation, innovation-resource exchange and public-space scenario testing—but a capability uses the same registry, risk, evidence, version and retirement language. That common contract is what makes the Capability Backbone an exchange network rather than five isolated innovation zones.