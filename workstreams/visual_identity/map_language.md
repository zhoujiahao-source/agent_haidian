# Map Language

## 1. Principle

The map must show what is known, estimated, proposed and unknown without making provisional geometry look official. Existing/locked context should be stable and quiet; proposals should be clear but explicitly non-statutory.

## 2. Base layers

- building/context fill: `paper-200` at 35–55% visual strength;
- ordinary roads: neutral 0.25–0.35 mm lines;
- rail: double neutral line with station ticks where evidence supports them;
- water: light neutral-teal fill, no decorative glow;
- green space: muted green-gray fill; do not reuse risk-low green in legends without category text.

## 3. Locked vs editable

### Locked existing layers

- stable solid line;
- square-ended boundary logic;
- `LOCKED / EXISTING` label when relevant;
- no interactive-looking handles.

### Editable/proposed layers

- primary civic-blue outline;
- slight translucent fill;
- explicit `PROPOSED` tag;
- if diagrammatic rather than parcel-accurate, use rounded/diagrammatic construction so it cannot be mistaken for a statutory line.

## 4. Design-status grammar

| Status | Line | Fill | Tag |
|---|---|---|---|
| Known | solid | neutral 70–100% | `K` / KNOWN |
| Estimated | long dash | 45° light hatch | `E` / ESTIMATED |
| Proposed | solid + outer keyline | translucent civic accent | `P` / PROPOSED |
| Unknown | dotted / broken | no fill or sparse dot texture | `?` / UNKNOWN |

Color is optional. The line/fill/tag combination must survive monochrome.

## 5. Provisional boundary

Current official polygons are absent. Therefore provisional site/key-area constraint should render as:

- 0.25 mm long-dash neutral line;
- no saturated fill;
- 10–15% neutral wash at most;
- repeated label `PROVISIONAL CONSTRAINT — NOT OFFICIAL REDLINE` at major map scales;
- source note adjacent to legend;
- never the thickest line in the figure.

## 6. Capability Backbone

Use two parallel strokes rather than one glowing line:

- outer/paired strokes: 0.55–0.8 mm;
- directional capability movement shown by sparse arrow/tick modules every 40–80 mm on A0 equivalent, not continuous chevrons;
- intersections use Open Node glyphs;
- forks use switch geometry.

The backbone is a spatial + institutional exchange layer, not a claimed new road/rail alignment. Caption accordingly.

## 7. Node hierarchy

- Level 1 regional exchange node: 8–10 mm A0 symbol + label + index;
- Level 2 learning unit node: 5–7 mm;
- Level 3 scenario/public interface node: 3.5–5 mm;
- experiment marker: separate badge attached to node, never replace node identity.

## 8. Time/version on maps

Version changes use milepost tags such as `V27·014`, where `V27` = City v2027 and `014` = release-note/node index. A map legend must explain the code.

## 9. Five-zone role labels

Every map of the three areas/two wings should pair place name with primary capability role, preventing homogeneous visualization:

- 众智园 — 技术能力生产 / 验证
- AI 原点社区 — 社会反馈 / 人才社区 / 公共服务学习
- 大钟寺 — 市场与 AI-native 服务验证
- 中关村科技服务翼 — 创新资源 / IP / 资本 / 服务交换
- 小月河场景赋能翼 — 公共空间 / 真实场景测试

## 10. Checkpoint — Phase 4

Map grammar defined for existing/locked, proposed, unknown, capability flows, node hierarchy and version/time. Official polygon remains an upstream dependency.