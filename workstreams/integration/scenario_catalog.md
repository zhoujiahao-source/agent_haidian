# City OS Scenario Catalog

> Status: conceptual scenario set for integration. Every final scenario must be linked to current site evidence, allowed design space, valid source records and schema-compatible structured outputs before canonical submission use.

The catalog intentionally exceeds the official minimum of 10 scenarios and includes more than 3 explicit test / validation scenarios.

# Common card schema

Each scenario uses:

- **Problem** — real public need / mismatch to verify
- **Primary users** — affected people
- **Spatial focus** — target area / node type; exact geometry remains evidence-dependent
- **Capability** — what public capability is being tested / provided
- **Entry route** — Problem Track or Capability Track
- **Mode** — Ambient / Consent / mixed
- **Conceptual risk tier** — L / M / H; must be rechecked against law / real implementation
- **Human Override** — non-AI / human fallback
- **Baseline evidence** — what must be known before pilot
- **Scene metrics** — additional metrics beyond Safety / Equity / Privacy / Environment / Cost
- **Test boundary** — how to keep it limited and reversible
- **Decision triggers** — STOP / MODIFY / CONTINUE / SCALE
- **Transfer rule** — conditions before reuse elsewhere

---

# S01 — Heat Refuge Network / 高温避暑能力网络

## Problem

Summer heat can make exposed public routes / waiting / resting spaces difficult for older adults, children, outdoor workers and other heat-sensitive users. The exact high-risk locations must be established from legitimate spatial / climate evidence rather than assumed.

## Primary users

- older adults
- children / caregivers
- outdoor workers
- commuters
- people with limited mobility

## Spatial focus

Priority candidate: 小月河场景赋能翼 + Capability Backbone public-realm nodes, subject to actual shade / green / route evidence.

## Capability

A network that combines existing shade / green / indoor refuge information with temporary low-risk environmental adaptation, route guidance and public-service coordination.

## Entry route

Problem Track.

## Mode

Mixed:

- Ambient: non-personal thermal / shade state display and low-risk environmental operations where appropriate.
- Consent: personalized route / assistance only when actively requested.

## Conceptual risk tier

L–M depending on whether personalized health / location data are involved.

## Human Override

- conventional signed refuge locations;
- staffed public facilities where applicable;
- non-AI route map;
- manual environmental controls.

## Baseline evidence

- public climate / temperature evidence;
- shade / tree / green / building-cover proxy;
- accessible routes;
- existing public facilities / water / rest points where publicly verifiable.

## Scene metrics

- refuge accessibility time / distance;
- thermal-comfort improvement proxy;
- vulnerable-user coverage;
- non-AI fallback availability.

## Test boundary

Small number of public nodes / one hot-weather period; reversible temporary interfaces before permanent construction.

## Decision triggers

STOP if route guidance creates safety / accessibility harm or environmental cost exceeds value. SCALE only after vulnerable-user outcomes are acceptable.

## Transfer rule

Revalidate microclimate, users and facility access in each new node.

---

# S02 — Barrier-Free Route Companion / 无障碍路径协同

## Problem

Accessible routes can be disrupted by steps, construction, narrow passages, temporary blockage or incomplete public information.

## Primary users

- wheelchair users
- visually impaired users
- older adults
- caregivers with strollers
- temporarily injured users

## Spatial focus

Backbone crossings / station-area links / east–west stitch points; exact barriers must be evidence-based.

## Capability

Actively requested accessible route assistance that combines verified barrier information, temporary reports and human service escalation.

## Entry route

Problem Track.

## Mode

Consent.

## Conceptual risk tier

M because incorrect route information can create real access / safety consequences.

## Human Override

- conventional accessible signs;
- staffed assistance / phone or physical help point;
- alternative verified route;
- user ability to reject / correct recommendation.

## Baseline evidence

- route / crossing geometry;
- accessibility evidence;
- verified barriers;
- public-facility entrances where available.

## Scene metrics

- successful accessible-route completion;
- false-safe-route rate;
- additional travel time;
- human handoff success;
- user correction / complaint rate.

## Test boundary

One route cluster before district expansion.

## Decision triggers

STOP on safety-critical false routing; MODIFY if coverage / false positives create substantial burden.

