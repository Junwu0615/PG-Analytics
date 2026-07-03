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
    LOGGER,
    LATEST_DIR,
    analytics_config,
    initialize_directories,
    repositories_config,
    save_json,
    utc_now,
)


def github_client() -> Github:
    """
    Create GitHub client.
    """
    token = os.getenv("PG_TOKEN")
    if not token:
        raise RuntimeError("PG_TOKEN is not defined.")

    return Github(token)


def collect_repository(repo):
    """
    Collect repository metrics.
    """
    data = {
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
        "traffic": {},
        "generated_at": utc_now().isoformat(),
    }

    return data


def collect_traffic(repo, metrics):
    """
    Collect traffic statistics.
    """
    try:
        views = repo.get_views_traffic()
        clones = repo.get_clones_traffic()

        LOGGER.warning(type(views))
        LOGGER.warning(type(clones))

        metrics["traffic"] = {
            "views": {
                # "count": views["count"],
                "count": views.count,
                # "uniques": views["uniques"],
                "uniques": views.uniques,
            },
            "clones": {
                # "count": clones["count"],
                "count": clones.count,
                # "uniques": clones["uniques"],
                "uniques": clones.uniques,
            },
        }

    except GithubException:
        LOGGER.warning(
            "Traffic API unavailable : %s",
            repo.name,
        )


def main():
    initialize_directories()
    config = repositories_config()
    github = github_client()
    LOGGER.info("Repository Collector Started")

    for repository in config["repositories"]:
        if not repository["enabled"]:
            continue

        name = repository["name"]
        LOGGER.info("Collecting %s", name)
        repo = github.get_repo(f'{config["owner"]}/{name}')
        metrics = collect_repository(repo)
        collect_traffic(repo, metrics)
        output = LATEST_DIR / f"{name}.json"
        save_json(output,metrics)
        LOGGER.info("Saved %s", output.name)

    LOGGER.info("Repository Collector Completed")


if __name__ == "__main__":
    main()