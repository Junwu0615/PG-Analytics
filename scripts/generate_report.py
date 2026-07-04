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
# from pathlib import Path
# from datetime import datetime
from utils import (
    utc_now,
    save_json,
    load_json,
    write_markdown,
    initialize_directories,
    LOGGER,
    DATA_DIR,
    LATEST_DIR,
    REPORT_DIR,
    HISTORY_DIR,
    SORTED_LIST,
)


def load_repositories() -> list[dict]:
    repositories = []
    for repository in SORTED_LIST:
        json_file = LATEST_DIR / f"{repository}.json"

        if not json_file.exists():
            LOGGER.warning("Skip missing file: %s", json_file.name)
            continue

        if json_file.stat().st_size == 0:
            LOGGER.warning("Skip empty file: %s", json_file.name)
            continue

        try:
            data = load_json(json_file)
        except Exception as e:
            LOGGER.warning("Skip corrupted JSON: %s (%s)", json_file.name, str(e))
            continue

        if not isinstance(data, dict):
            LOGGER.warning("Skip invalid JSON: %s", json_file.name)
            continue

        if "repository" not in data:
            LOGGER.warning("Skip malformed JSON: %s", json_file.name)
            continue

        repositories.append(data)

    return repositories


def generate_dashboard(repositories: list[dict]) -> str:
    if not repositories:
        return "> _Repository Dashboard :　No repositories available_"

    lines = []
    lines.append(" | *📁 Repository* | *⭐ Stars* | *🍴 Forks* | *👀 Views* | *👤 Unique Visitors* | *📥 Clones* | *👤 Unique Cloners* |")
    lines.append(" |:--|--:|--:|--:|--:|--:|--:|")

    total_views = 0
    total_clones = 0
    total_stars = 0
    total_forks = 0
    total_unique_views = 0
    total_unique_clones = 0

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
        unique_views = views.get("uniques", 0)
        unique_clones = clones.get("uniques", 0)

        total_stars += stars
        total_forks += forks
        total_views += view_count
        total_clones += clone_count
        total_unique_views += unique_views
        total_unique_clones += unique_clones

        lines.append(f" | *{repo_name}* | *{stars}* | *{forks}* | *{view_count}* | *{unique_views}* | *{clone_count}* | *{unique_clones}* |")

    lines.append("- ### *Summary*")
    lines.append(f"  - *📁 Repository :　{len(repositories)}*")
    lines.append(f"  - *⭐ Stars :　{total_stars}*")
    lines.append(f"  - *🍴 Forks :　{total_forks}*")
    lines.append(f"  - *👀 Views ( 14 days ) :　{total_views}*")
    lines.append(f"  - *👤 Unique Visitors ( 14 days ) :　{total_unique_views}*")
    lines.append(f"  - *📥 Clones ( 14 days ) :　{total_clones}*")
    lines.append(f"  - *👤 Unique Cloners ( 14 days ) :　{total_unique_clones}*")
    lines.append(f"> _Generated at [ UTC+0 ] :　{str(utc_now().isoformat())[:19]}_")

    return "\n".join(lines)


def generate_traffic(repositories: list[dict]) -> str:
    """
    Generate repository traffic report.
    """
    if not repositories:
        return "> _Traffic Analytics :　No repositories available._"

    lines = []
    lines.append("| *📁 Repository* | *👀 Views* | *👤 Views Unique* | *📥 Clones* | *👤 Clones Unique* |")
    lines.append("|:--|--:|--:|--:|--:|")

    total_views = 0
    total_unique_views = 0
    total_clones = 0
    total_unique_clones = 0

    for repo in repositories:
        repo_name = repo.get("repository", "unknown")

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
            f"| *{repo_name}* | "
            f"*{view_count}* | "
            f"*{unique_views}* | "
            f"*{clone_count}* | "
            f"*{unique_clones}* |"
        )

    lines.append("- ### *Summary*")
    lines.append(f"  - *👀 Views ( 14 Days ) :　{total_views}*")
    lines.append(f"  - *👤 Unique Visitors :　{total_unique_views}*")
    lines.append(f"  - *📥 Clones ( 14 Days ) :　{total_clones}*")
    lines.append(f"  - *👤 Unique Cloners :　{total_unique_clones}*")
    lines.append(f"> _Generated at [ UTC+0 ] :　{str(utc_now().isoformat())[:19]}_")

    return "\n".join(lines)


