#!/usr/bin/env python3
"""
Platform Genesis Universe Analytics

Module:
    Markdown Report Generator

Description:
    Generate Markdown reports from repository metrics.

Author:
    Junwu
License:
    MIT
"""
from __future__ import annotations
from pathlib import Path
from utils import (
    LOGGER,
    LATEST_DIR,
    REPORT_DIR,
    initialize_directories,
    load_json,
    write_markdown,
)


def load_repositories() -> list[dict]:
    repositories = []
    for file in sorted(LATEST_DIR.glob("*.json")):
        repositories.append(load_json(file))
    return repositories


def generate_dashboard(data: list[dict]) -> str:
    lines = []
    lines.append("# Repository Dashboard")
    lines.append("")
    lines.append("| Repository | ⭐ Stars | 🍴 Forks | 👀 Views | 📥 Clones |")
    lines.append("|:--|--:|--:|--:|--:|")

    total_views = 0
    total_clones = 0
    total_stars = 0

    for repo in data:
        metrics = repo["repository_metrics"]
        traffic = repo.get("traffic", {})
        views = traffic.get("views", {})
        clones = traffic.get("clones", {})
        stars = metrics["stars"]
        forks = metrics["forks"]
        view_count = views.get("count", 0)
        clone_count = clones.get("count", 0)

        total_stars += stars
        total_views += view_count
        total_clones += clone_count

        lines.append(
            f"| {repo['repository']} | "
            f"{stars} | "
            f"{forks} | "
            f"{view_count} | "
            f"{clone_count} |"
        )

    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Repository : {len(data)}")
    lines.append(f"- Stars : {total_stars}")
    lines.append(f"- Views (14 days) : {total_views}")
    lines.append(f"- Clones (14 days) : {total_clones}")
    return "\n".join(lines)


def main():
    initialize_directories()
    LOGGER.info("Generate Dashboard")
    repositories = load_repositories()
    markdown = generate_dashboard(repositories)
    write_markdown(REPORT_DIR / "dashboard.md", markdown)

    LOGGER.info("Dashboard Updated")


if __name__ == "__main__":
    main()