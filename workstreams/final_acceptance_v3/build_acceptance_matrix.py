#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORDER = [
    "urban_design.json",
    "learning_mechanism.json",
    "ai_governance.json",
    "evidence_architecture.json",
    "competition_delivery.json",
]
items = []
for name in ORDER:
    data = json.loads((ROOT / "criteria" / name).read_text(encoding="utf-8"))
    items.extend(data["items"])

status_order = ["COMPLETE", "IN_PROGRESS", "BLOCKED_OFFICIAL_DATA", "HUMAN_REQUIRED"]
out = {
    "schema_version": "1",
    "generated_at": "2026-08-10",
    "upstream_sha": "6405afe0ce1f23e1b7056e30c0fe12fe3c59ecab",
    "canonical_base_sha": "815f21207e72ffdcd3caf2bc2943c853b032cfda",
    "formal_branch": "submission/zhoujiahao-source/jingzhang-urban-capability-exchange-v3-final",
    "target_maturity": "L3 high-fidelity integrated prototype / L4-ready",
    "total_items": len(items),
    "priority_counts": {p: sum(x["priority"] == p for x in items) for p in ["P0","P1","P2"]},
    "status_counts": {s: sum(x["status"] == s for x in items) for s in status_order},
    "items": items,
}
(ROOT / "acceptance_matrix.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({
    "total": out["total_items"],
    "priority_counts": out["priority_counts"],
    "status_counts": out["status_counts"],
}, ensure_ascii=False, indent=2))
