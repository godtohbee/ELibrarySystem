from fastapi import HTTPException
from pydantic import ValidationError
from typing import List
from models.book import BookCreate, BookUpdate, BookResponse
from crud.book import BookCRUD


class BookService:
    @staticmethod
    def create_book(data: BookCreate) -> BookResponse:
        try:
            book = BookCRUD.create_book(data)
            return book
        except ValidationError as not_created:
            raise HTTPException(status_code=400, detail=f"Invalid data: {not_created}")

    @staticmethod
    def get_all_books() -> List[BookResponse]:
        books = BookCRUD.get_all_books()
        if not books:
            raise HTTPException(status_code=404, detail="No books found")
        return books

    @staticmethod
    def get_book_by_id(book_id: str) -> BookResponse:
        book = BookCRUD.get_book_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    @staticmethod
    def update_book(book_id: str, data: BookUpdate) -> BookResponse:
        existing_book = BookCRUD.get_book_by_id(book_id)
        if not existing_book:
            raise HTTPException(status_code=404, detail="Book not found")
        updated_book = BookCRUD.update_book(book_id, data)
        return updated_book

    @staticmethod
    def delete_book(book_id: str) -> str:
        book = BookCRUD.get_book_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        BookCRUD.delete_book(book_id)
        return f"Book with ID {book_id} successfully deleted."
    
    @staticmethod
    def mark_book_unavailable(book_id: str) -> BookResponse:
        book = BookCRUD.update_book_availability(book_id, False)
        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )
        if not book.is_available:
            raise HTTPException(
                status_code=400, 
                detail="Book is already unavailable"
            )
        return BookResponse(**book.model_dump())