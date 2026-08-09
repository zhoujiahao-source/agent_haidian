# Handoff — Long-Term Operations & Public Stewardship Agent

## 1. Repository state

- latest upstream observed at final audit refresh: `open-city-ai/haidian@d67795f2b72f074c491e2a1e9d21e21ba82f56dc` (2026-08-08T14:21:00Z)
- fork base at branch creation: `zhoujiahao-source/agent_haidian@5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1`
- branch: `agent/operations-stewardship`
- branch scope: `workstreams/operations_stewardship/**` only
- canonical `submissions/**`: intentionally untouched
- exact final branch HEAD: report externally after the final handoff commit/readback; a file cannot reliably embed the SHA of the commit that contains itself.

The upstream repository moved several times during this workstream (`b3d6fdaa…` → `e533da38…` → `d67795f2…`). The continuation pass therefore re-read mandatory current inputs rather than freezing the first snapshot.

## 2. What I completed

### Core required Window 6 deliverables

- Public Stewardship accountability model.
- RACI / role-responsibility matrix.
- independent Problem Track.
- independent Capability Track.
- developer ecosystem: Capability Registry, sandbox, interoperability, provenance, maintenance and deprecation.
- community rights and participation beyond surveys.
- continuous + Q1–Q4 annual operating calendar.
- annual City Learning Assembly centered on accountability rather than product exhibition.
- City Version Release with Added / Modified / Scaled / Responsible STOP / Retired / Suspended classes.
- Retired Capability Governance and public learning archive.
- 5/10/20-year technology-neutral roadmap.
- institutional risk register.
- phase checkpoints and final handoff.

### Additional closure work completed in the continuation pass

- completed the original Word manual's mandatory pre-read set at role-relevant depth: Skill, taskbook, allowed design space, site sources, source registry, planning limits, standards/index/reference snapshots, schemas, data workflow, review rubric, current geometry status and historical candidate evidence/validation assets;
- defined anti-gaming governance for the proposed `Urban Adaptation Rate` without inventing a present score;
- added current 2026 public-governance legal/regulatory screening boundary, explicitly not a legal opinion;
- audited the historical submission asset-by-asset for safe reuse;
- added a source/evidence register;
- mapped Window 6 into agent.1–agent.6, the three positioning themes, five functions and three-areas/two-wings operating logic;
- added five machine-readable integration templates;
- added explicit machine-readable workstream self-check and validation report;
- searched for an upstream duplicate Issue about the geometry-scoring wording problem and attempted Issue creation; GitHub returned 403 because the integration lacks upstream Issue-write access;
- attempted a blobless sparse local clone for runtime QA; the container could not resolve `github.com`, so connector readback + independent JSON parsing was used and the environment blocker is recorded.

## 3. Key decisions / findings

### A. Final accountability stays public

**Decision/finding:** public institutions must remain Accountable for rule-setting, authorization, data governance, public-value judgment, incident response and final `STOP / MODIFY / CONTINUE / SCALE / RETIRE` decisions. Experts, researchers, vendors, developers and community actors may supply evidence, review or maintenance but do not erase final public responsibility.

- confidence: high as a proposed design principle;
- Unknown: actual competent institution/legal delegation;
- consequence: never convert functional placeholder names into claims that a real organization has accepted a role.

### B. Two intake tracks converge on one public-value lifecycle

**Problem Track:** problem-first, baseline-first, solution-neutral and explicitly compares non-AI alternatives.

**Capability Track:** enables unsolicited social/technical innovation but requires proof of need, reversibility, data legitimacy, accessibility, interoperability, maintenance, vendor exit and sunset.

Both converge on evidence-based decisions rather than a permanent AI deployment pipeline.

### C. Community participation is a rights interface, not a survey program

Higher-impact capabilities require stronger notice, accessible/human alternatives, affected-group participation, objection/contestability and accountable human review. Window 6 participation mechanisms are supplementary governance interfaces and must not be described as substitutes for statutory hearings, planning approval or legal remedies.

### D. Annual operation must publish failure as well as success

