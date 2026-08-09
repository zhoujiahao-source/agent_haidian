# Persona Catalog

> These personas are design / evaluation archetypes, not claims about named real individuals. Final use should be grounded in public demographic / service evidence where available and should avoid stereotypes.

The set intentionally exceeds the official minimum of 5 personas.

# P01 — 通勤研究员 / Commuting Researcher

## Situation

Works / studies in the Zhongguancun–Jing-Zhang innovation ecosystem and crosses multiple transport / walking environments during peak hours.

## Needs

- reliable transfer information;
- clear walking / cycling continuity;
- fast transition between research / work and everyday city life;
- non-app fallback when digital services fail.

## Relevant scenarios

- S04 Morning Transfer Reliability
- S11 Full-Stack Capability Validation
- S12 City Version Public Review

## Design consequences

The Capability Backbone cannot be only a leisure route; it must support real weekday movement and connect knowledge / work destinations.

## Public-value checks

- travel-time reliability;
- accessible alternative-route availability;
- public / non-proprietary information access;
- no requirement to surrender unnecessary personal data for basic navigation.

---

# P02 — 社区老年居民 / Older Community Resident

## Situation

Lives near everyday public services and may use digital tools selectively but cannot be assumed to rely on a smartphone or AI interface.

## Needs

- human service remains available;
- shaded / comfortable rest and routes;
- legible public-space information;
- accessible transport / facilities;
- ability to refuse AI assistance without service penalty.

## Relevant scenarios

- S01 Heat Refuge Network
- S03 Elder Service Handoff
- S09 Public Facility Demand Balancer

## Design consequences

Every Public Capability Interface requires a credible non-AI path. Public-space design must work physically before digital optimization.

## Public-value checks

- Human Override Success Rate;
- digital opt-out parity;
- refuge / service accessibility;
- additional burden compared with digitally confident users.

---

# P03 — 轮椅使用者 / Wheelchair User

## Situation

Moves across station areas, roads, public spaces and facilities where one small barrier can invalidate an otherwise short route.

## Needs

- accurate, recently verified accessible routes;
- no “optimistic” AI route through an inaccessible segment;
- alternative human assistance;
- clear route state when construction / events change access.

## Relevant scenarios

- S02 Barrier-Free Route Companion
- S04 Morning Transfer Reliability
- S07 Emergency Public-Space Mode

## Design consequences

East–west stitching and north–south continuity must be tested as accessible paths, not only visual connections on a masterplan.

## Public-value checks

- false-safe-route rate;
- accessible-route completion;
- additional journey time;
- Human Override availability;
- emergency accessible-route continuity.

---

# P04 — 带儿童照护者 / Caregiver with Child

## Situation

Uses parks, public facilities, cultural routes and transport differently across weekdays / weekends and values safety, shade, toilets / rest and simple navigation more than visible technology.

## Needs

- child-friendly weekend public life;
- comfortable rest / heat refuge;
- predictable public facilities;
- ordinary public-space access even during programmed events.

## Relevant scenarios

- S01 Heat Refuge Network
- S05 Child-Friendly Weekend Mode
- S08 Railway Memory Companion
- S09 Public Facility Demand Balancer

## Design consequences

Scenario orchestration must not turn shared public space into single-group exclusive zones. Physical amenities remain more important than screens.

## Public-value checks

- public-space conflict / complaints;
- accessible family route coverage;
- thermal / rest coverage;
- non-digital information access.

---

# P05 — 大钟寺小型服务经营者 / Dazhongsi Small Service Operator

## Situation

Runs or experiments with a service in a mixed commercial / urban setting and may want to adopt AI but has limited capacity for complex compliance / infrastructure.

## Needs

- clear sandbox rules;
- temporary / reversible testing space;
- access to professional / technical support;
- transparent public-value criteria;
- fair opportunity rather than platform lock-in.

## Relevant scenarios

- S10 AI-Native Service Sandbox
- S12 City Version Public Review

## Design consequences

