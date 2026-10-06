# login.py

from members import Student, Librarian


def login():

    username = input("Username: ")
    password = input("Password: ")

    # Check password
    authenticated = False

    try:
        with open("password.txt", "r") as file:
            for line in file:
                user, pwd = line.strip().split("|")

                if username == user and password == pwd:
                    authenticated = True
                    break

    except FileNotFoundError:
        print("passwords.txt not found.")
        return None

    if not authenticated:
        print("Invalid username or password.")
        return None

    # Find role
    try:
        with open("members.txt", "r") as file:
            for line in file:

                user, name, role = line.strip().split("|")

                if username == user:

                    if role == "Librarian":
                        return Librarian(user, name)

                    else:
                        return Student(user, name)

    except FileNotFoundError:
        print("members.txt not found.")

    return None