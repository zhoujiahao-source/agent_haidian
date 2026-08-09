# Window 6 Validation Report｜工作流验证报告

## 1. Validation scope

This report validates the **Window 6 workstream**, not a canonical formal submission. No file under `submissions/**` was edited by this branch, so repository submission commands such as render/finalize/self-check/participant-preflight are correctly deferred to Final Integration.

Validation date: 2026-08-08.

## 2. Methods used

1. GitHub connector readback of workstream root, `audit/` and `templates/`.
2. Independent JSON parsing of the five intended template structures.
3. Cross-check against the attached Window 6 manual's required-output list, phase checkpoints and completion gate.
4. Re-read of current upstream Skill, taskbook, sources, data workflow, review rubric, planning limits, standards/index/reference snapshots and schemas.
5. Audit of the historical user submission's manifest, self-check, metrics, assumptions, sources, geometry/presentation metadata, matrices, PR/workflow status.
6. Current legal/regulatory screening from official public national-level sources, separated from project-specific legal conclusions.
7. Duplicate Issue search and attempted upstream Issue creation for a rule wording conflict.
8. Attempted blobless sparse local clone for runtime validation; container networking failed at DNS resolution, so no false local PASS is claimed.

## 3. Required Window 6 outputs

The original required list is present:

- `public_stewardship.md`
- `role_responsibility_matrix.csv`
- `problem_track.md`
- `capability_track.md`
- `developer_ecosystem.md`
- `community_rights.md`
- `participation_model.md`
- `annual_calendar.md`
- `annual_learning_assembly.md`
- `city_version_release.md`
- `retired_capability_governance.md`
- `five_ten_twenty_years.md`
- `institutional_risks.md`
- `audit/checkpoints.md`
- `handoff.md`

Additional integration/QA artifacts now present:

- `metrics_governance.md`
- `public_governance_legal_boundary.md`
- `integration_crosswalk.md`
- `audit/legacy_submission_audit.md`
- `audit/source_evidence_register.csv`
- `audit/workstream_self_check.json`
- `audit/validation_report.md`
- five JSON integration templates under `templates/`.

## 4. Template JSON validation

Independent parse results:

| template | parse result | record type |
|---|---|---|
| `problem_challenge.template.json` | PASS | `problem_challenge` |
| `capability_proposal.template.json` | PASS | `capability_proposal` |
| `capability_registry_record.template.json` | PASS | `capability_registry_record` |
| `city_version_release.template.json` | PASS | `city_version_release` |
| `retired_capability_record.template.json` | PASS | `retired_capability_record` |

Connector directory readback also confirms all five files exist in the branch. These are explicitly marked `proposed_integration_aid_not_upstream_schema`; they must not be mistaken for official repository schemas.

## 5. Responsibility-matrix sanity check

The RACI matrix is intentionally asymmetric: the proposed public stewardship function remains `A` for core public decisions such as rule setting, risk authorization, Problem Track/public-value definition, STOP/SCALE, procurement/lifecycle funding, City Version Release and retirement authorization.

This is a design principle, not a claim that a real institution named “Public Stewardship Office” exists. The exact competent public entity remains `Unknown`.

## 6. Source/evidence audit result

PASS with limitations:

- source types are separated into official / cleared / provisional / background / legacy;
- provisional geometry remains provisional;
- official announcement area text is not treated as exact GIS redline;
- missing architecture design-depth standard body remains a data gap;
- external legal sources are screening context, not a project approval or legal opinion;
- comparative NIST/OECD/UK material remains background only.

## 7. Upstream rule conflict

Current materials express two related but differently worded propositions:

- Skill / review rubric / data workflow: organizer-missing official geometry itself must not block or penalize **content scoring**;
- `design_brief.json` and site-package source wording: provisional geometry is not sufficient for **formal professional / geometry-dependent scoring**.

This may be an intentional distinction, but the machine-readable wording can be misunderstood. No matching existing Issue was found in targeted searches.

An upstream Issue creation was attempted after duplicate search; GitHub returned:

`403 Resource not accessible by integration`

Therefore the collaboration action is **permission-blocked**, not silently omitted. Final Integration or a maintainer with Issue-write access should preserve/resolve this item.

## 8. Historical submission validation audit

The old candidate must not be treated as current validation proof because:

- manifest says `package_state=ready_for_review` but `validation_claim.self_checked=false`;
- historical self-check has only five hand-authored PASS items;
- current review contract separates deterministic, spatial, visual and professional-evidence gates;
- old validation PR head had no workflow runs/status contexts in the inspected connector result;
- five required PNGs were anomalously tiny;
- A3/A0 PDFs were approximately 1.1 KB each;
- PDF page-image inspection could not be completed in the current connector environment;
- many design-depth items are marked `complete` while site-specific professional controls remain missing/Unknown.

Result: **concept heritage reusable; validation/presentation proof must be regenerated.**

## 9. Local runtime validation attempt

A lightweight, blobless, sparse clone was attempted using the public fork and role branch. The container returned:

`Could not resolve host: github.com`

This is an environment/network failure. It is not evidence of a repository failure or success. Connector readback and independent parsing were used for checks available in this environment.

## 10. Formal submission commands intentionally not claimed

Not run by Window 6 on the canonical package:

- `render_proposal_html.py`
- `finalize_submission.py`
- `self_check_submission.py`
- `participant_preflight.py --check-push`
- maintainer four-gate review on the integrated exact head
- formal scorecard

Reason: the Window 6 manual explicitly requires an isolated role branch and says only the Final Integration Agent may modify the canonical submission directory. Running those commands against an unintegrated historical candidate would create misleading validation evidence.

## 11. Completion-gate verdict

| completion question | result | evidence |
|---|---|---|
| Institution/process over tech event? | YES | stewardship + two tracks + lifecycle |
| Clear final public accountability? | YES, conceptually | RACI; exact institution Unknown |
| Developer ecosystem + capability registry + sandbox? | YES | `developer_ecosystem.md`, Capability Track, registry template |
| Community participation beyond survey? | YES | rights + multi-mode participation + response loop |
| Annual calendar + City Version Release? | YES | continuous/Q1–Q4 + annual assembly/release |
| 5/10/20-year evolution? | YES | technology-neutral roadmap |
| Independent Problem Track and Capability Track? | YES | separate admissions, common decisions |
| Responsible STOP + retired archive? | YES | first-class release/retirement mechanisms |
| No fake institution/budget/plan facts? | YES | Proposed/Unknown status protocol |
| Current upstream/data/legal gaps disclosed? | YES | audits/register/legal boundary |
| Current canonical formal preflight? | N/A for Window 6 | must run after Final Integration |

## 12. Final validation state

**WINDOW-6 WORKSTREAM: COMPLETE FOR HANDOFF, WITH EXPLICIT EXTERNAL BLOCKERS/UNKNOWNS.**

This verdict means the role-specific work is complete and auditable. It does **not** mean the overall urban-design submission has passed current formal submission gates. That claim can only be made after all workstreams are integrated into the canonical package and the latest repository-native validation is run against the exact integrated head.