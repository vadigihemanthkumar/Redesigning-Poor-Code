from datetime import datetime

class Checkout:
    def __init__(self, user_id, isbn):
        # Initialize a new checkout record
        self.user_id = user_id
        self.isbn = isbn
        self.checkout_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.checkin_date = None

    def checkin(self):
        # Record the date when the book is checked in
        self.checkin_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        # Return a string representation of the checkout record
        return (f"User ID: {self.user_id}, ISBN: {self.isbn}, "
                f"Checkout Date: {self.checkout_date}, Checkin Date: {self.checkin_date}")


