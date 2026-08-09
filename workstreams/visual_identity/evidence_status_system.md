# Evidence Status System

This file defines the **data/evidence provenance status** only. It must not be used to encode design proposal status, experiment outcomes or risk.

## 1. Status set

`Official / Verified / Derived / Assumed / Unknown`

## 2. Visual grammar

| Status | Primary code | Border | Fill / texture | Short tag | Meaning |
|---|---|---|---|---|---|
| Official | `O` | double solid | white / no texture | OFFICIAL | authoritative source appropriate to claim |
| Verified | `V` | solid | 10% neutral | VERIFIED | cross-checked or validated non-statutory fact |
| Derived | `D` | solid + one corner notch | 45° fine hatch | DERIVED | calculated/transformed from cited inputs |
| Assumed | `A` | long dash | sparse dot | ASSUMED | explicit design/research assumption |
| Unknown | `?` | dotted | none | UNKNOWN | unsupported / missing / intentionally not guessed |

The letter + word is mandatory when the status materially affects interpretation.

## 3. Map / chart application

- Evidence status belongs in metadata chips or an evidence rail, not as the main map color.
- If a layer contains mixed statuses, annotate features or sublayers individually rather than assigning one status to the whole board.
- `Official` is never inferred from visual precision.
- `Derived` values show method ID or source IDs in caption/footnote.
- `Assumed` can support scenario testing but should not be presented as current-city fact.
- `Unknown` remains visible; do not hide missing information by leaving an unexplained blank.

## 4. Black-and-white proof

The five statuses remain distinguishable through border/pattern/letter. Grayscale is the reference fallback; color may be added only as a small accent.

## 5. Evidence tag format

Preferred compact form:

`[D] 11.4 km² · derived display extent · SRC-...`

Preferred expanded form:

`DERIVED · method: area_calc_v2 · sources: SRC-01 + SRC-07 · confidence: medium`

## 6. Relationship to design status

Evidence status answers **“How do we know this?”**

Design status answers **“What kind of spatial statement is this?”**

A proposed feature may be supported by Official evidence; an existing feature may still be Estimated. Never merge these dimensions.

## Phase 5 checkpoint

Complete: five evidence statuses have redundant text/border/texture encoding and monochrome fallback.