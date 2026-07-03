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


def append_repository(path: Path, data: dict):
    """
    Append one repository row to CSV safely.
    """
    repo = data.get("repository", "unknown")
    repository = data.get("repository_metrics", {}) or {}
    traffic = data.get("traffic", {}) or {}
    views = traffic.get("views", {}) or {}
    clones = traffic.get("clones", {}) or {}

    row = [
        today(),
        repo,
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

    # atomic append (reduce corruption risk)
    with path.open("a", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(row)


def main():
    initialize_directories()
    history = csv_file()
    write_header(history)
    LOGGER.warning("Export History ...")

    for json_file in sorted(LATEST_DIR.glob("*.json")):
        LOGGER.info("Processing %s", json_file.name)

        if json_file.stat().st_size == 0:
            LOGGER.warning("Skip empty file: %s", json_file.name)
            continue

        try:
            metrics = load_json(json_file)
        except ValueError as e:
            LOGGER.warning("Skip corrupted JSON: %s (%s)", json_file.name, str(e))
            continue

        if not isinstance(metrics, dict):
            LOGGER.warning("Skip invalid JSON: %s", json_file.name)
            continue

        if "repository" not in metrics:
            LOGGER.warning("Skip malformed JSON: %s", json_file.name)
            continue

        append_repository(history, metrics)

    LOGGER.warning("History Updated.")


if __name__ == "__main__":
    main()