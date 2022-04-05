import requests

base_url = "https://httpbin.org/post"

r = requests.post(base_url, json={"username" : "dima", "password" : "test"})

print(r.raise_for_status)
print(r.text)
