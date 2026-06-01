"""
Online Bookstore System
Manage a collection of books stored as (title, author, year, genre) tuples.

Features:
  - Display all books
  - Add a new book  (duplicate title check)
  - Remove a book   (by title)
  - Show unique genres
  - Update book details (title | author | year | genre)

Run:
    python Online_Book_Store_System.py
"""


def display_books(book_list):
    """Print every book in book_list in a readable format."""
    if not book_list:
        print("No books in the list")
    else:
        print("\nList of all books:")
        for title, author, year, genre in book_list:
            print(f"  Title: {title} | Author: {author} | Year: ({year}) | Genre: {genre}")


def add_book(book_list):
    """Prompt the user for book details and append to book_list if title is unique."""
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre of the book: ")

    # Collect existing titles for duplicate check
    existing_titles = {book[0] for book in book_list}
    if title in existing_titles:
        print(f'"{title}" already exists in the list.')
    else:
        book_list.append((title, author, year, genre))
        print(f'"{title}" has been added to the list.')

    display_books(book_list)


def remove_book(book_list):
    """Remove the first book whose title matches user input."""
    remove_title = input("Enter the title of the book you want to remove: ").strip()
    for book in book_list:
        if book[0] == remove_title:
            book_list.remove(book)
            print(f'"{remove_title}" has been removed.')
            break
    else:
        print(f'"{remove_title}" not found in the list.')

    display_books(book_list)


def show_unique_genres(book_list):
    """Display all unique genre values present in the bookstore."""
    unique_genres = {book[3] for book in book_list}
    print(f"Unique genres: {unique_genres}")


def update_book(book_list):
    """Update a specific field (title/author/year/genre) of an existing book."""
    title_to_update = input("Enter the title of the book to update: ").strip()

    for index, book in enumerate(book_list):
        if book[0] == title_to_update:
            book_up = list(book)
            field = input(
                "Enter the field to update (title, author, year, genre): "
            ).lower().strip()

            if field == "title":
                new_value = input("Enter the new title: ")
                book_up[0] = new_value
                print(f"Title updated to '{new_value}'.")

            elif field == "author":
                new_value = input("Enter the new author: ")
                book_up[1] = new_value
                print(f"Author updated to '{new_value}'.")

            elif field == "year":
                new_value = int(input("Enter the new year: "))
                book_up[2] = new_value
                print(f"Year updated to {new_value}.")

            elif field == "genre":
                new_value = input("Enter the new genre: ")
                book_up[3] = new_value
                print(f"Genre updated to '{new_value}'.")

            else:
                print("Invalid field. Choose from: title, author, year, genre.")

            # Replace the old tuple with the updated one
            book_list[index] = tuple(book_up)
            display_books(book_list)
            return

    print(f'"{title_to_update}" not found in the list.')


def main():
    # Pre-existing book collection
    BookStore = [
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction"),
        ("One Piece", "Eiichiro Oda", 1997, "Manga"),
        ("Naruto", "Masashi Kishimoto", 1999, "Manga"),
    ]

    # Display initial list
    display_books(BookStore)
    while True:
        print("\nOnline Bookstore System Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Show Unique Genres")
        print("4. Update Book Details")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(BookStore)
        elif choice == "2":
            remove_book(BookStore)
        elif choice == "3":
            show_unique_genres(BookStore)
        elif choice == "4":
            update_book(BookStore)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    display_books(BookStore)


if __name__ == "__main__":
    main()
