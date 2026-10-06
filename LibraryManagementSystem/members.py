# members.py

class Person:
    def __init__(self, username, name):
        self.username = username
        self.name = name


class Student(Person):
    pass


class Librarian(Person):
    pass


# Load members
def load_members():
    members = []

    try:
        with open("members.txt", "r") as file:
            for line in file:
                members.append(line.strip().split("|"))
    except FileNotFoundError:
        pass

    return members


# View all members
def view_members():

    members = load_members()

    print("\n========== MEMBERS ==========")

    for username, name, role in members:
        print(f"Username : {username}")
        print(f"Name     : {name}")
        print(f"Role     : {role}")
        print("------------------------")


# Register Member
def register_member():

    username = input("Username: ")
    name = input("Full Name: ")
    password = input("Password: ")

    role = input("Role (Student/Librarian): ")

    members = load_members()

    for member in members:
        if member[0] == username:
            print("Username already exists.")
            return

    with open("members.txt", "a") as file:
        file.write(f"{username}|{name}|{role}\n")

    with open("passwords.txt", "a") as file:
        file.write(f"{username}|{password}\n")

    print("Member registered successfully.")


# Delete Member
def delete_member():

    username = input("Enter username to delete: ")

    members = load_members()

    updated_members = []

    found = False

    for member in members:

        if member[0] == username:
            found = True
        else:
            updated_members.append(member)

    if not found:
        print("Member not found.")
        return

    with open("members.txt", "w") as file:
        for member in updated_members:
            file.write("|".join(member) + "\n")

    # Update passwords
    with open("passwords.txt", "r") as file:
        passwords = file.readlines()

    with open("passwords.txt", "w") as file:
        for line in passwords:
            if not line.startswith(username + "|"):
                file.write(line)

    print("Member deleted successfully.")


# Update Profile
def update_profile(user):

    members = load_members()

    new_name = input("Enter new name: ")

    updated = []

    for member in members:

        if member[0] == user.username:
            updated.append([member[0], new_name, member[2]])
        else:
            updated.append(member)

    with open("members.txt", "w") as file:
        for member in updated:
            file.write("|".join(member) + "\n")

    print("Profile updated successfully.")