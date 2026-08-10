#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path

ROOT = Path(os.environ.get("SUBMISSION_ROOT", "submissions/zhoujiahao-source/jingzhang-legible-ai-belt"))
MARKER = "<!-- REVIEWER-SPATIAL-DEEPENING:V4 -->"

ZH_SECTION = r'''

<!-- REVIEWER-SPATIAL-DEEPENING:V4 -->
### 评委视角：三区空间证据房间 / Spatial Proof Rooms

为了让重点区不只停留在“任务清单”，本轮把三处 KEY_AREA 统一深化为**可在 30 秒内审查的空间证据房间**。每一区都必须同时回答：**空间角色是什么、普通人怎么走、核心公共空间在哪里、首层如何工作、蓝绿如何进入、AI 在哪里退到后台、失败时如何旁路、哪些条件仍待核验**。以下深化属于 **Derived / Not yet canonicalized**；正式 `KEY_AREA` 仍为 provisional，法定 FAR/高度、权属、道路红线、绿地法定属性和工程容量仍保持 Unknown。

| 重点区 | 第一空间问题 | 核心空间房间 | 普通城市基线 | AI 后台位置 |
|---|---|---|---|---|
| 众智园 / Verification Campus | 高风险能力如何不打断普通城市生活地被验证？ | 验证共享庭院 / 有界测试院 / 治理评测厅 / 普通通行旁路 | 连续步行、标识、树荫、照明、人工安全控制、物理停机 | 受控测试与评测层；公共边界保持普通城市可读性 |
| AI 原点 / Learning Neighborhood | 高校、人才与社区如何共享低扰动公共服务空间？ | 校社学习客厅 / 包容服务庭院 / TOD慢行门廊 / 低扰动更新界面 | 物理无障碍、普通导视、人工帮助、固定服务信息 | Ambient 只承载低风险支持；个性化/识别进入 Consent Layer |
| 大钟寺 / Market & Service Commons | AI-native 服务如何在真实商业与夜间生活中被检验？ | 四象限慢行缝合 / 市场服务街 / 夜间城市客厅 / 绿地复合庭院 | 普通商业、可见导视、人工帮助、安全步行与照明 | 服务编排支持商户与使用者，但不替代普通交易/导航/求助 |

![评委视角三区空间证据房间：角色、公共空间、普通旁路、AI后台与证据状态](assets/figures/reviewer-spatial-depth.svg)

**众智园空间深化。** 公共边界采用开放研发共享空间与治理评测界面，受控实验向内部退让；有界测试院必须同时具有安全缓冲、Human Stop、普通通行旁路和应急进入条件。五环联系、清河文化资源、建筑—绿地—水系一体化继续作为专项 evidence gate，不在图中预设工程 crossing。

**AI 原点空间深化。** 以细颗粒校社缝合、包容服务庭院和低扰动更新界面替代“大拆大建式 AI 园区”。五道口站、清华东路西口站相关 TOD 只作为 walkshed 与公共生活衔接的研究任务；无障碍和人工服务属于 Permanent baseline，个人化 AI 服务不得替代物理公共服务。

**大钟寺空间深化。** 把四象限步行连续、市场服务街、夜间城市客厅和绿地复合庭院作为四个可审查空间房间；装卸、骑行、静态交通与夜间使用被放进同一公共空间逻辑。任何跨路连接、规划绿地复合利用和停车组织都先验证红线、绿地属性、消防和运营条件。

这组 Spatial Proof Rooms 是评委快速读取方案的**空间说明层**，不改变 canonical GeoJSON 的权威顺序；若后续专业审查认可，再把道路断面、公共空间组件和场景节点逐项反写为正式可验证 geometry。
'''

