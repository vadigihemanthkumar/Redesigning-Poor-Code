from models import Library

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book            5. Add User              9. Checkout Book")
    print("2. Update Book         6. Update User           10. Check-in Book")
    print("3. Delete Book         7. Delete User           11. List Checkouts")
    print("4. List Books          8. List Users            12. Track Book Availability")
    print("13. Exit")
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
                isbn = input("Enter ISBN of the book to update: ")
                title = input("Enter new title (leave blank to keep current): ")
                author = input("Enter new author (leave blank to keep current): ")
                library.update_book(isbn, title, author)
                print("Book updated.")
            elif choice == '3':
                isbn = input("Enter ISBN of the book to delete: ")
                library.delete_book(isbn)
                print("Book deleted.")
            elif choice == '4':
                library.list_books()
            elif choice == '5':
                name = input("Enter name: ")
                user_id = input("Enter user ID: ")
                library.add_user(name, user_id)
                print("User added.")
            elif choice == '6':
                user_id = input("Enter user ID of the user to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                library.update_user(user_id, name)
                print("User updated.")
            elif choice == '7':
                user_id = input("Enter user ID of the user to delete: ")
                library.delete_user(user_id)
                print("User deleted.")
            elif choice == '8':
                library.list_users()
            elif choice == '9':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                library.checkout_book(user_id, isbn)
                print("Book checked out.")
            elif choice == '10':
                isbn = input("Enter ISBN of the book to check-in: ")
                library.check_in_book(isbn)
                print("Book checked in.")
            elif choice == '11':
                library.list_checkouts()
            elif choice == '12':
                print("Tracking Book Availability:")
                isbn = input("Enter ISBN of the book to track: ")
                book = library.find_book_by_isbn(isbn)
                if book:
                    status = "available" if not book.is_checked_out else f"checked out since {book.checkout_date}"
                    print(f"Book '{book.title}' is currently {status}.")
                else:
                    print(f"No book with ISBN {isbn} found.")
            elif choice == '13':
                library.save_data()
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()


