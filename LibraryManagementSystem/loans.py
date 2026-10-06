# loans.py

from datetime import datetime, timedelta
import books


# Borrow Book
def borrow_book(username):

    all_books = books.load_books()

    isbn = input("Enter ISBN of the book to borrow: ")

    found = False

    for book in all_books:

        if book.isbn == isbn:

            found = True

            if book.status == "Borrowed":
                print("Book is already borrowed.")
                return

            book.status = "Borrowed"

            books.save_books(all_books)

            borrow_date = datetime.today().strftime("%Y-%m-%d")
            due_date = (datetime.today() + timedelta(days=14)).strftime("%Y-%m-%d")

            with open("loans.txt", "a") as file:
                file.write(f"{username}|{isbn}|{borrow_date}|{due_date}\n")

            print("Book borrowed successfully.")
            print("Due Date:", due_date)
            return

    if not found:
        print("Book not found.")


# Return Book
def return_book(username):

    isbn = input("Enter ISBN to return: ")

    try:
        with open("loans.txt", "r") as file:
            loans = file.readlines()

    except FileNotFoundError:
        print("No loan records found.")
        return

    updated_loans = []
    returned = False

    for loan in loans:

        user, loan_isbn, borrow_date, due_date = loan.strip().split("|")

        if user == username and loan_isbn == isbn:
            returned = True
        else:
            updated_loans.append(loan)

    if not returned:
        print("Loan record not found.")
        return

    with open("loans.txt", "w") as file:
        file.writelines(updated_loans)

    all_books = books.load_books()

    for book in all_books:
        if book.isbn == isbn:
            book.status = "Available"

    books.save_books(all_books)

    print("Book returned successfully.")


# View My Loans
def view_my_loans(username):

    try:
        with open("loans.txt", "r") as file:

            found = False

            print("\n========== MY LOANS ==========")

            for loan in file:

                user, isbn, borrow_date, due_date = loan.strip().split("|")

                if user == username:
                    found = True

                    print("----------------------------")
                    print("ISBN :", isbn)
                    print("Borrowed :", borrow_date)
                    print("Due :", due_date)

            if not found:
                print("No borrowed books.")

    except FileNotFoundError:
        print("No loan file found.")
        def view_all_loans():

    try:

        with open("loans.txt", "r") as file:

            print("\n========== BORROWED BOOKS ==========")

            found = False

            for line in file:

                found = True

                username, isbn, borrow, due = line.strip().split("|")

                print("----------------------")
                print("Student :", username)
                print("ISBN    :", isbn)
                print("Borrow  :", borrow)
                print("Due     :", due)

            if not found:
                print("No borrowed books.")

    except FileNotFoundError:
        print("Loan file not found.")