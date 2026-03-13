from github_api.client import run_query
from github_api.query import top_repositories_query

def fetch_repositories(total=1000):

    cursor = None
    all_repos = []

    while len(all_repos) < total:

        print(f"Coletando página... ({len(all_repos)})")

        query = top_repositories_query(cursor)
        response = run_query(query)

        search = response["data"]["search"]

        repos = search["nodes"]
        all_repos.extend(repos)

        page_info = search["pageInfo"]

        if not page_info["hasNextPage"]:
            break

        cursor = page_info["endCursor"]

    return all_repos[:total]