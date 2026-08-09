# City Learning Metrics Specification

## Status

This file defines **proposed custom metrics** for the City OS concept. It does not invent current observed values. Conventional planning metrics required by the official schema remain mandatory and authoritative where computable from geometry.

# 1. Metric design principles

Every custom metric must be:

1. connected to a real public problem;
2. interpretable by non-specialists;
3. reproducible from documented inputs;
4. resistant to simple gaming;
5. decomposable by area / group / time where relevant;
6. explicit about current data availability;
7. able to record STOP / retirement as learning rather than hide it.

# 2. Flagship metric — Urban Adaptation Rate (UAR)

## 2.1 Concept

**Urban Adaptation Rate｜城市适应率** asks:

> Of the urban problems that entered a qualified city-learning cycle, what share produced a verified improvement or a verified risk-reducing learning outcome within the review period?

It must not reward simply launching more pilots.

## 2.2 Recommended unit of analysis

Use **qualified learning cases**, not raw AI deployments.

A case enters the denominator only after `QUALIFY` determines that:

- a real problem / need is defined;
- baseline evidence is sufficient for a test;
- a public-value evaluation plan exists.

This prevents the metric from being improved by creating many trivial “problems”.

## 2.3 Recommended formula

For review period `t`:

`UAR_t = (N_improved + w_stop × N_safe_stop + w_learning × N_verified_learning) / N_matured_cases × 100%`

Where:

- `N_improved` = matured cases with verified positive public-value outcome and acceptable mandatory-baseline thresholds;
- `N_safe_stop` = matured cases intentionally stopped because review identified unacceptable risk / inequity / privacy / cost / negative public value before scaling, with the failure documented and harmful continuation avoided;
- `N_verified_learning` = other matured cases that did not improve the target condition but produced a documented, reusable learning outcome that changes future policy / design / transfer rules;
- `N_matured_cases` = qualified cases whose planned review window has been reached;
- `w_stop` and `w_learning` = policy weights between 0 and 1 chosen transparently by the proposed governance institution.

### Competition-package recommendation

Do **not** assign an observed numerical UAR value unless a real compatible case dataset exists.

Formal status should likely be:

- definition: `proposed`
- current value: `unknown`
- future monitoring: `required`
- formula: fully documented

If the schema does not allow weighting syntax directly, store the conceptual formula and assumptions in the supported fields rather than forcing an invalid structure.

## 2.4 Why STOP receives partial learning credit

Without partial learning credit, teams are incentivized to keep weak pilots alive or hide failures.

A safe STOP receives credit only if:

- the original problem was legitimate;
- the test had a defined review process;
- stopping was evidence-based;
- the failure / risk is documented;
- the result changes future decisions;
- the case did not create avoidable severe harm.

A failed project with poor governance should not automatically receive learning credit.

# 3. Mandatory public-value baseline dimensions

Every scenario must monitor five baseline dimensions.

## 3.1 Safety

Possible measures:

- adverse events / near misses;
- emergency fallback success;
- unsafe recommendation / route incidents;
- service interruption duration;
- Human Override availability / success.

## 3.2 Equity

Possible measures:

- outcome gap between vulnerable / priority groups and overall population;
- accessibility gap;
- service-coverage difference by area / time;
- opt-out penalty;
- digital-exclusion rate.

## 3.3 Privacy

Possible measures:

- proportion of scenarios requiring personal data;
- data minimization compliance;
- retention / deletion completion;
- consent withdrawal success;
- privacy incidents.

Do not invent privacy compliance as a numeric score without a defined audit framework.

## 3.4 Environment

Possible measures:

- energy / resource use change;
- heat exposure / shade benefit where applicable;
- waste / hardware retirement burden;
- ecological disturbance indicators where relevant.

## 3.5 Cost

Possible measures:

- operating cost per public-value unit;
- maintenance burden;
- human fallback cost;
- lifecycle / retirement cost;
- avoided cost where evidence supports it.

# 4. Proposed custom metric family

## M1 — Problem-to-Test Conversion Rate

`qualified problems entering an authorized pilot / qualified problems eligible for testing`

Use:

- diagnose whether governance is stuck before testing;
- never treat higher as always better because some problems should choose `NON-AI FIRST`.

Anti-gaming:

Report `NON-AI FIRST` and rejected cases separately.

## M2 — Safe Rollback Rate

`pilots requiring rollback that successfully restore the defined fallback state within target time / pilots requiring rollback`

Purpose:

Measures reversibility, not AI performance.

## M3 — Human Override Success Rate

`override requests successfully transitioned to human / non-AI fallback / valid override requests`

Disaggregate by:

- user group;
- node;
- time;
- scenario type.

## M4 — Public Value Gain (PVG)

Scenario-specific composite or vector showing improvement from baseline across mandatory + scene metrics.

Recommendation:

Prefer a **dashboard vector** over a single opaque score. If a composite is used, publish weights and raw component values.

## M5 — Equity Gap Change

`post-test outcome gap − baseline outcome gap`

Interpretation depends on metric direction. Always state whether negative / positive means improvement.

## M6 — Capability Reuse Rate

`validated capability modules successfully reused after required revalidation / capability modules proposed for transfer`

Purpose:

Tests whether the Capability Backbone actually exchanges reusable capacity rather than only information.

