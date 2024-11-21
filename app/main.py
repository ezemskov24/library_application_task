from typing import Dict, Callable

from models import Library

def get_data_for_new_book(library: Library) -> None:
    """
    Prompts the user for book details and adds a new book to the library.

    Args:
        library (Library): The library instance to which the book will be added.
    """
    title = input('Enter the book title: ')
    author = input('Enter the author of the book: ')
    try:
        year = int(input('Enter the year the book was written: '))
        library.add_book(title=title, author=author, year=year)
    except ValueError:
        print('Invalid year. Please enter a numeric value.\n')

def delete_book_by_id(library: Library) -> None:
    """
    Prompts the user for a book ID and deletes the corresponding book.

    Args:
        library (Library): The library instance from which the book will be deleted.
    """
    try:
        book_id = int(input('Enter the ID of the book you want to delete: '))
        library.delete_book(book_id=book_id)
    except ValueError:
        print('Invalid ID. Please enter a numeric value.\n')


def find_books_in_library(library: Library) -> None:
    """
    Allows the user to search for books in the library by a specific field and value.

    Args:
        library (Library): The library instance to search in.
    """
    valid_fields = {"title", "author", "year"}  # Допустимые поля для поиска
    field = input("Search by (title/author/year): ").lower()

    if field not in valid_fields:
        print(f"Invalid field '{field}'. Please choose from {', '.join(valid_fields)}.\n")
        return

    value = input(f"Enter {field}: ")
    if field == "year":
        try:
            value = int(value)
        except ValueError:
            print("Year must be a number. Please try again.\n")
            return

    found_books = library.find_books(**{field: value})
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("No books found matching your criteria.\n")


def display_all_books(library: Library) -> None:
    """
    Displays all books in the library.

    Args:
        library (Library): The library instance containing the books.
    """
    books = library.get_all_books()
    if books:
        for book in books:
            print(book)
    else:
        print('No books in the library yet.\n')


def change_book_status(library: Library) -> None:
    """
    Prompts the user to change the status of a book.

    Args:
        library (Library): The library instance containing the book.
    """
    try:
        book_id = int(input('Enter the ID of the book you want to change status: '))
        print('1: Book in stock\n'
              '2: The book has been issued')
        user_status = int(input('Choose the new status (1/2): '))
        if user_status == 1:
            book_status = True
        elif user_status == 2:
            book_status = False
        else:
            print('Invalid choice. Please enter 1 or 2.\n')
            return
        library.change_book_status(book_id=book_id, new_status=book_status)
    except ValueError:
        print('Invalid input. Please enter numeric values for ID and status.\n')

def exit_program(_: Library) -> None:
    """
    Exits the program.

    Args:
        _: Placeholder for compatibility with action functions. Not used.
    """
    print('Have a good day!')
    exit()

def main() -> None:
    """
    Main function to run the library management system.
    """
    library = Library()

    actions: Dict[int, Callable[[Library], None]] = {
        1: get_data_for_new_book,
        2: delete_book_by_id,
        3: find_books_in_library,
        4: display_all_books,
        5: change_book_status,
        6: exit_program,
    }

    while True:
        try:
            answer = int(input('Choose a command by number:\n'
                               '1: Add a book\n'
                               '2: Delete a book\n'
                               '3: Find a book\n'
                               '4: Get all books\n'
                               '5: Change book status\n'
                               '6: Exit\n'
                               'Command: '))
            action = actions.get(answer)
            if action:
                action(library)
            else:
                print('Invalid command. Please choose a valid option.\n')
        except ValueError:
            print('Invalid input. Please enter a number corresponding to a command.\n')


if __name__ == '__main__':
    main()
