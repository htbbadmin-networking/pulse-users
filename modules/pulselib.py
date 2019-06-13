import requests
import json
import re

def get_token(username, password):
    base = "https://"
    uri = "/api/v1/auth"
    url = base + host + uri
    auth = (username, password)
    headers = {
    "Content-Type" : "application/json"
    }
    params = {
    }
    data = {
    }
    response = requests.post(url, auth=auth, headers=headers)
    token = response.json('api_key')
    print(response.status_code)
    print(response.text)
    return token

def create_vpn_user(host, auth_token, user):
    base = "https://"
    uri = "/api/v1/configuration/authentication/auth-servers/auth-server/Sys-Local/local/users/user"
    url = base + host + uri
    headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Basic " + auth_token
    }
    params = {
    }
    data = {
    "change-password-at-signin" : user['change-password-at-signin'],
    "console-access" : user['console-access'],
    "enabled" : user['enabled'],
    "fullname" : user['fullname'],
    "one-time-use" : user['one-time-use'],
    # "password-encrypted" : user['password-encrypted'],
    "password-cleartext" : user['password'],
    "username" : user['username']
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    return response
