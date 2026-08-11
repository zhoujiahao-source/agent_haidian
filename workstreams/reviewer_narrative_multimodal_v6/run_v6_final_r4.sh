#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
from pathlib import Path
# 1) descriptive image alt text in the reproducible builder
p=Path('workstreams/reviewer_narrative_multimodal_v6/build_v6.py')
t=p.read_text(encoding='utf-8')
t=t.replace('![众智园近景](assets/figures/close-range-zhongzhiyuan.png)','![众智园验证园区首层、普通旁路与有界测试近景示意](assets/figures/close-range-zhongzhiyuan.png)')
t=t.replace('![大钟寺近景](assets/figures/close-range-dazhongsi.png)','![大钟寺市场服务街、骑手装卸口袋与夜间公共空间近景示意](assets/figures/close-range-dazhongsi.png)')
p.write_text(t,encoding='utf-8')

# 2) strict manifest agent disclosure must include model_detail
p=Path('workstreams/reviewer_narrative_multimodal_v6/run_v6_final_r2.sh')
t=p.read_text(encoding='utf-8')
t=t.replace("m.setdefault('agent',{})['model_family']='gpt'","m.setdefault('agent',{})['model_family']='gpt'\\nm['agent']['model_detail']='GPT-5.6 Sol'",1)
p.write_text(t,encoding='utf-8')

# 3) current validator reads root tracks.json
p=Path('workstreams/reviewer_narrative_multimodal_v6/run_v6_final_r3.sh')
t=p.read_text(encoding='utf-8').replace('/tracks/\\nEOF','/tracks/\\n/tracks.json\\nEOF',1)
p.write_text(t,encoding='utf-8')

