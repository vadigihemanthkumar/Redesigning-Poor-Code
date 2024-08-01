from book import Book
from user import User
from check import Checkout
from storage import Storage
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        logging.info(f"Added book: {book}")

    def update_book(self, isbn, title=None, author=None):
        book = self.find_book_by_isbn(isbn)
        if not book:
            raise ValueError(f"No book with ISBN {isbn} found.")
        book.update(title, author)
        logging.info(f"Updated book: {book}")

    def delete_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if not book:
            raise ValueError(f"No book with ISBN {isbn} found.")
        self.books.remove(book)
        logging.info(f"Deleted book: {book}")

    def add_user(self, name, user_id):
        if self.find_user_by_id(user_id):
            raise ValueError(f"User with ID {user_id} already exists.")
        user = User(name, user_id)
        self.users.append(user)
        logging.info(f"Added user: {user}")

    def update_user(self, user_id, name=None):
        user = self.find_user_by_id(user_id)
        if not user:
            raise ValueError(f"No user with ID {user_id} found.")
        user.update(name)
        logging.info(f"Updated user: {user}")

    def delete_user(self, user_id):
        user = self.find_user_by_id(user_id)
        if not user:
            raise ValueError(f"No user with ID {user_id} found.")
        self.users.remove(user)
        logging.info(f"Deleted user: {user}")

    def find_book_by_isbn(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)

    def find_user_by_id(self, user_id):
        return next((user for user in self.users if user.user_id == user_id), None)

    def find_books_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_books_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def find_users_by_name(self, name):
        return [user for user in self.users if name.lower() in user.name.lower()]

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
        book.checkout_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        logging.info(f"Checked out book: {book}")

    def check_in_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book and book.is_checked_out:
            book.is_checked_out = False
            book.checkin_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for checkout in self.checkouts:
                if checkout.isbn == isbn and not checkout.checkin_date:
                    checkout.checkin()
                    break
            logging.info(f"Checked in book: {book}")
        else:
            raise ValueError(f"No book with ISBN {isbn} found or book is not checked out.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book)

    def list_users(self):
        if not self.users:
            print("No users in the library.")
        for user in self.users:
            print(user)

    def list_checkouts(self):
        if not self.checkouts:
            print("No checkouts.")
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