## Transfer rule

Never transfer route logic without fresh accessibility survey / verification.

---

# S03 — Elder Service Handoff / 老年公共服务转接

## Problem

Digital-first urban services can increase friction for older adults when AI becomes the only interface.

## Primary users

- older residents
- caregivers
- community workers

## Spatial focus

AI 原点社区 public-service / neighborhood interface nodes.

## Capability

AI assists with locating / preparing public-service requests but makes human handoff a first-class outcome rather than an exception.

## Entry route

Problem Track.

## Mode

Consent.

## Conceptual risk tier

M; higher if sensitive personal information or eligibility decisions are involved. The competition concept should avoid automating rights-affecting decisions.

## Human Override

- staff / phone / physical desk;
- paper / conventional service route;
- family / caregiver assistance with appropriate consent.

## Baseline evidence

- public-service inventory;
- documented service process where public;
- accessibility / digital inclusion evidence.

## Scene metrics

- successful human handoff rate;
- service completion time;
- digital opt-out parity;
- repeat-contact rate;
- complaint / correction rate.

## Test boundary

Only information / coordination functions first; no autonomous eligibility decision.

## Decision triggers

STOP if AI creates barriers to human service or produces systematic group disadvantage.

## Transfer rule

Revalidate service workflow and population needs for each community.

---

# S04 — Morning Transfer Reliability / 早高峰换乘协同

## Problem

Commuters experience uncertainty where walking, cycling, rail / metro, bus and station-area public space meet.

## Primary users

- commuters
- students
- workers
- users with mobility constraints

## Spatial focus

Capability Backbone mobility nodes / major transfer areas, subject to real transit data.

## Capability

Non-exclusive multimodal guidance, crowd / disruption information where public data permit, and accessible alternative-route suggestions.

## Entry route

Problem Track.

## Mode

Ambient + Consent.

## Conceptual risk tier

L–M depending on personalization and operational integration.

## Human Override

- conventional signs / schedules;
- staffed transport information;
- non-AI route options.

## Baseline evidence

- public transit / station / route data;
- walking network;
- transfer geometry;
- publicly available service reliability where available.

## Scene metrics

- transfer-time reliability;
- missed-transfer proxy;
- accessible transfer time;
- fallback-use success.

## Test boundary

Information / guidance layer only before operational control.

## Decision triggers

STOP if guidance increases safety risk or systematically disadvantages non-app users.

## Transfer rule

Revalidate schedules, station morphology and accessible routes.

---

# S05 — Child-Friendly Weekend Mode / 儿童友好周末模式

## Problem

Public spaces optimized for weekday commuting may underperform for children / caregivers on weekends.

## Primary users

- children
- caregivers
- nearby residents

## Spatial focus

小月河 / community public-space nodes where existing public use supports the scenario.

## Capability

Time-based programming / wayfinding / environmental support that helps existing public spaces host child-friendly routes and activities without permanent single-purpose redesign.

## Entry route

Problem Track or community Capability Track.

## Mode

Ambient; no child recognition / profiling required.

## Conceptual risk tier

L if designed without personal data.

## Human Override

- conventional event / route plan;
- staffed activity management;
- ordinary public-space use remains available.

## Baseline evidence

- public-space inventory;
- safe / accessible route evidence;
- existing facilities;
- temporal-use evidence if available.

## Scene metrics

- temporal use diversity;
- caregiver-reported usability where ethically / lawfully collected;
- accessible play / rest coverage;
- conflict with ordinary users / complaints.

## Test boundary

Weekend / limited nodes; fully reversible program layer.

## Decision triggers

MODIFY if programming crowds out ordinary public access or creates inequity.

## Transfer rule

Local community / facility context must be rechecked.

---

# S06 — Night Culture Route / 夜间文化线路

## Problem

Cultural / public-space networks can lose continuity and service visibility after normal business hours.

## Primary users

- residents
- students / young workers
- visitors
- night-shift workers

## Spatial focus

Railway culture / 大钟寺 / backbone cultural-public nodes, depending on real existing functions.

## Capability

Night wayfinding, public-facility information, event orchestration and human-assistance visibility; no surveillance-centric framing.

## Entry route

Problem Track + cultural-program Capability Track.

## Mode