# 4) formal visual may only use visual/index*.html + visual/assets/*.
# Patch base runner so Three.js is embedded in the allowed index HTMLs, while fallback media lives under assets/media/.
p=Path('workstreams/reviewer_narrative_multimodal_v6/run_v6_final.sh')
t=p.read_text(encoding='utf-8')
t=t.replace('cp "$SRC/reviewer-threejs.html" "$DST/reviewer-threejs.html"','''python - <<'PY2'
from pathlib import Path
root=Path('/tmp/formal-v6-final/submissions/zhoujiahao-source/jingzhang-legible-ai-belt')
# Move static fallback to the official media location.
media=root/'assets/media'; media.mkdir(parents=True,exist_ok=True)
src=root/'visual/assets/reviewer-fallback.png'
if src.exists(): src.replace(media/'reviewer-fallback.png')
# Embed the local Three.js shell into the only allowed formal visual HTML entry points.
csp="default-src 'self' data: blob:; connect-src 'none'; img-src 'self' data:; script-src 'self'; style-src 'unsafe-inline'; font-src 'self' data:; media-src 'self'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'"
css='''<style id="v6-three-style">#threejs-reviewer{margin-top:18px;border:1px solid #c8cdc7;background:#faf9f4;padding:12px}#threejs-layout{display:grid;grid-template-columns:260px 1fr;gap:10px}#threejs-controls button{display:block;width:100%;margin:5px 0;padding:8px;text-align:left;border:1px solid #c8cdc7;background:white;cursor:pointer}#threejs-controls button[aria-pressed="true"]{border-color:#b65345;box-shadow:inset 4px 0 #b65345}#scene{position:relative;min-height:520px;background:#e5e7e1}#fallback{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}.v6hud{font:11px monospace;margin:5px 0;color:#5e6964}@media(max-width:850px){#threejs-layout{grid-template-columns:1fr}#scene{min-height:420px}}@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}</style>'''
for name,en in [('index.html',False),('index.en.html',True)]:
    p=root/'visual'/name; s=p.read_text(encoding='utf-8')
    # Remove the earlier link-card target and point its fallback to official media.
    s=s.replace('href="reviewer-threejs.html"','href="#threejs-reviewer"').replace('src="assets/reviewer-fallback.png"','src="../assets/media/reviewer-fallback.png"')
    if 'Content-Security-Policy' not in s:
        s=s.replace('<meta charset="utf-8">',f'<meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="{csp}">',1)
    title='Offline Three.js · AI ON / AI OFF' if en else '离线 Three.js · AI ON / AI OFF'
    intro='Same civic floor; optional AI never removes the ordinary baseline.' if en else '同一城市底盘；可选择 AI 能力不取消普通城市基线。'
    block=f'''<section id="threejs-reviewer" class="card wide"><h2>{title}</h2><p>{intro} <b>Derived / KEY_AREA provisional / not statutory.</b></p><div id="threejs-layout"><div id="threejs-controls"><button data-area="0" aria-pressed="true">1 · Zhongzhiyuan / 众智园</button><button data-area="1" aria-pressed="false">2 · AI Origin / AI 原点</button><button data-area="2" aria-pressed="false">3 · Dazhongsi / 大钟寺</button><hr><button data-ai="off" aria-pressed="true">O · AI OFF · Permanent baseline</button><button data-ai="on" aria-pressed="false">I · AI ON · Ambient / Consent / Bounded Test</button><div class="v6hud" id="areaTitle">Loading local model…</div><div class="v6hud" id="modeTitle">AI OFF · permanent civic baseline</div><div class="v6hud" id="status">LOCAL · OFFLINE · CONNECT-SRC NONE</div><p>Keyboard: 1–3 / O / I / R. Drag to orbit, wheel to zoom.</p></div><div id="scene" aria-label="Three-dimensional AI ON and AI OFF key-area reviewer model"><img id="fallback" src="../assets/media/reviewer-fallback.png" alt="Static fallback comparing AI OFF permanent civic baseline and AI ON optional capability in the three key areas"></div></div></section>'''
    if 'id="threejs-reviewer"' not in s:
        s=s.replace('</main>',block+'</main>',1)
    if 'assets/reviewer-twin.bundle.js' not in s:
        s=s.replace('</body>','<script src="assets/reviewer-twin.bundle.js"></script></body>',1)
    if 'id="v6-three-style"' not in s:
        s=s.replace('</head>',css+'</head>',1)
    p.write_text(s,encoding='utf-8')
PY2''',1)
t=t.replace('if grep -Eiq \'https?://|//cdn\' "$DST/reviewer-threejs.html"; then echo \'reviewer HTML contains a remote runtime reference\'; exit 1; fi','''for HTML in "$DST/index.html" "$DST/index.en.html"; do
  if grep -Eiq 'https?://|//cdn' "$HTML"; then echo "formal visual contains a remote runtime reference: $HTML"; exit 1; fi
  grep -Fq "connect-src 'none'" "$HTML"
  grep -q 'prefers-reduced-motion' "$HTML"
  grep -q 'aria-pressed' "$HTML"
  grep -q '../assets/media/reviewer-fallback.png' "$HTML"
done''',1)
t=t.replace('grep -Fq "connect-src \'none\'" "$DST/reviewer-threejs.html"\ngrep -q \'prefers-reduced-motion\' "$DST/reviewer-threejs.html"\ngrep -q \'aria-pressed\' "$DST/reviewer-threejs.html"\ngrep -q \'reviewer-fallback.png\' "$DST/reviewer-threejs.html"\n','',1)
t=t.replace("p=Path('/tmp/formal-v6-final/submissions/zhoujiahao-source/jingzhang-legible-ai-belt/visual/reviewer-threejs.html')","p=Path('/tmp/formal-v6-final/submissions/zhoujiahao-source/jingzhang-legible-ai-belt/visual/index.html')",1)
t=t.replace("assert 'assets/reviewer-fallback.png' in t","assert '../assets/media/reviewer-fallback.png' in t",1)
# Clean manifest entries after builder: remove disallowed extra HTML, relocate fallback media metadata.
needle='printf \'\\n== refresh manifest hashes ==\\n\''
cleanup='''python - <<'PY2'
import json
from pathlib import Path
root=Path('/tmp/formal-v6-final/submissions/zhoujiahao-source/jingzhang-legible-ai-belt'); p=root/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8'))
new=[]
for item in m.get('files',[]):
    path=item.get('path') if isinstance(item,dict) else None
    if path=='visual/reviewer-threejs.html': continue
    if path=='visual/assets/reviewer-fallback.png':
        item['path']='assets/media/reviewer-fallback.png'; item['role']='media_poster'; item['required']=False
        item['title_zh']='离线 Three.js 静态回退'; item['title_en']='Offline Three.js static fallback'
        item['description_zh']='WebGL 不可用时显示的三区 AI ON/OFF 静态对照。'; item['description_en']='Static AI ON/OFF key-area comparison used when WebGL is unavailable.'
    new.append(item)
m['files']=new
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\\n',encoding='utf-8')
PY2
\n'''+needle
if needle not in t: raise SystemExit('manifest cleanup insertion point missing')
t=t.replace(needle,cleanup,1)
p.write_text(t,encoding='utf-8')
print('patched v6 formal packaging for current validator')
PY
bash workstreams/reviewer_narrative_multimodal_v6/run_v6_final_r3.sh