City Version Release includes Responsible STOPs, incidents, retirements, unresolved problems, objections and evidence limitations as first-class outputs. The annual assembly is an accountability/release ritual, not an AI summit or product expo.

### E. Retirement is part of the architecture

Sunset conditions begin at admission. Retirement includes service continuity, authorization/notice, shutdown, credential/API cleanup, data disposition, physical-asset handling, registry tombstone and post-retirement verification, followed by a public learning archive.

### F. Long-term inheritance is technology-neutral

Preserve public accountability, rights, provenance, evidence, capability identity/history, migration and retirement. Intentionally allow models, vendors, clouds, sensors, robots, interfaces and software stacks to be replaced.

### G. UAR must not become an AI-deployment counter

Candidate governance formula:

`verified_improved_problem_records / evaluable_qualified_problem_records`

but the exact official formula/window/threshold is **not** decided by Window 6. Cohorts must be locked before outcomes; failures cannot disappear from the denominator; common safety/privacy/fairness/accessibility/environment/cost/override floors constrain every scenario. Responsible STOP is an important learning outcome but is not automatically counted as verified public-value improvement.

### H. Current repository wording requires maintainer clarification

Current Skill / review rubric / data workflow say organizer-missing official geometry itself must not block or penalize **content scoring**. `design_brief.json` still contains `provisional_boundary_blocks_formal_professional_scoring=true`, while site sources say provisional geometry is not usable for formal professional scoring.

This may intentionally distinguish:

1. content evaluation that should not punish organizer data gaps; and
2. precise geometry-dependent professional evidence that provisional polygons cannot support.

No matching Issue was found in targeted searches. An Issue was prepared and creation attempted, but GitHub returned `403 Resource not accessible by integration`. A contributor/maintainer with upstream Issue-write access should resolve the wording.

### I. Historical candidate is concept heritage, not current readiness proof

Safe to reuse after current integration: reversible trial logic, legibility/human alternative, public failure learning, developer/open-city concepts, provisional-data disclosures.

Do not reuse as proof: old manifest hashes, old self-check, old PR status, old visual/PDF readiness, or optimistic design-depth statuses.

Concrete reasons:

- old manifest `package_state=ready_for_review` but `validation_claim.self_checked=false`;
- old self-check has only five hand-authored checks;
- inspected old PR head has no recorded successful workflow/status contexts;
- required PNGs were anomalously tiny;
- A3/A0 PDFs were about 1.1 KB each and could not be visually page-inspected in the current connector environment;
- many design-depth items are `complete` while underlying official controls remain Unknown.

## 4. Files added or modified

### Required Window 6 set

| file | purpose | status |
|---|---|---|
| `public_stewardship.md` | institutional accountability / authorization model | complete |
| `role_responsibility_matrix.csv` | RACI / responsibility matrix | complete |
| `problem_track.md` | city problem intake / decision gates | complete |
| `capability_track.md` | social capability intake / lifecycle | complete |
| `developer_ecosystem.md` | registry / sandbox / version / maintenance / IP | complete |
| `community_rights.md` | notice / objection / contestability / human alternatives | complete |
| `participation_model.md` | participation beyond surveys | complete |
| `annual_calendar.md` | continuous + quarterly rhythm | complete |
| `annual_learning_assembly.md` | annual accountability/release assembly | complete |
| `city_version_release.md` | annual version-release process | complete |
| `retired_capability_governance.md` | sunset / decommission / archive | complete |
| `five_ten_twenty_years.md` | long-term institutional/technical evolution | complete |
| `institutional_risks.md` | institutional risk register | complete |
| `audit/checkpoints.md` | current rule/data audit + phases 0–9 | complete |
| `handoff.md` | integration handoff | complete |

### Additional closure / integration assets

