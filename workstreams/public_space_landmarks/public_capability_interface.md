# Public Capability Interface｜公共能力接口

## 1. Purpose

The public-space system does not ask residents to “experience AI.” It lets them use city capabilities — cooling, navigation, accessibility, public help, emergency support, cultural interpretation, community services and reversible experiments — while AI stays mostly backstage.

This workstream treats **Public Capability Interface (PCI)** as a civic-space specification rather than a screen, kiosk or app category.

## 2. Interface contract

Every PCI node must satisfy six layers.

### A. Non-AI civic baseline

The space remains useful when AI, network, power or personal devices fail. Baseline elements include continuous walking surfaces, shade/seating where relevant, readable static wayfinding, staffed/help contact, lighting, drainage, universal-design details and conventional emergency procedures.

### B. Ambient Layer

Low-risk environmental capabilities may operate by default when they do not require personal identification or individualized judgment. Examples include thermal/environment sensing, non-identifying equipment-health monitoring, public-space lighting schedule coordination, water/cooling equipment control where professionally approved, queue/load balancing from aggregated counts, and public transit/service status display.

Ambient operation should expose a simple status: **ON / DEGRADED / OFF / MANUAL**.

### C. Consent Layer

Functions using personal preferences, individual route needs, recommendation, account linkage or other individualized decisions require explicit user action. A user must retain a meaningful non-AI or minimally digital alternative.

Rules:
1. No forced app installation.
2. No passive inference of disability, age, health or identity as a public-space default.
3. Purpose and retention are explained before collection.
4. Consent can be withdrawn without losing access to the basic public space.

### D. Human Override

Human responsibility is always named. Each node shows who can stop, correct or replace the automated function. Higher-risk temporary tests have a physical/local operator stop procedure appropriate to the equipment; ordinary information services provide staff/contact escalation.

### E. Failure-safe spatial mode

Failure must not make the space unusable. Examples:
- navigation → static map + tactile/printed route + staff contact;
- cooling control → passive shade/planting/drinking-water baseline remains;
- service assistant → human counter/phone/service directory remains;
- robotic test → device stops and the public route remains physically separated;
- digital memory display → physical archive labels remain legible.

### F. Public learning record

Each capability carries a public record: problem addressed, current status, operator/steward, data class, human override, trial dates if any, result (`STOP / MODIFY / CONTINUE / SCALE`) and an archive reference when appropriate.

## 3. Risk-to-interface matrix

| Risk | Typical use | Default | Required control | Spatial response |
|---|---|---|---|---|
| R0 | static history, seating, conventional signage | non-AI | normal management | always available |
| R1 | environmental coordination, non-personal public info | Ambient | status visibility, logs, manual fallback | may run by default |
| R2 | personalized routing/recommendations/account service | Consent | active opt-in, minimization, exit, human escalation | basic service remains without opt-in |
| R3 | robot/vehicle/physical-world test or high-impact support | Consent + controlled trial | professional approval, bounded zone/time, named operator, stop authority, incident protocol | separated from ordinary circulation; reversible |

This is a design-governance classification, not a legal classification.

## 4. Spatial grammar

PCI is a **node network**, not repeated smart kiosks. The family shares only a small identity kit: Open Node symbol, paired-rail line motif, capability/status tags and common information hierarchy.

- **Line** = Capability Backbone / movement and exchange logic.
- **Node** = place where a capability can be called, understood or transferred.
- **Switch** = choice point: manual/AI, route A/B, continue/stop, local/remote service.
- **Mileage mark** = time/version marker rather than nostalgic decoration.
- **Archive tag** = evidence of a capability life cycle.

## 5. Five-zone fit

- **Zhongzhiyuan**: controlled test and capability-production interfaces; strongest R3 governance and physical separation.
- **Beijing AI Origin Community**: daily public-service, community co-creation and talent/community interfaces; strongest no-app and mixed-age accessibility requirements.
- **Dazhongsi**: AI-native service/business validation; strong consent, consumer clarity, human-service fallback and after-hours operation.
- **Zhongguancun Technology Service Wing**: capability exchange, professional services, standards/translation and cross-zone routing.
- **Xiaoyuehe Scenario Empowerment Wing**: climate, blue-green, accessibility, leisure and real public-space testing; low-tech spatial performance first.

## 6. Hard design tests

A node fails if:
- it becomes meaningless without a screen/app;
- AI replaces basic urban-design duties such as shade, ramps, lighting or safe crossings;
- ordinary public-space access requires personal identification;
- there is no visible human owner or override path;
- network/power/model failure blocks ordinary circulation or basic service;
- it is primarily a technology showcase rather than a public capability.

## 7. Integration note

Exact placement is intentionally withheld until official boundary/key-area, heritage-control, ownership, traffic and engineering information is available. Integration should map typologies to verified existing conditions rather than preserve provisional coordinates.