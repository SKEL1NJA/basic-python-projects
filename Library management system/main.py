class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

# --- The Base Class ---
class User:
    def __init__(self, name):
        self.name = name

# --- The Child Classes ---
class Member(User):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = set() # Using a Set to track unique books

    def borrow_book(self, book):
        """Adds a book to borrowed_books if it is available."""
        if book.is_available:
            book.is_available = False
            self.borrowed_books.add(book.title)

    def return_book(self, book):
        """Removes a book from borrowed_books."""
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
            book.is_available = True

class Librarian(User):
    def __init__(self, name):
        super().__init__(name)
        
    def add_book_to_library(self, library_list, title, author):
        """Creates a new Book object and adds it to the library's inventory."""
        new_book = Book(title, author)
        library_list.append(new_book)
        print(f"Librarian {self.name} added '{title}' to the library.")

# --- Testing the Library System ---

library_inventory = []

admin = Librarian("Sarah")
member = Member("Uday")

print("--- Adding Books ---")
admin.add_book_to_library(library_inventory, "1984", "George Orwell")
admin.add_book_to_library(library_inventory, "The Hobbit", "J.R.R. Tolkien")

print("\n--- Borrowing a Book ---")
book_to_borrow = library_inventory[0] 
member.borrow_book(book_to_borrow)

print(f"{member.name}'s borrowed books: {member.borrowed_books}")
print(f"Is '{book_to_borrow.title}' available? {book_to_borrow.is_available}")

print("\n--- Trying to borrow an unavailable book ---")
member.borrow_book(book_to_borrow) 
print(f"{member.name}'s borrowed books: {member.borrowed_books}")

print("\n--- Returning a Book ---")
member.return_book(book_to_borrow)
print(f"{member.name}'s borrowed books: {member.borrowed_books}")
print(f"Is '{book_to_borrow.title}' available? {book_to_borrow.is_available}")