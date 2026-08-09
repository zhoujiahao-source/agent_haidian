# Full Repository Audit — 2026-08-09

## 0. Purpose

This audit reviews the current `integration/final-city-os` branch, all six specialist workstream branches, the canonical submission package, and the latest upstream `open-city-ai/haidian` rules as of 2026-08-09.

The goal is not to generate more concepts. The goal is to identify where the project is already strong, where specialist research has not yet reached the formal package, where stale artifacts create contradictions, and which changes most improve formal-review readiness and competition score.

---

## 1. Current state in one sentence

The project has a strong and differentiated City OS design constitution and unusually deep specialist research, but the formal submission package is still a hybrid state: `proposal.md`, metrics, sources and assumptions have partially migrated to the new concept, while geometry, figures, A3/A0, report HTML, visual HTML, self-check, matrices and manifest still retain substantial legacy or stale content.

This is primarily an integration problem, not an idea-generation problem.

---

# 2. P0 — rule baseline changed after the current integration base

Current integration/fork baseline used for the last CI cycle: approximately `d400d48...`.

Latest observed upstream main during this audit:

`open-city-ai/haidian@275ef0c81a96cfb3bf31fbd746ec7a5c0308437c`

The upstream delta includes core-rule changes, not only peer submissions.

## New/changed requirements that matter immediately

### Proposal format v2

For a deliberate full narrative upgrade, use:

- `proposal_format_version: "2"`
- human-readable prose first;
- one to three claim-adjacent evidence markers for normal claims;
- no more than three consecutive markers;
- no more than eight markers in one paragraph/content block;
- exhaustive evidence coverage belongs in JSON / GeoJSON / matrices.

The current proposal is readable but still uses v1-style evidence density in several passages.

### Blocking bilingual contract

New packages / full v2 upgrades are expected to use:

- `bilingual_contract_version: "1"`
- `translation_file: "proposal.en.md"` for Chinese primary proposal;
- complete `proposal.en.md`;
- `report/proposal.en.html`;
- `visual/index.en.html`;
- `drawings/a3-booklet.en.pdf`;
- `drawings/a0-boards.en.pdf`;
- English counterparts for every text-bearing required figure;
- matching manifest language/translation mappings and hashes.

The present package does not satisfy this new bilingual contract.

### Current visual HTML validation

`visual/index.html` must visibly include:

- 总览地图
- 三层范围
- 重点区域
- 用地分区
- 交通慢行
- 蓝绿公共空间
- 建筑
- 更新项目
- AI 场景
- 核心指标
- 任务覆盖
- 自检状态
- 来源
- 假设

It must also declare numeric `data-metric` values matching `metrics.json`, including at least:

- `site_area_sqm`
- `green_ratio`
- `public_space_ratio`

The current visual technically includes many legacy required markers and the three required metrics, but its design content is stale and must be regenerated from the final package.

## P0 action

Before any final package claims:

1. sync/rebase against latest upstream;
2. re-read changed Skill / formal guide / schema / validation scripts;
3. rerun the current deterministic + spatial + visual + professional checks only after final assets are rebuilt.

Previous CI status must not be treated as current after the rule change.

---

# 3. Repository architecture audit

## Current knowledge sources

There are currently eight relevant states:

1. `agent/evidence-basemap`
2. `agent/urban-structure`
3. `agent/ai-governance-metrics`
4. `agent/public-space-landmarks`
5. `agent/visual-identity`
6. `agent/operations-stewardship`
7. `integration/final-city-os`
8. canonical submission under `submissions/zhoujiahao-source/jingzhang-legible-ai-belt/`

The integration branch does not contain the six specialist workstream directories. It contains independent summaries under `workstreams/integration/`.

## Risk

Specialist research is richer than the integration summary and can be lost, simplified or contradicted during final migration.

## Improvement

Create a machine-readable integration decision register before final migration, e.g.:

`workstreams/integration/adoption_register.json`

For every adopted specialist artifact record:

- source branch
- source commit
- source file
- decision: adopt / adapt / archive / reject
- canonical target file
- reason
- evidence status
- integration commit

This should become the authoritative bridge between specialist work and formal package.

