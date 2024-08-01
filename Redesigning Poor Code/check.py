from datetime import datetime

class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn
        self.checkout_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.checkin_date = None

    def checkin(self):
        self.checkin_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (f"User ID: {self.user_id}, ISBN: {self.isbn}, "
                f"Checkout Date: {self.checkout_date}, Checkin Date: {self.checkin_date}")

