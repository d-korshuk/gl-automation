import requests

headers = {
        "User-Agent": "test"
}

response = requests.get("https://httpbin.org/get", headers=headers)


print(response.raise_for_status())
print(response.headers)
print(response.url)