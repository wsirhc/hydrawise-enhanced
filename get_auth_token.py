# From Bruno Code Generator
import requests

def get_auth_token(user, password, client_secret):

    url = "https://app.hydrawise.com/api/v2/oauth/access-token"

    payload = {
        "grant_type": "password",
        "client_id": "hydrawise_app",
        "client_secret": client_secret,
        "username": user,
        "password": password,
        "scope": "all"
    }
    headers = {
        "host": "app.hydrawise.com",
        "referer": "https://app.hydrawise.com/config/login",
        "origin": "https://app.hydrawise.com",
        "content-type": "application/x-www-form-urlencoded",
        "connection": "keep-alive",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "priority": "u=4",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "te": "trailers"
    }

    response = requests.post(url, data=payload, headers=headers)
    access_token = response.json()['access_token']
    #print(response.json())

    return access_token
