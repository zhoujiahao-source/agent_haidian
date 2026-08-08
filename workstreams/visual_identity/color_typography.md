# Color & Typography

## 1. Palette role

Color is supportive, never the only carrier of meaning.

### Civic foundation

| Token | HEX | Use |
|---|---|---|
| `ink-900` | `#17212B` | primary text / major outlines |
| `ink-700` | `#34424F` | secondary text |
| `paper-000` | `#FFFFFF` | background |
| `paper-050` | `#F5F7F8` | panels / low-priority basemap |
| `paper-200` | `#DCE2E6` | rules / inactive boundaries |
| `civic-blue` | `#2463A6` | primary civic emphasis / selected capability backbone |
| `civic-teal` | `#147D76` | public-service capability / blue-green links |
| `civic-gold` | `#A56B16` | heritage/time/version accent, sparingly |

Avoid electric cyan, violet-neon gradients and luminous blue-on-black as default identity.

### Risk colors — secondary to symbols/text

- low: `#3F7A4A`
- medium: `#A56B16`
- high: `#A33A35`

Risk is always paired with `R1 / R2 / R3`, shield/triangle icon and text `LOW / MEDIUM / HIGH`.

### Experiment state colors

These are **not** risk colors and use a separate hue family plus labels:

- TEST: `#52616F`
- STOP: `#8A3F52`
- MODIFY: `#8A6428`
- CONTINUE: `#2E6F73`
- SCALE: `#365E9D`

Every state uses a distinct wordmark and border pattern; grayscale remains readable.

## 2. Evidence status styling

Evidence status should rely primarily on fill/pattern/border, not semantic hue. Recommended: neutral monochrome base with small accent ticks.

## 3. Typography

### Chinese

Preferred open/system-safe stack:

`"Noto Sans SC", "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif`

### English / numerals

`Inter, "Noto Sans", "Source Sans 3", Arial, sans-serif`

For offline HTML, do **not** load remote fonts. Use installed/system fallbacks unless redistributable local font assets are explicitly included and licensed.

## 4. Type scale

### A0

- board title: 34–44 pt;
- section title: 22–28 pt;
- figure conclusion: 18–22 pt;
- body: 16–18 pt;
- annotation: 14–16 pt;
- absolute minimum essential label: 12 pt.

### A3

- title: 20–24 pt;
- section: 14–17 pt;
- body: 9.5–11 pt;
- annotation: 8.5–10 pt;
- essential minimum: 8 pt.

### HTML

- H1: clamp(32px, 4vw, 56px)
- H2: 30–36 px
- H3: 22–26 px
- body: 16–18 px
- metadata: 13–14 px
- line-height body: 1.55–1.7

## 5. Numerical typography

- use tabular numerals for metrics tables;
- never imply false precision: derived/assumed values should retain appropriate significant figures;
- version labels use monospaced numerals only as a small secondary device, not as the whole brand.

## 6. Contrast

Target WCAG 2.2 AA for HTML text wherever practical: 4.5:1 normal text, 3:1 large text and essential UI graphics. Print must also pass grayscale proofing.

## Checkpoint — Phase 3

Palette and type scale are executable. Final font files are intentionally not embedded by this workstream; Integration must respect redistribution licenses.