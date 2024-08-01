from datetime import datetime

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}, Added: {self.added_date}"

    def update(self, name=None):
        if name:
            self.name = name

