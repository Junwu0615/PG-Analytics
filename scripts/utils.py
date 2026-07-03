#!/usr/bin/env python3
"""
Platform Genesis Universe Analytics

Module:
    Shared Utilities

Description:
    Common helper functions for configuration loading,
    JSON serialization, filesystem operations,
    timestamp generation, and logging.

Author:
    Junwu
License:
    MIT
"""
from __future__ import annotations
import json, yaml, logging
from datetime import datetime
from pathlib import Path
from typing import Any


# ==============================================================================
# Path
# ==============================================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = PROJECT_ROOT / "data"
LATEST_DIR = DATA_DIR / "latest"
REPORT_DIR = PROJECT_ROOT / "reports"
HISTORY_DIR = PROJECT_ROOT / "history"


# ==============================================================================
# Logger
# ==============================================================================
LOGGER = logging.getLogger("PG-Analytics")
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)


# ==============================================================================
# Filesystem
# ==============================================================================
def ensure_directory(path: Path) -> None:
    """
    Create directory if it does not exist.
    """
    path.mkdir(parents=True, exist_ok=True)


def initialize_directories() -> None:
    """
    Create required project directories.
    """
    for directory in [
        DATA_DIR,
        LATEST_DIR,
        REPORT_DIR,
        HISTORY_DIR,
    ]:
        ensure_directory(directory)


# ==============================================================================
# YAML
# ==============================================================================
def load_yaml(path: Path) -> dict[str, Any]:
    """
    Load YAML configuration file.
    """
    with path.open(
        "r",
        encoding="utf-8",
    ) as fp:
        return yaml.safe_load(fp)


# ==============================================================================
# JSON
# ==============================================================================
def load_json(path: Path) -> dict[str, Any]:
    """
    Load JSON file.
    """
    with path.open(
        "r",
        encoding="utf-8",
    ) as fp:
        return json.load(fp)


def save_json(
    path: Path,
    data: dict[str, Any],
) -> None:
    """
    Save JSON file.
    """
    with path.open(
        "w",
        encoding="utf-8",
    ) as fp:
        json.dump(
            data,
            fp,
            indent=4,
            ensure_ascii=False,
            sort_keys=False,
        )


# ==============================================================================
# Markdown
# ==============================================================================
def write_markdown(
    path: Path,
    content: str,
) -> None:
    """
    Save Markdown report.
    """
    with path.open(
        "w",
        encoding="utf-8",
    ) as fp:
        fp.write(content)


# ==============================================================================
# Time
# ==============================================================================
def utc_now() -> datetime:
    """
    Current UTC timestamp.
    """
    return datetime.utcnow()


def today() -> str:
    """
    YYYY-MM-DD
    """
    return utc_now().strftime("%Y-%m-%d")


def current_month() -> str:
    """
    YYYY-MM
    """
    return utc_now().strftime("%Y-%m")


# ==============================================================================
# Config
# ==============================================================================
def repositories_config() -> dict[str, Any]:
    """
    Load repositories.yml
    """
    return load_yaml(CONFIG_DIR / "repositories.yml")


def analytics_config() -> dict[str, Any]:
    """
    Load analytics.yml
    """
    return load_yaml(CONFIG_DIR / "analytics.yml")