from modules.helpers import *
from modules.pulselib import get_token

def main():
    host = get_host()
    username = get_username()
    password = get_password()
    filename = get_filename()
    user_list = read_users(filename)
    '''
    auth_token = get_token(host, username, password)
    for user in user_list:
        try:
            create_vpn_user(host, auth_token, user)
        except:
            print("oops")
    '''
    return

if __name__ == '__main__':
    main()
