import os

MASTER_PASSWORD = input("What is the master password? ")

# Ensure the file exists
if not os.path.exists("passwords.txt"):
    with open("passwords.txt", "w") as f:
        pass

def view():
    """View saved passwords."""
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.strip())

def add():
    """Add a new password."""
    name = input('Account Name: ')
    pwd = input('Password: ')
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + pwd + '\n')

def delete():
    """Delete an account's saved password."""
    account = input("Enter account name to delete: ")
    lines = []
    with open('passwords.txt', 'r') as f:
        lines = f.readlines()
    with open('passwords.txt', 'w') as f:
        for line in lines:
            if not line.startswith(account + ' |'):
                f.write(line)

def update():
    """Update an existing password."""
    account = input("Enter account name to update: ")
    new_pwd = input("Enter new password: ")
    lines = []
    with open('passwords.txt', 'r') as f:
        lines = f.readlines()
    with open('passwords.txt', 'w') as f:
        for line in lines:
            if line.startswith(account + ' |'):
                f.write(account + ' | ' + new_pwd + '\n')
            else:
                f.write(line)

while True:
    mode = input("Would you like to add, view, update, or delete a password? (add, view, update, delete), press q to quit: ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "update":
        update()
    elif mode == "delete":
        delete()
    else:
        print("Invalid mode")
