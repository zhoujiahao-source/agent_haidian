# Source & Uncertainty Gap Register

## Purpose

This register prevents the integration from converting missing organizer / public data into fictional planning certainty.

Every gap must be handled by one of four actions:

1. **Obtain / verify a formal-ready source**
2. **Use a clearly labeled reproducible proxy**
3. **Keep the value / geometry unknown**
4. **Limit the design claim to a conceptual / scenario range**

## High-priority known / likely organizer-data gaps

### 1. Exact official overall design boundary polygon

Risk: high.

Do not infer an official redline from a screenshot or approximate map.

Allowed interim response:

- use organizer-provided provisional geometry only with the exact role / precision metadata required by current schema;
- label maps as provisional / conceptual;
- do not use provisional geometry to claim statutory precision.

### 2. Exact official key-area polygons

Includes the three key areas where precise GIS may be incomplete or updated separately.

Risk: high.

Response:

- prefer trusted organizer geometry when available;
- otherwise retain provisional status and avoid parcel-level precision claims.

### 3. Survey / authoritative CRS / cadastral-grade base

Risk: medium-high.

Response:

- use repository-prescribed CRS / geometry workflow;
- do not present OSM / public basemap precision as survey-grade.

### 4. Statutory FAR controls

Risk: high.

Response:

- `Unknown` unless supported by a formal-ready source;
- schema sanity ranges are not approvals or statutory controls;
- design scenarios may use explicit assumptions only when rules permit.

### 5. Statutory height controls

Risk: high.

Same treatment as FAR.

### 6. Statutory building density / green ratio / setback controls

Risk: high.

Same treatment as FAR.

### 7. Exact road redlines / future road-control lines

Risk: high.

Response:

- distinguish existing road evidence from proposed connectivity design;
- no exact future redline claim without source.

### 8. Parcel ownership / land-right information

Risk: high.

Response:

- do not infer ownership from POIs, land use or imagery;
- do not make parcel-level demolition / acquisition / commitment claims.

### 9. Building height / floor count / use completeness

Risk: medium.

Potential response:

- cross-validate public sources;
- if derived from public imagery / geometry / other proxy, mark `Derived` / `Estimated` and document method;
- do not convert estimated height into regulatory fact.

### 10. Park implementation phases / confirmed projects

Risk: medium-high.

Response:

- distinguish existing condition, officially announced project, and proposal;
- never imply a conceptual phase is funded / confirmed.

### 11. Heritage GIS / exact protection-control polygons

Risk: high.

Response:

- use official textual / spatial material where available;
- if only heritage location / historical narrative is public, keep exact protection geometry unknown;
- do not invent control distances.

### 12. Traffic counts / pedestrian counts / temporal activity data

Risk: medium.

Response:

- use public authoritative data where available;
- otherwise use clearly labeled proxy / qualitative diagnosis;
- proposed AI scenarios must not claim current congestion improvement without a baseline.

### 13. Utility / safety / emergency infrastructure capacity

Risk: high for engineering claims.

Response:

- keep conceptual;
- do not claim engineering feasibility / capacity without formal data.

### 14. Public-facility demand / vulnerable-group service gaps

Risk: medium-high.

Response:

- use public statistics / facility inventories / accessibility evidence;
- treat unmet demand estimates as derived / assumed unless directly measured.

## New data needs created by the City OS concept

The integration introduces additional evidence needs. These are not permission to invent data.

### A. Problem-diagnosis baseline

For each proposed scenario, identify what baseline would be required to prove improvement, such as:

- temperature / thermal-comfort baseline
- accessibility barrier inventory
- travel-time reliability
- facility access / service response time
- public-space temporal use
- complaint / override / failure counts

If current data do not exist, mark the scenario metric as **proposed future monitoring**, not current evidence.

### B. Risk-tier evidence

Risk classification should be rule-based and scenario-specific. Avoid presenting a universal legal classification unless sourced. The proposal can define a **conceptual governance framework**.

### C. Urban Adaptation Rate baseline

An observed Urban Adaptation Rate cannot be computed for a future governance system unless historical experiment records exist in a compatible dataset.

Therefore the likely formal status is:

- metric definition = `Proposed / reproducible framework`
- current value = `Unknown` unless evidence exists
- future monitoring = required

### D. Capability-transfer evidence

Do not assume a solution validated in one learning unit transfers unchanged to another. Require revalidation rules and record context differences.

### E. Annual City Version Release evidence

This is a proposed operating institution. Do not present a v2027 release as already committed. Illustrative future version labels must be visibly conceptual.

## Priority basemap evidence inventory

The evidence pass should prioritize:

1. Building footprints
2. Existing roads / paths
3. Existing rail
4. Water
5. Green / public open space
6. Public facilities
7. POIs
8. Universities / research institutions
9. AI / innovation ecosystem actors
10. Metro / transit access
11. Important railway-history locations
12. Existing community / commercial patterns

## Evidence-classification contract

### Official

Direct organizer / government / formal source appropriate to the claim.

### Verified

Important claim supported by at least two independent credible public sources or a formal source plus an independent check.

### Derived

Reproducibly calculated or inferred from public evidence; method must be documented.

### Assumed

Explicit design / scenario assumption used for exploration; never presented as existing condition.

### Unknown

Insufficient evidence. Unknown is an acceptable professional result and must not be visually filled with false precision.

## Drawing-classification contract

### Known

Existing or formal evidence with adequate confidence for the represented scale.

### Estimated

Proxy / derived condition whose uncertainty is disclosed.

### Proposed

Design intervention / governance / future scenario.

### Unknown

Missing evidence / unresolved official status.

## Source conflict handling

If two credible sources disagree:

1. preserve both source records;
2. record geographic / temporal / methodological differences;
3. prefer the source appropriate to the exact claim rather than assigning blanket authority;
4. reduce confidence when conflict cannot be resolved;
5. do not silently overwrite the conflict in maps or metrics;
6. if the conflict affects formal scoring / statutory interpretation, keep the claim limited and consider opening / joining an upstream Issue according to the official participation workflow.

## Formal-language examples

### Acceptable

> The current diagram uses organizer-provided provisional geometry for conceptual coordination; it is not an official redline.

> Building heights shown as Estimated are derived from documented public sources and are not statutory height controls.

> Urban Adaptation Rate is proposed as a future monitoring metric; no current observed value is claimed.

### Not acceptable

> The approved boundary is …

> The statutory FAR is …

> The government will operate …

> This project will be implemented in 2027 …

unless a formal-ready source explicitly supports the exact statement.

## Exit criteria

Before finalization, every major spatial / metric / governance claim must have either:

- a valid evidence reference;
- a documented derived method;
- an explicit design assumption;
- or an explicit Unknown status.

No fifth category of “looks plausible” is allowed.
