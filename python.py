import requests

# Set the access token and API endpoint URL
access_token = "your-access-token"
api_url = "https://api.github.com/repos/:owner/:repo/pulls/:pull_number/reviews/:review_id/events"

# Set the owner, repo, pull number, and review ID
owner = "your-repo-owner"
repo = "your-repo-name"
pull_number = "pull-request-number"
review_id = "review-id-to-approve"

# Set the request headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/vnd.github.v3+json"
}

# Set the request payload
payload = {
    "event": "APPROVE",
    "body": "Looks good to me!"
}

# Send the API request to approve the pull request
response = requests.put(
    api_url.replace(":owner", owner)
          .replace(":repo", repo)
          .replace(":pull_number", pull_number)
          .replace(":review_id", review_id),
    headers=headers,
    json=payload
)

# Check the response status code and print the response content
if response.status_code == 200:
    print("Pull request approved!")
else:
    print(f"Error: {response.status_code} - {response.content}")