| file | purpose | status |
|---|---|---|
| `metrics_governance.md` | UAR/common-floor/anti-gaming contract | complete |
| `public_governance_legal_boundary.md` | current legal/regulatory screening boundary | complete |
| `integration_crosswalk.md` | Window 6 → agent.1–6 / positioning / areas / proposal sections | complete |
| `audit/legacy_submission_audit.md` | safe/unsafe historical asset reuse | complete |
| `audit/source_evidence_register.csv` | source/status/use/license/limitation ledger | complete |
| `audit/workstream_self_check.json` | explicit role completion / blockers / N/A checks | complete |
| `audit/validation_report.md` | QA evidence and environment limitations | complete |
| `templates/problem_challenge.template.json` | problem record integration aid | complete |
| `templates/capability_proposal.template.json` | capability proposal integration aid | complete |
| `templates/capability_registry_record.template.json` | public capability registry integration aid | complete |
| `templates/city_version_release.template.json` | annual release integration aid | complete |
| `templates/retired_capability_record.template.json` | retirement/archive integration aid | complete |

All writes remain under `workstreams/operations_stewardship/`.

## 5. Sources / evidence status

Detailed ledger: `audit/source_evidence_register.csv`.

### Repository authority / mandatory context

- current upstream Skill;
- `design_brief.json`;
- `agent_taskbook.json` and local taskbook reference;
- `allowed_design_space.json`;
- site-package `sources.json`;
- `planning_limits.json`;
- standards registry + reference index + local reference snapshots;
- current schemas;
- `data/source_registry.json`;
- `docs/data-workflow.md`;
- `docs/review-rubric.md`;
- current provisional geometry directory.

### Official planning/standard context

- official competition announcement;
- MOHURD Urban Design Measures;
- MOHURD control-detailed-planning rules;
- MNR land-use classification guide.

The repository's architecture design-depth reference remains `missing_source_url`; it is a data gap.

### Current legal/regulatory screening — not project-specific conclusions

Recorded as of 2026-08-08:

- PRC Personal Information Protection Law;
- PRC Data Security Law;
- current Cybersecurity Law context (amendment effective 2026-01-01);
- algorithmic recommendation rules;
- interim generative-AI service measures;
- AI-generated/synthetic content labeling measures effective 2025-09-01;
- interim anthropomorphic AI interaction measures effective 2026-07-15;
- Accessible Environment Construction Law.

Applicability must be mapped to the actual future operator, service, user/data flow and sector. Window 6 does not issue a legal opinion, filing conclusion or deployment authorization.

### Comparative background only

- NIST AI RMF;
- OECD AI Principles;
- UK Algorithmic Transparency Recording Standard.

No third-party images, map tiles, models, proprietary datasets or copied external code were added by this workstream.

## 6. Data / design status

### Official

- project/task facts and area text values only to the extent supported by official/cleared repository sources.

### Verified

- inspected repository refs/files/statuses;
- required Window 6 files exist by branch readback;
- five JSON integration templates exist and their intended structures independently parse as JSON;
- historical validation/asset limitations stated above.

### Derived / Proposed

- Public Stewardship functional architecture;
- RACI;
- Problem/Capability Track gates;
- registry/sandbox/maintenance model;
- community-rights interfaces;
- annual calendar/assembly/release;
- UAR governance contract;
- retirement/archive;
- 5/10/20 roadmap;
- conceptual operating-role anchors for the three areas/two wings.

### Unknown

- actual competent institution(s);
- legal delegation/authorization route;
- real budget/staffing/procurement;
- final risk classes/thresholds;
- incident/appeal/retention SLAs;
- real community representation mechanism;
- actual future data categories;
- capability-specific legal filing/registration/security obligations;
- official exact SITE_BOUNDARY / KEY_AREA;
- missing statutory planning controls;
- whether any future capability will actually be deployed.

## 7. Conflicts / blockers / limitations

1. upstream wording distinction/conflict on provisional geometry and formal/content scoring;
2. upstream Issue creation blocked by connector permission (403);
3. local sparse clone blocked by container DNS (`Could not resolve host: github.com`);
4. historical A3/A0 visual inspection unavailable; metadata/file size warrants regeneration;
5. canonical submission formal preflight intentionally not run until all workstreams are integrated;
6. living upstream continues moving, so Final Integration must re-fetch `main` immediately before canonical work.

These are disclosed limitations, not hidden PASS claims.

## 8. Must adopt in Final Integration

