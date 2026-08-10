#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
SPEC = json.loads((HERE / "ground_interface_spec.json").read_text(encoding="utf-8"))
ROOT = Path(os.environ["SUBMISSION_ROOT"]).resolve()
FIG = ROOT / "assets" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

ZH_MARK = "<!-- GROUND-INTERFACE-PROOF:V5 -->"
EN_MARK = "<!-- GROUND-INTERFACE-PROOF:V5 -->"

ZH_BLOCK = r'''<!-- GROUND-INTERFACE-PROOF:V5 -->
### 首层与街道真实性：Ground Interface Proof

上一轮 Spatial Proof Rooms 回答“三区为什么不同”；本轮进一步回答**人在一层究竟如何走、坐、问人、避雨、绕开试验、进入商店或学习空间，以及 AI 关闭后城市是否仍然成立**。以下内容是 **Derived / Not yet canonicalized** 的近景城市设计证据层，不改变 canonical GeoJSON；示意剖面使用的是空间比例而非法定道路宽度。KEY_AREA 仍为 provisional，FAR、法定高度、权属、道路红线、绿地法定属性、地下管线与工程容量继续保持 Unknown。[data:geometry/key_areas.geojson#KEY-001] [assumption:A-CONTROLS-001]

| 重点区 | 首层/边缘组织 | 普通人主线 | 蓝绿与舒适 | AI / 测试后台边界 |
|---|---|---|---|---|
| 众智园 | 开放研发首层 → 治理评测界面 → 有界测试内缘 → 后勤设备边缘 | 公共门厅—林荫共享庭院—普通旁路—人工安全台，无需 AI 许可 | 树荫共享庭院、雨水花园、可坐边缘 | 高风险测试向内退让；Human Stop、应急入口和非参与者旁路同时存在 |
| AI 原点 | 学习共享首层 → 包容服务首层 → 慢行门廊 → 低扰动生活边缘 | 社区入口—校社学习客厅—包容庭院—慢行门廊；普通导视与人工帮助持续可用 | 可坐树荫庭院、透水/雨水边缘、避热节点 | Ambient 仅做低风险支持；个性化/识别性服务进入 Consent Layer |
| 大钟寺 | 市场服务首层 → 骑手/装卸口袋 → 夜间城市客厅 → 绿地复合庭院 | 站城方向—市场服务街—夜间客厅—绿地庭院；支付、导航、求助保留非 AI 方式 | 树池/雨水花园、遮荫座席、夜间停留 | 主步行线与骑手/装卸/后勤分层；AI 调度不取消人工管理与普通交易 |

![三区首层界面、无障碍普通路线、蓝绿舒适、运营边界与人的真实使用](assets/figures/ground-interface-proof.svg)

**众智园的真实感来自“边界分层”。** 面向城市的一侧先是共享门厅、研发展示与人工安全台；验证越高风险，空间越向内部后退。主要公共庭院不承担设备堆放或试验等待，保洁、安保、访客和轮椅用户都保留一条连续普通路径。有界测试只在安全缓冲、应急进入、人工停机和非参与者旁路同时成立时才具有空间资格。

**AI 原点的真实感来自“生活混合”。** 学生、老人、儿童、低视力用户和开发者共享同一套首层公共空间，而不是分成“AI 用户”和“普通用户”。最直接的无障碍路线与主要公共空间重合；人工服务点、固定公共信息、树荫座席和普通导视属于 Permanent baseline。Consent 不是弹窗，而是个性化服务从普通公共空间进入识别/个人数据层之前的空间与操作门槛。

**大钟寺的真实感来自“运营共存”。** 市场首层、骑手短停、补货装卸、通勤穿行、老人停留和夜间公共生活被放在同一张地面运营图里。骑手和装卸使用口袋空间而不是侵占主步行线；主要入口、座席、无障碍线和人工问询位于同一可达层。夜间安全依靠照明、可见人流、人工帮助和普通导航先成立，AI 只是辅助。

三处近景均采用同一条评审底线：**AI 全部关闭时，普通步行、无障碍、树荫/避雨、座席、人工帮助、基本交易/导航、应急和后勤仍然工作。** 只有通过这一底线的数字能力才进入 Ambient / Consent / bounded-test 层。所有门厅、树阵、雨水花园、骑手口袋、测试缓冲和首层界面位置目前均是 reviewer detail，后续必须结合真实建筑、道路、水务、消防、权属与现场测绘再决定是否 canonicalize。

'''

