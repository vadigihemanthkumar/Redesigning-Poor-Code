from datetime import datetime

class Checkout:
    def __init__(self, user_id, isbn, checkout_date=None, checkin_date=None):
        # Set up the basic information for a checkout record
        self.user_id = user_id
        self.isbn = isbn
        # Record the date and time when the book was checked out
        self.checkout_date = checkout_date if checkout_date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Record the date and time when the book was checked in
        self.checkin_date = checkin_date

    def checkin(self):
        # Record the date and time when the book was checked in
        self.checkin_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        # Create a string representation of the checkout record
        return (f"User ID: {self.user_id}, ISBN: {self.isbn}, "
                f"Checkout Date: {self.checkout_date}, Checkin Date: {self.checkin_date}")



