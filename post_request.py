import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s")


base_url = "https://httpbin.org/post"
payload = {"firstName": "john", "lastName": "Doe"}


def post_request():
    r = requests.post(base_url, data=payload)
    logging.info(r.json())



if __name__ == "__main__":
    post_request()
