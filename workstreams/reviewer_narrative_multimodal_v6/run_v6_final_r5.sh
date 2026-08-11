#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
from pathlib import Path
# Descriptive alt text.
p=Path('workstreams/reviewer_narrative_multimodal_v6/build_v6.py'); t=p.read_text(encoding='utf-8')
t=t.replace('![众智园近景](assets/figures/close-range-zhongzhiyuan.png)','![众智园验证园区首层、普通旁路与有界测试近景示意](assets/figures/close-range-zhongzhiyuan.png)')
t=t.replace('![大钟寺近景](assets/figures/close-range-dazhongsi.png)','![大钟寺市场服务街、骑手装卸口袋与夜间公共空间近景示意](assets/figures/close-range-dazhongsi.png)')
p.write_text(t,encoding='utf-8')
# Strict 0.2 model disclosure.
p=Path('workstreams/reviewer_narrative_multimodal_v6/run_v6_final_r2.sh'); t=p.read_text(encoding='utf-8')
t=t.replace("m.setdefault('agent',{})['model_family']='gpt'","m.setdefault('agent',{})['model_family']='gpt'\\nm['agent']['model_detail']='GPT-5.6 Sol'",1)
p.write_text(t,encoding='utf-8')
# Current track registry is root tracks.json.
p=Path('workstreams/reviewer_narrative_multimodal_v6/run_v6_final_r3.sh'); t=p.read_text(encoding='utf-8')
t=t.replace('/tracks/\\nEOF','/tracks/\\n/tracks.json\\nEOF',1)
p.write_text(t,encoding='utf-8')
# Run formal Three.js shell QA first, then integrate it into legal visual/index*.html and remove staging HTML.
p=Path('workstreams/reviewer_narrative_multimodal_v6/run_v6_final.sh'); t=p.read_text(encoding='utf-8')
marker="printf '\\n== refresh manifest hashes ==\\n'"
call="python workstreams/reviewer_narrative_multimodal_v6/integrate_threejs_into_visual.py \"/tmp/formal-v6-final/$PKG\"\n\n"+marker
if marker not in t: raise SystemExit('refresh marker missing')
t=t.replace(marker,call,1)
p.write_text(t,encoding='utf-8')
print('v6 current-validator patches applied')
PY
bash workstreams/reviewer_narrative_multimodal_v6/run_v6_final_r3.sh