EN_BLOCK = r'''<!-- GROUND-INTERFACE-PROOF:V5 -->
### Ground Interface Proof: Street and Ground-Floor Realism

The previous Spatial Proof Rooms established **why the three areas are different**. This pass asks what a person actually experiences at ground level: **walking, sitting, asking a human for help, finding shade, bypassing a test, entering a shop or learning space, and continuing when AI is offline**. The following is **Derived / Not yet canonicalized** reviewer-detail design and does not alter canonical GeoJSON. Section graphics use spatial proportions rather than statutory road widths. KEY_AREA remains provisional; FAR, statutory height, ownership, road redlines, legal green-space status, underground utilities and engineering capacity remain Unknown. [data:geometry/key_areas.geojson#KEY-001] [assumption:A-CONTROLS-001]

| Key area | Ground-floor / edge sequence | Ordinary route | Blue-green comfort | AI / test backstage boundary |
|---|---|---|---|---|
| Zhongzhiyuan | open research frontage → governance review frontage → bounded-test inner edge → service/equipment edge | public lobby—shaded commons court—ordinary bypass—staffed safety desk, with no AI permission required | tree-shaded commons, rain-garden strip, sittable edges | higher-risk tests move inward; Human Stop, emergency access and non-participant bypass coexist |
| AI Origin | learning commons frontage → inclusive service frontage → slow-mobility threshold → low-disturbance living edge | neighborhood entry—learning commons—inclusive court—walking gate; ordinary signs and staffed help remain available | sittable shade court, permeable/rain edge, heat-refuge nodes | Ambient provides low-risk support only; personalization/recognition enters the Consent Layer |
| Dazhongsi | market-service frontage → rider/loading pocket → night commons → green mixed-use court | station-city direction—market street—night commons—green court; non-AI payment, navigation and help remain available | tree/rain-garden band, shaded seats, night stay | clear walk line is separated from rider/loading/service pockets; AI dispatch never removes human management or ordinary trade |

![Ground-interface proof for the three key areas: accessible ordinary routes, blue-green comfort, operating boundaries and everyday users](assets/figures/ground-interface-proof.en.svg)

**Zhongzhiyuan becomes credible through layered boundaries.** The city-facing edge begins with shared lobbies, visible research exchange and a staffed safety desk; greater test risk moves progressively inward. The main public court is not used as an equipment yard or test queue. Cleaners, security staff, visitors and wheelchair users keep a continuous ordinary route. A bounded test has spatial legitimacy only when safety buffer, emergency access, Human Stop and a non-participant bypass all exist together.

**AI Origin becomes credible through mixed daily life.** Students, older residents, children, low-vision users and developers share the same ground-floor civic spaces rather than being split into “AI users” and “ordinary users.” The most direct accessible route coincides with the main public realm. Staffed help, fixed public information, shade seating and ordinary wayfinding are Permanent baselines. Consent is treated as an operational and spatial threshold before personalized or recognition-based service enters the personal-data layer, not merely as a pop-up.

**Dazhongsi becomes credible through operational coexistence.** Market frontage, short rider stops, loading, commuting, older-user rest and night public life are reviewed on one ground-operations plan. Rider and loading functions use pockets instead of taking over the main walking line. Main entrances, seating, accessible movement and staffed help share the same reachable level. Night safety begins with lighting, visible activity, human help and ordinary navigation; AI remains support.

All three close-range prototypes share one review floor: **if every AI function is switched off, ordinary walking, accessibility, shade/rain protection, seating, staffed help, basic trade/navigation, emergency access and servicing must still work.** Only capabilities that pass this floor can enter Ambient, Consent or bounded-test layers. Locations of lobbies, tree rows, rain gardens, rider pockets, test buffers and ground-floor interfaces remain reviewer detail and require verified buildings, roads, water, fire, ownership and field-survey evidence before canonicalization.

'''


def patch_proposal(path: Path, marker: str, block: str, anchor: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r'iteration:\s*"v[^"]+"', 'iteration: "v2.3.0"', text, count=1)
    if marker not in text:
        if anchor not in text:
            raise RuntimeError(f"anchor not found in {path.name}: {anchor}")
        text = text.replace(anchor, block + anchor, 1)
    path.write_text(text, encoding="utf-8")


