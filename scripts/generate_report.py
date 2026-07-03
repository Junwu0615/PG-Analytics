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
import csv
from pathlib import Path
from utils import (
    LOGGER,
    LATEST_DIR,
    REPORT_DIR,
    HISTORY_DIR,
    initialize_directories,
    load_json,
    write_markdown,
)


def load_repositories() -> list[dict]:
    repositories = []

    for file in sorted(LATEST_DIR.glob("*.json")):
        if file.stat().st_size == 0:
            LOGGER.warning("Skip empty file: %s", file.name)
            continue

        try:
            data = load_json(file)
        except Exception as e:
            LOGGER.warning("Skip corrupted JSON: %s (%s)", file.name, str(e))
            continue

        if not isinstance(data, dict):
            LOGGER.warning("Skip invalid JSON: %s", file.name)
            continue

        if "repository" not in data:
            LOGGER.warning("Skip malformed JSON: %s", file.name)
            continue

        repositories.append(data)

    return repositories


def generate_dashboard(
    repositories: list[dict],
) -> str:
    if not repositories:
        return "> Repository Dashboard: _No repositories available_"

    lines = []
    lines.append(" | Repository | ⭐ Stars | 🍴 Forks | 👀 Views | 📥 Clones |")
    lines.append(" |:--|--:|--:|--:|--:|")

    total_views = 0
    total_clones = 0
    total_stars = 0

    for repo in repositories:
        repo_name = repo.get("repository", "unknown")

        metrics = repo.get("repository_metrics", {}) or {}
        traffic = repo.get("traffic", {}) or {}
        views = traffic.get("views", {}) or {}
        clones = traffic.get("clones", {}) or {}

        stars = metrics.get("stars", 0)
        forks = metrics.get("forks", 0)
        view_count = views.get("count", 0)
        clone_count = clones.get("count", 0)

        total_stars += stars
        total_views += view_count
        total_clones += clone_count

        lines.append(f" | {repo_name} | {stars} | {forks} | {view_count} | {clone_count} |")

    lines.append("<br>")
    lines.append("### *Summary*")
    lines.append(f"- *Repository : {len(repositories)}*")
    lines.append(f"- *Stars : {total_stars}*")
    lines.append(f"- *Views (14 days) : {total_views}*")
    lines.append(f"- *Clones (14 days) : {total_clones}*")
    return "\n".join(lines)


def generate_traffic(
    repositories: list[dict],
) -> str:
    """
    Generate repository traffic report.
    """
    if not repositories:
        return "> Traffic Analytics : _No repositories available._"

    lines = []
    lines.append("| Repository | 👀 Views | 👤 Unique | 📥 Clones | 👤 Unique |")
    lines.append("|:--|--:|--:|--:|--:|")

    total_views = 0
    total_unique_views = 0
    total_clones = 0
    total_unique_clones = 0

    for repo in repositories:

        traffic = repo.get("traffic", {}) or {}

        views = traffic.get("views", {}) or {}
        clones = traffic.get("clones", {}) or {}

        view_count = int(views.get("count", 0))
        unique_views = int(views.get("uniques", 0))

        clone_count = int(clones.get("count", 0))
        unique_clones = int(clones.get("uniques", 0))

        total_views += view_count
        total_unique_views += unique_views

        total_clones += clone_count
        total_unique_clones += unique_clones

        lines.append(
            f"| {repo['repository']} | "
            f"{view_count} | "
            f"{unique_views} | "
            f"{clone_count} | "
            f"{unique_clones} |"
        )

    lines.append("")
    lines.append("### *Summary*")
    lines.append("")
    lines.append(f"- *Views (14 Days) : {total_views}*")
    lines.append(f"- *Unique Visitors : {total_unique_views}*")
    lines.append(f"- *Clones (14 Days) : {total_clones}*")
    lines.append(f"- *Unique Cloners : {total_unique_clones}*")

    return "\n".join(lines)


def generate_growth(
    repositories: list[dict],
) -> str:
    """
    Generate growth report from history.
    """
    history = sorted(HISTORY_DIR.glob("*.csv"))
    if not history:
        return "> Growth Analytics : _No history available._"

    latest = history[-1]
    repository_rows = {}

    with latest.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            repository_rows.setdefault(
                row["repository"],
                [],
            ).append(row)

    lines = []
    lines.append("| Repository | ⭐ Growth | 👀 Views Δ | 📥 Clones Δ |")
    lines.append("|:--|--:|--:|--:|")

    for repo, rows in sorted(repository_rows.items()):
        if len(rows) == 1:
            star_growth = 0
            view_growth = 0
            clone_growth = 0

        else:
            first = rows[0]
            last = rows[-1]
            star_growth = (
                int(last["stars"])
                - int(first["stars"])
            )
            view_growth = (
                int(last["views"])
                - int(first["views"])
            )
            clone_growth = (
                int(last["clones"])
                - int(first["clones"])
            )

        lines.append(
            f"| {repo} | "
            f"{star_growth:+d} | "
            f"{view_growth:+d} | "
            f"{clone_growth:+d} |"
        )

    lines.append("")
    lines.append(
        f"> Monthly History : **{latest.name}**"
    )
    return "\n".join(lines)


def main():
    initialize_directories()
    LOGGER.info("Generate Reports ...")
    repositories = load_repositories()

    reports = {
        "dashboard.md": generate_dashboard(repositories),
        "traffic.md": generate_traffic(repositories),
        "growth.md": generate_growth(repositories),
    }

    for filename, content in reports.items():
        write_markdown(
            REPORT_DIR / filename,
            content,
        )
        LOGGER.info(
            "Updated %s",
            filename,
        )

    LOGGER.warning("Reports All Updated [3].")


if __name__ == "__main__":
    main()