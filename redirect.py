import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s")
base_url = "http://github.com"

def redirect_request():
    r = requests.get(base_url, allow_redirects=True)
    logging.info(r.history)


if __name__ == "__main__":
    redirect_request()