#!/usr/bin/env python3
"""Stdlib-only validator for the Codex skill kit."""
from __future__ import annotations
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    "hackathon-intake", "readme-analysis", "dataset-audit", "problem-deep-dive",
    "solution-design", "mvp-build", "verification", "demo-submission", "debug-recovery", "architecture-map",
]


def main() -> int:
    errors = []
    skill_root = ROOT / ".agents" / "skills"
    skills = sorted(p for p in skill_root.iterdir() if p.is_dir()) if skill_root.exists() else []
    names = []
    for folder in skills:
        skill_file = folder / "SKILL.md"
        prompt_file = folder / "PROMPT_EXAMPLE.md"
        if not skill_file.is_file():
            errors.append(f"{folder.name}: SKILL.md missing")
            continue
        text = skill_file.read_text(encoding="utf-8")
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
        if not match:
            errors.append(f"{folder.name}: frontmatter missing")
            continue
        meta = dict(re.findall(r"^([A-Za-z_]+):\s*(.+?)\s*$", match.group(1), flags=re.M))
        name = meta.get("name", "")
        desc = meta.get("description", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{folder.name}: invalid name '{name}'")
        if len(desc) < 20:
            errors.append(f"{folder.name}: description too short")
        if not prompt_file.is_file():
            errors.append(f"{folder.name}: prompt example missing")
        elif f"${name}" not in prompt_file.read_text(encoding="utf-8"):
            errors.append(f"{folder.name}: prompt does not invoke ${name}")
        names.append(name)
    if sorted(names) != sorted(EXPECTED):
        errors.append(f"Skill names differ. Found: {names}")
    for expected in ("README.md", "AGENTS.md", "QUICKSTART.md", "PROMPTS.md", "ARCHITECTURE.md"):
        if not (ROOT / expected).is_file():
            errors.append(f"Missing {expected}")
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"PASS: {len(skills)} skills validated; metadata and example prompts present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
