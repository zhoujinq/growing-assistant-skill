#!/usr/bin/env python3
"""Lint a Growing Assistant workspace. Stdlib only."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REQUIRED_FILES = ["PROFILE.md", "RULES.md", "WORKFLOW.md"]
REQUIRED_DIRS = ["memory", "docs", "workflows", "evals", "output", "skills", "private"]
PROFILE_SECTIONS = ["## Who", "## Goals", "## Privacy"]
WORKFLOW_SECTIONS = ["## Inputs", "## Steps", "## Output", "## Acceptance", "## Stop"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="./assistant")
    args = ap.parse_args()
    root = Path(args.root).expanduser().resolve()

    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        print(f"FAIL: {root} does not exist")
        return 2

    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            errors.append(f"missing file: {name}")

    for name in REQUIRED_DIRS:
        if not (root / name).is_dir():
            errors.append(f"missing dir: {name}/")

    profile = (root / "PROFILE.md").read_text(encoding="utf-8") if (root / "PROFILE.md").exists() else ""
    for sec in PROFILE_SECTIONS:
        if sec not in profile:
            errors.append(f"PROFILE.md missing section: {sec}")

    rules = (root / "RULES.md").read_text(encoding="utf-8") if (root / "RULES.md").exists() else ""
    if "## R-" not in rules:
        warnings.append("RULES.md has no numbered rule yet (G0 can pass, G3 cannot)")

    workflow = (root / "WORKFLOW.md").read_text(encoding="utf-8") if (root / "WORKFLOW.md").exists() else ""
    for sec in WORKFLOW_SECTIONS:
        if sec not in workflow:
            errors.append(f"WORKFLOW.md missing section: {sec}")

    evals = list((root / "evals").glob("*.md")) if (root / "evals").is_dir() else []
    if not evals:
        warnings.append("no eval case yet (G3 not met)")
    outputs = [p for p in (root / "output").glob("*") if p.is_dir()] if (root / "output").is_dir() else []
    if not outputs:
        warnings.append("no task output yet (G2 not met)")

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}")

    if errors:
        print("LINT: FAIL")
        return 1
    print("LINT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
