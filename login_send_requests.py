import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s")


login_url = "https://app.cosmosid.com/api/v1/login"
login_payload = {"expiry": 86400, "login_from": "login page"}
login_headers = {"Authorization": "Basic bWFpbGludGVzdEB1a3IubmV0Om1haWxpbnRlc3RAdWtyLm5ldA=="}
root_folder_url = "https://app.cosmosid.com/api/metagenid/v2/files?"
files_count_url = "https://app.cosmosid.com/api/metagenid/v2/files/count?"
runs_url = "https://app.cosmosid.com/api/metagenid/v1/files/7f4c7326-0a4e-4b56-a8d0-8ce002191672/runs?_=1622700773181"
analyses_url = "https://app.cosmosid.com/api/metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/analysis?filter=total&_=1622700773184"
artifacts_url = "https://app.cosmosid.com/api/metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/artifacts?_=1622700773185"

root_folder_params = {"breadcrumbs": "1", "offset": "0", "limit": "1000", "folder_id": "84c966d5-8dce-429d-8f92-44d5e28b1581"}
count_params = {"folder_id": "84c966d5-8dce-429d-8f92-44d5e28b1581"}


def login():
    r = requests.post(login_url, json=login_payload, headers=login_headers) 
    access_token = r.json()["token"]
    return access_token


def root_folder():
    r = requests.get(root_folder_url, headers={"x-token": access_token}, params=root_folder_params)     
    logging.info(r.json())


def files_count():
    r = requests.get(files_count_url, headers={"x-token": access_token}, params=root_folder_params)       
    logging.info(r.raise_for_status)


def file_runs():
    r = requests.get(runs_url, headers={"x-token": access_token})
    logging.info(r.raise_for_status)
                                                                                                       

def file_analyses():
    r = requests.get(analyses_url, headers={"x-token": access_token})     
    logging.info(r.raise_for_status)
                                                                                                 

def file_artifacts():  
    r = requests.get(artifacts_url, headers={"x-token": access_token}) 
    logging.info(r.raise_for_status)


if __name__ == "__main__":
    access_token = login()
    root_folder()
    files_count()
    file_runs()
    file_analyses()
    file_artifacts()