Also consolidate PR strategy. PR #3 and PR #4 currently point to the same evolving integration head but use different bases and purposes. Keep one integration review path and preserve the historical validated submission as a tag/branch rollback point rather than maintaining competing integration PR semantics.

---

# 4. Specialist module audit

## 4.1 Evidence & Basemap

### Strongest assets

- detailed source inventory and conflict register;
- Official / Verified / Derived / Assumed / Unknown method;
- Known / Estimated / Proposed / Unknown drawing-state method;
- differentiated profiles for Three Areas / Two Wings;
- 15 field-audit targets;
- source-registry promotion candidate;
- executable OSM/Overpass basemap fetcher;
- executable Microsoft Global ML Building Footprints fetcher;
- validation scripts;
- six global ecosystem case evidence records.

### Main gap

The workflow is executable, but real current basemap data has not yet been materialized in a networked checkout and the field audit has not been executed.

### Improvement priority

Run the basemap scripts in a networked workspace, preserve provenance and timestamp, cross-check OSM vs Microsoft vs public official references, then promote only validated features.

This is one of the highest-value improvements for `implementation_feasibility`, `spatial_specificity`, and `expression_completeness`.

### Do not do

Do not promote OSM/Microsoft features to Official. Do not use open data to infer legal redlines, ownership, statutory controls or heritage permission.

---

## 4.2 Urban Structure

### Strongest assets

- six-layer Capability Backbone;
- five differentiated learning-unit prototypes;
- evidence-gated east-west stitch framework;
- north-south public-life sequence;
- seven node prototypes;
- Permanent / Adaptive / Experimental implementation model;
- detailed key-area section briefs;
- candidate GeoJSON for Backbone, stitch axes and capability nodes.

### Main gap

These hard spatial artifacts have not replaced the legacy canonical geometry.

### Current canonical geometry problems

- `land_use.geojson` remains a four-stripe conceptual partition;
- `roads.geojson` remains one north-south study line plus schematic east-west lines;
- `public_space.geojson` still contains old Legible-AI node names and footprints;
- `phasing.geojson` still uses large blanket phase polygons;
- `buildings.geojson` is conceptual program envelopes, not an existing building base.

### Improvement priority

1. preserve provisional SITE_BOUNDARY / KEY_AREA with current warnings;
2. integrate Capability Backbone as a study/design feature, not a verified route;
3. integrate `SCENARIO_NODE` capability anchors with host-verification flags;
4. demote/rebuild east-west cross-lines as study axes until crossings are verified;
5. replace old public-space footprints with current PCI/landmark taxonomy;
6. replace blanket phasing with component-level `implementation_layer`, `delivery_phase`, `reversibility`, `evidence_status`, and `host_verification_required` logic where schema permits;
7. rebuild spatial drawings from these canonical layers.

---

## 4.3 AI Governance & Metrics

### Strongest assets

- eligible-issue gate;
- Problem Track + Capability Track;
- consequence-based risk tiers;
- authorization matrix;
- bounded experiment protocol;
- public-value floors;
- STOP / MODIFY / CONTINUE / SCALE semantics;
- UAR eligibility/numerator/denominator discipline;
- Responsible STOP reported separately;
- 17 custom metric candidates;
- Capability transfer revalidation;
- dashboard public/audit split;
- anti-gaming rules;
- machine-readable schemas for issue, experiment, capability and annual release.

### Main gap

Canonical package currently adopts only part of this sophistication.

### Improvement priority

- retain UAR-90 and UAR-365 as `unknown/null` until real records exist;
- selectively add only the custom metrics that improve judging clarity;
- use the governance schemas as implementation-contract evidence, not as claims of deployed infrastructure;
- turn authorization / lifecycle / transfer / dashboard rules into 2–3 high-quality diagrams;
- keep legal references as screening/comparative inputs, not deployment authorization.

### Key scoring opportunity

This module can strongly differentiate the project on AI-planning innovation if it is shown visually and spatially rather than buried in prose.

---

## 4.4 Public Space & Landmarks

### Strongest assets

