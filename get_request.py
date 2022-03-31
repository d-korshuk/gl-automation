import requests

headers = {
        "User-Agent": "test"
}

r = requests.get("https://httpbin.org/get", headers=headers)


print(r.raise_for_status())
print(r.headers)
print(r.url)