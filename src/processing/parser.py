def parse_repository(repo):

    return {
        "name": repo["name"],
        "owner": repo["owner"]["login"],
        "created_at": repo["createdAt"],
        "updated_at": repo["updatedAt"],
        "releases": repo["releases"]["totalCount"],
        "pull_requests": repo["pullRequests"]["totalCount"],
        "issues": repo["issues"]["totalCount"],
        "closed_issues": repo["closedIssues"]["totalCount"],
        "language": repo["primaryLanguage"]["name"] if repo["primaryLanguage"] else None
    }