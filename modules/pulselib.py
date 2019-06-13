import requests
import json
import re

def get_token(host, username, password, verbosity=1):
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
    token = response.json()['api_key']
    if verbosity >= 1:
        print("Retrieving API token...")
    if verbosity >= 2:
        print(response.status_code)
    if verbosity >= 3:
        print(response.text)
    return token

def create_vpn_user(host, auth_token, user, verbosity=1):
    base = "https://"
    auth_server = "DR-Sys-Local"
    uri = "/api/v1/configuration/authentication/auth-servers/auth-server/{}/local/users/user".format(auth_server)
    url = base + host + uri
    auth = (auth_token, '')
    headers = {
    "Content-Type" : "application/json"
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
    "password-cleartext" : user['password-cleartext'],
    "username" : user['username']
    }
    response = requests.post(url, auth=auth, headers=headers, data=json.dumps(data))
    if verbosity >= 1:
        print("Creating user " + username)
    if verbosity >= 2:
        print(response.status_code)
    if verbosity >= 3:
    	print(response.text)
    return response
