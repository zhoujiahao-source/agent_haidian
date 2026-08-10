#!/usr/bin/env bash
set -euo pipefail

ROOT="$GITHUB_WORKSPACE/workstreams/ground_interface_realism_v5"
FORMAL_BRANCH="submission/zhoujiahao-source/jingzhang-urban-capability-exchange-v5-ground-interface"
PKG="submissions/zhoujiahao-source/jingzhang-legible-ai-belt"
AUDITED="fd1bf351cd02b6ee65a0f6b506e6d126745f08b0"

printf '\n== static ground-interface contract ==\n'
python -m py_compile "$ROOT/apply_ground_interface_v5.py"
python - <<'PY'
import json,re
from pathlib import Path
root=Path('workstreams/ground_interface_realism_v5')
spec_text=(root/'ground_interface_spec.json').read_text(encoding='utf-8')
spec=json.loads(spec_text)
assert spec['status']=='Derived / Not yet canonicalized'
assert len(spec['areas'])==3
assert spec['human_stop_contract']['name']=='Human Stop / Human Override'
for a in spec['areas']:
    assert a.get('human_stop_role')
    assert len(a['edge_types'])==4
    assert len(a['detail_components'])>=10
    assert len(a['human_scenes'])>=5
html=(root/'threejs/keyarea_ground_interface_twin.html').read_text(encoding='utf-8')
required=['WebGPURenderer','OrbitControls','mergeGeometries','ExtrudeGeometry','InstancedMesh','overpass-api','osmLandscape','canonicalBuildings','pointInPoly','Ground Interface','Not yet canonicalized','ODbL','Staffed safety / governance desk','Test safety buffer','Ordinary + accessible route','Rider / loading pocket','__FORMAL_REF__']
for token in required: assert token in html,token
m=re.search(r'<script type="module">(.*?)</script>',html,re.S); assert m
Path('/tmp/keyarea-ground-v5.mjs').write_text(m.group(1),encoding='utf-8')
print('static spatial contract: PASS')
PY
node --check /tmp/keyarea-ground-v5.mjs

printf '\n== exact upstream guard ==\n'
LATEST="$(git ls-remote https://github.com/open-city-ai/haidian.git refs/heads/main | cut -f1)"
echo "audited=$AUDITED"
echo "latest=$LATEST"
if [[ "$LATEST" != "$AUDITED" ]]; then
  rm -rf /tmp/upstream-guard && git init -q /tmp/upstream-guard
  git -C /tmp/upstream-guard remote add origin https://github.com/open-city-ai/haidian.git
  git -C /tmp/upstream-guard -c protocol.version=2 fetch -q --no-tags --filter=blob:none origin "$AUDITED" "$LATEST"
  git -C /tmp/upstream-guard diff --name-only "$AUDITED" "$LATEST" > /tmp/upstream-changed.txt
  python - <<'PY'
from pathlib import Path
fs=[x.strip() for x in Path('/tmp/upstream-changed.txt').read_text().splitlines() if x.strip()]
non=[f for f in fs if not (f.startswith('submissions/') or f=='submissions-data.js')]
print('changed paths since audited baseline:',len(fs))
if non:
    print('Rule/tool/source changes require re-audit:')
    print('\n'.join(non))
    raise SystemExit(1)
print('Only peer submissions/gallery changed since audited baseline.')
PY
fi

printf '\n== materialize formal fork branch ==\n'
rm -rf /tmp/formal-v5 /tmp/upstream-v5
git clone -q --filter=blob:none --no-checkout "https://x-access-token:${GITHUB_TOKEN}@github.com/zhoujiahao-source/agent_haidian.git" /tmp/formal-v5
git -C /tmp/formal-v5 sparse-checkout init --cone
git -C /tmp/formal-v5 sparse-checkout set "$PKG"
git -C /tmp/formal-v5 checkout -q "$FORMAL_BRANCH"
SUBMISSION_ROOT="/tmp/formal-v5/$PKG" python "$ROOT/apply_ground_interface_v5.py"

printf '\n== materialize exact official workspace ==\n'
git clone -q --filter=blob:none --no-checkout https://github.com/open-city-ai/haidian.git /tmp/upstream-v5
git -C /tmp/upstream-v5 sparse-checkout init --cone
git -C /tmp/upstream-v5 sparse-checkout set scripts skills/urban-design-ai-submission requirements-review.txt brief/site-package data/source_registry.json docs/data-workflow.md scenarios tracks
git -C /tmp/upstream-v5 checkout -q "$LATEST"
git -C /tmp/upstream-v5 switch -q -c validation/ground-interface-v5
python -m pip install -q -r /tmp/upstream-v5/requirements-review.txt
mkdir -p "/tmp/upstream-v5/submissions/zhoujiahao-source"
cp -a "/tmp/formal-v5/$PKG" "/tmp/upstream-v5/submissions/zhoujiahao-source/jingzhang-legible-ai-belt"
git -C /tmp/upstream-v5 remote rename origin upstream
git -C /tmp/upstream-v5 remote add origin "https://x-access-token:${GITHUB_TOKEN}@github.com/zhoujiahao-source/agent_haidian.git"
git -C /tmp/upstream-v5 config remote.origin.partialclonefilter blob:none
git -C /tmp/upstream-v5 update-ref refs/remotes/upstream/main "$LATEST"

