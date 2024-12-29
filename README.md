This project is a simple e-library management system built with FastAPI.
It provides functionalities to manage books, users, borrowing and returning operations.
The system is designed to be efficient, modular, and easy to understand,
while leveraging error handling, validation, and RESTful APIs.


FEATURES
* User Management:
        i. create, update, delete, and retrieve user records.
        ii. deactivate users when necessary.

* Book Management:
        i. create, update, delete, retrieve book records
        ii. mark books as unavailable
        iii. list all available books in the system

* Borrow and Return Services:
        i. borrow books and record the borrowing date
        ii. return books and update the records
        iii. fetch all books borrowed or returned by users

* Error Handling:
        i. handles validation error with detailed error messages.
        ii. includes custom handlers for HTTP exceptions

* UUID Integration:
        i. ensures unique identification for users and books to improve database reliability


REQUIREMENTS
* python
* FastAPI
* Uvicorn
* Pydantic
* Pytest


API Endpoints
* User Endpoints
    Create User: POST/users/
    Get All Users: GET/users/
    Update User: PUT/users/{user_id}/
    Delete User: DELETE/users/{user_id}/
    Deactivate User: PATCH/users/{user_id}/deactivate/

* Book Endpoints
    Create Book: POST/books/
    Get All Books: GET/books/
    Get Available Books: GET/books/available/
    Update Book: PUT/books/{books_id}/
    Delete Book: DELETE/books/{book_id}/

* Borrow and Return Endpoints
    Borrow Book: POST/borrow/
    Return Book: POST/return/
    Get Borrowed Books: GET/borrowed/
    Mark Unavailable Books: PATCH/books/unavailable/{book_id}


PROJECT STRUCTURE
e_library_management_system/
    config/
        __init__.py             configuration initialization
        settings.py             manages application configuration
    crud/
        __init__.py             model initialization
        book_model.py           logic for book-related operations
        borrow_model.py         logic for borrow-related operations
        user_model.py           logic for user-related operations
    routers/
        __init__.py             route initialization
        books_routers.py        book-related endpoints
        borrow_routers.py       borrow-related endpoints
        user_routers.py         user-related endpoints 
    schemas/
        __init__.py             services initialization
        books.py                 book management model
        borrow.py               borrow management model
        users.py                 user management model
    tests/
        __init__.py             test initialization
        books.py                unit tests for book routes
        borrow.py               unit tests for borrow routes
        users.py                unit tests for user routes
    utils/
        __init.py__             utilities initialization
        error_handler.py        handles custom error responses
    __init__.py                 application initialization
    main.py                     entry point for the application
    README.md                   project documentation
    requirements.txt            list of dependencies


FUTURE IMPROVEMENTS
* Integration with a real database
* Add user authentication and authorization
* Appication logging and events
* Implement role-based access control 