AI-native business should be represented as a governed urban-service ecosystem, not only flagship tech firms or high-end retail.

## Public-value checks

- public-need traceability;
- entry accessibility for smaller actors;
- vendor / platform lock-in risk;
- public-space externalities;
- service accessibility.

---

# P06 — 众智园青年开发者 / Young Developer at Zhongzhiyuan

## Situation

Can build / test technical capability but needs a disciplined route from prototype to real urban application.

## Needs

- clear test / validation pipeline;
- real public problem definitions;
- reusable public / cleared datasets;
- documentation / sandbox / audit support;
- recognition for contribution even when an experiment is stopped.

## Relevant scenarios

- S11 Full-Stack Capability Validation
- S10 AI-Native Service Sandbox
- S12 City Version Public Review

## Design consequences

Developer-community space must be tied to governance and real scenes. A hackathon without capability transfer / review is insufficient.

## Public-value checks

- evidence completeness;
- safe rollback readiness;
- capability transfer success;
- contribution traceability;
- failure documentation.

---

# P07 — 一线公共服务人员 / Frontline Public-Service Worker

## Situation

Receives escalations when AI fails, users refuse automation, or unusual cases require judgment.

## Needs

- clear Human Override workflows;
- tools that reduce rather than hide workload;
- visibility into why AI made a suggestion;
- authority to stop unsafe / inappropriate operation;
- training and fallback procedures.

## Relevant scenarios

- S03 Elder Service Handoff
- S07 Emergency Public-Space Mode
- S09 Public Facility Demand Balancer

## Design consequences

Human service space cannot be removed simply because a digital interface exists. Back-of-house / staff workflows belong in the urban-service design.

## Public-value checks

- escalation load;
- handoff success;
- override response time;
- unresolved-case backlog;
- worker-reported / observed workflow burden where responsibly measured.

---

# P08 — 京张文化访客 / Jing-Zhang Cultural Visitor

## Situation

Comes to understand the railway history and contemporary AI-city experiment, but should not need an app to understand the place.

## Needs

- physical historical evidence and place-based interpretation;
- clear distinction between history, current fact, design proposal and future experiment;
- accessible cultural routes;
- understandable city-version / learning archive.

## Relevant scenarios

- S08 Railway Memory Companion
- S12 City Version Public Review
- 1909 / 2026 / Future landmark sequence

## Design consequences

Landmark design must be legible as real place and material, not merely AR / screen content.

## Public-value checks

- source traceability;
- non-digital accessibility;
- correction / factual accuracy;
- accessible route continuity.

# Cross-persona design tests

Every final flagship scenario should answer:

1. Does it work for P02 if they refuse AI?
2. Does it work for P03 if the shortest route is inaccessible?
3. Does it disadvantage P05 relative to a large platform company?
4. Can P07 safely override it?
5. Does P08 understand which information is historical fact vs proposed future?
6. Does P01 still benefit during an ordinary weekday rather than a special event?
7. Does P04 retain ordinary public-space access during scenario programming?
8. Can P06 contribute without bypassing public-value review?

# Persona-to-area coverage

| Persona | 众智园 | AI 原点社区 | 大钟寺 | 中关村翼 | 小月河翼 / Backbone |
|---|---:|---:|---:|---:|---:|
| P01 Commuting Researcher | ✓ | ✓ |  | ✓ | ✓ |
| P02 Older Resident |  | ✓ |  |  | ✓ |
| P03 Wheelchair User |  | ✓ | ✓ |  | ✓ |
| P04 Caregiver with Child |  | ✓ |  |  | ✓ |
| P05 Small Service Operator |  |  | ✓ | ✓ |  |
| P06 Young Developer | ✓ |  | ✓ | ✓ |  |
| P07 Public-Service Worker |  | ✓ |  |  | ✓ |
| P08 Cultural Visitor |  |  | ✓ |  | ✓ |

The final package should avoid treating these as isolated stories. Their needs must change spatial, governance or metric decisions.
