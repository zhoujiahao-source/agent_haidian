#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from reportlab.lib.pagesizes import A0, A3, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas

pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))

ZH_FONT = "STSong-Light"
EN_FONT = "Helvetica"
EN_BOLD = "Helvetica-Bold"


def wrap_text(c, text, font, size, width):
    words = list(text) if font == ZH_FONT else text.split()
    lines=[]; cur=""
    for w in words:
        test = cur + w if font == ZH_FONT else (w if not cur else cur + " " + w)
        if c.stringWidth(test, font, size) <= width:
            cur=test
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines


def draw_paragraph(c, text, x, y, width, font, size=11, leading=15, max_lines=None):
    lines=wrap_text(c,text,font,size,width)
    if max_lines: lines=lines[:max_lines]
    c.setFont(font,size)
    for line in lines:
        c.drawString(x,y,line)
        y-=leading
    return y


def draw_title(c, title, subtitle, page_w, page_h, lang):
    font = ZH_FONT if lang=="zh" else EN_BOLD
    body = ZH_FONT if lang=="zh" else EN_FONT
    c.setFont(font, 28)
    c.drawString(38, page_h-48, title)
    c.setFont(body, 11)
    c.drawString(40, page_h-67, subtitle)
    c.line(38,page_h-76,page_w-38,page_h-76)


def draw_image_fit(c, path: Path, x, y, w, h):
    if not path.is_file():
        c.rect(x,y,w,h)
        c.drawString(x+8,y+h/2,"missing figure")
        return
    img=ImageReader(str(path))
    iw,ih=img.getSize()
    scale=min(w/iw,h/ih)
    dw,dh=iw*scale,ih*scale
    c.drawImage(img,x+(w-dw)/2,y+(h-dh)/2,dw,dh,preserveAspectRatio=True,mask='auto')
    c.rect(x,y,w,h,stroke=1,fill=0)


def footer(c, page_w, label, lang):
    font=ZH_FONT if lang=="zh" else EN_FONT
    c.setFont(font,8)
    c.drawRightString(page_w-36,20,label)


def figure(root, name, lang):
    if lang=="en":
        stem,ext=name.rsplit('.',1)
        return root / "assets/figures" / f"{stem}.en.{ext}"
    return root / "assets/figures" / name