## M7 — Cross-Area Revalidation Completion Rate

`cross-area transfers completing context revalidation / transfers requiring revalidation`

Anti-gaming:

Do not count an untested copy as reuse success.

## M8 — Experiment Transparency Coverage

`active / recently reviewed pilots with complete public-facing purpose, status, risk / consent, review and feedback information / active / recently reviewed pilots`

This is where `Legible AI` survives as a measurable transparency layer.

## M9 — Failure Documentation Rate

`stopped / materially modified cases with complete cause + lesson + next-rule record / stopped / materially modified cases`

Purpose:

Prevents disappearance of negative results.

## M10 — Retired Capability Documentation Rate

`retired significant capabilities with complete retirement record / significant retired capabilities`

Record should include:

- reason for original deployment;
- public-value history;
- failure / obsolescence reason;
- replacement / fallback;
- decommissioning note.

## M11 — Capability Half-Life / Review Age

Time since last substantive review for an active capability.

Purpose:

Expose “permanent pilots” or legacy systems that persist without re-evaluation.

## M12 — Public Need Traceability Rate

`active capabilities with a documented current public-need / problem link / active capabilities`

Purpose:

Prevent technology-supply-driven accumulation.

# 5. Scenario-specific metric examples

## Heat refuge / thermal comfort

Possible scene metrics:

- thermal comfort / heat exposure proxy;
- vulnerable-user coverage;
- shade / cool-space accessibility;
- energy / water cost;
- manual fallback availability.

## Accessibility navigation

- accessible-route success rate;
- barrier false-negative / false-positive rate;
- trip-time reliability;
- user-reported confidence;
- human assistance handoff success.

## Elderly community service

- response time;
- successful human handoff;
- service coverage;
- digital opt-out parity;
- complaint / correction rate.

## Commute / transfer

- travel-time reliability;
- missed-transfer rate;
- accessible transfer time;
- crowding / safety proxy if publicly measurable;
- conventional-wayfinding fallback success.

## Night culture / public life

- temporal use diversity;
- perceived / observed access and safety measures where responsibly sourced;
- noise / resident-impact complaint trend;
- business / public-space use balance;
- accessibility after dark.

# 6. Anti-gaming protocol

No headline metric can be interpreted without companion diagnostics.

For UAR, always report at least:

- number of diagnosed problems;
- number of qualified cases;
- number of matured cases;
- STOP / MODIFY / CONTINUE / SCALE distribution;
- vulnerable-group outcome;
- safety / privacy incidents;
- Human Override use;
- unresolved / missing-data cases.

Do not allow UAR to rise simply by:

- lowering problem ambition;
- excluding hard-to-serve populations;
- delaying review dates;
- hiding stopped projects;
- reclassifying failures as “learning” without evidence;
- launching many trivial low-risk cases.

# 7. Dashboard information architecture

## Layer 1 — Public city overview

Show:

- current city version;
- number of active / modified / stopped / scaled capabilities;
- UAR status / value only if valid;
- key public-value changes;
- unresolved priority problems;
- evidence / uncertainty legend.

## Layer 2 — Area / capability view

For each three-area / two-wing learning unit:

- active capabilities;
- primary role;
- recent tests;
- transfer relationships;
- local public-value outcomes;
- next review.

## Layer 3 — Experiment detail

For each pilot:

- problem;
- capability;
- evidence class;
- risk tier;
- data / consent mode;
- Human Override;
- baseline;
- current indicators;
- failures / complaints;
- decision history;
- next review.

## Layer 4 — Archive

- stopped cases;
- retired capabilities;
- version history;
- failure lessons;
- replacement relationships.

# 8. Metric status model for formal submission

Use current official schema fields where available. Conceptually, distinguish:

- `computed_current` — reproducible from current geometry / real evidence;
- `derived_proxy` — current value derived from documented public proxy;
- `proposed_monitoring` — future operational metric with formula but no observed value;
- `unknown` — formula / target not justified by available evidence.

Never invent a numeric value solely to make the metrics panel look complete.

# 9. Conventional planning metrics remain required

This custom family supplements, never replaces, required planning metrics such as:

- site area;
- land-use areas;
- total floor area;
- FAR;
- building density;
- green area / ratio;
- public-space area / ratio;
- road area / ratio;
- phase areas;
- key-area count / areas.

If official planning controls are missing, current design metrics must be described as proposal / geometry-derived values, not statutory approvals.

# 10. Figure-ready metrics story

The final `metrics-evidence.png` should not become a wall of numbers.

Recommended hierarchy:

1. Conventional spatial metrics — what the geometry says.
2. Evidence / uncertainty legend — how certain the base is.
3. Urban Adaptation Rate — how city learning will be evaluated.
4. Public-value five baseline dimensions.
5. Example scenario metric chain — baseline → test → review → decision.
6. Anti-gaming / vulnerable-group check.

# 11. Validation checklist

Before inserting a custom metric into canonical `metrics.json`:

- [ ] official current metrics schema re-read;
- [ ] field names / enums valid;
- [ ] formula documented;
- [ ] source files identified;
- [ ] unit defined;
- [ ] current / proposed status unambiguous;
- [ ] no invented value;
- [ ] assumptions recorded;
- [ ] confidence recorded where supported;
- [ ] narrative and figure use the exact same definition.
