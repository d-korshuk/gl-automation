import requests

base_url = "https://httpbin.org/get"
payload = {"firstName" :"John", "lastName" :"Doe"}
headers = {
        "User-Agent": "test"
}

r = requests.get(base_url, headers=headers, params=payload)


print(r.raise_for_status)
print(r.headers)
print(r.url)


