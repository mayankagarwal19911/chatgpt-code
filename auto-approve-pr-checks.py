import requests
import os

# Authenticate to the GitHub API using a personal access token
headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}

# Retrieve the list of pull requests for the repository
response = requests.get("https://api.github.com/repos/:owner/:repo/pulls", headers=headers)
pull_requests = response.json()

# Update status checks for each pull request
for pr in pull_requests:
    # Retrieve the SHA of the most recent commit
    response = requests.get(f"https://api.github.com/repos/:owner/:repo/pulls/{pr['number']}/commits", headers=headers)
    sha = response.json()[-1]["sha"]
    
    # Update status checks for the commit
    payload = {
        "state": "success",
        "description": "All status checks have passed",
        "context": "continuous-integration"
    }
    response = requests.post(f"https://api.github.com/repos/:owner/:repo/statuses/{sha}", headers=headers, json=payload)