Ambient + optional Consent.

## Conceptual risk tier

L–M.

## Human Override

- conventional lighting / signage;
- staffed event / security / service points where applicable;
- non-digital route.

## Baseline evidence

- public-space / route evidence;
- operating hours / transport information from public sources;
- cultural assets / destinations.

## Scene metrics

- route continuity / access;
- night public-service coverage;
- noise / resident-impact complaints;
- accessibility after dark;
- non-digital access parity.

## Test boundary

Event nights / selected route first.

## Decision triggers

STOP / MODIFY if resident burden, safety or exclusion worsens.

## Transfer rule

Revalidate local operating hours, transport and residents' conditions.

---

# S07 — Emergency Public-Space Mode / 公共空间应急模式

## Problem

Ordinary public spaces may need rapid transition during heat, severe weather, local disruption or other emergency conditions.

## Primary users

Everyone, with priority to vulnerable users.

## Spatial focus

Backbone exchange / resilience nodes.

## Capability

A public-space state change that prioritizes verified emergency information, accessible routes, refuge / service points and human authority.

## Entry route

Problem Track.

## Mode

Ambient for public alerts; Consent only for optional personalized help.

## Conceptual risk tier

H if integrated with safety-critical emergency decisions. The competition proposal should keep the AI role advisory / assistive unless formal authority and evidence support more.

## Human Override

Emergency authority / conventional procedures always dominate. AI failure must not remove basic emergency information.

## Baseline evidence

Formal public emergency procedures and facility evidence where available.

## Scene metrics

- fallback availability;
- accessible information coverage;
- transition time;
- false / conflicting information incidence;
- vulnerable-user service access.

## Test boundary

Simulation / drill / non-operational demonstration before any real emergency role.

## Decision triggers

Any conflict with official emergency authority → STOP / redesign.

## Transfer rule

Requires full institutional revalidation; never treated as plug-and-play.

---

# S08 — Railway Memory Companion / 京张铁路文化解释

## Problem

Railway history can become static signage disconnected from today's city and contemporary technical culture.

## Primary users

- residents
- students
- visitors
- researchers

## Spatial focus

1909 Railway Memory nodes / documented heritage / historical locations.

## Capability

Optional layered interpretation linking verified history, physical traces and city-learning stories; digital content is secondary to place.

## Entry route

Capability Track from cultural / research institutions or public program.

## Mode

Ambient basic interpretation + optional Consent for deeper personalized content without sensitive profiling.

## Conceptual risk tier

L.

## Human Override

Physical interpretation / archival references remain accessible without AI.

## Baseline evidence

Verified historical / heritage sources.

## Scene metrics

- source-traceability coverage;
- physical / non-digital access;
- interpretation correction rate;
- route / place engagement measures only if responsibly collected.

## Test boundary

Selected history nodes.

## Decision triggers

STOP / correct immediately for factual / attribution errors.

## Transfer rule

Every location requires place-specific historical evidence.

---

# S09 — Public Facility Demand Balancer / 公共设施供需协同

## Problem

Some public facilities may experience temporal mismatch between capacity and demand, while nearby alternatives are underused. This must be established from real public data before claiming a mismatch.

## Primary users

- residents
- students / workers
- facility staff

## Spatial focus

AI 原点社区 / backbone service nodes.

## Capability

Public information / booking / redirection support that helps users find available legitimate alternatives without automating rights-affecting allocation.

## Entry route

Problem Track.

## Mode

Consent for individual service choice; aggregate non-personal information may be Ambient.

## Conceptual risk tier

M if service access / personal data involved.

## Human Override

Staff / conventional booking / service access remains available.

## Baseline evidence

Public facility inventory, operating rules, capacity / usage only where lawfully available.

## Scene metrics

- successful alternative-service access;
- wait / response time;
- digital opt-out parity;
- spatial equity of service access;
- complaint rate.

## Test boundary

Information coordination first; no automated denial / priority ranking.

## Decision triggers

STOP if users without digital access receive worse service or if allocation fairness is compromised.

## Transfer rule

Revalidate facility rules and demand patterns.

---

# S10 — AI-Native Service Sandbox / 大钟寺 AI 原生服务沙盒

## Problem

AI-native services need real-world validation but can easily become technology looking for a market / city scene.

