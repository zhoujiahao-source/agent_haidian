# Handoff — Long-Term Operations & Public Stewardship Agent

## 1. Repository state

- upstream ref: `open-city-ai/haidian@b3d6fdaa2331fdc60a3e618019fd8e6596532fff` inspected 2026-08-08
- fork base ref: `zhoujiahao-source/agent_haidian@5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1` (`main` at branch creation)
- branch: `agent/operations-stewardship`
- pre-handoff branch head: `806cfb0b09f6efaaf61d54f0bc64d61114e236d2`
- final commit SHA: **use the branch HEAD containing this file / final Agent report**. A Git commit cannot reliably contain its own SHA because the file contents participate in the hash; the exact post-handoff SHA is therefore intentionally reported outside this self-referential field.

## 2. What I completed

- Audited current upstream Skill/rules, geometry status, source policy, review rubric and historical user proposal operations assets.
- Defined a Public Stewardship accountability model and RACI matrix.
- Defined independent Problem Track and Capability Track admission/exit/decision logic.
- Defined durable developer ecosystem: Capability Registry, sandbox, attribution, interoperability, maintenance and deprecation.
- Defined community rights: notice, human route, objection, contestability, accessibility, collective representation, vulnerable-group review and observer interfaces.
- Defined participation beyond surveys with traceable response-to-feedback.
- Defined continuous + Q1–Q4 annual operating calendar.
- Reframed the annual gathering as Jing-Zhang City Learning Assembly centered on accountability and City Version Release, not an AI expo.
- Defined Annual City Version Release with Added / Modified / Scaled / Responsible STOP / Retired / Suspended classes.
- Defined Retired Capability Governance from sunset-at-admission through credential/data/device cleanup, registry tombstone and public learning archive.
- Defined 5/10/20-year roadmap toward a technology-neutral Urban Capability Exchange Network.
- Added institutional risk register covering deployment treadmill, vendor capture, accountability dilution, participation theater, metric gaming, maintenance debt, unsafe retirement, lock-in and event capture.

## 3. Key decisions / findings

### Finding A — final accountability stays public
- decision/finding: Public institutions must remain Accountable for rule-setting, authorization, data governance, public-value judgment, incidents and final SCALE/STOP/RETIRE decisions. Experts/researchers/vendors/community contribute evidence and review but do not erase final public responsibility.
- evidence: project locked decision `Public Stewardship`; current taskbook/brief public-interest requirements; comparative NIST/OECD accountability patterns.
- confidence: high as a design principle; actual competent institution Unknown.
- why it matters: prevents responsibility being outsourced to a vendor, model supplier or advisory committee.

### Finding B — dual intake must converge on one public-value/risk lifecycle
- decision/finding: Problem Track is problem-first and solution-neutral; Capability Track allows unsolicited innovation but requires proof of need, non-AI comparison, reversibility, data legitimacy, maintenance and sunset. Both converge on STOP/MODIFY/CONTINUE/SCALE.
- evidence: locked two-track decision plus role-specific prompt requirements.
- confidence: high as proposed design.
- why it matters: preserves innovation without creating a vendor bypass around public need.

### Finding C — community participation is a rights interface
- decision/finding: higher-impact capabilities need objection/appeal/human alternative/affected-group review, not only feedback forms.
- evidence: prompt public-interest/governance requirements; OECD transparency/challenge/override principles as comparative background.
- confidence: high as design direction; exact legal remedy route Unknown.
- why it matters: makes Human Override and public accountability operational.

### Finding D — annual assembly must publish failures and unresolved problems
- decision/finding: City Learning Assembly centers on City Version Release. Responsible STOPs, incidents, retirements, objections and unresolved problems are first-class outputs.
- evidence: locked Annual City Version Release + Retired Capability Archive decisions.
- confidence: high.
- why it matters: avoids AI-summit/product-expo drift and creates durable civic memory.

### Finding E — retirement is part of architecture, not cleanup after abandonment
- decision/finding: sunset conditions are recorded at admission; retirement includes service continuity, authorization/notice, shutdown, credential/data/device disposition, registry tombstone and post-retirement verification.
- evidence: locked retirement mechanism plus OECD safe decommissioning principle as comparative background.
- confidence: high as operational design; exact retention/security procedures Unknown.
- why it matters: prevents orphaned infrastructure, lingering access and institutional amnesia.

### Finding F — 20-year target is technology-neutral
- decision/finding: preserve public accountability, rights, capability identity/history, evidence and retirement; intentionally replace models, vendors, sensors, interfaces and software stacks.
- evidence: locked Urban Capability Exchange Network decision.
- confidence: high.
- why it matters: protects the concept from being frozen around 2026 AI technology.

