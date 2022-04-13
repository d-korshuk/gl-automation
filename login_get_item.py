import json
from socketserver import BaseRequestHandler
import requests


base_url = "https://reqres.in/"
login_url = base_url + "api/login"
get_item_url = base_url + "api/unknown/2"
payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}


#Logging in to get a token
r = requests.post(login_url, data=payload)
print(r.text)
r.json = r.json()
token = r.json["token"]


#Getting an item
r = requests.get(get_item_url, headers={"Autorization": token})
print(r.text)



