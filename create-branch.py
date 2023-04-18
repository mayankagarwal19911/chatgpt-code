import requests
import json

repository_name = "my-repository"
owner_name = "my-username"
new_branch_name = "my-new-branch"
access_token = "my-personal-access-token"
base_branch = "main"

url = f"https://api.github.com/repos/{owner_name}/{repository_name}/git/refs"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "ref": f"refs/heads/{new_branch_name}",
    "sha": base_branch
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 201:
    print(f"The new branch '{new_branch_name}' was created successfully.")
else:
    print(f"Error creating the new branch. Status code: {response.status_code}")
