def extract_metrics(repo):
    return {
        "owner": repo["owner"]["login"],
        "name": repo["name"],
        "stars": repo["stargazerCount"],
        "created_at": repo["createdAt"],
        "updated_at": repo["updatedAt"],
        "language": repo["primaryLanguage"]["name"] if repo["primaryLanguage"] else None,
        "merged_prs": repo["pullRequests"]["totalCount"],
        "releases": repo["releases"]["totalCount"],
        "issues_total": repo["issues"]["totalCount"],
        "issues_closed": repo["closedIssues"]["totalCount"],
    }