def build_summary(repositories: list[dict]) -> dict:
    """
    Summary 統計 => 儲存 json
    """
    summary = {
        "repository_count": len(repositories),
        "stars": 0,
        "forks": 0,
        "views": 0,
        "unique_views": 0,
        "clones": 0,
        "unique_clones": 0,
    }
    for repo in repositories:
        metrics = repo.get("repository_metrics", {}) or {}
        traffic = repo.get("traffic", {}) or {}
        views = traffic.get("views", {}) or {}
        clones = traffic.get("clones", {}) or {}

        summary["stars"] += metrics.get("stars", 0)
        summary["forks"] += metrics.get("forks", 0)
        summary["views"] += views.get("count", 0)
        summary["clones"] += clones.get("count", 0)

        summary["unique_views"] += views.get("uniques", 0)
        summary["unique_clones"] += clones.get("uniques", 0)

    save_json(DATA_DIR / "summary.json", summary)
    return summary


def generate_summary(summary_dict: dict) -> str:
    """
    Summary 統計 => 建立 Markdown 表格結構
    """
    lines = []
    lines.append("| *📐 Metric* | *🧮 Value* |")
    lines.append("|:--|--:|")
    lines.append(f"| *📁 Total Repositories* | *{summary_dict.get('repository_count', 0)}* |")
    lines.append(f"| *⭐ Total Stars* | *{summary_dict.get('stars', 0)}* |")
    lines.append(f"| *🍴 Total Forks* | *{summary_dict.get('forks', 0)}* |")
    lines.append(f"| *👀 Total Views* | *{summary_dict.get('views', 0)}* |")
    lines.append(f"| *👤 Unique Visitors* | *{summary_dict.get('unique_views', 0)}* |")
    lines.append(f"| *📥 Total Clones* | *{summary_dict.get('clones', 0)}* |")
    lines.append(f"| *👤 Unique Cloners* | *{summary_dict.get('unique_clones', 0)}* |")
    lines.append(f"> _Note :　Metrics are aggregated across all tracked repositories._")
    lines.append(f">")
    lines.append(f"> _Generated at [ UTC+0 ] :　{str(utc_now().isoformat())[:19]}_")

    return "\n".join(lines)


def generate_growth() -> str:
    """
    Generate growth report from historical CSV snapshots.
    """
    history = sorted(HISTORY_DIR.glob("*.csv"))
    if not history:
        return "> _Growth Analytics :　No history available._"

    first_record = {
        repo: None
        for repo in SORTED_LIST
    }
    last_record = {
        repo: None
        for repo in SORTED_LIST
    }

    # Scan history csv
    csv_file = history[-1]
    with csv_file.open("r", encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            repo = row.get("repository")
            if repo not in SORTED_LIST:
                continue

            # first occurrence
            if first_record[repo] is None:
                first_record[repo] = row

            # keep newest
            last_record[repo] = row

    # Markdown
    lines = []
    lines.append("| *📁 Repository* | *⭐ Stars ↕* | *👀 Forks ↕* | *📥 Open Issues ↕* |")
    lines.append("|:--|--:|--:|--:|")

    for repo in SORTED_LIST:
        first = first_record[repo]
        last = last_record[repo]
        if first is None or last is None:
            lines.append(f"| *{repo}* | *0* | *0* | *0* |")
            continue

        star_growth = int(last["stars"]) - int(first["stars"])
        fork_growth = int(last["forks"]) - int(first["forks"])
        open_issues_growth = int(last["open_issues"]) - int(first["open_issues"])

        lines.append(
            f"| *{repo}* | "
            f"*{star_growth:+d}* | "
            f"*{fork_growth:+d}* | "
            f"*{open_issues_growth:+d}* |"
        )

    # lines.append(f"> _Statistical Scope :　"
    #              f"**{'-'.join(history[0].stem.split('-')[:2])}** → "
    #              f"**{'-'.join(history[-1].stem.split('-')[:2])}**_")
    lines.append(f"> _Statistical Scope :　**{'-'.join(history[-1].stem.split('-')[:2])}**_")
    lines.append(">")
    lines.append(f"> _Generated at [ UTC+0 ] :　{str(utc_now().isoformat())[:19]}_")

    return "\n".join(lines)


def main():
    initialize_directories()
    LOGGER.info("Generate Reports ...")
    repositories = load_repositories()

    summary_dict = build_summary(repositories)
    reports = {
        "dashboard.md": generate_dashboard(repositories),
        "traffic.md": generate_traffic(repositories),
        "growth.md": generate_growth(),
        "summary.md": generate_summary(summary_dict),
    }
    for filename, content in reports.items():
        if not isinstance(content, str):
            LOGGER.warning("Warning: Content for %s is type %s, not str. "
                           "Converting to str.", filename, type(content))
            content = str(content)

        write_markdown(REPORT_DIR / filename, content)
        LOGGER.info("Updated %s", filename)

    LOGGER.warning("Reports All Updated [3].")


if __name__ == "__main__":
    main()