### Finding G — current repository has a rule wording conflict
- decision/finding: current Skill and `docs/review-rubric.md` state that organizer-missing official geometry itself does not block content scoring; `design_brief.json` still contains `provisional_boundary_blocks_formal_professional_scoring=true`.
- evidence: latest inspected upstream files.
- confidence: high that wording differs; repository maintainers/Integration should decide canonical interpretation.
- why it matters: avoid silently turning a data gap into a participant content failure.

## 4. Files added or modified

| file | purpose | status |
|---|---|---|
| `audit/checkpoints.md` | rule/data audit and Phase 0–9 checkpoints | complete |
| `public_stewardship.md` | institutional accountability and authorization model | complete |
| `role_responsibility_matrix.csv` | RACI / responsibility matrix | complete |
| `problem_track.md` | city problem intake and decision gates | complete |
| `capability_track.md` | social capability proposal intake and lifecycle | complete |
| `developer_ecosystem.md` | registry/sandbox/version/maintenance/IP ecosystem | complete |
| `community_rights.md` | rights, objection, appeal, human alternatives | complete |
| `participation_model.md` | participation beyond surveys | complete |
| `annual_calendar.md` | continuous + quarterly operating rhythm | complete |
| `annual_learning_assembly.md` | annual accountability/release assembly | complete |
| `city_version_release.md` | annual version-release schema/process | complete |
| `retired_capability_governance.md` | sunset/decommission/archive governance | complete |
| `five_ten_twenty_years.md` | long-term institutional/technical evolution | complete |
| `institutional_risks.md` | institutional risk register and mitigations | complete |
| `handoff.md` | integration handoff | complete |

All writes are confined to `workstreams/operations_stewardship/` on the role branch. No canonical `submissions/**` file was modified.

## 5. Sources and licenses

### Repository sources / rule inputs
- Current upstream Skill: `skills/urban-design-ai-submission/SKILL.md`, blob `0b6a9b1b7360f4d112f48fa4c54a9f137420c763` — project operating rule, latest inspected upstream.
- `brief/site-package/design_brief.json`, blob `f30f7f855c093f81252cb82c624c0d8b4466683c` — project/site/task structure; contains the noted geometry-scoring wording conflict.
- `brief/site-package/allowed_design_space.json`, blob `b2aec48767766b2b233a0c11c37f16127dc667f2` — real/public data, provisional geometry, locked/editable layer and forbidden-claim policy.
- `brief/site-package/ranges/planning_limits.json`, blob `1daf654ff6c0c74ddfaf6e56cc994d8b3c47f1c4` — official area text values and missing planning controls.
- `brief/site-package/standards/standards.json`, blob `06cd221a1ce76c51d8260dbab2c9e9f34fc64149` — standard/source-status registry.
- `data/source_registry.json`, blob `faa574fb801e26009690c7bc54389c257ada3e3a` — formal/background/provisional source-use boundaries.
- `docs/review-rubric.md`, blob `30e6f6fa88fd3f2d22558330b5ef387749d340b8` — review dimensions, public-interest/long-term-operation criteria and geometry-content-scoring language.
- `brief/site-package/visual_style_recommendations.json`, blob `00b63a30a3bf61ecd9d502de115566d32c5efc9d` — visual evidence/anti-pattern context.
- `brief/site-package/geometry/` — only provisional geometry assets were found in latest inspection; no new official `SITE_BOUNDARY`/`KEY_AREA` files.
- Historical user proposal: `submission/zhoujiahao-source/jingzhang-legible-ai-belt/submissions/zhoujiahao-source/jingzhang-legible-ai-belt/proposal.md`, blob `62a5095ed3f5d248745a77d8097c186bf73cbd09` — reused only as audited concept heritage, not as current authority.

### External comparative governance sources — background only
- NIST, AI Risk Management Framework 1.0 / Playbook — https://www.nist.gov/itl/ai-risk-management-framework — voluntary, cross-sector risk-management reference; used for lifecycle/govern-map-measure-manage patterns, not local law.
- OECD AI Principles, updated 2024 — https://www.oecd.org/en/topics/ai-principles.html — intergovernmental principles; used for human oversight, transparency, challenge, safe decommissioning and accountability patterns.
- UK Government, Algorithmic Transparency Recording Standard guidance/hub — https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub — public-sector disclosure pattern; used only as comparative design inspiration.

Licensing/reuse: no third-party images, code, map tiles or datasets were added by this workstream. External sources are referenced as public background links and paraphrased at principle level.

