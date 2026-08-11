from __future__ import annotations
import json, sys
from pathlib import Path

root=Path(sys.argv[1]).resolve()
visual=root/'visual'; media=root/'assets/media'; media.mkdir(parents=True,exist_ok=True)
# Static fallback is formal media, not a visual-runtime asset.
src=visual/'assets/reviewer-fallback.png'; dst=media/'reviewer-fallback.png'
if src.exists(): src.replace(dst)

csp="default-src 'self' data: blob:; connect-src 'none'; img-src 'self' data:; script-src 'self'; style-src 'unsafe-inline'; font-src 'self' data:; media-src 'self'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'"
css="""<style id=\"v6-three-style\">#threejs-reviewer{margin-top:18px;border:1px solid #c8cdc7;background:#faf9f4;padding:12px}#threejs-layout{display:grid;grid-template-columns:260px 1fr;gap:10px}#threejs-controls button{display:block;width:100%;margin:5px 0;padding:8px;text-align:left;border:1px solid #c8cdc7;background:white;cursor:pointer}#threejs-controls button[aria-pressed=\"true\"]{border-color:#b65345;box-shadow:inset 4px 0 #b65345}#scene{position:relative;min-height:520px;background:#e5e7e1}#fallback{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}.v6hud{font:11px monospace;margin:5px 0;color:#5e6964}@media(max-width:850px){#threejs-layout{grid-template-columns:1fr}#scene{min-height:420px}}@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}</style>"""

def integrate(name:str,en:bool)->None:
    p=visual/name; s=p.read_text(encoding='utf-8')
    s=s.replace('href="reviewer-threejs.html"','href="#threejs-reviewer"')
    s=s.replace('src="assets/reviewer-fallback.png"','src="../assets/media/reviewer-fallback.png"')
    if 'Content-Security-Policy' not in s:
        s=s.replace('<meta charset="utf-8">',f'<meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="{csp}">',1)
    title='Offline Three.js · AI ON / AI OFF' if en else '离线 Three.js · AI ON / AI OFF'
    intro='Same civic floor; optional AI never removes the ordinary baseline.' if en else '同一城市底盘；可选择 AI 能力不取消普通城市基线。'
    block=f'''<section id="threejs-reviewer" class="card wide"><h2>{title}</h2><p>{intro} <b>Derived / KEY_AREA provisional / not statutory.</b></p><div id="threejs-layout"><div id="threejs-controls"><button data-area="0" aria-pressed="true">1 · Zhongzhiyuan / 众智园</button><button data-area="1" aria-pressed="false">2 · AI Origin / AI 原点</button><button data-area="2" aria-pressed="false">3 · Dazhongsi / 大钟寺</button><hr><button data-ai="off" aria-pressed="true">O · AI OFF · Permanent baseline</button><button data-ai="on" aria-pressed="false">I · AI ON · Ambient / Consent / Bounded Test</button><div class="v6hud" id="areaTitle">Loading local model…</div><div class="v6hud" id="modeTitle">AI OFF · permanent civic baseline</div><div class="v6hud" id="status">LOCAL · OFFLINE · CONNECT-SRC NONE</div><p>Keyboard: 1–3 / O / I / R. Drag to orbit, wheel to zoom.</p></div><div id="scene" aria-label="Three-dimensional AI ON and AI OFF key-area reviewer model"><img id="fallback" src="../assets/media/reviewer-fallback.png" alt="Static fallback comparing AI OFF permanent civic baseline and AI ON optional capability in the three key areas"></div></div></section>'''
    if 'id="threejs-reviewer"' not in s: s=s.replace('</main>',block+'</main>',1)
    if 'assets/reviewer-twin.bundle.js' not in s: s=s.replace('</body>','<script src="assets/reviewer-twin.bundle.js"></script></body>',1)
    if 'id="v6-three-style"' not in s: s=s.replace('</head>',css+'</head>',1)
    p.write_text(s,encoding='utf-8')

integrate('index.html',False); integrate('index.en.html',True)
# Staging HTML is useful for bundle QA but is not a legal formal package path.
(visual/'reviewer-threejs.html').unlink(missing_ok=True)

p=root/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8')); files=[]
for item in m.get('files',[]):
    if not isinstance(item,dict): files.append(item); continue
    path=item.get('path')
    if path=='visual/reviewer-threejs.html': continue
    if path=='visual/assets/reviewer-fallback.png':
        item['path']='assets/media/reviewer-fallback.png'; item['role']='media_poster'; item['required']=False
        item['title_zh']='离线 Three.js 静态回退'; item['title_en']='Offline Three.js static fallback'
        item['description_zh']='WebGL 不可用时显示的三区 AI ON/OFF 静态对照。'
        item['description_en']='Static AI ON/OFF key-area comparison used when WebGL is unavailable.'
    files.append(item)
m['files']=files
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

for name in ['index.html','index.en.html']:
    t=(visual/name).read_text(encoding='utf-8')
    assert "connect-src 'none'" in t
    assert 'assets/reviewer-twin.bundle.js' in t
    assert '../assets/media/reviewer-fallback.png' in t
    assert 'reviewer-threejs.html' not in t
print('formal Three.js integrated into allowed visual/index HTML: PASS')
