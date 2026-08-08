# Public-Space Component Library｜公共空间组件库

This library is a **design kit**, not a procurement list. Exact product, material, dimension and engineering specifications remain for later verified professional design. Components may be combined differently by node type; repetition of the same “smart object” is explicitly avoided.

## C01 — Open Node Marker / 开放节点标
- **Job:** identifies a callable civic capability and its status.
- **Physical-first:** durable title, capability icon/text, operator/steward, analog fallback.
- **Optional digital:** current service/trial status.
- **Must show:** `concept / trial / service / degraded / retired` when applicable.
- **Accessibility:** high contrast; text + symbol; tactile/large-print layer where appropriate.

## C02 — Capability Status Strip / 能力状态条
- **Job:** compact disclosure of `ON / DEGRADED / OFF / MANUAL`.
- **Use:** service ports, climate nodes, test yards, archive displays.
- **Rule:** never use green/red alone; pair color with word/symbol/shape.

## C03 — Rail-Pair Wayfinding Line / 双轨导向线
- **Job:** carries the railway DNA into modern routing/capability exchange.
- **Meaning:** one line = ordinary civic route; paired line = optional capability/service layer.
- **Rule:** not a fake historic track; detailed design must avoid trip/visual-accessibility hazards.

## C04 — Switch Choice Plate / 道岔选择牌
- **Job:** makes a real choice visible: manual/AI, direct/deeper interpretation, participate/bypass.
- **Rule:** choices must be materially equivalent enough that opting out does not punish the user.

## C05 — Static + Tactile Map Board / 静态触觉地图板
- **Job:** guaranteed no-power orientation.
- **Content:** north/route/service/help, verified temporary closures, accessible information as professionally designed.
- **Rule:** dynamic services may add layers but never remove the static map requirement at critical nodes.

## C06 — Rest + Lean + Wheelchair Companion Module / 复合休息模块
- **Job:** supports older users, caregivers, disabled users and short commuter stops.
- **Options:** seat with back/arm, perch/lean, adjacent wheelchair/companion space.
- **Rule:** placement comes from actual rest demand and circulation clearance, not a decorative grid.

## C07 — Shade / Climate Canopy Kit / 遮阴气候构件
- **Job:** passive thermal protection first.
- **Elements:** tree canopy, architectural shade where appropriate, seating integration, rainfall/drainage interface.
- **Optional AI:** scheduling/maintenance of approved active systems.
- **Rule:** no “smart cooling” substitutes for basic shade design.

## C08 — Water / Refill Interface / 饮水补给接口
- **Job:** supports heat resilience where utilities/hygiene/maintenance make it feasible.
- **Rule:** exact location/specification requires utility, public-health and maintenance review.

## C09 — Human Help Beacon / 人工帮助点
- **Job:** visible escalation path.
- **Forms:** staffed counter, intercom/phone, service-hour/contact panel.
- **Rule:** the responsible human/organization role is legible; it is not only a chatbot icon.

## C10 — Consent Threshold / 同意阈值界面
- **Job:** marks the transition from ambient/non-personal public service to individualized function.
- **Must state:** purpose, data class, retention summary, operator, exit, human escalation.
- **Rule:** crossing ordinary public space is never treated as consent.

## C11 — Trial Card / 实验卡
- **Job:** makes a reversible experiment publicly understandable.
- **Fields:** problem; version; test window; status; risk; steward; data; participant rule; bypass; human stop; success/STOP criteria.
- **Rule:** concept/test/approved service states must not be visually conflated.

## C12 — Bypass Marker / 非参与绕行标
- **Job:** keeps ordinary users outside controlled tests without confusion.
- **Rule:** bypass is physically continuous and not stigmatized or materially inferior.

## C13 — Manual Stop / Operator Point / 人工停机与操作点
- **Job:** provides real operational override appropriate to the trial/equipment.
- **Rule:** exact safety architecture is professional/engineering work; this component is a requirement, not a claimed design solution.

## C14 — Evidence Card / 证据卡
- **Job:** standard comparison unit in City Learning Archive.
- **Fields:** problem, intervention, evidence, subgroup effects, incidents/limitations, decision, source/confidence.
- **Rule:** include STOP/MODIFY cases; no single success leaderboard.

## C15 — Version / Mileage Marker / 版本里程标
- **Job:** connects 1909, 2026 and future city versions through a restrained physical motif.
- **Rule:** time/version information must remain readable in black-and-white and without animation.

## C16 — Retirement Tag / 退役标签
- **Job:** explains why a capability left service and what replaced it.
- **Fields:** capability/version, active period, value, limitations, retirement reason, replacement, data deletion/retention, artifact status, lesson.

## C17 — Community Review Table / 公共评议桌
- **Job:** physical setting for co-creation, explanation, appeal and version review.
- **Fallback:** paper input and face-to-face facilitation.
- **Rule:** AI summaries do not replace original authorized input or human deliberation.

## C18 — Continuity Cabinet / 应急连续柜
- **Job:** stores/manualizes critical offline information/equipment appropriate to the site.
- **Possible contents:** printed emergency map/contact, temporary signage, approved backup communication equipment.
- **Rule:** contents depend on formal operations/emergency planning; no unverified resilience claim.

## C19 — Archive Shelf / 档案陈列架
- **Job:** holds a small number of safely deactivated, rights-cleared, genuinely instructive retired artifacts.
- **Rule:** artifact-light; no warehouse accumulation; storage media/credentials removed; provenance/status explicit.

## C20 — Reset / Reuse Bench / 重置再用工作台
- **Job:** makes removal, reconfiguration and reuse visible at Future Test Station / Retired Archive interfaces.
- **Rule:** public display only for safe activities; hazardous handling remains backstage under professional procedure.

## Component-to-node mapping

| Component | N1 Service | N2 Climate | N3 Care | N4 Memory | N5 Test | N6 Community | N7 Continuity | N8 Interchange |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C01 Open Node | ● | ● | ● | ● | ● | ● | ● | ● |
| C05 Static/tactile map | ● | ○ | ● | ○ | ○ | ○ | ● | ● |
| C06 Rest module | ● | ● | ● | ● | ○ | ● | ○ | ● |
| C09 Human help | ● | ○ | ● | ○ | ● | ● | ● | ● |
| C10 Consent threshold | ● | ○ | ● | ○ | ● | ● | ○ | ○ |
| C11 Trial card |  |  |  |  | ● | ○ |  | ○ |
| C14 Evidence card | ○ | ○ | ○ | ● | ● | ● | ○ | ● |
| C16 Retirement tag |  |  |  | ● | ○ | ○ |  | ● |
| C17 Review table |  |  |  | ○ | ○ | ● |  | ● |
| C18 Continuity cabinet | ○ | ○ | ○ |  | ● | ○ | ● | ○ |

Legend: ● primary / ○ optional by verified need.

## Procurement / implementation boundary

Nothing in this library names a supplier, product, precise dimension, sensor model or construction specification. Integration must convert it into a professional component schedule only after site, accessibility, heritage, fire, municipal, maintenance and procurement constraints are known.