#!/usr/bin/env bash
set -euo pipefail
ROOT="$PWD/workstreams/reviewer_narrative_multimodal_v6"
PKG="submissions/zhoujiahao-source/jingzhang-legible-ai-belt"
FORMAL_BRANCH="submission/zhoujiahao-source/jingzhang-urban-capability-exchange-v6-reviewer-multimodal"
AUDITED="9f67bf2771b96cbec9ce47fff32d43f494b22695"

printf '\n== resolve current upstream ==\n'
LATEST="$(git ls-remote https://github.com/open-city-ai/haidian.git refs/heads/main | cut -f1)"
echo "audited=$AUDITED"
echo "latest=$LATEST"
if [ "$LATEST" != "$AUDITED" ]; then
  rm -rf /tmp/upstream-guard-v6 && git init -q /tmp/upstream-guard-v6
  git -C /tmp/upstream-guard-v6 remote add origin https://github.com/open-city-ai/haidian.git
  git -C /tmp/upstream-guard-v6 -c protocol.version=2 fetch -q --no-tags --filter=blob:none origin "$AUDITED" "$LATEST"
  git -C /tmp/upstream-guard-v6 diff --name-only "$AUDITED" "$LATEST" > /tmp/upstream-v6-changed.txt
  python - <<'PY'
from pathlib import Path
fs=[x.strip() for x in Path('/tmp/upstream-v6-changed.txt').read_text().splitlines() if x.strip()]
non=[f for f in fs if not (f.startswith('submissions/') or f=='submissions-data.js')]
print('changed paths since audited baseline:',len(fs))
if non:
    print('Rule/tool/source changes require re-audit:')
    print('\n'.join(non)); raise SystemExit(1)
print('Only peer submissions/gallery changed since audited baseline.')
PY
fi

printf '\n== materialize v6 formal branch ==\n'
gh auth setup-git
rm -rf /tmp/formal-v6-final
git clone -q --filter=blob:none --sparse https://github.com/zhoujiahao-source/agent_haidian.git /tmp/formal-v6-final
git -C /tmp/formal-v6-final sparse-checkout set "$PKG"
git -C /tmp/formal-v6-final switch -q "$FORMAL_BRANCH"

printf '\n== build reviewer sequence / close range / cover / A0+A3 ==\n'
SUBMISSION_ROOT="/tmp/formal-v6-final/$PKG" WORKSTREAM_ROOT="$ROOT" python "$ROOT/build_v6.py"

printf '\n== bundle formal local Three.js ==\n'
SRC="$ROOT/threejs"
DST="/tmp/formal-v6-final/$PKG/visual"
cp "$SRC/reviewer-threejs.html" "$DST/reviewer-threejs.html"
(
  cd "$SRC"
  npx esbuild reviewer_twin_src.js --bundle --format=iife --platform=browser --target=es2020 --minify --legal-comments=none --outfile="$DST/assets/reviewer-twin.bundle.js" --loader:.json=json
)
node --check "$DST/assets/reviewer-twin.bundle.js"
# Runtime network contract: participant code has no network calls, HTML has no remote runtime URLs,
# and CSP blocks all connect-src requests even though Three.js may contain dormant generic loader code.
if grep -Eiq 'fetch\(|XMLHttpRequest|WebSocket|EventSource' "$SRC/reviewer_twin_src.js"; then echo 'participant Three.js source contains a network API'; exit 1; fi
if grep -Eiq 'https?://|//cdn' "$DST/reviewer-threejs.html"; then echo 'reviewer HTML contains a remote runtime reference'; exit 1; fi
grep -Fq "connect-src 'none'" "$DST/reviewer-threejs.html"
grep -q 'prefers-reduced-motion' "$DST/reviewer-threejs.html"
grep -q 'aria-pressed' "$DST/reviewer-threejs.html"
grep -q 'reviewer-fallback.png' "$DST/reviewer-threejs.html"
python - <<'PY'
from pathlib import Path
p=Path('/tmp/formal-v6-final/submissions/zhoujiahao-source/jingzhang-legible-ai-belt/visual/reviewer-threejs.html')
t=p.read_text(encoding='utf-8')
assert 'connect-src \'none\'' in t
assert 'assets/reviewer-twin.bundle.js' in t
assert 'assets/reviewer-fallback.png' in t
print('offline Three.js contract: PASS')
PY

