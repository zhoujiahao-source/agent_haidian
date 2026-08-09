# Retired Capability Governance｜城市能力退役治理

## 1. Sunset by design

Retirement begins at admission, not when a system is already abandoned. Every capability proposal should state a sunset condition, rollback path, maintenance owner and exit/dependency assumptions before public trial.

The Retired Capability Archive is a governance memory interface; it is not a dumping ground for obsolete hardware or a museum that keeps risky services operational for nostalgia.

## 2. Retirement triggers — proposed

A capability should enter retirement review when one or more apply:
- public-value objective is no longer met or need has disappeared;
- unacceptable safety, rights, privacy, accessibility, environmental or distributional effect;
- a simpler/non-AI alternative provides better public value;
- vendor/model/API end-of-support or unacceptable dependency change;
- maintainer/incident-response owner is no longer viable;
- interoperability/migration obligations cannot be met;
- security/technical architecture can no longer be maintained responsibly;
- capability duplicates a better successor;
- operating cost/energy/resource burden becomes unjustified;
- legal/authorization basis changes or is absent;
- community/operational evidence demonstrates persistent failure that modification cannot reasonably cure.

These are governance triggers, not automatic legal determinations.

## 3. Retirement sequence

### R0 — open retirement review
Record trigger, evidence, affected groups, service dependency and accountable owner.

### R1 — continuity plan
Identify what public function still needs to exist: successor capability, manual/non-AI service, temporary degraded mode, or no replacement if the need has ended.

### R2 — authorization and notice
Competent public authority decides retirement/suspension and communicates timing/impact in accessible form appropriate to the capability.

### R3 — stop operation safely
Disable service/model/automation within the authorized plan; prevent silent continued operation by abandoned components.

### R4 — revoke credentials and integrations
Remove API keys, service accounts, machine identities, scheduled jobs, data feeds and other operational access according to applicable security/data rules.

### R5 — data disposition
Classify records into required operational/legal retention, public learning archive, research record if separately authorized, and deletion. Do not archive unnecessary personal data merely for historical interest. Exact retention periods remain Unknown until applicable rules are mapped.

### R6 — physical asset disposition
Remove, repurpose or safely isolate sensors, robots, kiosks, signs, edge devices, barriers or other physical components. Consider accessibility, e-waste/resource reuse, heritage/public-space impacts and residual network access.

### R7 — registry tombstone
Keep a stable `capability_id` and public retirement record so historical links do not disappear. Mark operation status as retired and link successor if any.

### R8 — archive learning
Preserve why it existed, public value created/not created, incidents/limitations, why it retired, what replaced it and what future teams should not repeat.

### R9 — post-retirement verification
Verify credentials/data feeds/devices are actually inactive, continuity works, and public-facing interfaces no longer imply the capability is active.

## 4. Archive record

Recommended public-safe fields:
- capability ID/name at retirement;
- purpose and problem addressed;
- lifecycle dates/status history;
- accountable owner / maintainer status at retirement;
- main public-value evidence and limitations;
- major modifications / responsible STOPs;
- public-safe incident/complaint lessons;
- retirement trigger and decision rationale;
- data/credential/device cleanup status categories;
- successor/replacement or explicit no-replacement rationale;
- source/audit/version-release links;
- what cannot be disclosed and why, without exposing protected information.

## 5. Physical Retired Capability Archive / “capability graveyard”

A physical-first learning space may preserve selected non-sensitive artifacts, replicas, interface fragments or explanatory exhibits. Selection should prioritize public learning and historical significance, not novelty. Operational credentials, personal data, unsafe active systems and restricted technical details are excluded.

The archive should include successful retirements as well as failures: responsible cities replace even once-useful systems when conditions change.

## 6. Emergency retirement vs planned sunset

Emergency STOP may precede full retirement when immediate safety/rights/service risks require it. After containment, the same cleanup, continuity and archive duties still apply. Planned sunset follows a published migration/deprecation sequence where feasible.

## 7. Anti-abandonment rule

A capability is not “retired” merely because a project team stops talking about it. Retirement is complete only when operational authority/access/data/physical dependencies are dealt with, service continuity is resolved, registry status is updated and learning is preserved.