def build_a3(root: Path, out: Path, lang: str):
    pw,ph=landscape(A3)
    c=canvas.Canvas(str(out), pagesize=(pw,ph))
    body=ZH_FONT if lang=="zh" else EN_FONT
    pages = []
    if lang=="zh":
        pages=[
          ("01 城市能力操作系统", "京张·城市能力交换带 / City First, AI Backstage", "site-overview.png",
           "一条 Capability Backbone 连接五个 Learning Units；AI 通过问题诊断、风险授权、可逆试验、公共价值评审、能力交换和主动退役进入城市。SITE_BOUNDARY / KEY_AREA 仍为 provisional，不是官方红线。"),
          ("02 总体空间结构与五条剖面", "Permanent / Adaptive / Experimental", "spatial-sections.png",
           "空间先满足普通步行、树荫、无障碍、消防和非 AI 服务，再放置 PCI。铁路记忆、慢行 stitch、蓝绿网络、能力节点与事件运营形成六层 Backbone。"),
          ("03 三处重点区：官方点名任务逐条进入深化", "众智园 / AI原点 / 大钟寺", "key-areas.png",
           "众智园：五环交通、清河文化、建筑-绿地-水系一体化与治理测试；AI原点：高校转化、五道口/清华东路西口 TOD 研究、低扰动更新；大钟寺：AI-native 业态、大钟寺站四象限步行、非机动车与绿地复合利用。以上均为概念建议，具体条件待专业核验。"),
          ("04 AI生态、场景与公共能力接口", "6 global cases / 8 personas / 12 scenarios / 4 bounded tests", "pci-prototypes.png",
           "PCI 六层：Non-AI Baseline / Ambient / Consent / Human Override / Failure-Safe / Public Learning Record。测试场景必须有非参与者旁路、人类 STOP 权和退出条件。"),
          ("05 公共空间、风貌与时间地标", "1909 → 2026 → Future + Retired Archive", "landmarks-memory.png",
           "高度、强度不造数：用渐变高度、承载力前置核验、孔隙化体量、第五立面与公共服务美学作为专业深化导则；法定 FAR/高度/退界继续 Unknown。"),
          ("06 长期运营：agent.6 六项机制", "全年持续学习 + 年度 City Version Release", "city-version-dashboard.png",
           "年度城市学习大会；Developer Commons；Scenario Open Days；无障碍公共体验路线；中英双语国际传播；Challenge→Sandbox→Pilot→Public-Value Review→采购/合作/规模化评估。无政府购买或签约承诺。"),
          ("07 指标与证据：定义先行，不造数", "UAR + organizer industry/talent metrics", "metrics-evidence.png",
           "新增官方指标接口：AI创新指数、AI人才密度、AI产值、AI产业空间规模、产业功能结构，全部保持 unknown/null 直到统计边界、企业/人才/产值和完整 GFA 数据可核验。OSM live=5,532 features / 1,898 buildings；Microsoft 当前目标分区=0，仅为候选/覆盖审计。"),
          ("08 官方任务覆盖与长期遗产", "agent.1–agent.6 / 20-year legacy", "twenty-year-legacy.png",
           "命名与 Open Node VI、6 个全球案例、12 场景、8 personas、4 测试场景、3+ 时间地标、铁路/中关村/AI文化叙事、年度活动、开发者运营、开放场景、公共路线、国际传播、招引转化均进入可读成果。20 年后留下普通公共空间、协议、开放接口与学习档案，而不是某一代模型。"),
        ]
    else:
        pages=[
          ("01 Urban Capability Operating System", "Jing-Zhang Urban Capability Exchange / City First, AI Backstage", "site-overview.png",
           "One Capability Backbone links five Learning Units. AI enters through diagnosis, risk authorization, reversible trials, public-value review, capability exchange and retirement. SITE_BOUNDARY / KEY_AREA remain provisional, not official redlines."),
          ("02 Spatial Structure and Five Sections", "Permanent / Adaptive / Experimental", "spatial-sections.png",
           "Ordinary walking, shade, accessibility, fire safety and non-AI services work first; PCI is added second. Railway memory, slow-mobility stitches, blue-green networks, capability nodes and event operations form the six-layer Backbone."),
          ("03 Three Key Areas: Organizer-Named Deepening Tasks", "Zhongzhiyuan / AI Origin / Dazhongsi", "key-areas.png",
           "Zhongzhiyuan: Fifth Ring access, Qinghe culture, building-green-water integration and governance tests. AI Origin: university conversion, Wudaokou/Qinghuadongluxikou TOD research and low-disturbance renewal. Dazhongsi: AI-native services, station four-quadrant walking, bicycle/static traffic and composite green-space use. All are conceptual tasks pending professional verification."),
          ("04 AI Ecosystem, Scenarios and PCI", "6 global cases / 8 personas / 12 scenarios / 4 bounded tests", "pci-prototypes.png",
           "PCI layers: Non-AI Baseline / Ambient / Consent / Human Override / Failure-Safe / Public Learning Record. Bounded tests require nonparticipant bypass, human STOP authority and exit conditions."),
          ("05 Public Realm, Character and Time Landmarks", "1909 → 2026 → Future + Retired Archive", "landmarks-memory.png",
           "No invented statutory numbers: stepped height, capacity-gated intensity, porous massing, fifth-facade roofs and a public-service aesthetic guide later professional design. Statutory FAR/height/setbacks remain Unknown."),
          ("06 Long-Term Operations: Full agent.6", "Continuous learning + annual City Version Release", "city-version-dashboard.png",
           "Annual Urban Learning Conference; Developer Commons; Scenario Open Days; accessible public experience route; bilingual international communication; Challenge→Sandbox→Pilot→Public-Value Review→procurement/partnership/scaling consideration. No guaranteed government purchase or partnership."),
          ("07 Metrics and Evidence: Define, Do Not Fabricate", "UAR + organizer industry/talent metrics", "metrics-evidence.png",
           "Organizer interfaces added as unknown/null: AI Innovation Index, AI Talent Density, AI Output Value, AI Industry Space Scale and Industry Function Mix. OSM live materialization=5,532 features / 1,898 buildings; Microsoft target partition=0. Both remain candidate/coverage evidence, never statutory survey."),
          ("08 Official Task Coverage and 20-Year Legacy", "agent.1–agent.6 / persistent civic assets", "twenty-year-legacy.png",
           "Naming/Open Node VI, six global cases, 12 scenarios, 8 personas, four bounded tests, 3+ time landmarks, railway/Zhongguancun/AI cultural narrative, annual activities, developer operations, open scenarios, public route, international communication and attraction/conversion are all readable outputs."),
        ]
    for i,(title,sub,img_name,text) in enumerate(pages,1):
        draw_title(c,title,sub,pw,ph,lang)
        draw_image_fit(c,figure(root,img_name,lang),38,70,pw*0.63,ph-160)
        x=pw*0.67; y=ph-120
        c.setFont(body,15 if lang=="zh" else 13)
        y=draw_paragraph(c,text,x,y,pw*0.29,body,15 if lang=="zh" else 12,22 if lang=="zh" else 17,18)
        if i==3:
            c.setFont(body,10)
            y-=10
            extras=("每一项均绑定 Evidence Gate：官方 polygon / 权属 / 道路红线 / 控规 / 市政 / 现场条件到位后再深化。" if lang=="zh" else "Every item is gated by organizer polygons, ownership, road redlines, statutory controls, utilities and field evidence before deepening.")
            draw_paragraph(c,extras,x,y,pw*0.29,body,10,14,8)
        footer(c,pw,f"Jing-Zhang Urban Capability Exchange · A3 {i}/{len(pages)}",lang)
        c.showPage()
    c.save()


