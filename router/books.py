from fastapi import APIRouter
from typing import Optional
from schemas.books import BookCreate, BookUpdate, Book
from uuid import UUID
from crud.books import book_crud

book_router = APIRouter()


@book_router.get("/", summary="Get all available books", status_code=200)
def get_available_books():
    return {
        "message": "List of all available books in the system.",
        "data": book_crud.get_available_books()
    }


@book_router.get("/{book_id}", summary="Get book details", status_code=200)
def get_book(book_id: int):
    return {
        "message": "Book retrieved succesfully",
        "data": book_crud.get_book(book_id)
    }


@book_router.post("/", summary="Create a new book", status_code=201)
def create_book(payload: BookCreate):
    new_book = book_crud.create_book(payload)
    return {
        "message": "Book created successfully",
        "data": new_book
    }
    
    
@book_router.put("/{book_id}", summary="Update a book", status_code=200)
def update_book(book_id: str, payload: BookUpdate):
    book: Optional[Book] = book_crud.get_available_books(book_id)
    update_book[Book] = book_crud.update_book(book, payload)
    return {
        "message": "Book updated successfully",
        "data": "updated_book"
    }
    
    
@book_router.delete("/{book_id}", summary="Delete a book", status_code=200)
def delete_book(book_id: UUID):
    return book_crud.delete_book(book_id)
    

@book_router.patch("/books/{book_id}/unavailable", summary="Mark a book as unavailable", status_code=200)
def mark_book_unavailable(book_id: UUID):
    return book_crud.mark_book_unavailable(book_id)