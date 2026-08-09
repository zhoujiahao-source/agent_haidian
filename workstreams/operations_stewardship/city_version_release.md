# Annual City Version Release｜年度城市版本发布

## 1. Definition

A City Version Release is a public, auditable annual snapshot of how the urban capability network changed. It borrows versioning discipline from software without turning the city into a literal code repository.

Example naming is conceptual: `Jing-Zhang City v2027`, `v2028`, etc. Final naming belongs to integration/competent operators.

## 2. Required release contents

Every release should include:
1. version number and publication date;
2. Added capabilities;
3. Modified capabilities;
4. Scaled capabilities;
5. Retired capabilities;
6. Responsible STOPs;
7. major incidents / lessons appropriate for public disclosure;
8. public-value metric changes, including Urban Adaptation Rate where methodologically valid;
9. distributional / vulnerable-group findings and important outliers;
10. complaints, appeals or objections that materially changed governance or remain unresolved;
11. unresolved urban problems;
12. next-year challenge candidates;
13. capability owner/maintainer changes;
14. major dependency/deprecation/migration changes;
15. source, audit and evidence links;
16. data/geometry status and material Unknowns that affect interpretation.

## 3. Change categories

### ADDED
A capability has entered an authorized lifecycle state. Added does not automatically mean citywide production deployment.

### MODIFIED
Material changes to function, scope, model/vendor, data, interface, safeguards, owner, maintenance or evaluation. Material risk changes require reauthorization.

### SCALED
A bounded capability has expanded only after evidence, public-value/distributional review, maintenance/exit readiness and competent authorization.

### RESPONSIBLE STOP
A trial/proposal is ended because risk, value, evidence, maintenance, legitimacy or a superior alternative makes continuation unjustified. STOP is a learning outcome, not a hidden failure.

### RETIRED
A previously active/scaled capability is deliberately decommissioned. Retirement requires cleanup, continuity/replacement consideration and an archive record.

### SUSPENDED
Temporary non-operation pending incident review, maintenance, authority, evidence or external dependency. Suspension must not be misreported as retirement or successful operation.

## 4. Release evidence packet

Recommended fields per capability/change:
- `capability_id`
- old status → new status
- public-value objective
- accountable owner status
- maintainer status
- risk tier/authorization status
- evidence period and evaluation method
- metric changes + confidence/limitations
- affected-group/distributional finding
- complaint/incident/override summary links
- decision rationale
- rollback/retirement/migration status
- data/source references
- decision date and next review date

## 5. Release process

1. Freeze evidence for annual reporting while urgent incidents continue to be handled immediately.
2. Reconcile Capability Registry lifecycle states.
3. Maintainers attest current dependencies/support status.
4. Professional/research reviewers test evidence and uncertainty.
5. Community/affected-group review focuses on material changes and unresolved objections.
6. Public Stewardship makes accountable change decisions.
7. Publish machine-readable + plain-language release together.
8. Archive the exact release so later versions cannot overwrite historical decisions.
9. Carry unresolved problems into the next cycle.

## 6. Urban Adaptation Rate relationship

Urban Adaptation Rate should measure conversion from diagnosed/qualified urban problems to verified public-value improvement, not raw AI deployment. Its exact denominator/window/thresholds belong to the metrics workstream. This operations workstream requires release notes to expose the underlying problem lifecycle so the metric cannot be gamed by silently deleting failed challenges.

## 7. Anti-gaming rules

- no retroactive removal of failed trials from the denominator merely to improve the release;
- no success claim based only on model accuracy/uptime/deployment count;
- no average-only reporting where groups experience materially different outcomes;
- no hiding STOP/retirement/incident records;
- no redefining a metric after observing results without a versioned rationale;
- no implying a repository merge, event display or capability registry entry equals government approval.

## 8. Historical durability

Every release becomes part of Landmark as Memory and the Retired Capability Archive. Twenty years later, reviewers should be able to reconstruct why a capability was introduced, what evidence justified it, what changed, what failed, why it ended and what replaced it—even if the original vendor, model or interface no longer exists.