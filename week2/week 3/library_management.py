import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "books.json"

class Book:
    def __init__(self, title, author, is_issued=False):
        self.title = title
        self.author = author
        self.is_issued = is_issued

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued
        }

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        if FILE_PATH.exists():
            try:
                with open(FILE_PATH, "r", encoding="utf-8") as file:
                    data = json.load(file)

                self.books = [
                    Book(
                        item["title"],
                        item["author"],
                        item.get("is_issued", False)
                    )
                    for item in data
                ]

            except (json.JSONDecodeError, KeyError, TypeError):
                print("Error reading books.json. Starting with an empty list.")
                self.books = []

    def save_books(self):
        data = [book.to_dict() for book in self.books]

        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_book(self, title, author):
        if any(book.title.lower() == title.lower() for book in self.books):
            print("This book already exists.")
            return

        self.books.append(Book(title, author))
        self.save_books()
        print(f"'{title}' added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    print("Return the book before removing it.")
                    return

                self.books.remove(book)
                self.save_books()
                print(f"'{title}' removed successfully.")
                return

        print("Book not found.")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    print("This book is already issued.")
                else:
                    book.is_issued = True
                    self.save_books()
                    print(f"'{title}' issued successfully.")
                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_issued:
                    print("This book has not been issued.")
                else:
                    book.is_issued = False
                    self.save_books()
                    print(f"'{title}' returned successfully.")
                return

        print("Book not found.")

    def display_books(self):
        if not self.books:
         print("No books in the library.")
         return

        print("\n--- Library Books ---")
        for book in self.books:
               status = "Issued" if book.is_issued else "Available"
               print(f"{book.title} by {book.author} - {status}")

def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add book")
        print("2. Remove book")
        print("3. Issue book")
        print("4. Return book")
        print("5. Display books")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()

            if title and author:
                library.add_book(title, author)
            else:
                print("Title and author cannot be empty.")

        elif choice == "2":
            title = input("Enter book title to remove: ").strip()
            library.remove_book(title)

        elif choice == "3":
            title = input("Enter book title to issue: ").strip()
            library.issue_book(title)

        elif choice == "4":
            title = input("Enter book title to return: ").strip()
            library.return_book(title)

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            print("Library data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
