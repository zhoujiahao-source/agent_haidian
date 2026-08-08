# Pixel-level Inspection — Legacy Five Core Figures

Status: **completed** against the existing candidate branch `submission/zhoujiahao-source/jingzhang-legible-ai-belt`.

## Method

The five PNG files were fetched as repository blobs and decoded without OCR. Each file was opened at native resolution and inspected visually.

All five are **400 × 225 px**, indexed-palette PNGs:

| figure | blob SHA | bytes | native size |
|---|---|---:|---:|
| `site-overview.png` | `c130ed49b4977f2964de09328bce46b9509d657e` | 1406 | 400×225 |
| `land-use-structure.png` | `0cc6c46cebbf33e451131929893060605850aa89` | 1251 | 400×225 |
| `key-areas.png` | `8a4d4c60576ca3b7227fcfced3ff8a5320a0a77c` | 1247 | 400×225 |
| `mobility-bluegreen.png` | `3e3684b56e08474d19f922467de49130f9f26bc1` | 1297 | 400×225 |
| `metrics-evidence.png` | `3fe4eb7055474333c76b554c11ca665d3944d1ef` | 1198 | 400×225 |

## Findings by figure

### `site-overview.png`

Observed: a dark header strip, one vertical green line with three colored circular nodes, and three mostly empty callout rectangles.

Missing for a professional site overview:

- no geographic/site basemap;
- no boundary or provisional-boundary notation;
- no named areas;
- no Capability Backbone spatial relationship;
- no figure title inside the image;
- no legend, source note, evidence tag or scale/context.

Decision: **REBUILD**.

### `land-use-structure.png`

Observed: three empty bordered cards with colored side bars and one horizontal line with three nodes.

Missing:

- no land-use polygons or spatial structure;
- no land-use categories;
- no geographic relationships;
- no labels, legend, evidence status or source note.

Decision: **REBUILD**.

### `key-areas.png`

Observed: three vertically framed boxes with different top/accent colors and an inner rectangular frame.

Missing:

- no map or key-area geometry;
- no names or roles of the three areas;
- no relationship to the overall site;
- no evidence/provisional status.

Decision: **REBUILD**.

### `mobility-bluegreen.png`

Observed: four horizontal blue lines crossing one vertical green band, plus three empty legend-style boxes.

Missing:

- no real road/rail/slow-mobility context;
- no continuous blue-green network geography;
- no labels, crossings, nodes or hierarchy;
- no source or confidence state.

Decision: **REBUILD**.

### `metrics-evidence.png`

Observed: six empty card frames with blue header bars and one wide red bar at the bottom.

Missing:

- no metric names;
- no values;
- no formula or source;
- no confidence/evidence status;
- no Urban Adaptation Rate explanation.

Decision: **REBUILD**.

## Conclusion

The previous file-size warning is now replaced by direct visual evidence: all five files are minimal schematic placeholders, not evidence-dense professional urban-design figures. They should not be reused as final figures or merely recolored.

Integration should regenerate all five from authoritative/declared machine-readable data under the Window 5 figure grammar. This inspection does **not** authorize Window 5 to edit the canonical submission itself.