def build_a0(root: Path, out: Path, lang: str):
    pw,ph=landscape(A0)
    c=canvas.Canvas(str(out), pagesize=(pw,ph))
    body=ZH_FONT if lang=="zh" else EN_FONT
    boards=[]
    if lang=="zh":
        boards=[
          ("A0-01 城市能力操作系统与总体空间", ["site-overview.png","land-use-structure.png","spatial-sections.png"],
           "一句话：城市不是部署 AI，而是学习如何改变自己。Capability Backbone + 五个 Learning Units，把铁路记忆、慢行、蓝绿、公共空间、PCI 与运营叠加为城市能力交换骨架。"),
          ("A0-02 三区详细设计、PCI 与公共空间", ["key-areas.png","pci-prototypes.png","landmarks-memory.png"],
           "官方重点区任务显式覆盖：众智园的五环/清河/建筑绿水一体化；AI原点的高校转化、五道口/清华东路西口 TOD 与低扰动更新；大钟寺的 AI-native 业态、四象限步行、非机动车与绿地复合。建筑导则采用渐变高度、孔隙体量、第五立面和公共服务美学，不伪造法定数值。"),
          ("A0-03 治理、指标、运营与证据", ["metrics-evidence.png","city-version-dashboard.png","twenty-year-legacy.png"],
           "UAR + 5 个官方产业/人才指标公式接口；全年学习 + 年度 City Version Release；Developer Commons、Scenario Open Days、公共体验路线、国际传播与招引转化。OSM 已 live materialize 5,532 features / 1,898 buildings；Microsoft 当前目标分区无覆盖；官方 polygon/控规/权属仍 Unknown。"),
        ]
    else:
        boards=[
          ("A0-01 Urban Capability OS and Spatial Structure", ["site-overview.png","land-use-structure.png","spatial-sections.png"],
           "Thesis: the city does not merely deploy AI; it learns how to change itself. Capability Backbone + five Learning Units combine railway memory, walking, blue-green space, public realm, PCI and operations as an urban capability-exchange structure."),
          ("A0-02 Key Areas, PCI and Public Realm", ["key-areas.png","pci-prototypes.png","landmarks-memory.png"],
           "Organizer key-area tasks are explicit: Zhongzhiyuan Fifth Ring/Qinghe/building-green-water integration; AI Origin university conversion, Wudaokou/Qinghuadongluxikou TOD and low-disturbance renewal; Dazhongsi AI-native services, four-quadrant walking, bicycle/static traffic and composite green-space use. Building guidance uses stepped height, porous massing, fifth-facade roofs and public-service aesthetics without invented statutory values."),
          ("A0-03 Governance, Metrics, Operations and Evidence", ["metrics-evidence.png","city-version-dashboard.png","twenty-year-legacy.png"],
           "UAR + five organizer industry/talent metric interfaces; continuous learning + annual City Version Release; Developer Commons, Scenario Open Days, public experience route, international communication and attraction/conversion. OSM live=5,532 features / 1,898 buildings; Microsoft target partition unavailable; organizer polygons/statutory controls/ownership remain Unknown."),
        ]
    for i,(title,imgs,text) in enumerate(boards,1):
        draw_title(c,title,"Jing-Zhang Urban Capability Exchange · Official completeness v2.1",pw,ph,lang)
        margin=45; gap=22; y0=150; h=ph-260; w=(pw-2*margin-2*gap)/3
        for j,name in enumerate(imgs):
            draw_image_fit(c,figure(root,name,lang),margin+j*(w+gap),y0,w,h)
        c.setFont(body,15 if lang=="zh" else 13)
        draw_paragraph(c,text,margin,118,pw-2*margin,body,15 if lang=="zh" else 13,20 if lang=="zh" else 17,5)
        footer(c,pw,f"Jing-Zhang Urban Capability Exchange · A0 {i}/{len(boards)}",lang)
        c.showPage()
    c.save()


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("submission_dir"); args=ap.parse_args()
    root=Path(args.submission_dir).resolve(); drawings=root/"drawings"; drawings.mkdir(exist_ok=True)
    build_a3(root,drawings/"a3-booklet.pdf","zh")
    build_a3(root,drawings/"a3-booklet.en.pdf","en")
    build_a0(root,drawings/"a0-boards.pdf","zh")
    build_a0(root,drawings/"a0-boards.en.pdf","en")
    print("generated bilingual A3/A0 official-completeness drawings")

if __name__=="__main__": main()
