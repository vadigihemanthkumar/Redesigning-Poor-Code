# models.py

from book import Book
from user import User
from check import Checkout
from storage import Storage

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.checkouts = []

    def add_book(self, title, author, isbn):
        if self.find_book_by_isbn(isbn):
            raise ValueError(f"Book with ISBN {isbn} already exists.")
        book = Book(title, author, isbn)
        self.books.append(book)

    def add_user(self, name, user_id):
        if self.find_user_by_id(user_id):
            raise ValueError(f"User with ID {user_id} already exists.")
        user = User(name, user_id)
        self.users.append(user)

    def find_book_by_isbn(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)

    def find_user_by_id(self, user_id):
        return next((user for user in self.users if user.user_id == user_id), None)

    def checkout_book(self, user_id, isbn):
        book = self.find_book_by_isbn(isbn)
        user = self.find_user_by_id(user_id)

        if not book:
            raise ValueError(f"No book with ISBN {isbn} found.")
        if book.is_checked_out:
            raise ValueError(f"Book with ISBN {isbn} is already checked out.")
        if not user:
            raise ValueError(f"No user with ID {user_id} found.")

        book.is_checked_out = True
        self.checkouts.append(Checkout(user_id, isbn))

    def check_in_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book and book.is_checked_out:
            book.is_checked_out = False
            self.checkouts = [co for co in self.checkouts if co.isbn != isbn]

    def list_books(self):
        for book in self.books:
            print(book)

    def list_users(self):
        for user in self.users:
            print(user)

    def list_checkouts(self):
        for checkout in self.checkouts:
            print(checkout)

    def save_data(self):
        Storage.save_to_file([book.__dict__ for book in self.books], 'books.json')
        Storage.save_to_file([user.__dict__ for user in self.users], 'users.json')
        Storage.save_to_file([checkout.__dict__ for checkout in self.checkouts], 'checkouts.json')

    def load_data(self):
        self.books = [Book(**data) for data in Storage.load_from_file('books.json')]
        self.users = [User(**data) for data in Storage.load_from_file('users.json')]
        self.checkouts = [Checkout(**data) for data in Storage.load_from_file('checkouts.json')]
