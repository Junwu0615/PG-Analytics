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
    LOGGER,
    LATEST_DIR,
    HISTORY_DIR,
    current_month,
    today,
    initialize_directories,
    load_json,
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
    return HISTORY_DIR / f"{current_month()}.csv"


def write_header(path: Path) -> None:
    """
    Ensure CSV header exists and is valid.
    """
    if not path.exists() or path.stat().st_size == 0:
        with path.open("w", newline="", encoding="utf-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(CSV_HEADER)


def safe_get(data: dict, path: list, default=None):
    """
    Safe nested dict access (contract layer)
    """

    for key in path:
        if not isinstance(data, dict):
            return default
        data = data.get(key, {})
    return data or default


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
            key = (
                row["date"],
                row["repository"],
            )
            records[key] = row

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
    records[key] = dict(zip(CSV_HEADER, row))


def rewrite_history(path: Path, records: dict) -> None:
    """
    Rewrite monthly history CSV.
    """
    with path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as fp:
        writer = csv.DictWriter(
            fp,
            fieldnames=CSV_HEADER,
        )
        writer.writeheader()
        for key in sorted(records):
            writer.writerow(
                records[key]
            )


def main():
    initialize_directories()
    history = csv_file()
    write_header(history)
    records = load_history(history)
    LOGGER.warning("Export History ...")

    for json_file in sorted(LATEST_DIR.glob("*.json")):
        LOGGER.info("Processing %s", json_file.name)

        if json_file.stat().st_size == 0:
            LOGGER.warning(
                "Skip empty %s",
                json_file.name,
            )
            continue

        try:
            metrics = load_json(json_file)

        except Exception as e:
            LOGGER.warning(
                "Skip %s (%s)",
                json_file.name,
                str(e),
            )
            continue

        if not isinstance(metrics, dict) or "repository" not in metrics:
            LOGGER.warning(
                "Malformed %s",
                json_file.name,
            )
            continue

        merge_history(records, metrics)

    rewrite_history(history, records)
    LOGGER.warning("History Updated.")


if __name__ == "__main__":
    main()