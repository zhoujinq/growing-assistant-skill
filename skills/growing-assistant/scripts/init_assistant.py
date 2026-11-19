#!/usr/bin/env python3
"""Scaffold a Growing Assistant workspace. Stdlib only."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="./assistant")
    ap.add_argument("--name", default="My Assistant")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).expanduser().resolve()
    if root.exists() and any(root.iterdir()) and not args.force:
        print(f"REFUSE: {root} is not empty. Use --force to overwrite.")
        return 2

    root.mkdir(parents=True, exist_ok=True)
    for d in ["memory", "docs", "workflows", "evals", "output", "skills", "private"]:
        (root / d).mkdir(exist_ok=True)

    for name in ["PROFILE.md", "RULES.md", "WORKFLOW.md", "EVAL.md"]:
        src = TEMPLATES / name
        if src.exists():
            shutil.copyfile(src, root / name)
        else:
            write(root / name, f"# {name[:-3]}\n")

    write(root / "memory" / "open-loops.md", "# Open loops\n\n- \n")
    write(root / "docs" / "README.md", "# Docs\n\nPut read-only source material here. Cite by path#heading or path:line.\n")
    write(root / "skills" / "README.md", "# Skills\n\nDistilled standalone skills live here, one folder per skill.\n")
    write(root / "output" / ".gitkeep", "")
    write(root / "private" / ".gitkeep", "")
    write(
        root / ".gitignore",
        "private/\noutput/*\n!output/.gitkeep\n__pycache__/\n*.pyc\n.DS_Store\n",
    )

    profile = root / "PROFILE.md"
    text = profile.read_text(encoding="utf-8")
    profile.write_text(f"# PROFILE — {args.name}\n\n" + text.split("\n", 1)[1], encoding="utf-8")

    print(f"OK: {root}")
    print("Next:")
    print("  1) fill PROFILE.md (5-8 questions)")
    print("  2) write WORKFLOW.md")
    print(f"  3) python scripts/lint_assistant.py --root {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
