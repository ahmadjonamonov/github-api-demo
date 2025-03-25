import requests

username = "octocat"
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
data = response.json()

print(f"Username: {data['login']}")
print(f"Followers: {data['followers']}")
print(f"Public Repos: {data['public_repos']}")
