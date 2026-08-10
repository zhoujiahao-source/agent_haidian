# Final Acceptance v3 — 100-item P0/P1/P2 matrix

This workstream turns the five project-level completion principles into 100 executable acceptance checks and binds each check to the current canonical submission.

- Upstream rules frozen for this pass: `6405afe0ce1f23e1b7056e30c0fe12fe3c59ecab`
- Canonical base: `815f21207e72ffdcd3caf2bc2943c853b032cfda`
- Formal target branch: `submission/zhoujiahao-source/jingzhang-urban-capability-exchange-v3-final`
- Target maturity: **competition-grade high-fidelity City Learning OS design prototype / L4-ready**
- It is **not** an implemented autonomous city system.

## Acceptance structure

| Category | Items |
|---|---:|
| Complete urban design | 30 |
| Complete city-learning mechanism | 20 |
| Complete AI governance | 20 |
| Complete evidence architecture | 15 |
| Complete competition delivery | 15 |
| **Total** | **100** |

Priority split:

- P0: 50 — submission-critical / must be true before formal PR
- P1: 34 — professional completeness / governance / depth
- P2: 16 — organizer-blocked, human-required, or post-competition L4 transition

Current state after the v3 standard-matrix alignment:

- COMPLETE: 87
- IN_PROGRESS: 0
- BLOCKED_OFFICIAL_DATA: 3
- HUMAN_REQUIRED: 10

## Status contract

`COMPLETE` means there is current repository evidence that satisfies the acceptance test at competition-prototype depth.

`IN_PROGRESS` means the Agent can still finish it in this pass.

`BLOCKED_OFFICIAL_DATA` means completion would require organizer-supplied exact geometry or statutory/engineering data. It must not be closed by invention.

`HUMAN_REQUIRED` means the item depends on field observation, public/professional participation, final human judgment, real operation, or authorization that an AI Agent cannot fabricate.

## Rules

1. Never convert `BLOCKED_OFFICIAL_DATA` into `COMPLETE` by estimating an official polygon, statutory FAR/height, ownership, road redline, heritage boundary, or engineering capacity.
2. Never convert live-systems metrics such as UAR, STOP rate, human-override success, complaint resolution, or transfer revalidation into known values from simulation.
3. OSM remains candidate public context under ODbL, not an official survey.
4. Supplementary Three.js work is design simulation; it never overrides canonical GeoJSON.
5. The final upstream submission branch must modify only `submissions/zhoujiahao-source/jingzhang-legible-ai-belt/`.

## Files

- `acceptance_matrix.json` — 100 machine-readable acceptance checks.
- `validate_acceptance.py` — deterministic workstream validator.
- `.github/workflows/final-acceptance-v3.yml` — validates the formal branch using the latest upstream scripts and updates generated formal artifacts on success.

The workflow deliberately keeps orchestration files outside the formal submission branch so an eventual upstream PR can remain submission-directory-only.

## Latest successful validation

- Upstream: `d444c44b8252bf6f7e558443924717bafade90e6`
- Formal branch SHA: `3fde1ebe2e125414ab38e5b3c83f1f0516b00c15`
- Agent-executable acceptance items remaining: **0**