python workstreams/reviewer_narrative_multimodal_v6/integrate_threejs_into_visual.py "/tmp/formal-v6-final/$PKG"

printf '\n== refresh manifest hashes ==\n'
SUB="/tmp/formal-v6-final/$PKG" SUB="$SUB" python - <<'PY'
import os,json,hashlib
from pathlib import Path
root=Path(os.environ['SUB']); p=root/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8'))
for item in m.get('files',[]):
    if not isinstance(item,dict): continue
    rel=item.get('path')
    if rel and rel!='manifest.json' and (root/rel).is_file(): item['sha256']=hashlib.sha256((root/rel).read_bytes()).hexdigest()
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
PY

printf '\n== PDF render / no blank QA ==\n'
mkdir -p "$ROOT/validation"
python - <<'PY'
import json,fitz
from pathlib import Path
from PIL import Image,ImageStat,ImageOps,ImageDraw
root=Path('/tmp/formal-v6-final/submissions/zhoujiahao-source/jingzhang-legible-ai-belt/drawings')
out=Path('workstreams/reviewer_narrative_multimodal_v6/validation'); checks={}
def check(name,expected,contact):
    doc=fitz.open(root/name); assert len(doc)==expected,(name,len(doc),expected)
    thumbs=[]; rec=[]
    for i,p in enumerate(doc):
        pix=p.get_pixmap(matrix=fitz.Matrix(.22,.22),alpha=False)
        im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        stat=ImageStat.Stat(im); std=sum(stat.stddev)/3
        gray=ImageOps.grayscale(im); hist=gray.histogram(); nonwhite=1-sum(hist[248:256])/(im.width*im.height)
        assert std>2.0,(name,i+1,std); assert nonwhite>.015,(name,i+1,nonwhite)
        rec.append({'page':i+1,'stddev':round(std,2),'nonwhite_fraction':round(nonwhite,4),'size_px':[im.width,im.height]})
        im.thumbnail((360,240)); thumbs.append(im.copy())
    sheet=Image.new('RGB',(380*len(thumbs),270),'white'); d=ImageDraw.Draw(sheet)
    for j,im in enumerate(thumbs): sheet.paste(im,(j*380+10,20)); d.text((j*380+10,248),str(j+1),fill='black')
    sheet.save(out/contact,'WEBP',quality=82)
    checks[name]={'pages':len(doc),'expected':expected,'pages_qa':rec}
check('a0-boards.pdf',3,'a0_contact_sheet.webp')
check('a0-boards.en.pdf',3,'a0_en_contact_sheet.webp')
check('a3-booklet.pdf',8,'a3_contact_sheet.webp')
check('a3-booklet.en.pdf',8,'a3_en_contact_sheet.webp')
(out/'pdf_render_qa.json').write_text(json.dumps({'status':'PASS','checks':checks},indent=2)+'\n')
print('PDF render QA: PASS')
PY

printf '\n== exact official workspace ==\n'
rm -rf /tmp/upstream-v6-final
git clone -q --filter=blob:none --no-checkout https://github.com/open-city-ai/haidian.git /tmp/upstream-v6-final
git -C /tmp/upstream-v6-final sparse-checkout init --no-cone
cat > /tmp/v6-sparse-patterns.txt <<'EOF'
/scripts/
/skills/urban-design-ai-submission/
/requirements-review.txt
/brief/site-package/
/data/source_registry.json
/docs/data-workflow.md
/scenarios/
/tracks/
/tracks.json
EOF
git -C /tmp/upstream-v6-final sparse-checkout set --no-cone --stdin < /tmp/v6-sparse-patterns.txt
git -C /tmp/upstream-v6-final checkout -q "$LATEST"
cp -a "/tmp/formal-v6-final/$PKG" "/tmp/upstream-v6-final/$PKG"
git -C /tmp/upstream-v6-final switch -c validation/reviewer-multimodal-v6 >/dev/null
git -C /tmp/upstream-v6-final remote rename origin upstream
git -C /tmp/upstream-v6-final remote add origin https://github.com/zhoujiahao-source/agent_haidian.git
git -C /tmp/upstream-v6-final config remote.origin.partialclonefilter blob:none
git -C /tmp/upstream-v6-final update-ref refs/remotes/upstream/main "$LATEST"
python -m pip install --quiet -r /tmp/upstream-v6-final/requirements-review.txt