- public institution retains final accountability;
- Problem Track + Capability Track converge on one public-value/risk lifecycle;
- non-AI comparator, reversibility, rollback and sunset are first-class fields;
- public notice, human/non-AI alternative, objection/contestability and affected-group review scale with impact;
- Capability Registry records owner/maintainer/risk/provenance/evidence/version/dependencies/interoperability/sunset;
- scenario metrics sit below common safety/privacy/fairness/accessibility/environment/cost/override floors;
- UAR measures verified public-value improvement, not deployments;
- Annual City Version Release publishes Responsible STOPs, incidents, objections, unresolved problems and retirements;
- retirement includes continuity + credential/data/device cleanup + registry tombstone + archive;
- 20-year inheritance is technology-neutral, allowing current AI stacks to be replaced;
- all unresolved authority/budget/legal/planning facts remain Proposed/Unknown.

## 9. Strong candidates

- proposed PSO / Professional Review Pool / Research & Evaluation Network functional decomposition;
- Q1 Diagnose → Q2 Sandbox/Authorize → Q3 Trial/Transfer → Q4 Evidence/Release rhythm;
- physical/digital Retired Capability Archive linked to Landmark-as-Memory;
- conceptual operating anchors: higher-risk testing at Zhongzhiyuan, community/developer co-design at AI Origin Community, public-facing service validation at Dazhongsi, ecosystem/interoperability support in Zhongguancun service wing, reversible scenario testing in Xiaoyuehe scenario wing;
- migration/replacement stress tests at 5/10/20-year milestones.

All area anchors remain conceptual, not parcel/property/operator commitments.

## 10. Exploratory only / Integration decides

- final overall proposal name;
- final institutional names;
- exact annual event/version name;
- exact risk categories/thresholds;
- exact UAR formula/window/effect threshold;
- community recruitment/compensation methods;
- future international learning network or named partners;
- specific software/API/vendor stack.

## 11. What I intentionally did NOT modify

- canonical or historical `submissions/**` files;
- official/locked geometry;
- repository validation scripts/schemas;
- another Agent's workstream;
- upstream source/rule files;
- government policy/procurement/legal documents.

## 12. Validation performed

- connector readback: Window 6 root/audit/templates exist;
- required original file set: complete;
- five intended JSON templates: independently parsed PASS;
- RACI core public-accountability mapping: inspected;
- mandatory pre-read: completed at role-relevant depth;
- historical package: audited for manifest/self-check/metrics/sources/geometry/presentation/matrices/PR status;
- latest upstream refreshed repeatedly during the session;
- current law/regulation sources screened and status-bounded;
- explicit self-check: `audit/workstream_self_check.json`;
- detailed QA: `audit/validation_report.md`.

**Formal canonical render/finalize/self-check/participant-preflight is not claimed.** It must be executed against the exact integrated submission head by Final Integration.

## 13. Final Integration sequence

1. fetch latest upstream `main` again;
2. install/read latest submission Skill and changed mandatory inputs;
3. resolve/document upstream geometry-scoring wording ambiguity;
4. integrate all Window workstreams into one canonical proposal architecture;
5. use `integration_crosswalk.md` to thread Window 6 through agent.1–agent.6 rather than appending it as an isolated chapter;
6. convert useful templates into the canonical package's existing schemas/records without pretending the templates are upstream schemas;
7. recalculate all geometry-dependent metrics from the actual integrated geometry;
8. regenerate figures/HTML/A3/A0 and bilingual companion assets required by current rules;
9. re-audit compliance/standard/design-depth matrix statuses row by row;
10. refresh manifest hashes using the current repository-supported method;
11. run current render → finalize → self-check → participant preflight `--check-push` and the current four review gate families;
12. fix every participant-controlled blocker before the real submission PR is opened/updated;
13. keep official/provisional/derived/proposed/assumed/unknown status visible in both human-readable and machine-readable outputs.

## 14. Window 6 completion verdict

**ROLE WORKSTREAM COMPLETE FOR FINAL INTEGRATION.**

This means the required Window 6 operations/public-governance research, design, machine-readable aids, audits and handoff are complete to the level supported by current repository/source access. It does **not** mean the overall urban-design submission is formally review-ready; that status belongs only to the exact canonical integrated package after current repository-native validation.