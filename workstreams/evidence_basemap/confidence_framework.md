# Confidence & Uncertainty Framework

## Data classes

| class | meaning | allowed use | prohibited promotion |
|---|---|---|---|
| Official | Explicit official/cleared project fact or official geospatial/control dataset appropriate to the claim. | Formal claim within the source's stated scope. | Extending beyond source scope. |
| Verified | Real-world state corroborated by at least one authoritative source plus an independent check or second credible source when practical. | Existing-condition evidence and design diagnosis. | Calling it statutory approval/control. |
| Derived | Reproducible inference or calculation from cited data. | Analysis if method, inputs, date, confidence and limitation are disclosed. | Presenting as direct observation or official fact. |
| Assumed | Explicit design/research assumption made to keep work moving. | Scenario testing only. | Existing-condition statistics or formal control. |
| Unknown | Material fact cannot be supported with current public/cleared evidence. | Missing-data register; sensitivity/next-survey planning. | Guessing a value to complete a table/map. |

## Drawing classes

| class | visual rule | interpretation |
|---|---|---|
| Known | solid outline + direct label/source ID | supported existing state |
| Estimated | dashed outline + estimate tag | derived approximation with method |
| Proposed | distinct proposal symbol/label | future design suggestion only |
| Unknown | hatch/question marker + missing-data ID | intentionally unresolved |

Do not rely on color alone; line type, boundary style, label and symbol must also encode certainty for monochrome printing and color-vision accessibility.

## Cross-check protocol

1. Ask whether the claim is statutory/formal or physical/current-state.
2. For statutory claims, use the competent official source; do not let OSM, imagery, news diagrams or reference-area arithmetic override it.
3. For physical state, prefer official open data; use OSM/public imagery/credible publications as independent checks where licensing permits.
4. Record publication/retrieval date, temporal coverage, spatial coverage, license/reuse status and transformation.
5. If sources conflict, keep both in `source_conflicts.md`; do not silently overwrite.
6. If no defensible proxy exists, use Unknown.

## Confidence notation

- High: authoritative source fit for the claim and independently consistent.
- Medium: authoritative or credible source exists but time/spatial precision is limited, or cross-check is incomplete.
- Low: single non-authoritative clue or substantial inference; normally remains Derived/Assumed and should not drive irreversible design.
