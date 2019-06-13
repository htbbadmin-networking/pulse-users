from getpass import getpass

def get_username():
    username = input("Pulse API Username: ")
    return username

def get_password():
    password = getpass("Pulse API Password: ")
    return password

def get_filename():
    filename = input("User file: ")
    return filename

def get_host():
    host = input("Pulse Host: ")
    return host

def read_file(filename):
    contents = []
    with open(filename, "r") as file:
        for line in file:
            contents.append(line.split(','))
    return contents

def read_users(filename):
    users = []
    for user in read_file(filename):
        new_user = {}
        new_user['change-password-at-signin'] = 'true'
        new_user['console-access'] = 'false'
        new_user['enabled'] = 'true'
        new_user['fullname'] = user[0]
        new_user['one-time-use'] = 'false'
        new_user['password-cleartext'] = user[1].strip('\n')
        new_user['username'] = user[0]
        users.append(new_user)
    return users

