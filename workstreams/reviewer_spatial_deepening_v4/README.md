# Reviewer Spatial Deepening v4

This workstream advances the Jing-Zhang Urban Capability Exchange from compliance-complete design package to reviewer-facing spatial proof without pretending that the project is already an operating city system.

## Goals

1. **Reviewer-first spatial design** — the three key areas must be distinguishable in 30 seconds through urban form, public rooms, movement, ground-floor logic, blue-green function, ordinary-city baseline and evidence status.
2. **Key-area 3D realism** — the supplementary Three.js twin loads OSM candidate buildings/roads/rail only for the active key-area bbox, uses real footprints and height/levels where available, and keeps Derived planning rooms visually separate.
3. **Exact-head validation** — apply the deepening to a clean formal branch, then rerun the current upstream `render_proposal_html.py`, `self_check_submission.py` and `participant_preflight.py` against the exact upstream main SHA resolved during CI.

## Branches

- Formal target: `submission/zhoujiahao-source/jingzhang-urban-capability-exchange-v4-reviewer`
- Integration: `integration/reviewer-spatial-deepening-v4`
- Formal base: v3 final `3fde1ebe2e125414ab38e5b3c83f1f0516b00c15`

## Spatial proof contract

Every key area must answer:

- What is the distinct urban role?
- Where is the core public room?
- How does an ordinary person move through it?
- What is the ground-floor/public-edge relationship?
- How does blue-green infrastructure support ordinary public life?
- Where does AI move backstage?
- What remains available when AI or an experiment stops?
- Which facts are Official / Verified / Derived / Proposed / Unknown?

All new reviewer rooms remain **Derived / Not yet canonicalized** until professional review. No statutory FAR, height, ownership, road redline, green-space legal status or engineering capacity is inferred.

## Three key-area proofs

- **Zhongzhiyuan / Verification Campus** — Verification Commons Court, Bounded Test Yard, Governance Review Hall, Ordinary Bypass.
- **AI Origin / Learning Neighborhood** — Campus-Neighborhood Learning Commons, Inclusive Service Court, TOD Walking Gate, Low-disturbance Renewal Edge.
- **Dazhongsi / Market & Service Commons** — Four-Quadrant Walking Stitch, Market Service Street, Night Urban Living Room, Green Mobility Court.

## Outputs

- `spatial_deepening.json` — one shared spatial-detail contract.
- `apply_reviewer_deepening.py` — idempotently patches bilingual proposal, builds bilingual SVG reviewer atlas, updates changelog/manifest.
- `threejs/keyarea_reviewer_twin.html` — supplementary WebGPU reviewer twin with on-demand OSM candidate context.
- `.github/workflows/reviewer-spatial-deepening-v4.yml` — exact-head validation and formal-branch update.

## Three.js truth boundary

The reviewer twin is **supplementary**, online and non-formal. It does not replace `visual/index.html`. OSM is candidate context under ODbL. Canonical GeoJSON remains authoritative. 3D qualitative massing and Spatial Proof Rooms are reviewer design interpretation only.
