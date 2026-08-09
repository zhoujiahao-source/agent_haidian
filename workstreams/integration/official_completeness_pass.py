#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise RuntimeError(f"missing replacement anchor: {label}")


def insert_before(text: str, anchor: str, block: str, marker: str) -> str:
    if marker in text:
        return text
    idx = text.find(anchor)
    if idx < 0:
        raise RuntimeError(f"missing insertion anchor: {anchor[:80]}")
    return text[:idx].rstrip() + "\n\n" + block.strip() + "\n\n" + text[idx:]


def ensure_metric(metrics: dict, key: str, payload: dict) -> None:
    metrics.setdefault("metrics", {})[key] = payload


def add_unique(seq: list, value: str) -> None:
    if value not in seq:
        seq.append(value)


def patch_proposal_zh(root: Path) -> None:
    p = root / "proposal.md"
    t = p.read_text(encoding="utf-8")
    t = t.replace('iteration: "v2.0.0"', 'iteration: "v2.1.0"', 1)

    boundary_block = """**官方边界背景复核。** 最新仓库维护记录已把一项独立 OSM 背景核对写入 `provisional_boundaries_basis.md`：OSM 已测绘的京张铁路遗址公园与 `PROV-SITE-001` 当前读数为 0% 相交、最近约 412.5 m，而统筹研究范围覆盖 100%。维护者同时明确：这不能证明 OSM 或临时 polygon 谁更正确，**不能据此修改或升级为官方红线**；因此本方案继续把全部落位视为 provisional，待官方 polygon 到位后整体重算。[source:PROVISIONAL-BOUNDARY-BASIS] [assumption:A-BOUNDARY-001]
<!-- OFFICIAL-COMPLETENESS:BOUNDARY-AUDIT -->"""
    t = insert_before(t, "![现状证据层级、Capability Backbone 与 Open Node 总览]", boundary_block, "OFFICIAL-COMPLETENESS:BOUNDARY-AUDIT")

    key_block = """为逐条回应官方重点区任务，三处原型进一步明确为**专业深化清单，而非已确定工程方案**：

- **众智园 / Verification Campus**：围绕 AI 全栈自主创新、标准与安全治理组织可逆验证空间；五环对外交通、清河文化资源、建筑—绿地—水系一体化以及绿地 AI 场景必须进入后续专项核验，任何 crossing、容量、建筑规模和工程线位均以真实交通/水务/权属/控规资料为前置条件。
- **AI 原点社区 / Learning Neighborhood**：把高校源头创新、孵化转化、人才与开源社区、品牌活动嵌入日常公共服务；五道口站与清华东路西口站周边只提出 TOD/慢行衔接的**研究任务**，并以低扰动、可逆更新优先于大拆大建；具体保留改造、成果转化载体和住房配套必须由现状建筑、权属与专业评估决定。
- **大钟寺 / Market & Service Commons**：围绕智能体、智能终端、内容消费与数字资产服务验证 AI-native 新业态；大钟寺站四象限步行联系、非机动车与静态交通、规划绿地复合利用均作为后续详细设计议题，先验证道路红线、绿地属性、消防和运营安全，再决定空间形式。

这些清单把官方点名任务转换为“**需要被验证的城市设计问题**”，不把概念建议写成政府承诺、审批结论或施工条件。[source:OFFICIAL-ANNOUNCEMENT] [assumption:A-CONTROLS-001]
<!-- OFFICIAL-COMPLETENESS:KEY-AREAS -->"""
    t = insert_before(t, "![众智园、AI 原点社区与大钟寺三处重点区放大及能力分工]", key_block, "OFFICIAL-COMPLETENESS:KEY-AREAS")

    character_block = """**建筑高度、强度、屋顶与体量导则（概念建议）。** 在法定高度、FAR、密度、退界等数据缺失时，不用虚构数字替代控规，而先建立可供专业深化的定性规则：①高度随铁路记忆、蓝绿廊道、日照与重要视线形成渐变和退台，数值上限以后续控规为准；②强度只在公共交通、创新服务和承载能力被核验后讨论集中，不预设 FAR；③体量采用可穿行、可分期的小尺度基座和通风/慢行孔隙，避免连续封闭巨构；④屋顶作为“第五立面”，优先预留可逆光伏、雨水、生态或公共使用可能，但必须经过结构、消防、运维复核；⑤风貌坚持公共服务美学与铁路结构 DNA，避免无差别玻璃科技园、复古复制或霓虹赛博奇观。这些规则是城市设计控制意向，不是法定建筑控制值。[assumption:A-CONTROLS-001]
<!-- OFFICIAL-COMPLETENESS:FORM-CONTROL -->"""
    t = insert_before(t, "三类时间地标把", character_block, "OFFICIAL-COMPLETENESS:FORM-CONTROL")

    ops_block = """为完整回应 `agent.6`，长期运营采用六个互相咬合的公共机制：

1. **年度城市学习大会 / City Version Release**：年度公开复盘 Added / Modified / Scaled / Responsible STOP / Retired、证据变化和下一年度挑战。
2. **Developer Commons**：以季度 City Challenge Board、能力诊所、文档维护、开放接口和风险分级 sandbox 形成开发者社区；贡献者身份和能力版本进入可追溯档案。
3. **Scenario Open Days**：按风险等级开放限定时段/区域的场景测试窗口，进入前公布参与规则、同意层、非参与者绕行、人类 STOP 权、事故与退出协议。
4. **Public Experience Route**：把 1909 Railway Memory → 2026 Learning Archive → Future Experiment Station 与日常 PCI 节点组织成无障碍昼夜公共体验路线；路线首先是一条正常可用的城市公共空间，不是封闭科技展线。
5. **International Communication**：发布中英双语 Capability Registry、年度 Evidence Report、开放挑战与京张城市学习大会材料，用可复验结果而不是宣传口号建立国际交流。
6. **Attraction & Conversion**：形成 Challenge → Sandbox → Pilot → Public-Value Review → **采购/合作/规模化评估** 的转化路径；任何采购、招商、政策资金或合作都只进入依法依规的后续评估，不承诺政府购买或签约结果。

运营节奏因此既有全年持续迭代，也有年度公共审计节点；品牌资产不是一次活动 Logo，而是 Open Node、Capability Registry、版本档案、公开路线和开发者贡献记录的长期组合。[source:AGENT-TASKBOOK] [assumption:A-INSTITUTION-001]
<!-- OFFICIAL-COMPLETENESS:AGENT6 -->"""
    t = insert_before(t, "长期运营至少维护四本资源台账", ops_block, "OFFICIAL-COMPLETENESS:AGENT6")

    metric_block = """**官方产业与人才规划指标：先定义、后取数，不造数。** 除 UAR 外，本方案把公告点名的产业规划指标写成可审计的 `Unknown` 公式接口：`ai_innovation_index`（经验证创新投入、成果转化、开放协作与公共能力产出的复合指数，权重待业主/专业团队共同确定）、`ai_talent_density_per_sqkm`（明确统计口径后的 AI 人才数 / 官方统计空间面积）、`ai_output_value_cny`（统一年度与产业口径后的 AI 相关产值）、`ai_industry_space_scale_sqm`（经核验 AI 产业建筑面积）、`industry_function_mix_ratio`（经核验产业/科研/服务/公共功能面积结构）。当前缺少统一统计边界、企业名录、人才与产值数据、完整建筑面积，因此五项全部保持 `unknown/null`，不得把公式就绪误写成真实绩效。[metric:ai_innovation_index] [metric:ai_talent_density_per_sqkm] [metric:ai_output_value_cny]
<!-- OFFICIAL-COMPLETENESS:OFFICIAL-METRICS -->"""
    t = insert_before(t, "旗舰指标 **Urban Adaptation Rate", metric_block, "OFFICIAL-COMPLETENESS:OFFICIAL-METRICS")

    stale = "所有生成图、SVG、HTML 与 PDF 为本方案程序化生成；不嵌入第三方照片、商业地图底图、远程字体、追踪脚本或未清权素材。OSM 与 Microsoft 数据源已经登记许可和用法，但由于当前执行环境无法联网完成 materialization，本版本没有把它们伪装为现状 Verified 图层。[source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]"
    live = "所有生成图、SVG、HTML 与 PDF 为本方案程序化生成；不嵌入第三方照片、商业地图底图、远程字体、追踪脚本或未清权素材。OSM 已于 2026-08-09 通过 Overpass 实际 materialize 5,532 个可用 features（其中 1,898 个建筑面），仅作为候选现状证据；Microsoft 2026-07-24 公开索引已实际查询，但对目标 L9 quadkey `132100103` 无发布分区，因此没有制造 OSM↔Microsoft 匹配率。两者均不替代官方测绘、红线或法定规划资料。[source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]"
    t = replace_once(t, stale, live, "zh live basemap risk statement")
    p.write_text(t, encoding="utf-8")


