# Sources & Evidence Register — AI Governance & Metrics

This register distinguishes **competition/repository authority** from **external governance references**. External AI-governance materials are comparative/design references; they do not create planning approval, statutory geometry or project-specific legal authority.

## A. Project / repository sources

### GOV-REPO-SKILL
- Publisher: open-city-ai / haidian repository
- Source: `skills/urban-design-ai-submission/SKILL.md`
- Upstream ref reviewed: `b3d6fdaa2331fdc60a3e618019fd8e6596532fff`
- Use: current submission rules, geometry-gap handling, review workflow, evidence expectations
- Confidence: high for repository state at the reviewed commit
- Limitation: living repository; must be re-read before final integration

### GOV-REPO-BRIEF
- Publisher: open-city-ai / haidian repository
- Sources: `brief/site-package/design_brief.json`, `agent_taskbook.json`, `allowed_design_space.json`, `sources.json`, `ranges/planning_limits.json`, `standards/standards.json`, `standards/references/index.json`, `visual_style_recommendations.json`
- Use: three positioning statements, five functions, agent task boundaries, editable/locked space, source rules, planning-data gaps
- Confidence: high for repository state at reviewed commit
- Limitation: some text still conflicts with the latest SKILL/review-rubric wording on whether organizer-missing official geometry blocks professional scoring; conflict is preserved rather than silently resolved

### GOV-REPO-METRICS-SCHEMA
- Publisher: open-city-ai / haidian repository
- Source: `brief/site-package/schemas/metrics.schema.json`
- Use: machine-ready metric field design
- Confidence: high for reviewed commit
- Key constraint used: custom metric entries still require `status`, `value`, `unit`, `source_files`, `formula`, `confidence`, and `assumptions`; `unknown` metrics use `value: null` and a reason

### GOV-REPO-DATA-WORKFLOW
- Publisher: open-city-ai / haidian repository
- Sources: `data/source_registry.json`, `docs/data-workflow.md`, `docs/review-rubric.md`, `brief/site-package/geometry/`
- Use: Official/Verified/Derived/Assumed/Unknown discipline; missing-data handling; provisional geometry status
- Confidence: high for reviewed commit
- Limitation: exact organizer-issued `SITE_BOUNDARY` / `KEY_AREA` polygon was not present at audit time

### GOV-USER-LEGIBLE-BELT
- Publisher: user's fork
- Source branch: `submission/zhoujiahao-source/jingzhang-legible-ai-belt`
- Files sampled: `proposal.md`, `metrics.json`
- Use: reusable legibility/disclosure/evidence-chain assets
- Confidence: high as existing user-work evidence
- Limitation: historical submission asset, not the new design constitution and not automatically current

## B. External governance references

### GOV-NIST-AIRMF
- Publisher: U.S. National Institute of Standards and Technology (NIST)
- URL: https://www.nist.gov/itl/ai-risk-management-framework
- Use: voluntary lifecycle-oriented AI risk-management reference; supports explicit risk governance, monitoring and accountability concepts
- License/authority: public authoritative guidance; not a Beijing planning regulation
- Confidence: high for existence/source authority

### GOV-OECD-AI-PRINCIPLES
- Publisher: OECD
- URL: https://www.oecd.org/en/topics/ai-principles.html
- Use: human rights/fairness/privacy, transparency, robustness/safety and accountability cross-check
- Authority: intergovernmental principles; not project-specific statutory control
- Confidence: high

### GOV-EU-AI-ACT
- Publisher: European Union / EUR-Lex
- URL: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- Use: comparative reference for lifecycle risk management and meaningful human oversight of high-risk AI
- Authority: EU law where applicable; **not assumed applicable to this Beijing urban-design proposal**
- Confidence: high for the cited regulation; applicability requires separate legal review

### GOV-CN-PIPL
- Publisher: PRC official legal publication
- URL: https://www.gov.cn/xinwen/2021-08/20/content_5632486.htm
- Use: personal-information minimisation/necessity, automated-decision transparency/fairness and rights, impact-assessment and public-place identification considerations
- Authority: national law; concrete obligations depend on the actual deployment/data-processing facts
- Confidence: high for source authority; legal interpretation/application not performed by this workstream

### GOV-CN-GBT45392
- Publisher: State Administration for Market Regulation / national standards system
- URL: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=AAF1CD9403AC05FC861DFE522A9D5C7C
- Standard: GB/T 45392-2025, security requirements for automated decision making based on personal information
- Use: current Chinese automated-decision security benchmark for future implementation cross-check
- Authority: national recommended standard; not a planning-control value
- Confidence: high for publication/status; implementation applicability should be verified by the responsible compliance owner

## C. No imported operational dataset

This governance workstream does **not** import a live city-operating dataset and therefore does not publish measured values for UAR or the other AI-city metrics. Formula readiness is intentionally separated from measurement readiness.
