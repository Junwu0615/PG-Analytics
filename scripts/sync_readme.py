#!/usr/bin/env python3
"""
Platform Genesis Universe Analytics

Module:
    Markdown Sync README

Description:
    Sync README.

Author:
    Junwu
License:
    MIT
"""
from pathlib import Path

REPORT_DIR = Path("reports")
README = Path("README.md")


def load_section(file: Path) -> str:
    if not file.exists():
        return ""
    return file.read_text(encoding="utf-8")


def inject_section(readme: str, marker: str, content: str) -> str:
    start = f"<!-- {marker}:start -->"
    end = f"<!-- {marker}:end -->"

    before = readme.split(start)[0]
    after = readme.split(end)[1]

    return before + start + "\n" + content + "\n" + end + after


def main():
    readme = README.read_text(encoding="utf-8")
    dashboard = load_section(REPORT_DIR / "dashboard.md")
    traffic = load_section(REPORT_DIR / "traffic.md")
    growth = load_section(REPORT_DIR / "growth.md")
    readme = inject_section(readme, "dashboard", dashboard)
    readme = inject_section(readme, "traffic", traffic)
    readme = inject_section(readme, "growth", growth)
    README.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()