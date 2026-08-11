#!/usr/bin/env bash
set -euo pipefail
BASE="workstreams/reviewer_narrative_multimodal_v6/run_v6_final.sh"
python - <<'PY'
from pathlib import Path
p=Path('workstreams/reviewer_narrative_multimodal_v6/run_v6_final.sh')
t=p.read_text(encoding='utf-8')
old='''git clone -q --filter=blob:none --sparse https://github.com/open-city-ai/haidian.git /tmp/upstream-v6-final
git -C /tmp/upstream-v6-final sparse-checkout set scripts skills/urban-design-ai-submission requirements-review.txt brief/site-package data/source_registry.json docs/data-workflow.md scenarios tracks
git -C /tmp/upstream-v6-final checkout -q "$LATEST"'''
new='''git clone -q --filter=blob:none --no-checkout https://github.com/open-city-ai/haidian.git /tmp/upstream-v6-final
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
git -C /tmp/upstream-v6-final checkout -q "$LATEST"'''
if old not in t: raise SystemExit('old sparse workspace block not found')
p.write_text(t.replace(old,new,1),encoding='utf-8')
print('patched exact official sparse workspace to non-cone patterns + root tracks.json')
PY
bash workstreams/reviewer_narrative_multimodal_v6/run_v6_final_r2.sh
