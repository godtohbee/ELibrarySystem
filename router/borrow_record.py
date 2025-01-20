from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from models.borrow_record import BorrowRecordCreate, BorrowRecordResponse, BorrowRecordUpdate
from crud.borrow_record import BorrowRecordCRUD

borrow_record_router = APIRouter(prefix="/borrow-records", tags=["Borrow Records"])


@borrow_record_router.post("/", response_model=BorrowRecordResponse, status_code=201)
def create_borrow_record(borrow_record: BorrowRecordCreate):
    new_record = BorrowRecordCRUD.create_borrow_record(borrow_record)
    if not new_record:
        raise HTTPException(status_code=400, detail="Failed to create borrow record.")
    return new_record


@borrow_record_router.get("/", response_model=List[BorrowRecordResponse], status_code=200)
def get_all_borrow_records():
    return BorrowRecordCRUD.get_all_borrow_records()


@borrow_record_router.get("/{record_id}", response_model=BorrowRecordResponse, status_code=200)
def get_borrow_record(record_id: UUID):
    record = BorrowRecordCRUD.get_borrow_record_by_id(record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Borrow record not found.")
    return record


@borrow_record_router.put("/{record_id}", response_model=BorrowRecordResponse, status_code=200)
def update_borrow_record(record_id: UUID, record_data: BorrowRecordUpdate):
    updated_record = BorrowRecordCRUD.update_borrow_record(record_id, **record_data.model_dump())
    if not updated_record:
        raise HTTPException(status_code=404, detail="Borrow record not found or update failed.")
    return updated_record


@borrow_record_router.delete("/{record_id}", status_code=204)
def delete_borrow_record(record_id: UUID):
    success = BorrowRecordCRUD.delete_borrow_record(record_id)
    if not success:
        raise HTTPException(status_code=404, detail="Borrow record not found.")
    return {"message": "Borrow record deleted successfully."}


@borrow_record_router.patch("/{record_id}/return", response_model=BorrowRecordResponse, status_code=200)
def mark_book_as_returned(record_id: UUID):
    record = BorrowRecordCRUD.return_book(record_id)
    if not record:
        raise HTTPException(
            status_code=400, 
            detail="Failed to mark the book as returned. Either the record doesn't exist or the book is already returned."
        )
    return record