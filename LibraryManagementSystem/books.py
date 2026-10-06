# books.py

class Book:
    def __init__(self, title, author, isbn, genre, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.status = status


# Load all books
def load_books():
    books = []

    try:
        with open("books.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 5:
                    books.append(Book(*data))

    except FileNotFoundError:
        pass

    return books


# Save all books
def save_books(books):
    with open("books.txt", "w") as file:
        for book in books:
            file.write(
                f"{book.title}|{book.author}|{book.isbn}|{book.genre}|{book.status}\n"
            )


# View Books
def view_books():

    books = load_books()

    if not books:
        print("\nNo books available.")
        return

    print("\n================ BOOK LIST ================")
    print("{:<25} {:<20} {:<12} {:<15} {:<10}".format(
        "Title", "Author", "ISBN", "Genre", "Status"))

    print("-"*90)

    for book in books:
        print("{:<25} {:<20} {:<12} {:<15} {:<10}".format(
            book.title,
            book.author,
            book.isbn,
            book.genre,
            book.status
        ))


# Add Book
def add_book():

    books = load_books()

    print("\nAdd New Book")

    title = input("Title : ")
    author = input("Author : ")
    isbn = input("ISBN : ")
    genre = input("Genre : ")

    # Check duplicate ISBN
    for book in books:
        if book.isbn == isbn:
            print("Book already exists.")
            return

    books.append(Book(title, author, isbn, genre, "Available"))

    save_books(books)

    print("Book added successfully.")


# Remove Book
def remove_book():

    books = load_books()

    isbn = input("Enter ISBN to remove: ")

    new_books = []

    found = False

    for book in books:

        if book.isbn == isbn:
            found = True

        else:
            new_books.append(book)

    if found:

        save_books(new_books)

        print("Book removed successfully.")

    else:

        print("Book not found.")


# Search Book
def search_book():

    books = load_books()

    keyword = input("Enter title, author, ISBN or genre: ").lower()

    found = False

    print("\nSearch Results\n")

    for book in books:

        if (
            keyword in book.title.lower()
            or keyword in book.author.lower()
            or keyword in book.genre.lower()
            or keyword in book.isbn.lower()
        ):

            found = True

            print("---------------------------------------")
            print("Title :", book.title)
            print("Author:", book.author)
            print("ISBN  :", book.isbn)
            print("Genre :", book.genre)
            print("Status:", book.status)

    if not found:
        print("No matching books found.")