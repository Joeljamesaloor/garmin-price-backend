import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("ADMITAD_CLIENT_ID")
CLIENT_SECRET = os.getenv("ADMITAD_CLIENT_SECRET")

def get_access_token():
    url = "https://api.admitad.com/token/"
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "public_data"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()
    return response.json()
