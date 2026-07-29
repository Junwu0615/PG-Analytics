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
from decimal import Decimal, ROUND_HALF_UP
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


def truncate_name(name: str, max_length: int = 22) -> str:
    """
    限制字串長度，超過則進行截斷並加上 ...
    """
    if len(name) > max_length:
        return name[:max_length - 3] + "..."
    return name


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


def extract_metrics(repo: dict) -> dict:
    metrics = repo.get("repository_metrics", {}) or {}
    activity = repo.get("activity", {}) or {}
    traffic = repo.get("traffic", {}) or {}
    views = traffic.get("views", {}) or {}
    clones = traffic.get("clones", {}) or {}

    return {
        "repository": repo.get("repository", "unknown") or "unknown",
        "full_name": repo.get("full_name", "unknown") or "unknown",
        "stars": int(metrics.get("stars", 0)),
        "forks": int(metrics.get("forks", 0)),
        "size_kb": int(metrics.get("size_kb", 0)),
        "watchers": int(metrics.get("watchers", 0)),
        "open_issues": int(metrics.get("open_issues", 0)),
        "commits_count": int(metrics.get("commits_count", 0)),
        "views": int(views.get("count", 0)),
        "unique_views": int(views.get("uniques", 0)),
        "daily_views": views.get("daily", {}),
        "clones": int(clones.get("count", 0)),
        "unique_clones": int(clones.get("uniques", 0)),
        "daily_clones": clones.get("daily", {}),
        "created_at": activity.get("created_at", "")[:10],
        "updated_at": activity.get("updated_at", "")[:10],
        "pushed_at": activity.get("pushed_at", "")[:10],
    }


def generate_dashboard(repositories: list[dict]) -> str:
    if not repositories:
        return "> _Repository Dashboard :　No repositories available_"

    lines = []
    lines.append("")
    lines.append(" | *📁 Repository* | *⭐ Stars* | *🍴 Forks* | *📩 Commit* | *📦 Size<br>( MB )* | *📝 Updated* | *📅 Created* |")
    lines.append(" |:--|--:|--:|--:|--:|--:|--:|")

    for repo in repositories:
        metrics = extract_metrics(repo)

        repo_name = truncate_name(metrics["repository"])
        full_name = metrics["full_name"]
        stars = metrics["stars"]
        forks = metrics["forks"]
        commits_count = metrics["commits_count"]
        size = Decimal(metrics["size_kb"] / 1024).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        created_at = metrics["created_at"]
        pushed_at = metrics["pushed_at"]

        lines.append(f" | _**[{repo_name}](https://github.com/{full_name})**_ | *{stars}* | *{forks}* | *{commits_count}* | *{size}* | *{pushed_at}* | *{created_at}* |")

    return "\n".join(lines)


def generate_traffic(repositories: list[dict]) -> str:
    """
    Generate repository traffic report.
    """
    if not repositories:
        return "> _Traffic Analytics :　No repositories available._"

    lines = []
    lines.append("> _Traffic in the past **14 Days**_")
    lines.append("")
    lines.append("| *📁 Repository* | *👀 Views* | *👤 Views Unique* | *📥 Clones* | *👤 Clones Unique* |")
    lines.append("|:--|--:|--:|--:|--:|")

    total_views = 0
    total_unique_views = 0
    total_clones = 0
    total_unique_clones = 0

    for repo in repositories:
        metrics = extract_metrics(repo)

        repo_name = truncate_name(metrics["repository"])
        full_name = metrics["full_name"]
        # stars = metrics["stars"]
        # forks = metrics["forks"]
        views = metrics["views"]
        clones = metrics["clones"]
        unique_views = metrics["unique_views"]
        unique_clones = metrics["unique_clones"]

        total_views += views
        total_unique_views += unique_views
        total_clones += clones
        total_unique_clones += unique_clones

        lines.append(
            f"| _**[{repo_name}](https://github.com/{full_name})**_ | "
            f"*{views}* | "
            f"*{unique_views}* | "
            f"*{clones}* | "
            f"*{unique_clones}* |"
        )

    lines.append("- ### *Summary*")
    lines.append(f"  - *👀 Views :　{total_views}*")
    lines.append(f"  - *👤 Unique Visitors :　{total_unique_views}*")
    lines.append(f"  - *📥 Clones :　{total_clones}*")
    lines.append(f"  - *👤 Unique Cloners :　{total_unique_clones}*")

    return "\n".join(lines)


