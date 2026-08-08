# Public Governance Legal Boundary｜公共治理法律与合规筛查边界

> Review date: **2026-08-08**. Status: **screening framework, not legal opinion**. Applicability depends on the actual capability, operator/provider role, data, users, deployment context and competent authority. Professional legal review is required before any real public deployment, procurement, filing, appeal design, retention rule or rights-affecting automation.

## 1. Why this file exists

Window 6 proposes institutional accountability, community rights, human override, public notice, incident handling and retirement. These are governance-design interfaces. They must not be presented as substitutes for applicable law, statutory planning procedures, regulatory filing/registration, sector-specific authorization or judicial/administrative remedies.

The operating principle is:

**governance concept → determine actual operator/service/data → legal applicability mapping → required professional/authority review → authorization → bounded operation.**

## 2. Current national-level screening map

| source | current relevance to a capability | operational screening question | boundary for this workstream |
|---|---|---|---|
| Personal Information Protection Law of the PRC (PIPL) | Personal-information processing, rights, sensitive information, automated decision-making and related processor obligations | Does the capability process identifiable or identifiable-by-combination personal information; what purpose, necessity, scope and rights route apply? | Window 6 does not invent a lawful basis, consent model, retention period or automated-decision compliance conclusion. |
| Data Security Law of the PRC | Data-processing lifecycle and data-security responsibilities | What data is collected/stored/used/transmitted/provided; what classification, security and incident responsibilities apply? | `public/cleared` project evidence rules do not automatically answer operational data-law obligations. |
| Cybersecurity Law of the PRC, as amended in 2025 and effective 2026-01-01 | Network operation/security obligations and the current national framework's express AI development/risk-governance context | Does the service constitute a network/operator context with security, incident, protection or other duties? | Exact cybersecurity level/filing/technical controls remain capability-specific and Unknown here. |
| Provisions on the Administration of Algorithmic Recommendations in Internet Information Services | Applies when the actual internet information service falls within regulated algorithm-recommendation functions | Does the public service use generation/synthesis, personalized push, ranking/selection, search filtering, scheduling/decision or other covered recommendation functions? | Do not assume every urban AI capability is an algorithmic-recommendation service; scope must be assessed. |
| Interim Measures for the Management of Generative Artificial Intelligence Services | Public-facing generative-AI services within the Measures' scope | Is the capability providing generative-AI services to the public in China; what provider/data/content/security requirements and filing/registration practice apply? | A model call embedded in a city tool is not automatically enough to reach a legal conclusion; provider/service architecture matters. |
| Measures for Labeling AI-Generated and Synthetic Content, effective 2025-09-01 | Explicit/implicit labeling of generated/synthetic content in covered services/content | Does the capability generate/synthesize content subject to labeling and metadata requirements? | Labeling design belongs in the capability record when applicable; Window 6 does not claim all outputs require one identical label. |
| Interim Measures for the Management of Anthropomorphic AI Interactive Services, effective 2026-07-15 | Current 2026 rules for covered anthropomorphic AI interaction services | Does the capability simulate human personality/emotion/relationship interaction in a way covered by the Measures? | Only triggered when the actual service fits scope; do not generalize to ordinary agents, kiosks or automation. |
| Law on Building an Accessible Environment | Accessible facilities, information and services for persons with disabilities, older adults and other persons with accessibility needs | Can the public-facing capability, notice, complaint route and human/non-AI alternative be used accessibly? | Accessibility is a design and rights floor; exact compliance method still needs relevant professional review. |

## 3. Official source register for this screening

The following official public sources were inspected for current screening context. They are not bundled or reproduced in the workstream.

- Personal Information Protection Law of the PRC — National People's Congress: `https://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html`
- Data Security Law of the PRC — National People's Congress: `https://www.npc.gov.cn/npc/c2/c30834/202106/t20210610_311888.html`
- Cybersecurity Law current consolidated/amended context — Cyberspace Administration of China: `https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm`
- Algorithmic Recommendation Provisions — Cyberspace Administration of China: `https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm`
- Interim Measures for Generative AI Services — Cyberspace Administration of China: `https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm`
- AI-Generated/Synthetic Content Labeling Measures — Cyberspace Administration of China: `https://www.cac.gov.cn/2025-03/14/c_1743654685899683.htm`
- Interim Measures for Anthropomorphic AI Interactive Services — Cyberspace Administration of China: `https://www.cac.gov.cn/2026-04/10/c_1777558395078289.htm`
- Law on Building an Accessible Environment — official legal-publication mirror of the Supreme People's Procuratorate: `https://www.spp.gov.cn/spp/fl/202306/t20230628_618991.shtml`

