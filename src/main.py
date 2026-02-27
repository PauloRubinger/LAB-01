import csv
from dotenv import load_dotenv
import os

load_dotenv()

from .github_api.client import run_query
from .github_api.query import top_repositories_query
from .processing.parser import parse_repositories
from .processing.metrics import extract_metrics

def test_query():
    return """
    {
      viewer {
        login
      }
    }
    """

def main():
    response = run_query(top_repositories_query())
    # response = run_query(test_query())
    print(response)
    repos = parse_repositories(response)

    os.makedirs("data", exist_ok=True)

    with open("data/repos_100.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "owner", "name", "stars",
                "created_at", "updated_at", "language",
                "merged_prs", "releases",
                "issues_total", "issues_closed"
            ]
        )
        writer.writeheader()

        for repo in repos:
            writer.writerow(extract_metrics(repo))

    print("✅ Sprint 1 concluída com sucesso")

if __name__ == "__main__":
    main()