def generate_growth(user_name="Junwu0615") -> str:
    """
    Generate growth report from historical CSV snapshots.
    """
    history = sorted(HISTORY_DIR.glob("*.csv"))
    if not history:
        return "> _Growth Analytics : No history available._"

    first_record = {repo: None for repo in SORTED_LIST}
    last_record = {repo: None for repo in SORTED_LIST}

    # 獨立用字典累加每日流量，避免搞混變數
    total_traffic = {
        repo: {
            "views": 0, "unique_views": 0,
            "clones": 0, "unique_clones": 0
        }
        for repo in SORTED_LIST
    }

    # 取最新的當月歷史檔進行統計
    csv_file = history[-1]
    with csv_file.open("r", encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            repo = row.get("repository")
            if repo not in SORTED_LIST:
                continue

            # 1. 抓取最早的一筆（第一行）作為基準點
            if first_record[repo] is None:
                first_record[repo] = row

            # 2. 持續覆蓋，讓迴圈結束時停在最後一筆（最新總量）
            last_record[repo] = row

            # 3. 流量類指標：把每一行的日流量進行區間累加 (Sum)
            total_traffic[repo]["views"] += int(row.get("views", 0) or 0)
            total_traffic[repo]["unique_views"] += int(row.get("unique_views", 0) or 0)
            total_traffic[repo]["clones"] += int(row.get("clones", 0) or 0)
            total_traffic[repo]["unique_clones"] += int(row.get("unique_clones", 0) or 0)

    # Markdown
    lines = []
    lines.append(f"> _Statistical Scope : **{'-'.join(history[-1].stem.split('-')[:2])}**_")
    lines.append("")
    lines.append("| *📁 Repository* | *⭐ Stars ↕* | *🍴 Forks ↕* | *💡 Open Issues ↕* | *👀 Views ↕* | *📥 Clones ↕* |")
    lines.append("|:--|--:|--:|--:|--:|--:|")

    for repo in SORTED_LIST:
        first = first_record[repo]
        last = last_record[repo]
        if first is None or last is None:
            lines.append(f"| _**[{truncate_name(repo)}](https://github.com/{user_name}/{repo})**_ | *0* | *0* | *0* | *0* | *0* |")
            continue

        # 狀態指標：採頭尾 diff (最後一天總量 - 第一天總量)
        star_growth = int(last["stars"]) - int(first["stars"])
        fork_growth = int(last["forks"]) - int(first["forks"])
        open_issues_growth = int(last["open_issues"]) - int(first["open_issues"])

        # 事件流量指標：直接取該區間的累加總和
        views_growth = total_traffic[repo]["views"]
        clones_growth = total_traffic[repo]["clones"]

        lines.append(
            f"| _**[{truncate_name(repo)}](https://github.com/Junwu0615/{repo})**_ | "
            f"*{star_growth:+d}* | "
            f"*{fork_growth:+d}* | "
            f"*{open_issues_growth:+d}* | "
            f"*{views_growth}* | "
            f"*{clones_growth}* | "
        )

    return "\n".join(lines)


def build_summary(repositories: list[dict]) -> dict:
    """
    Summary 統計 → 具備冷啟動支援、嚴格增量更新、對齊按月分區 CSV與冪等性的實作
    """
    summary_file = DATA_DIR / "summary.json"

    # 1. 狀態類指標：直接由當前最新 repositories (latest/*.json) 累加
    summary = {
        "repository_count": len(repositories),
        "stars": 0,
        "forks": 0,
        "commits_count": 0,
        "views": 0,
        "unique_views": 0,
        "clones": 0,
        "unique_clones": 0,
        "size": Decimal("0.00"),
        "last_processed_date": "",  # 記錄最後處理的日期 (YYYY-MM-DD)，用於增量與冪等防護
    }

    for repo in repositories:
        metrics = extract_metrics(repo)
        summary["stars"] += metrics["stars"]
        summary["forks"] += metrics["forks"]
        summary["commits_count"] += metrics["commits_count"]
        summary["size"] += Decimal(metrics["size_kb"] / 1024).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    summary["size"] = str(summary["size"])

    # 2. 處理流量類指標（增量更新 + 冷啟動 + 冪等防護）
    existing_summary = load_json(summary_file) if summary_file.exists() else {}
    last_processed_date = existing_summary.get("last_processed_date", "")

    # 判斷是否為冷啟動
    is_cold_start = not existing_summary or not last_processed_date

    # 冷啟動處理：如果 summary.json 不存在或沒有紀錄上次處理日期，則以現有舊流量為 0 開始
    if not existing_summary:
        LOGGER.warning("Summary.json not found. Performing cold start initialization.")
        summary["views"] = 0
        summary["unique_views"] = 0
        summary["clones"] = 0
        summary["unique_clones"] = 0
    else:
        # 繼承先前的總流量作為基底
        summary["views"] = int(existing_summary.get("views", 0))
        summary["unique_views"] = int(existing_summary.get("unique_views", 0))
        summary["clones"] = int(existing_summary.get("clones", 0))
        summary["unique_clones"] = int(existing_summary.get("unique_clones", 0))

    history = sorted(HISTORY_DIR.glob("*.csv"))
    if history:
        delta_views = 0
        delta_unique_views = 0
        delta_clones = 0
        delta_unique_clones = 0
        max_date_in_csv = last_processed_date

        # - 若是冷啟動，遍歷所有歷史 CSV 建立完整基底
        # - 若是日常增量，只抓取最後 2 份 CSV ([-2:])，完美涵蓋當月與跨月的上月底邊界
        target_history = history if is_cold_start else history[-2:]

        for csv_path in target_history:
            if not csv_path.exists():
                continue

            with csv_path.open("r", encoding="utf-8", newline="") as fp:
                reader = csv.DictReader(fp)
                for row in reader:
                    repo_name = row.get("repository")
                    row_date = row.get("date")

                    if repo_name not in SORTED_LIST or not row_date:
                        continue

                    # 冪等與增量防護：大於上次已處理日期的才計入 Delta
                    if last_processed_date and row_date <= last_processed_date:
                        continue

                    delta_views += int(row.get("views", 0) or 0)
                    delta_unique_views += int(row.get("unique_views", 0) or 0)
                    delta_clones += int(row.get("clones", 0) or 0)
                    delta_unique_clones += int(row.get("unique_clones", 0) or 0)

                    if row_date > max_date_in_csv:
                        max_date_in_csv = row_date

        # 將 Delta 增量安全地疊加到總數上
        summary["views"] += delta_views
        summary["unique_views"] += delta_unique_views
        summary["clones"] += delta_clones
        summary["unique_clones"] += delta_unique_clones
        summary["last_processed_date"] = max_date_in_csv

        mode_str = "Cold Start" if is_cold_start else "Incremental (Last 2 CSVs)"
        LOGGER.info(f"Summary Updated [{mode_str}]: Processed up to date {max_date_in_csv}")

    save_json(summary_file, summary)
    return summary


def generate_summary(summary_dict: dict) -> str:
    """
    Summary 統計 → 建立 Markdown 表格結構
    """
    lines = []
    lines.append(f"> _Note :　Metrics are aggregated across all tracked repositories._")
    lines.append("")
    lines.append("| *📐 Metric* | *🧮 Value* |")
    lines.append("|:--|--:|")
    lines.append(f"| *📁 Total Repositories* | *{summary_dict['repository_count']}* |")
    lines.append(f"| *⭐ Total Stars* | *{summary_dict['stars']}* |")
    lines.append(f"| *🍴 Total Forks* | *{summary_dict['forks']}* |")
    lines.append(f"| *📩 Total Commit* | *{summary_dict['commits_count']}* |")
    lines.append(f"| *📦 Size ( MB )* | *{summary_dict['size']}* |")
    lines.append(f"| *👀 Total Views* | *{summary_dict['views']}* |")
    lines.append(f"| *👤 Total Unique Visitors* | *{summary_dict['unique_views']}* |")
    lines.append(f"| *📥 Total Clones* | *{summary_dict['clones']}* |")
    lines.append(f"| *👤 Total Unique Cloners* | *{summary_dict['unique_clones']}* |")
    return "\n".join(lines)


def generate_update_time():
    # Markdown
    lines = []
    lines.append(">")
    lines.append(f"> _Generated at [ UTC+0 ] :　{str(utc_now().isoformat())[:19]}_")
    lines.append("")
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
        "update_time.md": generate_update_time(),
    }
    for filename, content in reports.items():
        if not isinstance(content, str):
            LOGGER.warning("Warning: Content for %s is type %s, not str. "
                           "Converting to str.", filename, type(content))
            content = str(content)
        write_markdown(REPORT_DIR / filename, content)
        LOGGER.info("Updated %s", filename)

    LOGGER.warning(f"Reports All Updated [{len(reports.keys())}].")


if __name__ == "__main__":
    main()