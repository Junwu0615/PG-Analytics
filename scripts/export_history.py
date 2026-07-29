#!/usr/bin/env python3
"""
Platform Genesis Universe Analytics

Module:
    Historical Metrics Exporter

Description:
    Export repository metrics into monthly history CSV files (supports cross-month data).

Author:
    Junwu
License:
    MIT
"""
from __future__ import annotations
import csv
from pathlib import Path
from collections import defaultdict
from utils import (
    load_json,
    current_month,
    initialize_directories,
    LOGGER,
    LATEST_DIR,
    HISTORY_DIR,
)

CSV_HEADER = [
    "date",
    "repository",
    "stars",
    "forks",
    "watchers",
    "open_issues",
    "language",
    "views",
    "unique_views",
    "clones",
    "unique_clones",
]


def get_csv_file_by_date(date_str: str) -> Path:
    """
    Get the monthly history file path based on a specific date (YYYY-MM-DD -> YYYY-MM).
    """
    try:
        year_month = date_str[:7]  # 取出 YYYY-MM
    except Exception:
        year_month = current_month()
    return HISTORY_DIR / f"{year_month}-history.csv"


def write_header(path: Path) -> None:
    """
    Ensure CSV header exists and is valid.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.stat().st_size == 0:
        with path.open("w", newline="", encoding="utf-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(CSV_HEADER)


def build_14_days(data: dict) -> list:
    """
    Create 14 historical records based on the repository metrics.
    """
    row_list = []

    repository = data.get("repository_metrics", {}) or {}
    traffic = data.get("traffic", {}) or {}
    views = traffic.get("views", {}) or {}
    clones = traffic.get("clones", {}) or {}

    daily_views = views.get("daily", {})
    daily_clones = clones.get("daily", {})

    # 聯集所有日期的 key，避免某一邊缺少日期導致 KeyError
    all_dates = sorted(set(daily_views.keys()) | set(daily_clones.keys()))

    for daily in all_dates:
        view_data = daily_views.get(daily, {"count": 0, "uniques": 0})
        clone_data = daily_clones.get(daily, {"count": 0, "uniques": 0})

        row_list.append([
            daily,
            data.get("repository", "unknown"),
            repository.get("stars", 0),
            repository.get("forks", 0),
            repository.get("watchers", 0),
            repository.get("open_issues", 0),
            repository.get("language", "unknown"),
            view_data.get("count", 0),
            view_data.get("uniques", 0),
            clone_data.get("count", 0),
            clone_data.get("uniques", 0),
        ])
    return row_list


def load_history(path: Path) -> dict:
    """
    Load history into memory.
    Key:
        (date, repository)
    """
    records = {}
    if not path.exists():
        return records

    with path.open("r", newline="", encoding="utf-8") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            date = row.get("date")
            repo = row.get("repository")

            if not date or not repo:
                continue

            records[(date, repo)] = row

    return records


def rewrite_history(path: Path, records: dict) -> None:
    """
    Rewrite monthly history CSV atomically.

    Validation:
        - Record count must not decrease unexpectedly.
    """
    write_header(path)

    # 重新精確計算該檔案實際已存在的記錄數（避免跨檔案干擾）
    previous_count = 0
    if path.exists():
        with path.open("r", newline="", encoding="utf-8") as fp:
            previous_count = max(sum(1 for _ in csv.DictReader(fp)), 0)

    # Write temporary file
    tmp_path = path.with_suffix(".tmp")

    with tmp_path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=CSV_HEADER)
        writer.writeheader()
        for _, row in sorted(records.items()):
            writer.writerow(row)

    # Validate
    current_count = len(records)
    if current_count < previous_count:
        raise RuntimeError(
            f"History corruption detected for {path.name} "
            f"(before={previous_count}, after={current_count})"
        )

    # Atomic replace
    tmp_path.replace(path)
    LOGGER.warning("History Updated for %s (%d records)", path.name, current_count)


def main():
    initialize_directories()
    LOGGER.warning("Export History ...")

    # 結構: { Path(file_path): { (date, repository): row_dict } }
    grouped_records = defaultdict(dict)

    for json_file in sorted(LATEST_DIR.glob("*.json")):
        LOGGER.info("Processing %s", json_file.name)

        if json_file.stat().st_size == 0:
            LOGGER.warning("Skip empty %s", json_file.name)
            continue

        try:
            metrics = load_json(json_file)
        except Exception as e:
            LOGGER.warning("Skip %s (%s)", json_file.name, str(e))
            continue

        if not isinstance(metrics, dict) or "repository" not in metrics:
            LOGGER.warning("Malformed %s", json_file.name)
            continue

        # 取得 14 天的歷史資料並依照日期分組載入對應月份的記錄
        row_list = build_14_days(metrics)
        for row in row_list:
            date_str = row[0]
            repo_name = row[1]

            target_file = get_csv_file_by_date(date_str)

            # 若該月份尚未載入記憶體，進行初始化並讀取舊檔
            if target_file not in grouped_records:
                write_header(target_file)
                grouped_records[target_file] = load_history(target_file)

            # 更新或加入記錄
            key = (date_str, repo_name)
            grouped_records[target_file][key] = dict(zip(CSV_HEADER, row))


    # 逐一將各個月份的檔案安全寫回
    for path, records in grouped_records.items():
        rewrite_history(path, records)

    LOGGER.warning("All History Updated.")


if __name__ == "__main__":
    main()