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
    Create CSV header.
    """
    if path.exists(): return
    with path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as fp:
        writer = csv.writer(fp)
        writer.writerow(CSV_HEADER)


def append_repository(path: Path, data: dict):
    repo = data["repository"]
    repository = data["repository_metrics"]
    traffic = data.get("traffic", {})
    views = traffic.get("views", {})
    clones = traffic.get("clones", {})

    row = [
        today(),
        repo,
        repository["stars"],
        repository["forks"],
        repository["watchers"],
        repository["open_issues"],
        repository["language"],
        views.get("count", 0),
        views.get("uniques", 0),
        clones.get("count", 0),
        clones.get("uniques", 0),
    ]
    with path.open(
        "a",
        newline="",
        encoding="utf-8",
    ) as fp:
        writer = csv.writer(fp)
        writer.writerow(row)


def main():
    initialize_directories()
    history = csv_file()
    write_header(history)
    LOGGER.info("Export History")

    for json_file in sorted(LATEST_DIR.glob("*.json")):
        LOGGER.info("Processing %s", json_file.name)
        metrics = load_json(json_file)
        append_repository(history,metrics)

    LOGGER.info("History Updated")


if __name__ == "__main__":
    main()