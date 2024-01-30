import sys

from cryptography.fernet import Fernet #encryption

pwd = input("Whats the master password ")

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
       

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.strip()
            user , passw = data.split("|")
            print("user: " + user + " passw: " + passw)

def add():
    name = input("Enter username: ")
    password = input("Enter new password: ")
    
    with open("password.txt", "a") as f:
        f.write(name + "|" + password + "\n")

while True:
    mode = input("add a password or view (view, add), press q to quit ").lower()

    if mode == "q":
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode ")

