from fastapi import APIRouter
from crud.borrow import borrow_crud
from uuid import UUID

borrow_router = APIRouter()
    
@borrow_router.get("/", summary="Get All Borrowed Books", status_code=200)
def get_all_borrowed_books():
    return {
        "message": "Borrowed books retrieved successfully",
        "data": borrow_crud.get_all_borrowed_books
    }            
            
@borrow_router.get("/{borrow_id}", summary="Get users who borrowed books", status_code=200)
def get_users_who_borrowed_books():
    return {
        "message": "Users who borrowed books",
        "data": list(borrow_crud.get_users_who_borrowed_books())
        }

@borrow_router.post("/{borrow_id}", summary="Borrow a book", status_code=200)
def borrow_book(borrow_id: UUID):
    return {
        "message": "Book borrowed successfully",
        "data": borrow_crud.borrow_book(borrow_id)
    }
 
@borrow_router.post("/{borrow_id}", summary="Books Returned", status_code=200)
def books_returned(borrow_id: UUID):
    return {
        "message": "Books returned successfully",
        "data": borrow_crud.books_returned()
    }