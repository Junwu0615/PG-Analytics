#!/usr/bin/env python3
"""
Platform Genesis Universe Analytics

Module:
    Historical Metrics Exporter

Description:
    Export repository metrics into monthly history CSV files.

Author:
    Junwu
License:
    MIT
"""
from __future__ import annotations
import csv
from pathlib import Path
from utils import (
    today,
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


def csv_file() -> Path:
    """
    Current monthly history file.
    """
    return HISTORY_DIR / f"{current_month()}-history.csv"


def write_header(path: Path) -> None:
    """
    Ensure CSV header exists and is valid.
    """
    if not path.exists() or path.stat().st_size == 0:
        with path.open("w", newline="", encoding="utf-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(CSV_HEADER)


def build_row(data: dict) -> list:
    """
    Build one history row from repository metrics.
    """
    repository = data.get("repository_metrics", {}) or {}
    traffic = data.get("traffic", {}) or {}
    views = traffic.get("views", {}) or {}
    clones = traffic.get("clones", {}) or {}

    return [
        today(),
        data.get("repository", "unknown"),
        repository.get("stars", 0),
        repository.get("forks", 0),
        repository.get("watchers", 0),
        repository.get("open_issues", 0),
        repository.get("language", "unknown"),
        views.get("count", 0),
        views.get("uniques", 0),
        clones.get("count", 0),
        clones.get("uniques", 0),
    ]


def load_history(path: Path) -> dict:
    """
    Load history into memory.
    Key:
        (date, repository)
    """
    records = {}
    if not path.exists():
        return records

    with path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            date = row.get("date")
            repo = row.get("repository")

            if not date or not repo:
                continue

            records[(date, repo)] = row

    return records


def merge_history(records: dict, metrics: dict) -> None:
    """
    Merge latest repository metrics.

    Existing records of the same
    (date, repository)
    will be replaced.
    """
    row = build_row(metrics)
    key = (row[0], row[1])
    record = dict(zip(CSV_HEADER, row))
    records[key] = record


def rewrite_history(path: Path, records: dict) -> None:
    """
    Rewrite monthly history CSV atomically.

    Validation:
        - Record count must not decrease unexpectedly.
    """
    # Existing record count
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
            f"History corruption detected "
            f"(before={previous_count}, after={current_count})"
        )

    # Atomic replace
    tmp_path.replace(path)
    LOGGER.warning("History Updated (%d records)", current_count)


def main():
    initialize_directories()
    history = csv_file()
    write_header(history)
    records = load_history(history)
    LOGGER.warning("Export History ...")

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

        merge_history(records, metrics)

    rewrite_history(history, records)
    LOGGER.warning("History Updated.")


if __name__ == "__main__":
    main()