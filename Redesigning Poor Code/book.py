from datetime import datetime

class Book:
    def __init__(self, title, author, isbn, is_checked_out=False, added_date=None, 
                 checkout_date=None, checkin_date=None):
        # Initialize a new book with given details
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out
        self.added_date = added_date if added_date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.checkout_date = checkout_date
        self.checkin_date = checkin_date

    def __str__(self):
        # Return a string representation of the book details
        return (f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, "
                f"Available: {not self.is_checked_out}, Added: {self.added_date}, "
                f"Checkout Date: {self.checkout_date}, Checkin Date: {self.checkin_date}")

    def update(self, title=None, author=None):
        # Update book title or author if new values are provided
        if title:
            self.title = title
        if author:
            self.author = author
