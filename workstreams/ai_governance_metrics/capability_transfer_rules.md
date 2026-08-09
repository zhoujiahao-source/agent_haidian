# Capability Transfer & Revalidation Rules

## 1. Core rule

`SCALE` means a capability is suitable for a **defined validated context**. It does not mean “copy everywhere.” Moving a capability to a materially different Learning Unit is a new governance event called `TRANSFER_REVIEW`.

## 2. Transfer evidence package

A source-area capability offered through Capability Backbone carries:

- capability ID/version and owner;
- eligible issues addressed;
- source-area baseline and population/space context;
- public-value decision and confidence;
- safety/equity/privacy/environment/cost findings;
- incidents, near misses, complaints and overrides;
- data categories and provenance;
- autonomy and human-override design;
- dependency/vendor architecture;
- rollback/retirement evidence;
- known failure boundaries and unresolved questions.

Capability Backbone exchanges this **evidence-bearing capability record**, not just code/model weights.

## 3. Material context changes that trigger revalidation

Revalidate when any material change occurs in:

1. population, accessibility need or affected subgroup;
2. physical/public-space geometry or traffic/safety context;
3. data source, distribution, quality or legal basis;
4. model/rule/capability version;
5. autonomy or actuation authority;
6. service entitlement/rights impact;
7. responsible institution, operator or human workflow;
8. network/infrastructure/fallback environment;
9. vendor/dependency or exit conditions;
10. risk tier or failure detectability.

A “similar district” label is not evidence of transferability.

## 4. Transfer gates

### T1 — Source evidence complete
The source case has a signed public-value outcome and unresolved risks are visible.

### T2 — Context comparability review
Target owner documents what is similar, different and unknown. Unknown critical differences force local evidence collection.

### T3 — Re-tier risk
Apply the target context to the eight risk dimensions. Risk can go up even if the source pilot was Low/Medium.

### T4 — Target baseline
Measure the target problem before claiming that the source capability is needed or likely to improve it.

### T5 — Local authorisation
The target Public Steward accepts responsibility. Source authorisation does not transfer automatically.

### T6 — Shadow/sandbox where feasible
Validate data/operational compatibility without exposing the public to full autonomous behaviour.

### T7 — Bounded revalidation
Run the smallest useful target-context experiment with local guardrails and stop/rollback.

### T8 — Target decision
Issue `TRANSFER_READY`, `MODIFY_FOR_CONTEXT`, `REVALIDATE`, or `DO_NOT_TRANSFER` with evidence.

## 5. Decision meanings

- **TRANSFER_READY** — target-context evidence supports controlled adoption within the approved envelope.
- **MODIFY_FOR_CONTEXT** — public purpose remains useful but capability/workflow/safeguards must change.
- **REVALIDATE** — evidence is insufficient; continue bounded target testing.
- **DO_NOT_TRANSFER** — target need, public value or risk does not justify adoption.

## 6. UAR rule

Source-area adaptation credit belongs to the source cohort. The target area receives no UAR numerator credit until its own eligible issue and public-value review confirm target-context improvement. This prevents “transfer laundering.”

## 7. Five Learning Unit implications

- A robotics capability validated in 众智园 may need a new physical-safety and public-notice regime in 小月河 public space.
- A community public-service capability from AI 原点社区 may need new transaction, consumer and service-failure measures in 大钟寺.
- A professional-service capability routed through 中关村科技服务翼 does not automatically obtain authority to make consequential public decisions elsewhere.

These are conceptual governance examples, not fixed implementation commitments.

## 8. Retirement on transfer failure

If transfer repeatedly fails because the capability is too context-specific, unsafe, unaffordable or locked to an unsuitable dependency, archive that limitation. The city should learn “where not to deploy” rather than forcing standardisation.
