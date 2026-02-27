def top_repositories_query():
    return """
    query {
      search(query: "stars:>10000", type: REPOSITORY, first: 10) {
        nodes {
          ... on Repository {
            name
            owner { login }
            stargazerCount
            createdAt
            updatedAt
            primaryLanguage { name }
            pullRequests(states: MERGED) { totalCount }
            releases { totalCount }
            issues { totalCount }
            closedIssues: issues(states: CLOSED) { totalCount }
          }
        }
      }
    }
    """