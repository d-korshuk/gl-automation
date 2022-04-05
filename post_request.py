import requests

base_url = "https://httpbin.org/post"
payload = {"firstName": "john", "lastName": "Doe"}

r = requests.post(base_url, params=payload)

print(r.raise_for_status)
print(r.text)
