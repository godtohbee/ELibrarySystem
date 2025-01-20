from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from models.book import BookCreate, BookResponse, BookUpdate
from crud.book import BookCRUD

book_router = APIRouter(prefix="/books", tags=["Books"])


@book_router.post("/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate):
    new_book = BookCRUD.create_book(book)
    if not new_book:
        raise HTTPException(status_code=400, detail="Book creation failed.")
    return new_book


@book_router.get("/", response_model=List[BookResponse], status_code=200)
def get_all_books():
    return BookCRUD.get_all_books()


@book_router.get("/{book_id}", response_model=BookResponse, status_code=200)
def get_book(book_id: UUID):
    book = BookCRUD.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


@book_router.put("/{book_id}", response_model=BookResponse, status_code=200)
def update_book(book_id: UUID, book_data: BookUpdate):
    updated_book = BookCRUD.update_book(book_id, **book_data.model_dump())
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found or update failed.")
    return updated_book


@book_router.delete("/{book_id}", status_code=204)
def delete_book(book_id: UUID):
    success = BookCRUD.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found.")
    return {"message": "Book deleted successfully."}


@book_router.patch("/{book_id}/unavailable", response_model=BookResponse, status_code=200)
def mark_book_unavailable(book_id: UUID):
    book = BookCRUD.mark_as_unavailable(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found or already unavailable.")
    return book
