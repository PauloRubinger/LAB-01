def parse_repositories(api_response: dict):
    return api_response["data"]["search"]["nodes"]