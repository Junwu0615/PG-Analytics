#!/usr/bin/env python3
"""
Platform Genesis Universe Analytics

Module:
    Repository Metrics Collector

Description:
    Collect repository metadata and traffic statistics
    from GitHub REST API.

Author:
    Junwu
License:
    MIT
"""
from __future__ import annotations
import os
from github import Github
from github.GithubException import GithubException
from utils import (
    analytics_config,
    initialize_directories,
    repositories_config,
    save_json,
    utc_now,
    LOGGER,
    LATEST_DIR,
)


def github_client() -> Github:
    """
    Create GitHub client.
    """
    token = os.getenv("PG_TOKEN")
    if not token:
        raise RuntimeError("PG_TOKEN is not defined.")

    return Github(token)


def safe_collect_repo(github, config, name):
    try:
        repo = github.get_repo(f"{config['owner']}/{name}")
        metrics = collect_repository(repo)
        return metrics

    except Exception as e:
        LOGGER.error("Repo failed %s: %s", name, str(e))
        return {
            "repository": name,
            "repository_metrics": {},
            "traffic": {},
            "error": str(e),
            "generated_at": utc_now().isoformat(),
        }


def collect_repository(repo):
    """
    Collect repository metrics.
    """
    # 預設 Traffic 結構初始化
    daily_views = {}
    views_count = 0
    views_uniques = 0

    daily_clones = {}
    clones_count = 0
    clones_uniques = 0

    try:
        # 取得含每日明細的 traffic 物件
        views = repo.get_views_traffic(per="day")
        views_count = views.get("count", 0) if hasattr(views, "get") else getattr(views, "count", 0)
        views_uniques = views.get("uniques", 0) if hasattr(views, "get") else getattr(views, "uniques", 0)

        # PyGithub 通常將每日明細存在 .views 屬性中
        if hasattr(views, "views"):
            daily_views = {
                v.timestamp.strftime("%Y-%m-%d"): {
                    "count": v.count,
                    "uniques": v.uniques
                }
                for v in views.views
            }
    except Exception as e:
        pass

    try:
        clones = repo.get_clones_traffic(per="day")
        clones_count = clones.get("count", 0) if hasattr(clones, "get") else getattr(clones, "count", 0)
        clones_uniques = clones.get("uniques", 0) if hasattr(clones, "get") else getattr(clones, "uniques", 0)

        # PyGithub 通常將每日明細存在 .clones 屬性中
        if hasattr(clones, "clones"):
            daily_clones = {
                c.timestamp.strftime("%Y-%m-%d"): {
                    "count": c.count,
                    "uniques": c.uniques
                }
                for c in clones.clones
            }
    except Exception as e:
        pass

    return {
        "repository": repo.name,
        "full_name": repo.full_name,
        "description": repo.description,
        "private": repo.private,
        "repository_metrics": {
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "watchers": repo.subscribers_count,
            "open_issues": repo.open_issues_count,
            "default_branch": repo.default_branch,
            "language": repo.language,
            "size_kb": repo.size,
        },
        "activity": {
            "created_at": repo.created_at.isoformat(),
            "updated_at": repo.updated_at.isoformat(),
            "pushed_at": repo.pushed_at.isoformat(),
        },
        "traffic": {
            "views": {
                "count": views_count,
                "uniques": views_uniques,
                "daily": daily_views  # 取得精準的單日鍵值對
            },
            "clones": {
                "count": clones_count,
                "uniques": clones_uniques,
                "daily": daily_clones  # 取得精準的單日鍵值對
            },
        },
        "generated_at": utc_now().isoformat(),
    }


def main():
    initialize_directories()
    config = repositories_config()
    github = github_client()
    LOGGER.warning("Repository Collector Started ...")

    for repository in config["repositories"]:
        if not repository["enabled"]:
            continue

        name = repository["name"]
        LOGGER.info("Collecting %s", name)

        metrics = safe_collect_repo(
            github,
            config,
            repository["name"]
        )

        output = LATEST_DIR / f"{name}.json"
        save_json(output, metrics)
        LOGGER.info("Saved %s", output.name)

    LOGGER.warning("Repository Collector Completed.")


if __name__ == "__main__":
    main()