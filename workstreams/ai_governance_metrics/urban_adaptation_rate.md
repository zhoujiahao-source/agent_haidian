# Urban Adaptation Rate (UAR)｜城市适应率

## 1. Why this is the flagship metric

Urban Adaptation Rate measures how effectively a governed city-learning system converts **eligible diagnosed public problems** into verified meaningful improvement. It deliberately avoids counting raw Agent alerts, AI deployments, model calls, procurement volume or project completion as success.

UAR is a **cohort outcome metric**, not a real-time vanity counter.

## 2. Denominator: `eligible_issue`

An issue enters the denominator only after the eligibility gate in `problem_diagnosis.md` confirms:

- unique/stable issue record and duplicate control;
- legitimate public-value relevance;
- affected population/space;
- baseline or approved baseline-establishment plan;
- traceable evidence and limitations;
- alternative explanations/uncertainty;
- named human owner;
- at least one plausible intervention or reason to investigate;
- risk pre-screen.

Raw anomaly detections, duplicate complaints, unsupported correlations and synthetic “issues” created to raise throughput are excluded.

## 3. Numerator: `adapted_issue`

An eligible issue becomes adapted only when, within the declared horizon:

1. a governed intervention/response has completed the required review;
2. the predeclared minimum meaningful public outcome is achieved;
3. safety/equity/privacy/environment/cost/human-control floors do not contain an unresolved critical failure;
4. coverage and confidence meet the experiment's predeclared minimum;
5. the Public Value Review owner signs the outcome;
6. evidence is versioned and auditable.

“Project completed”, “AI deployed”, “usage increased” or “model accuracy improved” are insufficient by themselves.

## 4. Primary formula

For a cohort `C` of eligible issues accepted during a fixed intake period and an evaluation horizon `h`:

`UAR_h(C) = adapted_issues_due_by_h(C) / eligible_issues_due_by_h(C)`

Where:

- `eligible_issues_due_by_h(C)` includes only cohort issues that have reached the agreed evaluation due date for horizon `h`;
- unresolved cases remain visible as unresolved/overdue; they are never silently deleted;
- an issue may be credited once in a cohort, regardless of how many capabilities or subprojects were used.

Report numerator and denominator with the ratio.

## 5. Proposed time windows

Because urban adaptation has latency, report at least two horizons when operations exist:

### `UAR_90` — operational adaptation
Proposed 90-day horizon for issues whose near-term operational improvement can reasonably be assessed.

### `UAR_365` — durable adaptation
Proposed 365-day horizon to test persistence, rebound, maintenance and longer-tail harms.

**These horizons are design proposals, not official competition/planning requirements.** A scenario may require a different registered horizon; if so, the dashboard must explain why and must not compare incompatible cohorts as if identical.

## 6. Responsible STOP is separate from UAR numerator

A responsible decision to stop can be successful city learning but is not the same as “the problem improved.” Therefore:

- `adapted_issue` contributes to UAR numerator;
- `responsible_stop` contributes to a **Learning Safety / Stop Compliance** companion indicator;
- do not add both into one inflated “success” numerator.

This separation removes the incentive to keep risky experiments running merely to protect UAR.

## 7. Companion indicators

### Stop Compliance Rate

`experiments_halted_within_required_response_after_verified_stop_trigger / experiments_with_verified_stop_trigger`

This asks whether the city obeys its own safety governance when evidence says stop.

### Learning Closure Rate

`closed_experiments_with_public_postmortem_and_archived_learning / all_closed_experiments`

This asks whether STOP, MODIFY, inconclusive and successful experiments actually produce reusable institutional memory.

## 8. Weighting

Headline UAR is **unweighted** to preserve legibility. An optional severity/equity-weighted companion may be reported only when:

- weights are defined before outcomes are known;
- caps prevent a few large weights from dominating;
- raw unweighted UAR remains primary;
- difficult issues cannot be hidden by redefining weights;
- sensitivity results are published.

## 9. Confidence and coverage

Every UAR publication includes:

- cohort intake dates;
- horizon and evaluation due date logic;
- numerator / denominator / ratio;
- number and share unresolved/overdue;
- data coverage and missingness;
- confidence distribution;
- relevant subgroup distribution;
- number of Responsible STOPs;
- number of material incidents and manual overrides linked to the cohort;
- metric version.

No percentage is published when the denominator cannot be validly established.

## 10. Anti-gaming rules specific to UAR

1. **No alert dumping:** raw Agent alerts do not count as eligible issues.
2. **No easy-problem cherry-pick:** maintain an intake register including rejected/deferred cases and reason.
3. **No issue splitting:** one underlying public problem cannot be split into many trivial tickets solely to inflate successes.
4. **No issue merging after failure:** definitions freeze at cohort entry; material scope changes create a new version with linkage.
5. **No denominator deletion:** overdue/unsolved cohort issues remain visible.
6. **No target switching:** primary target changes require a new experiment version and cannot retroactively create adaptation credit.
7. **No success-only reporting:** STOP, MODIFY, inconclusive, incidents, complaints and overrides are published in aggregate.
8. **No average-only success:** a serious subgroup floor failure blocks adaptation credit when that floor was material.
9. **No hidden manual substitution:** material human labour required to create the apparent outcome is disclosed.
10. **No transfer laundering:** success in one area does not grant UAR credit in another before local revalidation confirms improvement.

## 11. Machine-ready proposal names

- `urban_adaptation_rate_90d`
- `urban_adaptation_rate_365d`
- `stop_compliance_rate`
- `learning_closure_rate`

All four remain `status: unknown, value: null` until a real issue/experiment registry exists. Formula readiness is not evidence of an operational value.
