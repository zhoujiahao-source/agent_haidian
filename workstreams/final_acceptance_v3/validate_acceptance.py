#!/usr/bin/env python3
import json, os, sys, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
matrix = ROOT / "acceptance_matrix.json"
if not matrix.exists():
    subprocess.run([sys.executable, str(ROOT / "build_acceptance_matrix.py")], check=True)

data = json.loads(matrix.read_text(encoding="utf-8"))
items = data["items"]

errors = []
if len(items) != 100:
    errors.append(f"expected 100 items, got {len(items)}")
ids = [x["id"] for x in items]
if len(ids) != len(set(ids)):
    errors.append("duplicate acceptance ids")
for x in items:
    if x["priority"] not in {"P0","P1","P2"}:
        errors.append(f"{x['id']}: bad priority {x['priority']}")
    if x["status"] not in {"COMPLETE","IN_PROGRESS","BLOCKED_OFFICIAL_DATA","HUMAN_REQUIRED"}:
        errors.append(f"{x['id']}: bad status {x['status']}")
    for k in ("category","requirement","acceptance_test","owner"):
        if not str(x.get(k,"")).strip():
            errors.append(f"{x['id']}: missing {k}")
    if not x.get("evidence_refs"):
        errors.append(f"{x['id']}: no evidence_refs")

p0_open=[x["id"] for x in items if x["priority"]=="P0" and x["status"]!="COMPLETE"]
agent_open=[x["id"] for x in items if x["owner"]=="AGENT" and x["status"]=="IN_PROGRESS"]

print(json.dumps({
    "total":len(items),
    "complete":sum(x["status"]=="COMPLETE" for x in items),
    "in_progress":sum(x["status"]=="IN_PROGRESS" for x in items),
    "blocked_official_data":sum(x["status"]=="BLOCKED_OFFICIAL_DATA" for x in items),
    "human_required":sum(x["status"]=="HUMAN_REQUIRED" for x in items),
    "p0_open":p0_open,
    "agent_open":agent_open
}, ensure_ascii=False, indent=2))

if errors:
    print("\nERRORS:", file=sys.stderr)
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
if p0_open:
    print(f"\nP0 acceptance is not closed: {p0_open}", file=sys.stderr)
    raise SystemExit(2)
if agent_open and os.getenv("ALLOW_AGENT_OPEN") != "1":
    print(f"\nAgent-executable acceptance remains open: {agent_open}", file=sys.stderr)
    raise SystemExit(3)
