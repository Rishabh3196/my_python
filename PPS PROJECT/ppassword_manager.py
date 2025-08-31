import os
import base64
import hashlib
import getpass

# Simple menu driven password manager

def list_passwords():
    files = os.listdir('passwords')
    print('Saved Passwords:')
    for filename in files:
        print(filename[:-4])

def get_master_password():
    while True:
        password = getpass.getpass('Enter your master password: ')
        if check_password(password):
            return password
        else:
            print('Incorrect password, please try again.')

def check_password(password):
    stored_password = None
    try:
        with open('passwords/.master', 'r') as f:
            stored_password = f.read()
    except FileNotFoundError:
        pass

    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)

    return pwdhash == stored_password

def save_password(site, password):
    try:
        os.mkdir('passwords')
    except FileExistsError:
        pass

    cipher_suite = Fernet(get_master_password().encode())
    cipher_text = cipher_suite.encrypt(password.encode())

    with open(f'passwords/{site}.txt', 'wb') as f:
        f.write(cipher_text)

def retrieve_password(site):
    try:
        with open(f'passwords/{site}.txt', 'rb') as f:
            cipher_text = f.read()
    except FileNotFoundError:
        print(f"Password for {site} does not exist.")
        return None

    cipher_suite = Fernet(get_master_password().encode())
    plain_text = cipher_suite.decrypt(cipher_text)

    return plain_text.decode()

def menu():
    print('=' * 20)
    print('Password Manager')
    print('=' * 20)
    while True:
        print('1. List Passwords')
        print('2. Save Password')
        print('3. Retrieve Password')
        print('4. Quit')
        choice = input('Enter your choice: ')

        if choice == '1':
            list_passwords()
        elif choice == '2':
            site = input('Enter the site name: ')
            password = getpass.getpass('Enter the password: ')
            save_password(site, password)
        elif choice == '3':
            site = input('Enter the site name: ')
            password = retrieve_password(site)
            if password:
                print('Password: ', password)
        elif choice == '4':
            break
        else:
            print('Invalid choice, please try again.')

menu()