## Primary users

- local residents
- workers
- visitors
- service providers
- public-space users

## Spatial focus

大钟寺.

## Capability

A governed sandbox for temporary AI-native urban services that must demonstrate a real need, public-space compatibility and human fallback before longer operation.

## Entry route

Capability Track.

## Mode

Scenario-dependent.

## Conceptual risk tier

L–H depending on service; each proposal classified separately.

## Human Override

Mandatory for every service.

## Baseline evidence

Real service problem, existing market / public-service context, user / spatial constraints.

## Scene metrics

- public-need traceability;
- service completion / reliability;
- non-AI fallback use;
- public-space externalities;
- accessibility / equity outcomes.

## Test boundary

Temporary physical / service module with explicit end date.

## Decision triggers

No demonstrated public need → NO TEST. Vendor lock-in / exclusion / negative public-space impact → STOP.

## Transfer rule

Market success alone does not authorize citywide scaling; public-value revalidation required.

---

# S11 — Full-Stack Capability Validation / 众智园能力验证链

## Problem

Research prototypes often lack a clear path from lab performance to governed urban usefulness.

## Primary users

- researchers
- developers
- professional reviewers
- downstream public-service teams
- eventual public users

## Spatial focus

众智园 controlled / semi-controlled validation spaces before real-city transfer.

## Capability

A full-stack validation sequence from technical test to governance / public-value readiness.

## Entry route

Capability Track.

## Mode

Mostly controlled before public Consent / Ambient classification.

## Conceptual risk tier

Varies by capability.

## Human Override

Required before any public test.

## Baseline evidence

Technical benchmark alone is insufficient; target urban problem, public need and transfer context required.

## Scene metrics

- sandbox-to-pilot readiness;
- documented failure-mode coverage;
- rollback readiness;
- evidence completeness;
- downstream revalidation success.

## Test boundary

Controlled validation first.

## Decision triggers

Lack of public need / rollback / evidence → do not enter public pilot.

## Transfer rule

Every capability receives context-specific revalidation.

---

# S12 — City Version Public Review / 城市版本公共复盘

## Problem

Urban AI experiments can accumulate without a clear public record of what changed, failed, scaled or retired.

## Primary users

- residents
- public institutions
- developers / researchers
- professional reviewers
- media / visitors

## Spatial focus

2026 City Learning Archive + major Backbone Exchange Hub + online/offline annual publication.

## Capability

An annual / ongoing public interface that turns experiment histories into a city changelog and invites review of next priorities.

## Entry route

Public Stewardship operating process.

## Mode

Ambient public information; Consent for optional personalized participation.

## Conceptual risk tier

L for publication interface; governance content may involve higher institutional sensitivity but should use aggregated / appropriate public data.

## Human Override

Human-curated official / professional review of all published public claims.

## Baseline evidence

Capability registry, experiment decision records, public-value metrics, source / uncertainty metadata.

## Scene metrics

- experiment-transparency coverage;
- failure-documentation rate;
- retired-capability documentation rate;
- participation diversity where lawfully measured;
- unresolved-problem visibility.

## Test boundary

Start with one annual release / selected capability records.

## Decision triggers

Incomplete / misleading record → MODIFY before publication.

## Transfer rule

The release framework can scale corridor-wide once data definitions are stable.

---

# Explicit test / validation scenario set

The following satisfy the taskbook intent for at least three test / validation scenarios and should be clearly marked in the formal package:

1. **S10 — AI-Native Service Sandbox / 大钟寺** — market + public-value validation.
2. **S11 — Full-Stack Capability Validation / 众智园** — lab-to-city technical / governance validation.
3. **S01 — Heat Refuge Network / 小月河** — real public-space environmental-service validation.
4. **S02 — Barrier-Free Route Companion** may serve as an additional high-value public-service validation scenario.

# Portfolio balance check

The final formal package should retain at least:

- 3 scenarios primarily serving vulnerable / inclusion needs;
- 2 mobility / access scenarios;
- 2 culture / public-life scenarios;
- 2 innovation / industry validation scenarios;
- 1 resilience / emergency scenario;
- 1 governance / transparency scenario.

Do not let the portfolio become 10 variations of a smart kiosk.