printf '\n== official bilingual render ==\n'
python /tmp/upstream-v6-final/scripts/render_proposal_html.py "/tmp/upstream-v6-final/$PKG"
SUB="/tmp/upstream-v6-final/$PKG" SUB="$SUB" python - <<'PY'
import os,json,hashlib
from pathlib import Path
root=Path(os.environ['SUB']); p=root/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8'))
for item in m.get('files',[]):
    if not isinstance(item,dict): continue
    rel=item.get('path')
    if rel and rel!='manifest.json' and (root/rel).is_file(): item['sha256']=hashlib.sha256((root/rel).read_bytes()).hexdigest()
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
PY

printf '\n== official persisted self-check ==\n'
(
 cd /tmp/upstream-v6-final
 python scripts/self_check_submission.py "$PKG" --pr-author zhoujiahao-source --mark-self-checked --json | tee /tmp/v6-self-final.json
)

printf '\n== official participant preflight ==\n'
(
 cd /tmp/upstream-v6-final
 python scripts/participant_preflight.py "$PKG" --pr-author zhoujiahao-source --json | tee /tmp/v6-preflight-final.json
)

printf '\n== copy persisted official outputs back + commit formal ==\n'
for f in report/proposal.html report/proposal.en.html self_check.json manifest.json; do cp "/tmp/upstream-v6-final/$PKG/$f" "/tmp/formal-v6-final/$PKG/$f"; done
git -C /tmp/formal-v6-final config user.name 'github-actions[bot]'
git -C /tmp/formal-v6-final config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git -C /tmp/formal-v6-final add "$PKG"
if ! git -C /tmp/formal-v6-final diff --cached --quiet; then
  git -C /tmp/formal-v6-final commit -q -m "Align reviewer narrative and multimodal package with upstream ${LATEST:0:8}"
  git -C /tmp/formal-v6-final push -q origin "HEAD:$FORMAL_BRANCH"
fi
FORMAL_SHA="$(git -C /tmp/formal-v6-final rev-parse HEAD)"
echo "formal_sha=$FORMAL_SHA"

printf '\n== safe evidence ==\n'
cp /tmp/v6-self-final.json "$ROOT/validation/self_check_exact.json"
UPSTREAM_SHA="$LATEST" FORMAL_SHA="$FORMAL_SHA" python - <<'PY'
import json,os
from pathlib import Path
root=Path('workstreams/reviewer_narrative_multimodal_v6')
raw=json.loads(Path('/tmp/v6-preflight-final.json').read_text())
safe={'schema_version':'1','evidence_type':'official_participant_preflight_safe_summary','ok':raw.get('ok'),'submission_dir':raw.get('submission_dir'),'pr_author':raw.get('pr_author'),'branch':raw.get('branch'),'origin_repo':'zhoujiahao-source/agent_haidian','upstream_repo':'open-city-ai/haidian','workspace':raw.get('workspace'),'base_ref':raw.get('base_ref'),'outside_scope_files':raw.get('outside_scope_files'),'package_file_count':raw.get('package_file_count'),'package_bytes':raw.get('package_bytes'),'self_check_ok':(raw.get('self_check') or {}).get('ok'),'blockers':raw.get('blockers'),'warnings':raw.get('warnings'),'sanitization_note':'Credential-bearing remote URLs are intentionally not persisted.'}
(root/'validation/preflight_exact.json').write_text(json.dumps(safe,ensure_ascii=False,indent=2)+'\n')
report={'schema_version':'1','status':'PASS','validated_upstream_sha':os.environ['UPSTREAM_SHA'],'validated_formal_sha':os.environ['FORMAL_SHA'],'checks':['reviewer_sequence_spec','three_close_range_renderings','ai_on_off_pair','participant_cover','a0_3_pages_rendered','a3_8_pages_rendered','offline_threejs_local_bundle','csp_connect_src_none','keyboard_and_reduced_motion','official_render_proposal_html','official_self_check_mark_self_checked','official_participant_preflight'],'truth_boundary':['canonical GeoJSON unchanged','KEY_AREA remains provisional','close-range renderings are conceptual / Derived','AI ON/OFF is reviewer evidence, not operational result','no statutory FAR/height/ownership/road-redline/approved-engineering claim']}
(root/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
PY

git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git add "$ROOT"
git commit -q -m 'Record exact-head reviewer multimodal v6 validation'
git push -q origin HEAD:integration/reviewer-narrative-multimodal-v6

echo "V6_FINAL_PASS upstream=$LATEST formal=$FORMAL_SHA"
