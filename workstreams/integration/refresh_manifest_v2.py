#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("submission_dir")
    parser.add_argument("--self-checked", choices=["true", "false"], required=True)
    args = parser.parse_args()
    root = Path(args.submission_dir).resolve()
    path = root / "manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("package_state") != "ready_for_review":
        raise SystemExit("manifest is not ready_for_review")
    for item in manifest.get("files", []):
        if not isinstance(item, dict):
            continue
        rel = item.get("path")
        target = root / rel if rel else None
        if rel and rel != "manifest.json" and target.is_file():
            item["sha256"] = digest(target)
    manifest.setdefault("validation_claim", {})["self_checked"] = args.self_checked == "true"
    manifest["generated_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"manifest refreshed; self_checked={args.self_checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
