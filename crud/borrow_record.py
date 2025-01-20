from uuid import UUID
from typing import List, Optional
from models.borrow_record import BorrowRecordCreate, BorrowRecordResponse
from datetime import datetime
from crud.book import BookCRUD
from crud.user import UserCRUD


class BorrowRecordCRUD:
    # In-memory storage for borrow records
    borrow_records_db: List[BorrowRecordResponse] = []

    @staticmethod
    def borrow_book(borrow_record: BorrowRecordCreate) -> Optional[BorrowRecordResponse]:
        user = UserCRUD.get_user_by_id(borrow_record.user_id)
        book = BookCRUD.get_book_by_id(borrow_record.book_id)

        if not user or not user.is_active:
            return None  # User does not exist or is inactive

        if not book or not book.is_available:
            return None  # Book does not exist or is unavailable

        # Ensure user has not already borrowed this book
        for record in BorrowRecordCRUD.borrow_records_db:
            if record.user_id == borrow_record.user_id and record.book_id == borrow_record.book_id and not record.return_date:
                return None  # Book is already borrowed by this user
            
        # Check if user already has an active borrow record for this book
        active_borrow = next(
            (record for record in BorrowRecordCRUD.borrow_records_db 
            if record.user_id == borrow_record.user_id 
            and record.book_id == borrow_record.book_id 
            and not record.return_date),
            None
        )
        if active_borrow:
            return {
            "message": "User already has this book borrowed."
            }     

        new_record = BorrowRecordResponse(
            id = UUID,
            user_id = borrow_record.user_id,
            book_id = borrow_record.book_id,
            borrow_date = datetime.now(),
            return_date = None,
        )
        # Update database and book status
        BorrowRecordCRUD.borrow_records_db.append(new_record)
        BookCRUD.update_book(borrow_record.book_id, {"is_available": False})
        return BorrowRecordResponse(**new_record.model_dump())

    @staticmethod
    def create_borrow_record(borrow_record: BorrowRecordCreate) -> Optional[BorrowRecordResponse]:
        user = UserCRUD.get_user_by_id(borrow_record.user_id)
        book = BookCRUD.get_book_by_id(borrow_record.book_id)

        new_record = BorrowRecordResponse(
            id = UUID,
            user_id = borrow_record.user_id,
            book_id = borrow_record.book_id,
            borrow_date = datetime.now(),
            return_date = None,
        )
        BorrowRecordCRUD.borrow_records_db.append(new_record)
        return new_record
    
    @staticmethod
    def return_book(record_id: UUID) -> Optional[BorrowRecordResponse]:
        record = BorrowRecordCRUD.get_borrow_record_by_id(record_id)
        if not record or record.return_date:
            return None  # Record not found or book already returned
        # Mark the book as available again
        BookCRUD.update_book(record.book_id, {"is_available": True})
        record.return_date = datetime.now()
        return record

    @staticmethod
    def get_borrow_record_by_id(record_id: UUID) -> Optional[BorrowRecordResponse]:
        return next((record for record in BorrowRecordCRUD.borrow_records_db if record.id == record_id), None)

    @staticmethod
    def get_all_borrow_records() -> List[BorrowRecordResponse]:
        return BorrowRecordCRUD.borrow_records_db

    @staticmethod
    def get_records_by_user(user_id: UUID) -> List[BorrowRecordResponse]:
        return [record for record in BorrowRecordCRUD.borrow_records_db if record.user_id == user_id]
    
    @staticmethod
    def get_active_borrow_by_user_and_book(user_id: str, book_id: str) -> Optional[BorrowRecordResponse]:
        # check if a user has an active borrow record for a specific book.
        for record in BorrowRecordCRUD.borrow_records_db:
            if (record.user_id == user_id and 
                record.book_id == book_id and 
                record.return_date is None):
                return record
        return None
    
    @staticmethod
    def update_borrow_record(borrow_id: str, update_data: dict) -> Optional[BorrowRecordResponse]:
        # updates a borrow record with the provided data, returns updated record if found, None otherwise.
        for id, record in enumerate(BorrowRecordCRUD.borrow_records_db):
            if record.id == borrow_id:
                for key, value in update_data.items():
                    setattr(record, key, value)
                return BorrowRecordCRUD.borrow_records_db[id]
        return None
    
    @staticmethod
    def get_borrow_records_by_user(user_id: str) -> List[BorrowRecordResponse]:
        # retrieves all borrow records for a specific user and returns a list of borrow records.
        return [
            record for record in BorrowRecordCRUD.borrow_records_db 
            if record.user_id == user_id
        ]

    @staticmethod
    def delete_borrow_record(record_id: UUID) -> bool:
        # find the record to delete
        record_to_delete = BorrowRecordCRUD.get_borrow_record_by_id(record_id)
        if record_to_delete:
            # remove the record from the database
            BorrowRecordCRUD.borrow_records_db = [
                record for record in BorrowRecordCRUD.borrow_records_db if record.id != record_id
            ]
            return True
        return False