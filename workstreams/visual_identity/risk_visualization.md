# Risk Visualization

This system answers **“What level of public authorization / scrutiny is required?”** It is not the experiment outcome.

## 1. Risk set

- `R1 LOW`
- `R2 MEDIUM`
- `R3 HIGH`

## 2. Visual grammar

| Level | Symbol | Border | Text requirement | Default implication |
|---|---|---|---|---|
| R1 LOW | shield with 1 notch | single | `R1 LOW` | reversible, bounded, low-impact trial possible |
| R2 MEDIUM | shield with 2 notches | double | `R2 MEDIUM` | professional approval / added controls |
| R3 HIGH | triangle-shield with 3 notches | heavy double | `R3 HIGH` | stricter authorization; public deliberation where needed |

Color accents may be green/brown/red but are secondary and must not stand alone.

## 3. Risk label placement

- scenario cards: top-right fixed risk block;
- maps: small attached shield adjacent to scenario node, not the node itself;
- dashboards: dedicated risk column;
- annual release notes: risk appears before change decision if the capability affects individuals or critical public systems.

## 4. Human override

Any R2/R3 public interface depiction should include a visible Human Override icon or label. R3 diagrams should also show authorization owner and exit/appeal route.

## 5. Failure-safe wording

Do not write “AI decides.” Use `Agent proposes/diagnoses → authorized process → human/public responsibility`.

## 6. Accessibility

- minimum 24 px digital icon box / 5 mm print;
- shape + R-number + word label;
- do not depend on hue or saturation;
- use at least 3:1 non-text graphic contrast against adjacent background in HTML.

## Phase 6 checkpoint

Complete: independent low/medium/high risk grammar with human-responsibility cues.