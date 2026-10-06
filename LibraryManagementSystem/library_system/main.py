"""
main.py
Library Resource Management System - entry point.

Run with:  python3 main.py

Demonstrates:
- Role-based access control (Librarian vs Student, via polymorphic menu_options())
- OOP + inheritance (member.py: User -> Librarian / Student)
- Exception handling throughout (see exceptions.py and the try/except blocks below)
- Modular design (separate modules for storage, auth, book/member models, and
  role-specific operations)
"""

import sys

import auth
import storage
import librarian_ops
import student_ops
import analytics
from member import Librarian, Student
from exceptions import LibraryError


def pause():
    input("\nPress Enter to continue...")


def print_header(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


# --------------------------------------------------------------- LOGIN -----

def do_login():
    print_header("LOGIN")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    try:
        user = auth.login(username, password)
        print(f"\nWelcome, {user.name} ({user.role})!")
        return user
    except LibraryError as e:
        print(f"Login failed: {e}")
        return None


# --------------------------------------------------------- LIBRARIAN UI ----

def librarian_menu(user: Librarian):
    while True:
        print_header(f"LIBRARIAN MENU - {user.name}")
        options = user.menu_options()
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                add_book_flow()
            elif choice == "2":
                remove_book_flow()
            elif choice == "3":
                update_member_flow()
            elif choice == "4":
                overdue_report_flow()
            elif choice == "5":
                analytics_flow()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")
        except LibraryError as e:
            print(f"Error: {e}")
        pause()


def add_book_flow():
    print_header("ADD BOOK")
    isbn = input("ISBN: ").strip()
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    genre = input("Genre: ").strip() or "General"
    book = librarian_ops.add_book(isbn, title, author, genre)
    print(f"Added: {book}")


def remove_book_flow():
    print_header("REMOVE BOOK")
    isbn = input("ISBN to remove: ").strip()
    removed = librarian_ops.remove_book(isbn)
    print(f"Removed: {removed}")


def update_member_flow():
    print_header("UPDATE MEMBER RECORD")
    member_id = input("Member ID: ").strip()
    name = input("New name (blank to skip): ").strip()
    email = input("New email (blank to skip): ").strip()
    role = input("New role Librarian/Student (blank to skip): ").strip()
    member = librarian_ops.update_member(
        member_id, name or None, email or None, role or None
    )
    print(f"Updated: {member}")


def overdue_report_flow():
    print_header("OVERDUE REPORT")
    report = librarian_ops.generate_overdue_report()
    if not report:
        print("No overdue loans. ")
        return
    for entry in report:
        print(f"- {entry['member_name']} ({entry['member_id']}) has '{entry['book_title']}' "
              f"overdue since {entry['due_date']} ({entry['days_overdue']} days overdue)")


def analytics_flow():
    print_header("BORROWING ANALYTICS")
    try:
        genre_path = analytics.plot_popular_genres(
            "/home/claude/library_system/genre_popularity.png"
        )
        trend_path = analytics.plot_borrowing_trend(
            "/home/claude/library_system/borrowing_trend.png"
        )
        print(f"Saved genre popularity chart to: {genre_path}")
        print(f"Saved borrowing trend chart to: {trend_path}")
    except ValueError as e:
        print(f"Could not generate charts: {e}")

    print("\nMost Popular Genres:")
    for genre, count in analytics.most_popular_genres().most_common():
        print(f"  {genre}: {count} loan(s)")

    print("\nOverdue Alerts (members with frequent overdue books):")
    alerts = analytics.overdue_alerts()
    if not alerts:
        print("  None.")
    for name, member_id, count in alerts:
        print(f"  ALERT: {name} ({member_id}) has {count} overdue books.")


# ----------------------------------------------------------- STUDENT UI ----

def student_menu(user: Student):
    while True:
        print_header(f"STUDENT MENU - {user.name}")
        options = user.menu_options()
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                search_book_flow()
            elif choice == "2":
                view_loans_flow(user)
            elif choice == "3":
                update_profile_flow(user)
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")
        except LibraryError as e:
            print(f"Error: {e}")
        pause()


def search_book_flow():
    print_header("SEARCH FOR A BOOK")
    keyword = input("Enter title/author/genre keyword: ").strip()
    results = student_ops.search_books(keyword)
    if not results:
        print("No matching books found.")
    for book in results:
        print(f"  {book}")

    borrow_choice = input("\nBorrow one of these? Enter ISBN or leave blank: ").strip()
    if borrow_choice:
        member_id = input("Confirm your Member ID: ").strip()
        loan = student_ops.borrow_book(member_id, borrow_choice)
        print(f"Borrowed! Due back by {loan['due_date']}.")


def view_loans_flow(user: Student):
    print_header("MY CURRENT LOANS")
    loans = student_ops.view_own_loans(user.member_id)
    active = [l for l in loans if l["return_date"] == "None"]
    if not active:
        print("You have no active loans.")
    for loan in active:
        print(f"  ISBN {loan['isbn']} - borrowed {loan['borrow_date']}, due {loan['due_date']}")


def update_profile_flow(user: Student):
    print_header("UPDATE MY PROFILE")
    name = input("New name (blank to skip): ").strip()
    email = input("New email (blank to skip): ").strip()
    updated = student_ops.update_own_profile(user.member_id, name or None, email or None)
    print(f"Profile updated: {updated}")


# --------------------------------------------------------------- ENTRY -----

def main():
    print_header("LIBRARY RESOURCE MANAGEMENT SYSTEM")
    print("Type 'quit' at the username prompt at any time to exit.\n")

    while True:
        user = do_login()
        if user is None:
            again = input("Try again? (y/n): ").strip().lower()
            if again != "y":
                print("Goodbye.")
                sys.exit(0)
            continue

        if isinstance(user, Librarian):
            librarian_menu(user)
        elif isinstance(user, Student):
            student_menu(user)

        again = input("\nLog in as someone else? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
