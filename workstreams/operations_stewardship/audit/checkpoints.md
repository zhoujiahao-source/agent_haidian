# Operations Stewardship — Audit Baseline & Phase Checkpoints

Date: 2026-08-08
Role: WINDOW 6 — Long-Term Operations & Public Stewardship Agent
Status: conceptual governance workstream; **not** a government decision, statutory plan, implementation commitment, or canonical submission edit.

## Repository baseline

- Latest upstream inspected: `open-city-ai/haidian@b3d6fdaa2331fdc60a3e618019fd8e6596532fff` (2026-08-08T13:17:04Z).
- Fork working base: `zhoujiahao-source/agent_haidian@5481e2d1be4cba7ec45b3b5a97fb9c38e2a6f5f1` on `main`.
- Work branch: `agent/operations-stewardship`.
- Current upstream submission Skill inspected: `skills/urban-design-ai-submission/SKILL.md`, blob `0b6a9b1b7360f4d112f48fa4c54a9f137420c763`.
- Historical user proposal exists only on the older candidate branch inspected: `submission/zhoujiahao-source/jingzhang-legible-ai-belt/submissions/zhoujiahao-source/jingzhang-legible-ai-belt/`.
- This workstream does not edit that historical proposal or any canonical `submissions/**` path.

## Required-input audit

Inspected current upstream materials relevant to this role, including the latest Skill, `design_brief.json`, `agent_taskbook.json`, `allowed_design_space.json`, `planning_limits.json`, `standards.json`, source registry, review rubric, visual recommendations, geometry directory, and the old proposal's operations section.

### Rule / data findings

1. **Official geometry remains missing.** `brief/site-package/geometry/` currently contains `provisional_boundaries.geojson`, its basis note, and `study_area_bbox.geojson`; no newly supplied official `SITE_BOUNDARY` / `KEY_AREA` files were found.
2. **Planning controls remain Unknown.** Current planning limits still mark FAR, height, building density, green ratio and setback as missing. This governance workstream therefore does not invent site-specific statutory thresholds.
3. **Current source policy remains strict.** Real public or explicitly cleared data, source tracing, ODbL attribution for OSM, and no commercial map tiles as submission data remain required.
4. **Current Skill makes content scoring geometry-tolerant.** It states that missing organizer-supplied official polygons do not by themselves block content scoring, while provisional geometry must remain clearly labeled and recalculated when official data arrives.
5. **Repository-internal wording conflict retained for integration.** `design_brief.json` still contains `provisional_boundary_blocks_formal_professional_scoring=true`, while the current Skill and `docs/review-rubric.md` state that organizer-missing official geometry itself must not block content scoring. This workstream does not silently resolve that conflict; Integration should follow the current Skill/rubric for participant workflow and flag the stale field for repository maintainers if necessary.
6. **Historical operations assets are useful but insufficient.** The old proposal contains a roughly 100-day reversible pilot charter, public display of failed pilots, an Open City Week concept, developer co-creation, human takeover and non-AI alternatives. Window 6 expands these into durable public accountability, dual intake, rights, retirement, maintenance and 5/10/20-year institutional continuity.

## External comparative references — background only

These are used as comparative governance patterns, not as project law or claimed local policy:

- NIST AI Risk Management Framework 1.0 / Playbook: lifecycle risk governance; Govern–Map–Measure–Manage; explicit proceed/not-proceed decisions; ongoing risk management.
- OECD AI Principles (updated 2024): human agency/oversight, transparency, traceability, ability to challenge outputs, safe override/repair/decommission, lifecycle accountability.
- UK Algorithmic Transparency Recording Standard: a concrete public-sector pattern for standardized, accessible disclosure of algorithmic tools with public effect.

All local institutional names and procedures in this workstream are therefore marked **Proposed** unless directly sourced from the project brief/taskbook.

## Phase checkpoints

### Phase 0 — operations task audit
- Completed: latest upstream/fork state, Skill, taskbook, source/geometry constraints, historical proposal operations assets.
- Finding: operations must move from event branding toward a public stewardship operating system.
- Unknown: actual competent government bodies, statutory authorization routes, budgets, staffing and procurement authority.
- Dependency: Final Integration Agent must preserve conceptual-status language.

### Phase 1 — Public Stewardship roles
- Completed in `public_stewardship.md` and `role_responsibility_matrix.csv`.
- Finding: external experts can review, but final public accountability cannot be outsourced.
- Unknown: actual institutional host and legal delegation.

### Phase 2 — Problem Track
- Completed in `problem_track.md`.
- Finding: every challenge begins with a real baseline/public-value objective and non-AI alternatives, not an AI procurement request.

### Phase 3 — Capability Track
- Completed in `capability_track.md`.
- Finding: unsolicited innovation must prove need, reversibility, maintenance, interoperability and sunset before trial.

### Phase 4 — developer ecosystem
- Completed in `developer_ecosystem.md`.
- Finding: a Capability Registry plus compatibility/deprecation contract is more durable than event-based developer recruitment.

### Phase 5 — community rights
- Completed in `community_rights.md` and `participation_model.md`.
- Finding: participation requires objection, appeal, human alternative, vulnerable-group review and public observer roles, not surveys alone.

### Phase 6 — annual operating calendar
- Completed in `annual_calendar.md` and `annual_learning_assembly.md`.
- Finding: the annual assembly is an accountability/release ritual, not an AI expo.

### Phase 7 — City Version Release
- Completed in `city_version_release.md`.
- Finding: release notes must include STOPs, incidents, retirements, unresolved problems and evidence links as first-class items.

### Phase 8 — Retired Capability Governance
- Completed in `retired_capability_governance.md`.
- Finding: sunset is designed at admission; retirement includes data/credential/device cleanup plus a public learning record.

### Phase 9 — 5/10/20 years
- Completed in `five_ten_twenty_years.md`.
- Finding: long-term inheritance is a technology-neutral Urban Capability Exchange Network, not today's models/hardware.

## Deliberate scope boundary

No government, university, company, community group or auditor is claimed to have accepted any role. No budget, staffing level, SLA, statutory risk class, hearing procedure, procurement route, data-retention period or incident threshold is represented as official. Those remain integration/implementation questions for competent human institutions.