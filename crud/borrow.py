from fastapi import HTTPException
from uuid import UUID
from datetime import datetime
from crud.books import books
from crud.users import users

borrow_records = {}

borrow_records() = {
    "id": str,
    "user_id": str,
    "book_id": int,
    "borrow_date": datetime.now(),
    "return_date": None
}

class BorrowCrud:
    @staticmethod
    def get_all_borrowed_books():
        borrowed_books = []
        for record in borrow_records.values():
            if not record["return_date"]:
                book = books.get(record["book_id"])
                user = users.get(record["user_id"])
                return {
                    borrowed_books.append({
                    "book_id": record["book_id"],
                    "title": book["title"],
                    "author": book["author"],
                    "borrowed_by": {
                        "user_id": user["id"],
                        "name": user["name"],
                        "email": user["email"],
                    },
                    "borrow_date": record["borrow_date"]
                })
                }            
    
    @staticmethod
    def get_users_who_borrowed_books():
        users_borrowed_books = {}
        for record in borrow_records.values():
            user_id = record["user_id"]
            book_id = record["book_id"]
            book = books.get(book_id)
            user = users.get(user_id)
        if user_id not in users_borrowed_books:
            # create a new entry for the user
            users_borrowed_books[user_id] = {
                "user_id": user_id,
                "name": user["name"],
                "email": user["email"],
                "borrowed_books": []
            }
        # append book details to the user's borrowed books    
        users_borrowed_books[user_id]["borrow_records"].append({
            "book_id": book_id,
            "title": book["title"],
            "author": book["author"],
            "borrow_date": record["borrow_date"],
            "return_date": record["return_date"]
        })
        
        return {"users": list(users_borrowed_books.values())}
        
    @staticmethod
    def books_returned(book_id: str, user_id: str):
        # check if the book exists in the borrowed books database
        borrowed_record = next(
            (record for record in borrow_records.values() 
            if record["book_id"] == book_id and record["user_id"] == user_id),
            None
        )
        if not borrowed_record:
            raise HTTPException(
            status_code=404, detail="Borrowed book not found. Book might not have been borrowed."
        )
        # remove the book from the borrowed books database
        borrow_records.pop(borrowed_record("id"), None)
        # update the book status in the books database (mark book as available)
        if book_id in books:
            books[book_id]["is_available"] = True
        else:
            raise HTTPException(status_code=404, detail="Book not found in the database.")
        # return confirmation
        return {
            "message": "Book has been successfully returned",
            "book_id": book_id,
            "user_id": user_id,
        }
        
        
    @staticmethod
    def borrow_book(user_id: str, book_id: str):
            # check if the user exists
        if user_id not in users:
            raise HTTPException(status_code=404, detail="User not found")
            # check if the book exists
        if book_id not in books:
            raise HTTPException(status_code=404, detail="Book not found")
            # check if the book is already borrowed
        for record in borrow_records.values():
            if record["book_id"] == book_id and record["return_date"] is None:
                raise HTTPException(status_code=400, detail="Book is already borrowed")   
            # create a new borrow record
        borrow_id = str(UUID())
        borrow_date = datetime.timestamp()
        borrow_records[borrow_id] = {
            "id": borrow_id,
            "user_id": user_id,
            "book_id": book_id,
            "borrow_date": borrow_date,
            "return_date": None
        }
        return {
            "message": "Book borrowed successfully",
            "borrow_record": borrow_records[borrow_id]
        }
            
borrow_crud = BorrowCrud()