- PCI as a six-layer civic contract;
- 9 public capabilities;
- 8 node typologies;
- 20 public-space components;
- 8 personas;
- 12 scenario cards;
- 4 explicit test/validation scenarios;
- 24-hour / seasonal / emergency orchestration;
- 1909 → 2026 → Future → Retired Capability Archive;
- section and user/lifecycle briefs;
- controlled render briefs.

### Main gap

The work remains mostly programmatic. It has not yet become final physical urban design.

### Improvement priority

Produce spatially specific design outputs:

- 3–5 PCI prototype plans/sections;
- one ordinary-service OFF-mode / AI-enabled ON-mode comparison;
- three key-area enlargements;
- 1909 Railway Memory Ground spatial concept;
- 2026 City Learning Archive spatial/architectural concept;
- Future Open Test Station reversible spatial concept;
- Retired Capability Archive spatial and operational sequence;
- one 8AM–Midnight scenario orchestration drawing.

Each should show shade, seating, ordinary wayfinding, accessibility, staff/manual fallback and failure-safe public-space operation before technology spectacle.

---

## 4.5 Visual Identity

### Strongest assets

- Public Service Aesthetic rules;
- Open Node Family A + Micro master;
- Family B map glyph;
- Family C version/milepost device;
- grayscale/monochrome optical QA;
- independent evidence/design/outcome/risk semantics;
- complete state legend;
- map grammar;
- design tokens CSS;
- offline specimen;
- A0/A3/HTML layout rules.

### Main gap

Almost none of these production-ready assets are currently used in the canonical submission.

### Improvement priority

- adopt Open Node into the actual package;
- adopt the four semantic systems into every figure/HTML/A3/A0;
- add explicit `PROVISIONAL CONSTRAINT — NOT OFFICIAL REDLINE` map styling;
- regenerate all five required figures;
- generate bilingual figure variants;
- use shared tokens so report HTML, visual HTML and boards visibly belong to one system;
- preserve non-color redundancy for status communication.

---

## 4.6 Operations & Public Stewardship

### Strongest assets

- Public Stewardship accountability architecture;
- RACI;
- Problem Track / Capability Track;
- Capability Registry;
- developer sandbox and maintenance/deprecation logic;
- community rights beyond surveys;
- annual operating calendar;
- City Learning Assembly;
- Annual City Version Release;
- retirement/decommission protocol;
- 5/10/20-year roadmap;
- institutional risks;
- integration templates.

### Main gap

Operations are conceptually rigorous but still weakly connected to implementation resources and the actual spatial package.

### Improvement priority

Without inventing named government commitments, add:

- functional operator roles;
- indicative staff/service functions;
- maintenance responsibilities;
- failure/offline service continuity;
- procurement/vendor exit principles;
- qualitative resource bands or delivery complexity classes instead of invented budgets;
- explicit 0–1 / 1–3 / 3–5 year gate conditions tied to evidence maturity;
- one annual operating calendar diagram;
- one Capability Registry → Annual Release → Retired Archive diagram.

---

# 5. Integration workstream audit

Current handoff reports `canonical_files_modified: false`, but canonical files on `integration/final-city-os` have already been changed.

This is stale and must be corrected.

The integration workstream also duplicates specialist content in summary form. This is useful for synthesis but dangerous if treated as the sole evidence source.

## Improvement

- update `handoff.json` to current reality;
- add adoption register;
- record latest upstream ref used;
- distinguish specialist-source facts from Integration reinterpretations;
- stop creating new summary modules once canonical migration begins;
- move effort into formal package consistency.

---

# 6. Canonical submission — file-by-file audit

## `proposal.md`

### Current state

Strong City OS narrative already migrated:

- Urban Capability Exchange master name;
- Capability Backbone;
- distributed learning units;
- PCI;
- UAR;
- Public Stewardship;
- 8 personas;
- 12 scenarios;
- global cases;
- current Beijing/Haidian evidence.

### Improvements

- adopt proposal format v2;
- add `bilingual_contract_version: "1"` and `translation_file` if doing full current upgrade;
- produce complete `proposal.en.md`;
- reduce citation density to claim-adjacent evidence;
- add more spatially specific design descriptions from the specialist branch;
- make implementation responsibilities/gates more explicit;
- add regional synergy beyond the immediate corridor where evidence supports it;
- ensure one final naming hierarchy only.

