import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s")


base_url = "https://httpbin.org/get"
payload = {"firstName" :"John", "lastName" :"Doe"}
headers = {
        "User-Agent": "test"
}


def get_request():
        r = requests.get(base_url, headers=headers, params=payload)
        logging.info(r.content)


if __name__ == "__main__":
        get_request()