If any URL or rule changes, Final Integration must re-check current official sources rather than relying on this dated screening snapshot.

## 4. Capability legal-screening record — minimum questions

Before a real trial, the accountable operator should map at least:

1. **Operator/provider identity:** who is the real public owner, technical operator, data processor/controller-equivalent role, model/API provider and maintainer?
2. **Purpose and necessity:** what public function is being performed and why is each data element/function necessary?
3. **Data categories:** public/open data, personal information, sensitive personal information, children's information, operational/security data, possible important data or other regulated classes.
4. **Collection/source/provenance:** where did the data come from, under what authorization, and can the purpose change?
5. **Retention and cleanup:** what rule controls storage, deletion, archival, model/log retention and retirement cleanup?
6. **Automated outcome:** does the capability materially recommend, rank, restrict, allocate or decide something affecting a person; what human review/contestability is legally and operationally required?
7. **Public AI service scope:** do algorithmic recommendation, generative-AI, content-labeling, anthropomorphic-interaction or other AI-service rules apply?
8. **Filing/registration/security assessment:** is any current filing, registration, security assessment or model/service disclosure triggered? Determine from the actual service architecture and current regulator guidance.
9. **Cross-border / external transfer:** is data transferred or made available outside the relevant jurisdiction; what rules apply?
10. **Cybersecurity and incident chain:** what security controls, logs, reporting/escalation and continuity obligations apply?
11. **Accessibility and human route:** is the public service, notice, objection and fallback route accessible and genuinely usable?
12. **Sector-specific law:** transport, health, education, finance, employment, public security, minors, consumer protection, mapping/geospatial, radio/device safety, procurement and other sectors may add requirements.
13. **Planning/public-space authority:** does a physical deployment require planning, property, heritage, road, fire, utility, park, construction, event or other competent approval?
14. **Complaint/appeal route:** what statutory administrative, supervisory, consumer, civil or other remedy actually applies? Do not substitute a project feedback form for a legal remedy.

## 5. Relationship to Public Stewardship

`Public Stewardship Office (PSO)` and other names in this workstream are **functional placeholders only**. They are not asserted to be existing competent authorities and are not claimed to satisfy any statutory allocation of power.

The intended relationship is:

- statutory/competent authorities retain powers given by law;
- the proposed stewardship layer organizes evidence, ownership, risk review, notice, maintenance and public memory;
- where law sets a stronger procedure, threshold, notice, hearing, authorization or remedy, the legal requirement prevails;
- where the concept proposes stronger transparency or reversibility without conflicting with law, it may be retained as a design safeguard after professional review.

## 6. Planning and public participation boundary

Repository reference snapshots show that formal urban-design/control-detailed-planning processes have their own responsible authorities, public-comment/consultation and approval procedures. Window 6's workshops, observers, objections and co-evaluation are **not** described as statutory hearings, approvals or legally sufficient public participation.

For Final Integration, use language such as:

- `Proposed community participation interface`
- `supplementary operating feedback and contestability route`
- `subject to statutory planning/public-consultation procedures where applicable`

Avoid language such as:

- `this fulfills the statutory public hearing requirement`
- `PSO approves the regulatory plan`
- `community vote authorizes deployment`

unless an identified competent legal basis actually supports it.

## 7. Current 2026 implementation watchpoints

As of this review date, two particularly time-sensitive issues should be re-checked immediately before any real implementation:

- AI-generated/synthetic-content labeling rules have been effective since **2025-09-01** and may affect public-facing generated content.
- the interim measures for covered anthropomorphic AI interactive services became effective **2026-07-15** and are therefore current, not a future proposal.

Current regulator filing/registration practice for public generative-AI services should also be checked against the exact provider/model/application architecture at deployment time. A repository concept cannot pre-approve this.

## 8. Unknowns that must stay Unknown

Window 6 does not know and must not invent:

- the project's final competent authority or interdepartmental allocation;
- the final procurement/legal entity;
- the legal basis for any specific personal-information operation;
- actual data categories used by future capabilities;
- retention/deletion periods;
- filing/registration obligations for an unspecified future service;
- cross-border transfer mechanism;
- statutory appeal authority or response deadline;
- sector-specific licenses/permits;
- security level, assessment result or certification;
- whether a future capability is legally deployable.

These remain explicit pre-deployment gates.