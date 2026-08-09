# Operations Stewardship — Audit Baseline & Phase Checkpoints

Date: 2026-08-08
Role: WINDOW 6 — Long-Term Operations & Public Stewardship Agent
Status: conceptual governance workstream; **not** a government decision, statutory plan, implementation commitment, or canonical submission edit.

## Repository baseline

- Initial upstream inspected during this workstream: `open-city-ai/haidian@b3d6fdaa2331fdc60a3e618019fd8e6596532fff`.
- Continuation re-check observed upstream advance first to `e533da38c89c2766aee202b19b9d053057385ef6`, then to **`d67795f2b72f074c491e2a1e9d21e21ba82f56dc` (2026-08-08T14:21:00Z)**.
- Latest observed upstream merge at the final re-check changed another participant submission; no new exact official geometry was observed in the mandatory-input re-read.
- Fork working base at branch creation: `zhoujiahao-source/agent_haidian@5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1` on `main`.
- Work branch: `agent/operations-stewardship`.
- Current upstream submission Skill re-read during continuation; its core package/source/continuous-participation rules remained consistent with the initial workstream interpretation.
- Historical user proposal exists only on the older candidate branch inspected: `submission/zhoujiahao-source/jingzhang-legible-ai-belt/submissions/zhoujiahao-source/jingzhang-legible-ai-belt/`.
- This workstream does not edit that historical proposal or any canonical `submissions/**` path.

## Required-input audit

The continuation pass completed the original Word manual's mandatory pre-read set at role-relevant depth, including:

- `skills/urban-design-ai-submission/SKILL.md`;
- `brief/site-package/design_brief.json`;
- `brief/site-package/agent_taskbook.json` and its local reference snapshot;
- `brief/site-package/allowed_design_space.json`;
- `brief/site-package/sources.json`;
- `brief/site-package/ranges/planning_limits.json`;
- `brief/site-package/standards/standards.json`;
- `brief/site-package/standards/references/index.json` and all listed local reference Markdown files;
- `brief/site-package/schemas/*.json` relevant to package, metrics, matrices, GeoJSON, self-check, advisory review and formal scoring;
- `data/source_registry.json`;
- `docs/data-workflow.md`;
- `docs/review-rubric.md`;
- current `brief/site-package/geometry/` status;
- historical candidate `proposal.md`, metrics, sources, assumptions, manifest, self-check, geometry, figures, report/PDF metadata, matrices and PR/CI status.

### Rule / data findings

1. **Official geometry remains missing in the inspected mandatory geometry directory.** Current project geometry material remains provisional; no newly supplied exact official `SITE_BOUNDARY` / `KEY_AREA` was promoted by this workstream.
2. **Planning controls remain Unknown.** Current planning limits still mark FAR, height, building density, green ratio and setback as missing. This governance workstream therefore does not invent site-specific statutory thresholds.
3. **Current source policy remains strict.** Real public or explicitly cleared data, source tracing, ODbL attribution for OSM and no commercial map tiles as submission data remain required.
4. **Current Skill/rubric/data-workflow make organizer geometry gaps content-scoring tolerant.** Missing organizer-supplied official polygons do not by themselves block/penalize content scoring, while provisional geometry remains unsuitable for official redlines, precise geometry-dependent claims and formal use beyond its stated role.
5. **Repository-internal wording distinction/conflict retained for integration.** `design_brief.json` still contains `provisional_boundary_blocks_formal_professional_scoring=true`, and `sources.json` says provisional geometry is not usable for formal professional scoring, while Skill/rubric/data-workflow explicitly protect participant content scoring from organizer data gaps. This may be an intentional distinction between content scoring and geometry-dependent professional evidence, but the field wording can be misunderstood.
6. **Upstream collaboration was attempted.** Targeted searches found no duplicate Issue for this wording problem. An Issue creation attempt returned `403 Resource not accessible by integration`; therefore the item is permission-blocked and remains for a contributor/maintainer with write access.
7. **Historical operations assets are useful but insufficient.** The old proposal contains a reversible-pilot charter, public display of failed pilots, an Open City Week concept, developer co-creation, human takeover and non-AI alternatives. Window 6 expands these into durable public accountability, dual intake, rights, retirement, maintenance and 5/10/20-year institutional continuity.
8. **Historical validation is not current proof.** Its manifest says `ready_for_review` but `validation_claim.self_checked=false`; the old self-check contains only five checks; inspected PR/commit had no successful workflow/status evidence; figures/PDFs are anomalously small and require regeneration/visual review.
9. **Current schemas permit a custom UAR metric.** `metrics.schema.json` accepts custom metric keys when each metric carries status/value/unit/source files/formula/confidence/assumptions. Window 6 therefore defines UAR governance without fabricating a current score.
10. **Current review architecture is multi-gate.** Advisory review separates deterministic, spatial, visual and professional-evidence gates; a historical hand-authored self-check cannot replace them.
11. **Architecture design-depth source remains a data gap.** The repository reference for `MOHURD-ARCH-DESIGN-DEPTH-2016` still has `missing_source_url` and no authoritative body text; Window 6 does not upgrade it.
12. **Legal/governance screening has been refreshed to 2026-08-08.** Current national-level privacy/data/cybersecurity/AI-content/AI-service/accessibility sources were used only as screening context, not as project-specific legal conclusions.

