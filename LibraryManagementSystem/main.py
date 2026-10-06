from login import login
import books
import members


def librarian_menu():

    import loans

    while True:

        print("\n========== LIBRARIAN MENU ==========")
        print("1. View Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Register Member")
        print("6. Delete Member")
        print("7. View Members")
        print("8. View Borrowed Books")
        print("9. Logout")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            books.view_books()

        elif choice == 2:
            books.add_book()

        elif choice == 3:
            books.remove_book()

        elif choice == 4:
            books.search_book()

        elif choice == 5:
            members.register_member()

        elif choice == 6:
            members.delete_member()

        elif choice == 7:
            members.view_members()

        elif choice == 8:
            loans.view_all_loans()

        elif choice == 9:
            break

        else:
            print("Invalid choice.")

def student_menu(user):

    import loans

    while True:

        print("\n========== STUDENT MENU ==========")
        print("1. View Books")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View My Loans")
        print("6. Logout")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            books.view_books()

        elif choice == 2:
            books.search_book()

        elif choice == 3:
            loans.borrow_book(user.username)

        elif choice == 4:
            loans.return_book(user.username)

        elif choice == 5:
            loans.view_my_loans(user.username)

        elif choice == 6:
            break

        else:
            print("Invalid choice.")

def main():

    while True:

        print("\n===== LIBRARY RESOURCE MANAGEMENT SYSTEM =====")
        print("1. Login")
        print("2. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:

            user = login()

            if user:

                print(f"\nWelcome {user.name}")

                if user.__class__.__name__ == "Librarian":
                    librarian_menu()
                else:
                    student_menu()

        elif choice == 2:
            print("Thank you for using the Library System!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
