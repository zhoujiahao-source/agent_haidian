# Open Node Logo System

## Core idea

`Open Node` is a public interface / station / exchange point with a deliberate opening, not a generic AI symbol. Railway DNA is structural: parallel track = capability flow; station = callable public interface; switch = routing/choice; milepost = time/version.

The mark must remain identifiable in monochrome. A single full-detail symbol is **not** forced into every scale: this continuation pass added an optically simplified micro master after actual raster testing.

## Geometry family A — Open Ring Switch (primary, recommended)

Construction on a 24 × 24 conceptual grid:

- ring centered at (12,12), outer diameter 16, primary stroke 2;
- remove a 4-unit arc in the east-northeast quadrant;
- two parallel tracks enter from the west at y=9 and y=15;
- one route continues through the opening and one bends to create a route choice;
- opening remains actual negative space, never a color-only cut.

Meaning: station + route choice + unfinished/open system.

Strengths: strongest master identity; excellent route animation; extensible to zone indexing.

### Full-detail use

- digital: **32 px and above**;
- print: **4 mm and above**, subject to final production proof;
- master SVG: `assets_drafts/open-node-family-a.svg`.

A 48 px raster proxy (≈4.06 mm at 300 dpi) remains clean in grayscale. This is a useful prepress proxy, not a vendor proof.

## Family A Micro — small-size optical master

Actual 16/20/24 px raster testing showed the full diagonal switch competes with the ring opening at small sizes. The micro master therefore:

- preserves the open ring;
- preserves both incoming parallel tracks;
- preserves one outgoing route;
- removes the diagonal switch;
- increases stroke from 20/240 to 24/240.

Use:

- digital: **16–24 px**;
- do not use the full-detail master at 16 px simply for conceptual completeness;
- master SVG: `assets_drafts/open-node-family-a-micro.svg`;
- QA exports: `open-node-family-a-micro-16.png`, `open-node-family-a-micro-24.png`.

This is an optical correction, not a different logo family.

## Geometry family B — Open Interchange

Construction:

- two parallel vertical tracks spaced five units apart;
- an open circular interchange intersects them;
- routes visibly pass through rather than terminate;
- one diagonal switch leg exits at 45°.

Meaning: capabilities pass through and exchange.

Use: network diagrams, maps, Capability Backbone nodes. Do **not** use as the 16 px primary mark; its internal rail/arc structure crowds at micro scale.

## Geometry family C — Split Milepost Node

Construction:

- open square/circle hybrid with one missing corner;
- two parallel ticks enter from the west;
- a version/milepost notch sits on the lower edge;
- east opening remains visibly larger than decorative cuts.

Meaning: versioned public infrastructure / milepost / open access.

Use: Annual City Version Release, archive, release-note and milestone secondary device. It reads less strongly as the primary capability-exchange identity.

## Final hierarchy for Integration

1. **Family A full** — primary identity at normal sizes.
2. **Family A Micro** — primary identity at 16–24 px.
3. **Family B** — network/cartographic glyph.
4. **Family C** — version/archive/milepost device.

## Clear space

Let `x` equal the primary stroke width. Minimum clear space around the primary logo is `4x`; use `6x` on public signage where space permits.

## Minimum size / proof status

| output | master | status |
|---|---|---|
| 16 px | Family A Micro | raster + grayscale PASS |
| 20 px | Family A Micro | raster PASS |
| 24 px | Family A Micro | raster + grayscale PASS |
| ≥32 px | Family A Full | PASS |
| ≈4 mm print proxy | Family A Full at 48 px / 300 dpi | grayscale proxy PASS |
| <4 mm physical print | Micro only after vendor proof | NOT VERIFIED in this runtime |

Final paper/ink/toner/ICC/device proof is production-environment work and remains the only logo QA item this Agent cannot execute here.

## Monochrome

Primary and micro marks work as single ink. The opening is geometry, not a color transition. `open-node-family-a-mono-256.png` and `open-node-optical-proof-grayscale.png` are QA evidence exports.

## Five-zone extension

Do not create five unrelated logos. Keep Open Node geometry and add an index + capability subtitle:

- `01` 众智园 — 技术能力生产 / 验证;
- `02` AI 原点社区 — 社会反馈 / 人才社区 / 公共服务学习;
- `03` 大钟寺 — 市场 / AI-native 服务验证;
- `W1` 中关村科技服务翼 — 创新资源 / IP / 资本 / 专业服务交换;
- `W2` 小月河场景赋能翼 — 真实公共空间 / AI+ 场景测试.

These are visual-role labels, not statutory zoning claims.

## Motion principle

At normal sizes a 1.2–2.0 s route loop may show tracks entering, node outline drawing while leaving the opening, one route switching, and motion stopping on the static mark. At micro size, animate only entry/exit; do not reintroduce the removed diagonal switch.

No pulsing brain, particle cloud, glowing AI core, robot face, chip or infinity motif.

## Logo audit against the 10 required questions

- open not closed: YES, negative-space opening;
- station/interface/exchange: YES;
- avoids generic AI symbol: YES;
- 16–24 px: YES using tested micro master;
- monochrome: YES;
- extensible to five zones: YES via index system;
- route/switch animation: YES at normal sizes;
- railway DNA logical: YES, track/station/switch/milepost grammar;
- durable public-service context: YES;
- avoids startup look: YES when paired with the restrained type/grid system.

## Checkpoint — Phase 2 closure

Primary selection remains an Integration decision, but Window 5 now supplies a tested full + micro production hierarchy rather than an untested candidate only. See `logo_optical_qa.md` for the test record.