---

## `metrics.json`

### Current state

One of the strongest canonical files.

It already separates official text reference areas from provisional geometry metrics and keeps UAR/operations metrics unknown where unmeasured.

### Improvements

- recalculate all geometry-dependent metrics after geometry migration;
- demote visually misleading conceptual ratios where needed;
- selectively add 17-metric catalog items only if they make evaluation clearer;
- ensure every displayed HTML metric is known and exactly synchronized;
- retain UAR operational values as null until real registry records exist.

---

## `sources.json`

### Current state

Good source diversity and limitations, including official Beijing/Haidian sources, OSM/Microsoft candidates and six global cases.

### Improvements

- merge approved entries from Evidence Agent source-promotion candidate;
- normalize publisher, URL, retrieval/publication date, license/reuse status and limitation fields;
- confirm every claim uses a source fit for that claim;
- do not let background-only sources support statutory/spatial control claims;
- rerun against latest source registry.

---

## `assumptions.json`

### Current state

Good explicit uncertainty structure.

### Improvements

- add/revise assumptions after canonical geometry migration;
- connect each unresolved host/crossing/heritage/utility question to a recalculation trigger;
- keep institutional and governance roles explicitly proposed;
- remove assumptions that are superseded by newly verified basemap evidence.

---

## `self_check.json`

### Current state

Stale and insufficient.

It contains only five hand-authored checks and still states `7 personas`, while the current proposal/metrics use `8 personas`.

### Improvement

Do not manually repair this file as the final evidence. Regenerate it from the then-current official script after all files are synchronized.

Final readiness should come from the current four gate families and current self-check/preflight output, not historical handwritten PASS statements.

---

## `compliance_matrix.json`

### Current problem

Many requirements map to the same generic report sections, geometry files, metrics, sources and checks.

This may satisfy structural validation but is weak professional evidence.

### Improvement

Make evidence requirement-specific.

Examples:

- agent.1 → final naming/VI/Capability Backbone figure;
- agent.2 → six global cases + ecosystem map + Zhongzhiyuan;
- agent.3 → 12 scenarios + 8 personas + four tests + AI lifecycle;
- agent.4 → PCI + east/west stitch + three landmarks + Dazhongsi;
- agent.5 → 1909→2026→Future cultural system;
- agent.6 → Public Stewardship + annual assembly + developer ecosystem + version release.

Each requirement should point to the best few evidence artifacts, not the whole package.

---

## `standard_matrix.json`

### Current problem

Repeated generic evidence blocks and widespread `review_status: addressed` overstate specificity.

### Improvement

- map each standard to the exact relevant design evidence;
- separate `addressed`, `partial`, and `pending professional confirmation` where schema/status allows;
- never claim a mandatory standard is fully resolved when its official reference/data is missing;
- refresh local reference IDs/hashes from latest upstream.

---

## `design_depth_matrix.json`

### Current problem

Many items are marked `complete` despite missing real basemap, planning controls, engineering data and detailed physical drawings.

### Improvement

Recommended conservative statuses:

- existing conditions diagnosis → partial until basemap materialization;
- three-level scope → complete at conceptual/task level;
- overall spatial structure → strong conceptual / partial professional;
- land-use layout → conceptual complete, professional confirmation pending;
- development intensity → pending official data;
- height/massing → pending;
- retain/renovate/demolish → pending building survey;
- traffic/crossings → partial, engineering verification pending;
- municipal/new infrastructure → partial/pending;
- blue-green/public space → conceptual strong, host/detail verification pending;
- three key-area detailed design → partial until enlarged plans/sections exist;
- implementation/phasing → conceptual strong, institutional/resource confirmation pending;
- metrics recalculation → complete only for explicitly provisional/design geometry.

A credible partial status is stronger than an unconvincing blanket `complete`.

---

## `manifest.json`

### Current problem

Stale.

It still declares `ready_for_review`, old generated time, old SHA256 values and only Chinese assets while current canonical content has changed.

