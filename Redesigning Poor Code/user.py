from datetime import datetime

class User:
    def __init__(self, name, user_id):
        # Set up the basic information for a user
        self.name = name
        self.user_id = user_id
        # Record the date and time when the user was added
        self.added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        # Create a string representation of the user
        return f"Name: {self.name}, User ID: {self.user_id}, Added: {self.added_date}"

    def update(self, name=None):
        # Update the user's name if a new value is provided
        if name:
            self.name = name

