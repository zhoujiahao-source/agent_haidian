#!/usr/bin/env python3
"""Dependency-free structural validator for the AI Governance & Metrics workstream.

This validates the workstream contract only. It does NOT claim that the canonical
competition submission passes participant_preflight, and it does not validate live
operational outcomes.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

REQUIRED_FILES = [
    "urban_learning_protocol.md",
    "problem_diagnosis.md",
    "risk_tiers.md",
    "authorization_matrix.csv",
    "experiment_protocol.md",
    "public_value_framework.md",
    "urban_adaptation_rate.md",
    "custom_metrics_catalog.md",
    "anti_gaming.md",
    "audit_and_dashboard.md",
    "capability_transfer_rules.md",
    "metric_proposals.json",
    "figure_briefs.md",
    "handoff.md",
    "integration_crosswalk.md",
    "dashboard_data_contract.json",
    "schemas/eligible_issue.schema.json",
    "schemas/experiment_card.schema.json",
    "schemas/capability_record.schema.json",
    "schemas/city_version_release.schema.json",
    "audit/rule_audit.md",
    "audit/checkpoints.md",
]

REQUIRED_METRIC_FIELDS = {
    "status", "value", "unit", "source_files", "formula", "confidence", "assumptions"
}
ALLOWED_STATUS = {"known", "unknown", "not_applicable"}
ALLOWED_UNITS = {"sqm", "m", "ratio", "count", "index", "none"}
ALLOWED_CONFIDENCE = {"high", "medium", "low", "unknown"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, f"invalid JSON: {path}: {exc}")
        return None


def validate_metrics(root: Path, errors: list[str]) -> int:
    data = load_json(root / "metric_proposals.json", errors)
    if not isinstance(data, dict):
        return 0
    metrics = data.get("metrics")
    if not isinstance(metrics, dict):
        fail(errors, "metric_proposals.json: metrics must be an object")
        return 0
    if len(metrics) < 10:
        fail(errors, f"metric_proposals.json: expected at least 10 custom metrics, found {len(metrics)}")
    for metric_id, metric in metrics.items():
        if not isinstance(metric, dict):
            fail(errors, f"metric {metric_id}: record must be an object")
            continue
        missing = REQUIRED_METRIC_FIELDS - set(metric)
        if missing:
            fail(errors, f"metric {metric_id}: missing fields {sorted(missing)}")
        if metric.get("status") not in ALLOWED_STATUS:
            fail(errors, f"metric {metric_id}: invalid status {metric.get('status')!r}")
        if metric.get("unit") not in ALLOWED_UNITS:
            fail(errors, f"metric {metric_id}: invalid unit {metric.get('unit')!r}")
        if metric.get("confidence") not in ALLOWED_CONFIDENCE:
            fail(errors, f"metric {metric_id}: invalid confidence {metric.get('confidence')!r}")
        if metric.get("status") == "unknown":
            if metric.get("value") is not None:
                fail(errors, f"metric {metric_id}: unknown metric must use value=null")
            if not isinstance(metric.get("reason"), str) or not metric.get("reason", "").strip():
                fail(errors, f"metric {metric_id}: unknown metric requires non-empty reason")
    return len(metrics)


def validate_authorization_matrix(root: Path, errors: list[str]) -> None:
    path = root / "authorization_matrix.csv"
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            headers = set(reader.fieldnames or [])
    except Exception as exc:
        fail(errors, f"authorization_matrix.csv unreadable: {exc}")
        return
    expected_tokens = {"risk", "approval", "rollback"}
    normalized = " ".join(sorted(h.lower() for h in headers))
    for token in expected_tokens:
        if token not in normalized:
            fail(errors, f"authorization_matrix.csv: no header containing {token!r}")
    if len(rows) < 4:
        fail(errors, f"authorization_matrix.csv: expected at least 4 risk rows, found {len(rows)}")


def validate_contracts(root: Path, errors: list[str]) -> None:
    for rel in [
        "schemas/eligible_issue.schema.json",
        "schemas/experiment_card.schema.json",
        "schemas/capability_record.schema.json",
        "schemas/city_version_release.schema.json",
        "dashboard_data_contract.json",
    ]:
        obj = load_json(root / rel, errors)
        if obj is None:
            continue
        if not isinstance(obj, dict):
            fail(errors, f"{rel}: top level must be an object")
    dashboard = load_json(root / "dashboard_data_contract.json", errors)
    if isinstance(dashboard, dict):
        prohibited = set(dashboard.get("public_layer", {}).get("prohibited_fields", []))
        for required in {"raw_personal_data", "sensitive_personal_data"}:
            if required not in prohibited:
                fail(errors, f"dashboard_data_contract.json: public prohibited_fields missing {required}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            fail(errors, f"missing required workstream file: {rel}")

    metric_count = validate_metrics(root, errors)
    validate_authorization_matrix(root, errors)
    validate_contracts(root, errors)

    if errors:
        print("AI governance workstream validation: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    print("AI governance workstream validation: PASS")
    print(f"- custom metric candidates: {metric_count}")
    print("- unknown metrics are required to use value=null + reason")
    print("- governance JSON contracts parse structurally")
    print("- this is NOT canonical submission participant_preflight")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
