from fastapi import HTTPException
from typing import List
from datetime import datetime
from models.borrow_record import BorrowRecordCreate, BorrowRecordResponse
from crud.borrow_record import BorrowRecordCRUD
from crud.user import UserCRUD
from crud.book import BookCRUD
from uuid import UUID


class BorrowRecordService:
    @staticmethod
    def borrow_book(data: BorrowRecordCreate) -> BorrowRecordResponse:
        user = UserCRUD.get_user_by_id(data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.is_active:
            raise HTTPException(status_code=400, detail="User is not active")
        
        book = BookCRUD.get_book_by_id(data.book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        if not book.is_available:
            raise HTTPException(status_code=400, detail="Book is not available for borrowing")

        existing_borrow = BorrowRecordCRUD.get_active_borrow_by_user_and_book(data.user_id, data.book_id)
        if existing_borrow:
            raise HTTPException(status_code=400, detail="User has already borrowed this book")
    
                # Create new borrow record
        new_record = BorrowRecordCreate(
            id = UUID,
            user_id = data.user_id,
            book_id = data.book_id,
            borrow_date = datetime.now(),
            return_date = None
        )
            # Save to database
        BorrowRecordCRUD.borrow_records_db.append(new_record)
        BookCRUD.update_book(BorrowRecordResponse.book_id, {"is_available": False})
        return BorrowRecordResponse(**new_record.model_dump())

    @staticmethod
    def create_borrow_record(borrow_record_create) -> List[BorrowRecordResponse]:
        new_record = BorrowRecordCRUD.create_borrow_record(borrow_record_create)
        return new_record

    @staticmethod
    def return_book(borrow_id: str) -> BorrowRecordResponse:
        borrow_record = BorrowRecordCRUD.get_borrow_record_by_id(borrow_id)
        if not borrow_record:
            raise HTTPException(status_code=404, detail="Borrow record not found")
        if borrow_record.return_date:
            raise HTTPException(status_code=400, detail="Book is already returned")
        
        # Proceed with returning the book
        BookCRUD.update_book(borrow_record.book_id, {"is_available": True})
        updated_borrow_record = BorrowRecordCRUD.update_borrow_record(
            borrow_id, {"return_date": datetime.utcnow()}
        )
        return BorrowRecordResponse(**updated_borrow_record.model_dump())

    @staticmethod
    def get_all_borrow_records() -> List[BorrowRecordResponse]:
        borrow_records = BorrowRecordCRUD.get_all_borrow_records()
        if not borrow_records:
            raise HTTPException(status_code=404, detail="No borrow records found")
        return borrow_records
    
    @staticmethod
    def get_borrow_records_by_user(user_id: str) -> List[BorrowRecordResponse]:
    # retrieves all borrow records for a specific user and raises HTTPException if user not found or no records exist.
        user = UserCRUD.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, 
                                detail="User not found")

        borrow_records = BorrowRecordCRUD.get_borrow_records_by_user(user_id)
        if not borrow_records:
            raise HTTPException(status_code=404, 
                                detail="No borrow records found for this user")

        return [BorrowRecordResponse(**record.model_dump()) for record in borrow_records]
    
    @staticmethod
    def delete_borrow_record(record_id: UUID) -> bool:
        return BorrowRecordCRUD.delete_borrow_record(record_id)
