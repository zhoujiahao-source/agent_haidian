# Personas｜人物与公共生活需求

Personas are evaluation lenses, not demographic predictions. They prevent the public-space/AI system from optimizing only for developers or smartphone-proficient users.

## P01 — Daily commuter / 通勤者
- **Moment:** early morning / evening transfer between rail, campus, office and neighborhood.
- **Needs:** direct route, reliable crossing, weather protection, disruption information, safe night return.
- **AI may help:** live route/service synthesis and disruption explanation.
- **Must not replace:** continuous walking/cycling route, lighting, crossings, static signs.
- **Consent trigger:** saving route/preferences or personalized alerts.
- **Failure test:** can the commuter finish the trip with no app and AI off?

## P02 — Older resident / 老年居民
- **Moment:** late morning community service, park walk, clinic/service navigation.
- **Needs:** seating intervals, legible type, clear language, human assistance, no forced QR/app.
- **AI may help:** optional voice/multilingual explanation and service routing.
- **Consent trigger:** storing personal service history or preferences.
- **Human override:** staff counter/phone/service volunteer.
- **Failure test:** ordinary service remains available without a smartphone.

## P03 — Child + caregiver / 儿童与照护者
- **Moment:** after school / weekend park use.
- **Needs:** safe edges/crossings, shade, toilets/rest, play and learning without surveillance pressure.
- **AI may help:** optional public cultural interpretation and environmental status.
- **Consent trigger:** any account, image/audio collection or personalized learning function; guardian/professional rules apply where relevant.
- **Hard boundary:** no passive child profiling as a public-space default.
- **Failure test:** play and movement remain fully usable when digital layers are off.

## P04 — Disabled user / 残障人士（含轮椅、低视力、听障等）
- **Moment:** full everyday journey, not a special event.
- **Needs:** continuous physical accessibility, tactile/audio/visual redundancy, reliable barrier information, assistance when needed.
- **AI may help:** opt-in accessible-route synthesis and barrier reporting.
- **Hard boundary:** disability is not inferred from passive behavior or appearance.
- **Human override:** mobility/service assistance.
- **Failure test:** the route is physically accessible before the routing model is considered.

## P05 — Visitor / cultural user / 游客与文化使用者
- **Moment:** weekend/daytime heritage walk, international visit.
- **Needs:** truthful history, orientation, multilingual access, places to pause without blocking daily users.
- **AI may help:** optional archive search, translation and accessible audio.
- **Must not replace:** physical historical interpretation and verified provenance.
- **Failure test:** uncertain historical claims are labeled or omitted, never presented as verified fact.

## P06 — Developer / researcher / 开发者与研究者
- **Moment:** workshop, trial, field validation, cross-zone collaboration.
- **Needs:** clear test rules, approved interfaces/data, reproducible evidence, rapid stop/modify feedback.
- **AI may help:** capability discovery, simulation, experiment support and evidence processing.
- **Authorization:** test permission follows risk/professional/public authorization, not technical capability alone.
- **Failure test:** the experiment can be stopped without disrupting baseline public-space functions.

## P07 — Frontline operator / 一线运营者（保洁、安保、园林、维修、配送等）
- **Moment:** throughout day/night, including degraded and emergency modes.
- **Needs:** workable maintenance access, clear responsibilities, tools that do not invisibly shift risk/workload to staff.
- **AI may help:** maintenance prioritization, equipment status and incident triage.
- **Hard boundary:** no opaque worker scoring/surveillance as part of public-space operation.
- **Human override:** operational supervisor and established safety procedure.
- **Failure test:** manual operation is documented and realistically staffable.

## P08 — Local merchant / service operator / 商户与服务运营者
- **Moment:** Dazhongsi service/business testing, evening economy, customer support.
- **Needs:** clear trial terms, predictable public-space interface, consumer transparency, human dispute resolution.
- **AI may help:** opt-in service assistant, translation, aggregated queue/demand coordination.
- **Consent trigger:** individualized recommendation, loyalty/account linkage, personal profile.
- **Hard boundary:** a pilot must not masquerade as an approved permanent business model.
- **Failure test:** consumers can access terms, human support and exit/dispute channels without AI mediation.

## Coverage rule

Every scenario card names at least one primary persona and one potentially affected non-primary group. Integration should test subgroup outcomes, complaints, manual takeover, safety incidents and unequal impacts — not only average satisfaction.