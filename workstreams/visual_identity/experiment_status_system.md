# Experiment Status System

This file defines the city-learning experiment lifecycle. It is separate from risk level and evidence status.

## 1. Status set

`TEST / STOP / MODIFY / CONTINUE / SCALE`

## 2. Badge grammar

| State | Code | Shape | Border | Meaning |
|---|---|---|---|---|
| TEST | `T` | open square | dotted | currently testing / not concluded |
| STOP | `S!` | square with terminal bar | heavy double line | stop and document learning |
| MODIFY | `M↺` | square with one reroute corner | dashed | revise before next test |
| CONTINUE | `C→` | open-right rectangle | solid | continue within current scope |
| SCALE | `↑` | expanding double frame | solid double | expand only after public-value review |

Text label always accompanies the shape in public-facing outputs.

## 3. Color accents

- TEST `#52616F`
- STOP `#8A3F52`
- MODIFY `#8A6428`
- CONTINUE `#2E6F73`
- SCALE `#365E9D`

These colors are not reused as risk colors in the same legend.

## 4. Timeline treatment

Use a station/milepost sequence:

`diagnose → authorize → TEST → review → STOP/MODIFY/CONTINUE/SCALE → archive/release`

The branch at review should look like a railway switch, reinforcing project DNA without literal train graphics.

## 5. STOP is not failure styling

STOP should not be rendered as a destructive red X. A responsibly stopped high-risk or low-value experiment is valid city learning. The badge should signal closure + archive, not shame.

## 6. Required metadata beside experiment state

When space permits include:

- experiment ID;
- current version;
- review date;
- responsible human/public body;
- risk level shown in the separate risk system;
- public-value result / reason.

## Phase 6 checkpoint

Complete: TEST/STOP/MODIFY/CONTINUE/SCALE use a distinct badge family and do not collapse into traffic-light semantics.