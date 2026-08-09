# Logo Optical QA — Open Node

Status: completed for digital raster and grayscale checks.

## Test matrix

Family A primary and a new small-size micro variant were rasterized at:

- 16 px;
- 20 px;
- 24 px;
- 48 px;
- 256 px.

The 48 px test approximates **4.06 mm at 300 dpi** and is therefore a useful proxy for the documented 4 mm absolute-minimum print mark. It is not a substitute for a physical print proof.

## Finding 1 — primary Family A

The full Family A communicates all intended railway DNA: two tracks, open ring/station and a switch route.

At 48 px and above: **PASS**.

At 24 px: usable, but the diagonal switch begins to compete with the negative-space opening.

At 16–20 px: the diagonal branch can merge visually with the ring and weaken immediate recognition.

## Finding 2 — micro variant

A micro variant was created for small digital uses:

- same open ring;
- same two incoming parallel tracks;
- one outgoing route retained;
- diagonal switch removed;
- stroke increased from 20/240 to 24/240.

Result:

- 16 px: **PASS** for open-node silhouette;
- 24 px: **PASS** and cleaner than the full version;
- monochrome/grayscale: **PASS** because openness and dual-track structure are geometric, not color-dependent.

## Production rule

- **≤24 px digital:** use `open-node-family-a-micro.svg` or its 16/24 px PNG exports.
- **≥32 px digital:** use full Family A.
- **≥4 mm print:** full Family A is acceptable based on the 48 px / 300 dpi proxy.
- **<4 mm print:** do not approve by proxy; use the micro form only after an actual physical print proof.
- Never restore the diagonal switch at micro sizes merely for conceptual completeness.

## Family B / C

Family B remains better as a network/cartographic glyph; at 16 px its two vertical rails and intersecting arcs crowd together.

Family C is the simplest at small size but reads more strongly as a terminal/milepost/version device than as the primary exchange mark.

Therefore the earlier recommendation remains:

1. Family A primary;
2. Family A micro for small output;
3. Family B map/network glyph;
4. Family C version/archive secondary device.

## Remaining production-only check

A physical vendor proof with the final paper, ink/toner, output device and ICC workflow remains external to this Agent runtime. This is the only unresolved logo production QA item.