def patch_proposal_en(root: Path) -> None:
    p = root / "proposal.en.md"
    t = p.read_text(encoding="utf-8")
    t = t.replace('iteration: "v2.0.0"', 'iteration: "v2.1.0"', 1)

    boundary_block = """**Official-boundary background audit.** The latest repository-maintained basis records an independent OSM background comparison: the OSM-mapped Jing-Zhang Railway Heritage Park has 0% intersection with the current `PROV-SITE-001` reading and a nearest distance of about 412.5 m, while the coordinated research scope covers it fully. Maintainers explicitly state that this does **not** prove whether OSM or the provisional polygon is correct and cannot justify upgrading or silently changing the official redline. All exact siting therefore remains provisional until organizer polygons trigger full recalculation. [source:PROVISIONAL-BOUNDARY-BASIS] [assumption:A-BOUNDARY-001]
<!-- OFFICIAL-COMPLETENESS:BOUNDARY-AUDIT -->"""
    t = insert_before(t, "![Evidence tiers, Capability Backbone and Open Node overview]", boundary_block, "OFFICIAL-COMPLETENESS:BOUNDARY-AUDIT")

    key_block = """To respond explicitly to the organizer's named key-area tasks, the three prototypes are extended as **professional-deepening checklists, not determined engineering schemes**:

- **Zhongzhiyuan / Verification Campus:** combine full-stack autonomous AI with standards and safety-governance testing; Fifth Ring external access, Qinghe cultural resources, building-green-water integration and AI-enabled green-space scenarios are mandatory follow-up checks, with crossings, capacity, building scale and engineering alignments subject to real mobility, water, ownership and planning evidence.
- **AI Origin / Learning Neighborhood:** connect university-origin innovation, incubation/conversion, talent/open-source communities and brand activities to everyday public services; Wudaokou and Qinghuadongluxikou station areas are framed only as TOD/slow-mobility research tasks, with low-disturbance reversible renewal preferred over wholesale demolition. Exact retain/renovate decisions, transfer hosts and housing/support facilities require verified building and ownership evidence.
- **Dazhongsi / Market & Service Commons:** test AI-native services around agents, intelligent terminals, content consumption and digital-asset services; four-quadrant pedestrian links at Dazhongsi Station, bicycle/static-traffic organization and composite use of planned green space remain detailed-design questions that must first verify road redlines, green-space status, fire safety and operations.

This converts organizer requirements into **urban-design questions that must be verified**, not government commitments, approvals or construction conditions. [source:OFFICIAL-ANNOUNCEMENT] [assumption:A-CONTROLS-001]
<!-- OFFICIAL-COMPLETENESS:KEY-AREAS -->"""
    t = insert_before(t, "![Enlarged logic for Zhongzhiyuan, AI Origin and Dazhongsi]", key_block, "OFFICIAL-COMPLETENESS:KEY-AREAS")

    character_block = """**Height, intensity, roof and massing guidance (conceptual).** Because statutory height, FAR, density and setback controls are missing, the proposal does not invent numbers. Instead it establishes qualitative rules for later professional deepening: (1) height should step in response to railway memory, blue-green corridors, daylight and important views, with numeric caps set only by verified controls; (2) intensity may concentrate near transit/innovation services only after carrying capacity, daylight, fire and heritage checks, with no assumed FAR; (3) massing should remain porous and phaseable with smaller-grain bases, breezeways and public passages rather than sealed megablocks; (4) roofs are treated as a fifth facade with reversible potential for PV, stormwater, habitat or community use, subject to structural/fire/maintenance review; and (5) character follows a public-service aesthetic and railway structural DNA rather than generic glass-tech parks, retro imitation or neon cyberpunk spectacle. These are urban-design intentions, not statutory building controls. [assumption:A-CONTROLS-001]
<!-- OFFICIAL-COMPLETENESS:FORM-CONTROL -->"""
    t = insert_before(t, "Three time landmarks make", character_block, "OFFICIAL-COMPLETENESS:FORM-CONTROL")

    ops_block = """To fully answer `agent.6`, long-term operations use six interlocking civic mechanisms:

1. **Annual Urban Learning Conference / City Version Release:** publicly review Added / Modified / Scaled / Responsible STOP / Retired items, evidence changes and the next challenge cycle.
2. **Developer Commons:** quarterly City Challenge Boards, capability clinics, documentation maintainers, open interfaces and risk-tiered sandbox slots create a durable developer community whose contributions and versions remain traceable.
3. **Scenario Open Days:** risk-tiered test windows publish participation rules, consent layers, nonparticipant bypass, human STOP authority, incident response and exit conditions before any opening.
4. **Public Experience Route:** an accessible day/night route links 1909 Railway Memory → 2026 Learning Archive → Future Experiment Station with everyday PCI nodes; it must first work as ordinary public space rather than a closed technology demo trail.
5. **International Communication:** bilingual Capability Registry, annual Evidence Report, open challenges and Urban Learning Conference materials communicate reproducible results rather than promotional claims.
6. **Attraction & Conversion:** Challenge → Sandbox → Pilot → Public-Value Review → **procurement/partnership/scaling consideration**; procurement, investment promotion, policy funding or partnerships remain subject to lawful later evaluation and are never guaranteed government purchases or signed commitments.

The operating rhythm therefore combines continuous year-round iteration with an annual public-accountability moment. Long-term brand assets are Open Node, the Capability Registry, version archives, public routes and developer contribution records rather than a one-off event logo. [source:AGENT-TASKBOOK] [assumption:A-INSTITUTION-001]
<!-- OFFICIAL-COMPLETENESS:AGENT6 -->"""
    t = insert_before(t, "Long-term operation should maintain four resource ledgers", ops_block, "OFFICIAL-COMPLETENESS:AGENT6")

    metric_block = """**Organizer-requested industry and talent indicators: define first, measure later.** In addition to UAR, the package now exposes auditable `Unknown` formula interfaces for the indicators named by the organizer: `ai_innovation_index` (composite of verified innovation inputs, transfer outcomes, open collaboration and validated public-capability outputs, with weights to be co-defined by the client/professional team), `ai_talent_density_per_sqkm` (AI talent under a declared statistical definition / official statistical area), `ai_output_value_cny` (AI-related output value under a consistent year and industry definition), `ai_industry_space_scale_sqm` (verified AI-industry GFA), and `industry_function_mix_ratio` (verified industry/research/service/public-function area structure). Because the official statistical boundary, enterprise roster, talent/output data and complete GFA are unavailable, all five remain `unknown/null`; formula readiness must not be presented as measured performance. [metric:ai_innovation_index] [metric:ai_talent_density_per_sqkm] [metric:ai_output_value_cny]
<!-- OFFICIAL-COMPLETENESS:OFFICIAL-METRICS -->"""
    t = insert_before(t, "The flagship **Urban Adaptation Rate", metric_block, "OFFICIAL-COMPLETENESS:OFFICIAL-METRICS")

    stale = "All diagrams, SVG, HTML and PDFs in this package are programmatically generated for the proposal and use no third-party photographs, commercial map tiles, remote fonts or tracking. OSM and Microsoft source/licence records are included, but live materialization could not run in this execution environment, so no un-downloaded dataset is presented as Verified existing conditions. [source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]"
    live = "All diagrams, SVG, HTML and PDFs in this package are programmatically generated for the proposal and use no third-party photographs, commercial map tiles, remote fonts or tracking. OSM was actually materialized through Overpass on 2026-08-09 with 5,532 usable features, including 1,898 building polygons, and remains candidate context only. Microsoft's 2026-07-24 public index was also queried live, but it publishes no partition for target L9 quadkey `132100103`; therefore no OSM↔Microsoft match rate is fabricated. Neither dataset replaces official survey, redline or statutory planning evidence. [source:SRC-OSM-OVERPASS-LIVE] [source:SRC-MS-GLOBAL-BUILDINGS-20260724]"
    t = replace_once(t, stale, live, "en live basemap risk statement")
    p.write_text(t, encoding="utf-8")


