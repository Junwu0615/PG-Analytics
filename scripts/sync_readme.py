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
from __future__ import annotations
from pathlib import Path
from utils import (
    LOGGER,
)

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
    LOGGER.warning("Starting Sync README ...")

    readme = README.read_text(encoding="utf-8")

    dashboard = load_section(REPORT_DIR / "dashboard.md")
    readme = inject_section(readme, "dashboard", dashboard)

    traffic = load_section(REPORT_DIR / "traffic.md")
    readme = inject_section(readme, "traffic", traffic)

    growth = load_section(REPORT_DIR / "growth.md")
    readme = inject_section(readme, "growth", growth)

    README.write_text(readme, encoding="utf-8")

    LOGGER.warning("Sync README Done.")


if __name__ == "__main__":
    main()