def text_svg(x: int, y: int, value: str, size: int = 22, weight: int = 400, fill: str = "#29302c", anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" font-family="Arial, Microsoft YaHei, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(value)}</text>'


def wrap(text: str, width: int) -> list[str]:
    if not text:
        return []
    if any('\u4e00' <= c <= '\u9fff' for c in text):
        out, line = [], ""
        for c in text:
            line += c
            if len(line) >= width or (c in "，。；：、" and len(line) >= width * 0.7):
                out.append(line); line = ""
        if line: out.append(line)
        return out
    words = text.split()
    out, line = [], ""
    for w in words:
        test = (line + " " + w).strip()
        if len(test) > width and line:
            out.append(line); line = w
        else:
            line = test
    if line: out.append(line)
    return out


def build_svg(lang: str) -> str:
    zh = lang == "zh"
    W, H = 1800, 1040
    bg, ink, muted, hair = "#f4f2eb", "#252b28", "#68726d", "#c7ccc5"
    accents = ["#4f818f", "#b8954b", "#b65345"]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="{bg}"/>']
    title = "三区 Ground Interface Proof｜城市先成立，AI 再进入" if zh else "Three Key Areas — Ground Interface Proof | City First, AI Backstage"
    sub = "Derived / Not yet canonicalized · KEY_AREA remains provisional · section proportions are diagrammatic" if not zh else "Derived / Not yet canonicalized · KEY_AREA 仍为 provisional · 剖面仅为空间比例示意"
    parts += [text_svg(64, 70, title, 38, 700, ink), text_svg(64, 108, sub, 17, 400, muted)]
    x0, gap, colw = 64, 28, 538
    for i, area in enumerate(SPEC["areas"]):
        x = x0 + i * (colw + gap)
        accent = accents[i]
        parts.append(f'<rect x="{x}" y="150" width="{colw}" height="808" rx="8" fill="#fbfaf6" stroke="{hair}"/>')
        parts.append(f'<rect x="{x}" y="150" width="{colw}" height="10" rx="5" fill="{accent}"/>')
        name = area["name_zh"] if zh else area["name_zh"].split("/")[-1].strip()
        thesis = area["ground_interface_thesis_zh"] if zh else area["ground_interface_thesis_en"]
        parts += [text_svg(x+24, 204, name, 28, 700, ink)]
        yy = 238
        for line in wrap(thesis, 31 if zh else 54)[:3]:
            parts.append(text_svg(x+24, yy, line, 17, 400, muted)); yy += 24
        parts.append(text_svg(x+24, 326, "GROUND EDGE SEQUENCE" if not zh else "首层 / 边缘序列", 14, 700, accent))
        edge_y = 354
        edge_w = (colw-48)/4
        for j, e in enumerate(area["edge_types"]):
            ex = x+24+j*edge_w
            parts.append(f'<rect x="{ex}" y="{edge_y}" width="{edge_w-6:.1f}" height="88" fill="{accent}" fill-opacity="{0.10+0.08*j:.2f}" stroke="{accent}" stroke-opacity=".55"/>')
            label = e["zh"] if zh else e["en"]
            for k, line in enumerate(wrap(label, 7 if zh else 15)[:3]):
                parts.append(text_svg(int(ex+8), edge_y+26+k*18, line, 13, 600, ink))
        parts.append(text_svg(x+24, 480, "ORDINARY + ACCESSIBLE ROUTE" if not zh else "普通 + 无障碍主线", 14, 700, accent))
        route = area["ordinary_route"] if zh else {"KEY-001":"Public lobby → shaded commons → ordinary bypass → staffed safety desk; no AI permission required.","KEY-002":"Neighborhood entry → learning commons → inclusive court → walking gate; ordinary signs and staffed help remain.","KEY-003":"Station-city direction → market street → night commons → green court; non-AI payment/navigation/help remain."}[area["id"]]
        for k, line in enumerate(wrap(route, 30 if zh else 62)[:3]):
            parts.append(text_svg(x+24, 510+k*22, line, 15, 400, ink))
        sec_y = 596
        parts.append(text_svg(x+24, sec_y, "DIAGRAMMATIC SECTION RATIO" if not zh else "剖面比例（非红线尺寸）", 14, 700, accent))
        ratios = area["section_ratio"]
        total = sum(ratios.values()); sx = x+24; sw = colw-48
        colors = ["#e5e1d7", "#d5dfd3", "#c9d7d9", "#e1d2b9", "#d6d0c5", "#c9c9c3"]
        cursor = sx
        for j, (key, val) in enumerate(ratios.items()):
            w = sw * val / total
            parts.append(f'<rect x="{cursor:.1f}" y="{sec_y+18}" width="{w:.1f}" height="48" fill="{colors[j%len(colors)]}" stroke="#b8beb8"/>')
            short = key.replace("_", " ")
            parts.append(text_svg(int(cursor+w/2), sec_y+48, short, 10, 500, muted, "middle"))
            cursor += w
        parts.append(text_svg(x+24, 704, "EVERYDAY USERS" if not zh else "真实使用者", 14, 700, accent))
        scenes = area["human_scenes"]
        for k, scene in enumerate(scenes[:5]):
            parts.append(f'<circle cx="{x+31}" cy="{734+k*29}" r="4" fill="{accent}"/>')
            parts.append(text_svg(x+44, 739+k*29, scene if zh else scene, 14, 400, ink))
        parts.append(text_svg(x+24, 900, "REVIEW FLOOR" if not zh else "评审底线", 14, 700, accent))
        floor = "AI off: walk + access + shade + seating + human help + emergency/service still work." if not zh else "AI 全关：步行、无障碍、树荫座席、人工帮助、应急/后勤仍可工作。"
        for k, line in enumerate(wrap(floor, 31 if zh else 58)[:2]):
            parts.append(text_svg(x+24, 928+k*19, line, 13, 500, ink))
    parts.append(text_svg(64, 1008, "Evidence status: canonical KEY_AREA / OSM candidate context / reviewer-detail ground interface. No statutory FAR, height, ownership or road-redline claim.", 14, 400, muted))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def add_manifest_file(m: dict, item: dict) -> None:
    files = m.setdefault("files", [])
    if not any(isinstance(x, dict) and x.get("path") == item["path"] for x in files):
        files.append(item)