### Improvement

Do not hand-maintain final hashes.

After all content is frozen:

1. render;
2. finalize;
3. generate current manifest hashes;
4. generate self-check;
5. run participant preflight;
6. rerun current CI.

Only then set package/review state based on actual validation.

---

## `agent.json`

Currently consistent and low risk.

Keep model/agent declaration accurate. Update only if current submission schema requires new metadata.

---

## `report/copyright_statement.md`

Currently sensible and conservative.

Update it when final graphics are generated to document:

- programmatic diagram generation method;
- any AI image generation if later used;
- all third-party/open-data licenses and attribution boundaries;
- whether final figures are maps, derived diagrams, or illustrative spatial renderings.

---

# 7. Canonical geometry audit

## `site_boundary.geojson`

Keep provisional and locked. Do not sharpen or reinterpret as official.

## `key_areas.geojson`

Keep provisional. Separate taskbook reference hectares from polygon-derived measurements.

## `land_use.geojson`

Current four vertical bands are too schematic for the new concept and may visually imply a real regulatory land-use plan.

Rebuild/demote using evidence-backed functional structure while preserving valid topology and official land-use codes.

## `buildings.geojson`

Do not treat as existing condition. Replace or clearly retain as conceptual program envelopes until real basemap/building facts are available.

## `roads.geojson`

ROAD-001 can remain a candidate continuity study axis only. East-west lines must remain study axes until crossing/right-of-way/heritage/engineering verification.

## `green_space.geojson`

Rebuild from verified public-space/water/park evidence where possible; separate current/known green from proposed blue-green capability interventions.

## `public_space.geojson`

Legacy names/roles are obsolete relative to the current PCI + Landmark-as-Memory system.

Rebuild around current node taxonomy, using verified/proposed status and host verification.

## `phasing.geojson`

The current large geographic phase polygons are inconsistent with reversible City OS logic.

Replace with component-level implementation/reversibility logic and truthful spatial phasing only where host/site evidence exists.

## `constraints.geojson`

Keep strong uncertainty disclosure. Add only real verified constraints from public/cleared sources; do not manufacture regulatory control geometry.

---

# 8. Core figures audit

Current canonical required figures are approximately 1.2–1.4 KB each and remain legacy placeholders.

They must all be rebuilt from final canonical data:

1. `site-overview.png`
2. `land-use-structure.png`
3. `key-areas.png`
4. `mobility-bluegreen.png`
5. `metrics-evidence.png`

## Recommended final figure content

### Figure 1 — Site / Evidence / Capability Backbone

Real basemap context + provisional boundary + verified/derived status + three key areas + five learning units + Backbone.

### Figure 2 — Spatial Structure / Implementation Layers

Functional structure + Permanent / Adaptive / Experimental + capability flow, not statutory-looking stripes.

### Figure 3 — Three Key Areas

Three enlarged mini-plans / sections showing physically different urban prototypes.

### Figure 4 — Mobility / Blue-Green / PCI Network

North-south continuity + evidence-gated east-west stitch + blue-green network + PCI nodes + OFF-mode/human fallback.

### Figure 5 — Urban Learning / Public Value / UAR

Eligible Issue → risk authorization → bounded experiment → public value review → STOP/MODIFY/CONTINUE/SCALE → transfer/retire + UAR formula + audit/anti-gaming.

All text-bearing figures need bilingual counterparts under v2 bilingual contract.

---

# 9. A3 / A0 drawings audit

Current canonical PDFs are approximately 1.1 KB and are not substantive final competition drawings.

The local preview generated during the integration conversation is visually stronger but still is not the canonical GitHub artifact.

## Final A3/A0 should include

- real/derived existing-condition evidence map;
- master spatial plan;
- Capability Backbone system;
- three key-area enlarged plans;
- 3–5 sections;
- PCI node axonometrics / plans;
- 1909 / 2026 / Future / Retired spatial sequence;
- AI governance lifecycle;
- UAR/public-value dashboard;
- scenario/persona mapping;
- implementation/operations/version release;
- evidence legend and uncertainty status;
- bilingual variants.

