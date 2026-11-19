#!/usr/bin/env python3
"""Self-test for the Growing Assistant skill. Stdlib only."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
INIT = SKILL / "scripts" / "init_assistant.py"
LINT = SKILL / "scripts" / "lint_assistant.py"


def run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], text=True, capture_output=True)


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "assistant"
        p = run([str(INIT), "--root", str(root), "--name", "Selftest"])
        if p.returncode != 0:
            print(p.stdout)
            print(p.stderr)
            print("SELFTEST: FAIL (init)")
            return 1

        required = ["PROFILE.md", "RULES.md", "WORKFLOW.md", "memory", "docs", "workflows", "evals", "output", "skills", "private"]
        for name in required:
            if not (root / name).exists():
                print(f"SELFTEST: FAIL (missing {name})")
                return 1

        p = run([str(LINT), "--root", str(root)])
        if p.returncode != 0:
            print(p.stdout)
            print(p.stderr)
            print("SELFTEST: FAIL (lint bootstrap)")
            return 1

        # Simulate G3: one rule, one eval, one output.
        with (root / "RULES.md").open("a", encoding="utf-8") as f:
            f.write("\n## R-001 先结论，后依据\n- 触发：所有正式输出\n- 动作：先结论，后最多三条依据\n")
        (root / "evals" / "E-001.md").write_text("# E-001\n\n## Input\nx\n\n## Expected\ny\n", encoding="utf-8")
        out = root / "output" / "2026-11-19-selftest"
        out.mkdir(parents=True)
        (out / "report.md").write_text("# report\n", encoding="utf-8")

        p = run([str(LINT), "--root", str(root)])
        if p.returncode != 0:
            print(p.stdout)
            print(p.stderr)
            print("SELFTEST: FAIL (lint grow)")
            return 1

    print("SELFTEST: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
