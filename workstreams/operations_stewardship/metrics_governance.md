# Metrics Governance｜公共价值指标治理

> Status: **Proposed operations/measurement contract**. This file does not set an official project KPI, statutory threshold, or government performance target. Exact formulas, cohorts and thresholds remain subject to the Metrics/Governance integration pass and competent professional review.

## 1. Purpose

The operating system needs a metric that rewards verified improvement of urban problems rather than the number of AI systems deployed. The locked concept calls this **Urban Adaptation Rate (UAR)**. Window 6 defines the governance contract around that metric so it cannot be turned into a deployment counter.

The invariant is:

**problem lifecycle is the denominator → verified public-value improvement is the numerator → common safeguard floors constrain every scenario → Responsible STOP remains visible as learning but is not silently reclassified as improvement.**

## 2. Candidate definition for Integration

A candidate cohort-based expression is:

```text
UAR(t, cohort) = verified_improved_problem_records / evaluable_qualified_problem_records
```

Where:

- `evaluable_qualified_problem_records` are Problem Track records admitted into the declared cohort before outcomes are known and for which the evaluation window has closed or a terminal decision has been made;
- `verified_improved_problem_records` are those records for which the pre-declared public-value outcome improved against the baseline/counterfactual to the required confidence **and** all applicable common safeguard floors were satisfied;
- all cohort inclusion/exclusion rules, evidence windows and changes are versioned before results are observed.

This is a **candidate formula**, not a final official metric. The Metrics workstream / Final Integration Agent must define the exact denominator, evaluation window, minimum effect, confidence test and treatment of unresolved records.

## 3. What UAR must not become

UAR must not be calculated from:

- number of AI deployments;
- number of models, robots, sensors or screens installed;
- number of challenge submissions;
- model accuracy alone;
- uptime alone;
- publicity reach, event attendance or developer registrations alone;
- raw count of pilots that reached `SCALE`;
- retroactively edited cohorts that remove failed trials.

A technically successful capability can still fail to improve public value. A non-AI intervention may be the best solution and should not be treated as an operating-system failure.

## 4. Common safeguard floors

Every scenario-specific success metric sits below these common floors. Integration should express each floor as an auditable record with status, evidence and limitations rather than assume a numeric threshold where no authoritative threshold is available.

| floor | minimum governance question | examples of evidence | current threshold status |
|---|---|---|---|
| Safety | Did operation remain within pre-declared physical/operational risk limits? | incidents, near misses, manual takeover, stop events | exact project threshold Unknown |
| Privacy & data | Was data use necessary, proportionate, authorized and consistent with declared purpose? | data map, provenance, minimization, retention/cleanup status | capability-specific legal review required |
| Fairness & distribution | Did a subgroup bear materially worse burden or exclusion? | subgroup outcomes, accessibility failures, complaint patterns | exact statistical test Unknown |
| Accessibility & human alternative | Could people use the public service without an inaccessible or coercive AI-only path where relevant? | alternative route audit, accessibility testing, human-channel availability | capability-specific |
| Environment & energy | Did the intervention create disproportionate energy, material, noise or environmental burden? | energy/material measurements, environmental logs | scenario-specific |
| Cost & maintainability | Is the public-value gain credible against lifecycle cost and maintenance burden? | maintenance record, failure/repair, migration/exit cost | budget/threshold Unknown |
| Human override & contestability | Could material failures/outcomes reach accountable human review? | override logs, complaint/appeal records, response chain | legal route/SLAs Unknown |

Failure of an applicable floor prevents that record from being counted as verified public-value improvement even if the primary benefit metric improved.

## 5. Scenario-specific metrics

Scenario-specific metrics are selected before trial and linked to the actual urban problem. Examples of metric forms include:

- time to reach a human public service;
- successful accessible wayfinding rate for a defined user group;
- heat exposure reduction under declared conditions;
- conflict/near-miss reduction in a bounded mobility experiment;
- maintenance response and service-continuity performance;
- resource/energy reduction per verified service outcome.

These are examples of forms, not project facts or official targets.

## 6. Responsible STOP and learning

`RESPONSIBLE STOP` is a valid institutional learning result. It is **not automatically a UAR numerator**.

Recommended separation:

- `urban_adaptation_rate`: measures verified public-value improvement;
- `responsible_stop_count`: records trials/problems deliberately stopped for risk, weak value, insufficient evidence, maintenance failure, legitimacy failure or superior alternatives;
- `learning_record_completion_ratio`: optional governance-quality indicator for whether terminal decisions include reason, evidence, affected groups, cleanup and next action.

This preserves both truths: a STOP can demonstrate healthy governance, while UAR continues to mean actual verified improvement rather than “anything we learned from.”

## 7. Anti-gaming contract

1. Freeze cohort rules before reading outcomes.
2. Preserve every qualified problem record, including failures, unresolved cases and non-AI resolutions.
3. Version any metric/baseline/population change and explain why it changed.
4. Publish subgroup/distributional results where lawful and methodologically appropriate; do not rely only on averages.
5. Never count a registry entry, repository merge, event display or pilot authorization as public-value improvement.
6. Treat missing data as `Unknown`, not zero and not success.
7. Distinguish measurement uncertainty from operational failure.
8. Preserve source files and calculation logic so the annual City Version Release can be reproduced.

## 8. Mapping to the repository `metrics.schema.json`

The current schema permits custom metric keys. A future integrated entry can therefore be represented without changing the schema, for example:

```json
{
  "urban_adaptation_rate": {
    "status": "unknown",
    "value": null,
    "unit": "ratio",
    "source_files": [
      "problem_registry.json",
      "city_version_release.json"
    ],
    "formula": "verified_improved_problem_records / evaluable_qualified_problem_records",
    "confidence": "unknown",
    "assumptions": [
      "Candidate operations formula; cohort/window/effect threshold require Metrics and professional confirmation."
    ],
    "reason": "No approved evaluation cohort or verified outcome dataset exists in the current concept package."
  }
}
```

The example is intentionally `unknown`; Window 6 does not fabricate a baseline or score.

## 9. Annual release relationship

City Version Release is the audit surface for UAR. Each annual release should show:

- cohort definition and changes;
- numerator/denominator counts;
- records excluded and why;
- confidence/limitations;
- subgroup/distributional findings;
- Responsible STOPs;
- unresolved problems;
- metric definition/version changes;
- source/evidence links.

A headline ratio without those records is not considered auditable.

## 10. Open decisions for Final Integration

- exact observation/evaluation window;
- minimum public-value effect and confidence requirement;
- treatment of long-running or unresolved problems;
- whether cohorts are annual, rolling or both;
- which common floors are universally applicable versus scenario-triggered;
- which body signs off methodological changes;
- privacy-preserving rules for subgroup reporting;
- how non-AI resolutions are represented in the headline and companion indicators.

Until these are formally resolved, UAR remains **Proposed / Unknown**, not an official performance claim.