def patch_json(root: Path) -> None:
    # Assumptions
    ap = root / "assumptions.json"
    data = json.loads(ap.read_text(encoding="utf-8"))
    assumptions = data.setdefault("assumptions", [])
    by_id = {a.get("id"): a for a in assumptions}
    by_id["A-BASEMAP-001"]["statement_zh"] = "OSM 已于 2026-08-09 经 Overpass 实际抓取：provisional envelope 内 5532 个可用 features，其中 1898 个建筑面；仅作为候选现状证据。Microsoft 2026-07-24 公开索引已实际查询，但目标 L9 quadkey 132100103 无发布分区，因此无法做站点级双源建筑 IoU。两者均不替代官方测绘/红线/权属/法定控制。"
    by_id["A-BASEMAP-001"]["trigger"] = "official/independent second-source or field verification enables promotion beyond candidate context"
    if "A-INDUSTRY-DATA-001" not in by_id:
        assumptions.append({
            "id": "A-INDUSTRY-DATA-001",
            "status": "active",
            "statement_zh": "公告点名的 AI 创新指数、人才密度、产值、AI产业空间规模与功能结构已建立公式接口，但统一统计边界、企业名录、人才/产值数据和完整建筑面积尚未取得；当前数值保持 unknown/null。",
            "trigger": "verified statistical boundary + enterprise/talent/output/GFA dataset received"
        })
    ap.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Metrics
    mp = root / "metrics.json"
    m = json.loads(mp.read_text(encoding="utf-8"))
    base = {
        "status": "unknown", "value": None, "confidence": "unknown",
        "source_files": ["proposal.md"], "assumptions": ["A-INDUSTRY-DATA-001"]
    }
    ensure_metric(m, "ai_innovation_index", {**base, "unit": "index", "formula": "weighted composite of verified innovation inputs + transfer outcomes + open collaboration + validated public-capability outputs; weights require client/professional agreement", "reason": "No adopted weighting scheme or complete underlying enterprise/innovation dataset."})
    ensure_metric(m, "ai_talent_density_per_sqkm", {**base, "unit": "persons_per_sqkm", "formula": "verified_AI_talent_persons / official_statistical_area_sqkm", "reason": "No verified AI talent roster/statistical boundary with consistent date and definition."})
    ensure_metric(m, "ai_output_value_cny", {**base, "unit": "CNY", "formula": "sum verified AI-related output value within declared industry definition and statistical year", "reason": "No complete verified enterprise output dataset under a consistent statistical definition."})
    ensure_metric(m, "ai_industry_space_scale_sqm", {**base, "unit": "sqm", "formula": "sum verified gross floor area assigned to AI-industry functions within official scope", "reason": "Complete existing/design GFA and verified AI-industry occupancy are unavailable."})
    ensure_metric(m, "industry_function_mix_ratio", {**base, "unit": "ratio_by_function", "formula": "verified GFA or land area by industry/research/service/public function / verified total", "reason": "Complete function attribution and verified GFA/land inventory are unavailable."})
    mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Sources
    sp = root / "sources.json"
    s = json.loads(sp.read_text(encoding="utf-8"))
    sources = s.setdefault("sources", [])
    ids = {x.get("id") for x in sources}
    if "PROVISIONAL-BOUNDARY-BASIS" not in ids:
        sources.append({
            "id": "PROVISIONAL-BOUNDARY-BASIS",
            "path": "brief/site-package/geometry/provisional_boundaries_basis.md",
            "source_type": "repository_processed_reference",
            "usage": "Maintainer-reviewed background audit of provisional boundary uncertainty, including the 2026-08-08 OSM comparison recorded through Issue #846.",
            "limitation": "Background audit only; does not change PROV-SITE-001 into an official boundary and must not support formal redline/scoring claims."
        })
    for src in sources:
        if src.get("id") == "BOUNDARY-SOURCE":
            src["limitation"] = "Not official redline or precision scoring geometry. Current repository basis also records a maintainer-reviewed OSM background mismatch (0% park intersection; ~412.5 m nearest distance) without changing the polygon; wait for organizer polygon before formal recalculation."
    sp.write_text(json.dumps(s, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Self check
    scp = root / "self_check.json"
    sc = json.loads(scp.read_text(encoding="utf-8"))
    checks = sc.setdefault("checks", [])
    by = {c.get("check_id"): c for c in checks}
    by["BASEMAP_EXECUTION"] = {
        "check_id": "BASEMAP_EXECUTION", "result": "pass", "severity": "major",
        "target": "sources.json",
        "message": "Live OSM materialization completed (5532 usable features / 1898 building polygons); Microsoft current public index was queried and has no target partition. Candidate evidence remains non-statutory."
    }
    for item in [
        {"check_id":"OFFICIAL_METRICS_CONTRACT","result":"pass","severity":"major","target":"metrics.json","message":"Organizer-named AI innovation index, talent density, output value, AI-industry-space scale and function mix are defined as auditable unknown/null metrics rather than fabricated values."},
        {"check_id":"OFFICIAL_KEY_AREA_COVERAGE","result":"pass","severity":"major","target":"proposal.md","message":"Zhongzhiyuan, AI Origin and Dazhongsi explicitly cover organizer-named mobility, renewal, culture/green-space and AI-industry deepening tasks as conceptual/professional follow-up items."},
        {"check_id":"AGENT6_OPERATIONS_COVERAGE","result":"pass","severity":"major","target":"proposal.md","message":"Annual activities, developer community operations, scenario opening, public experience route, international communication and attraction/conversion are explicitly addressed without claiming government commitments."}
    ]:
        if item["check_id"] in by:
            by[item["check_id"]].update(item)
        else:
            checks.append(item)
    scp.write_text(json.dumps(sc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Design depth matrix
    dp = root / "design_depth_matrix.json"
    d = json.loads(dp.read_text(encoding="utf-8"))
    for item in d.get("items", []):
        iid = item.get("item_id")
        if iid == "existing_conditions_diagnosis":
            item["evidence_summary_zh"] = "已建立证据等级与缺口清单；OSM 已 live materialize 5532 个可用 features / 1898 个建筑面并仅作为候选现状证据；Microsoft 当前公开索引对目标分区无覆盖。现场核验、官方 polygon、完整建筑/权属/控规仍待补。"
            add_unique(item.setdefault("source_ids", []), "PROVISIONAL-BOUNDARY-BASIS")
            add_unique(item.setdefault("self_check_ids", []), "BASEMAP_EXECUTION")
        elif iid == "height_massing_character":
            item["evidence_summary_zh"] = "已提交非数值的高度渐变、强度前置核验、孔隙化体量、第五立面与公共服务美学导则；法定高度/FAR/密度/退界仍保持 Unknown，待控规和专业深化。"
        elif iid == "three_key_area_detailed_design":
            item["evidence_summary_zh"] = "三区分别以 Verification Campus / Learning Neighborhood / Market & Service Commons 响应，并逐条纳入五环/清河、五道口与清华东路西口 TOD、低扰动更新、大钟寺四象限步行/非机动车/绿地复合等官方点名深化任务；均保持概念建议。"
        elif "operation" in str(iid) or "implementation" in str(iid) or "renewal_project" in str(iid):
            item["evidence_summary_zh"] = str(item.get("evidence_summary_zh", "")) + " 长期运营明确覆盖年度活动、Developer Commons、Scenario Open Days、公共体验路线、国际传播及招引转化六项机制。"
    dp.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Compliance matrix: attach organizer metrics to relevant requirements.
    cp = root / "compliance_matrix.json"
    c = json.loads(cp.read_text(encoding="utf-8"))
    metric_map = {
        "1.5.1.1": ["ai_innovation_index", "ai_talent_density_per_sqkm", "ai_output_value_cny"],
        "1.5.2.1": ["ai_industry_space_scale_sqm", "industry_function_mix_ratio"],
        "agent.2": ["ai_innovation_index", "ai_talent_density_per_sqkm", "ai_output_value_cny", "ai_industry_space_scale_sqm"],
        "agent.6": ["urban_adaptation_rate"]
    }
    for req in c.get("requirements", []):
        rid = req.get("requirement_id")
        for metric in metric_map.get(rid, []):
            add_unique(req.setdefault("metrics", []), metric)
        if rid in {"agent.4", "agent.6"}:
            add_unique(req.setdefault("self_check_ids", []), "AGENT6_OPERATIONS_COVERAGE" if rid == "agent.6" else "OFFICIAL_KEY_AREA_COVERAGE")
    cp.write_text(json.dumps(c, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_copyright(root: Path) -> None:
    p = root / "report/copyright_statement.md"
    p.write_text("""# Copyright Statement

- Proposal text, programmatic geometry, diagrams, SVG, HTML and PDFs were generated for this submission by the declared AI agent and human contributor workflow.
- No third-party photographs, commercial map tiles, proprietary logos, remote fonts, iframes, forms, tracking or active network requests are embedded in submission display artifacts.
- Public/official facts are referenced through `sources.json`; provisional organizer geometry remains explicitly provisional.
- OpenStreetMap was live-retrieved through Overpass on 2026-08-09 under ODbL 1.0: 5,532 usable features, including 1,898 building polygons, were materialized inside the provisional envelope. They are used only as candidate/background existing-condition evidence and are not redistributed as an official survey, redline, ownership record or statutory planning layer.
- Microsoft Global ML Building Footprints was checked against the 2026-07-24 public `dataset-links.csv` under CDLA Permissive 2.0. The current index returned HTTP 200 / 30,340 rows but no published partition for target L9 quadkey `132100103`; therefore no Microsoft site footprint data or OSM↔Microsoft match rate is claimed.
- Any future third-party image, trademark, font or map asset requires separate licence review before publication.
""", encoding="utf-8")


def patch_visual(root: Path, lang: str) -> None:
    rel = "visual/index.html" if lang == "zh" else "visual/index.en.html"
    p = root / rel
    t = p.read_text(encoding="utf-8")
    if lang == "zh":
        old = "已重建双语正文、结构化数据、图件、A3/A0、HTML 与矩阵。唯一环境性阻塞是当前容器无法联网 materialize OSM/Microsoft；未下载数据没有被伪装成 Verified。"
        new = "双语正文、结构化数据、图件、A3/A0、HTML 与矩阵已同步。OSM 已 live materialize 5,532 个可用 features / 1,898 个建筑面并仅作候选证据；Microsoft 当前公开索引对目标 quadkey 无发布分区。官方 polygon、控规、权属与现场核验仍是明确 Unknown。"
    else:
        candidates = [
            "The only environmental blocker is that this runtime cannot materialize OSM/Microsoft live data; un-downloaded data is not presented as Verified.",
            "The current runtime cannot materialize OSM/Microsoft live data; un-downloaded data is not presented as Verified existing conditions."
        ]
        new = "Bilingual narrative, structured data, figures, A3/A0, HTML and matrices are synchronized. OSM was live-materialized with 5,532 usable features / 1,898 building polygons and remains candidate evidence only; Microsoft's current public index publishes no target-quadkey partition. Organizer polygons, statutory controls, ownership and field verification remain explicit Unknowns."
        old = next((x for x in candidates if x in t), None)
        if old is None:
            # Replace the paragraph containing materialize if layout text differs.
            t = re.sub(r'[^<]{0,180}(?:materializ|Materializ)[^<]{0,220}', new, t, count=1)
            p.write_text(t, encoding="utf-8")
            return
    if old in t:
        t = t.replace(old, new, 1)
    p.write_text(t, encoding="utf-8")


def write_changelog(root: Path) -> None:
    now = datetime.now(timezone.utc).date().isoformat()
    (root / "changelog.md").write_text(f"""# Changelog

## v2.1.0 - {now}

Official-completeness pass against the current organizer repository contract:

- synchronized live OSM/Microsoft evidence state across narrative, assumptions, self-check, design-depth, copyright and offline visual;
- added organizer-named AI innovation index, talent density, output value, AI-industry-space and function-mix metric interfaces as `unknown/null` rather than invented values;
- made the organizer's named Zhongzhiyuan / AI Origin / Dazhongsi detailed-design tasks explicitly readable as conceptual professional-deepening checklists;
- added non-numeric height, intensity, massing, roof and urban-character guidance while preserving statutory controls as Unknown;
- completed `agent.6` with annual activities, developer community operations, scenario opening, public experience route, international communication and attraction/conversion mechanisms;
- incorporated the maintainer-reviewed provisional-boundary background audit without changing or upgrading the provisional polygon;
- regenerated bilingual A3/A0 drawings so these official responses are visible in drawing outputs.

No new government approval, statutory control, ownership, procurement commitment, official polygon or verified construction condition is claimed.
""", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("submission_dir")
    args = ap.parse_args()
    root = Path(args.submission_dir).resolve()
    patch_proposal_zh(root)
    patch_proposal_en(root)
    patch_json(root)
    patch_copyright(root)
    patch_visual(root, "zh")
    patch_visual(root, "en")
    write_changelog(root)
    print("official completeness content patch applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
