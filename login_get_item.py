import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s")



base_url = "https://reqres.in/"
login_url = base_url + "api/login"
get_item_url = base_url + "api/unknown/2"
payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}


#Logging in to get a token
def login():
    r = requests.post(login_url, data=payload)
    logging.info(r.text)
    global token
    token = r.json()["token"]


#Getting an item
def get_item():
    r = requests.get(get_item_url, headers={"Autorization": token})
    logging.info(r.text)


if __name__ == "__main__":
    login()
    get_item()

