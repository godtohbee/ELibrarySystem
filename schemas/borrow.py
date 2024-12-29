from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class BorrowBase(BaseModel):
    user_id: int
    book_id: int
    
class Borrow(BorrowBase):
    id: UUID
    borrow_date: datetime
    return_date: datetime | None
    returned: bool = Field(default=False)
    