def top_repositories_query(cursor=None):
    after = f', after: "{cursor}"' if cursor else ""

    return f"""
    {{
      search(query: "stars:>10000 sort:stars-desc", type: REPOSITORY, first: 10{after}) {{
        pageInfo {{
          hasNextPage
          endCursor
        }}
        nodes {{
          ... on Repository {{
            name
            owner {{
              login
            }}
            stargazerCount
            createdAt
            updatedAt
            primaryLanguage {{
              name
            }}
            pullRequests(states: MERGED) {{
              totalCount
            }}
            releases {{
              totalCount
            }}
            issues {{
              totalCount
            }}
            closedIssues: issues(states: CLOSED) {{
              totalCount
            }}
          }}
        }}
      }}
    }}
    """