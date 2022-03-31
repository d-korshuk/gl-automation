import requests

base_url = "https://httpbin.org/get"
headers = {
        "User-Agent": "test"
}

r = requests.get(base_url, headers=headers)


print(r.raise_for_status())
print(r.headers)
print(r.url)