## 6. Data / design status

- Official: project/task texts and area values only to the extent supported by repository official/cleared sources; no new official geometry discovered.
- Verified: latest inspected repository states, branch existence, historical proposal path/content, current workstream files.
- Derived: this Agent's governance architecture, RACI, lifecycle gates, calendar, release/retirement schema and long-term roadmap.
- Assumed: functional placeholder institutions such as `Public Stewardship Office`, review pools, observer mechanisms and future registry operations are proposed organizational interfaces.
- Unknown: actual competent public institution(s), legal authority, staffing, budget, procurement route, formal risk classes/thresholds, appeal deadlines, data-retention periods, SLA, community representation/recruitment method, official geometry and missing statutory planning controls.

## 7. Conflicts or risks

- Current Skill/rubric vs `design_brief.json` wording on the effect of missing official geometry on content/professional scoring.
- Fork `main` was behind the latest upstream commit at work start; this branch intentionally preserves the user's `main` base while auditing the newer upstream rules instead of silently rewriting unrelated fork content.
- Historical `Jing-Zhang Legible AI Belt` proposal is reusable but its operations layer is event/pilot-heavy relative to the new City OS/Public Stewardship constitution.
- The proposed PSO/review-pool names must not be converted into claims that real institutions already exist or agreed to participate.
- Exact numeric risk/incident/appeal/retention thresholds must not be invented during integration.
- City Version Release and Learning Assembly will lose their differentiating value if failures, STOPs, retirements and unresolved objections are removed for promotional reasons.

## 8. What the Final Integration Agent should adopt

### Must adopt
- final public accountability remains with public institutions;
- Problem Track + Capability Track converge on one risk/public-value lifecycle;
- non-AI alternatives and sunset/rollback are required fields;
- community objection/appeal/human-alternative and vulnerable-group mechanisms scale with impact;
- Capability Registry records owner, maintainer, risk, provenance, evidence, version, dependency, interoperability and sunset;
- Annual City Version Release includes Responsible STOPs, incidents, retirements and unresolved problems;
- retirement includes data/credential/device cleanup + continuity + archive;
- 20-year target is technology-neutral Urban Capability Exchange Network.

### Strong candidate
- the proposed PSO / Professional Review Pool / Research & Evaluation Network functional decomposition;
- Q1 diagnose → Q2 sandbox/authorize → Q3 trial/transfer → Q4 evidence/release calendar;
- physical-first Retired Capability Archive tied to Landmark as Memory;
- migration/replacement stress tests at 5/10/20-year milestones.

### Exploratory only
- exact name of annual event/version;
- exact organizational names;
- exact participation formats, recruitment/compensation rules;
- any future international city-learning network until real partners are verified.

## 9. What I intentionally did NOT modify

- any canonical `submissions/**` path;
- historical user submission branch contents;
- geometry, metrics, figures, PDF/HTML deliverables;
- official/locked layers;
- repository validation scripts or schemas;
- any other Agent workstream;
- upstream repository files;
- actual government policy, procurement or legal documents.

## 10. Validation performed

- command/check: GitHub branch readback of `workstreams/operations_stewardship/` on `agent/operations-stewardship`.
- result: expected role files/directories returned with Git blob SHAs; no canonical submission writes observed in this workstream.
- command/check: direct readback of `role_responsibility_matrix.csv` from the role branch.
- result: header and all responsibility rows returned as UTF-8 CSV; public institution is consistently Accountable for core public decisions while other actors retain R/C roles.
- command/check: rule cross-check against latest Skill, allowed design space, planning limits, source registry, review rubric and geometry directory.
- result: workstream wording keeps official/verified/derived/assumed/unknown distinctions, avoids official-approval claims, preserves provisional-geometry limitations and records the identified rule conflict.
- formal submission preflight: **not run / not claimed**, because this Agent intentionally did not modify the canonical formal submission package.

## 11. Non-blocking next actions for Integration

1. Re-fetch upstream `main` immediately before integration; it is a living repository.
2. Decide how to document or escalate the geometry-scoring wording conflict.
3. Map proposed functional public-stewardship roles to real competent institutions only if authoritative evidence becomes available.
4. Integrate governance diagrams/summary into the final proposal without turning concepts into claimed government commitments.
5. Coordinate with metrics workstream on the exact Urban Adaptation Rate formula and anti-gaming denominator.
6. Coordinate with spatial/visual workstreams so Capability Backbone, Public Capability Interface, Landmark as Memory and Retired Capability Archive have legible spatial counterparts.
7. After canonical integration, run the full latest Skill render/finalize/self-check/participant-preflight sequence.