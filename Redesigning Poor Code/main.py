# main.py

from models import Library

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. Check-in Book")
    print("7. List Checkouts")
    print("8. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    library = Library()
    library.load_data()

    while True:
        choice = main_menu()
        try:
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                library.add_book(title, author, isbn)
                print("Book added.")
            elif choice == '2':
                library.list_books()
            elif choice == '3':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                library.add_user(name, user_id)
                print("User added.")
            elif choice == '4':
                library.list_users()
            elif choice == '5':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                library.checkout_book(user_id, isbn)
                print("Book checked out.")
            elif choice == '6':
                isbn = input("Enter ISBN of the book to check-in: ")
                library.check_in_book(isbn)
                print("Book checked in.")
            elif choice == '7':
                library.list_checkouts()
            elif choice == '8':
                library.save_data()
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
