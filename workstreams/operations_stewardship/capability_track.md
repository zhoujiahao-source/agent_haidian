# Capability Track｜社会能力提案入口

> Proposed mechanism for developer, enterprise, research, civic and community teams to propose a Capability. No real organization is claimed to participate.

## 1. Principle

Capability Track is not a shortcut around Problem Track. A team may arrive with a new capability first, but admission requires proof that it addresses a real public need and can be governed, maintained and retired.

**proposal → need evidence → public-value hypothesis → risk/data/IP/maintenance review → sandbox → bounded trial → evidence → STOP/MODIFY/CONTINUE/SCALE → registry / retirement.**

## 2. Minimum proposal record

Required:
- capability proposal / `capability_id` candidate
- problem/need evidence
- beneficiaries and groups that may be burdened
- why AI/technology is necessary or materially beneficial
- non-AI comparator
- public-value hypothesis and evaluation metric
- data requirements, provenance and minimization approach
- operational/rights/safety risk analysis
- interoperability interfaces and dependency inventory
- human override / manual service route where relevant
- maintainer and support model
- vendor lock-in / migration assessment
- sunset condition
- rollback and incident containment
- IP/open-source/license status
- expected public value and distributional effects
- proposed test scope, clearly labeled as Proposed until authorized

## 3. Admission gates

### C0 — need gate
A clever technology with no evidenced public need does not enter a public trial merely because it is novel. It may remain a research/demo artifact outside the public Capability lifecycle.

### C1 — necessity and proportionality gate
Compare the proposal with simpler technical and non-technical options. Higher complexity requires a stronger public-value case and a stronger maintenance/exit case.

### C2 — data and rights gate
Reject or redesign proposals that depend on non-public/uncleared data, unnecessary sensitive inference, excessive retention, hidden secondary uses, or rights-impacting automation without human responsibility and contestability.

### C3 — reversibility gate
A proposal must state how it can be paused, rolled back, replaced and cleaned up. A capability that cannot be safely exited requires substantially higher scrutiny and may be unsuitable for trial.

### C4 — maintainability and interoperability gate
Before public trial, identify the maintainer, dependencies, supported versions, interfaces and what happens if a vendor/model/API disappears. “We will maintain it later” is not an acceptable lifecycle plan.

### C5 — public-value test design
Define evidence before trial. Include common floors—safety, fairness, privacy, environment and cost—and scenario-specific outcomes. Include complaints, overrides and failures.

## 4. Sandbox stages

1. **Documentation sandbox** — architecture, model/system cards, data map, risk record, license/IP and dependency review.
2. **Synthetic/open-data sandbox** — test logic without production secrets or personal data where feasible.
3. **Controlled technical sandbox** — integration and failover tests; no implied authorization for public use.
4. **Bounded public trial** — only after risk authorization; clear site/time/population boundaries, notice, human fallback and stop conditions.
5. **Cross-area revalidation** — a capability proven in one Learning Unit is not presumed valid elsewhere; it must revalidate context, affected groups and operations before transfer through the Capability Backbone.

## 5. Trial decision rules

- **STOP:** need unsupported; public value absent; safeguards fail; maintenance/exit unacceptable; affected-group harm is unacceptable; data/legal authority absent; non-AI option is better.
- **MODIFY:** preserve need but change design, scope, model/vendor, interface, data, hours, safeguards or maintainer.
- **CONTINUE:** evidence promising but not sufficient to scale; keep bounded trial and publish Unknowns.
- **SCALE:** demonstrated public value, acceptable distributional result, durable accountable owner, maintenance funding path, interoperability/exit and appropriate human authorization.

## 6. Vendor lock-in test

Before SCALE, answer:
- Can the public owner export required configuration/data/records in a usable format where lawful?
- Are interfaces documented enough to substitute a component?
- Is the capability identifier independent of vendor branding?
- What happens if the model/API is withdrawn, price rises sharply or terms change?
- Is a degraded/manual mode possible?
- Are historical evidence and audit records still intelligible after component replacement?

A proprietary component is not automatically rejected; **unmanageable dependency without an exit plan is**.

## 7. Maintenance covenant — proposed

Every scaled capability should keep a machine/human-readable lifecycle record containing:
- accountable public owner;
- maintainer and support contact;
- current version and dependency versions;
- last review date;
- risk tier/status;
- known limitations;
- incident/complaint summary links;
- compatibility contract;
- deprecation notice rules;
- sunset condition and migration plan.

Exact contractual terms, response times and retention periods are Unknown until competent procurement/legal rules are identified.

## 8. Intellectual property and openness

Record license/IP status before admission. Open source can improve inspectability and portability but is not by itself proof of safety, public value or sustainable maintenance. Proprietary proposals must still provide sufficient operational transparency, auditability, exit support and public-interest safeguards. Contributions must preserve attribution and source provenance.

## 9. Capability Track is not a permanent deployment incentive

The program should not reward teams merely for getting into production. Recognition should include responsible withdrawals, successful handoffs, interoperable components, documented failures, accessibility improvements and low-cost non-AI substitutions. This prevents the ecosystem from becoming a deployment treadmill.