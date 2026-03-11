import csv
from dotenv import load_dotenv
import os

load_dotenv()

from .github_api.pagination import fetch_repositories
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

    print("Coletando repositórios...")

    repos = fetch_repositories(1000)

    os.makedirs("data", exist_ok=True)

    with open("data/repos_1000.csv", "w", newline="", encoding="utf-8") as f:
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

    print(f"✅ Coletados {len(repos)} repositórios com sucesso!")

if __name__ == "__main__":
    main()