## External comparative references — background only

These are used as comparative governance patterns, not as project law or claimed local policy:

- NIST AI Risk Management Framework 1.0 / Playbook: lifecycle risk governance; Govern–Map–Measure–Manage; explicit proceed/not-proceed decisions; ongoing risk management.
- OECD AI Principles (updated 2024): human agency/oversight, transparency, traceability, ability to challenge outputs, safe override/repair/decommission, lifecycle accountability.
- UK Algorithmic Transparency Recording Standard: a concrete public-sector pattern for standardized, accessible disclosure of algorithmic tools with public effect.

All local institutional names and procedures in this workstream are therefore marked **Proposed** unless directly sourced from the project brief/taskbook.

## Current legal-screening references — project applicability not presumed

The continuation pass records current national-level screening sources in `audit/source_evidence_register.csv` and `public_governance_legal_boundary.md`, including PIPL, Data Security Law, the current Cybersecurity Law context, algorithmic recommendation rules, generative-AI measures, AI-generated/synthetic content labeling, anthropomorphic AI interaction measures effective 2026-07-15, and the Accessibility Environment Construction Law.

These are used to identify **questions that must be answered for a real capability**. They do not establish that a hypothetical capability is legal, registered, approved, exempt, or deployable.

## Phase checkpoints

### Phase 0 — operations task audit
- Completed: latest upstream/fork state, full mandatory pre-read, Skill, taskbook, source/geometry constraints, schemas, standard snapshots, historical proposal/evidence/validation assets.
- Finding: operations must move from event branding toward a public stewardship operating system.
- Unknown: actual competent government bodies, statutory authorization routes, budgets, staffing and procurement authority.
- Dependency: Final Integration Agent must preserve conceptual-status language.

### Phase 1 — Public Stewardship roles
- Completed in `public_stewardship.md` and `role_responsibility_matrix.csv`.
- Finding: external experts can review, but final public accountability cannot be outsourced.
- Unknown: actual institutional host and legal delegation.

### Phase 2 — Problem Track
- Completed in `problem_track.md` plus `templates/problem_challenge.template.json`.
- Finding: every challenge begins with a real baseline/public-value objective and non-AI alternatives, not an AI procurement request.

### Phase 3 — Capability Track
- Completed in `capability_track.md` plus `templates/capability_proposal.template.json`.
- Finding: unsolicited innovation must prove need, reversibility, maintenance, interoperability and sunset before trial.

### Phase 4 — developer ecosystem
- Completed in `developer_ecosystem.md` plus `templates/capability_registry_record.template.json`.
- Finding: a Capability Registry plus compatibility/deprecation contract is more durable than event-based developer recruitment.

### Phase 5 — community rights
- Completed in `community_rights.md` and `participation_model.md`.
- Finding: participation requires objection, human alternative, affected-group review and public observer roles, not surveys alone; exact statutory remedy route remains Unknown.

### Phase 6 — annual operating calendar
- Completed in `annual_calendar.md` and `annual_learning_assembly.md`.
- Finding: the annual assembly is an accountability/release ritual, not an AI expo.

### Phase 7 — City Version Release
- Completed in `city_version_release.md`, `metrics_governance.md` and `templates/city_version_release.template.json`.
- Finding: release notes must include STOPs, incidents, retirements, unresolved problems and evidence links as first-class items; UAR must measure verified public-value improvement, not deployment count.

### Phase 8 — Retired Capability Governance
- Completed in `retired_capability_governance.md` plus `templates/retired_capability_record.template.json`.
- Finding: sunset is designed at admission; retirement includes data/credential/device cleanup plus a public learning record.

### Phase 9 — 5/10/20 years
- Completed in `five_ten_twenty_years.md` and linked through `integration_crosswalk.md`.
- Finding: long-term inheritance is a technology-neutral Urban Capability Exchange Network, not today's models/hardware.

## QA / validation checkpoints

- Required Window 6 file set: present by connector readback.
- Five machine-readable integration templates: present by connector readback.
- Intended structures of all five templates: independently parsed as valid JSON.
- RACI public-accountability principle: preserved.
- Legacy asset/validation reuse boundary: documented in `audit/legacy_submission_audit.md`.
- Source/provenance ledger: documented in `audit/source_evidence_register.csv`.
- Explicit YES/NO/Unknown/N/A self-check: `audit/workstream_self_check.json`.
- Validation evidence and environment blockers: `audit/validation_report.md`.
- Blobless sparse local clone: attempted, but container DNS could not resolve `github.com`; no false runtime PASS claimed.
- Canonical formal submission preflight: intentionally not run because Window 6 did not edit the canonical submission and only Final Integration may do so.

## Deliberate scope boundary

No government, university, company, community group or auditor is claimed to have accepted any role. No budget, staffing level, SLA, statutory risk class, hearing procedure, procurement route, data-retention period or incident threshold is represented as official. Those remain integration/implementation questions for competent human institutions.