# LibraryManager.py

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year_of_publication):
        """Add a book to the library."""
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year_of_publication': year_of_publication
        }
        print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed successfully.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def retrieve_book(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        book = self.books.get(isbn)
        if book:
            return book
        else:
            print(f"Book with ISBN {isbn} not found.")
            return None

    def search_books(self, title=None, author=None):
        """Search for books by title or author."""
        results = []
        for book in self.books.values():
            if title and title.lower() in book['title'].lower():
                results.append(book)
            elif author and author.lower() in book['author'].lower():
                results.append(book)
        return results

    def list_books(self):
        """List all books currently in the library."""
        return self.books

    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year_of_publication=None):
        """Update the details of an existing book."""
        book = self.books.get(isbn)
        if book:
            if title is not None:
                book['title'] = title
            if author is not None:
                book['author'] = author
            if publisher is not None:
                book['publisher'] = publisher
            if volume is not None:
                book['volume'] = volume
            if year_of_publication is not None:
                book['year_of_publication'] = year_of_publication
            print(f"Book with ISBN {isbn} updated successfully.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def check_availability(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books

# Example usage
if __name__ == "__main__":
    library = LibraryManager()

    # Add some books
    library.add_book('978-0134685991', 'Operating Systems: Three Easy Pieces', 'Remzi H. Arpaci-Dusseau', 'Arpaci-Dusseau', '3rd', 2020)
    library.add_book('978-0262046235', 'Introduction to Algorithms', 'Thomas H. Cormen', 'MIT Press', '4th', 2021)
    library.add_book('978-0134670959', 'Machine Learning Yearning', 'Andrew Ng', 'Self-published', '1st', 2022)

    # List all books
    print("All Books:", library.list_books())

    # Retrieve a book
    print("Book Details:", library.retrieve_book('978-0134685991'))

    # Search for books by title
    print("Search Results (title 'Operating Systems'):", library.search_books(title='Operating Systems'))

    # Search for books by author
    print("Search Results (author 'Andrew Ng'):", library.search_books(author='Andrew Ng'))

    # Update a book
    library.update_book('978-0134685991', title='Operating Systems: Three Easy Pieces - Updated Edition')

    # Check availability
    print("Book availability (ISBN '978-0134685991'):", library.check_availability('978-0134685991'))

    # Remove a book
    library.remove_book('978-0134670959')
    print("All Books after removal:", library.list_books())
