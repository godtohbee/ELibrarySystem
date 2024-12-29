from fastapi import HTTPException
from schemas.books import Book
from uuid import UUID
from datetime import datetime


books = {}
borrow_records = {}


books = [
    Book(id=1, name="book 1", author="author 1", copies=5),
    Book(id=2, name="book 2", author="author 2", copies=6),
    Book(id=3, name="book 3", author="author 3", copies=4),
    Book(id=4, name="book 4", author="author 4", copies=5),
    Book(id=5, name="book 5", author="author 5", copies=3),
]


borrow_records() = {
    "id": str,
    "user_id": str,
    "book_id": int,
    "borrow_date": datetime.now(),
    "return_date": None
}


class BookCrud():
    @staticmethod
    def get_available_books():
        # filter books that are available
        available_books = [book for book in books.values() if books.get("is_available", False)]    
        return {
        "message": "List of all available books in the system.",
        "available_books": available_books,
        }
        
        
    @staticmethod
    def get_book(book_id: UUID):
        # check if the book exists in the database
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return {
            "message": "Book retrieved succesfully",
            "book": book
        }
        
        
    @staticmethod
    def create_book(title: str, author: str, copies: int, description: str = None):
        # check if the book already exists
        for book in books():
            if book["title"] == title.lower() and book["author"] == author.lower():
                raise HTTPException(status_code=400, detail="Book already exists")
            # generate a unique book ID
        book_id = str(UUID())
        # create a new book entry
        books[book_id] = {
            "id": book_id,
            "title": title,
            "author": author,
            "copies": copies,
            "description": description,
            "is_borrowed": False
            }
        return {
            "message": "Book created successfully",
            "book": books[book_id]
        }
    
    
    @staticmethod
    def update_book(book_id: str, title: str = None, author: str = None, copies: int = None, description: str = None):
        # check if the book exists
        if book_id not in books:
            raise HTTPException(status_code=404, detail="Book not found")
        # update the book details
        if title is not None:
            books[book_id]["title"] = title
        if author is not None:
            books[book_id]["author"] = author
        if copies is not None:
            books[book_id]["copies"] = copies
        if description is not None:
            books[book_id]["description"] = description
        return {
            "message": "Book updated successfully",
            "book": books[book_id]
        }
        
        
    @staticmethod
    def delete_book(book_id: UUID):
        # check if the book exists
        if book_id not in books:
            raise HTTPException(status_code=404, detail="Book not found")
        # delete the book
        deleted_book = books.pop(book_id)
        return {
            "message": "Book deleted succesfully",
            "deleted_book": deleted_book
        }
        
        
    @staticmethod
    def mark_book_unavailable(book_id: UUID):
       # check if the book exists in the database
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        # update the availability status of the book
        if not book.get("is_available", True):
            raise HTTPException(status_code=400, detail="Book is already marked as unavailable")
        book["is_available"] = False
        return {
            "message": f"The book '{book['title']}' has been marked as unavailable.",
            "book": book,
        }

    
book_crud = BookCrud()