def main() -> None:
    patch_proposal(ROOT / "proposal.md", ZH_MARK, ZH_BLOCK, "## AI 创新生态、人才画像与 AI+ 场景")
    patch_proposal(ROOT / "proposal.en.md", EN_MARK, EN_BLOCK, "## AI Innovation Ecosystem, Personas, and AI+ Scenarios")
    (FIG / "ground-interface-proof.svg").write_text(build_svg("zh"), encoding="utf-8")
    (FIG / "ground-interface-proof.en.svg").write_text(build_svg("en"), encoding="utf-8")

    changelog = ROOT / "changelog.md"
    c = changelog.read_text(encoding="utf-8") if changelog.exists() else "# Changelog\n"
    marker = "GROUND-INTERFACE-REALISM-V5"
    if marker not in c:
        c += "\n## v2.3.0 — Ground Interface Realism\n<!-- GROUND-INTERFACE-REALISM-V5 -->\n- Added reviewer-facing ground-floor/edge sequences for the three key areas.\n- Added ordinary + accessible route, blue-green comfort, human-help baseline, operations separation and AI-off review floor.\n- Added bilingual `ground-interface-proof.svg`; all detailed placements remain Derived / Not yet canonicalized.\n- No canonical GeoJSON geometry, statutory FAR/height, ownership, road-redline or approved-engineering claim was added.\n"
        changelog.write_text(c, encoding="utf-8")

    mp = ROOT / "manifest.json"
    m = json.loads(mp.read_text(encoding="utf-8"))
    add_manifest_file(m, {"path":"assets/figures/ground-interface-proof.svg","role":"proposal_figure","required":False,"language":"zh"})
    add_manifest_file(m, {"path":"assets/figures/ground-interface-proof.en.svg","role":"proposal_figure","required":False,"language":"en","translation_of":"assets/figures/ground-interface-proof.svg"})
    mp.write_text(json.dumps(m, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("ground-interface v5 deepening applied")
    print("proposal iteration: v2.3.0")
    print("atlas pair: ground-interface-proof.svg / .en.svg")

if __name__ == "__main__":
    main()
