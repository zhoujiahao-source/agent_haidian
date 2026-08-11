from __future__ import annotations
import os,re,json,hashlib,shutil
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A0,A3,landscape
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.utils import ImageReader

ROOT=Path(os.environ['SUBMISSION_ROOT']).resolve(); WORK=Path(os.environ.get('WORKSTREAM_ROOT','')).resolve() if os.environ.get('WORKSTREAM_ROOT') else None
FIG=ROOT/'assets/figures'; MEDIA=ROOT/'assets/media'; VIS=ROOT/'visual'; VAS=VIS/'assets'; DRAW=ROOT/'drawings'
for p in [FIG,MEDIA,VAS,DRAW]: p.mkdir(parents=True,exist_ok=True)
C={'paper':(246,244,237),'ink':(30,39,36),'muted':(96,107,101),'line':(198,204,198),'red':(182,83,69),'blue':(79,129,143),'gold':(184,149,75),'green':(98,127,104),'white':(255,255,255),'dark':(63,74,69)}
AREAS={'zhong':('众智园','Verification Campus','blue'),'origin':('AI 原点社区','Learning Neighborhood','gold'),'dazhongsi':('大钟寺','Market & Service Commons','red')}

def fontpath(b=False):
    cs=['/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc' if b else '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if b else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
    return next((x for x in cs if Path(x).exists()),cs[-1])
def F(n,b=False): return ImageFont.truetype(fontpath(b),n)
def tx(d,xy,s,n=28,b=False,fill=None,anchor=None): d.text(xy,s,font=F(n,b),fill=fill or C['ink'],anchor=anchor)
def iso(d,x,y,w,dep,h,col):
    d.polygon([(x,y-h),(x+w,y-h-dep//2),(x+w+dep,y-h),(x+dep,y-h+dep//2)],fill=tuple(min(255,q+24) for q in col),outline=C['line']); d.polygon([(x,y-h),(x+dep,y-h+dep//2),(x+dep,y+dep//2),(x,y)],fill=tuple(max(0,q-16) for q in col),outline=C['line']); d.polygon([(x+dep,y-h+dep//2),(x+w+dep,y-h),(x+w+dep,y),(x+dep,y+dep//2)],fill=col,outline=C['line'])
def tree(d,x,y): d.rectangle((x-3,y-18,x+3,y+7),fill=(105,88,70)); d.ellipse((x-16,y-48,x+16,y-16),fill=C['green'])
def person(d,x,y): d.ellipse((x-4,y-16,x+4,y-8),fill=C['dark']); d.line((x,y-8,x,y+6),fill=C['dark'],width=3)

def closeup(k,lang,out):
    zh,en,acn=AREAS[k]; ac=C[acn]; W,H=1600,980; im=Image.new('RGB',(W,H),C['paper']); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,120),fill=C['white']); d.rectangle((0,116,W,122),fill=ac); tx(d,(70,42),f'{zh} / {en}' if lang=='zh' else f'{en} / {zh}',42,True); tx(d,(1500,62),'CONCEPTUAL REVIEWER RENDER',18,True,ac,'ra'); tx(d,(1500,92),'Derived / Not yet canonicalized',16,False,C['muted'],'ra')
    d.polygon([(90,790),(1320,790),(1510,690),(280,690)],fill=(225,226,218),outline=C['line']); d.polygon([(170,748),(1220,748),(1380,690),(330,690)],fill=(242,238,227),outline=C['line']); d.polygon([(210,680),(1180,680),(1310,615),(340,615)],fill=(199,216,203)); [tree(d,260+i*82,665-(i%2)*8) for i in range(12)]
    if k=='zhong':
        iso(d,250,590,270,80,160,(150,165,160)); iso(d,900,570,260,90,180,(141,158,153)); iso(d,570,500,240,75,140,(166,175,169)); d.rectangle((620,610,880,735),outline=C['red'],width=5); tx(d,(750,635),'有界测试院' if lang=='zh' else 'Bounded Test',22,True,C['red'],'ma'); d.line((560,738,935,738),fill=ac,width=10); tx(d,(747,765),'普通旁路 / Human Stop' if lang=='zh' else 'Ordinary bypass / Human Stop',20,True,ac,'ma')
    elif k=='origin':
        for x,y,w in [(260,590,170),(500,535,150),(760,600,180),(1030,535,150)]: iso(d,x,y,w,65,110,(185,176,151))
        d.ellipse((600,585,880,735),fill=(224,218,194),outline=ac,width=4); tx(d,(740,642),'包容服务庭院' if lang=='zh' else 'Inclusive Court',22,True,ac,'ma'); d.line((330,748,1120,692),fill=ac,width=9); tx(d,(760,770),'无障碍主线 + 人工服务' if lang=='zh' else 'Accessible spine + human help',20,True,ac,'ma')
    else:
        for i in range(6): iso(d,230+i*175,575+(i%2)*18,115,48,80,(190,156,134))
        d.rectangle((270,700,1160,755),fill=(218,207,192),outline=ac,width=4); tx(d,(715,728),'市场服务街' if lang=='zh' else 'Market Service Street',22,True,ac,'mm'); d.rectangle((980,620,1230,675),fill=(202,207,201),outline=C['dark'],width=3); tx(d,(1105,648),'骑手 / 装卸口袋' if lang=='zh' else 'Rider / loading',18,True,C['dark'],'mm'); d.ellipse((520,610,760,700),fill=(229,222,205),outline=ac,width=4); tx(d,(640,650),'夜间城市客厅' if lang=='zh' else 'Night Commons',19,True,ac,'mm')
    for i in range(18): person(d,240+i*60,770-(i%3)*18)
    d.rectangle((0,850,W,H),fill=(43,52,48)); labs=['普通步行','无障碍','树荫避雨','人工帮助','应急','AI关闭仍可用'] if lang=='zh' else ['WALK','ACCESS','SHADE','HUMAN HELP','EMERGENCY','AI OFF OK']
    for i,l in enumerate(labs): x=70+i*250; d.rounded_rectangle((x,888,x+205,938),10,outline=(185,196,190),width=2); tx(d,(x+102,913),l,17,True,(240,240,234),'mm')
    im.save(out,optimize=True)

def mini(d,box,k,on,lang):
    x0,y0,x1,y1=box; zh,en,acn=AREAS[k]; ac=C[acn]; d.rounded_rectangle(box,14,fill=C['white'],outline=C['line'],width=2); tx(d,(x0+24,y0+22),zh if lang=='zh' else en,21,True,ac); tx(d,(x1-24,y0+23),'AI ON' if on else 'AI OFF',19,True,ac if on else C['dark'],'ra')
    for i in range(4): bx=x0+40+i*150; d.rectangle((bx,y0+70,bx+95,y0+130+(i%2)*20),fill=(208,211,205),outline=(170,176,171))
    d.line((x0+55,y1-65,x1-55,y0+155),fill=(244,239,225),width=16); d.rectangle((x0+60,y1-125,x1-70,y1-95),fill=(194,214,199))
    if on:
        labs=[('Ambient',C['blue']),('Consent',C['gold']),('Bounded',C['red'])]
    else:
        labs=[('Wayfinding',C['dark']),('Human help',C['dark']),('Bypass',C['dark'])]
    for j,(l,c) in enumerate(labs): xx=x0+115+j*190; d.rounded_rectangle((xx,y0+190,xx+150,y0+245),10,fill=(245,244,238),outline=c,width=3); tx(d,(xx+75,y0+218),l,15,True,c,'mm')

def onoff(lang,out):
    W,H=1900,1240; im=Image.new('RGB',(W,H),C['paper']); d=ImageDraw.Draw(im); tx(d,(70,55),'AI ON / AI OFF 空间证据' if lang=='zh' else 'AI ON / AI OFF Spatial Evidence',46,True); tx(d,(70,108),'同一城市底盘，AI 只增加可选择能力，不取消普通城市基线。' if lang=='zh' else 'The same civic floor remains usable; AI only adds optional capability layers.',24,False,C['muted']); tx(d,(1830,72),'CONCEPTUAL / DERIVED',18,True,C['red'],'ra')
    for k,y in zip(['zhong','origin','dazhongsi'],[165,505,845]): mini(d,(60,y,920,y+300),k,False,lang); mini(d,(980,y,1840,y+300),k,True,lang)
    d.rectangle((60,1165,1840,1215),fill=(43,52,48)); tx(d,(950,1190),'AI OFF = Permanent baseline · AI ON = Ambient / Consent / Bounded Test；均不代表已批准实施。' if lang=='zh' else 'AI OFF = Permanent baseline · AI ON = Ambient / Consent / Bounded Test; neither implies approved implementation.',18,True,(244,244,238),'mm'); im.save(out,optimize=True)

def cover(out):
    W,H=1600,1000; im=Image.new('RGB',(W,H),C['paper']); d=ImageDraw.Draw(im); d.rectangle((0,0,28,H),fill=C['red']); d.rectangle((28,0,W,10),fill=C['gold']); tx(d,(90,80),'京张·城市能力交换带',58,True); tx(d,(90,150),'JING-ZHANG URBAN CAPABILITY EXCHANGE',27,True,C['muted']); tx(d,(90,215),'城市成为 AI 进入现实世界的操作系统',31,True,C['red']); tx(d,(90,258),'City first · AI backstage · reversible public-value learning',22,False,C['muted']); d.line((150,375,1400,375),fill=C['dark'],width=10)
    for (zh,en),xx,c in zip([('大钟寺','Market'),('学习档案','Memory'),('小月河','Scenario'),('AI 原点','Learning'),('众智园','Verify')],[260,500,760,1030,1320],[C['red'],C['gold'],C['green'],C['gold'],C['blue']]): d.ellipse((xx-18,357,xx+18,393),fill=C['white'],outline=c,width=7); tx(d,(xx,430),zh,22,True,c,'ma'); tx(d,(xx,462),en,16,False,C['muted'],'ma')
    for i,(a,b,c) in enumerate([('众智园','BOUND TEST / HUMAN STOP',C['blue']),('AI 原点','ACCESS / HUMAN HELP',C['gold']),('大钟寺','MARKET / NIGHT COMMONS',C['red'])]): xx=90+i*500; d.rounded_rectangle((xx,550,xx+440,760),22,fill=C['white'],outline=c,width=4); tx(d,(xx+28,590),a,30,True,c); tx(d,(xx+28,640),b,18,True,C['muted']); d.line((xx+28,690,xx+390,690),fill=(210,211,202),width=16); d.line((xx+28,690,xx+250,690),fill=c,width=5); tx(d,(xx+28,730),'AI OFF baseline remains usable',16,False,C['dark'])
    d.rectangle((90,835,1510,920),fill=(43,52,48)); tx(d,(120,867),'Capability Backbone · PCI · Urban Adaptation Rate · STOP / MODIFY / CONTINUE / SCALE',20,True,(244,244,238)); tx(d,(120,900),'Concept proposal · Provisional geometry · No statutory FAR / height / ownership / road-redline claim',16,False,(196,205,200)); im.save(out,'WEBP',quality=88,method=6)

def patch_once(p,marker,block,before):
    t=p.read_text(encoding='utf-8');
    if marker in t:return
    if before not in t: raise RuntimeError(f'missing insertion point: {before}')
    p.write_text(t.replace(before,block+'\n\n'+before,1),encoding='utf-8')

def patch_text():
    p=ROOT/'proposal.md'; p.write_text(p.read_text(encoding='utf-8').replace('iteration: "v2.3.0"','iteration: "v2.4.0"'),encoding='utf-8')
    zh='''<!-- REVIEWER-SEQUENCE:V6 -->\n### 评委最终阅读路径：AI ON / AI OFF 成对证据\n\nv6 不增加新的城市概念，而把已有成果压缩为一条明确评审顺序：**总体结构 → 三区差异 → 人的地面层 → AI OFF 基线 → AI ON 可选能力 → 城市学习决策 → 证据与实施边界**。A0/A3、offline visual 与 Three.js 均采用同一顺序。\n\n![众智园近景](assets/figures/close-range-zhongzhiyuan.png)\n![AI 原点近景](assets/figures/close-range-ai-origin.png)\n![大钟寺近景](assets/figures/close-range-dazhongsi.png)\n\n![同一城市底盘的 AI OFF / AI ON 成对空间证据](assets/figures/ai-on-off-review.png)\n\n**AI OFF** 是正式设计底线：普通步行、物理无障碍、固定导视、树荫避雨、座席、人工帮助、普通交易/导航、应急与后勤持续工作。**AI ON** 只增加 Ambient、Consent 与 Bounded Test 三类可选择能力；个性化、识别或较高风险行为不能取消人工覆盖和普通旁路。三张近景与 AI ON/OFF 图均为 **Conceptual reviewer rendering / Derived / Not yet canonicalized**，不是现场照片、批准效果图或居民意见证据。\n\n正式离线 `visual/index.html` 新增本地 Three.js 评审入口。该模式只使用打包进本地 bundle 的 canonical proposal geometry 与 Derived reviewer detail，不请求 CDN、地图瓦片、Overpass、远程字体或网络 API；提供静态 fallback、键盘操作、loading/error 状态和 reduced-motion 行为。它用于比较空间层级与 AI ON/OFF，不替代 GeoJSON、A0/A3 或法定专业判断。'''
    patch_once(p,'<!-- REVIEWER-SEQUENCE:V6 -->',zh,'## AI 创新生态、人才画像与 AI+ 场景')
    e=ROOT/'proposal.en.md'; e.write_text(e.read_text(encoding='utf-8').replace('iteration: "v2.3.0"','iteration: "v2.4.0"'),encoding='utf-8')
    en='''<!-- REVIEWER-SEQUENCE:V6 -->\n### Final Reviewer Sequence: Paired AI ON / AI OFF Evidence\n\nv6 adds no new urban concept. It compresses the work into one review sequence: **overall structure → three-area differentiation → human ground interface → AI OFF baseline → AI ON optional capability → city-learning decision → evidence and implementation boundary**. A0/A3, the offline visual and Three.js follow the same sequence.\n\n![Zhongzhiyuan close range](assets/figures/close-range-zhongzhiyuan.en.png)\n![AI Origin close range](assets/figures/close-range-ai-origin.en.png)\n![Dazhongsi close range](assets/figures/close-range-dazhongsi.en.png)\n\n![Paired AI OFF / AI ON spatial evidence on the same civic floor](assets/figures/ai-on-off-review.en.png)\n\n**AI OFF** is the formal design floor: ordinary walking, physical accessibility, fixed wayfinding, shade/weather protection, seating, staffed help, ordinary transaction/navigation, emergency access and servicing keep working. **AI ON** only adds optional Ambient, Consent and Bounded Test layers. Personalization, recognition or higher-risk behavior never removes human override or the ordinary bypass. The close-range images are **Conceptual reviewer renderings / Derived / Not yet canonicalized** - not site photographs, approved renderings or evidence of resident opinion.\n\nThe formal offline `visual/index.html` now links to a locally bundled Three.js reviewer mode. It uses only canonical proposal geometry and Derived reviewer detail embedded in the local bundle, with no CDN, map tiles, Overpass, remote fonts or network APIs. It provides a static fallback, keyboard operation, loading/error state and reduced-motion behavior. It does not replace GeoJSON, A0/A3 or statutory professional judgment.'''
    patch_once(e,'<!-- REVIEWER-SEQUENCE:V6 -->',en,'## AI Innovation Ecosystem, Personas, and AI+ Scenarios')
    for name,lang in [('index.html','zh'),('index.en.html','en')]:
        q=VIS/name; t=q.read_text(encoding='utf-8')
        if 'reviewer-threejs.html' not in t:
            txt='同一城市底盘比较 Permanent baseline 与可选择 AI 能力。全部本地打包，无 CDN / 远程地图 / 网络 API。' if lang=='zh' else 'Compare the Permanent civic baseline with optional AI capability layers. Fully local: no CDN, remote maps or network APIs.'
            card=f'<section class="card wide"><h2>AI ON / AI OFF · Offline Three.js Reviewer</h2><p>{txt}</p><p><a href="reviewer-threejs.html" style="display:inline-block;padding:10px 14px;border:1px solid #b65345;color:#8f3e34;text-decoration:none;font-weight:bold">OPEN LOCAL 3D REVIEW</a></p><img src="assets/reviewer-fallback.png" alt="AI ON / AI OFF static fallback"></section>'
            q.write_text(t.replace('</main></body></html>',card+'</main></body></html>'),encoding='utf-8')
    cp=ROOT/'report/copyright_statement.md'; t=cp.read_text(encoding='utf-8'); marker='## v6 reviewer multimodal additions'
    if marker not in t: cp.write_text(t+'\n\n'+marker+'\n\n- `close-range-*.png`, `ai-on-off-review*.png`, `assets/media/cover.webp`, and `visual/assets/reviewer-fallback.png` are procedurally generated conceptual reviewer renderings. They are synthetic presentation artifacts, not photographs, resident testimony, approved renderings, or verified existing conditions.\n- The offline Three.js reviewer is bundled locally from Three.js 0.184.0 under the MIT License. It contains no CDN, remote tiles, remote fonts, trackers, Overpass, or other network API calls.\n- No identifiable real persons, private interiors, voices, music, or third-party trademarks are used in these additions.\n- KEY_AREA remains provisional; statutory FAR, height, ownership, road redlines, legal green boundaries and engineering capacity remain Unknown.\n',encoding='utf-8')
    ch=ROOT/'changelog.md'; t=ch.read_text(encoding='utf-8')
    if 'v2.4.0 reviewer narrative + multimodal' not in t: ch.write_text(t+'\n\n## v2.4.0 reviewer narrative + multimodal\n\n- Re-sequenced A0/A3 around structure → key areas → ground interface → AI OFF/ON → learning/governance → evidence/implementation.\n- Added three conceptual close-range key-area renderings, paired AI OFF/AI ON evidence, participant-authored cover, and local offline Three.js reviewer.\n- Preserved canonical GeoJSON and all statutory/ownership/engineering Unknowns.\n',encoding='utf-8')

def raster(p,tmp):
    if p.suffix.lower()!='.svg': return p
    import cairosvg; o=tmp/(p.stem+'.png'); cairosvg.svg2png(url=str(p),write_to=str(o),output_width=1800); return o
def place(c,p,x,y,w,h,tmp):
    p=raster(p,tmp); im=Image.open(p); iw,ih=im.size; s=min(w/iw,h/ih); ww,hh=iw*s,ih*s; c.drawImage(ImageReader(im),x+(w-ww)/2,y+(h-hh)/2,ww,hh,preserveAspectRatio=True,mask='auto')
def reg():
    try: pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
    except Exception: pass
def ptxt(c,x,y,s,n,lang,b=False): c.setFillColorRGB(.12,.16,.15); c.setFont('STSong-Light' if lang=='zh' else ('Helvetica-Bold' if b else 'Helvetica'),n); c.drawString(x,y,s)
def head(c,W,H,i,n,title,sub,lang): c.setFillColorRGB(.72,.33,.27); c.rect(0,H-12,W,12,fill=1,stroke=0); ptxt(c,24*mm,H-27*mm,title,25 if W>800*mm else 16,lang,True); c.setFillColorRGB(.38,.43,.4); c.setFont('STSong-Light' if lang=='zh' else 'Helvetica',10 if W>800*mm else 7.5); c.drawString(24*mm,H-35*mm,sub); c.setFont('Helvetica',8); c.drawRightString(W-22*mm,H-27*mm,f'{i:02d}/{n:02d}')
def foot(c,W): c.setFillColorRGB(.3,.34,.32); c.setFont('Helvetica',6.5); c.drawString(20*mm,8*mm,'JING-ZHANG URBAN CAPABILITY EXCHANGE · v2.4.0'); c.drawRightString(W-20*mm,8*mm,'PROVISIONAL / DERIVED WHERE MARKED · NOT STATUTORY')
def pdf(out,lang,a0):
    reg(); ps=landscape(A0 if a0 else A3); W,H=ps; c=canvas.Canvas(str(out),pagesize=ps,pageCompression=1); tmp=ROOT/'_tmp_v6'; tmp.mkdir(exist_ok=True)
    f=lambda b: FIG/(b if lang=='zh' else b.replace('.png','.en.png').replace('.svg','.en.svg')); close=lambda k: FIG/(f'close-range-{k}.png' if lang=='zh' else f'close-range-{k}.en.png'); oo=FIG/('ai-on-off-review.png' if lang=='zh' else 'ai-on-off-review.en.png')
    if a0: pages=[('01 / WHY + STRUCTURE','为什么是城市学习操作系统 / Why a learning city OS',[(f('site-overview.png'),(25,65,610,675)),(f('land-use-structure.png'),(660,390,480,350)),(f('regional-capability-network.png'),(660,70,480,280))]),('02 / THREE KEY AREAS','三区 30 秒比较 + 地面层 + AI OFF/ON',[(close('zhongzhiyuan'),(22,480,365,255)),(close('ai-origin'),(407,480,365,255)),(close('dazhongsi'),(792,480,365,255)),(f('ground-interface-proof.svg'),(22,78,555,360)),(oo,(600,78,555,360))]),('03 / LEARN + GOVERN','城市学习闭环、公共价值、实施与记忆',[(f('metrics-evidence.png'),(22,400,540,330)),(f('pci-prototypes.png'),(585,400,275,330)),(f('city-version-dashboard.png'),(880,400,275,330)),(f('mobility-bluegreen.png'),(22,70,360,285)),(f('landmarks-memory.png'),(402,70,360,285)),(f('twenty-year-legacy.png'),(782,70,373,285))])]
    else: pages=[('01 / COVER','评委阅读路线 / Reviewer route',[(MEDIA/'cover.webp',(18,45,384,215))]),('02 / OVERALL','一主轴 + 五学习单元 + 三区两翼',[(f('site-overview.png'),(18,75,240,175)),(f('land-use-structure.png'),(270,75,132,175))]),('03 / VERIFICATION CAMPUS','众智园：验证而不打断城市',[(close('zhongzhiyuan'),(18,75,250,175)),(f('ground-interface-proof.svg'),(276,75,126,175))]),('04 / LEARNING NEIGHBORHOOD','AI 原点：无障碍与人工服务是 Permanent baseline',[(close('ai-origin'),(18,75,250,175)),(f('reviewer-spatial-depth.svg'),(276,75,126,175))]),('05 / MARKET + SERVICE COMMONS','大钟寺：市场、骑手、通勤和夜生活共存',[(close('dazhongsi'),(18,75,250,175)),(f('mobility-bluegreen.png'),(276,75,126,175))]),('06 / AI OFF → AI ON','城市关闭 AI 仍成立；AI 只增加可选择能力',[(oo,(18,75,250,175)),(f('pci-prototypes.png'),(276,75,126,175))]),('07 / CITY LEARNING','Detect → Evidence → Risk → Trial → Review → STOP/MODIFY/CONTINUE/SCALE',[(f('metrics-evidence.png'),(18,75,240,175)),(f('city-version-dashboard.png'),(270,75,132,175))]),('08 / EVIDENCE + LEGACY','证据边界、分期、长期记忆',[(f('twenty-year-legacy.png'),(18,75,185,175)),(f('landmarks-memory.png'),(212,75,190,175))])]
    for i,(t,s,ims) in enumerate(pages,1): head(c,W,H,i,len(pages),t,s,lang); [place(c,p,x*mm,y*mm,w*mm,h*mm,tmp) for p,(x,y,w,h) in ims]; foot(c,W); c.showPage()
    c.save(); shutil.rmtree(tmp,ignore_errors=True)

def manifest():
    p=ROOT/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8')); m['cover_image']='assets/media/cover.webp'; fs=m['files']; ix={x['path']:x for x in fs if isinstance(x,dict) and x.get('path')}; add=[]
    for b in ['close-range-zhongzhiyuan','close-range-ai-origin','close-range-dazhongsi','ai-on-off-review']:
        add+=[{'path':f'assets/figures/{b}.png','role':'proposal_figure','required':False,'language':'zh'},{'path':f'assets/figures/{b}.en.png','role':'proposal_figure','required':False,'language':'en','translation_of':f'assets/figures/{b}.png'}]
    add += [{'path':'assets/media/cover.webp','role':'media_poster','required':False,'language':'neutral','title_zh':'京张·城市能力交换带概念封面','title_en':'Jing-Zhang Urban Capability Exchange conceptual cover','description_zh':'能力骨干、三区首层证据与 AI OFF 基线构成的参赛者概念封面。','description_en':'Participant-authored conceptual cover combining the Capability Backbone, three key-area ground interfaces and AI OFF baseline.'},{'path':'visual/reviewer-threejs.html','role':'visualization','required':False,'language':'neutral'},{'path':'visual/assets/reviewer-twin.bundle.js','role':'visualization','required':False,'language':'neutral'},{'path':'visual/assets/reviewer-fallback.png','role':'media_poster','required':False,'language':'neutral','title_zh':'离线 Three.js 静态回退','title_en':'Offline Three.js static fallback','description_zh':'WebGL 不可用时显示的三区 AI ON/OFF 静态对照。','description_en':'Static AI ON/OFF comparison shown if WebGL is unavailable.'}]
    for e in add: ix[e['path']].update(e) if e['path'] in ix else (fs.append(e),ix.setdefault(e['path'],e))
    for x in fs:
        r=x.get('path') if isinstance(x,dict) else None
        if r and r!='manifest.json' and (ROOT/r).is_file(): x['sha256']=hashlib.sha256((ROOT/r).read_bytes()).hexdigest()
    cl=m.setdefault('validation_claim',{}); cl['self_checked']=False; cl.pop('readiness_contract',None); p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def data():
    if not WORK:return
    td=WORK/'threejs'; td.mkdir(parents=True,exist_ok=True); rec={'status':'Derived / Not yet canonicalized','areas':[{'id':'zhong','zh':'众智园','en':'Verification Campus','accent':'blue'},{'id':'origin','zh':'AI 原点社区','en':'Learning Neighborhood','accent':'gold'},{'id':'dazhongsi','zh':'大钟寺','en':'Market & Service Commons','accent':'red'}]}; (td/'reviewer-data.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    for k,stem in [('zhong','zhongzhiyuan'),('origin','ai-origin'),('dazhongsi','dazhongsi')]: closeup(k,'zh',FIG/f'close-range-{stem}.png'); closeup(k,'en',FIG/f'close-range-{stem}.en.png')
    onoff('zh',FIG/'ai-on-off-review.png'); onoff('en',FIG/'ai-on-off-review.en.png'); cover(MEDIA/'cover.webp'); shutil.copy2(FIG/'ai-on-off-review.png',VAS/'reviewer-fallback.png'); patch_text(); data(); pdf(DRAW/'a0-boards.pdf','zh',True); pdf(DRAW/'a0-boards.en.pdf','en',True); pdf(DRAW/'a3-booklet.pdf','zh',False); pdf(DRAW/'a3-booklet.en.pdf','en',False); manifest(); print('v6 package built')
if __name__=='__main__': main()
