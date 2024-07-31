# user.py

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"
