import requests

username = input("Enter username: ")

sites = [
    f"https://github.com/{username}",
    f"https://instagram.com/{username}",
    f"https://twitter.com/{username}",
    f"https://tiktok.com/@{username}"
]

for site in sites:
    r = requests.get(site)

    if r.status_code == 200:
        print(f"Found: {site}")
    else:
        print(f"Not found: {site}")
