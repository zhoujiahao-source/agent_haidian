#!/usr/bin/env bash
set -euo pipefail
BASE="workstreams/reviewer_narrative_multimodal_v6/run_v6_final.sh"
python - <<'PY'
from pathlib import Path
p=Path('workstreams/reviewer_narrative_multimodal_v6/run_v6_final.sh')
t=p.read_text(encoding='utf-8')
t=t.replace('AUDITED="9f67bf2771b96cbec9ce47fff32d43f494b22695"','AUDITED="d07abb5dda76d22245a3f5d97b3f5dffcb09ef0a"')
needle='SUBMISSION_ROOT="/tmp/formal-v6-final/$PKG" WORKSTREAM_ROOT="$ROOT" python "$ROOT/build_v6.py"'
upgrade=needle+'''\nSUB="/tmp/formal-v6-final/$PKG" SUB="$SUB" python - <<'PYS'\nimport os,json\nfrom datetime import datetime,timezone\nfrom pathlib import Path\nroot=Path(os.environ['SUB']); p=root/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8'))\nm['schema_version']='0.2.0'\nm['generated_at']=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')\nm.setdefault('agent',{})['model_family']='gpt'\nallowed={'manifest','agent_card','metrics','assumptions','sources','self_check','compliance_matrix','standard_matrix','design_depth_matrix','geometry','drawing','narrative','copyright_statement','visualization','proposal_figure','rendered_proposal_html','video','audio','media_poster','caption_track','transcript','changelog','asset','figure','evidence_data','verification_script','other'}\nfor item in m.get('files',[]):\n    assert isinstance(item.get('required'),bool), item.get('path')\n    assert item.get('role') in allowed,(item.get('path'),item.get('role'))\n    if item.get('role')=='other': assert item.get('role_detail')\ncl=m.setdefault('validation_claim',{})\nfor k in list(cl):\n    if k not in {'self_checked','known_blockers','data_confidence','readiness_contract','extensions'}: cl.pop(k)\ncl['self_checked']=False\ncl.pop('readiness_contract',None)\np.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\\n',encoding='utf-8')\nprint('manifest upgraded to strict 0.2.0')\nPYS'''
if needle not in t: raise SystemExit('build insertion point missing')
t=t.replace(needle,upgrade,1)
needle2='git -C /tmp/upstream-v6-final checkout -q "$LATEST"\ncp -a "/tmp/formal-v6-final/$PKG" "/tmp/upstream-v6-final/$PKG"'
repl2='git -C /tmp/upstream-v6-final checkout -q "$LATEST"\nmkdir -p "/tmp/upstream-v6-final/submissions/zhoujiahao-source"\ncp -a "/tmp/formal-v6-final/$PKG" "/tmp/upstream-v6-final/$PKG"'
if needle2 not in t: raise SystemExit('workspace insertion point missing')
t=t.replace(needle2,repl2,1)
needle3="printf '\\n== official persisted self-check ==\\n'"
strict='''printf '\\n== strict manifest 0.2 schema audit ==\\n'\n(\n cd /tmp/upstream-v6-final\n python scripts/validate_manifest_schema.py --manifest "$PKG/manifest.json" --strict --json | tee /tmp/v6-manifest-schema.json\n)\n\n'''+needle3
if needle3 not in t: raise SystemExit('strict audit insertion point missing')
t=t.replace(needle3,strict,1)
needle4="cp /tmp/v6-self-final.json \"$ROOT/validation/self_check_exact.json\""
repl4="cp /tmp/v6-self-final.json \"$ROOT/validation/self_check_exact.json\"\ncp /tmp/v6-manifest-schema.json \"$ROOT/validation/manifest_schema_exact.json\""
t=t.replace(needle4,repl4,1)
t=t.replace("'checks':['reviewer_sequence_spec'","'checks':['strict_manifest_0_2_schema','reviewer_sequence_spec'",1)
Path('/tmp/run-v6-final-r2-generated.sh').write_text(t,encoding='utf-8')
PY
bash /tmp/run-v6-final-r2-generated.sh
