
import json

class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open('books.json', 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        genre = input("Enter genre: ")
        self.books.append({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre
        })
        self.save_books()
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter book title to remove: ")
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                self.save_books()
                print("Book removed successfully!")
                return
        print("Book not found")

    def update_book(self):
        title = input("Enter a book title to update: ")
        for book in self.books:
            if book["title"] == title:
                book["title"] = input("Enter a new title: ")
                book["author"] = input("Enter a new author: ")
                book["year"] = input("Enter a new year: ")
                book["genre"] = input("Enter a new genre: ")
                self.save_books()
                print("Book updated successfully!")
                return
        print("Book not found")

    def display_book(self):
        title = input("Enter a book title to display: ")
        for book in self.books:
            if book["title"] == title:
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Year: {book['year']}")
                print(f"Genre: {book['genre']}")
                return
        print("Book not found")

    def list_books(self):
        if not self.books:
            print("No books found")
        else:
            print("List of books:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")

    def search_book(self):
        query = input("Enter your search query: ")
        result = [book for book in self.books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
        if result:
            print("Search results:")
            for book in result:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")
        else:
            print("No results found")


def main():
    library = Library()
    while True:
        print("\n📚 Welcome To Library System Manager")
        print("1. Add book")
        print("2. Remove book")
        print("3. List books")
        print("4. Update book")
        print("5. Display book")
        print("6. Search book")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.remove_book()
        elif choice == "3":
            library.list_books()
        elif choice == "4":
            library.update_book()
        elif choice == "5":
            library.display_book()
        elif choice == "6":
            library.search_book()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")


if __name__ == "__main__":
    main()
