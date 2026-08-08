# Visual Audit — WINDOW 5

Status: working evidence/design audit for Final Integration Agent; **not** a canonical submission change.

## 0. Audit baseline and latest re-check

- Upstream repository: `open-city-ai/haidian`
- Initial observed upstream `main`: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff` (2026-08-08 13:17:04Z)
- Continuation observed upstream `main`: `a3c14da8431f6ca63ff2059c90733132c2d4e8eb` (2026-08-08 14:17:02Z)
- Upstream delta since initial audit: 107 commits; returned changed paths were under participant `submissions/...`, with no observed Skill/brief/allowed-design/visual-recommendation/organizer-geometry path in that compare.
- User fork: `zhoujiahao-source/agent_haidian`
- Working branch: `agent/visual-identity`
- Working base: `796d29a69774f4722fd7b5012505a3f20bb2e35d`
- Owned path: `workstreams/visual_identity/`
- Canonical submission modified by this Agent: **No**

## 1. Current-rule audit

### 1.1 Must preserve

The upstream package requires a professional, machine-readable, spatially reviewable and visually inspectable submission. Visual expression is a verification/readability interface; it cannot overrule GeoJSON, metrics, matrices, sources or assumptions.

The current brief fixes three positioning statements and five functional requirements and requires agent.1–agent.6 coverage. The visual system must therefore support, not replace:

- 百年京张文化带;
- 都市 AI 生活体验带;
- AI 融合创新带;
- AI 全栈自主创新体系;
- 世界级 AI 创新生态;
- AI+ 场景赋能新范式;
- 智能化 AI 活力城市;
- AI 治理全球话语权.

### 1.2 Geometry status

At the audited upstream geometry listing, only these organizer geometry helpers were present:

- `provisional_boundaries.geojson`;
- `provisional_boundaries_basis.md`;
- `study_area_bbox.geojson`.

No organizer-supplied official `SITE_BOUNDARY` / `KEY_AREA` polygon was observed. Therefore all current visual treatment of those extents must remain explicitly provisional, low-contrast and non-statutory.

### 1.3 Rule conflict — preserve and escalate, do not silently resolve

A repository-level tension remains:

- Skill language says organizer missing official polygons do not by themselves block content scoring;
- `design_brief.json` / `allowed_design_space.json` retain policy fields saying exact official boundary is required for professional scoring / provisional geometry blocks formal professional scoring.

Window 5 searched upstream Issues for a matching clarification and found no connector result. It attempted to open an upstream Issue and received `403 Resource not accessible by integration`; a fallback fork Issue failed because Issues are disabled (`410`). See `collaboration_log.md`.

Until upstream resolves the mismatch, Integration should preserve the disclaimer and avoid claiming either interpretation is authoritative.

## 2. Existing submission visual audit

### 2.1 Existing brand narrative

The current candidate is `京张·可读AI城市带 / Jing-Zhang Legible AI Belt` and describes an old logo as “two parallel tracks + a central transparent node.” Railway abstraction and public legibility remain useful assets, but the locked newer constitution elevates `City OS / Capability Backbone / Public Capability Interface / Open Node / Annual City Version Release` above “Legible AI” as the total concept.

**Retain:** railway abstraction; public readability and human responsibility; bilingual communication; explicit provisional-boundary disclosure.

**Reframe:** central transparent node → Open Node; Legible AI → governance/visual sub-principle or naming candidate; old L0–L3 logic → scenario-governance content rather than a universal status palette.

### 2.2 Five required core figures — pixel-level inspection completed

The existing candidate branch contains all five required files. Window 5 fetched and decoded every PNG and inspected them at native resolution. All are **400 × 225 px indexed-palette PNGs**.

| figure | bytes | direct observation | decision |
|---|---:|---|---|
| `site-overview.png` | 1406 | header + vertical line + 3 nodes + empty callout frames; no geographic basemap/boundary/legend | **REBUILD** |
| `land-use-structure.png` | 1251 | empty cards + line/nodes; no land-use polygons/categories | **REBUILD** |
| `key-areas.png` | 1247 | three framed boxes; no map/key-area geometry/names | **REBUILD** |
| `mobility-bluegreen.png` | 1297 | horizontal blue lines + vertical green band + empty boxes; no actual mobility/blue-green geography | **REBUILD** |
| `metrics-evidence.png` | 1198 | empty metric-card frames + bottom bar; no metrics/formulas/source/confidence | **REBUILD** |

This replaces the earlier file-size-only warning. The figures are now directly confirmed as minimal schematic placeholders rather than professional evidence-dense urban-design figures.

See `legacy_figure_inspection.md` for the inspection record.

### 2.3 Existing proposal strengths to preserve

- distinguishes provisional geometry from official planning;
- links narrative to `[data:]`, `[metric:]`, `[source:]`, `[standard:]`, `[depth:]` references;
- frames AI interventions as reviewable, reversible and human-accountable;
- differentiates the three key areas rather than making all districts identical.

These are sound foundations for the rebuilt figures.

### 2.4 Visual-system gaps that Window 5 has now closed

- Open Node has three geometry families plus a tested small-size micro master;
- evidence, design, experiment and risk semantics are four independent systems;
- black/white fallback grammar is explicit;
- A3/A0/HTML/figures/scenario cards/dashboard share grid/token rules;
- Annual City Version Release links version, release note, node label and archive;
- reusable civic icon grammar exists;
- complete semantic legend includes all O/V/D/A/?, K/E/P/?, TEST/STOP/MODIFY/CONTINUE/SCALE and R1/R2/R3 states;
- SVG, CSS, PNG QA exports, asset manifest and offline specimen are available in `assets_drafts/`.

## 3. Retain / replace matrix

| Existing asset/idea | Decision | Reason |
|---|---|---|
| railway double-track abstraction | RETAIN | project-specific DNA; structural rather than nostalgic |
| transparent central node | REBUILD | needs explicit opening/routing/exchange semantics |
| Legible AI as total master concept | DEMOTE / CANDIDATE | new constitution prioritizes City OS/capability exchange |
| evidence-linked proposal annotations | RETAIN | supports auditability |
| provisional-boundary disclaimers | RETAIN + STRENGTHEN | official organizer polygon still not observed |
| one traffic-light system for all states | REJECT | unsafe semantic collapse |
| cyberpunk/neon/robot-face/chip motifs | REJECT | conflicts with Public Service Aesthetic |
| literal steam-train/ticket nostalgia | REJECT | railway DNA is structural |
| five legacy core PNGs | **REBUILD CONFIRMED** | pixel-level inspection proves they are schematic placeholders |
| bilingual labels | RETAIN | international communication |

## 4. Phase 0 + continuation checkpoint

Completed:

- latest upstream rule re-check;
- geometry availability re-check through upstream delta analysis;
- existing proposal/brand audit;
- native-pixel inspection of all five required legacy figures;
- retain/rebuild/reject decisions;
- Open Node optical QA and micro master;
- complete semantic legend + reusable tokens + offline specimen;
- attempted rules-conflict collaboration escalation.

Remaining Unknown / external dependency:

- organizer-supplied official `SITE_BOUNDARY` / `KEY_AREA` polygons;
- final project master name, owned by Integration;
- final print vendor device, paper/stock, ink/toner and ICC workflow.

There is no longer an Unknown about the visual content of the legacy five PNGs: they have been directly inspected and are confirmed rebuild targets.
