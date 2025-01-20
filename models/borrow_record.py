from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


# Base schema for shared fields
class BorrowRecordBase(BaseModel):
    user_id: UUID
    book_id: UUID
    borrow_date: datetime
    return_date: datetime | None = None  # Optional for books not yet returned


# Schema for creating a borrowing record (input model)
class BorrowRecordCreate(BorrowRecordBase):
    pass  # Inherits fields from BorrowRecordBase


# Schema for updating a borrowing record (input model)
class BorrowRecordUpdate(BaseModel):
    return_date: datetime  # Used when marking a book as returned


# Schema for borrowing record response (output model)
class BorrowRecordResponse(BorrowRecordBase):
    id: UUID
