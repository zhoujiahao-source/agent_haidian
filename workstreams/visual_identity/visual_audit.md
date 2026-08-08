# Visual Audit — WINDOW 5

Status: working document for Final Integration Agent; **not** a canonical submission change.

## 0. Audit baseline

- Upstream repository: `open-city-ai/haidian`
- Upstream `main` observed at: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff` (2026-08-08 13:17:04Z)
- User fork: `zhoujiahao-source/agent_haidian`
- Working branch: `agent/visual-identity`
- Working base: `submission/zhoujiahao-source/jingzhang-legible-ai-belt`
- Owned path: `workstreams/visual_identity/`
- Canonical submission modified by this Agent: **No**

## 1. Current-rule audit

### 1.1 Must preserve

The current upstream package still requires a professional, machine-readable, spatially reviewable and visually inspectable submission. The visual layer cannot overrule GeoJSON, metrics, matrices, sources or assumptions. Visuals must remain an explanatory and verification interface.

The current upstream brief fixes three positioning statements and five functional requirements, and requires agent.1–agent.6 coverage. For this workstream the visual system must therefore support, rather than replace:

- 百年京张文化带
- 都市 AI 生活体验带
- AI 融合创新带
- AI 全栈自主创新体系
- 世界级 AI 创新生态
- AI+ 场景赋能新范式
- 智能化 AI 活力城市
- AI 治理全球话语权

### 1.2 Geometry status

At the observed upstream snapshot, `brief/site-package/geometry/` contains only:

- `provisional_boundaries.geojson`
- `provisional_boundaries_basis.md`
- `study_area_bbox.geojson`

No official `SITE_BOUNDARY` or `KEY_AREA` polygon file was present in the directory listing. Therefore every visual treatment of the current site/key-area extent must remain explicitly provisional.

### 1.3 Rule conflict to preserve, not silently resolve

There is a current repository-level tension:

- the current Skill text says missing organizer-supplied official polygons do not by themselves block content scoring;
- `design_brief.json` and `allowed_design_space.json` still contain fields that say exact official boundary is required for professional scoring / provisional boundary blocks formal professional scoring.

This Agent must not pick one interpretation and hide the other. Integration should flag the mismatch and keep all provisional geometry visually de-emphasized and labeled until the repository resolves it.

## 2. Existing submission visual audit

### 2.1 Existing brand narrative

The current candidate submission is titled `京张·可读AI城市带 / Jing-Zhang Legible AI Belt` and defines its old logo as “two parallel tracks + a central transparent node.” That is useful railway-derived DNA, but it is not yet the locked new visual constitution. The newer design constitution elevates `City OS / Capability Backbone / Public Capability Interface / Open Node / Annual City Version Release` above “Legible AI” as the total concept.

**Keep:**

- railway abstraction rather than literal train nostalgia;
- parallel-track logic;
- public readability / human responsibility as a governance sub-principle;
- bilingual structure;
- explicit provisional-boundary disclaimer.

**Reframe:**

- “central transparent node” → `Open Node`: a node with a visible opening, connection or route continuation;
- “Legible AI” → governance/visual sub-principle, not necessarily final master name;
- old four-level legibility gradient → may remain as scenario-governance content but must not become the universal color system for evidence, design status, experiment state and risk.

### 2.2 Existing required figures

The branch contains the five required core figure filenames:

- `site-overview.png` — 1406 bytes
- `land-use-structure.png` — 1251 bytes
- `key-areas.png` — 1247 bytes
- `mobility-bluegreen.png` — 1297 bytes
- `metrics-evidence.png` — 1198 bytes

These extremely small file sizes are a strong warning that the current figures are likely minimal/generated placeholders rather than information-dense professional boards. File size alone is not proof of visual failure, but they should be treated as **REBUILD CANDIDATES** until visually inspected and verified.

**Action for Integration:** regenerate all five figures under one visual grammar; do not simply recolor the existing PNGs.

### 2.3 Existing proposal strengths to preserve

- It already distinguishes provisional geometry from official planning.
- It already links narrative to `[data:]`, `[metric:]`, `[source:]`, `[standard:]`, `[depth:]` references.
- It already frames AI interventions as reviewable, reversible and human-accountable.
- It already differentiates the three key areas rather than making all districts identical.

These are good foundations for evidence-led graphics.

### 2.4 Existing visual weaknesses / risks

1. The old identity is conceptually closer to a “closed badge with central point” than a fully developed `Open Node` interface language.
2. There is no documented four-system separation for evidence status, design status, experiment status and risk.
3. There is no documented black-and-white fallback grammar.
4. There is no explicit shared grid/token system for A3, A0, HTML, figures, scenario cards and dashboards.
5. There is no visible version-release identity linking `v2027`, release notes, node labels and archive status.
6. There is no reusable icon family tying node, route, consent, human override, archive and capability exchange together.
7. Current core PNGs are suspiciously tiny and should not be assumed to satisfy the professional-expression bar.

## 3. Retain / delete / rebuild matrix

| Existing asset/idea | Decision | Reason |
|---|---|---|
| Railway double-track abstraction | RETAIN | Strong project-specific DNA; non-nostalgic and extensible |
| “Transparent central node” | REBUILD | Upgrade to explicitly open, routable, exchangeable node |
| “Legible AI” as total master concept | DEMOTE / CANDIDATE | New constitution prioritizes City OS and capability exchange |
| Evidence-linked proposal annotations | RETAIN | Supports auditability |
| Provisional-boundary disclaimers | RETAIN + STRENGTHEN | Current official polygon still absent |
| One color system for all states | REJECT | Semantically unsafe; four status families must remain separate |
| Cyberpunk / neon / robot-face / chip motifs | REJECT | Conflicts with Public Service Aesthetic |
| Literal steam-train / ticket nostalgia | REJECT | Railway DNA must be structural, not decorative |
| Five current core PNGs | REBUILD CANDIDATES | Need unified, evidence-dense professional information design |
| Bilingual labels | RETAIN | Required for international communication |

## 4. Phase 0 checkpoint

Completed:

- checked latest upstream Skill and key brief files;
- checked geometry directory for official polygons;
- checked current visual recommendations;
- checked existing user candidate proposal and required figure set;
- established retain/rebuild/reject decisions.

Unknown:

- exact visual content of each tiny PNG has not been pixel-inspected in this connector-only pass;
- official `SITE_BOUNDARY` / `KEY_AREA` polygons remain absent in the observed upstream geometry directory;
- final project master name remains Integration-owned;
- final print vendor ICC profile, exact paper stock and final board printing process are unknown.

Next dependency:

- define an executable public-service visual grammar, then develop Open Node, state systems, map language, version identity and cross-format layout tokens.
