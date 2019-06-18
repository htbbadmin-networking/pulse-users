from modules.helpers import *
from modules.pulselib import get_token
from modules.pulselib import create_vpn_user
from modules.pulselib import delete_vpn_user

def main():
    host = get_host()
    username = get_username()
    password = get_password()
    filename = get_filename()
    user_list = read_users(filename)
    auth_token = get_token(host, username, password)
    output = []
    for user in user_list:
        print(user)
        try:
            create_vpn_user(host, auth_token, user)
            # delete_vpn_user(host, auth_token, user)
            # print(user['username'] + ', ' + user['password-cleartext'])
        except Exception as e:
            print("Exception")
            print(e)
    return

if __name__ == '__main__':
    main()
