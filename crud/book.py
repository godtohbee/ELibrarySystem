from uuid import UUID
from typing import List, Optional
from models.book import BookCreate, BookUpdate, BookResponse
from datetime import datetime


class BookCRUD:
    # In-memory storage for books
    books_db: List[BookResponse] = []

    @staticmethod
    def create_book(book: BookCreate) -> BookResponse:
        new_book = BookResponse(
            id = UUID,
            title = book.title,
            author = book.author,
            is_available = True,
            created = datetime.now(),
            updated = datetime.now(),
        )
        BookCRUD.books_db.append(new_book)
        return new_book

    @staticmethod
    def get_book_by_id(book_id: UUID) -> Optional[BookResponse]:
        return next((book for book in BookCRUD.books_db if book.id == book_id), None)

    @staticmethod
    def get_all_books() -> List[BookResponse]:
        return BookCRUD.books_db

    @staticmethod
    def update_book(book_id: UUID, book_update: BookUpdate) -> Optional[BookResponse]:
        book = BookCRUD.get_book_by_id(book_id)
        if book:
            if book_update.title:
                book.title = book_update.title
            if book_update.author:
                book.author = book_update.author
            if book_update.is_available is not None:
                book.is_available = book_update.is_available
            book_update.updated = datetime.now()
            return book
        return None

    @staticmethod
    def delete_book(book_id: UUID) -> bool:
        initial_count = len(BookCRUD.books_db)
        BookCRUD.books_db = [book for book in BookCRUD.books_db if book.id != book_id]
        return len(BookCRUD.books_db) < initial_count

    @staticmethod
    def mark_as_unavailable(book_id: UUID) -> Optional[BookResponse]:
        book = BookCRUD.get_book_by_id(book_id)
        if book:
            book.is_available = False
            book.updated = datetime.now()
            return book
        return None
    
    @staticmethod
    def update_book_availability(book_id: str, is_available: bool) -> Optional[BookResponse]:
    # updates the availability status of a book and returns the updated book if successful, None if book not found.
        book = BookCRUD.get_book_by_id(book_id)
        if book:
            book.is_available = is_available
            for id, available_book in enumerate(BookCRUD.books_db):
                if available_book.id == book_id:
                    BookCRUD.books_db[id].is_available = is_available
                    return book
            return book
        return None
