from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class BookBase(BaseModel):
    id: UUID
    title: str
    author: str
    copies: int
    is_available: bool = True
    created: datetime
    updated: datetime
    borrow_date: datetime
    return_date: datetime | None
    returned: bool = Field(default=False)


class Book(BookBase):
    pass
    
class BookCreate(BookBase):
    pass
    
class BookUpdate(BookBase):
    pass

class BookDelete(BookBase):
    pass