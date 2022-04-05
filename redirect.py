import requests

base_url = "http://github.com"

r = requests.get(base_url, allow_redirects=True)
print(r.raise_for_status)
print(r.history)