# Custom AI-City Metrics Catalog

All metrics below are **candidates** for Integration Agent review. They define formulas and data contracts; they do not assert operational values. Unless measured from a future governed registry, status remains `unknown` and value remains `null`.

| metric | unit | readiness | formula / interpretation | current status | anti-gaming control |
|---|---|---|---|---|---|
| `urban_adaptation_rate_90d` | ratio | schema-ready | adapted issues due by 90d / eligible issues due by 90d | future monitoring | fixed cohort; no denominator deletion; STOP separate |
| `urban_adaptation_rate_365d` | ratio | schema-ready | durably adapted issues due by 365d / eligible issues due by 365d | future monitoring | registered horizon; unresolved cases visible |
| `stop_compliance_rate` | ratio | schema-ready | timely halted experiments after verified stop trigger / experiments with verified stop trigger | future monitoring | independently sample triggers and late stops |
| `learning_closure_rate` | ratio | schema-ready | closed experiments with postmortem + archived learning / all closed experiments | future monitoring | includes failed/inconclusive/STOP cases |
| `median_time_to_adaptation_days` | none | schema-ready | median(adaptation confirmed - eligible issue accepted), days | future monitoring | stratify severity; do not delay hard intake |
| `public_value_target_achievement_rate` | ratio | schema-ready | experiments meeting predeclared public-value target / experiments due for review | future monitoring | targets frozen before result review |
| `equity_floor_pass_rate` | ratio | schema-ready | reviewed experiments without material equity-floor failure / applicable reviews | future monitoring | do not infer sensitive attributes just to fill metric |
| `human_override_effectiveness_rate` | ratio | schema-ready | sampled required override events with timely authoritative successful intervention / sampled required override events | future monitoring | button availability alone is not effectiveness |
| `choice_and_consent_coverage_rate` | ratio | schema-ready | exposures with required notice/choice/consent control / exposures where required | future monitoring | applicability set by governance/legal review, not vendor choice |
| `complaint_resolution_within_sla_rate` | ratio | schema-ready | valid complaints resolved within registered SLA / valid complaints due | future monitoring | show channel visibility and repeat complaints too |
| `incident_detection_latency_days` | none | schema-ready | median(detected_at - incident start/best estimate), days | future monitoring | unknown start stays unknown, never zero-filled |
| `rollback_readiness_rate` | ratio | schema-ready | active capabilities with current passed rollback/safe-stop test / capabilities requiring test | future monitoring | paper plans do not count as drills |
| `capability_transfer_revalidation_rate` | ratio | schema-ready | cross-context transfers completed after required target revalidation / transfers requiring revalidation | future monitoring | source-area success cannot waive target review |
| `data_minimization_compliance_index` | index | design-defined | auditable necessity/minimisation/retention/access/deletion component index | future audit | components and exceptions remain visible |
| `vendor_exit_readiness_index` | index | design-defined | auditable export/substitution/continuity/exit/decommission/portability components | future audit | prefer tested portability over paper plan |
| `manual_intervention_disclosure_rate` | ratio | schema-ready | disclosed material manual interventions / material interventions found by audit | future monitoring | audit-derived denominator exposes hidden labour |
| `manual_fallback_availability_rate` | ratio | schema-ready | applicable public-service capabilities with tested human/non-AI fallback / applicable capabilities | future monitoring | test fallback under realistic outage |

## Readiness classes

- **schema-ready** — formula fits current `metrics.schema.json`; real value needs issue/experiment/incident/operations records.
- **design-defined** — governance concept is defined, but operations must adopt an auditable component rubric before publishing an index.

## Required reporting rules

1. Show numerator and denominator for ratios.
2. Show registered time window, cohort and metric version.
3. Show confidence, coverage and missingness.
4. Show relevant subgroup/worst-case evidence without inventing sensitive attributes.
5. Keep STOP/MODIFY/incidents/complaints/manual intervention visible.
6. Preserve old metric versions when definitions change.
7. Do not compare materially different denominators/horizons without explanation.

## Priority first dashboard set

Start with UAR-90, UAR-365, Stop Compliance, Learning Closure, Public Value Target Achievement, Equity Floor Pass, Rollback Readiness and Manual Fallback Availability. Add the deeper audit metrics after reliable operational logs exist.

## Planning-metric separation

These AI-city metrics do not replace required land-use, area, FAR, density, green/public-space, road or phasing metrics. Missing official planning controls remain `unknown`; governance innovation cannot manufacture planning certainty.