The biggest expression gap is not graphic styling. It is the absence of enough physical urban-design drawings.

---

# 10. `report/proposal.html` audit

Current report HTML still renders the old Legible AI narrative while `proposal.md` has already migrated to Urban Capability Exchange.

This is a critical consistency failure.

Regenerate only after final v2 proposal and figures are frozen. Then create the English counterpart.

---

# 11. `visual/index.html` audit

Current visual HTML is also legacy:

- title remains `京张·可读AI城市带`;
- lead remains the old legibility thesis;
- hierarchy is old `一脊 · 三核 · 两翼 · 四级可读性 · 100日可逆试点`;
- KPI still says 7 personas;
- scenarios are the old L0–L3 presentation language.

It technically contains several required visual-review text markers and numeric metrics, but conceptually it is obsolete.

## Improvement

Rebuild as a City OS evidence exhibition:

- hero = Urban Capability Exchange thesis;
- Capability Backbone map;
- five learning units;
- Public Capability Interface;
- current 12 scenarios / 8 personas;
- Public Value + UAR;
- risk/experiment state;
- Annual City Version Release;
- Landmark as Memory;
- sources/assumptions/self-check;
- exact data-metric synchronization;
- fully offline;
- English counterpart.

---

# 12. Competition-score improvement priorities

## P0 — correctness / integration blockers

1. Sync latest upstream and audit new rules.
2. Choose and implement v2 + bilingual contract for the full upgraded package.
3. Consolidate integration PR/source-of-truth strategy.
4. Fix split-brain proposal/report/visual/figures/matrices/self-check/manifest.
5. Migrate specialist hard artifacts into canonical files.
6. Rebuild five figures and A3/A0.
7. Regenerate manifest/self-check/preflight/CI with latest scripts.

## P1 — highest score uplift

1. Materialize real basemap data and cross-validation evidence.
2. Replace schematic canonical geometry with evidence-gated Capability Backbone / node / public-space design.
3. Produce true detailed urban-design plans and sections.
4. Make matrices requirement-specific and honest about partial status.
5. Add implementation roles, maintenance, resource complexity and gate conditions.
6. Add an evidence-based regional synergy diagram/mechanism for broader innovation networks where the brief/rubric requires it.
7. Make AI governance spatially visible rather than text-only.

## P2 — differentiation and communication

1. Integrate Open Node identity assets.
2. Use v2 human-readable citation discipline.
3. Build Capability Registry / Annual Release / Retired Archive graphics.
4. Show what remains in 20 years vs what is replaceable technology.
5. Translate railway DNA into physical materials, furniture, wayfinding and sections, not only logo symbolism.
6. Show ordinary high-quality public space first and AI backstage.

---

# 13. Recommended execution order

1. Sync latest upstream.
2. Freeze one integration branch / PR strategy.
3. Create adoption register from six specialist branches.
4. Run Evidence Agent real-basemap materialization.
5. Rebuild canonical spatial geometry.
6. Recalculate conventional metrics.
7. Finalize AI metrics/governance structured records.
8. Rewrite proposal to v2 human-readable form.
9. Produce English proposal.
10. Rebuild five core figures in zh/en.
11. Produce detailed A3/A0 in zh/en.
12. Regenerate report HTML and visual HTML in zh/en.
13. Rewrite compliance/standard/design-depth matrices from actual evidence.
14. Update copyright/disclosure.
15. Run current render/finalize/self-check/participant-preflight.
16. Fix all participant-controlled errors.
17. Trigger current CI and inspect full feedback.
18. Only after real PASS / formal-review-ready state, refresh package status and upstream PR.

---

# 14. Bottom line

The project does not need more conceptual breadth.

Its biggest opportunity is to convert already excellent specialist research into one synchronized, evidence-backed, bilingual, physically specific urban-design package.

The current weakest layer is not AI thinking; it is the final spatial/professional evidence layer:

**real basemap → canonical geometry → detailed plans/sections → figures/A3/A0 → bilingual display → honest matrices → current validation.**

Once that chain is closed, the City OS / Capability Exchange concept will be much more competitive because the novelty will be visible as actual urban design rather than only as a sophisticated governance narrative.
