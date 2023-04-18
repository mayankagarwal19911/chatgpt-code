import requests

# Set the API endpoint and the required headers
api_endpoint = 'https://api.github.com'
headers = {
    'Authorization': 'Token YOUR_PAT_HERE',
    'Accept': 'application/vnd.github.v3+json'
}

# Set the repository details and the pull request number
owner = 'OWNER_NAME'
repo = 'REPO_NAME'
pr_number = 'PR_NUMBER'

# Create the merge payload
payload = {
    'commit_title': 'Auto-merge pull request',
    'commit_message': 'Automatically merged pull request',
    'merge_method': 'merge'
}

# Send the merge request to the API
url = f'{api_endpoint}/repos/{owner}/{repo}/pulls/{pr_number}/merge'
response = requests.put(url, headers=headers, json=payload)

# Check the response status code
if response.status_code == 200:
    print(f'Pull request #{pr_number} merged!')
else:
    print('Error merging pull request')
