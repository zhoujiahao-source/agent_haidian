# Experiment Protocol｜城市 AI 试验协议

## 1. Minimum experiment card

Every experiment record must include at least:

- `experiment_id`
- `eligible_issue_ids`
- `capability_id` and immutable `capability_version`
- `problem`
- `baseline`
- `hypothesis`
- `target`
- `control_or_comparator`
- `population_space`
- `exclusions`
- `duration` and fixed review/expiry date
- `data` (categories, source, minimum necessary fields, retention, provenance)
- `risk_tier`
- `authorization_ref`
- `human_owner`
- `mandatory_reviewers`
- `public_notice`
- `consent_mode_or_lawful_basis_record`
- `human_override`
- `stop_conditions`
- `rollback`
- `primary_public_value_metric`
- `guardrail_metrics`
- `equity_subgroups_or_reason_not_applicable`
- `incident_logging`
- `version_log`
- `next_decision_date`

## 2. Baseline rule

A baseline is not a decorative “before” number. Record:

- measurement period;
- data source and status (`Official / Verified / Derived / Assumed / Unknown` where relevant);
- spatial/population coverage;
- missingness;
- seasonal/event effects;
- known confounders;
- whether the baseline itself creates privacy or equity risks.

If a defensible baseline cannot yet be measured, the first experiment phase is baseline establishment—not a success claim.

## 3. Target rule

Targets must be predeclared and tied to the public problem. This workstream does **not** invent universal percentages. A target record must state:

- direction of improvement;
- minimum meaningful change;
- required confidence/coverage;
- guardrails that cannot be traded away;
- subgroup/worst-case conditions;
- target owner and rationale.

## 4. Comparator hierarchy

Use the strongest practical comparison:

1. controlled/randomised comparison when lawful, ethical and operationally plausible;
2. staggered or matched comparison;
3. before/after with confounder analysis;
4. shadow mode / simulation against a non-AI baseline;
5. structured expert/operational benchmark when stronger comparison is impossible.

The absence of a randomised trial does not invalidate a city experiment, but weaker designs must lower confidence and narrow claims.

## 5. Monitoring families

Monitor more than the primary KPI:

- public outcome;
- safety incidents and near misses;
- equity distribution and worst-performing subgroup/quantile;
- privacy/data events;
- human overrides and manual interventions;
- complaints/appeals/opt-outs;
- reliability and failure detection;
- environmental/resource burden;
- operating and exit cost;
- vendor/dependency risk.

## 6. Predeclared stop triggers

Every pilot must define machine-detectable and/or human-detectable triggers. Typical categories:

- serious safety event or unacceptable near miss;
- privacy/security breach or unauthorised data use;
- material discriminatory/exclusionary effect;
- loss of required human oversight or override capability;
- data/model drift outside the approved envelope;
- inability to detect failures at the required latency;
- legal/authorisation condition no longer valid;
- dependency outage with unsafe/no-service fallback;
- predefined public-value guardrail breach;
- evidence of manipulation, metric gaming or undisclosed manual substitution.

Trigger thresholds are scenario-specific and must be approved before activation.

## 7. Incident record

At minimum:

`incident_id, detected_at, detected_by, experiment_id, capability_version, affected_scope, severity, description, immediate_action, human_owner, stop_trigger_ref, override_used, rollback_started_at, recovery_status, affected_groups, notification, root_cause_status, corrective_action, reopen_authorization_ref`.

## 8. Version discipline

Any change to the following creates a new version/review checkpoint:

- model or decision rule;
- training/reference data with material behavioural effect;
- sensor/input category;
- autonomy level;
- target population/space;
- primary metric/guardrail;
- consent/notice path;
- override/rollback mechanism;
- vendor/service dependency.

An experiment cannot quietly change its measurement definition after poor results.

## 9. Meaningful human override test

An override counts as real only if the responsible person:

1. can perceive the relevant system state in time;
2. has the authority to disregard, reverse or stop the automated action;
3. has an operational fallback after override;
4. has training and is not penalised for justified intervention.

A decorative “human in the loop” button without these conditions is not a safeguard.

## 10. Closeout

Every closed experiment receives one outcome classification:

- `adaptation_success` — meaningful public improvement confirmed;
- `responsible_stop` — stopped because guardrails/risk evidence justified stopping;
- `successful_stop` — the test demonstrated that non-deployment/retirement is the correct public-value result;
- `harmful_failure` — harm/critical breach occurred; incident remediation required;
- `inconclusive` — evidence insufficient;
- `modify_and_retest` — promising direction but safeguards/design/evidence need change.

Closeout records must include public-value decision, incidents, overrides, complaints, data deletion/retention actions, rollback status, lesson, and whether the capability/issue remains active.
