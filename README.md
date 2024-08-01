# Library Management System

## Project Overview
This Library Management System is a Python-based application designed to efficiently manage books, users, and library operations. It demonstrates the use of object-oriented programming principles to create a modular and extensible system for library management.

## Features
- Manage books (add, update, delete, list, and search by various attributes like title, author, or ISBN)
- Manage users (add, update, delete, list, and search by attributes like name, user ID)
- Check out and check-in books
- Track book availability
- Simple logging of operations

## Project Structure
The project consists of the following main components:
- `main.py`: The entry point of the application, handling user interaction through a CLI.
- `library.py`: Contains the `Library` class, which manages the overall system.
- `book.py`: Defines the `Book` class representing individual books.
- `user.py`: Defines the `User` class representing library users.
- `storage.py`: Handles data persistence using JSON files.

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Clone the repository:
   ```
   git clone https://github.com/vadigihemanthkumar/Redesigning-Poor-Code.git
   ```
3. Navigate to the project directory:
   ```
   cd Redesigning-Poor-Code
   ```

## Usage
Run the application by executing the `main.py` file:
```
python main.py
```
Follow the on-screen prompts to interact with the Library Management System. You can perform operations such as adding books, registering users, checking out books, and more.

## Design Decisions and Architecture

### Object-Oriented Design
The system uses classes to represent key entities (Library, Book, User) and their relationships. This approach allows for easy extension and modification of the system.

### Data Persistence
JSON file storage is used for data persistence, allowing for easy reading and writing of data while maintaining a structured format.

### User Interface
A command-line interface (CLI) is implemented for user interaction, providing a simple and intuitive way to access the system's functionalities.

### Error Handling
The application includes error handling to manage common issues such as invalid inputs or file operations, ensuring a smooth user experience.

### Modularity and Scalability
The application is designed to be modular, with clear separation of concerns between different components. This architecture facilitates future expansions and modifications.

## Class Descriptions

### Library Class (`library.py`)
The central class managing all library operations.

Key methods:
- `add_book(book)`: Adds a new book to the library.
- `update_book(isbn, title, author)`: Updates book information.
- `delete_book(isbn)`: Removes a book from the library.
- `search_book(isbn)`: Finds a book by ISBN.
- `add_user(user)`: Adds a new user to the library.
- `check_out_book(isbn, user_id)`: Checks out a book to a user.
- `check_in_book(isbn, user_id)`: Returns a book to the library.

### Book Class (`book.py`)
Represents a book in the library.

Attributes:
- `title`: The title of the book.
- `author`: The author of the book.
- `isbn`: Unique identifier for the book.
- `available`: Boolean indicating if the book is available for checkout.

### User Class (`user.py`)
Represents a library user.

Attributes:
- `name`: The name of the user.
- `user_id`: Unique identifier for the user.
- `checked_out_books`: List of books currently checked out by the user.

### Storage Class (`storage.py`)
Handles data persistence using JSON files.

Key methods:
- `save_books(books)`: Saves the book data to a JSON file.
- `load_books()`: Loads book data from a JSON file.
- `save_users(users)`: Saves the user data to a JSON file.
- `load_users()`: Loads user data from a JSON file.

## Future Enhancements
- Implement due dates for books and late fee calculation
- Add support for different types of library items (e.g., magazines, DVDs)
- Integrate with a database for more efficient data management
- Develop a graphical user interface (GUI) for easier interaction

## Contributing
Contributions to improve the Library Management System are welcome. Please feel free to submit pull requests or open issues for any bugs or feature requests.

## License
This project is open-source and available under the MIT License.