EN_SECTION = r'''

<!-- REVIEWER-SPATIAL-DEEPENING:V4 -->
### Reviewer Lens: Three Key-Area Spatial Proof Rooms

To move the three key areas beyond a task checklist, this iteration turns each KEY_AREA into a **30-second spatial proof**. Every area must make eight things immediately legible: **its urban role, ordinary movement, core public room, ground-floor relationship, blue-green function, where AI moves backstage, the non-participant bypass, and what evidence is still missing**. The following deepening is **Derived / Not yet canonicalized**. The formal `KEY_AREA` geometry remains provisional, while statutory FAR/height, ownership, road redlines, legal green-space status and engineering capacity remain Unknown.

| Key area | First spatial question | Core spatial rooms | Ordinary-city baseline | AI backstage position |
|---|---|---|---|---|
| Zhongzhiyuan / Verification Campus | How can higher-risk capabilities be tested without interrupting ordinary urban life? | Verification Commons Court / Bounded Test Yard / Governance Review Hall / Ordinary Bypass | continuous walking, signage, shade, lighting, manual safety control and physical stop | controlled test/review layers; public edge remains readable without AI |
| AI Origin / Learning Neighborhood | How can universities, talent and neighborhoods share low-disturbance public-service space? | Campus-Neighborhood Learning Commons / Inclusive Service Court / TOD Walking Gate / Low-disturbance Renewal Edge | physical accessibility, ordinary wayfinding, manual help and fixed service information | low-risk Ambient support only by default; personalization/recognition enters Consent Layer |
| Dazhongsi / Market & Service Commons | How can AI-native services be tested in real commerce and night-time public life? | Four-Quadrant Walking Stitch / Market Service Street / Night Urban Living Room / Green Mobility Court | ordinary commerce, visible wayfinding, staffed help, safe walking and lighting | service orchestration supports users/merchants but never replaces ordinary transaction, navigation or help |

![Reviewer spatial proof rooms for the three key areas: role, public realm, ordinary bypass, AI backstage and evidence status](assets/figures/reviewer-spatial-depth.en.svg)

**Zhongzhiyuan deepening.** Public-facing research commons and governance-review interfaces sit on the public edge, while controlled experiments move inward. Every bounded test yard must pair its safety buffer and Human Stop with an ordinary bypass and emergency access. Fifth Ring links, Qinghe cultural resources and building-green-water integration remain evidence-gated specialist tasks rather than assumed engineering crossings.

**AI Origin deepening.** Fine-grain campus-neighborhood stitches, inclusive service courts and low-disturbance renewal replace the image of a sealed AI park. Wudaokou and Qinghuadongluxikou station relationships remain walkshed/public-life research tasks. Physical accessibility and staffed/manual service are Permanent baselines; personalized AI cannot replace ordinary civic service.

**Dazhongsi deepening.** Four spatial proofs organize the review: four-quadrant walking continuity, a market-service street, a night urban living room and a green mobility court. Loading, cycling, static transport and night-time public life are reviewed together. Any crossing, planned-green multifunction use or parking arrangement remains conditional on verified road, green-space, fire-safety and operating constraints.

These Spatial Proof Rooms are a **reviewer-facing explanatory layer**. They do not override canonical GeoJSON. Only after professional review should approved road sections, public-space components and scenario nodes be written back into canonical geometry.
'''


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def atlas(lang: str) -> str:
    zh = lang == "zh"
    title = "三区空间证据房间｜评委快速审查图" if zh else "THREE KEY-AREA SPATIAL PROOFS | REVIEWER ATLAS"
    subtitle = "Derived / Not yet canonicalized · 非法定控规 · KEY_AREA provisional" if zh else "Derived / Not yet canonicalized · not statutory · KEY_AREA provisional"
    areas = [
        {
            "title": "众智园 / Verification Campus" if zh else "ZHONGZHIYUAN / VERIFICATION CAMPUS",
            "role": "Research · Test · Governance",
            "q": "高风险验证不打断普通生活" if zh else "TEST WITHOUT INTERRUPTING ORDINARY LIFE",
            "rooms": ["验证共享庭院","有界测试院","治理评测厅","普通通行旁路"] if zh else ["Verification Commons","Bounded Test Yard","Governance Review","Ordinary Bypass"],
            "base": "连续步行 + Human Stop + 应急旁路" if zh else "walk + Human Stop + emergency bypass",
            "accent": "#507f8e"
        },
        {
            "title": "AI原点 / Learning Neighborhood" if zh else "AI ORIGIN / LEARNING NEIGHBORHOOD",
            "role": "Community · Talent · Public Service",
            "q": "高校与社区共享低扰动服务" if zh else "LOW-DISTURBANCE CAMPUS–COMMUNITY SERVICE",
            "rooms": ["校社学习客厅","包容服务庭院","TOD慢行门廊","低扰动更新界面"] if zh else ["Learning Commons","Inclusive Service Court","TOD Walking Gate","Low-disturbance Edge"],
            "base": "物理无障碍 + 普通导视 + 人工服务" if zh else "physical access + wayfinding + staffed service",
            "accent": "#b8954b"
        },
        {
            "title": "大钟寺 / Market & Service Commons" if zh else "DAZHONGSI / MARKET & SERVICE COMMONS",
            "role": "Market · Service · Night Life",
            "q": "真实商业与夜间生活中验证服务" if zh else "TEST SERVICES IN REAL COMMERCE + NIGHT LIFE",
            "rooms": ["四象限慢行缝合","市场服务街","夜间城市客厅","绿地复合庭院"] if zh else ["Four-Quadrant Stitch","Market Service Street","Night Urban Living Room","Green Mobility Court"],
            "base": "普通商业 + 安全步行 + 可见求助" if zh else "ordinary commerce + safe walking + visible help",
            "accent": "#b45d4e"
        }
    ]
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="960" viewBox="0 0 1800 960">
<rect width="1800" height="960" fill="#f2f0e9"/>
<style>
.t{{font-family:Arial,"Microsoft YaHei",sans-serif;fill:#242a27}} .m{{font-family:Arial,"Microsoft YaHei",sans-serif;fill:#69736e}}
.h1{{font-size:32px;font-weight:700}} .h2{{font-size:21px;font-weight:700}} .h3{{font-size:14px;font-weight:700}} .b{{font-size:13px}} .s{{font-size:11px}}
</style>
<text x="46" y="54" class="t h1">{esc(title)}</text><text x="46" y="82" class="m b">{esc(subtitle)}</text>
<line x1="46" y1="102" x2="1754" y2="102" stroke="#b8beb8" stroke-width="1"/>
''']
    xs=[40,620,1200]
    for idx,(x,a) in enumerate(zip(xs,areas)):
        accent=a["accent"]
        out.append(f'''<g transform="translate({x},132)">
<rect x="0" y="0" width="560" height="754" rx="2" fill="#fbfaf6" stroke="#c7cbc5"/>
<rect x="0" y="0" width="7" height="754" fill="{accent}"/>
<text x="24" y="38" class="t h2">{esc(a['title'])}</text>
<text x="24" y="62" class="m b">{esc(a['role'])}</text>
<text x="24" y="94" class="t h3">{esc(a['q'])}</text>
<rect x="24" y="120" width="512" height="300" fill="#efeee8" stroke="#aaaFA9" stroke-dasharray="8 7"/>
<text x="34" y="142" class="m s">KEY_AREA · PROVISIONAL REVIEW FRAME</text>
<line x1="280" y1="150" x2="280" y2="402" stroke="#b44f40" stroke-width="8" opacity=".78"/>
<text x="290" y="170" class="m s">Capability Backbone</text>
<line x1="54" y1="272" x2="506" y2="272" stroke="#6b7570" stroke-width="4" stroke-dasharray="10 6"/>
<text x="58" y="262" class="m s">Derived cross-axis / relationship</text>
<rect x="58" y="178" width="158" height="66" fill="{accent}" opacity=".18" stroke="{accent}"/>
<rect x="344" y="178" width="150" height="66" fill="{accent}" opacity=".11" stroke="{accent}"/>
<rect x="58" y="300" width="158" height="70" fill="{accent}" opacity=".11" stroke="{accent}"/>
<rect x="344" y="300" width="150" height="70" fill="none" stroke="{accent}" stroke-width="2" stroke-dasharray="6 5"/>
<circle cx="280" cy="272" r="17" fill="#f3c96b" stroke="#6b5e3a"/><circle cx="280" cy="272" r="5" fill="#2c3a35"/>
<text x="64" y="203" class="t b">{esc(a['rooms'][0])}</text><text x="350" y="203" class="t b">{esc(a['rooms'][1])}</text>
<text x="64" y="329" class="t b">{esc(a['rooms'][2])}</text><text x="350" y="329" class="t b">{esc(a['rooms'][3])}</text>
<text x="24" y="454" class="t h3">{'普通城市基线 / NON-AI BASELINE' if zh else 'ORDINARY-CITY / NON-AI BASELINE'}</text>
<text x="24" y="478" class="m b">{esc(a['base'])}</text>
<text x="24" y="518" class="t h3">{'评委检查 / REVIEW CHECK' if zh else 'REVIEW CHECK'}</text>
<text x="24" y="542" class="m b">{'AI关闭后空间仍成立；实验关闭后通行仍连续。' if zh else 'Urban space still works with AI off; circulation remains continuous when experiments stop.'}</text>
<text x="24" y="582" class="t h3">{'证据状态 / EVIDENCE' if zh else 'EVIDENCE STATUS'}</text>
<rect x="24" y="598" width="116" height="24" fill="#ebe9e2" stroke="#9d9f99"/><text x="34" y="615" class="m s">KEY_AREA · PROV</text>
<rect x="148" y="598" width="112" height="24" fill="#f5ead0" stroke="#b8954b"/><text x="158" y="615" class="m s">ROAD · DERIVED</text>
<rect x="268" y="598" width="120" height="24" fill="#f3ded9" stroke="#b45d4e"/><text x="278" y="615" class="m s">ROOMS · PROPOSED</text>
<rect x="396" y="598" width="116" height="24" fill="#e8e9e6" stroke="#888f8a"/><text x="406" y="615" class="m s">FAR/HEIGHT · ?</text>
<line x1="24" y1="650" x2="536" y2="650" stroke="#d0d3cd"/>
<text x="24" y="680" class="t h3">{'空间判断不是工程承诺' if zh else 'SPATIAL JUDGMENT ≠ ENGINEERING COMMITMENT'}</text>
<text x="24" y="706" class="m s">{'所有房间为评审深化；只有通过专业复核后才反写 canonical geometry。' if zh else 'All rooms are reviewer deepening; only professionally reviewed elements may be written back to canonical geometry.'}</text>
<text x="24" y="730" class="m s">{'不推断法定高度、FAR、权属、红线、绿地属性或建设规模。' if zh else 'No inferred statutory height, FAR, ownership, road redline, green-space status or construction scale.'}</text>
</g>''')
    out.append('''<g transform="translate(46,914)"><circle cx="6" cy="0" r="5" fill="#f3c96b" stroke="#6b5e3a"/><text x="18" y="4" class="m s">PCI / public capability interface anchor</text><line x1="310" y1="0" x2="350" y2="0" stroke="#b44f40" stroke-width="6"/><text x="360" y="4" class="m s">Capability Backbone</text><line x1="570" y1="0" x2="610" y2="0" stroke="#6b7570" stroke-width="3" stroke-dasharray="8 5"/><text x="620" y="4" class="m s">Derived relationship, not road redline</text></g></svg>''')
    return "".join(out)


def insert_after_image(text: str, section: str, english: bool) -> str:
    if MARKER in text:
        return text
    pattern = r'!\[[^\n]*\]\(assets/figures/key-areas(?:\.en)?\.png\)'
    matches = list(re.finditer(pattern, text))
    if not matches:
        raise RuntimeError("key-areas figure anchor not found")
    m = matches[-1]
    return text[:m.end()] + section + text[m.end():]


def add_manifest_file(manifest: dict, path: str, language: str, translation_of: str | None = None) -> None:
    files = manifest.setdefault("files", [])
    if any(x.get("path") == path for x in files if isinstance(x, dict)):
        return
    item = {"path": path, "role": "proposal_figure", "required": False, "language": language}
    if translation_of:
        item["translation_of"] = translation_of
    files.append(item)


def update_hashes(manifest: dict) -> None:
    for item in manifest.get("files", []):
        if not isinstance(item, dict):
            continue
        rel = item.get("path")
        if not rel or rel == "manifest.json":
            continue
        p = ROOT / rel
        if p.is_file():
            item["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    if not ROOT.is_dir():
        raise SystemExit(f"submission root missing: {ROOT}")
    fig = ROOT / "assets/figures"
    fig.mkdir(parents=True, exist_ok=True)
    (fig / "reviewer-spatial-depth.svg").write_text(atlas("zh"), encoding="utf-8")
    (fig / "reviewer-spatial-depth.en.svg").write_text(atlas("en"), encoding="utf-8")

    zh = ROOT / "proposal.md"
    en = ROOT / "proposal.en.md"
    zt = zh.read_text(encoding="utf-8")
    et = en.read_text(encoding="utf-8")
    zt = re.sub(r'iteration:\s*"v[^"]+"', 'iteration: "v2.2.0"', zt, count=1)
    et = re.sub(r'iteration:\s*"v[^"]+"', 'iteration: "v2.2.0"', et, count=1)
    zh.write_text(insert_after_image(zt, ZH_SECTION, False), encoding="utf-8")
    en.write_text(insert_after_image(et, EN_SECTION, True), encoding="utf-8")

    changelog = ROOT / "changelog.md"
    ct = changelog.read_text(encoding="utf-8") if changelog.exists() else ""
    stamp = "## v2.2.0 — Reviewer spatial deepening"
    if stamp not in ct:
        ct = ct.rstrip() + "\n\n" + stamp + "\n\n- Added bilingual reviewer-facing Spatial Proof Rooms atlas for Zhongzhiyuan, AI Origin and Dazhongsi.\n- Deepened key-area movement, public-space, ground-floor, blue-green, Non-AI baseline and AI-backstage logic without inventing statutory controls.\n- Kept all new spatial rooms Derived / Not yet canonicalized pending professional review and official geometry.\n"
        changelog.write_text(ct, encoding="utf-8")

    mp = ROOT / "manifest.json"
    manifest = json.loads(mp.read_text(encoding="utf-8"))
    add_manifest_file(manifest, "assets/figures/reviewer-spatial-depth.svg", "zh")
    add_manifest_file(manifest, "assets/figures/reviewer-spatial-depth.en.svg", "en", "assets/figures/reviewer-spatial-depth.svg")
    update_hashes(manifest)
    mp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("reviewer spatial deepening applied")
    print("proposal iteration: v2.2.0")
    print("atlas pair: reviewer-spatial-depth.svg / .en.svg")

if __name__ == "__main__":
    main()