printf '\n== render and hash refresh ==\n'
python /tmp/upstream-v5/scripts/render_proposal_html.py "/tmp/upstream-v5/$PKG"
SUB="/tmp/upstream-v5/$PKG" python - <<'PY'
import hashlib,json,os
from pathlib import Path
root=Path(os.environ['SUB']); p=root/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8'))
for item in m.get('files',[]):
    if not isinstance(item,dict): continue
    rel=item.get('path')
    if not rel or rel=='manifest.json': continue
    f=root/rel
    if f.is_file(): item['sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
if isinstance(m.get('validation_claim'),dict): m['validation_claim']['self_checked']=True
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
PY

printf '\n== official self-check ==\n'
(
  cd /tmp/upstream-v5
  python scripts/self_check_submission.py "$PKG" --pr-author zhoujiahao-source --json | tee /tmp/ground-self.json
)
printf '\n== official participant preflight ==\n'
(
  cd /tmp/upstream-v5
  python scripts/participant_preflight.py "$PKG" --pr-author zhoujiahao-source --json | tee /tmp/ground-preflight.json
)

printf '\n== commit formal v5 ==\n'
cp "/tmp/upstream-v5/$PKG/report/proposal.html" "/tmp/formal-v5/$PKG/report/proposal.html"
cp "/tmp/upstream-v5/$PKG/report/proposal.en.html" "/tmp/formal-v5/$PKG/report/proposal.en.html"
cp "/tmp/upstream-v5/$PKG/manifest.json" "/tmp/formal-v5/$PKG/manifest.json"
git -C /tmp/formal-v5 config user.name "github-actions[bot]"
git -C /tmp/formal-v5 config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git -C /tmp/formal-v5 add "$PKG"
if ! git -C /tmp/formal-v5 diff --cached --quiet; then
  git -C /tmp/formal-v5 commit -q -m "Deepen ground interface against upstream ${LATEST:0:8}"
  git -C /tmp/formal-v5 push -q origin "HEAD:$FORMAL_BRANCH"
fi
FORMAL_SHA="$(git -C /tmp/formal-v5 rev-parse HEAD)"
echo "formal_sha=$FORMAL_SHA"

printf '\n== freeze Three.js plan source and save raw validation evidence ==\n'
mkdir -p "$ROOT/validation"
cp /tmp/ground-self.json "$ROOT/validation/self_check_exact.json"
cp /tmp/ground-preflight.json "$ROOT/validation/preflight_exact.json"
UPSTREAM_SHA="$LATEST" FORMAL_SHA="$FORMAL_SHA" python - <<'PY'
import json,os,re
from pathlib import Path
root=Path('workstreams/ground_interface_realism_v5')
twin=root/'threejs/keyarea_ground_interface_twin.html'
t=twin.read_text(encoding='utf-8')
t=re.sub(r"DEFAULT_REF='[^']+'",f"DEFAULT_REF='{os.environ['FORMAL_SHA']}'",t,count=1)
twin.write_text(t,encoding='utf-8')
report={
 'schema_version':'1','status':'PASS','validated_upstream_sha':os.environ['UPSTREAM_SHA'],'validated_formal_sha':os.environ['FORMAL_SHA'],
 'checks':['ground_interface_spec','threejs_node_syntax','bilingual_proposal_patch','official_render_proposal_html','official_self_check_submission','official_participant_preflight'],
 'spatial_deepening':['ground-floor edge sequence','ordinary accessible route','blue-green comfort','human-help baseline','Human Stop / Human Override contract','test/service separation','AI-off review floor','OSM water/green context','per-building OSM height evidence'],
 'truth_boundary':['KEY_AREA remains provisional','ground-interface placements are Derived / Not yet canonicalized','section proportions are diagrammatic only','OSM remains candidate existing context','no statutory FAR/height/ownership/road-redline/approved-engineering claim']
}
(root/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert '__FORMAL_REF__' not in t
m=re.search(r'<script type="module">(.*?)</script>',t,re.S); assert m
Path('/tmp/keyarea-ground-v5-final.mjs').write_text(m.group(1),encoding='utf-8')
PY
node --check /tmp/keyarea-ground-v5-final.mjs

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add workstreams/ground_interface_realism_v5
git commit -q -m "Record exact-head ground-interface v5 validation"
git push -q origin HEAD:integration/ground-interface-realism-v5

echo "V5_EXACT_VALIDATION_PASS upstream=$LATEST formal=$FORMAL_SHA"
